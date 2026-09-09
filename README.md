# Steltic Grok Bot - turn Grok Bot into your structural steel design assistant

No external RAG required, everything is done inside Grok Bot.

This repository is the **whole Steltic Grok Bot setup**: four bots that work together so you can start designing buildings and running nonlinear checks. It is **standards-free**. The seven copyrighted specifications are **not** included in any form — no PDFs, no converted text, no spec indexes. Each site supplies its own licensed PDFs and converts them locally with the tooling here. See `NOTICE.md`.

## Watch the setup video on my website at [stelticai.com](https://stelticai.com)

## What's in the repo

```
skills/
  Skill_query_file_manager_PACKAGED.md   load into the Query file manager bot
  Skill_querying_PACKAGED.md             load into HR Steel App, CFS Steel App, and Steltic Nonlinear
  Skill_SNL_PACKAGED.md                  load into Steltic Nonlinear (with Skill_querying_PACKAGED.md)
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

Companion repos (cloned by the design / nonlinear bots, not shipped here):

- https://github.com/Steltic/steltic — HR Steel App engine
- https://github.com/Steltic/steltic_cfs — CFS Steel App engine
- https://github.com/Steltic/steltic_nonlinear — Steltic Nonlinear (SNL): pushover + NLRHA + DDM in one pass

## Fastest install — one Admin prompt (recommended)

Create **one** new Grok Bot named **Admin** (or any name you like). Paste **Prompt A** below into that bot once. Admin creates the four teammate bots and sends each its Prompt 1 + Prompt 2 setup. You only create one bot and paste once.

### Prompt A — paste into Admin

```
You are the site Admin for a new Steltic Grok Bot install. Create four teammate Grok Bots (use CreateAgent), then message each one its setup prompts so they bootstrap themselves. Do not design buildings yourself.

Create these bots (names exact):
1. Query file manager
2. HR Steel App
3. CFS Steel App
4. Steltic Nonlinear

Then SendToAgent each bot the messages below, in order 1→4. For each bot: first send Prompt 1, wait until they confirm the skill is loaded (or send both in one message clearly labeled Prompt 1 then Prompt 2). Report back when all four have been created and messaged.

=== Query file manager — Prompt 1 ===
Load skills/Skill_query_file_manager_PACKAGED.md from https://github.com/Steltic/steltic_grokbot as a skill.

=== Query file manager — Prompt 2 ===
Clone https://github.com/Steltic/steltic_grokbot onto your computer. Copy scripts/ to /workspace/engineering_rag/scripts and engineering_rag_phase2/ into /workspace/engineering_rag/. Create a Python venv at /workspace/engineering_rag/.venv, install Docling 2.123.1 (do not upgrade it without revalidation), and set TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/ and DOCLING_DEVICE=cpu. Tell me when that bootstrap is done.

(After Prompt 2, remind the user: Supply the specs — place your own licensed PDFs in the working-folder standards/. Follow the first-run sequence in the Query file manager skill. The Bot will run retrieval checks on the converted specifications, revise as needed, then report when they are ready for design. Also convert ASCE/SEI 41-23 and ANSI/AISC 342-22 with stems ASCE_41_23 and AISC_342_22 for Steltic Nonlinear.)

=== HR Steel App — Prompt 1 ===
Load skills/Skill_querying_PACKAGED.md from https://github.com/Steltic/steltic_grokbot as a skill.

=== HR Steel App — Prompt 2 ===
Clone https://github.com/Steltic/steltic onto your computer. Install it per the README (Python 3.12, pip install -e . — openseespy needs native libs, install those too). Verify by running the app with model MOCK and confirming a design package appears. Then read contract/AGENT_START.md: for future design tasks you will follow that contract yourself — write cfg.py, run the engine via python in your terminal, fill the calc package, run consistency.check, and deliver report.html + viewer_3d.html. Let me know after you complete the MOCK tests, then Run the first example building end to end that way.

=== CFS Steel App — Prompt 1 ===
Load skills/Skill_querying_PACKAGED.md from https://github.com/Steltic/steltic_grokbot as a skill (same file as HR).

=== CFS Steel App — Prompt 2 ===
Clone https://github.com/Steltic/steltic_cfs onto your computer. Install it per the README (Python 3.12, pip install -e . — openseespy needs native libs, install those too). Verify by running the app with model MOCK and confirming a design package appears. Then read contract/AGENT_START.md and contract/CFS_REFERENCE.md: for future design tasks you will follow that contract yourself — write cfg.py, run the engine via python in your terminal, fill the calc package, run consistency.check, and deliver report.html + viewer_3d.html. Let me know after you complete the MOCK tests, then Run the first example building end to end that way.

=== Steltic Nonlinear — Prompt 1 ===
Load two skills from https://github.com/Steltic/steltic_grokbot: skills/Skill_querying_PACKAGED.md and skills/Skill_SNL_PACKAGED.md.

=== Steltic Nonlinear — Prompt 2 ===
Clone https://github.com/Steltic/steltic_nonlinear onto your computer, next to the Steltic (HR) repository (the DDM step needs its steel_engine folder). Create a Python 3.12 venv (openseespy only ships wheels for 3.10–3.12) and pip install -e . in the repo. Set STELTIC_ENGINE_DIR to the absolute path of steltic/steel_engine.

Verify the install on the packaged example (no retrieval needed):
  python -m snl inspect examples/Ex22_SMF
  python -m snl report  examples/Ex22_SMF
  python -m pytest tests -q
  python -m snl run examples/Ex22_SMF --only pushover --params examples/Ex22_SMF/hinge_params_ex22_aisc342.json

Open examples/Ex22_SMF/steltic_viewer_bundle.html and flip through the four viewers.

From now on, for every job, follow skills/Skill_SNL_PACKAGED.md: inspect the HR package zip; send ONE wave-1 retrieval plan to Query file manager; fill the job hinge_params.json from excerpts; run python -m snl run <zip> --params <job>_hinge_params.json --steltic-engine $STELTIC_ENGINE_DIR --parallel 2; judge pushover, NLRHA and DDM; deliver the job folder with four_analyses.html, steltic_viewer_bundle.html, narrative, retrieval_log.md and open items. Product defaults are in docs/PRODUCT_DEFAULTS.md (NLRHA ModIMK→PZ×1→fibre; dual-gate; CFS DDM Tier 2; HR DDM/NSP fibre+mesh 10%).

Report back: example Omega in X and Y, BSE-2N targets, viewer bundle confirmed.
```

## Install (manual — four bots)

If you prefer to create each bot yourself: create **Query file manager**, **HR Steel App**, **CFS Steel App**, and **Steltic Nonlinear**. Do them in this order. When the steps below are done, all four are ready.

### 1. Query file manager — two prompts

**Prompt 1.** Load `skills/Skill_query_file_manager_PACKAGED.md` as a skill.

**Prompt 2.** Paste this into the bot:

```
Clone https://github.com/Steltic/steltic_grokbot onto your computer. Copy scripts/ to /workspace/engineering_rag/scripts and engineering_rag_phase2/ into /workspace/engineering_rag/. Create a Python venv at /workspace/engineering_rag/.venv, install Docling 2.123.1 (do not upgrade it without revalidation), and set TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/ and DOCLING_DEVICE=cpu. Tell me when that bootstrap is done.
```

Supply the specs: place your own licensed PDFs in the working-folder `standards/`. Follow the first-run sequence in the Query file manager skill. The Bot will run through multiple examples of text retrieval from the converted specifications to confirm their accuracy, make any necessary revisions to them, then report back when they are ready for use in design.

For Steltic Nonlinear you also need `ASCE_41_23` and `AISC_342_22` in the corpus (in addition to the seven design stems). Place those PDFs in `standards/` and convert with those canonical stems.

### 2. HR Steel App — two prompts

**Prompt 1.** Load `skills/Skill_querying_PACKAGED.md` as a skill.

**Prompt 2.** Paste this into the bot:

```
Clone https://github.com/Steltic/steltic onto your computer. Install it per the README (Python 3.12, pip install -e . — openseespy needs native libs, install those too). Verify by running the app with model MOCK and confirming a design package appears. Then read contract/AGENT_START.md: for future design tasks you will follow that contract yourself — write cfg.py, run the engine via python in your terminal, fill the calc package, run consistency.check, and deliver report.html + viewer_3d.html. Let me know after you complete the MOCK tests, then Run the first example building end to end that way.
```

### 3. CFS Steel App — two prompts

**Prompt 1.** Load `skills/Skill_querying_PACKAGED.md` as a skill (same file as HR).

**Prompt 2.** Paste this into the bot:

```
Clone https://github.com/Steltic/steltic_cfs onto your computer. Install it per the README (Python 3.12, pip install -e . — openseespy needs native libs, install those too). Verify by running the app with model MOCK and confirming a design package appears. Then read contract/AGENT_START.md and contract/CFS_REFERENCE.md: for future design tasks you will follow that contract yourself — write cfg.py, run the engine via python in your terminal, fill the calc package, run consistency.check, and deliver report.html + viewer_3d.html. Let me know after you complete the MOCK tests, then Run the first example building end to end that way.
```

### 4. Steltic Nonlinear — two prompts

**Prompt 1.** Load `skills/Skill_querying_PACKAGED.md` and `skills/Skill_SNL_PACKAGED.md` as skills.

**Prompt 2.** Paste this into the bot:

```
Clone https://github.com/Steltic/steltic_nonlinear onto your computer, next to the Steltic (HR) repository (the DDM step needs its steel_engine folder). Create a Python 3.12 venv (openseespy only ships wheels for 3.10–3.12) and pip install -e . in the repo — that installs pushover, nlrha, steltic_ddm, the snl orchestrator, openseespy, numpy, scipy and matplotlib; the P-695 ground-motion library ships in records/. Set STELTIC_ENGINE_DIR to the absolute path of steltic/steel_engine.

Verify the install on the packaged example, no retrieval needed:
  python -m snl inspect examples/Ex22_SMF
  python -m snl report  examples/Ex22_SMF
  python -m pytest tests -q
  python -m snl run examples/Ex22_SMF --only pushover --params examples/Ex22_SMF/hinge_params_ex22_aisc342.json

Open examples/Ex22_SMF/steltic_viewer_bundle.html and flip through the four viewers with the module strip.

From now on, for every job, follow skills/Skill_SNL_PACKAGED.md: python -m snl inspect <zip>; send ONE wave-1 retrieval plan to Query file manager (AISC_342_22, ASCE_41_23, ASCE7 Ch.16, AISC_341_22); fill the job copy of hinge_params.json from the excerpts and set verified=true only when every needed block is cited; run python -m snl run <zip> --params <job>_hinge_params.json --steltic-engine $STELTIC_ENGINE_DIR --parallel 2; judge pushover, NLRHA and DDM each with its own protocol; deliver the job folder (pushover/, nlrha/, ddm_*, steltic_viewer_bundle.html, four_analyses.html, snl_summary.json) with your four-analyses narrative, retrieval_log.md and open items. Product defaults: docs/PRODUCT_DEFAULTS.md.

Report back now: the example's Omega in X and Y, the BSE-2N target displacements, and confirm the viewer bundle opened.
```

## Canonical stems (do not rename)

`AISC_360_22` · `AISC_341_22` · `AISC_358_22` · `ASCE7` · `AISI_S100` · `AISI_S240` · `AISI_S400_20`

Plus for Steltic Nonlinear: `ASCE_41_23` · `AISC_342_22`

Edition is part of the stem where the tree was converted with one; `AISI_S100` and `AISI_S240`
have no edition suffix and must stay that way so retrieval `doc` ids match the skills.

**Locked editions:** AISC 360-22, 341-22, 358-22 · ASCE/SEI 7-22 · AISI S100-16 (R2020) w/S3,
S240-20, S400-20 · ASCE/SEI 41-23 · ANSI/AISC 342-22. The skills' id traps and honest-absence lists are edition-specific facts —
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
