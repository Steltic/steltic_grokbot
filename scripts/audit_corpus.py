#!/usr/bin/env python3
"""Audit the converted specification corpus for the faults that are invisible to a query.

Every check here is one that, on 2026-09-18, was found by hand after four rounds of retrieval
fixes had been applied to an index whose records were wrong. A query cannot see any of them: the
index answered, the answers were plausible, and the clause under an AISC 358 heading was AISC
341's. `build_index` runs this at the end of every build and prints the summary; the hub's
*Audit corpus* tab runs it on demand; `skills/CHECK-AND-CLEAN-CONVERSIONS.md` tells an LLM what
to do about each finding.

Severity:
  FAIL  the index is wrong and the design agents will be served wrong text -- fix before use
  WARN  coverage or hygiene is poor; retrieval works but misses or shows noise
  INFO  worth knowing, nothing to do

Usage:
  python scripts/audit_corpus.py --root <workspace> [--json-out F] [--md-out F] [--no-smoke]

Exit status 1 when any FAIL is present, else 0. Reports go to <root>/indexes/audit_report.{json,md}
unless told otherwise.
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

P2_COLLECTIONS = {"opensees", "examples", "steel_design_examples"}
CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
ROMAN_RE = re.compile(r"^[ivxlcdm]+$", re.I)
LIGATURE_SPLIT_RE = re.compile(r"\b[A-Za-z]+ (?:fi|fl|ffi|ffl) [a-z]+\b")
WATERMARK_RE = re.compile(r"^(?:Downloaded from|Copyright .*all rights reserved)", re.I | re.M)
ID_SHAPE_RE = re.compile(r"^(C-)?([A-N]\d*(\.\d+)*[a-z]?|\d+(\.\d+)*[a-z]?|C\d+(\.\d+)*[a-z]?|App(?:endix)?\s*[A-Z0-9]+|A-\d+(\.\d+)*)$")
EMBEDDED_ID_RE = re.compile(r"\(((?:C-)?[A-Z]\d+(?:\.\d+)*-\d+[a-z]?)\)")
EMBEDDED_NUM_ID_RE = re.compile(r"\((C?\d{1,2}(?:\.\d+)*-\d{1,3}[a-z]?)\)$")   # (5.7-1), (7-1): only at the end
RELATION_RE = re.compile(r"=|\\le|\\ge|\\leq|\\geq|<|>|\\approx|\\neq")
CAPTION_RE = re.compile(r"^\s*(?:#+\s*)?(?:\|\s*)?TABLE\s+((?:C-)?[A-Z]?\d+(?:\s?\.\d+)*[A-Za-z]?(?:-\d+[A-Za-z]?)?)\b", re.I | re.M)
PDF_EQ_ID_RE = re.compile(r"\(((?:C-?)?[A-Z]?\d{1,2}(?:\.\d+)*-\d{1,3}[a-z]?)\)")


class Findings:
    def __init__(self) -> None:
        self.items: list[dict[str, Any]] = []

    def add(self, level: str, doc: str, code: str, msg: str, **details: Any) -> None:
        self.items.append({"level": level, "doc": doc, "code": code, "message": msg, **details})

    def count(self, level: str) -> int:
        return sum(1 for f in self.items if f["level"] == level)


def load_json(p: Path) -> Any:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def roman_tail(label: Any) -> bool:
    tail = str(label or "").strip().split("-")[-1]
    return bool(tail) and bool(ROMAN_RE.fullmatch(tail))


def printed_id_in_latex(latex: Optional[str]) -> Optional[str]:
    if not latex:
        return None
    t = re.sub(r"\s+", "", latex)
    t = t.replace("\\cdot", "-").replace("^{-", "-").replace("{-}", "-").replace("{-", "-").replace("}", "")
    m = EMBEDDED_ID_RE.search(t) or EMBEDDED_NUM_ID_RE.search(t)
    return m.group(1) if m else None


def find_pdf(rec: dict[str, Any], root: Path, pdf_dir: Optional[Path]) -> Optional[Path]:
    for cand in (rec.get("source_pdf"), rec.get("file")):
        if not cand:
            continue
        p = Path(str(cand))
        if p.is_file():
            return p
        name = Path(str(cand).replace("\\", "/")).name
        for d in ([pdf_dir] if pdf_dir else []) + [root / "documents" / "standards", root / "documents"]:
            if d and (d / name).is_file():
                return d / name
    return None


def pdf_equation_ids(pdf: Path) -> set[str]:
    if not shutil.which("pdftotext"):
        return set()
    try:
        r = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True, timeout=300)
    except Exception:
        return set()
    text = r.stdout or ""
    # a bare "(7-1)" closing an equation line; "Eq. (7-1)" in prose is a reference
    ids: set[str] = set()
    for m in PDF_EQ_ID_RE.finditer(text):
        before = text[max(0, m.start() - 12):m.start()]
        if re.search(r"(Eqs?\.|Equations?)\s*$", before):
            continue
        ids.add(m.group(1).upper() if m.group(1)[:1].isalpha() else m.group(1))
    return ids


# ---------------------------------------------------------------------------------------------

def audit(root: Path, smoke: bool = True, pdf_dir: Optional[Path] = None) -> dict[str, Any]:
    root = root.resolve()
    idx = root / "indexes"
    F = Findings()
    docs = [d for d in (load_json(idx / "documents.json") or []) if isinstance(d, dict)]
    sections = load_json(idx / "sections.json") or []
    equations = load_json(idx / "equations.json") or []
    tables = load_json(idx / "tables.json") or []
    stats = load_json(idx / "build_stats.json") or {}
    if stats.get("id_collisions"):
        F.add("FAIL", "*", "id-collisions", f"build_stats reports id collisions: {stats['id_collisions'][:5]}")

    spec_docs = [d for d in docs if (d.get("collection") or d.get("corpus")) not in P2_COLLECTIONS]
    built = [d for d in spec_docs if d.get("collection") == "specification"]
    if not built:
        F.add("FAIL", "*", "no-built-index", f"{idx / 'documents.json'} holds no built specification records -- run Rebuild index")
    # the same document under two ids (canonical + stem) means the build ingested its own output
    ids = collections.Counter(d.get("id") for d in spec_docs)
    for k, v in ids.items():
        if v > 1:
            F.add("FAIL", str(k), "document-twice", f"documents.json lists {k} {v} times")
    stems_seen = {d.get("converted_stem") for d in built if d.get("converted_stem")}
    for d in spec_docs:
        if d.get("id") in stems_seen:
            F.add("FAIL", str(d.get("id")), "stem-and-canonical", f"{d['id']} is listed both as a stem and under its canonical id")

    converted_dir = idx / "converted"
    conv_docs = load_json(converted_dir / "documents.json") or []
    legacy_conv = [d for d in docs if (d.get("collection") or d.get("corpus")) not in P2_COLLECTIONS and d.get("collection") != "specification"]
    if legacy_conv:
        F.add("INFO", "*", "legacy-converter-records", f"{len(legacy_conv)} converter record(s) still in indexes/ (pre-split); converted/ holds {len(conv_docs)}")

    by_doc_s: dict[str, list] = collections.defaultdict(list)
    by_doc_e: dict[str, list] = collections.defaultdict(list)
    by_doc_t: dict[str, list] = collections.defaultdict(list)
    for r in sections:
        by_doc_s[r.get("doc")].append(r)
    for r in equations:
        by_doc_e[r.get("doc")].append(r)
    for r in tables:
        by_doc_t[r.get("doc")].append(r)

    summary: list[dict[str, Any]] = []
    for rec in built:
        doc = rec["id"]
        stem = rec.get("converted_stem") or doc
        S, E, T = by_doc_s.get(doc, []), by_doc_e.get(doc, []), by_doc_t.get(doc, [])
        row: dict[str, Any] = {"doc": doc, "stem": stem, "sections": len(S), "equations": len(E), "tables": len(T)}

        # --- document record ---------------------------------------------------------------
        digits = re.findall(r"\d{2,4}", stem)
        title = rec.get("title") or ""
        if digits and not any(d in title for d in digits):
            F.add("WARN", doc, "title-mismatch", f"title {title[:60]!r} does not mention {digits} -- may belong to another standard")
        if rec.get("unvalidated"):
            F.add("WARN", doc, "unvalidated", f"document record marked unvalidated: {rec['unvalidated'][:100]}")
        if not rec.get("pdf_pages_total"):
            F.add("INFO", doc, "no-page-total", "pdf_pages_total is empty")
        pages_total = int(rec.get("pdf_pages_total") or 0)

        # --- sections: provenance, duplicates, part vs boundary ------------------------------
        if not S:
            F.add("FAIL", doc, "no-sections", "no section records")
        foreign = [r for r in S if r.get("chunk") and not str(r["chunk"]).startswith(stem + "_")]
        if foreign:
            who = collections.Counter(str(r["chunk"]).split("_p")[0] for r in foreign)
            F.add("FAIL", doc, "foreign-chunk", f"{len(foreign)} section records name another document's chunk file: {dict(who)}")
        key = lambda r: (r.get("section_id"), r.get("title"), r.get("pdf_page"), r.get("chunk"), r.get("part"))
        dup = sum(v - 1 for v in collections.Counter(map(key, S)).values())
        if dup:
            F.add("FAIL", doc, "duplicate-sections", f"{dup} exact duplicate section records (re-process appended instead of replacing)")
        bnd = (rec.get("commentary_boundary") or {}).get("cover_pdf_page")
        parts = collections.Counter(r.get("part") for r in S)
        row["standard"], row["commentary"] = parts.get("standard", 0), parts.get("commentary", 0)
        if bnd:
            bad_std = [r for r in S if r.get("part") == "standard" and (r.get("pdf_page") or 0) >= bnd]
            bad_com = [r for r in S if r.get("part") == "commentary" and (r.get("pdf_page") or 10**9) < bnd]
            if bad_std:
                F.add("FAIL", doc, "commentary-as-standard", f"{len(bad_std)} records tagged standard on/after the commentary cover (pdf {bnd}); e.g. {[(r['section_id'], r['pdf_page']) for r in bad_std[:3]]}")
            if bad_com:
                F.add("FAIL", doc, "standard-as-commentary", f"{len(bad_com)} records tagged commentary before the cover (pdf {bnd})")
        elif parts.get("commentary", 0) == 0 and pages_total > 120:
            F.add("WARN", doc, "no-commentary-split", "no commentary boundary detected and every record is part=standard -- if this standard has a commentary, the profile did not find it")
        ctrl = [r for r in S if CTRL_RE.search(r.get("title") or "")]
        if ctrl:
            F.add("WARN", doc, "control-chars-titles", f"{len(ctrl)} section titles contain control characters ({ctrl[0].get('title', '')[:30]!r})")
        odd = sorted({r["section_id"] for r in S if not ID_SHAPE_RE.match(str(r.get("section_id") or ""))})
        if odd:
            F.add("INFO", doc, "odd-ids", f"{len(odd)} section ids of unexpected shape: {odd[:8]}")
        empty = sum(1 for r in S if not (r.get("title") or "").strip())
        if empty:
            F.add("INFO", doc, "empty-titles", f"{empty} section records have no title (chapter-level headings)")
        if pages_total and len(S) / pages_total * 100 < 25:
            F.add("WARN", doc, "sparse-sections", f"{len(S)} sections for {pages_total} pages ({len(S)/pages_total*100:.0f} per 100) -- deeper headings probably missed (run-in headings or unqualified 1./2a. subsections)")
        chapters = collections.Counter(re.match(r"^(C-)?([A-Z]+|\d+)", str(r.get("section_id") or "?")).group(0) if re.match(r"^(C-)?([A-Z]+|\d+)", str(r.get("section_id") or "?")) else "?" for r in S if r.get("part") == "standard")
        row["chapters"] = " ".join(sorted(chapters, key=lambda s: (len(s), s)))

        # --- searchable markdown hygiene ----------------------------------------------------
        md = None
        for cand in (rec.get("searchable_markdown"), root / "markdown" / f"{stem}.search.md"):
            if cand and Path(str(cand)).is_file():
                md = Path(str(cand)); break
            name = Path(str(cand).replace("\\", "/")).name if cand else None
            if name and (root / "markdown" / name).is_file():
                md = root / "markdown" / name; break
        if md is None:
            F.add("WARN", doc, "no-search-md", "searchable markdown not found; sections are indexed without page text")
        else:
            text = md.read_text(encoding="utf-8", errors="replace")
            n = len(CTRL_RE.findall(text))
            if n:
                F.add("WARN", doc, "control-chars-text", f"{n} control characters in the searchable markdown (show as ^G to the agent)")
            n = len(LIGATURE_SPLIT_RE.findall(text))
            if n > 50:
                F.add("WARN", doc, "split-ligatures", f"{n} split fi/fl ligatures ('speci fi ed'): words like specified/flexural will not match -- re-process with the PDF")
            n = len(WATERMARK_RE.findall(text))
            if n:
                F.add("WARN", doc, "watermark", f"{n} watermark/copyright lines in the searchable text")
            # generic running-header detection: a line repeated at the top of many pages
            pages_dir = root / "markdown" / "pages_search" / stem
            if pages_dir.is_dir():
                firsts: collections.Counter = collections.Counter()
                files = sorted(pages_dir.glob("page_*.md"))
                for f in files:
                    for ln in f.read_text(encoding="utf-8", errors="replace").splitlines():
                        s = ln.strip()
                        if s and not s.startswith("<!--"):
                            firsts[re.sub(r"\d+", "#", s)[:80]]; firsts[re.sub(r"\d+", "#", s)[:80]] += 1
                            break
                if files:
                    for line, c in firsts.most_common(3):
                        if c >= 20 and c / len(files) >= 0.2 and not line.startswith(("#", "|")):
                            F.add("WARN", doc, "running-header", f"line {line!r} opens {c} of {len(files)} pages -- a running header in the searchable text")
            caps = {re.sub(r"\s+", "", m.group(1)) for m in CAPTION_RE.finditer(text)}
        # --- equations ----------------------------------------------------------------------
        with_id = [r for r in E if r.get("eq_id")]
        uniq = {r["eq_id"] for r in with_id}
        row["eq_ids"] = len(uniq)
        if E and len(with_id) / len(E) < 0.6:
            F.add("WARN", doc, "unidentified-equations", f"{len(E) - len(with_id)} of {len(E)} formula rows have no equation id -- the id grammar may not know this document's numbering")
        dis = [(r["eq_id"], printed_id_in_latex(r.get("latex"))) for r in with_id if printed_id_in_latex(r.get("latex")) and printed_id_in_latex(r.get("latex")) != r["eq_id"]]
        if dis:
            F.add("FAIL", doc, "latex-wrong-equation", f"{len(dis)} equation rows carry LaTeX printed with another id: {dis[:4]}")
        norel = sum(1 for r in with_id if r.get("latex") and not RELATION_RE.search(r["latex"]))
        if with_id and norel / len(with_id) > 0.05:
            F.add("INFO", doc, "latex-no-relation", f"{norel} of {len(with_id)} identified equations have LaTeX without =/<=/>= (Docling dropped it; `orig` has it)")
        pdf = find_pdf(rec, root, pdf_dir)
        if pdf:
            printed = pdf_equation_ids(pdf)
            if printed:
                cov = len(printed & {u.upper() for u in uniq} | printed & uniq) / len(printed)
                row["pdf_eq_ids"] = len(printed)
                if cov < 0.7:
                    F.add("WARN", doc, "equation-coverage", f"only {cov:.0%} of the {len(printed)} equation ids printed in the PDF are in the index")
        # --- tables --------------------------------------------------------------------------
        tid = [r for r in T if r.get("table_id")]
        row["table_ids"] = len({r["table_id"] for r in tid})
        fm = [r for r in tid if roman_tail(r.get("printed_label"))]
        if fm:
            F.add("FAIL", doc, "front-matter-table-id", f"{len(fm)} tables on roman-numbered pages carry an id ({fm[0]['table_id']} at {fm[0]['printed_label']}) -- TOC/symbols lists posing as tables")
        if md is not None and caps:
            have = {str(r["table_id"]).replace(" ", "") for r in tid}
            missing = sorted(c for c in caps if c not in have and not c.startswith("C-"))
            if caps and len(missing) / len(caps) > 0.3:
                F.add("WARN", doc, "table-id-coverage", f"{len(missing)} of {len(caps)} 'TABLE X' captions in the text have no table with that id: {missing[:8]}")
        summary.append(row)

    # --- retrieval smoke: what the agent gets back is the record asked for -------------------
    if smoke and built:
        try:
            from retrieval import Corpus  # noqa: E402
            corpus = Corpus(root)
            corpus.use_cache = False
            for rec in built:
                doc = rec["id"]
                S = [r for r in by_doc_s.get(doc, []) if r.get("part") == "standard" and r.get("section_id")]
                S.sort(key=lambda r: r.get("pdf_page") or 0)
                picks = [S[i] for i in {0, len(S) // 2, len(S) - 1} if S] if S else []
                for r in picks:
                    res = corpus.search(type_="exact_section", query=r["section_id"], doc=doc, limit=1)
                    hits = res.get("hits") or []
                    if not hits or hits[0].get("doc") != doc or hits[0].get("section_id") != r["section_id"]:
                        F.add("FAIL", doc, "smoke-section", f"exact_section {r['section_id']} did not return that record of {doc}")
                    elif hits[0].get("part") != "standard":
                        F.add("FAIL", doc, "smoke-part", f"exact_section {r['section_id']} returned the commentary record first")
                E = [r for r in by_doc_e.get(doc, []) if r.get("eq_id") and r.get("part") == "standard"]
                if E:
                    e = E[len(E) // 2]
                    res = corpus.search(type_="exact_equation", query=e["eq_id"], doc=doc, limit=1)
                    hits = res.get("hits") or []
                    if not hits or hits[0].get("doc") != doc:
                        F.add("FAIL", doc, "smoke-equation", f"exact_equation {e['eq_id']} did not return {doc}")
            corpus.close()
        except Exception as exc:  # the audit must never take the build down
            F.add("WARN", "*", "smoke-skipped", f"retrieval smoke test could not run: {exc.__class__.__name__}: {exc}")

    return {"root": str(root), "summary": summary, "findings": F.items,
            "counts": {"FAIL": F.count("FAIL"), "WARN": F.count("WARN"), "INFO": F.count("INFO")}}


def render_md(report: dict[str, Any]) -> str:
    c = report["counts"]
    out = [f"# Corpus audit -- {c['FAIL']} FAIL, {c['WARN']} WARN, {c['INFO']} INFO", "", f"root: `{report['root']}`", "",
           "| document | sections (std/comm) | eq ids | tables (with id) | chapters |", "|---|---|---|---|---|"]
    for r in report["summary"]:
        out.append(f"| {r['doc']} | {r['sections']} ({r.get('standard', 0)}/{r.get('commentary', 0)}) | {r.get('eq_ids', 0)}"
                   f"{' of ' + str(r['pdf_eq_ids']) + ' printed' if r.get('pdf_eq_ids') else ''} | {r['tables']} ({r.get('table_ids', 0)}) | {r.get('chapters', '')} |")
    out.append("")
    for level in ("FAIL", "WARN", "INFO"):
        items = [f for f in report["findings"] if f["level"] == level]
        if not items:
            continue
        out.append(f"## {level}")
        for f in items:
            out.append(f"- **{f['doc']}** `{f['code']}`: {f['message']}")
        out.append("")
    if c["FAIL"] == 0:
        out.append("No FAIL findings: the index describes each document with its own text, once, with commentary told apart from provisions.")
    else:
        out.append("FAIL findings mean the design agents are being served wrong records. See skills/CHECK-AND-CLEAN-CONVERSIONS.md.")
    return "\n".join(out) + "\n"


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", type=Path, default=None, help="workspace root (default: found from this script's location)")
    ap.add_argument("--json-out", type=Path, default=None)
    ap.add_argument("--md-out", type=Path, default=None)
    ap.add_argument("--pdf-dir", type=Path, default=None, help="where the source PDFs are, for the equation-coverage check")
    ap.add_argument("--no-smoke", action="store_true", help="skip the retrieval smoke test")
    args = ap.parse_args(argv)
    root = args.root
    if root is None:
        from retrieval import find_root
        root = find_root()
    report = audit(Path(root), smoke=not args.no_smoke, pdf_dir=args.pdf_dir)
    md = render_md(report)
    (args.md_out or Path(root) / "indexes" / "audit_report.md").write_text(md, encoding="utf-8")
    (args.json_out or Path(root) / "indexes" / "audit_report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
    print(md)
    return 1 if report["counts"]["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
