# Steltic Engineering Retrieval — Query File Manager (standards-free distribution)

Install package for a **Query file manager** Grok Bot: a non-vector (exact-lookup + BM25/FTS)
retrieval system over structural-steel design specifications, plus the retrieval-plan skill for
the **HR Steel App** and **CFS Steel App** design bots.

This repository is **standards-free**. The seven copyrighted specifications are **not** included
in any form — no PDFs, no converted text, no spec indexes. Each site supplies its own licensed
PDFs and converts them locally with the tooling here. See `NOTICE.md`.

## What's in the repo

```
skills/
  Skill_query_file_manager_PACKAGED.md   load into the Query file manager bot
  Skill_querying_PACKAGED.md             load into HR Steel App and CFS Steel App
scripts/                                 conversion + retrieval pipeline (Python)
  convert_pdf.py  recover_image_pages.py  postprocess.py  validate.py
  build_index.py  search.py  serve_queue.py  validate_merged.py
  retrieval.py  pack_distributable.py  pipeline_fixes.py  aliases.json
engineering_rag_phase2/                  distributable phase-2 data (STANDARD, not optional):
  documents/opensees/…                   OpenSees / OpenSeesPy documentation chunks
  documents/examples/…                   worked-example chunks (_p1 id family)
  indexes/  search/  scripts/            phase-2 index slices + FTS + standalone search CLI
LICENSE  NOTICE.md
```

## Install (new site)

1. **Create the three Grok Bots:** `Query file manager`, `HR Steel App`, `CFS Steel App`.
   Load `skills/Skill_querying_PACKAGED.md` into BOTH design bots **first**, then
   `skills/Skill_query_file_manager_PACKAGED.md` into the Query file manager bot.
2. **Clone onto the Query file manager computer** and copy into the working root:
   ```
   git clone <this-repo> steltic-retrieval
   mkdir -p /workspace/engineering_rag
   cp -r steltic-retrieval/scripts /workspace/engineering_rag/scripts
   cp -r steltic-retrieval/engineering_rag_phase2/. /workspace/engineering_rag/
   ```
3. **Bootstrap the environment** (Docling pin **2.123.1**; see the skill for the
   only-upgrade-with-revalidation rule):
   ```
   python3 -m venv /workspace/engineering_rag/.venv
   source /workspace/engineering_rag/.venv/bin/activate
   pip install docling==2.123.1
   export TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/
   export DOCLING_DEVICE=cpu
   ```
4. **Supply the specs:** the user places their own licensed PDFs in their working-folder
   `standards/` (they must own them — never fetch copies from unofficial sources).
5. **Follow the first-run sequence in the Query file manager skill, in order** — convert ONE
   document at a time (`convert_pdf.py` → `recover_image_pages.py` → `postprocess.py` →
   `validate.py` must PASS), then indexes/FTS/queue, then the gold probes, then HR and CFS
   query-test suites. Production buildings are blocked until both test suites close.

## Canonical stems (do not rename)

`AISC_360_22` · `AISC_341_22` · `AISC_358_22` · `ASCE7` · `AISI_S100` · `AISI_S240` · `AISI_S400_20`

Edition is part of the stem where the tree was converted with one; `AISI_S100` and `AISI_S240`
have no edition suffix and must stay that way so retrieval `doc` ids match the skills.

**Locked editions:** AISC 360-22, 341-22, 358-22 · ASCE/SEI 7-22 · AISI S100-16 (R2020) w/S3,
S240-20, S400-20. The skills' id traps and honest-absence lists are edition-specific facts —
re-verify every one before applying any of this to a different edition.

## Ground rules (enforced by the skills)

- Retrieval-accuracy first: TableFormer ACCURATE, formula enrichment ON, OCR fallback,
  `--chunk-pages 5`; never lower accuracy settings.
- No vector database of spec text. Verbatim excerpts only; `found: false` is an honest answer;
  never invent a citation, id, or φ/Ω factor.
- Only `corpus=specification` + `part=standard` may supply design values; examples and OpenSees
  content are not authoritative.
- Spec-derived content never leaves the Query file manager computer (see `NOTICE.md` and the
  `.gitignore` guards).

## License

Scripts and skill documents: MIT (see `LICENSE`). Data collections and excluded content:
see `NOTICE.md`.
