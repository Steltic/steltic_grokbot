#!/usr/bin/env python3
"""Union per-doc spec indexes + phase-2 indexes; build spec FTS5.

Does not modify original PDFs, per-doc chunk/index files, or phase-2 markdown.
Writes /workspace/engineering_rag/indexes/ and search/spec_fts.sqlite.
Reuses search/phase2_fts.sqlite as-is (symlink).

Usage:
  python scripts/build_index.py
  python scripts/build_index.py --root /workspace/engineering_rag
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from retrieval import (  # noqa: E402
    HTML_COMMENT_RE,
    PAGE_MARK_RE,
    find_root,
    nfkc,
    normalize_eq_id,
)
from pipeline_fixes import (  # noqa: E402
    build_example_id_aliases,
    inherit_continued_table_ids,
    orig_cites_other_eq,
    orig_is_phi_omega_only,
    pdf_page_text,
)

SPEC_STEMS = [
    "AISC_360_22",
    "AISC_341_22",
    "AISC_358_22",
    "AISI_S100",
    "AISI_S240",
    "AISI_S400_20",
    "ASCE7",
]

SEED_GROUPS = [
    ["LTB", "lateral-torsional buckling", "lateral torsional buckling", "L-T buckling"],
    ["overstrength", "Ω0", "Ω_0", "omega_0", "omega0", "Om0", "Ω0", "Ω₀"],
    ["drift", "story drift", "storey drift", "story-drift", "interstory drift", "Δ"],
    ["phi", "φ", "ϕ", "φc", "φb", "φv", "resistance factor"],
    ["Ry", "R_y", "expected yield stress ratio"],
    ["Rt", "R_t", "expected tensile strength ratio"],
    ["SCWB", "strong-column weak-beam", "strong column weak beam", "moment ratio"],
    ["RBS", "reduced beam section", "Reduced Beam Section"],
    ["Ω0", "omega_0", "Om0", "overstrength factor"],
    ["Cd", "C_d", "deflection amplification", "deflection amplification factor"],
    ["SDS", "S_DS", "Sds", "short-period design spectral acceleration"],
    ["SD1", "S_D1", "Sd1", "1-second design spectral acceleration"],
    ["SMF", "special moment frame", "special moment frames"],
    ["IMF", "intermediate moment frame", "intermediate moment frames"],
    ["OMF", "ordinary moment frame"],
    ["SCBF", "special concentrically braced frame"],
    ["EBF", "eccentrically braced frame"],
    ["BRBF", "buckling-restrained braced frame"],
    ["SPSW", "steel plate shear wall"],
    ["STMF", "special truss moment frame"],
    ["CFS", "cold-formed steel", "cold formed steel"],
    ["HSS", "hollow structural section", "hollow structural sections"],
    ["SFRS", "seismic force-resisting system", "seismic force resisting system"],
    ["CJP", "complete joint penetration"],
    ["PJP", "partial joint penetration"],
    ["WUF-W", "welded unreinforced flange-welded web"],
    ["BUEEP", "bolted unstiffened extended end-plate"],
    ["protected zone", "protected zones"],
    ["panel zone", "panel-zone"],
    ["continuity plate", "continuity plates"],
    ["doubler plate", "doubler plates"],
    ["H-pile", "H-piles", "H piles"],
    ["flat strap", "flat-strap", "flat strap bracing", "strap bracing"],
    ["P-delta", "P-Δ", "P-Delta", "second-order"],
    ["Mn", "M_n", "nominal flexural strength"],
    ["Mp", "M_p", "plastic moment"],
    ["Fy", "F_y", "specified minimum yield stress"],
    ["Zx", "Z_x", "plastic section modulus"],
    ["Ie", "I_e", "importance factor"],
    ["R factor", "response modification coefficient", "response modification factor"],
    ["lambda", "λ", "width-to-thickness ratio"],
    ["highly ductile", "highly-ductile"],
    ["moderately ductile", "moderately-ductile"],
    ["expected yield", "Ry Fy", "RyFy"],
    ["base shear", "V", "seismic base shear"],
    ["Cs", "seismic response coefficient"],
    ["exposure B", "Exposure B"],
    ["shear wall", "shear walls"],
    ["chord", "collector", "diaphragm"],
    ["block shear"],
    ["fillet weld"],
    ["slender element", "noncompact", "compact"],
    ["effective length", "K factor"],
    ["notional load"],
    ["capacity-limited", "capacity limited horizontal seismic load effect", "Emh", "E_mh"],
    ["Steel02", "Steel02 Material"],
    ["Giuffre-Menegotto-Pinto", "Menegotto-Pinto"],
    ["forceBeamColumn", "force beam column", "ForceBeamColumn"],
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sanitize_fts(text: Any) -> str:
    if text is None:
        return ""
    s = nfkc(str(text))
    s = s.replace(chr(0), " ")
    s = s.replace("", " ")
    return s


def dump_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def find_search_md(root: Path, stem: str, doc_rec: dict[str, Any]) -> Optional[Path]:
    p = Path(doc_rec.get("searchable_markdown") or "")
    if p.is_file():
        return p
    for cand in (
        root / "documents" / "standards" / stem / "markdown" / f"{stem}.search.md",
        root / "documents" / "standards" / stem / f"{stem}.search.md",
        root / "documents" / "standards" / stem / "complete" / f"{stem}.search.md",
    ):
        if cand.is_file():
            return cand
    return None


def parse_pages(search_md: Path, pages_dir: Optional[Path]) -> dict[int, dict[str, Any]]:
    pages: dict[int, dict[str, Any]] = {}
    if search_md.is_file():
        text = search_md.read_text(encoding="utf-8")
        parts = re.split(r"(?=<!--\s*pdf_page=\d+)", text)
        for part in parts:
            m = PAGE_MARK_RE.search(part)
            if not m:
                m2 = re.match(r"<!--\s*pdf_page=(\d+)\b", part)
                if not m2:
                    continue
                pdf = int(m2.group(1))
                pm = re.search(r"part=(\S+)", part)
                part_flag = pm.group(1) if pm else "standard"
                printed = None
                printed_q = None
            else:
                pdf = int(m.group(1))
                printed = None if m.group(2) in ("None", "none") else m.group(2)
                printed_q = None if m.group(3) in ("None", "none") else m.group(3)
                part_flag = m.group(4)
            body = nfkc(HTML_COMMENT_RE.sub("", part))
            pages[pdf] = {
                "pdf_page": pdf,
                "printed_label": printed,
                "printed_label_qualified": printed_q,
                "part": part_flag,
                "body": body,
            }
    if pages_dir and pages_dir.is_dir():
        for fp in pages_dir.glob("page_*.md"):
            m = re.search(r"page_(\d+)", fp.name)
            if not m:
                continue
            pdf = int(m.group(1))
            body = nfkc(HTML_COMMENT_RE.sub("", fp.read_text(encoding="utf-8")))
            if pdf not in pages:
                pages[pdf] = {
                    "pdf_page": pdf,
                    "printed_label": None,
                    "printed_label_qualified": None,
                    "part": None,
                    "body": body,
                }
            elif len(body) > len(pages[pdf].get("body") or ""):
                pages[pdf]["body"] = body
    return pages


def alias_tokens_for_text(text: str, groups: list[list[str]]) -> str:
    blob = nfkc(text).casefold()
    extra: list[str] = []
    for g in groups:
        if any(nfkc(t).casefold() in blob for t in g if t):
            extra.extend(g)
    return " ".join(dict.fromkeys(extra))


def dropped_letter_aliases(eq_ids: list[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for eid in eq_ids:
        if not eid:
            continue
        m = re.match(r"^([A-Z])(\d[\d.]*-?\d*[A-Za-z]?)$", eid)
        if m:
            dropped = m.group(2)
            out.setdefault(dropped, [])
            if eid not in out[dropped]:
                out[dropped].append(eid)
            out.setdefault(eid, [])
            if dropped not in out[eid]:
                out[eid].append(dropped)
        # Do NOT alias C-prefixed commentary eqs as standard ids (F2-1 != C-F2-1).
    return out


def pick_body_occurrence(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return max(
        rows,
        key=lambda s: (
            int(bool(s.get("children"))),
            int(bool(s.get("synthetic"))),
            int(s.get("pdf_page") or 0),
            len(s.get("title") or ""),
        ),
    )


def build(root: Path) -> dict[str, Any]:
    std_root = root / "documents" / "standards"
    p2_root = root / "engineering_rag_phase2"
    out_idx = root / "indexes"
    out_search = root / "search"
    out_idx.mkdir(parents=True, exist_ok=True)
    out_search.mkdir(parents=True, exist_ok=True)

    documents: list[dict[str, Any]] = []
    sections: list[dict[str, Any]] = []
    equations: list[dict[str, Any]] = []
    tables: list[dict[str, Any]] = []
    spec_pages: dict[str, dict[int, dict[str, Any]]] = {}
    collisions: list[str] = []

    # ----- specs -----
    for stem in SPEC_STEMS:
        ddir = std_root / stem
        idx = ddir / "indexes"
        if not (idx / "documents.json").is_file():
            raise SystemExit(f"missing spec indexes for {stem}: {idx}")
        docs = load_json(idx / "documents.json")
        secs = load_json(idx / "sections.json")
        eqs = load_json(idx / "equations.json")
        tbls = load_json(idx / "tables.json")
        doc0 = docs[0] if isinstance(docs, list) else docs
        edition = doc0.get("edition")
        search_md = find_search_md(root, stem, doc0)
        pages_dir = ddir / "markdown" / "pages_search"
        if search_md:
            spec_pages[stem] = parse_pages(search_md, pages_dir if pages_dir.is_dir() else None)
            doc0 = dict(doc0)
            doc0["searchable_markdown"] = str(search_md)
        doc0["collection"] = "specification"
        doc0["corpus"] = "specification"
        doc0["authoritative"] = True
        documents.append(doc0)

        for s in secs:
            rec = dict(s)
            rec["edition"] = edition
            rec["collection"] = "specification"
            rec["corpus"] = "specification"
            rec["authoritative"] = True
            rec["id"] = f"spec:{stem}:{rec.get('part')}:{rec.get('section_id')}:{rec.get('pdf_page')}"
            sections.append(rec)

        for e in eqs:
            rec = dict(e)
            rec["edition"] = edition
            rec["collection"] = "specification"
            rec["corpus"] = "specification"
            rec["authoritative"] = True
            rec["id"] = (
                f"spec-eq:{stem}:{rec.get('part')}:{rec.get('eq_id')}:{rec.get('pdf_page')}"
            )
            equations.append(rec)

        for t in tbls:
            rec = dict(t)
            rec["edition"] = edition
            rec["collection"] = "specification"
            rec["corpus"] = "specification"
            rec["authoritative"] = True
            rec["id"] = (
                f"spec-tbl:{stem}:{rec.get('part')}:{rec.get('table_id')}:{rec.get('pdf_page')}:{rec.get('index')}"
            )
            tables.append(rec)

    # ----- phase-2 -----
    p2_docs = load_json(p2_root / "indexes" / "documents.json")
    p2_secs = load_json(p2_root / "indexes" / "sections.json")
    p2_eqs = load_json(p2_root / "indexes" / "equations.json")
    p2_toc = load_json(p2_root / "indexes" / "master_toc.json")

    for d in p2_docs:
        rec = dict(d)
        group = rec.get("group") or ("examples" if rec.get("collection") == "steel_design_examples" else "opensees")
        rec["id"] = rec.get("collection")
        rec["collection"] = group
        rec["source_collection"] = d.get("collection")
        rec["corpus"] = group
        rec["authoritative"] = False
        rec["edition"] = None
        rec["part"] = "n/a"
        documents.append(rec)

    p2_ids = set()
    for s in p2_secs:
        rec = dict(s)
        group = rec.get("group") or (
            "examples" if rec.get("collection") == "steel_design_examples" else "opensees"
        )
        src = s.get("collection")
        rec["source_collection"] = src
        rec["collection"] = group
        rec["corpus"] = group
        rec["authoritative"] = False
        rec["edition"] = None
        rec["doc"] = src
        rec["section_id"] = rec.get("id")
        rec["part"] = "n/a"
        rec["pdf_page"] = None
        rec["printed_label"] = None
        sections.append(rec)
        p2_ids.add(rec["id"])

    spec_raw_ids = {
        s["section_id"]
        for s in sections
        if s.get("collection") == "specification" and s.get("section_id")
    }
    overlap = spec_raw_ids & p2_ids
    if overlap:
        collisions.append(f"raw section_id overlap with phase-2 ids: {sorted(overlap)[:20]}")
    spec_constructed = {s["id"] for s in sections if s.get("collection") == "specification"}
    overlap2 = spec_constructed & p2_ids
    if overlap2:
        collisions.append(f"constructed spec id overlap: {sorted(overlap2)[:20]}")
    if collisions:
        raise SystemExit("ID COLLISION during merge:\n" + "\n".join(collisions))

    # phase-2 equations: map eq_id -> chunk ids
    if isinstance(p2_eqs, dict):
        byid = {s["id"]: s for s in p2_secs}
        for eid, cids in p2_eqs.items():
            for cid in cids:
                chunk = byid.get(cid) or {}
                group = chunk.get("group") or "examples"
                equations.append(
                    {
                        "id": f"p2-eq:{eid}:{cid}",
                        "doc": chunk.get("collection") or "steel_design_examples",
                        "edition": None,
                        "eq_id": eid,
                        "eq_id_display": f"({eid})",
                        "section": cid,
                        "part": "n/a",
                        "pdf_page": None,
                        "printed_label": None,
                        "collection": group if group in ("opensees", "examples") else "examples",
                        "corpus": "examples" if group == "examples" else "opensees",
                        "authoritative": False,
                        "chunk_id": cid,
                        "orig": None,
                        "latex": None,
                        "file": chunk.get("file"),
                        "title": chunk.get("title"),
                    }
                )
    # lightweight table pointers from phase-2 chunks
    for s in p2_secs:
        for tid in s.get("tables") or []:
            tables.append(
                {
                    "id": f"p2-tbl:{s.get('id')}:{tid}",
                    "doc": s.get("collection"),
                    "edition": None,
                    "table_id": str(tid),
                    "title": s.get("title"),
                    "section": s.get("id"),
                    "part": "n/a",
                    "pdf_page": None,
                    "printed_label": None,
                    "collection": s.get("group") or "examples",
                    "corpus": s.get("group") or "examples",
                    "authoritative": False,
                    "chunk_id": s.get("id"),
                    "file": s.get("file"),
                    "markdown_excerpt": None,
                    "md": None,
                    "num_rows": None,
                }
            )

    # Multi-page tables: inherit adjacent null-id pages (ASCE 12.2-1 gold).
    tables = inherit_continued_table_ids(tables)

    # Rebound orig when it is φ/Ω-only or the previous formula (J10-9..12 gold).
    try:
        from postprocess import orig_from_context  # noqa: E402
    except Exception:
        orig_from_context = None
    if orig_from_context:
        pdf_cache: dict[tuple, str] = {}
        meta_by = {d.get("id"): d for d in documents}
        for e in equations:
            if e.get("collection") != "specification" or not e.get("eq_id"):
                continue
            orig = e.get("orig") or ""
            if not (orig_is_phi_omega_only(orig) or orig_cites_other_eq(orig, e.get("eq_id") or "")):
                continue
            meta = meta_by.get(e.get("doc")) or {}
            pdfp = Path(meta.get("source_pdf") or "")
            pno = e.get("pdf_page")
            if not pdfp.is_file() or not pno:
                continue
            key = (str(pdfp), int(pno))
            if key not in pdf_cache:
                pdf_cache[key] = pdf_page_text(pdfp, int(pno))
            filled = orig_from_context(pdf_cache[key], e.get("eq_id"), e.get("eq_id_display"))
            if filled and not orig_is_phi_omega_only(filled) and not orig_cites_other_eq(filled, e.get("eq_id") or ""):
                e["orig"] = filled
                issues = list(e.get("issues") or [])
                msg = "orig rebound from PDF clause next to id token"
                if msg not in issues:
                    issues.append(msg)
                e["issues"] = issues

    # persist repaired spec tables/equations into per-doc indexes
    std_root = root / "documents" / "standards"
    for stem in SPEC_STEMS:
        idx = std_root / stem / "indexes"
        if not idx.is_dir():
            continue
        spec_eq = [e for e in equations if e.get("doc") == stem and e.get("collection") == "specification"]
        spec_tbl = [tb for tb in tables if tb.get("doc") == stem and tb.get("collection") == "specification"]
        if spec_eq:
            dump_json(idx / "equations.json", spec_eq)
        if spec_tbl:
            dump_json(idx / "tables.json", spec_tbl)

    # ----- aliases -----
    eq_ids = [e.get("eq_id") for e in equations if e.get("eq_id")]
    eq_aliases = dropped_letter_aliases(eq_ids)
    # extra common eq aliases
    for a, b in [("F2-1", "F21"), ("B4.1a", "B41a"), ("12.8-3", "12.8.3")]:
        eq_aliases.setdefault(a, []).append(b)
        eq_aliases.setdefault(b, []).append(a)
    id_aliases = build_example_id_aliases(sections)
    aliases = {
        "synonym_groups": SEED_GROUPS,
        "eq_id_aliases": eq_aliases,
        "id_aliases": id_aliases,
        "notes": (
            "Alias layer for keyword/FTS expansion. Ω0/omega_0/Om0 and φ/phi are "
            "handled here rather than a stemmer (stemming would break symbols). "
            "Dropped-letter AISI eq ids: 1.3.1.1-1 ↔ E1.3.1.1-1. "
            "Example chunk ids: F.1 / E.9 / F.1-1A resolve to *_p1 family. "
            "C-prefixed commentary eqs are not aliases of standard ids."
        ),
    }

    # ----- master TOC -----
    spec_toc: dict[str, Any] = {}
    for stem in SPEC_STEMS:
        spec_toc[stem] = {"standard": [], "commentary": []}
    for s in sections:
        if s.get("collection") != "specification":
            continue
        part = s.get("part") if s.get("part") in ("standard", "commentary") else "standard"
        spec_toc[s["doc"]][part].append(
            {
                "id": s["id"],
                "section_id": s.get("section_id"),
                "title": s.get("title"),
                "pdf_page": s.get("pdf_page"),
                "printed_label": s.get("printed_label"),
                "parent": s.get("parent"),
            }
        )
    master_toc = {
        "specification": spec_toc,
        "opensees": {},
        "examples": {},
        "phase2_nav": p2_toc,
    }
    for coll, groups in (p2_toc or {}).items():
        bucket = "examples" if coll == "steel_design_examples" else "opensees"
        master_toc[bucket][coll] = groups

    toc_md_lines = [
        "# Unified master TOC",
        "",
        "Specification sections are authoritative. OpenSees / examples are **not** authoritative.",
        "",
    ]
    for stem in SPEC_STEMS:
        toc_md_lines.append(f"## {stem} (specification)")
        for part in ("standard", "commentary"):
            toc_md_lines.append(f"\n### {part}")
            rows = spec_toc[stem][part]
            # unique by section_id keeping later page
            seen = {}
            for r in rows:
                seen[r["section_id"]] = r
            for r in list(seen.values())[:400]:
                toc_md_lines.append(
                    f"- `{r['section_id']}` — {r.get('title') or ''} (pdf {r.get('pdf_page')}, {r.get('printed_label')})"
                )
            if len(seen) > 400:
                toc_md_lines.append(f"- … {len(seen) - 400} more")
        toc_md_lines.append("")
    toc_md_lines.append("## Phase-2 collections (not authoritative)")
    for coll, groups in (p2_toc or {}).items():
        toc_md_lines.append(f"\n### {coll}")
        for nav in sorted(groups):
            toc_md_lines.append(f"- **{nav}**: {len(groups[nav])} chunks")

    dump_json(out_idx / "documents.json", documents)
    dump_json(out_idx / "sections.json", sections)
    dump_json(out_idx / "equations.json", equations)
    dump_json(out_idx / "tables.json", tables)
    dump_json(out_idx / "master_toc.json", master_toc)
    dump_json(out_idx / "aliases.json", aliases)
    (out_idx / "master_toc.md").write_text("\n".join(toc_md_lines) + "\n", encoding="utf-8")
    # copy aliases next to scripts for the staging list
    dump_json(root / "scripts" / "aliases.json", aliases)

    # ----- spec FTS -----
    fts_path = out_search / "spec_fts.sqlite"
    if fts_path.exists():
        fts_path.unlink()
    con = sqlite3.connect(fts_path, timeout=60)
    con.execute("PRAGMA journal_mode=DELETE")
    con.execute("PRAGMA synchronous=OFF")
    con.execute("PRAGMA temp_store=MEMORY")
    con.execute(
        """
        CREATE VIRTUAL TABLE spec_fts USING fts5(
          rec_id UNINDEXED,
          kind UNINDEXED,
          doc UNINDEXED,
          edition UNINDEXED,
          section_id,
          eq_id,
          table_id,
          part UNINDEXED,
          collection UNINDEXED,
          pdf_page UNINDEXED,
          printed_label UNINDEXED,
          title,
          body,
          aliases,
          tokenize = 'unicode61'
        )
        """
    )
    fts_rows: list[tuple] = []

    # section-level: one row per (doc, part, section_id) using body occurrence
    by_key: dict[tuple, list] = defaultdict(list)
    for s in sections:
        if s.get("collection") != "specification":
            continue
        by_key[(s["doc"], s.get("part"), s.get("section_id"))].append(s)
    for key, rows in by_key.items():
        s = pick_body_occurrence(rows)
        doc, part, sid = key
        pages = spec_pages.get(doc) or {}
        pdf = s.get("pdf_page")
        body = ""
        printed = s.get("printed_label")
        if pdf and pages:
            start = int(pdf)
            later = [
                int(x["pdf_page"])
                for x in rows_same_part(by_key, doc, part)
                if x.get("pdf_page") and int(x["pdf_page"]) > start
            ]
            # next *other* section at a later page
            later_other = [
                int(x["pdf_page"])
                for x in rows_same_part(by_key, doc, part)
                if x.get("section_id") != sid
                and x.get("pdf_page")
                and int(x["pdf_page"]) > start
            ]
            end = min(later_other) - 1 if later_other else start + 2
            end = max(start, min(end, start + 5))
            chunks = []
            for pno in range(start, end + 1):
                if pno in pages:
                    chunks.append(pages[pno]["body"])
                    if not printed:
                        printed = pages[pno].get("printed_label")
            body = "\n\n".join(chunks)
        title = s.get("title") or ""
        # prepend title so BM25 weights headings
        fts_body = nfkc(f"{sid} {title}\n\n{body}")
        aliases_s = alias_tokens_for_text(fts_body, SEED_GROUPS)
        fts_rows.append(
            (
                s["id"],
                "section",
                doc,
                s.get("edition"),
                sid,
                None,
                None,
                part,
                "specification",
                pdf,
                printed,
                title,
                fts_body,
                aliases_s,
            )
        )

    # equations with ids
    for e in equations:
        if e.get("collection") != "specification" or not e.get("eq_id"):
            continue
        body = nfkc(
            "\n".join(
                x
                for x in (
                    e.get("eq_id_display"),
                    e.get("orig"),
                    e.get("latex"),
                    (e.get("nearby_text") or "")[:2000],
                )
                if x
            )
        )
        fts_rows.append(
            (
                e["id"],
                "equation",
                e.get("doc"),
                e.get("edition"),
                e.get("section"),
                e.get("eq_id"),
                None,
                e.get("part"),
                "specification",
                e.get("pdf_page"),
                e.get("printed_label"),
                e.get("eq_id"),
                body,
                alias_tokens_for_text(body, SEED_GROUPS),
            )
        )

    # tables with ids — include markdown so row values are searchable
    seen_tbl = set()
    for t in tables:
        if t.get("collection") != "specification" or not t.get("table_id"):
            continue
        key = (t.get("doc"), t.get("table_id"), t.get("part"), t.get("pdf_page"))
        if key in seen_tbl:
            continue
        seen_tbl.add(key)
        blobs = [t.get("title") or "", t.get("markdown_excerpt") or ""]
        md = t.get("md")
        if md and Path(md).is_file():
            try:
                blobs.append(Path(md).read_text(encoding="utf-8")[:80000])
            except OSError:
                pass
        body = nfkc("\n".join(blobs))
        fts_rows.append(
            (
                t["id"],
                "table",
                t.get("doc"),
                t.get("edition"),
                t.get("section"),
                None,
                t.get("table_id"),
                t.get("part"),
                "specification",
                t.get("pdf_page"),
                t.get("printed_label"),
                t.get("title") or t.get("table_id"),
                body,
                alias_tokens_for_text(body, SEED_GROUPS),
            )
        )

    # Page-level FTS so commentary figures/prose (341 C-F2.18 / pdf 371 "2 t")
    # are searchable even when they are not a section start. Keep "2 t" tokens.
    for stem, pages in spec_pages.items():
        meta = next((d for d in documents if d.get("id") == stem), {}) or {}
        edition = meta.get("edition")
        for pno, rec in pages.items():
            body = rec.get("body") or ""
            if len(body.strip()) < 40:
                continue
            part = rec.get("part") or "standard"
            printed = rec.get("printed_label")
            title = f"{stem} pdf {pno} {printed or ''}".strip()
            fts_rows.append(
                (
                    f"spec-page:{stem}:{part}:{pno}",
                    "page",
                    stem,
                    edition,
                    None,
                    None,
                    None,
                    part,
                    "specification",
                    pno,
                    printed,
                    title,
                    nfkc(body),
                    alias_tokens_for_text(body, SEED_GROUPS),
                )
            )

    clean_rows = []
    for row in fts_rows:
        cr = []
        for i, v in enumerate(row):
            if v is None:
                cr.append("" if i not in {9} else None)  # pdf_page may be int/None
            elif isinstance(v, str):
                cr.append(sanitize_fts(v))
            else:
                cr.append(v)
        # pdf_page as text for UNINDEXED safety
        if cr[9] is None:
            cr[9] = ""
        else:
            cr[9] = str(cr[9])
        clean_rows.append(tuple(cr))
    con.executemany(
        "INSERT INTO spec_fts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        clean_rows,
    )
    con.commit()
    con.close()

    # ensure phase2 FTS symlink
    p2_fts_src = p2_root / "search" / "phase2_fts.sqlite"
    p2_fts_dst = out_search / "phase2_fts.sqlite"
    if not p2_fts_dst.exists():
        p2_fts_dst.symlink_to(p2_fts_src)

    spec_docs = [d for d in documents if d.get("collection") == "specification"]
    p2d = [d for d in documents if d.get("collection") != "specification"]
    spec_sec = [s for s in sections if s.get("collection") == "specification"]
    p2_sec = [s for s in sections if s.get("collection") != "specification"]
    spec_eq = [e for e in equations if e.get("collection") == "specification" and e.get("eq_id")]
    p2_eq = [e for e in equations if e.get("collection") != "specification"]
    spec_tbl = [t for t in tables if t.get("collection") == "specification" and t.get("table_id")]
    p2_tbl = [t for t in tables if t.get("collection") != "specification"]
    stats = {
        "documents_spec": len(spec_docs),
        "documents_phase2": len(p2d),
        "sections_spec": len(spec_sec),
        "sections_phase2": len(p2_sec),
        "equations_spec_with_id": len(spec_eq),
        "equations_phase2": len(p2_eq),
        "tables_spec_with_id": len(spec_tbl),
        "tables_phase2": len(p2_tbl),
        "fts_rows": len(fts_rows),
        "spec_fts_bytes": fts_path.stat().st_size,
        "phase2_fts_bytes": p2_fts_src.stat().st_size,
        "id_collisions": collisions,
    }
    dump_json(out_idx / "build_stats.json", stats)
    print(json.dumps(stats, indent=2))
    return stats


def rows_same_part(by_key: dict, doc: str, part: str) -> list[dict[str, Any]]:
    out = []
    for (d, p, _sid), rows in by_key.items():
        if d == doc and p == part:
            out.extend(rows)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Build unified indexes + spec FTS")
    ap.add_argument("--root", type=Path, default=None)
    args = ap.parse_args()
    root = args.root or find_root()
    build(root)


if __name__ == "__main__":
    main()
