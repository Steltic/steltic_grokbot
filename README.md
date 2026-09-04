# Steltic Grok Bot - turn Grok Bot into your structural steel design assistant

No external RAG required, everything is done inside Grok Bot.

This repository is the **whole Steltic Grok Bot setup**: three bots that work together so you can start designing buildings. It is **standards-free**. The seven copyrighted specifications are **not** included in any form â€” no PDFs, no converted text, no spec indexes. Each site supplies its own licensed PDFs and converts them locally with the tooling here. See `NOTICE.md`.

## Try the hosted version of Steltic for free using our servers [stelticai.com](https://stelticai.com)

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
  documents/opensees/â€¦                   OpenSees / OpenSeesPy documentation chunks
  documents/examples/â€¦                   worked-example chunks (_p1 id family)
  indexes/  search/  scripts/            phase-2 index slices + FTS + standalone search CLI
LICENSE  NOTICE.md
```

## Install (new site)

Create three Grok Bots: **Query file manager**, **HR Steel App**, **CFS Steel App**. Do them in this order. When the steps below are done, all three are ready to design buildings.

### 1. Query file manager â€” two prompts

**Prompt 1.** Load `skills/Skill_query_file_manager_PACKAGED.md` as a skill.

**Prompt 2.** Paste this into the bot:

```
Clone https://github.com/Steltic/steltic_grokbot onto your computer. Copy scripts/ to /workspace/engineering_rag/scripts and engineering_rag_phase2/ into /workspace/engineering_rag/. Create a Python venv at /workspace/engineering_rag/.venv, install Docling 2.123.1 (do not upgrade it without revalidation), and set TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/ and DOCLING_DEVICE=cpu. Tell me when that bootstrap is done.
```

Supply the specs: place your own licensed PDFs in the working-folder `standards/`. Follow the first-run sequence in the Query file manager skill. The Bot will run through multiple examples of text retrieval from the converted specifications to confirm their accuracy, make any necessary revisions to them, then report back when they are ready for use in design.

### 2. HR Steel App â€” two prompts

**Prompt 1.** Load `skills/Skill_querying_PACKAGED.md` as a skill.

**Prompt 2.** Paste this into the bot:

```
Clone https://github.com/Steltic/steltic onto your computer. Install it per the README (Python 3.12, pip install -e . â€” openseespy needs native libs, install those too). Verify by running the app with model MOCK and confirming a design package appears. Then read contract/AGENT_START.md: for future design tasks you will follow that contract yourself â€” write cfg.py, run the engine via python in your terminal, fill the calc package, run consistency.check, and deliver report.html + viewer_3d.html. Let me know after you complete the MOCK tests, then Run the first example building end to end that way.
```

### 3. CFS Steel App â€” two prompts

**Prompt 1.** Load `skills/Skill_querying_PACKAGED.md` as a skill (same file as HR).

**Prompt 2.** Paste this into the bot:

```
Clone https://github.com/Steltic/steltic_cfs onto your computer. Install it per the README (Python 3.12, pip install -e . â€” openseespy needs native libs, install those too). Verify by running the app with model MOCK and confirming a design package appears. Then read contract/AGENT_START.md and contract/CFS_REFERENCE.md: for future design tasks you will follow that contract yourself â€” write cfg.py, run the engine via python in your terminal, fill the calc package, run consistency.check, and deliver report.html + viewer_3d.html. Let me know after you complete the MOCK tests, then Run the first example building end to end that way.
```

## Canonical stems (do not rename)

`AISC_360_22` Â· `AISC_341_22` Â· `AISC_358_22` Â· `ASCE7` Â· `AISI_S100` Â· `AISI_S240` Â· `AISI_S400_20`

Edition is part of the stem where the tree was converted with one; `AISI_S100` and `AISI_S240`
have no edition suffix and must stay that way so retrieval `doc` ids match the skills.

**Locked editions:** AISC 360-22, 341-22, 358-22 Â· ASCE/SEI 7-22 Â· AISI S100-16 (R2020) w/S3,
S240-20, S400-20. The skills' id traps and honest-absence lists are edition-specific facts â€”
re-verify every one before applying any of this to a different edition.

## Ground rules (enforced by the skills)

- Retrieval-accuracy first: TableFormer ACCURATE, formula enrichment ON, OCR fallback,
  `--chunk-pages 5`; never lower accuracy settings.
- No vector database of spec text. Verbatim excerpts only; `found: false` is an honest answer;
  never invent a citation, id, or Ï†/Î© factor.
- Only `corpus=specification` + `part=standard` may supply design values; examples and OpenSees
  content are not authoritative.
- Spec-derived content never leaves the Query file manager computer (see `NOTICE.md` and the
  `.gitignore` guards).

## License

Scripts and skill documents: MIT (see `LICENSE`). Data collections and excluded content:
see `NOTICE.md`.
