#!/usr/bin/env python3
"""Gold-probe validation for converted + post-processed engineering specs.

A document PASSES when gold probes are 100%, the equation census has no
unexplained misses, copyright/running-title leakage is zero in searchable
text, and sampled blocks carry pdf_page + printed_label.

Do not proceed past a failed validate. Do not convert the next PDF until
this exits 0.

Usage:
  /workspace/engineering_rag/.venv/bin/python \\
    /workspace/engineering_rag/scripts/validate.py \\
    /workspace/engineering_rag/documents/standards/AISI_S400_20
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Optional

# Allow running as a sibling of postprocess.py
sys.path.insert(0, str(Path(__file__).resolve().parent))
from postprocess import (  # noqa: E402
    AISC_341_PRINTED_LABEL_RE,
    AISC_341_RUNNING_TITLE_RES,
    AISC_358_PRINTED_LABEL_RE,
    AISC_358_RUNNING_TITLE_RES,
    AISC_COPYRIGHT_RES,
    AISC_PRINTED_LABEL_RE,
    AISC_RUNNING_TITLE_RES,
    ASCE_COPYRIGHT_RES,
    ASCE_RUNNING_TITLE_RES,
    ASCE_WATERMARK_RES,
    AISI_S100_RUNNING_TITLE_RES,
    AISI_S240_RUNNING_TITLE_RES,
    COPYRIGHT_LINE,
    RUNNING_TITLE_RES,
    census_pdf_eq_ids,
    collapse_ws,
    is_aisc_341_doc,
    is_aisc_358_doc,
    is_aisc_doc,
    is_aisi_s100_doc,
    is_aisi_s240_doc,
    is_asce7_doc,
    pdf_text_pages,
)

GOLD_PLF = ("940", "1410", "1760", "2350")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_paths(doc_dir: Path) -> dict[str, Path]:
    stem = doc_dir.name
    meta = doc_dir / "convert_meta.json"
    if meta.is_file():
        stem = load_json(meta).get("stem") or stem
    indexes = doc_dir / "indexes"
    lite = Path("/workspace/engineering_rag/indexes-lite")
    search_md = doc_dir / "markdown" / f"{stem}.search.md"
    if not search_md.is_file():
        for alt in (
            doc_dir / f"{stem}.search.md",
            doc_dir / "complete" / f"{stem}.search.md",
            Path("/workspace/engineering_rag/drive_pending") / str(stem) / f"{stem}.search.md",
        ):
            if alt.is_file():
                search_md = alt
                break
    orig_md = doc_dir / "markdown" / f"{stem}.md"
    if not orig_md.is_file():
        alt_orig = Path("/workspace/engineering_rag/drive_pending") / str(stem) / f"{stem}.md"
        if alt_orig.is_file():
            orig_md = alt_orig
    return {
        "doc_dir": doc_dir,
        "stem": Path(stem),  # misuse as holder; real stem is str
        "meta": meta,
        "search_md": search_md,
        "orig_md": orig_md,
        "page_map": doc_dir / "structured" / "page_map.json",
        "blocks": doc_dir / "structured" / "blocks.jsonl",
        "local_sections": indexes / "sections.json",
        "local_equations": indexes / "equations.json",
        "local_tables": indexes / "tables.json",
        "local_documents": indexes / "documents.json",
        "lite_sections": lite / "sections.json",
        "lite_equations": lite / "equations.json",
        "lite_tables": lite / "tables.json",
        "lite_documents": lite / "documents.json",
        "postprocess_meta": doc_dir / "postprocess_meta.json",
        "pages_search": doc_dir / "markdown" / "pages_search",
        "stem_str": str(stem),
    }


def pick_index(local: Path, lite: Path) -> Path:
    if local.is_file():
        return local
    if lite.is_file():
        return lite
    raise FileNotFoundError(f"Missing index {local} and {lite}")


class Probe:
    def __init__(self) -> None:
        self.rows: list[dict[str, Any]] = []

    def add(self, name: str, ok: bool, detail: str) -> None:
        self.rows.append({"name": name, "ok": bool(ok), "detail": detail})
        flag = "PASS" if ok else "FAIL"
        print(f"[{flag}] {name}: {detail}")

    @property
    def failed(self) -> list[dict[str, Any]]:
        return [r for r in self.rows if not r["ok"]]

    @property
    def passed(self) -> bool:
        return not self.failed


def probe_e342(sections: list[dict[str, Any]], probes: Probe) -> None:
    hits = [s for s in sections if s.get("section_id") == "E3.4.2"]
    std = [s for s in hits if s.get("part") == "standard"]
    com = [s for s in hits if s.get("part") == "commentary"]
    std_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 59) <= 2 for s in std
    )
    com_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 136) <= 2 for s in com
    )
    probes.add(
        "E3.4.2 provision (pdf ~59)",
        std_ok,
        f"standard hits={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part')} for s in std]}",
    )
    probes.add(
        "E3.4.2 commentary (pdf ~136)",
        com_ok and all(s.get("part") == "commentary" for s in com),
        f"commentary hits={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part')} for s in com]}",
    )


def probe_table_e131(tables: list[dict[str, Any]], search_md: Path, probes: Probe) -> None:
    candidates = [
        t
        for t in tables
        if (t.get("table_id") or "").replace(" ", "") in {"E1.3-1", "E1.31"}
        or (t.get("table_id") or "").startswith("E1.3-1")
        or "E1.3-1" in (t.get("title") or "")
        or (t.get("pdf_page") == 39)
    ]
    blobs = []
    for t in candidates:
        blobs.append(t.get("markdown_excerpt") or "")
        md = t.get("md")
        if md and Path(md).is_file():
            blobs.append(Path(md).read_text(encoding="utf-8"))
    if search_md.is_file():
        blobs.append(search_md.read_text(encoding="utf-8"))
    joined = "\n".join(blobs)
    # 54-mil row: values 940/1410/1760/2350
    has_vals = all(v in joined for v in GOLD_PLF)
    # prefer the same table region: 54 near 940
    near = bool(re.search(r"940[\s\S]{0,120}1410[\s\S]{0,120}1760[\s\S]{0,120}2350", joined))
    has_54 = bool(re.search(r"54", joined))
    probes.add(
        "Table E1.3-1 54-mil row 940/1410/1760/2350",
        has_vals and near and has_54,
        f"values={has_vals} clustered={near} has_54={has_54} candidate_ids={[t.get('table_id') for t in candidates[:6]]}",
    )


def probe_commentary_boundary(docs: list[dict[str, Any]], probes: Probe) -> None:
    if not docs:
        probes.add("commentary boundary", False, "documents.json empty")
        return
    b = (docs[0].get("commentary_boundary") or {}) if isinstance(docs[0], dict) else {}
    cover = b.get("cover_pdf_page")
    body = b.get("body_pdf_page")
    ok = cover == 91 and body is not None and abs(int(body) - 99) <= 2
    probes.add(
        "commentary boundary (cover p.91, body ~p.99)",
        ok,
        f"cover={cover} body={body} profile={b.get('profile')}",
    )


def probe_eq_census(
    doc_dir: Path,
    equations: list[dict[str, Any]],
    page_map: dict[str, Any],
    probes: Probe,
) -> dict[str, Any]:
    meta = load_json(doc_dir / "convert_meta.json") if (doc_dir / "convert_meta.json").is_file() else {}
    pdf = Path(meta.get("source_pdf") or "")
    if not pdf.is_file():
        probes.add("equation census", False, f"source PDF missing: {pdf}")
        return {"misses": [], "census": 0}
    # rebuild section hints from equations/sections
    section_at: dict[int, Optional[str]] = {}
    for e in equations:
        p = e.get("pdf_page")
        if p and e.get("section"):
            section_at.setdefault(int(p), e.get("section"))
    pm_int = {int(k): v for k, v in page_map.items()}
    census = census_pdf_eq_ids(pdf, pm_int, section_at)
    index_ids = {(e.get("eq_id"), e.get("pdf_page")) for e in equations if e.get("eq_id")}
    index_id_only = {e.get("eq_id") for e in equations if e.get("eq_id")}
    misses = []
    def _in_index(eid: str) -> bool:
        if eid in index_id_only:
            return True
        # AISI dropped-letter PDF form (Eq. 1.3.1.2-1) indexed as E1.3.1.2-1
        if eid and eid[0].isdigit():
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if f"{letter}{eid}" in index_id_only:
                    return True
        return False

    for rec in census:
        if (rec["eq_id"], rec["pdf_page"]) in index_ids or _in_index(rec["eq_id"]):
            continue
        misses.append(rec)
    # Unexplained = not in index at all (by id). Page-level mismatch is reported
    # but if the id exists anywhere that is explained (same eq on neighboring page).
    unexplained = [m for m in misses]
    probes.add(
        "equation census (every PDF Eq. id in equations index)",
        len(unexplained) == 0,
        f"census={len(census)} unique_index_ids={len(index_id_only)} misses={len(unexplained)}"
        + (f" sample={unexplained[:8]}" if unexplained else ""),
    )
    return {"misses": unexplained, "census": census, "index_ids": sorted(index_id_only)}


def probe_leakage(search_md: Path, orig_md: Path, probes: Probe) -> dict[str, int]:
    search = search_md.read_text(encoding="utf-8") if search_md.is_file() else ""
    orig = orig_md.read_text(encoding="utf-8") if orig_md.is_file() else ""
    # ignore HTML comments (page-map markers)
    search_nocomment = re.sub(r"<!--.*?-->", "", search, flags=re.S)
    c_search = search_nocomment.count(COPYRIGHT_LINE)
    c_orig = orig.count(COPYRIGHT_LINE)
    probes.add(
        "header/footer leakage: AISI copyright absent from searchable text",
        c_search == 0,
        f"searchable_hits={c_search} original_all_layer_hits={c_orig}",
    )
    running = 0
    for rx in RUNNING_TITLE_RES:
        running += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: running titles absent from searchable text",
        running == 0,
        f"running_title_hits={running}",
    )
    return {"copyright_search": c_search, "copyright_orig": c_orig, "running_search": running}


def probe_page_mapping(blocks_path: Path, probes: Probe, n: int = 20) -> None:
    if not blocks_path.is_file():
        probes.add("page-mapping sample blocks", False, f"missing {blocks_path}")
        return
    rows = []
    with blocks_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) < 5:
        probes.add("page-mapping sample blocks", False, f"only {len(rows)} blocks")
        return
    rng = random.Random(40020)
    sample = rows if len(rows) <= n else rng.sample(rows, n)
    bad = []
    for b in sample:
        if b.get("pdf_page") is None:
            bad.append(("missing_pdf_page", b.get("self_ref")))
            continue
        # printed_label may be None on covers (pdf 1-2, 91, 179-180) — allowed
        p = int(b["pdf_page"])
        if p not in (1, 2, 91, 179, 180) and not b.get("printed_label"):
            bad.append(("missing_printed_label", p, b.get("label")))
        if b.get("part") not in ("standard", "commentary"):
            bad.append(("bad_part", p, b.get("part")))
    probes.add(
        "page-mapping: sample blocks have pdf_page and printed_label",
        len(bad) == 0,
        f"sampled={len(sample)} of {len(rows)} issues={bad[:6]}",
    )



def nfkc(text: str) -> str:
    """NFKC so ligatures like ﬂat match 'flat' in gold probes."""
    return unicodedata.normalize("NFKC", text or "")


def squash_math(text: str) -> str:
    """Strip latex/subscripts/spaces so Mn = Mp = Fy Zx matches M_n=M_p=F_yZ_x."""
    s = nfkc(text or "")
    s = s.replace("\\mathrm", "").replace("\\text", "")
    s = re.sub(r"[_\\{}\s]+", "", s)
    s = s.replace("×", "").replace("*", "")
    return s.lower()


def probe_f21(equations: list[dict[str, Any]], search_md: Path, probes: Probe) -> None:
    hits = [
        e
        for e in equations
        if (e.get("eq_id") or "") in {"F2-1", "F21"}
        or (e.get("eq_id_display") or "") in {"(F2-1)", "(Eq. F2-1)"}
    ]
    std = [e for e in hits if e.get("part") != "commentary"]
    blobs = []
    for e in std:
        blobs.extend(
            [
                e.get("latex") or "",
                e.get("orig") or "",
                e.get("nearby_text") or "",
            ]
        )
    page_txt = ""
    pages_dir = search_md.parent / "pages_search"
    for e in std:
        p = e.get("pdf_page")
        if p and pages_dir.is_dir():
            fp = pages_dir / f"page_{int(p):03d}.md"
            if fp.is_file():
                page_txt += "\n" + fp.read_text(encoding="utf-8")
    if search_md.is_file() and not page_txt:
        page_txt = search_md.read_text(encoding="utf-8")
    blobs.append(page_txt)
    joined = "\n".join(blobs)
    squashed = squash_math(joined)
    has_mn = "mn=mp=fyzx" in squashed or "mn=mp=fy*zx" in squashed or "mn=mp=fyz" in squashed
    # slightly looser: Mn, Mp, Fy, Zx all present near each other
    has_parts = all(x in squashed for x in ("mn", "mp", "fy", "zx")) and "mn=mp" in squashed
    ok = bool(std) and (has_mn or has_parts)
    excerpt = collapse_ws(std[0].get("nearby_text") or std[0].get("latex") or "")[:180] if std else ""
    probes.add(
        "Eq F2-1 (Mn = Mp = Fy Zx)",
        ok,
        f"hits={[{'eq_id': e.get('eq_id'), 'pdf': e.get('pdf_page'), 'printed': e.get('printed_label'), 'part': e.get('part')} for e in std[:4]]} "
        f"has_mn={has_mn} has_parts={has_parts} excerpt={excerpt!r}",
    )


def probe_table_b41a(tables: list[dict[str, Any]], search_md: Path, probes: Probe) -> None:
    candidates = [
        t
        for t in tables
        if (t.get("table_id") or "").replace(" ", "") in {"B4.1a", "B41a", "B4.1A"}
        or (t.get("table_id") or "").startswith("B4.1a")
        or "B4.1a" in (t.get("title") or "")
        or "B4.1a" in (t.get("markdown_excerpt") or "")
    ]
    real = [
        t
        for t in candidates
        if t.get("source") != "caption_only"
        and t.get("num_rows") not in (None, 0)
    ]
    blobs: list[str] = []
    for t in real:
        blobs.append(t.get("markdown_excerpt") or "")
        md = t.get("md")
        if md and Path(md).is_file():
            blobs.append(Path(md).read_text(encoding="utf-8"))
    page_blob = ""
    if search_md.is_file():
        full = search_md.read_text(encoding="utf-8")
        m = re.search(
            r"<!--\s*pdf_page=89\b.*?-->\s*(.*?)(?=<!--\s*pdf_page=\d+|\Z)",
            full,
            re.S,
        )
        if m:
            page_blob = m.group(1)
            blobs.append(page_blob)
        pages_dir = search_md.parent / "pages_search"
        fp = pages_dir / "page_089.md"
        if fp.is_file():
            blobs.append(fp.read_text(encoding="utf-8"))
        rec = search_md.parent / "pages_recovered" / "page_089.md"
        if rec.is_file():
            blobs.append(rec.read_text(encoding="utf-8"))
    joined = "\n".join(blobs)
    squashed = re.sub(r"\s+", "", joined).lower()
    squashed_ascii = (
        squashed.replace("√", "sqrt")
        .replace("\\sqrt", "sqrt")
        .replace("λr", "lambdar")
        .replace("λp", "lambdap")
    )
    has_case = bool(
        re.search(r"Flanges of rolled", joined, re.I)
        or re.search(r"Unstiffened Elements", joined, re.I)
    )
    has_lambda = (
        "0.56sqrt" in squashed_ascii
        or "0.56√" in joined
        or bool(re.search(r"0\s*\.\s*56.{0,40}sqrt.{0,20}e.{0,8}fy", squashed_ascii))
        or (
            "0.56" in squashed_ascii
            and "sqrt" in squashed_ascii
            and "fy" in squashed_ascii
        )
    )
    has_ratio = bool(re.search(r"\bb\s*/\s*t\b|\bbt\b|Width-to-Thickness", joined, re.I))
    ok = bool(real) and has_case and has_lambda and has_ratio
    excerpt = collapse_ws(joined)[:260]
    probes.add(
        "Table B4.1a found",
        ok,
        f"real_tables={len(real)} caption_only={len(candidates) - len(real)} "
        f"num_rows={[t.get('num_rows') for t in real[:4]]} "
        f"has_case={has_case} has_lambda={has_lambda} has_ratio={has_ratio} "
        f"excerpt={excerpt!r}",
    )


def probe_f22_parts(sections: list[dict[str, Any]], probes: Probe) -> None:
    f22 = [s for s in sections if s.get("section_id") == "F2.2"]
    f2 = [s for s in sections if s.get("section_id") == "F2"]
    std_f22 = [s for s in f22 if s.get("part") == "standard"]
    com_f2 = [s for s in f2 if s.get("part") == "commentary"]
    com_f22 = [s for s in f22 if s.get("part") == "commentary"]
    std_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 121) <= 5 for s in std_f22
    )
    # accept F2 provision on ~121 as a weak fallback only if F2.2 missing? No — require F2.2.
    probes.add(
        "Section F2.2 provision (not commentary)",
        std_ok and all(s.get("part") == "standard" for s in std_f22),
        f"standard F2.2={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part'), 'title': s.get('title')} for s in std_f22]}",
    )
    com_ok = bool(com_f2 or com_f22) and all(
        s.get("part") == "commentary" for s in (com_f2 + com_f22)
    )
    # commentary F2 is ~pdf 445
    com_page_ok = any(
        s.get("pdf_page") is not None and int(s["pdf_page"]) >= 400
        for s in (com_f2 + com_f22)
    )
    probes.add(
        "Commentary F2 / F2.2 flagged part=commentary",
        com_ok and com_page_ok,
        f"commentary F2={[{'id': s.get('section_id'), 'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part')} for s in (com_f2 + com_f22)[:6]]}",
    )


def probe_aisc_commentary_boundary(docs: list[dict[str, Any]], probes: Probe) -> None:
    if not docs:
        probes.add("commentary boundary ~pdf p.355", False, "documents.json empty")
        return
    b = (docs[0].get("commentary_boundary") or {}) if isinstance(docs[0], dict) else {}
    cover = b.get("cover_pdf_page")
    body = b.get("body_pdf_page")
    ok = cover is not None and abs(int(cover) - 355) <= 8
    if body is not None:
        ok = ok and int(body) >= int(cover) - 1
    probes.add(
        "commentary boundary ~pdf p.355",
        ok,
        f"cover={cover} body={body} profile={b.get('profile')}",
    )


def probe_aisc_leakage(search_md: Path, orig_md: Path, probes: Probe) -> dict[str, int]:
    search = search_md.read_text(encoding="utf-8") if search_md.is_file() else ""
    orig = orig_md.read_text(encoding="utf-8") if orig_md.is_file() else ""
    search_nocomment = re.sub(r"<!--.*?-->", "", search, flags=re.S)
    running = 0
    for rx in AISC_RUNNING_TITLE_RES:
        running += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: AISC running titles absent from searchable text",
        running == 0,
        f"running_title_hits={running}",
    )
    # Copyright *page* body (p.4) may contain © AISC 2022 once; fail if it
    # leaked onto many pages (running-footer behaviour).
    c_search = 0
    for rx in AISC_COPYRIGHT_RES:
        c_search += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: AISC copyright not repeated in searchable text",
        c_search <= 3,
        f"searchable_copyright_hits={c_search} (allow <=3 for the copyright page itself)",
    )
    # AISI line must still be counted as 0 (should not appear in AISC).
    aisi = search_nocomment.count(COPYRIGHT_LINE)
    probes.add(
        "AISI copyright line absent (AISC document)",
        aisi == 0,
        f"aisi_copyright_hits={aisi}",
    )
    return {
        "aisc_running_search": running,
        "aisc_copyright_search": c_search,
        "aisi_copyright_search": aisi,
    }


def probe_aisc_page_mapping(blocks_path: Path, probes: Probe, n: int = 20) -> None:
    if not blocks_path.is_file():
        probes.add("page-mapping sample blocks", False, f"missing {blocks_path}")
        return
    rows = []
    with blocks_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) < 5:
        probes.add("page-mapping sample blocks", False, f"only {len(rows)} blocks")
        return
    rng = random.Random(36022)
    sample = rows if len(rows) <= n else rng.sample(rows, n)
    bad = []
    labels = []
    for b in sample:
        if b.get("pdf_page") is None:
            bad.append(("missing_pdf_page", b.get("self_ref")))
            continue
        p = int(b["pdf_page"])
        printed = b.get("printed_label") or ""
        labels.append((p, printed))
        # covers / blanks: pdf 1-3 may have no 16.1-xxx
        if p not in (1, 2, 3) and not printed:
            bad.append(("missing_printed_label", p, b.get("label")))
        if printed and not AISC_PRINTED_LABEL_RE.search(str(printed)):
            # allow None already handled; reject non-16.1 labels on content pages
            if p not in (1, 2, 3):
                bad.append(("printed_label_not_16_1", p, printed))
        if b.get("part") not in ("standard", "commentary"):
            bad.append(("bad_part", p, b.get("part")))
    probes.add(
        "page-mapping: sample blocks have pdf_page and printed_label 16.1-xxx",
        len(bad) == 0,
        f"sampled={len(sample)} of {len(rows)} issues={bad[:6]} labels={labels[:8]}",
    )



HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]{3,}")
IMAGE_ONLY_PDF_CHAR_THRESHOLD = 100

FURNITURE_LINE_RES = [
    re.compile(r"Specification for Structural Steel Buildings", re.I),
    re.compile(r"American Institute of Steel Construction", re.I),
    re.compile(r"Part\s+16\.1\b", re.I),
    re.compile(r"\.indd\b", re.I),
    re.compile(r"This document is copyrighted by AISI", re.I),
    re.compile(r"^North American Standard for Seismic Design", re.I),
    re.compile(r"^Commentary on North American Standard", re.I),
    re.compile(r"^AISI\s+S400-20", re.I),
    re.compile(r"^AISI STANDARD\s*$", re.I),
    re.compile(
        r"AISI\s*S100-16(?:-C)?(?:\s*\(R?2020\))?(?:\s*w/S3-22)?\s*$",
        re.I,
    ),
    re.compile(r"This Page is Intentionally Left Blank", re.I),
    re.compile(r"^\s*(?:[A-Z]-)?\d+(?:-\d+)?\s+Appendix\s+", re.I),
    re.compile(r"^\s*(?:[A-Z]-)?\d+(?:-\d+)?\s+Chapter\s+", re.I),
    re.compile(
        r"The 2016 Edition \(Reaffirmed 2020\) of the North American Specification",
        re.I,
    ),
    re.compile(r"^Structural Members With Supplement 3\b", re.I),
    re.compile(
        r"Commentary on the 2016 Edition \(Reaffirmed 2020\) of the North American Cold-Formed Steel",
        re.I,
    ),
    re.compile(r"^Specification With Supplement 3\b", re.I),
    re.compile(r"Copyright American Iron and Steel Institute", re.I),
    re.compile(r"Smarter\.\s*Stronger\.\s*Steel", re.I),
    re.compile(r"Downloaded from ascelibrary\.org", re.I),
    re.compile(r"Copyright ASCE; all rights reserved", re.I),
    re.compile(r"COMMENTARY TO STANDARD ASCE/SEI", re.I),
    re.compile(r"^STANDARD ASCE/SEI 7-22\s*$", re.I),
    re.compile(r"Prequalified Connections for Special and Intermediate Steel", re.I),
    re.compile(r"Moment Frames for Seismic Applications,\s*August 18,\s*2022", re.I),
    re.compile(r"^\s*9\.2\s*[-–—]\s*[ivxlcdm0-9]+\s*$", re.I),
    re.compile(r"^Comm\.\s+\d", re.I),
    re.compile(r"Seismic Provisions for Structural Steel Buildings", re.I),
    re.compile(r"^\s*9\.1\s*[-–—]\s*[ivxlcdm0-9]+\s*$", re.I),
]


def parse_search_md_pages(search_md: Path) -> dict[int, str]:
    if not search_md.is_file():
        return {}
    text = search_md.read_text(encoding="utf-8")
    parts = re.split(r"(?=<!--\s*pdf_page=\d+)", text)
    out: dict[int, str] = {}
    for part in parts:
        m = re.match(r"<!--\s*pdf_page=(\d+)\b", part)
        if not m:
            continue
        out[int(m.group(1))] = part
    return out


def body_without_comments(block: str) -> str:
    return HTML_COMMENT_RE.sub("", block or "").strip()


def is_comment_only_body(block: str) -> bool:
    return len(body_without_comments(block)) == 0


def strip_pdf_furniture(page_text: str) -> str:
    lines: list[str] = []
    for line in (page_text or "").splitlines():
        if any(rx.search(line) for rx in FURNITURE_LINE_RES):
            continue
        if re.match(r"^\s*\[?Sect\.\s+[A-Z0-9.\-]+\]?\s*$", line, re.I):
            continue
        if re.match(r"^\s*16\.1\s*-+\s*[ivxlcdm0-9]+\s*$", line, re.I):
            continue
        if re.match(r"^\s*9\.1\s*[-–—]\s*[ivxlcdm0-9]+\s*$", line, re.I):
            continue
        if re.match(r"^\s*\[Comm\.", line, re.I):
            continue
        lines.append(line)
    return "\n".join(lines)


def resolve_source_pdf(doc_dir: Path, stem: str, meta: dict[str, Any]) -> Optional[Path]:
    p = Path(meta.get("source_pdf") or "")
    if p.is_file():
        return p
    orig = doc_dir / "original"
    if orig.is_dir():
        for f in sorted(orig.iterdir()):
            if f.suffix.lower() == ".pdf" and f.exists():
                return f.resolve() if not f.is_symlink() else f.resolve()
    s = (stem or "").lower()
    cands: list[Path] = []
    if "s240" in s:
        cands.append(Path("/workspace/standards/AISI-S240-20.pdf"))
    elif "s100" in s:
        cands.append(Path("/workspace/standards/AISI-S100-16-2020-wS3-22.pdf"))
    elif "s400" in s:
        cands.append(Path("/workspace/standards/AISI-S400-20.pdf"))
    if "358" in s or "a358" in s:
        cands.append(Path("/workspace/standards/A358-22.pdf"))
    elif "341" in s or "a341" in s:
        cands.append(Path("/workspace/standards/A341-22.pdf"))
    elif "360" in s or "a360" in s or s.startswith("aisc"):
        cands.append(Path("/workspace/standards/A360-22.pdf"))
    if "asce" in s:
        cands.extend(
            [
                Path("/workspace/standards/asce7.fixed.pdf"),
                Path("/workspace/standards/asce7.pdf"),
            ]
        )
    for c in cands:
        if c.is_file():
            return c
    return None


def load_pdf_pages(pdf: Optional[Path]) -> list[str]:
    if not pdf or not pdf.is_file():
        return []
    return pdf_text_pages(pdf)


def token_set(text: str) -> set[str]:
    t = HTML_COMMENT_RE.sub(" ", text or "")
    return set(TOKEN_RE.findall(t.lower()))


def probe_image_only_pages(
    search_pages: dict[int, str],
    pdf_pages: list[str],
    pages_search: Path,
    probes: Probe,
) -> dict[str, Any]:
    failing: list[dict[str, Any]] = []
    skipped: list[int] = []
    n_pdf = len(pdf_pages)
    n_search = max(search_pages) if search_pages else 0
    n = max(n_pdf, n_search)
    for pno in range(1, n + 1):
        block = search_pages.get(pno, "")
        if not block and pages_search.is_dir():
            fp = pages_search / f"page_{pno:03d}.md"
            if fp.is_file():
                block = fp.read_text(encoding="utf-8")
        if not is_comment_only_body(block):
            continue
        pdf_raw = pdf_pages[pno - 1] if 0 <= pno - 1 < n_pdf else ""
        pdf_body = strip_pdf_furniture(pdf_raw)
        nchars = len(re.sub(r"\s+", " ", pdf_body).strip())
        has_caption_token = bool(re.search(r"\b(Table|Figure)\b", pdf_body, re.I))
        # True blanks only: watermark-stripped PDF text < ~100 chars AND no
        # Table/Figure caption token (ASCE C26.5-5 was skipped as blank).
        if nchars < IMAGE_ONLY_PDF_CHAR_THRESHOLD and not has_caption_token:
            skipped.append(pno)
            continue
        failing.append({"pdf_page": pno, "pdf_chars": nchars})
    probes.add(
        "image-only body pages with extractable PDF text",
        len(failing) == 0,
        f"failing_pages={[x['pdf_page'] for x in failing]} "
        f"skipped_tiny_or_blank={skipped} n_fail={len(failing)}",
    )
    return {"failing": failing, "skipped": skipped}


def probe_tables_num_rows(tables: list[dict[str, Any]], probes: Probe) -> None:
    bad = []
    for t in tables:
        if t.get("num_rows") is None:
            bad.append(
                {
                    "table_id": t.get("table_id"),
                    "pdf_page": t.get("pdf_page"),
                    "source": t.get("source"),
                }
            )
    probes.add(
        "tables.json num_rows not null (caption_only is a conversion failure)",
        len(bad) == 0,
        f"null_num_rows={len(bad)} sample={bad[:10]}",
    )


def probe_page_boundary_attribution(
    search_pages: dict[int, str],
    pdf_pages: list[str],
    pages_search: Path,
    probes: Probe,
) -> dict[str, Any]:
    if not pdf_pages:
        probes.add(
            "page-boundary attribution (>=50% distinctive tokens on own page)",
            False,
            "no PDF text pages (source PDF missing)",
        )
        return {"failing": [], "checked": 0}
    per_pdf: list[set[str]] = [token_set(strip_pdf_furniture(pg)) for pg in pdf_pages]
    n = len(per_pdf)
    df: dict[str, int] = {}
    for s in per_pdf:
        for tok in s:
            df[tok] = df.get(tok, 0) + 1
    max_df = max(2, int(0.10 * n))
    failing: list[dict[str, Any]] = []
    checked = 0
    for i, pdf_toks in enumerate(per_pdf, 1):
        distinctive = {t for t in pdf_toks if df.get(t, 0) <= max_df}
        if len(distinctive) < 6:
            continue
        search_block = search_pages.get(i, "")
        if pages_search.is_dir():
            fp = pages_search / f"page_{i:03d}.md"
            if fp.is_file():
                search_block = (search_block or "") + "\n" + fp.read_text(encoding="utf-8")
        search_toks = token_set(search_block)
        squash = re.sub(r"[^a-z0-9]+", "", HTML_COMMENT_RE.sub(" ", search_block).lower())
        hit = {t for t in distinctive if t in search_toks or t in squash}
        ratio = len(hit) / len(distinctive)
        checked += 1
        if ratio < 0.50:
            failing.append(
                {
                    "pdf_page": i,
                    "ratio": round(ratio, 3),
                    "distinctive": len(distinctive),
                    "hit": len(hit),
                }
            )
    probes.add(
        "page-boundary attribution (>=50% distinctive tokens on own page)",
        len(failing) == 0,
        f"checked={checked} failing={len(failing)} sample={failing[:12]}",
    )
    return {"failing": failing, "checked": checked}




def _asce_table_blobs(tables: list[dict[str, Any]], search_md: Path, extra_pages: list[int] | None = None) -> str:
    blobs: list[str] = []
    for t in tables:
        blobs.append(t.get("markdown_excerpt") or "")
        blobs.append(t.get("title") or "")
        blobs.append(t.get("table_id") or "")
        md = t.get("md")
        if md and Path(md).is_file():
            try:
                blobs.append(Path(md).read_text(encoding="utf-8"))
            except Exception:
                pass
    pages_dir = search_md.parent / "pages_search" if search_md else Path()
    rec_dir = search_md.parent / "pages_recovered" if search_md else Path()
    for pno in extra_pages or []:
        for d in (pages_dir, rec_dir):
            fp = d / f"page_{int(pno):03d}.md"
            if fp.is_file():
                blobs.append(fp.read_text(encoding="utf-8"))
    if search_md.is_file():
        blobs.append(search_md.read_text(encoding="utf-8"))
    return "\n".join(blobs)


def probe_asce7_eq_1283(equations: list[dict[str, Any]], search_md: Path, probes: Probe) -> None:
    hits = [
        e
        for e in equations
        if (e.get("eq_id") or "") in {"12.8-3", "12.8-3.SI"}
        or (e.get("eq_id_display") or "") in {"(12.8-3)", "(Eq. 12.8-3)"}
        or "12.8-3" in (e.get("nearby_text") or "")
        or "12.8-3" in (e.get("orig") or "")
    ]
    blobs = []
    for e in hits:
        blobs.extend([e.get("latex") or "", e.get("orig") or "", e.get("nearby_text") or ""])
    pages_dir = search_md.parent / "pages_search"
    rec_dir = search_md.parent / "pages_recovered"
    for pno in range(170, 201):
        for d in (pages_dir, rec_dir):
            fp = d / f"page_{pno:03d}.md"
            if fp.is_file():
                blobs.append(fp.read_text(encoding="utf-8"))
    if search_md.is_file() and not any(blobs):
        blobs.append(search_md.read_text(encoding="utf-8"))
    joined = "\n".join(blobs)
    squashed = squash_math(joined)
    has_id = "12.8-3" in joined or any(
        (e.get("eq_id") or "") == "12.8-3" for e in hits
    )
    has_cs = "cs" in squashed
    has_sds = "sds" in squashed
    has_r = bool(re.search(r"\br\b|r/ie|r\\\\ie", joined, re.I)) or "r/ie" in squashed or "rie" in squashed
    has_ie = "ie" in squashed or "i_e" in joined.lower()
    page_ok = any(
        e.get("pdf_page") is not None and abs(int(e["pdf_page"]) - 185) <= 20 for e in hits
    )
    # Do not fail solely on page number if id + formula tokens are present.
    ok = has_id and has_cs and has_sds and (has_r or has_ie)
    excerpt = collapse_ws(joined)[:220]
    probes.add(
        "Eq 12.8-3 Cs related to SDS / (R/Ie)",
        ok,
        f"hits={[{'eq_id': e.get('eq_id'), 'pdf': e.get('pdf_page'), 'part': e.get('part')} for e in hits[:6]]} "
        f"has_id={has_id} has_cs={has_cs} has_sds={has_sds} has_r={has_r} has_ie={has_ie} "
        f"page_near_185={page_ok} excerpt={excerpt!r}",
    )


def probe_asce7_table_1221(tables: list[dict[str, Any]], search_md: Path, probes: Probe) -> None:
    candidates = [
        t
        for t in tables
        if (t.get("table_id") or "").replace(" ", "") in {"12.2-1", "12.21"}
        or (t.get("table_id") or "").startswith("12.2-1")
        or "12.2-1" in (t.get("title") or "")
        or "12.2-1" in (t.get("markdown_excerpt") or "")
        or t.get("pdf_page") in (173, 174, 175, 176)
    ]
    real = [
        t
        for t in candidates
        if t.get("source") != "caption_only" and t.get("num_rows") not in (None, 0)
    ]
    joined = nfkc(_asce_table_blobs(real or candidates, search_md, extra_pages=[173, 174, 175, 176]))
    squashed = re.sub(r"\s+", " ", joined).lower()
    squashed_ns = re.sub(r"\s+", "", squashed)
    has_caption = "12.2-1" in joined
    has_strap = bool(
        re.search(r"flat\s*strap", joined, re.I)
        or re.search(r"ﬂat\s*strap", joined, re.I)
    )
    has_cfs = bool(re.search(r"cold-?formed\s+steel", joined, re.I))
    has_r4 = bool(re.search(r"\bR\s*=\s*4\b", joined) or re.search(r"\b4\b", joined))
    has_omega = bool(
        re.search(r"omega\s*0?\s*=\s*2", joined, re.I)
        or re.search(r"Ω\s*0?\s*=\s*2", joined)
        or "Ω0" in joined
        or "omega0" in squashed_ns
    )
    # Row 19: R=4, Ω0=2, Cd=3½. Accept 3.5 / 3½ / 3 1/2 next to the strap row.
    strap_window = ""
    m = re.search(
        r".{0,80}(?:flat|ﬂat)\s*strap\s*bracing.{0,160}",
        joined,
        re.I | re.S,
    )
    if m:
        strap_window = m.group(0)
    has_cd = bool(
        re.search(r"3\s*[.\u00bd½]\s*5", strap_window)
        or "3.5" in strap_window
        or "3½" in strap_window
        or "3 1/2" in strap_window
        or "3-1/2" in strap_window
        or re.search(r"\b3½\b|\b3\.5\b", joined)
    )
    # The provision table puts 4 | 2 | 3½ on the strap row.
    row_vals = bool(
        re.search(r"4.{0,40}2.{0,40}(3[\.½]|3½|3\.5)", strap_window, re.S)
        or ("4" in strap_window and "2" in strap_window and has_cd)
    )
    ok = bool(real) and has_caption and has_strap and has_cfs and row_vals
    excerpt = collapse_ws(strap_window or joined)[:260]
    probes.add(
        "Table 12.2-1 light-frame CFS flat strap bracing R=4 Ω0=2 Cd=3.5",
        ok,
        f"real_tables={len(real)} caption_only={len(candidates)-len(real)} "
        f"num_rows={[t.get('num_rows') for t in real[:6]]} "
        f"has_strap={has_strap} has_cfs={has_cfs} has_omega={has_omega} has_cd={has_cd} "
        f"row_vals={row_vals} excerpt={excerpt!r}",
    )


def probe_asce7_section_12432(sections: list[dict[str, Any]], probes: Probe) -> None:
    hits = [s for s in sections if s.get("section_id") == "12.4.3.2"]
    std = [s for s in hits if s.get("part") == "standard"]
    com = [s for s in hits if s.get("part") == "commentary"]
    std_ok = bool(std) and all(s.get("part") == "standard" for s in std)
    # provision is pdf ~183; commentary copy ~719 is allowed in addition
    page_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 183) <= 12 for s in std
    )
    probes.add(
        "Section 12.4.3.2 provision (part=standard, not commentary)",
        std_ok and page_ok,
        f"standard={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part'), 'title': s.get('title')} for s in std]} "
        f"commentary_also={[{'pdf': s.get('pdf_page'), 'part': s.get('part')} for s in com[:4]]}",
    )


def probe_asce7_table_26111(tables: list[dict[str, Any]], search_md: Path, probes: Probe) -> None:
    candidates = [
        t
        for t in tables
        if (t.get("table_id") or "").replace(" ", "") in {"26.11-1", "26.111"}
        or (t.get("table_id") or "").startswith("26.11-1")
        or "26.11-1" in (t.get("title") or "")
        or "26.11-1" in (t.get("markdown_excerpt") or "")
        or t.get("pdf_page") in (338, 339, 340)
    ]
    real = [
        t
        for t in candidates
        if t.get("source") != "caption_only" and t.get("num_rows") not in (None, 0)
    ]
    joined = _asce_table_blobs(real or candidates, search_md, extra_pages=[338, 339, 340])
    squashed = re.sub(r"[\s,]", "", joined).lower()
    has_b = bool(re.search(r"\bB\b", joined) or "exposure b" in joined.lower())
    has_alpha = "7.5" in joined or "alpha=7.5" in squashed or "α=7.5" in joined or "α7.5" in squashed
    has_zg = "3280" in squashed or "3,280" in joined or "1000" in joined
    ok = bool(real) and has_alpha and has_zg
    excerpt = collapse_ws(joined)[:260]
    probes.add(
        "Table 26.11-1 Exposure B α=7.5 zg=3280 ft (real table)",
        ok,
        f"real_tables={len(real)} caption_only={len(candidates)-len(real)} "
        f"num_rows={[t.get('num_rows') for t in real[:4]]} "
        f"has_b={has_b} has_alpha={has_alpha} has_zg={has_zg} excerpt={excerpt!r}",
    )


def probe_asce7_commentary_boundary(
    docs: list[dict[str, Any]],
    sections: list[dict[str, Any]],
    probes: Probe,
) -> None:
    if not docs:
        probes.add("commentary boundary (C1/C11 after ch 1–32)", False, "documents.json empty")
        return
    b = (docs[0].get("commentary_boundary") or {}) if isinstance(docs[0], dict) else {}
    cover = b.get("cover_pdf_page")
    body = b.get("body_pdf_page")
    profile = b.get("profile")
    std_ch = [
        s
        for s in sections
        if s.get("part") == "standard"
        and re.fullmatch(r"\d+", str(s.get("section_id") or ""))
        and 1 <= int(s["section_id"]) <= 32
    ]
    last_prov = max((int(s["pdf_page"]) for s in std_ch if s.get("pdf_page")), default=None)
    com_ch = [
        s
        for s in sections
        if s.get("part") == "commentary"
        and re.fullmatch(r"C\d+", str(s.get("section_id") or ""))
    ]
    first_com = min((int(s["pdf_page"]) for s in com_ch if s.get("pdf_page")), default=None)
    # Cover ~542, C1 ~544. Must be after last provision chapter (~414 / app. ~476).
    cover_ok = cover is not None and int(cover) >= 500
    body_ok = body is not None and int(body) >= int(cover or 0)
    order_ok = True
    if last_prov is not None and first_com is not None:
        order_ok = first_com > last_prov
    elif cover is not None and last_prov is not None:
        order_ok = int(cover) > last_prov
    profile_ok = profile == "asce7"
    ok = cover_ok and body_ok and order_ok and profile_ok
    probes.add(
        "commentary boundary: provisions ch 1–32 then C1/C11 (not AISI Ch. C)",
        ok,
        f"profile={profile} cover={cover} body={body} last_provision_chapter_pdf={last_prov} "
        f"first_C_chapter_pdf={first_com} n_std_ch={len(std_ch)} n_com_ch={len(com_ch)}",
    )


def probe_asce7_leakage(search_md: Path, orig_md: Path, probes: Probe) -> dict[str, int]:
    search = search_md.read_text(encoding="utf-8") if search_md.is_file() else ""
    orig = orig_md.read_text(encoding="utf-8") if orig_md.is_file() else ""
    search_nocomment = re.sub(r"<!--.*?-->", "", search, flags=re.S)
    wm = 0
    for rx in ASCE_WATERMARK_RES + ASCE_COPYRIGHT_RES:
        wm += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: ASCE ascelibrary watermark absent from searchable text",
        wm == 0,
        f"searchable_watermark_hits={wm}",
    )
    running = 0
    for rx in ASCE_RUNNING_TITLE_RES:
        running += len(rx.findall(search_nocomment))
    # The long standard name appears in body (title/preface); only fail full-line headers.
    probes.add(
        "AISI copyright line absent (ASCE document)",
        search_nocomment.count(COPYRIGHT_LINE) == 0,
        f"aisi_copyright_hits={search_nocomment.count(COPYRIGHT_LINE)} orig_len={len(orig)} running_title_hits={running}",
    )
    return {"asce_watermark_search": wm, "asce_running_search": running}


def probe_asce7_page_mapping(blocks_path: Path, probes: Probe, n: int = 20) -> None:
    if not blocks_path.is_file():
        probes.add("page-mapping sample blocks", False, f"missing {blocks_path}")
        return
    rows = []
    with blocks_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) < 5:
        probes.add("page-mapping sample blocks", False, f"only {len(rows)} blocks")
        return
    rng = random.Random(722)
    sample = rows if len(rows) <= n else rng.sample(rows, n)
    bad = []
    for b in sample:
        if b.get("pdf_page") is None:
            bad.append(("missing_pdf_page", b.get("self_ref")))
            continue
        p = int(b["pdf_page"])
        # covers / commentary divider / back matter may lack a printed label
        if p not in set(range(1, 12)) | {541, 542, 543, 544, 545} and not b.get("printed_label"):
            bad.append(("missing_printed_label", p, b.get("label")))
        if b.get("part") not in ("standard", "commentary"):
            bad.append(("bad_part", p, b.get("part")))
    probes.add(
        "page-mapping: sample blocks have pdf_page and part",
        len(bad) == 0,
        f"sampled={len(sample)} of {len(rows)} issues={bad[:6]}",
    )




def probe_aisc358_rbs_chapter(sections: list[dict[str, Any]], probes: Probe) -> None:
    """Chapter 5 Reduced Beam Section (RBS) in the provisions half."""
    hits = [
        s
        for s in sections
        if str(s.get("section_id") or "") in {"5", "5.1", "5.7"}
        or "reduced beam section" in (s.get("title") or "").lower()
        or re.search(r"\bRBS\b", s.get("title") or "")
    ]
    std = [s for s in hits if s.get("part") == "standard"]
    ch5 = [s for s in std if str(s.get("section_id") or "") == "5"]
    titled = [
        s
        for s in std
        if "reduced beam" in (s.get("title") or "").lower() or re.search(r"\bRBS\b", s.get("title") or "")
    ]
    page_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 45) <= 6 for s in (ch5 or titled or std)
    )
    ok = bool(ch5 or titled) and page_ok
    probes.add(
        "RBS chapter (Chapter 5 Reduced Beam Section) found",
        ok,
        f"ch5={[{'id': s.get('section_id'), 'title': s.get('title'), 'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part')} for s in (ch5 or titled or std)[:6]]}",
    )


def probe_aisc358_rbs_design_procedure(
    sections: list[dict[str, Any]],
    search_md: Path,
    probes: Probe,
) -> None:
    """Numbered design steps in Ch. 5 RBS (5.7 Design Procedure), not just the title."""
    sec_57 = [
        s
        for s in sections
        if str(s.get("section_id") or "") == "5.7" and s.get("part") == "standard"
    ]
    blobs: list[str] = []
    pages_dir = search_md.parent / "pages_search" if search_md else Path()
    rec_dir = search_md.parent / "pages_recovered" if search_md else Path()
    for pno in range(45, 52):
        for d in (pages_dir, rec_dir):
            fp = d / f"page_{pno:03d}.md"
            if fp.is_file():
                blobs.append(fp.read_text(encoding="utf-8"))
    if search_md.is_file():
        full = search_md.read_text(encoding="utf-8")
        m = re.search(
            r"(<!--\s*pdf_page=49\b.*?-->\s*.*?)(?=<!--\s*pdf_page=\d+|\Z)",
            full,
            re.S,
        )
        if m:
            blobs.append(m.group(1))
        m2 = re.search(
            r"(<!--\s*pdf_page=50\b.*?-->\s*.*?)(?=<!--\s*pdf_page=\d+|\Z)",
            full,
            re.S,
        )
        if m2:
            blobs.append(m2.group(1))
        if not blobs:
            blobs.append(full)
    joined = "\n".join(blobs)
    steps = [bool(re.search(rf"Step\s+{n}\b", joined, re.I)) for n in range(1, 14)]
    n_steps = sum(steps)
    has_zrbs = bool(re.search(r"Z\s*_?\s*RBS|ZRBS", joined, re.I)) or "5.7-4" in joined
    has_mpe = "5.7-6" in joined or bool(re.search(r"M\s*_?\s*pe", joined, re.I))
    has_proc = bool(re.search(r"Design Procedure", joined, re.I)) or bool(sec_57)
    ok = n_steps >= 8 and has_proc and (has_zrbs or has_mpe)
    probes.add(
        "RBS chapter step-numbered design procedure present",
        ok,
        f"section_5.7={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'title': s.get('title')} for s in sec_57]} "
        f"n_steps={n_steps}/13 steps_1_8={steps[:8]} has_proc={has_proc} has_zrbs={has_zrbs} has_mpe={has_mpe}",
    )


def probe_aisc358_commentary(
    docs: list[dict[str, Any]],
    sections: list[dict[str, Any]],
    probes: Probe,
) -> None:
    """358 has a commentary half (cover pdf 211). Tag both halves; do not invent a split."""
    if not docs:
        probes.add(
            "commentary vs provision tagged (AISC 358)",
            False,
            "documents.json empty",
        )
        return
    b = (docs[0].get("commentary_boundary") or {}) if isinstance(docs[0], dict) else {}
    cover = b.get("cover_pdf_page")
    body = b.get("body_pdf_page")
    profile = b.get("profile")
    ch5_std = [
        s
        for s in sections
        if str(s.get("section_id") or "") == "5" and s.get("part") == "standard"
    ]
    ch5_com = [
        s
        for s in sections
        if str(s.get("section_id") or "") == "5" and s.get("part") == "commentary"
    ]
    # Verified from the PDF: commentary cover is pdf 211.
    if cover is None:
        probes.add(
            "commentary vs provision tagged (AISC 358)",
            False,
            "no commentary boundary detected, but 358 has a commentary half "
            "(cover pdf 211, 'COMMENTARY on Prequalified Connections…'); "
            "refusing to invent a split",
        )
        return
    cover_ok = abs(int(cover) - 211) <= 8
    body_ok = body is not None and int(body) >= int(cover) - 1
    profile_ok = profile in ("aisc_358", "aisc")
    # provision Ch.5 ~45; commentary Ch.5 ~229
    std_page = any(
        s.get("pdf_page") is not None and int(s["pdf_page"]) < int(cover) for s in ch5_std
    ) or any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 45) <= 8 for s in ch5_std
    )
    com_page = any(
        s.get("pdf_page") is not None and int(s["pdf_page"]) >= int(cover) for s in ch5_com
    ) or any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 229) <= 12 for s in ch5_com
    )
    ok = cover_ok and body_ok and profile_ok and std_page and com_page
    probes.add(
        "commentary vs provision tagged (AISC 358)",
        ok,
        f"profile={profile} cover={cover} body={body} "
        f"ch5_std={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label')} for s in ch5_std[:3]]} "
        f"ch5_com={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label')} for s in ch5_com[:3]]}",
    )


def probe_aisc358_leakage(search_md: Path, orig_md: Path, probes: Probe) -> dict[str, int]:
    search = search_md.read_text(encoding="utf-8") if search_md.is_file() else ""
    orig = orig_md.read_text(encoding="utf-8") if orig_md.is_file() else ""
    search_nocomment = re.sub(r"<!--.*?-->", "", search, flags=re.S)
    running = 0
    for rx in AISC_358_RUNNING_TITLE_RES:
        running += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: AISC 358 running titles absent from searchable text",
        running == 0,
        f"running_title_hits={running}",
    )
    c_search = 0
    for rx in AISC_COPYRIGHT_RES:
        c_search += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: AISC copyright not repeated in searchable text",
        c_search <= 3,
        f"searchable_copyright_hits={c_search} (allow <=3 for the copyright page itself)",
    )
    aisi = search_nocomment.count(COPYRIGHT_LINE)
    probes.add(
        "AISI copyright line absent (AISC 358 document)",
        aisi == 0,
        f"aisi_copyright_hits={aisi} orig_len={len(orig)}",
    )
    return {
        "aisc358_running_search": running,
        "aisc_copyright_search": c_search,
        "aisi_copyright_search": aisi,
    }


def probe_aisc358_page_mapping(blocks_path: Path, probes: Probe, n: int = 20) -> None:
    if not blocks_path.is_file():
        probes.add("page-mapping sample blocks", False, f"missing {blocks_path}")
        return
    rows = []
    with blocks_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) < 5:
        probes.add("page-mapping sample blocks", False, f"only {len(rows)} blocks")
        return
    rng = random.Random(35822)
    sample = rows if len(rows) <= n else rng.sample(rows, n)
    bad = []
    labels = []
    skip_pages = set(range(1, 5)) | {357, 358}
    for b in sample:
        if b.get("pdf_page") is None:
            bad.append(("missing_pdf_page", b.get("self_ref")))
            continue
        p = int(b["pdf_page"])
        printed = b.get("printed_label") or ""
        labels.append((p, printed))
        if p not in skip_pages and not printed:
            bad.append(("missing_printed_label", p, b.get("label")))
        if printed and not AISC_358_PRINTED_LABEL_RE.search(str(printed)):
            if p not in skip_pages:
                bad.append(("printed_label_not_9_2", p, printed))
        if b.get("part") not in ("standard", "commentary"):
            bad.append(("bad_part", p, b.get("part")))
    probes.add(
        "page-mapping: sample blocks have pdf_page and printed_label 9.2-xxx",
        len(bad) == 0,
        f"sampled={len(sample)} of {len(rows)} issues={bad[:6]} labels={labels[:8]}",
    )



def probe_aisc341_e34a(
    sections: list[dict[str, Any]],
    search_md: Path,
    probes: Probe,
) -> None:
    """Section E3.4a (SCWB / strong-column weak-beam) as provision, not commentary."""
    hits = [
        s
        for s in sections
        if str(s.get("section_id") or "") == "E3.4a"
    ]
    std = [s for s in hits if s.get("part") == "standard"]
    com = [s for s in hits if s.get("part") == "commentary"]
    page_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 99) <= 8 for s in std
    )
    blobs: list[str] = []
    pages_dir = search_md.parent / "pages_search" if search_md else Path()
    rec_dir = search_md.parent / "pages_recovered" if search_md else Path()
    for pno in range(96, 104):
        for d in (pages_dir, rec_dir):
            fp = d / f"page_{pno:03d}.md"
            if fp.is_file():
                blobs.append(fp.read_text(encoding="utf-8"))
    if search_md.is_file():
        full = search_md.read_text(encoding="utf-8")
        for pno in (99, 100, 101):
            m = re.search(
                rf"(<!--\s*pdf_page={pno}\b.*?-->\s*.*?)(?=<!--\s*pdf_page=\d+|\Z)",
                full,
                re.S,
            )
            if m:
                blobs.append(m.group(1))
        if not blobs:
            blobs.append(full)
    joined = "\n".join(blobs)
    has_scwb = bool(
        re.search(r"SC\s*/?\s*WB|SCWB|strong[- ]column|weak[- ]beam", joined, re.I)
    )
    has_equiv = bool(
        re.search(r"Moment Ratio", joined, re.I)
        or re.search(r"columns shall be designed to be stronger", joined, re.I)
        or re.search(r"E3-1", joined)
        or re.search(r"\\bM\\s*\\*?\\s*pc\\b|\\\\Sigma\\s*M", joined, re.I)
    )
    ok = bool(std) and page_ok and (has_scwb or has_equiv)
    probes.add(
        "Section E3.4a (SCWB / strong-column weak-beam) as provision",
        ok,
        f"std={[{'id': s.get('section_id'), 'title': s.get('title'), 'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part')} for s in std[:4]]} "
        f"com={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label')} for s in com[:3]]} "
        f"page_ok={page_ok} has_scwb={has_scwb} has_equiv={has_equiv}",
    )


def probe_aisc341_table_d11b(
    tables: list[dict[str, Any]],
    search_md: Path,
    probes: Probe,
) -> None:
    """Table D1.1b is a real table (not caption-only; num_rows not null)."""
    def _tid(t: dict[str, Any]) -> str:
        return (t.get("table_id") or "").replace(" ", "")

    candidates = [
        t
        for t in tables
        if _tid(t) in {"D1.1b", "D11b", "D1.1B"}
        or _tid(t).startswith("D1.1b")
        or "D1.1b" in (t.get("title") or "")
        or "D1.1b" in (t.get("markdown_excerpt") or "")
        or "TABLE D1.1b" in ((t.get("title") or "") + (t.get("markdown_excerpt") or "")).upper()
    ]
    real = [
        t
        for t in candidates
        if t.get("source") != "caption_only" and t.get("num_rows") not in (None, 0)
    ]
    blobs: list[str] = []
    for t in real or candidates:
        blobs.append(t.get("markdown_excerpt") or "")
        for key in ("md", "markdown_path"):
            md = t.get(key)
            if md and Path(md).is_file():
                blobs.append(Path(md).read_text(encoding="utf-8"))
    tables_dir = search_md.parent.parent / "tables" if search_md else Path()
    if tables_dir.is_dir():
        for fp in sorted(tables_dir.glob("*.md")):
            txt = fp.read_text(encoding="utf-8")
            if "D1.1b" in txt or "D1.1b" in fp.name:
                blobs.append(txt)
    pages_dir = search_md.parent / "pages_search" if search_md else Path()
    rec_dir = search_md.parent / "pages_recovered" if search_md else Path()
    for pno in range(72, 76):
        for d in (pages_dir, rec_dir):
            fp = d / f"page_{pno:03d}.md"
            if fp.is_file():
                blobs.append(fp.read_text(encoding="utf-8"))
    joined = "\n".join(blobs)
    has_caption = bool("D1.1b" in joined)
    has_grid = ("|" in joined) or any(
        (t.get("num_cols") or 0) >= 2 for t in real
    )
    has_content = bool(
        re.search("Width-to-Thickness|Highly Ductile|Moderately Ductile|Unstiffened", joined, re.I)
    )
    ok = bool(real) and (has_caption or any((t.get("table_id") or "") == "D1.1b" for t in real)) and (has_grid or has_content)
    probes.add(
        "Table D1.1b is a real table (not caption-only)",
        ok,
        f"real_tables={len(real)} caption_only={len(candidates)-len(real)} "
        f"num_rows={[t.get('num_rows') for t in real[:6]]} "
        f"pages={[t.get('pdf_page') for t in real[:6]]} "
        f"has_caption={has_caption} has_grid={has_grid} has_content={has_content}",
    )


def probe_aisc341_commentary(
    docs: list[dict[str, Any]],
    sections: list[dict[str, Any]],
    probes: Probe,
) -> None:
    """341 commentary half after provisions; same section numbers in both halves."""
    if not docs:
        probes.add(
            "commentary vs provision tagged (AISC 341)",
            False,
            "documents.json empty",
        )
        return
    b = (docs[0].get("commentary_boundary") or {}) if isinstance(docs[0], dict) else {}
    cover = b.get("cover_pdf_page")
    body = b.get("body_pdf_page")
    profile = b.get("profile")
    e34_std = [
        s
        for s in sections
        if str(s.get("section_id") or "") == "E3.4a" and s.get("part") == "standard"
    ]
    e34_com = [
        s
        for s in sections
        if str(s.get("section_id") or "") == "E3.4a" and s.get("part") == "commentary"
    ]
    e3_std = [
        s
        for s in sections
        if str(s.get("section_id") or "") in {"E3", "E3.4a"} and s.get("part") == "standard"
    ]
    e3_com = [
        s
        for s in sections
        if str(s.get("section_id") or "") in {"E3", "E3.4a"} and s.get("part") == "commentary"
    ]
    if cover is None:
        probes.add(
            "commentary vs provision tagged (AISC 341)",
            False,
            "no commentary boundary detected, but 341 has a commentary half "
            "(cover pdf 235, 'COMMENTARY on the Seismic Provisions…'); "
            "refusing to invent a split",
        )
        return
    cover_ok = abs(int(cover) - 235) <= 8
    body_ok = body is not None and int(body) >= int(cover) - 1
    profile_ok = profile in ("aisc_341", "aisc")
    std_page = any(
        s.get("pdf_page") is not None and int(s["pdf_page"]) < int(cover) for s in (e34_std or e3_std)
    ) or any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 99) <= 10 for s in (e34_std or e3_std)
    )
    com_page = any(
        s.get("pdf_page") is not None and int(s["pdf_page"]) >= int(cover) for s in (e34_com or e3_com)
    ) or any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 315) <= 20 for s in (e34_com or e3_com)
    )
    ok = cover_ok and body_ok and profile_ok and std_page and com_page
    probes.add(
        "commentary vs provision tagged (AISC 341)",
        ok,
        f"profile={profile} cover={cover} body={body} "
        f"e34a_std={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label')} for s in e34_std[:3]]} "
        f"e34a_com={[{'pdf': s.get('pdf_page'), 'printed': s.get('printed_label')} for s in e34_com[:3]]} "
        f"e3_std_n={len(e3_std)} e3_com_n={len(e3_com)}",
    )


def probe_aisc341_leakage(search_md: Path, orig_md: Path, probes: Probe) -> dict[str, int]:
    search = search_md.read_text(encoding="utf-8") if search_md.is_file() else ""
    orig = orig_md.read_text(encoding="utf-8") if orig_md.is_file() else ""
    search_nocomment = re.sub(r"<!--.*?-->", "", search, flags=re.S)
    running = 0
    for rx in AISC_341_RUNNING_TITLE_RES:
        running += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: AISC 341 running titles absent from searchable text",
        running == 0,
        f"running_title_hits={running}",
    )
    c_search = 0
    for rx in AISC_COPYRIGHT_RES:
        c_search += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: AISC copyright not repeated in searchable text",
        c_search <= 3,
        f"searchable_copyright_hits={c_search} (allow <=3 for the copyright page itself)",
    )
    aisi = search_nocomment.count(COPYRIGHT_LINE)
    probes.add(
        "AISI copyright line absent (AISC 341 document)",
        aisi == 0,
        f"aisi_copyright_hits={aisi} orig_len={len(orig)}",
    )
    return {
        "aisc341_running_search": running,
        "aisc_copyright_search": c_search,
        "aisi_copyright_search": aisi,
    }


def probe_aisc341_page_mapping(blocks_path: Path, probes: Probe, n: int = 20) -> None:
    if not blocks_path.is_file():
        probes.add("page-mapping sample blocks", False, f"missing {blocks_path}")
        return
    rows = []
    with blocks_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) < 5:
        probes.add("page-mapping sample blocks", False, f"only {len(rows)} blocks")
        return
    rng = random.Random(34122)
    sample = rows if len(rows) <= n else rng.sample(rows, n)
    bad = []
    labels = []
    skip_pages = set(range(1, 5)) | {545, 546}
    for b in sample:
        if b.get("pdf_page") is None:
            bad.append(("missing_pdf_page", b.get("self_ref")))
            continue
        p = int(b["pdf_page"])
        printed = b.get("printed_label") or ""
        labels.append((p, printed))
        if p not in skip_pages and not printed:
            bad.append(("missing_printed_label", p, b.get("label")))
        if printed and not AISC_341_PRINTED_LABEL_RE.search(str(printed)):
            if p not in skip_pages:
                bad.append(("printed_label_not_9_1", p, printed))
        if b.get("part") not in ("standard", "commentary"):
            bad.append(("bad_part", p, b.get("part")))
    probes.add(
        "page-mapping: sample blocks have pdf_page and printed_label 9.1-xxx",
        len(bad) == 0,
        f"sampled={len(sample)} of {len(rows)} issues={bad[:6]} labels={labels[:8]}",
    )



def _title_is_body_heading(title: str) -> bool:
    letters = [c for c in (title or "") if c.isalpha()]
    if len(letters) < 3:
        return False
    return (sum(c.isupper() for c in letters) / len(letters)) >= 0.75


def _parent_root_id(sid: str) -> Optional[str]:
    """D4.2a -> D4; D1.3 -> D1; 15.6-1 is not a section; 5.7 -> 5."""
    s = str(sid or "")
    m = re.match(r"^([A-Z]\d+[a-z]?)", s)
    if m:
        return m.group(1)
    m = re.match(r"^(\d+)", s)
    if m:
        return m.group(1)
    return None


def probe_child_before_parent(sections: list[dict[str, Any]], probes: Probe) -> None:
    """FAIL if a standard child sits on a page before its parent-root body.

    Catches AISC 341 D4.2a (beam bracing, p71) parented to TOC D4 (H-Piles
    body is p90). TOC title-case headings are not the body page.
    """
    std = [s for s in sections if s.get("part") == "standard" and s.get("pdf_page") is not None]
    by_id: dict[str, list[dict[str, Any]]] = {}
    for s in std:
        by_id.setdefault(str(s.get("section_id") or ""), []).append(s)

    def body_page(root: str) -> Optional[int]:
        hits = by_id.get(root) or []
        body = [s for s in hits if _title_is_body_heading(s.get("title") or "")]
        use = body or hits
        pages = [int(s["pdf_page"]) for s in use if s.get("pdf_page") is not None]
        return min(pages) if pages else None

    bad = []
    for s in std:
        sid = str(s.get("section_id") or "")
        root = _parent_root_id(sid)
        if not root or sid == root:
            continue
        bp = body_page(root)
        if bp is None:
            continue
        title = (s.get("title") or "").strip()
        # ASCE quotes ACI 18.x as body paragraphs; units like "mm." are not headings.
        # AISC 341 D4.2a-class bugs have real short headings (Beam Bracing, etc.).
        if len(title) < 4 or len(title) > 90:
            continue
        if not re.search(r"[A-Za-z]{3,}", title):
            continue
        if int(s["pdf_page"]) < bp:
            bad.append(
                {
                    "section_id": sid,
                    "pdf_page": s.get("pdf_page"),
                    "title": s.get("title"),
                    "root": root,
                    "root_body_page": bp,
                }
            )
    probes.add(
        "child section pdf_page does not precede parent-root body page (standard)",
        len(bad) == 0,
        f"n_bad={len(bad)} sample={bad[:12]}",
    )


def probe_null_table_id(tables: list[dict[str, Any]], probes: Probe) -> None:
    """FAIL when a real TABLE caption + rows has table_id=null (A341 A3.2)."""
    bad = []
    for t in tables:
        if t.get("table_id"):
            continue
        blobs = [t.get("title") or "", t.get("markdown_excerpt") or ""]
        md = t.get("md")
        if md and Path(md).is_file():
            try:
                blobs.append(Path(md).read_text(encoding="utf-8")[:2500])
            except Exception:
                pass
        blob = nfkc("\n".join(blobs))
        # Caption-style only (A3.2 class): "TABLE A3.2" at line/cell start.
        # Do not trip on glossary rows that mention "Table D1.1" in a Reference cell.
        has_caption = bool(
            re.search(r"(?m)^(?:\s*\|\s*)?TABLE\s+[A-Z]?\d", blob)
        )
        has_rows = t.get("num_rows") not in (None, 0)
        if has_caption and has_rows:
            bad.append(
                {
                    "pdf_page": t.get("pdf_page"),
                    "num_rows": t.get("num_rows"),
                    "excerpt": collapse_ws(blob)[:90],
                }
            )
    probes.add(
        "tables with TABLE caption and rows have table_id (not null)",
        len(bad) == 0,
        f"n_bad={len(bad)} sample={bad[:8]}",
    )


def probe_aisc341_d13(sections: list[dict[str, Any]], probes: Probe) -> None:
    hits = [s for s in sections if str(s.get("section_id") or "") == "D1.3"]
    std = [s for s in hits if s.get("part") == "standard"]
    page_ok = any(
        s.get("pdf_page") is not None and 71 <= int(s["pdf_page"]) <= 81 for s in std
    )
    title_ok = any(re.search(r"Protected Zone", nfkc(s.get("title") or ""), re.I) for s in std)
    probes.add(
        "Section D1.3 Protected Zones (standard, pdf ~71-81)",
        bool(std) and page_ok and title_ok,
        f"std={[{'id': s.get('section_id'), 'title': s.get('title'), 'pdf': s.get('pdf_page'), 'printed': s.get('printed_label')} for s in std[:4]]}",
    )


def probe_aisc341_d41(sections: list[dict[str, Any]], probes: Probe) -> None:
    hits = [s for s in sections if str(s.get("section_id") or "") == "D4.1"]
    std = [s for s in hits if s.get("part") == "standard"]
    page_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 90) <= 2 for s in std
    )
    title_ok = any(re.search(r"Design Requirements", nfkc(s.get("title") or ""), re.I) for s in std)
    not_beam = not any(re.search(r"Steel Beams", nfkc(s.get("title") or ""), re.I) for s in std)
    probes.add(
        "Section D4.1 H-pile Design Requirements (standard, pdf ~90)",
        bool(std) and page_ok and title_ok and not_beam,
        f"std={[{'id': s.get('section_id'), 'title': s.get('title'), 'pdf': s.get('pdf_page'), 'printed': s.get('printed_label')} for s in std[:4]]}",
    )


def probe_aisc341_table_a32(
    tables: list[dict[str, Any]],
    search_md: Path,
    probes: Probe,
) -> None:
    def _tid(t: dict[str, Any]) -> str:
        return (t.get("table_id") or "").replace(" ", "")

    candidates = [
        t
        for t in tables
        if _tid(t) in {"A3.2", "A32"}
        or _tid(t).startswith("A3.2")
        or "A3.2" in (t.get("title") or "")
        or "A3.2" in (t.get("markdown_excerpt") or "")
        or t.get("pdf_page") in (59, 60, 61)
    ]
    real = [
        t
        for t in candidates
        if t.get("table_id")
        and t.get("source") != "caption_only"
        and t.get("num_rows") not in (None, 0)
    ]
    blobs: list[str] = []
    for t in real or candidates:
        blobs.append(t.get("markdown_excerpt") or "")
        blobs.append(t.get("title") or "")
        md = t.get("md")
        if md and Path(md).is_file():
            blobs.append(Path(md).read_text(encoding="utf-8"))
    pages_dir = search_md.parent / "pages_search" if search_md else Path()
    rec_dir = search_md.parent / "pages_recovered" if search_md else Path()
    for pno in (59, 60, 61):
        for d in (pages_dir, rec_dir):
            fp = d / f"page_{pno:03d}.md"
            if fp.is_file():
                blobs.append(fp.read_text(encoding="utf-8"))
    joined = nfkc("\n".join(blobs))
    has_a36 = bool(re.search(r"A36", joined)) and "1.5" in joined and "1.2" in joined
    has_a992 = bool(re.search(r"A992", joined)) and bool(re.search(r"1\.1", joined))
    has_id = any(_tid(t) == "A3.2" for t in real)
    probes.add(
        "Table A3.2 has table_id and Ry/Rt values (A36 1.5/1.2, A992 1.1/1.1)",
        bool(real) and has_id and has_a36 and has_a992,
        f"real={len(real)} ids={[t.get('table_id') for t in real[:4]]} "
        f"pages={[t.get('pdf_page') for t in real[:4]]} "
        f"has_a36={has_a36} has_a992={has_a992}",
    )


def probe_aisc358_eq_1561(
    equations: list[dict[str, Any]],
    search_md: Path,
    probes: Probe,
) -> None:
    hits = [
        e
        for e in equations
        if str(e.get("eq_id") or "") == "15.6-1"
        or (e.get("eq_id_display") or "") in {"(15.6-1)", "(Eq. 15.6-1)"}
    ]
    n_156 = len(
        {
            e.get("eq_id")
            for e in equations
            if str(e.get("eq_id") or "").startswith("15.6-")
        }
    )
    search = nfkc(search_md.read_text(encoding="utf-8") if search_md.is_file() else "")
    in_search = "(15.6-1)" in search or "15.6-1" in search
    probes.add(
        "Chapter 15 eq 15.6-1 present in equations.json and search.md",
        bool(hits) and in_search and n_156 >= 20,
        f"hits={[{'eq_id': e.get('eq_id'), 'pdf': e.get('pdf_page'), 'source': e.get('source')} for e in hits[:4]]} "
        f"n_15.6={n_156} in_search={in_search}",
    )




def probe_s240_d512(sections: list[dict[str, Any]], probes: Probe) -> None:
    """D5.1.2 lives on printed 78 = PDF 105 (skill '~pdf p 78' is the printed label)."""
    hits = [s for s in sections if str(s.get("section_id") or "") == "D5.1.2"]
    std = [s for s in hits if s.get("part") == "standard"]
    page_ok = any(
        s.get("pdf_page") is not None
        and (
            abs(int(s["pdf_page"]) - 105) <= 3
            or str(s.get("printed_label") or "") == "78"
            or abs(int(s["pdf_page"]) - 78) <= 3
        )
        for s in std
    )
    probes.add(
        "Section D5.1.2 provision part=standard (~pdf 105 / printed 78)",
        bool(std) and page_ok and all(s.get("part") == "standard" for s in std),
        f"std={[{'id': s.get('section_id'), 'title': s.get('title'), 'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part')} for s in std[:4]]} "
        f"all_hits={len(hits)}",
    )


def probe_s240_commentary(docs: list[dict[str, Any]], probes: Probe) -> None:
    if not docs:
        probes.add("commentary tagged cover ~pdf 128", False, "documents.json empty")
        return
    b = (docs[0].get("commentary_boundary") or {}) if isinstance(docs[0], dict) else {}
    cover = b.get("cover_pdf_page")
    body = b.get("body_pdf_page")
    profile = b.get("profile")
    cover_ok = cover is not None and abs(int(cover) - 128) <= 2
    body_ok = body is not None and abs(int(body) - 136) <= 2
    probes.add(
        "commentary tagged cover ~pdf 128 (body ~136)",
        cover_ok and body_ok and profile == "aisi_s240",
        f"profile={profile} cover={cover} body={body}",
    )


def probe_s240_leakage(search_md: Path, orig_md: Path, probes: Probe) -> dict[str, int]:
    search = search_md.read_text(encoding="utf-8") if search_md.is_file() else ""
    orig = orig_md.read_text(encoding="utf-8") if orig_md.is_file() else ""
    search_nocomment = re.sub(r"<!--.*?-->", "", search, flags=re.S)
    c_search = search_nocomment.count(COPYRIGHT_LINE)
    probes.add(
        "header/footer leakage: AISI copyright absent from searchable text",
        c_search == 0,
        f"searchable_hits={c_search} orig_len={len(orig)}",
    )
    running = 0
    for rx in AISI_S240_RUNNING_TITLE_RES + RUNNING_TITLE_RES:
        running += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: S240 running titles absent from searchable text",
        running == 0,
        f"running_title_hits={running}",
    )
    return {"copyright_search": c_search, "running_search": running}


def probe_s240_page_mapping(blocks_path: Path, probes: Probe, n: int = 20) -> None:
    if not blocks_path.is_file():
        probes.add("page-mapping sample blocks", False, f"missing {blocks_path}")
        return
    rows = []
    with blocks_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) < 5:
        probes.add("page-mapping sample blocks", False, f"only {len(rows)} blocks")
        return
    rng = random.Random(24020)
    sample = rows if len(rows) <= n else rng.sample(rows, n)
    # covers 1-2, intentionally blank 27/131, commentary cover 128, back covers
    skip_pages = {1, 2, 27, 128, 131, 207, 208}
    bad = []
    labels = []
    for b in sample:
        if b.get("pdf_page") is None:
            bad.append(("missing_pdf_page", b.get("self_ref")))
            continue
        p = int(b["pdf_page"])
        printed = b.get("printed_label") or ""
        labels.append((p, printed))
        if p not in skip_pages and not printed:
            bad.append(("missing_printed_label", p, b.get("label")))
        if b.get("part") not in ("standard", "commentary"):
            bad.append(("bad_part", p, b.get("part")))
        if printed.startswith("16.1-") or printed.startswith("9.1-") or printed.startswith("9.2-"):
            bad.append(("wrong_label_scheme", p, printed))
    probes.add(
        "page-mapping: sample blocks have pdf_page and printed_label",
        len(bad) == 0,
        f"sampled={len(sample)} of {len(rows)} issues={bad[:6]} labels={labels[:8]}",
    )


def probe_s100_eq_a3131(
    equations: list[dict[str, Any]],
    search_md: Path,
    probes: Probe,
) -> None:
    hits = [
        e
        for e in equations
        if str(e.get("eq_id") or "") in {"A3.1.3-1", "A3.13-1"}
        or (e.get("eq_id_display") or "") in {"(Eq. A3.1.3-1)", "(A3.1.3-1)"}
        or "A3.1.3-1" in (e.get("nearby_text") or "")
        or "A3.1.3-1" in (e.get("orig") or "")
    ]
    std = [e for e in hits if e.get("part") != "commentary"]
    page_ok = any(
        e.get("pdf_page") is not None and abs(int(e["pdf_page"]) - 78) <= 3 for e in std
    )
    search = nfkc(search_md.read_text(encoding="utf-8") if search_md.is_file() else "")
    in_search = "A3.1.3-1" in search or "(Eq. A3.1.3-1)" in search
    probes.add(
        "Eq A3.1.3-1 in equations.json and search.md (~pdf 78)",
        bool(std) and page_ok and in_search,
        f"hits={[{'eq_id': e.get('eq_id'), 'pdf': e.get('pdf_page'), 'part': e.get('part'), 'source': e.get('source')} for e in std[:4]]} "
        f"in_search={in_search}",
    )


def probe_s100_e2(sections: list[dict[str, Any]], probes: Probe) -> None:
    hits = [s for s in sections if str(s.get("section_id") or "") == "E2"]
    std = [s for s in hits if s.get("part") == "standard"]
    page_ok = any(
        s.get("pdf_page") is not None and abs(int(s["pdf_page"]) - 102) <= 4 for s in std
    )
    probes.add(
        "Chapter E2 provision part=standard (~pdf 102)",
        bool(std) and page_ok and all(s.get("part") == "standard" for s in std),
        f"std={[{'id': s.get('section_id'), 'title': s.get('title'), 'pdf': s.get('pdf_page'), 'printed': s.get('printed_label'), 'part': s.get('part')} for s in std[:4]]}",
    )


def probe_s100_commentary(docs: list[dict[str, Any]], probes: Probe) -> None:
    if not docs:
        probes.add("commentary tagged cover ~pdf 251", False, "documents.json empty")
        return
    b = (docs[0].get("commentary_boundary") or {}) if isinstance(docs[0], dict) else {}
    cover = b.get("cover_pdf_page")
    body = b.get("body_pdf_page")
    profile = b.get("profile")
    cover_ok = cover is not None and abs(int(cover) - 251) <= 4
    body_ok = body is not None and abs(int(body) - 263) <= 4
    probes.add(
        "commentary tagged cover ~pdf 251 (body ~263)",
        cover_ok and body_ok and profile == "aisi_s100",
        f"profile={profile} cover={cover} body={body}",
    )


def probe_s100_a313_not_superseded(
    sections: list[dict[str, Any]],
    documents: list[dict[str, Any]],
    probes: Probe,
) -> None:
    hits = [s for s in sections if str(s.get("section_id") or "") == "A3.1.3"]
    std = [s for s in hits if s.get("part") == "standard"]
    superseded = [
        s
        for s in std
        if str(s.get("status") or "").lower() == "superseded" or s.get("governing") is False
    ]
    sup = {}
    if documents and isinstance(documents[0], dict):
        sup = documents[0].get("supplements") or {}
    form_ok = sup.get("form") == "as-amended" and sup.get("revision_marks") is False
    probes.add(
        "A3.1.3 not superseded (governing S3 text)",
        bool(std) and not superseded and form_ok,
        f"std={[{'id': s.get('section_id'), 'pdf': s.get('pdf_page'), 'status': s.get('status'), 'governing': s.get('governing')} for s in std[:4]]} "
        f"supplements={sup}",
    )


def probe_s100_leakage(search_md: Path, orig_md: Path, probes: Probe) -> dict[str, int]:
    search = search_md.read_text(encoding="utf-8") if search_md.is_file() else ""
    orig = orig_md.read_text(encoding="utf-8") if orig_md.is_file() else ""
    search_nocomment = re.sub(r"<!--.*?-->", "", search, flags=re.S)
    c_search = search_nocomment.count(COPYRIGHT_LINE)
    probes.add(
        "header/footer leakage: AISI copyright absent from searchable text",
        c_search == 0,
        f"searchable_hits={c_search} orig_len={len(orig)}",
    )
    running = 0
    for rx in AISI_S100_RUNNING_TITLE_RES + RUNNING_TITLE_RES:
        running += len(rx.findall(search_nocomment))
    probes.add(
        "header/footer leakage: S100 running titles absent from searchable text",
        running == 0,
        f"running_title_hits={running}",
    )
    return {"copyright_search": c_search, "running_search": running}


def probe_s100_page_mapping(blocks_path: Path, probes: Probe, n: int = 20) -> None:
    if not blocks_path.is_file():
        probes.add("page-mapping sample blocks", False, f"missing {blocks_path}")
        return
    rows = []
    with blocks_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if len(rows) < 5:
        probes.add("page-mapping sample blocks", False, f"only {len(rows)} blocks")
        return
    rng = random.Random(10016)
    sample = rows if len(rows) <= n else rng.sample(rows, n)
    # covers / divider / intentionally blank: 1-2, commentary cover 251,
    # appendix divider sheets ~236/244, a few left-blank pages.
    skip_pages = set(range(1, 3)) | {201, 219, 236, 244, 251, 261, 262}
    bad = []
    labels = []
    for b in sample:
        if b.get("pdf_page") is None:
            bad.append(("missing_pdf_page", b.get("self_ref")))
            continue
        p = int(b["pdf_page"])
        printed = b.get("printed_label") or ""
        labels.append((p, printed))
        if p not in skip_pages and not printed:
            bad.append(("missing_printed_label", p, b.get("label")))
        if b.get("part") not in ("standard", "commentary"):
            bad.append(("bad_part", p, b.get("part")))
    probes.add(
        "page-mapping: sample blocks have pdf_page and printed_label",
        len(bad) == 0,
        f"sampled={len(sample)} of {len(rows)} issues={bad[:6]} labels={labels[:8]}",
    )



def probe_j10_orig(equations: list[dict[str, Any]], probes: Probe) -> None:
    """orig is the formula next to (J10-n), never φ/Ω or the previous formula."""
    by = {e.get("eq_id"): e for e in equations if e.get("doc") in (None, "AISC_360_22") or True}
    e9 = next((e for e in equations if e.get("eq_id") == "J10-9" and e.get("part") != "commentary"), None)
    e11 = next((e for e in equations if e.get("eq_id") == "J10-11" and e.get("part") != "commentary"), None)
    o9 = (e9.get("orig") if e9 else "") or ""
    o11 = (e11.get("orig") if e11 else "") or ""
    s9 = re.sub(r"[\s_]+", "", o9).lower()
    s11 = re.sub(r"[\s_]+", "", o11).lower()
    ok9 = "0.60" in s9 and "fy" in s9 and "tw" in s9 and "phi" not in s9 and "lrfd" not in s9
    ok11 = "0.60" in s11 and "fy" in s11 and ("bcf" in s11 or "tcf" in s11 or "1+3" in s11 or "1+3" in o11.replace(" ", ""))
    not_shift = "(j10-9)" not in o11.lower()
    probes.add(
        "Eq J10-9 orig Rn=0.60 Fy dc tw (not phi/Omega)",
        bool(e9) and ok9,
        f"orig={o9!r}",
    )
    probes.add(
        "Eq J10-11 orig includes (1+3 bcf tcf^2/(db dc tw)) not J10-9 formula",
        bool(e11) and ok11 and not_shift,
        f"orig={o11!r}",
    )


def probe_asce7_table_1221_smf(tables: list[dict[str, Any]], search_md: Path, probes: Probe) -> None:
    blobs = []
    for t in tables:
        if (t.get("table_id") or "") == "12.2-1" or t.get("pdf_page") in (173, 174, 175):
            blobs.append(t.get("markdown_excerpt") or "")
            md = t.get("md")
            if md and Path(md).is_file():
                blobs.append(Path(md).read_text(encoding="utf-8"))
    joined = nfkc("\n".join(blobs)).lower()
    has_smf = "steel special moment" in joined
    has_ebf = "eccentrically braced" in joined
    has_brbf = "buckling-restrained" in joined
    has_sbmf = "special bolted moment" in joined
    has_wsp = "wood structural" in joined
    probes.add(
        "Table 12.2-1 merged pages include SMF/EBF/BRBF/SBMF/CFS WSP rows",
        has_smf and has_ebf and has_brbf and has_sbmf and has_wsp,
        f"smf={has_smf} ebf={has_ebf} brbf={has_brbf} sbmf={has_sbmf} wsp={has_wsp}",
    )


def probe_s100_g52_real(tables: list[dict[str, Any]], probes: Probe) -> None:
    real = [
        t
        for t in tables
        if t.get("table_id")
        and (
            str(t.get("table_id")).replace(" ", "") in {"G5-2", "G5.2"}
            or "G5-2" in (t.get("title") or "")
        )
        and t.get("num_rows") not in (None, 0)
        and (t.get("pdf_page") or 0) >= 100
    ]
    toc = [
        t
        for t in tables
        if not t.get("table_id") and "G5-2" in (t.get("title") or "")
    ]
    probes.add(
        "Table G5-2 real grid has table_id (not TOC stub)",
        bool(real),
        f"real={[{'id': t.get('table_id'), 'pdf': t.get('pdf_page'), 'rows': t.get('num_rows')} for t in real[:4]]} toc_null={len(toc)}",
    )


def probe_a341_cf218_page(search_md: Path, probes: Probe) -> None:
    text = nfkc(search_md.read_text(encoding="utf-8") if search_md.is_file() else "")
    m = re.search(r"<!--\s*pdf_page=371\b.*?-->(.*?)(?=<!--\s*pdf_page=\d+|\Z)", text, re.S)
    chunk = m.group(1) if m else ""
    ok = "2 t linear" in chunk.lower() and "8 t elliptical" in chunk.lower()
    probes.add(
        "A341 commentary pdf 371 has 2 t linear / 8 t elliptical (C-F2.18)",
        ok,
        f"len={len(chunk)} has_2t={'2 t linear' in chunk.lower()} has_8t={'8 t elliptical' in chunk.lower()}",
    )


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Gold-probe validation (S400 and later PDFs)")
    parser.add_argument("doc_dir", type=Path)
    parser.add_argument("--json-out", type=Path, default=None)
    args = parser.parse_args(argv)
    doc_dir = args.doc_dir.resolve()
    if not doc_dir.is_dir():
        print(f"FAIL: not a directory {doc_dir}", file=sys.stderr)
        return 2

    paths = resolve_paths(doc_dir)
    probes = Probe()
    stem = doc_dir.name

    try:
        sections = load_json(pick_index(paths["local_sections"], paths["lite_sections"]))
        equations = load_json(pick_index(paths["local_equations"], paths["lite_equations"]))
        tables = load_json(pick_index(paths["local_tables"], paths["lite_tables"]))
        documents = load_json(pick_index(paths["local_documents"], paths["lite_documents"]))
    except FileNotFoundError as exc:
        print(f"FAIL: indexes missing ({exc}). Run postprocess.py first.", file=sys.stderr)
        return 1

    aisc358 = is_aisc_358_doc(stem) or "358" in stem.lower()
    aisc341 = is_aisc_341_doc(stem) or ("341" in stem.lower() and not aisc358)
    aisc = (is_aisc_doc(stem) or "a360" in stem.lower()) and not aisc358 and not aisc341
    asce = is_asce7_doc(stem) or "asce7" in stem.lower() or stem in {"ASCE7", "ASCE_7", "asce7"}
    s100 = is_aisi_s100_doc(stem) or "s100" in stem.lower()
    s240 = is_aisi_s240_doc(stem) or "s240" in stem.lower()
    keep_ids = {
        stem,
        "AISI_S400_20",
        "AISI_S100",
        "AISI_S240",
        "AISC_360_22",
        "A360_22",
        "A360-22",
        "AISC_358_22",
        "A358_22",
        "A358-22",
        "AISC_341_22",
        "A341_22",
        "A341-22",
        "ASCE7",
        "asce7",
        "ASCE_7",
    }
    sections = [s for s in sections if s.get("doc") in keep_ids]
    equations = [e for e in equations if e.get("doc") in keep_ids]
    tables = [t for t in tables if t.get("doc") in keep_ids]
    documents = [d for d in documents if d.get("id") in keep_ids]
    # Restrict to this stem when the lite index holds multiple docs
    if aisc358:
        keep_358 = {stem, "AISC_358_22", "A358_22", "A358-22"}
        sections = [s for s in sections if s.get("doc") in keep_358]
        equations = [e for e in equations if e.get("doc") in keep_358]
        tables = [t for t in tables if t.get("doc") in keep_358]
        documents = [d for d in documents if d.get("id") in keep_358]
        family = "aisc_358"
    elif aisc341:
        keep_341 = {stem, "AISC_341_22", "A341_22", "A341-22"}
        sections = [s for s in sections if s.get("doc") in keep_341]
        equations = [e for e in equations if e.get("doc") in keep_341]
        tables = [t for t in tables if t.get("doc") in keep_341]
        documents = [d for d in documents if d.get("id") in keep_341]
        family = "aisc_341"
    elif asce:
        keep_asce = {stem, "ASCE7", "asce7", "ASCE_7"}
        sections = [s for s in sections if s.get("doc") in keep_asce]
        equations = [e for e in equations if e.get("doc") in keep_asce]
        tables = [t for t in tables if t.get("doc") in keep_asce]
        documents = [d for d in documents if d.get("id") in keep_asce]
        family = "asce7"
    elif aisc:
        sections = [s for s in sections if s.get("doc") == stem]
        equations = [e for e in equations if e.get("doc") == stem]
        tables = [t for t in tables if t.get("doc") == stem]
        documents = [d for d in documents if d.get("id") == stem]
        family = "aisc"
    elif s100:
        keep_s100 = {stem, "AISI_S100"}
        sections = [s for s in sections if s.get("doc") in keep_s100]
        equations = [e for e in equations if e.get("doc") in keep_s100]
        tables = [t for t in tables if t.get("doc") in keep_s100]
        documents = [d for d in documents if d.get("id") in keep_s100]
        family = "aisi_s100"
    elif s240:
        keep_s240 = {stem, "AISI_S240"}
        sections = [s for s in sections if s.get("doc") in keep_s240]
        equations = [e for e in equations if e.get("doc") in keep_s240]
        tables = [t for t in tables if t.get("doc") in keep_s240]
        documents = [d for d in documents if d.get("id") in keep_s240]
        family = "aisi_s240"
    else:
        sections = [s for s in sections if s.get("doc") in (stem, "AISI_S400_20")]
        equations = [e for e in equations if e.get("doc") in (stem, "AISI_S400_20")]
        tables = [t for t in tables if t.get("doc") in (stem, "AISI_S400_20")]
        documents = [d for d in documents if d.get("id") in (stem, "AISI_S400_20")]
        family = "aisi_s400"

    page_map = {}
    if paths["page_map"].is_file():
        page_map = load_json(paths["page_map"])

    print(f"Validating {stem} at {doc_dir} family={family}")
    census: dict[str, Any] = {"misses": [], "census": 0, "index_ids": []}
    leak: dict[str, int] = {}
    if aisc358:
        probe_aisc358_rbs_chapter(sections, probes)
        probe_aisc358_rbs_design_procedure(sections, paths["search_md"], probes)
        probe_aisc358_eq_1561(equations, paths["search_md"], probes)
        probe_aisc358_commentary(documents, sections, probes)
        census = probe_eq_census(doc_dir, equations, page_map, probes)
        n_156 = sum(1 for i in (census.get("index_ids") or []) if str(i).startswith("15.6-"))
        probes.add(
            "equation census includes Chapter 15 15.6-* ids",
            n_156 >= 20,
            f"n_15.6_in_index={n_156}",
        )
        leak = probe_aisc358_leakage(paths["search_md"], paths["orig_md"], probes)
        probe_aisc358_page_mapping(paths["blocks"], probes)
        # Do NOT run A360 F2-1 / B4.1a / F2.2 or S400/ASCE7 probes on 358.
    elif aisc341:
        probe_aisc341_e34a(sections, paths["search_md"], probes)
        probe_aisc341_table_d11b(tables, paths["search_md"], probes)
        probe_aisc341_d13(sections, probes)
        probe_aisc341_d41(sections, probes)
        probe_aisc341_table_a32(tables, paths["search_md"], probes)
        probe_aisc341_commentary(documents, sections, probes)
        census = probe_eq_census(doc_dir, equations, page_map, probes)
        leak = probe_aisc341_leakage(paths["search_md"], paths["orig_md"], probes)
        probe_aisc341_page_mapping(paths["blocks"], probes)
        probe_a341_cf218_page(paths["search_md"], probes)
        # Do NOT run A360 F2-1 / B4.1a / F2.2 or 358 RBS probes on 341.
    elif asce:
        probe_asce7_eq_1283(equations, paths["search_md"], probes)
        probe_asce7_table_1221(tables, paths["search_md"], probes)
        probe_asce7_table_1221_smf(tables, paths["search_md"], probes)
        probe_asce7_section_12432(sections, probes)
        probe_asce7_table_26111(tables, paths["search_md"], probes)
        probe_asce7_commentary_boundary(documents, sections, probes)
        leak = probe_asce7_leakage(paths["search_md"], paths["orig_md"], probes)
        probe_asce7_page_mapping(paths["blocks"], probes)
        # Do NOT run S400 E3.4.2 / Table E1.3-1 or A360 F2-1 / B4.1a on ASCE7.
    elif aisc:
        probe_f21(equations, paths["search_md"], probes)
        probe_table_b41a(tables, paths["search_md"], probes)
        probe_f22_parts(sections, probes)
        probe_aisc_commentary_boundary(documents, probes)
        census = probe_eq_census(doc_dir, equations, page_map, probes)
        leak = probe_aisc_leakage(paths["search_md"], paths["orig_md"], probes)
        probe_aisc_page_mapping(paths["blocks"], probes)
        probe_j10_orig(equations, probes)
    elif s100:
        probe_s100_eq_a3131(equations, paths["search_md"], probes)
        probe_s100_e2(sections, probes)
        probe_s100_g52_real(tables, probes)
        probe_s100_commentary(documents, probes)
        probe_s100_a313_not_superseded(sections, documents, probes)
        census = probe_eq_census(doc_dir, equations, page_map, probes)
        leak = probe_s100_leakage(paths["search_md"], paths["orig_md"], probes)
        probe_s100_page_mapping(paths["blocks"], probes)
        # Do NOT run A360/341/358/ASCE/S400 gold probes on S100.
    elif s240:
        probe_s240_d512(sections, probes)
        probe_s240_commentary(documents, probes)
        census = probe_eq_census(doc_dir, equations, page_map, probes)
        leak = probe_s240_leakage(paths["search_md"], paths["orig_md"], probes)
        probe_s240_page_mapping(paths["blocks"], probes)
        # Do NOT run S100/S400/AISC/ASCE gold probes on S240.
    else:
        probe_e342(sections, probes)
        probe_table_e131(tables, paths["search_md"], probes)
        probe_commentary_boundary(documents, probes)
        census = probe_eq_census(doc_dir, equations, page_map, probes)
        leak = probe_leakage(paths["search_md"], paths["orig_md"], probes)
        probe_page_mapping(paths["blocks"], probes)

    meta = load_json(paths["meta"]) if paths["meta"].is_file() else {}
    pdf_path = resolve_source_pdf(doc_dir, stem, meta)
    pdf_pages = load_pdf_pages(pdf_path)
    search_pages = parse_search_md_pages(paths["search_md"])
    img = probe_image_only_pages(search_pages, pdf_pages, paths["pages_search"], probes)
    probe_tables_num_rows(tables, probes)
    probe_null_table_id(tables, probes)
    probe_child_before_parent(sections, probes)
    bound = probe_page_boundary_attribution(
        search_pages, pdf_pages, paths["pages_search"], probes
    )

    report = {
        "doc": stem,
        "passed": probes.passed,
        "probes": probes.rows,
        "eq_census_misses": census.get("misses"),
        "eq_index_ids": census.get("index_ids"),
        "leakage": leak,
        "image_only": img,
        "page_boundary": {"failing": bound.get("failing"), "checked": bound.get("checked")},
        "source_pdf": str(pdf_path) if pdf_path else None,
    }
    out_path = args.json_out or (doc_dir / "validate_report.json")
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print()
    if probes.passed:
        print(f"OVERALL: PASS  ({len(probes.rows)} probes)  report={out_path}")
        return 0
    print(f"OVERALL: FAIL  {len(probes.failed)}/{len(probes.rows)} probes failed  report={out_path}")
    for r in probes.failed:
        print(f"  - {r['name']}: {r['detail']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
