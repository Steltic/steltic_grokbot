#!/usr/bin/env python3
"""Recover image-only / caption-only table pages.

Default paths target AISC 360-22. Pass --pdf --doc-dir --stem --pages for
other documents (ASCE7, S400, ...).


Path A: Docling TableFormer ACCURATE on 300 dpi rasters (precomputed).
Path B: Docling/RapidOCR markdown when no table grid.
Path C: pdftotext -layout (always spliced for searchable tokens).

Writes markdown/pages_recovered and tables/recovered_index.json.
Does not modify the original PDF.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Optional

DEFAULT_DOC_DIR = Path("/workspace/engineering_rag/documents/standards/AISC_360_22")
DEFAULT_PDF = Path("/workspace/standards/A360-22.pdf")
DEFAULT_DOCLING = Path("/tmp/a360_docling")
DEFAULT_STEM = "AISC_360_22"

# Runtime paths — set in main() / apply_config().
DOC_DIR = DEFAULT_DOC_DIR
PDF = DEFAULT_PDF
DOCLING = DEFAULT_DOCLING
STEM = DEFAULT_STEM

# Image-only QA pages + caption_only pages that need a real grid.
PAGES = [
    89, 90, 91, 200, 229, 231, 232, 234, 235, 236, 237, 238, 239, 241,
    260, 279, 281, 283, 285, 287, 289, 291, 293, 295, 297, 320, 427, 548, 597, 637,
]

PAGE_TABLE_ID = {
    89: "B4.1a",
    90: "B4.1b",
    91: "B4.1b",
    200: "J2.5",
    229: "K2.1",
    231: "K3.1",
    232: "K3.1A",
    234: "K3.2A",
    235: "K4.1",
    236: "K4.1A",
    237: "K4.2",
    238: "K4.2A",
    239: "K5.1",
    241: "K5.2",
    260: "N5.6-3",
    279: "A-3.1",
    281: "A-3.1",
    283: "A-3.1",
    285: "A-3.1",
    287: "A-3.1",
    289: "A-3.1",
    291: "A-3.1",
    293: "A-3.1",
    295: "A-3.1",
    297: "A-3.1",
    320: "A-4.3.1",
    427: "C-E4.1",
    548: "J2.3",
    597: "C-K1.1",
    637: "C-N5.6-2",
}

FURNITURE_LINE_RES = [
    re.compile(r"Specification for Structural Steel Buildings", re.I),
    re.compile(r"American Institute of Steel Construction", re.I),
    re.compile(r"Part\s+16\.1\b", re.I),
    re.compile(r"\.indd\b", re.I),
    re.compile(r"Smarter\.\s*Stronger\.\s*Steel", re.I),
    re.compile(r"Downloaded from ascelibrary\.org", re.I),
    re.compile(r"Copyright ASCE; all rights reserved", re.I),
    re.compile(r"Prequalified Connections for Special and Intermediate Steel", re.I),
    re.compile(r"Moment Frames for Seismic Applications", re.I),
    re.compile(r"^\s*9\.2\s*[-–—]\s*[ivxlcdm0-9]+\s*$", re.I),
    re.compile(r"^Comm\.\s+\d", re.I),
    re.compile(r"Seismic Provisions for Structural Steel Buildings", re.I),
    re.compile(r"^\s*9\.1\s*[-–—]\s*[ivxlcdm0-9]+\s*$", re.I),
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
    re.compile(
        r"AISI\s*S100-16(?:-C)?(?:\s*\(R?2020\))?(?:\s*w/S3-22)?\s*$",
        re.I,
    ),
    re.compile(r"This Page is Intentionally Left Blank", re.I),
    re.compile(r"This document is copyrighted by AISI", re.I),
    re.compile(
        r"North American Standard [Ff]or Cold-Formed Steel Structural Framing, 2020 Edition",
        re.I,
    ),
    re.compile(
        r"Commentary on the North American Standard for Cold-Formed Steel Structural Framing, 2020 Edition",
        re.I,
    ),
    re.compile(r"AISI\s+S240-20(?:-C)?\s*$", re.I),
    re.compile(r"^\s*(?:[A-Z]-)?\d+(?:-\d+)?\s+Appendix\s+", re.I),
    re.compile(r"^\s*(?:[A-Z]-)?\d+(?:-\d+)?\s+Chapter\s+", re.I),
]
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
TABLE_ID_RE = re.compile(r"Table\s+((?:C-)?[A-Z]?\d[\w.\-]*[0-9A-Za-z])", re.I)

B41A_SYMBOLIC = """
Limiting width-to-thickness ratios λr (PDF text layer; stacked radical E/Fy):

| Case | Description of Element | Width-to-Thickness Ratio | λr (nonslender/slender) |
|---:|---|---|---|
| 1 | Flanges of rolled I-shaped sections; plates projecting from rolled I-shaped sections; outstanding legs of pairs of angles connected with continuous contact; flanges of channels; flanges of tees | b/t | 0.56√(E/Fy) |
| 2 | Flanges of built-up I-shaped sections; plates or angle legs projecting from built-up I-shaped sections | b/t | 0.64√(kc E/Fy) |
| 3 | Legs of single angles; legs of double angles with separators; all other unstiffened elements | b/t | 0.45√(E/Fy) |
| 4 | Stems of tees | d/t | 0.75√(E/Fy) |
| 5 | Webs of doubly symmetric rolled and built-up I-shaped sections and channels | h/tw | 1.49√(E/Fy) |
| 6 | Walls of rectangular HSS | b/t | 1.40√(E/Fy) |
| 7 | Flange cover plates between lines of fasteners or welds | b/t | 1.40√(E/Fy) |
| 8 | All other stiffened elements | b/t | 1.49√(E/Fy) |
| 9 | Round HSS | D/t | 0.11√(E/Fy) |

E = modulus of elasticity of steel = 29,000 ksi (200 000 MPa)
Fy = specified minimum yield stress, ksi (MPa)
[a] kc = 4/(h/tw), but shall not be taken as less than 0.35 nor greater than 0.76 for calculation purposes.
"""

B41B_P90_SYMBOLIC = """
Limiting width-to-thickness ratios λp / λr (PDF text layer; stacked radical E/Fy):

| Case | Description of Element | Width-to-Thickness Ratio | λp (compact/noncompact) | λr (noncompact/slender) |
|---:|---|---|---|---|
| 10 | Flanges of rolled I-shaped sections; flanges of channels; flanges of tees | b/t | 0.38√(E/Fy) | 1.0√(E/Fy) |
| 11 | Flanges of doubly and singly symmetric I-shaped built-up sections | b/t | 0.38√(E/Fy) | 0.95√(kc E/FL) |
| 12 | Legs of single angles | b/t | 0.54√(E/Fy) | 0.91√(E/Fy) |
| 13 | Flanges of all I-shaped sections and channels in flexure about the minor axis | b/t | 0.38√(E/Fy) | 1.0√(E/Fy) |
| 14 | Stems of tees | d/t | 0.84√(E/Fy) | 1.52√(E/Fy) |
"""

B41B_P91_SYMBOLIC = """
Limiting width-to-thickness ratios λp / λr (PDF text layer; stacked radical E/Fy):

| Case | Description of Element | Width-to-Thickness Ratio | λp (compact/noncompact) | λr (noncompact/slender) |
|---:|---|---|---|---|
| 15 | Webs of doubly symmetric I-shaped sections and channels | h/tw | 3.76√(E/Fy) | 5.70√(E/Fy) |
| 16 | Webs of singly symmetric I-shaped sections | hc/tw | (hc/hp)√(E/Fy) (0.54 Mp/My − 0.09) ≤ λr | 5.70√(E/Fy) |
| 17 | Flanges of rectangular HSS | b/t | 1.12√(E/Fy) | 1.40√(E/Fy) |
| 18 | Flange cover plates between lines of fasteners or welds | b/t | 1.12√(E/Fy) | 1.40√(E/Fy) |
| 19 | Webs of rectangular HSS and box sections | h/t | 2.42√(E/Fy) | 5.70√(E/Fy) |
| 20 | Round HSS | D/t | 0.07√(E/Fy) | 0.31√(E/Fy) |
| 21 | Flanges of box sections | b/t | 1.12√(E/Fy) | 1.49√(E/Fy) |
"""


RUN_RX = re.compile(
    r"Specification for Structural Steel Buildings[ \t]*,?[ \t]*August 1,[ \t]*2022[^\n]*",
    re.I,
)
AISC_LINE_RX = re.compile(r"AMERICAN INSTITUTE OF STEEL CONSTRUCTION[^\n]*", re.I)


def strip_running_titles(text: str) -> str:
    text = RUN_RX.sub("", text or "")
    text = AISC_LINE_RX.sub("", text)
    return text


def strip_furniture(page_text: str) -> str:
    lines = []
    for line in (page_text or "").splitlines():
        if any(rx.search(line) for rx in FURNITURE_LINE_RES):
            continue
        if re.match(r"^\s*\[?Sect\.\s+[A-Z0-9.\-]+\]?\s*$", line, re.I):
            continue
        if re.match(r"^\s*16\.1\s*-+\s*[ivxlcdm0-9]+\s*$", line, re.I):
            continue
        if re.match(r"^\s*9\.2\s*[-–—]\s*[ivxlcdm0-9]+\s*$", line, re.I):
            continue
        if re.match(r"^\s*9\.1\s*[-–—]\s*[ivxlcdm0-9]+\s*$", line, re.I):
            continue
        if re.match(r"^\s*\[Comm\.", line, re.I):
            continue
        lines.append(line.rstrip())
    # drop leading/trailing blank runs
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def pdftotext_page(pno: int) -> str:
    r = subprocess.run(
        ["pdftotext", "-layout", "-f", str(pno), "-l", str(pno), str(PDF), "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    return r.stdout or ""


def is_comment_only(md: str) -> bool:
    body = HTML_COMMENT_RE.sub("", md or "").strip()
    return len(body) == 0


def md_table_stats(md: str) -> tuple[int, int]:
    rows = []
    cols = 0
    for ln in (md or "").splitlines():
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "") or "-") or set(c) <= set("-: ") for c in cells):
            continue
        rows.append(cells)
        cols = max(cols, len(cells))
    return len(rows), cols


def recover_table_id(blob: str, fallback: Optional[str]) -> Optional[str]:
    m = TABLE_ID_RE.search(blob or "")
    if m:
        tid = re.sub(r"\s+", "", m.group(1))
        return re.sub(r"-{2,}", "-", tid)
    return fallback


def load_docling(pno: int) -> dict[str, Any]:
    jp = DOCLING / f"p-{pno:03d}.json"
    if not jp.is_file():
        return {}
    try:
        return json.loads(jp.read_text(encoding="utf-8"))
    except Exception:
        return {}


def write_table_files(
    tables_dir: Path,
    pno: int,
    table_id: Optional[str],
    title: str,
    md: str,
    num_rows: int,
    num_cols: int,
    source: str,
) -> dict[str, Any]:
    tables_dir.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", table_id or "table")[:40].strip("_")
    base = f"{STEM}_recovered_p{pno:03d}_{safe}"
    md_path = tables_dir / f"{base}.md"
    csv_path = tables_dir / f"{base}.csv"
    json_path = tables_dir / f"{base}.json"
    md_path.write_text(md or "", encoding="utf-8")
    # crude csv: first markdown table
    rows = []
    for ln in (md or "").splitlines():
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(set(c.replace(":", "").replace("-", "").replace(" ", "")) == set() for c in cells):
            continue
        rows.append(cells)
    if rows:
        width = max(len(r) for r in rows)
        with csv_path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            for r in rows:
                w.writerow(r + [""] * (width - len(r)))
    else:
        csv_path = None
    payload = {
        "pdf_page": pno,
        "table_id": table_id,
        "title": title,
        "num_rows": num_rows,
        "num_cols": num_cols,
        "source": source,
        "markdown": md,
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {
        "table_id": table_id,
        "title": title,
        "pdf_page": pno,
        "pdf_pages": [pno],
        "num_rows": num_rows,
        "num_cols": num_cols,
        "md": str(md_path),
        "csv": str(csv_path) if csv_path else None,
        "json": str(json_path),
        "source": source,
        "markdown": md,
    }


def page_body(pno: int, pdf_text: str) -> tuple[str, str, list[dict[str, Any]]]:
    """Return (search_body, source_tag, table_records_partial)."""
    dl = load_docling(pno)
    md = (dl.get("markdown") or "").strip()
    tables = dl.get("tables") or []
    layout = strip_furniture(pdf_text)
    source = "pdftotext"
    parts: list[str] = []

    good_tables = [t for t in tables if (t.get("num_rows") or 0) >= 2 and (t.get("markdown") or "").count("|") >= 4]
    if good_tables:
        source = "tableformer_image"
        for t in good_tables:
            parts.append((t.get("markdown") or "").rstrip())
        # keep non-table Docling prose (captions, notes) if any
        leftover = HTML_COMMENT_RE.sub("", md).strip()
        if leftover and leftover not in "\n".join(parts):
            # avoid duplicating the same grid
            if leftover[:80] not in "\n".join(parts):
                parts.append(leftover)
    elif md and not is_comment_only(md):
        source = "rapidocr_image"
        parts.append(HTML_COMMENT_RE.sub("", md).strip())
    else:
        source = "pdftotext"
        parts.append(layout)

    if STEM in {"AISC_360_22", "A360_22"}:
        if pno == 89:
            parts.append(B41A_SYMBOLIC.strip())
        elif pno == 90:
            parts.append(B41B_P90_SYMBOLIC.strip())
        elif pno == 91:
            parts.append(B41B_P91_SYMBOLIC.strip())

    # Always splice furniture-stripped PDF text layer for token attribution
    # unless this page already IS the pdftotext body.
    if source != "pdftotext" and layout:
        parts.append("PDF text layer:\n\n" + layout)

    body = "\n\n".join(p for p in parts if p).strip() + "\n"
    body = strip_running_titles(body)
    return body, source, good_tables


def parse_pages_arg(text: Optional[str], default: list[int]) -> list[int]:
    if not text:
        return list(default)
    out: list[int] = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            lo, hi = int(a), int(b)
            if hi < lo:
                lo, hi = hi, lo
            out.extend(range(lo, hi + 1))
        else:
            out.append(int(part))
    # unique, stable order
    seen = set()
    uniq = []
    for n in out:
        if n not in seen:
            seen.add(n)
            uniq.append(n)
    return uniq


def apply_config(*, pdf: Path, doc_dir: Path, stem: str, docling: Path) -> None:
    global DOC_DIR, PDF, DOCLING, STEM
    DOC_DIR = doc_dir
    PDF = pdf
    DOCLING = docling
    STEM = stem


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Recover image-only / caption-only table pages")
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--doc-dir", type=Path, default=DEFAULT_DOC_DIR)
    parser.add_argument("--stem", default=DEFAULT_STEM)
    parser.add_argument("--pages", default=None, help="Comma/range list, e.g. 89,90,173-176")
    parser.add_argument("--docling-dir", type=Path, default=DEFAULT_DOCLING)
    args = parser.parse_args(argv)
    apply_config(pdf=args.pdf, doc_dir=args.doc_dir, stem=args.stem, docling=args.docling_dir)
    pages = parse_pages_arg(args.pages, PAGES)

    recovered_dir = DOC_DIR / "markdown" / "pages_recovered"
    recovered_dir.mkdir(parents=True, exist_ok=True)
    tables_dir = DOC_DIR / "tables"
    index: list[dict[str, Any]] = []

    extra_ids = {}
    if STEM in {"AISC_360_22", "A360_22"}:
        extra_ids = {
            229: [("K2.1A", "TABLE K2.1A Limits of Applicability of Table K2.1")],
            637: [("C-N5.6-3", "TABLE C-N5.6-3")],
        }
    page_table_id = PAGE_TABLE_ID if STEM in {"AISC_360_22", "A360_22"} else {}

    for pno in pages:
        pdf_text = pdftotext_page(pno)
        body, source, good_tables = page_body(pno, pdf_text)
        (recovered_dir / f"page_{pno:03d}.md").write_text(body, encoding="utf-8")

        fallback_id = page_table_id.get(pno)
        title = ""
        m = re.search(r"TABLE\s+[A-Z0-9.\-]+[^\n]*", body, re.I)
        if m:
            title = re.sub(r"\s+", " ", m.group(0)).strip()
        tid = recover_table_id(body, fallback_id)

        if good_tables:
            for i, t in enumerate(good_tables, 1):
                tmd = t.get("markdown") or ""
                nrows = t.get("num_rows") or md_table_stats(tmd)[0]
                ncols = t.get("num_cols") or md_table_stats(tmd)[1]
                use_md = tmd
                if STEM in {"AISC_360_22", "A360_22"} and pno in (89, 90, 91):
                    # keep TableFormer grid + symbolic λ columns in the shipped table file
                    if pno == 89:
                        use_md = tmd.rstrip() + "\n\n" + B41A_SYMBOLIC.strip() + "\n"
                    elif pno == 90:
                        use_md = tmd.rstrip() + "\n\n" + B41B_P90_SYMBOLIC.strip() + "\n"
                    else:
                        use_md = tmd.rstrip() + "\n\n" + B41B_P91_SYMBOLIC.strip() + "\n"
                    nrows = max(nrows, md_table_stats(use_md)[0])
                    ncols = max(ncols or 0, md_table_stats(use_md)[1])
                this_id = tid if i == 1 else recover_table_id(tmd, tid)
                rec = write_table_files(
                    tables_dir,
                    pno,
                    this_id,
                    title or f"Table {this_id}" if this_id else None,
                    use_md,
                    int(nrows),
                    int(ncols or 0),
                    source,
                )
                index.append(rec)
        else:
            nrows, ncols = md_table_stats(body)
            has_table = bool(tid) or bool(re.search(r"\bTABLE\s+", body or "", re.I))
            if has_table:
                if nrows < 2:
                    content_lines = [ln for ln in strip_furniture(pdf_text).splitlines() if ln.strip()]
                    nrows = max(1, len(content_lines))
                    ncols = max(ncols, 1)
                rec = write_table_files(
                    tables_dir,
                    pno,
                    tid,
                    title or (f"Table {tid}" if tid else None),
                    body,
                    int(nrows),
                    int(ncols or 1),
                    source,
                )
                index.append(rec)

        for extra_id, extra_title in extra_ids.get(pno, []):
            if any((r.get("table_id") or "") == extra_id for r in index if r.get("pdf_page") == pno):
                continue
            # second table on the same recovered page; point at the same markdown
            base = [r for r in index if r.get("pdf_page") == pno]
            if not base:
                continue
            clone = dict(base[0])
            clone["table_id"] = extra_id
            clone["title"] = extra_title
            index.append(clone)

        print(f"p{pno} source={source} tables={len(good_tables)} body={len(body)} id={tid}")

    idx_path = tables_dir / "recovered_index.json"
    existing: list[dict[str, Any]] = []
    if idx_path.is_file():
        try:
            existing = json.loads(idx_path.read_text(encoding="utf-8"))
            if not isinstance(existing, list):
                existing = []
        except Exception:
            existing = []
    new_keys = {
        (int(rec.get("pdf_page") or 0), rec.get("table_id"))
        for rec in index
    }
    kept = [
        rec for rec in existing
        if (int(rec.get("pdf_page") or 0), rec.get("table_id")) not in new_keys
    ]
    merged = kept + index
    idx_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {idx_path} n={len(merged)} (kept {len(kept)} + new {len(index)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
