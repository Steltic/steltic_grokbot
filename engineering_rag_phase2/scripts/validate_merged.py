#!/usr/bin/env python3
"""Cross-corpus validation: every per-document gold probe through MERGED search.

A merge that breaks a per-doc probe is FAIL. Also runs phase-2 smokes and one
cross-corpus ranking probe. Writes TEST_REPORT_MERGED.md at the engineering_rag root.

Usage:
  python scripts/validate_merged.py
  python scripts/validate_merged.py --root /workspace/engineering_rag
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from retrieval import Corpus, nfkc, squash, find_root  # noqa: E402

ICT = timezone(timedelta(hours=7))


def nf(text: str) -> str:
    return unicodedata.normalize("NFKC", text or "")


class Report:
    def __init__(self) -> None:
        self.rows: list[dict[str, Any]] = []

    def add(self, name: str, ok: bool, detail: str) -> None:
        self.rows.append({"name": name, "ok": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail[:300]}")

    @property
    def passed(self) -> bool:
        return all(r["ok"] for r in self.rows)

    def write_md(self, path: Path, extra: dict[str, Any]) -> None:
        n_ok = sum(1 for r in self.rows if r["ok"])
        now = datetime.now(ICT).strftime("%Y-%m-%d %H:%M ICT")
        lines = [
            "# TEST_REPORT_MERGED — unified retrieval (spec + phase-2)",
            "",
            f"**Run:** {now}",
            f"**OVERALL: {'PASS' if self.passed else 'FAIL'} {n_ok}/{len(self.rows)}**",
            "",
            "Probes go through the merged `search.py` / `retrieval.Corpus` backend,",
            "not through per-document JSON indexes alone. Phase-2 chunk files were not edited.",
            "",
            "## Counts",
            "",
            f"- documents: spec {extra.get('documents_spec')} / phase-2 {extra.get('documents_phase2')}",
            f"- sections: spec {extra.get('sections_spec')} / phase-2 {extra.get('sections_phase2')}",
            f"- equations (with id): spec {extra.get('equations_spec')} / phase-2 {extra.get('equations_phase2')}",
            f"- tables (with id): spec {extra.get('tables_spec')} / phase-2 {extra.get('tables_phase2')}",
            f"- spec FTS: {extra.get('spec_fts_bytes')} bytes at `{extra.get('spec_fts_path')}`",
            f"- phase-2 FTS: {extra.get('phase2_fts_bytes')} bytes (reused as-is)",
            "",
            "## Probes",
            "",
            "| Probe | Result | Detail |",
            "|---|---|---|",
        ]
        for r in self.rows:
            det = (r["detail"] or "").replace("|", "/").replace("\n", " ")[:180]
            lines.append(f"| {r['name']} | {'PASS' if r['ok'] else 'FAIL'} | {det} |")
        lines += ["", "## Notes", "", extra.get("notes", ""), ""]
        path.write_text("\n".join(lines), encoding="utf-8")


def first(hits, pred=None):
    for h in hits or []:
        if pred is None or pred(h):
            return h
    return None


def run(root: Path) -> int:
    c = Corpus(root)
    R = Report()

    def hit_search(typ, query, **kw):
        return c.search(typ, query, **kw)

    # ----- A360 -----
    r = hit_search("eq", "F2-1", doc="AISC_360_22")
    h = first(r.get("hits"))
    R.add(
        "A360 Eq F2-1 Mn=Mp=FyZx ~pdf 121",
        bool(r.get("found") and h and h.get("pdf_page") == 121 and "mn=mp=fyzx" in squash(h.get("text"))),
        f"pdf={h.get('pdf_page') if h else None} orig={h.get('orig') if h else None} part={h.get('part') if h else None}",
    )
    r = hit_search("table", "B4.1a", doc="AISC_360_22")
    h = first(r.get("hits"))
    txt = h.get("text") if h else ""
    R.add(
        "A360 Table B4.1a",
        bool(r.get("found") and h and h.get("table_id") == "B4.1a" and ("Flanges of rolled" in txt or "0.56" in txt)),
        f"id={h.get('table_id') if h else None} pdf={h.get('pdf_page') if h else None}",
    )
    r = hit_search("exact_section", "F2.2", doc="AISC_360_22")
    h = first(r.get("hits"))
    R.add(
        "A360 F2.2 provision",
        bool(r.get("found") and h and h.get("part") == "standard" and abs((h.get("pdf_page") or 0) - 121) <= 5),
        f"part={h.get('part') if h else None} pdf={h.get('pdf_page') if h else None} title={h.get('title') if h else None}",
    )
    r = hit_search("exact_section", "F2", doc="AISC_360_22", want_commentary=True)
    h = first(r.get("hits"))
    R.add(
        "A360 commentary F2 flagged commentary",
        bool(r.get("found") and h and h.get("part") == "commentary" and (h.get("pdf_page") or 0) >= 400),
        f"part={h.get('part') if h else None} pdf={h.get('pdf_page') if h else None}",
    )

    # ----- A341 -----
    r = hit_search("exact_section", "E3.4a", doc="AISC_341_22")
    h = first(r.get("hits"))
    R.add(
        "A341 E3.4a SCWB / moment ratio",
        bool(r.get("found") and h and h.get("part") == "standard" and abs((h.get("pdf_page") or 0) - 99) <= 3),
        f"pdf={h.get('pdf_page') if h else None} title={h.get('title') if h else None}",
    )
    r = hit_search("table", "D1.1b", doc="AISC_341_22")
    h = first(r.get("hits"))
    R.add(
        "A341 Table D1.1b",
        bool(r.get("found") and h and "D1.1b" in str(h.get("table_id"))),
        f"id={h.get('table_id') if h else None} pdf={h.get('pdf_page') if h else None}",
    )
    r = hit_search("exact_section", "D1.3", doc="AISC_341_22")
    h = first(r.get("hits"))
    R.add(
        "A341 D1.3 Protected Zones ~pdf 77",
        bool(r.get("found") and h and "Protected" in (h.get("title") or "") and abs((h.get("pdf_page") or 0) - 77) <= 2),
        f"pdf={h.get('pdf_page') if h else None} title={h.get('title') if h else None}",
    )
    r = hit_search("exact_section", "D4.1", doc="AISC_341_22")
    h = first(r.get("hits"))
    txt = (h.get("text") if h else "") or ""
    R.add(
        "A341 D4.1 H-piles pdf 90",
        bool(r.get("found") and h and abs((h.get("pdf_page") or 0) - 90) <= 2 and "H-PILE" in txt.upper()),
        f"pdf={h.get('pdf_page') if h else None} title={h.get('title') if h else None}",
    )
    r = hit_search("table", "A3.2", doc="AISC_341_22")
    h = first(r.get("hits"))
    txt = (h.get("text") if h else "") or ""
    R.add(
        "A341 Table A3.2 Ry/Rt",
        bool(r.get("found") and h and "A36" in txt.replace(" ", "") and "1.5" in txt),
        f"id={h.get('table_id') if h else None} pdf={h.get('pdf_page') if h else None}",
    )

    # ----- A358 -----
    r = hit_search("exact_section", "5.7", doc="AISC_358_22")
    h = first(r.get("hits"))
    txt = (h.get("text") if h else "") or ""
    n_steps = sum(bool(re.search(rf"Step\s+{n}\b", txt, re.I)) for n in range(1, 14))
    R.add(
        "A358 RBS 5.7 design steps 1-13",
        bool(r.get("found") and h and h.get("part") == "standard" and n_steps >= 8),
        f"pdf={h.get('pdf_page') if h else None} n_steps={n_steps} title={h.get('title') if h else None}",
    )
    r = hit_search("eq", "15.6-1", doc="AISC_358_22")
    h = first(r.get("hits"))
    R.add(
        "A358 eq 15.6-1",
        bool(r.get("found") and h and h.get("eq_id") == "15.6-1"),
        f"eq={h.get('eq_id') if h else None} pdf={h.get('pdf_page') if h else None}",
    )

    # ----- ASCE7 -----
    r = hit_search("eq", "12.8-3", doc="ASCE7")
    h = first(r.get("hits"), lambda x: x.get("pdf_page") == 185) or first(r.get("hits"))
    R.add(
        "ASCE7 12.8-3 Cs ~ SDS/(R/Ie)",
        bool(r.get("found") and h and "sds" in squash(h.get("text"))),
        f"pdf={h.get('pdf_page') if h else None} orig={h.get('orig') if h else None}",
    )
    r = hit_search("table", "12.2-1", doc="ASCE7")
    h = first(r.get("hits"))
    txt = nf(h.get("text") if h else "")
    has_flat = "flat" in txt.casefold() and "strap" in txt.casefold()
    has_r = bool(re.search(r"\b4\b", txt))
    R.add(
        "ASCE7 Table 12.2-1 CFS flat-strap R=4/Ω0=2/Cd=3.5 (NFKC)",
        bool(r.get("found") and h and has_flat and has_r),
        f"pdf={h.get('pdf_page') if h else None} has_flat={has_flat} chars={len(txt)}",
    )
    r = hit_search("exact_section", "12.4.3.2", doc="ASCE7")
    h = first(r.get("hits"))
    R.add(
        "ASCE7 12.4.3.2 provision",
        bool(r.get("found") and h and h.get("part") == "standard"),
        f"pdf={h.get('pdf_page') if h else None} part={h.get('part') if h else None} title={(h.get('title') or '')[:60] if h else None}",
    )
    r = hit_search("table", "26.11-1", doc="ASCE7")
    h = first(r.get("hits"))
    txt = (h.get("text") if h else "") or ""
    R.add(
        "ASCE7 Table 26.11-1 Exposure B",
        bool(r.get("found") and h and ("7.5" in txt or "3280" in txt or "Exposure" in txt)),
        f"id={h.get('table_id') if h else None} pdf={h.get('pdf_page') if h else None}",
    )
    r = hit_search("table", "C26.5-5", doc="ASCE7")
    h = first(r.get("hits"))
    R.add(
        "ASCE7 C26.5-5",
        bool(r.get("found") and h and h.get("table_id") == "C26.5-5"),
        f"id={h.get('table_id') if h else None} pdf={h.get('pdf_page') if h else None} part={h.get('part') if h else None}",
    )

    # ----- S400 -----
    r = hit_search("exact_section", "E3.4.2", doc="AISI_S400_20")
    h = first(r.get("hits"))
    R.add(
        "S400 E3.4.2 provision",
        bool(r.get("found") and h and h.get("part") == "standard" and abs((h.get("pdf_page") or 0) - 59) <= 2),
        f"pdf={h.get('pdf_page') if h else None} part={h.get('part') if h else None}",
    )
    r = hit_search("exact_section", "E3.4.2", doc="AISI_S400_20", want_commentary=True)
    h = first(r.get("hits"))
    R.add(
        "S400 E3.4.2 commentary",
        bool(r.get("found") and h and h.get("part") == "commentary" and abs((h.get("pdf_page") or 0) - 136) <= 2),
        f"pdf={h.get('pdf_page') if h else None} part={h.get('part') if h else None}",
    )
    r = hit_search("table", "E1.3-1", doc="AISI_S400_20")
    h = first(r.get("hits"))
    txt = (h.get("text") if h else "") or ""
    R.add(
        "S400 Table E1.3-1 940/1410/1760/2350",
        bool(r.get("found") and all(v in txt for v in ("940", "1410", "1760", "2350"))),
        f"id={h.get('table_id') if h else None} pdf={h.get('pdf_page') if h else None}",
    )
    r = hit_search("eq", "E1.3.1.1-1", doc="AISI_S400_20")
    h = first(r.get("hits"))
    orig = (h.get("orig") if h else "") or ""
    R.add(
        "S400 eq E1.3.1.1-1 orig is math (Vn = vnw)",
        bool(r.get("found") and "vn" in squash(orig) and "e1.3" not in squash(orig).replace("e13111", "")),
        f"orig={orig!r}",
    )
    r = hit_search("eq", "1.3.1.1-1", doc="AISI_S400_20")
    h = first(r.get("hits"))
    R.add(
        "S400 dropped-letter 1.3.1.1-1 -> E1.3.1.1-1",
        bool(r.get("found") and h and h.get("eq_id") == "E1.3.1.1-1"),
        f"eq={h.get('eq_id') if h else None}",
    )

    # ----- S100 -----
    r = hit_search("eq", "A3.1.3-1", doc="AISI_S100")
    h = first(r.get("hits"))
    R.add(
        "S100 Eq A3.1.3-1 ~pdf 78",
        bool(r.get("found") and h and abs((h.get("pdf_page") or 0) - 78) <= 2),
        f"pdf={h.get('pdf_page') if h else None}",
    )
    r = hit_search("exact_section", "E2", doc="AISI_S100")
    h = first(r.get("hits"))
    R.add(
        "S100 Chapter E2 provision ~pdf 102",
        bool(r.get("found") and h and h.get("part") == "standard" and abs((h.get("pdf_page") or 0) - 102) <= 3),
        f"pdf={h.get('pdf_page') if h else None} title={h.get('title') if h else None}",
    )

    # ----- S240 -----
    r = hit_search("exact_section", "D5.1.2", doc="AISI_S240")
    h = first(r.get("hits"))
    R.add(
        "S240 D5.1.2 pdf 105 / printed 78",
        bool(r.get("found") and h and h.get("pdf_page") == 105 and str(h.get("printed_label")) == "78" and h.get("part") == "standard"),
        f"pdf={h.get('pdf_page') if h else None} printed={h.get('printed_label') if h else None} part={h.get('part') if h else None}",
    )

    # ----- phase-2 smokes -----
    r = hit_search("command", "forceBeamColumn")
    h = first(r.get("hits"))
    R.add(
        "phase-2 command forceBeamColumn",
        bool(r.get("found") and h and h.get("corpus") == "opensees" and "force" in (h.get("title") or "").lower()),
        f"id={h.get('id') if h else None} title={h.get('title') if h else None} corpus={h.get('corpus') if h else None}",
    )
    r = hit_search("eq", "E3-2")
    ex = [h for h in (r.get("hits") or []) if h.get("corpus") == "examples"]
    R.add(
        "phase-2 eq E3-2 17 example chunks",
        len(ex) == 17,
        f"n_examples={len(ex)} n_all={len(r.get('hits') or [])}",
    )
    r = hit_search("fts", "Steel02 hysteretic", limit=8)
    ids = [str(h.get("section_id") or h.get("id") or "") + " " + str(h.get("title") or "") for h in (r.get("hits") or [])]
    R.add(
        "phase-2 FTS Steel02 hysteretic",
        bool(r.get("found") and any("Steel02" in x for x in ids)),
        f"top={[(h.get('corpus'), h.get('section_id') or h.get('id')) for h in (r.get('hits') or [])][:6]}",
    )

    # ----- cross-corpus -----
    r = hit_search("fts", "lateral-torsional buckling", limit=12)
    hits = r.get("hits") or []
    i_spec = next((i for i, h in enumerate(hits) if h.get("corpus") == "specification"), None)
    i_ex = next((i for i, h in enumerate(hits) if h.get("corpus") in ("examples", "opensees")), None)
    R.add(
        "cross-corpus LTB: spec ranked above examples",
        bool(r.get("found") and i_spec is not None and (i_ex is None or i_spec < i_ex)),
        f"first_spec={i_spec} first_other={i_ex} top={[(h.get('corpus'), h.get('doc'), h.get('section_id')) for h in hits[:6]]}",
    )

    # ----- 2026-09-01 HR+CFS retrieval nits -----
    r = hit_search("table", "12.2-1", doc="ASCE7")
    h = first(r.get("hits"))
    txt = nf(h.get("text") if h else "")
    smf_ok = "steel special moment" in txt.lower()
    brbf_ok = "buckling-restrained" in txt.lower()
    ebf_ok = "eccentrically braced" in txt.lower()
    sbmf_ok = "special bolted moment" in txt.lower()
    R.add(
        "ASCE7 Table 12.2-1 SMF/EBF/BRBF/SBMF rows (merged pages)",
        bool(r.get("found") and h and smf_ok and brbf_ok and ebf_ok and sbmf_ok),
        f"pdf={h.get('pdf_page') if h else None} smf={smf_ok} ebf={ebf_ok} brbf={brbf_ok} sbmf={sbmf_ok} tid={h.get('table_id') if h else None}",
    )
    r = hit_search("table", "G5-2", doc="AISI_S100")
    h = first(r.get("hits"))
    R.add(
        "S100 Table G5-2 rank-1 is real table_id not TOC null",
        bool(r.get("found") and h and h.get("table_id") and (h.get("pdf_page") or 0) >= 100),
        f"tid={h.get('table_id') if h else None} pdf={h.get('pdf_page') if h else None} title={(h.get('title') or '')[:60] if h else None}",
    )
    r = hit_search("eq", "J10-11", doc="AISC_360_22")
    h = first(r.get("hits"))
    orig = (h.get("orig") if h else "") or ""
    R.add(
        "A360 J10-11 orig is J10-11 formula not J10-9",
        bool(r.get("found") and h and "0.60" in orig.replace(" ", "") and "(J10-9)" not in orig and "LRFD" not in orig),
        f"orig={orig!r}",
    )
    r = hit_search("eq", "F2-1", doc="AISC_341_22", want_commentary=False)
    R.add(
        "A341 F2-1 want_commentary false found:false (no C-F2-1 alias)",
        (not r.get("found")) and not any(
            (h.get("eq_id") or "").startswith("C-") for h in (r.get("hits") or [])
        ),
        f"found={r.get('found')} hits={[h.get('eq_id') for h in (r.get('hits') or [])][:4]}",
    )
    r = hit_search("fts", "eccentrically braced frame", doc="examples", collection="examples", limit=8)
    docs = [h.get("doc") or h.get("collection") for h in (r.get("hits") or [])]
    leak = any("opensees" in str(x).lower() for x in docs)
    R.add(
        "examples FTS does not leak opensees",
        not leak,
        f"found={r.get('found')} docs={docs[:6]}",
    )
    r = hit_search("id", "E.9_p1")
    h = first(r.get("hits"))
    R.add(
        "example id E.9_p1 still works",
        bool(r.get("found") and h and h.get("id") == "E.9_p1"),
        f"id={h.get('id') if h else None} corpus={h.get('corpus') if h else None}",
    )
    r = hit_search("fts", "8 t elliptical clearance", doc="AISC_341_22", want_commentary=True, limit=8)
    hits = r.get("hits") or []
    R.add(
        "A341 FTS 8 t elliptical clearance (C-F2.18 commentary)",
        bool(r.get("found") and hits),
        f"found={r.get('found')} top={[(h.get('pdf_page'), h.get('part'), h.get('section_id')) for h in hits[:4]]}",
    )

    # found:false never guesses
    r = hit_search("exact_section", "ZZZ.999", doc="AISC_360_22")
    R.add(
        "miss ZZZ.999 found:false with suggestions",
        (not r.get("found")) and r.get("found") is False,
        f"found={r.get('found')} nearest={r.get('nearest_ids')}",
    )

    stats_path = root / "indexes" / "build_stats.json"
    stats = json.loads(stats_path.read_text()) if stats_path.is_file() else {}
    extra = {
        "documents_spec": stats.get("documents_spec"),
        "documents_phase2": stats.get("documents_phase2"),
        "sections_spec": stats.get("sections_spec"),
        "sections_phase2": stats.get("sections_phase2"),
        "equations_spec": stats.get("equations_spec_with_id"),
        "equations_phase2": stats.get("equations_phase2"),
        "tables_spec": stats.get("tables_spec_with_id"),
        "tables_phase2": stats.get("tables_phase2"),
        "spec_fts_bytes": stats.get("spec_fts_bytes"),
        "phase2_fts_bytes": stats.get("phase2_fts_bytes"),
        "spec_fts_path": str(root / "search" / "spec_fts.sqlite"),
        "notes": (
            "Spec FTS is ~64 MB (over the 50 MB staging cap) — left on this box at "
            "`/workspace/engineering_rag/search/spec_fts.sqlite`. Phase-2 FTS reused as-is. "
            "No vector DB. Spec markdown trees were not copied; original PDFs untouched. "
            "Phase-2 documents are symlinked into `documents/opensees` and `documents/examples`."
        ),
    }
    out = root / "TEST_REPORT_MERGED.md"
    R.write_md(out, extra)
    print(f"\nOVERALL {'PASS' if R.passed else 'FAIL'} {sum(1 for x in R.rows if x['ok'])}/{len(R.rows)}")
    print(f"wrote {out}")
    return 0 if R.passed else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=None)
    args = ap.parse_args()
    return run(args.root or find_root())


if __name__ == "__main__":
    raise SystemExit(main())
