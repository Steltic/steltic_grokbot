#!/usr/bin/env python3
"""Package phase-2 (distributable) WITHOUT any standards-derived trees.

Spec PDFs, documents/standards/, spec FTS, and specification rows in
indexes/ are copyrighted and must never ship with the product.

Usage:
  python scripts/pack_distributable.py --out /tmp/engineering_rag_phase2_ship

Copies:
  documents/opensees, documents/examples
  search/phase2_fts.sqlite
  phase-2-only index slices
  scripts that work without specs (search.py still runs; spec FTS simply misses)

Never copies:
  documents/standards/**
  search/spec_fts.sqlite
  original PDFs
  specification records from unified indexes
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from retrieval import find_root  # noqa: E402

EXCLUDE = [
    "documents/standards/",
    "search/spec_fts.sqlite",
    "indexes derived from standards (collection=specification rows)",
    "original PDFs",
    "queue contents (may contain spec excerpts)",
]


def filter_index(rows, collection_ok=("opensees", "examples")):
    out = []
    for r in rows:
        coll = r.get("collection") or r.get("corpus") or r.get("group")
        if coll in collection_ok:
            out.append(r)
        elif r.get("source_collection") and r.get("authoritative") is False:
            if coll != "specification":
                out.append(r)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--root", type=Path, default=None)
    args = ap.parse_args()
    root = args.root or find_root()
    out = args.out
    if out.exists():
        shutil.rmtree(out)
    (out / "documents").mkdir(parents=True)
    (out / "indexes").mkdir()
    (out / "search").mkdir()
    (out / "scripts").mkdir()
    # copy trees (follow the merge symlinks)
    for name in ("opensees", "examples"):
        src = (root / "documents" / name).resolve()
        dst = out / "documents" / name
        shutil.copytree(src, dst, symlinks=False)
    src_fts = (root / "search" / "phase2_fts.sqlite").resolve()
    shutil.copy2(src_fts, out / "search" / "phase2_fts.sqlite")
    # phase-2-only indexes
    idx = root / "indexes"
    docs = json.loads((idx / "documents.json").read_text(encoding="utf-8"))
    secs = json.loads((idx / "sections.json").read_text(encoding="utf-8"))
    eqs = json.loads((idx / "equations.json").read_text(encoding="utf-8"))
    tbls = json.loads((idx / "tables.json").read_text(encoding="utf-8"))
    toc = json.loads((idx / "master_toc.json").read_text(encoding="utf-8"))
    aliases = json.loads((idx / "aliases.json").read_text(encoding="utf-8"))
    (out / "indexes" / "documents.json").write_text(
        json.dumps(filter_index(docs), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out / "indexes" / "sections.json").write_text(
        json.dumps(filter_index(secs), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out / "indexes" / "equations.json").write_text(
        json.dumps(filter_index(eqs), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out / "indexes" / "tables.json").write_text(
        json.dumps(filter_index(tbls), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    toc_ship = {
        "specification": {},
        "opensees": toc.get("opensees") or {},
        "examples": toc.get("examples") or {},
        "phase2_nav": toc.get("phase2_nav") or {},
    }
    (out / "indexes" / "master_toc.json").write_text(
        json.dumps(toc_ship, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out / "indexes" / "aliases.json").write_text(
        json.dumps(aliases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for name in (
        "search.py",
        "build_index.py",
        "serve_queue.py",
        "validate_merged.py",
        "pack_distributable.py",
        "retrieval.py",
        "aliases.json",
    ):
        src = root / "scripts" / name
        if src.is_file():
            shutil.copy2(src, out / "scripts" / name)
    readme = out / "README_DISTRIBUTABLE.md"
    readme.write_text(
        "# Distributable phase-2 package\n\n"
        "This tree is **standards-free**. The seven copyrighted specifications,\n"
        "`documents/standards/`, and `search/spec_fts.sqlite` are excluded.\n\n"
        "Exclude list:\n" + "\n".join(f"- {x}" for x in EXCLUDE) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
