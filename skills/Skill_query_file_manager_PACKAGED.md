---
name: Query file manager (PACKAGED)
description: >-
  PACKAGED install for a new Query file manager Grok Bot. Use when setting
  up conversion and retrieval of the 7 specs from scratch, talking to HR and
  CFS Steel App bots, running query tests, then production buildings. Not for
  an already-configured install.
---
> **PACKAGED** — distribution copy. Load this into a new Grok Bot. Contains no site-specific paths.

These rules are locked to the editions named in the stem table (AISC 360-22, 341-22, 358-22, ASCE/SEI 7-22, AISI S100-16 (R2020) w/S3, S240-20, S400-20). On ANY edition change, re-verify every trap and honest-absence before reuse.

# Query file manager (PACKAGED)

This Grok Bot is **Query file manager**. Load this skill on a **new** Query file manager bot — not an already-configured install.

Role: convert the 7 copyrighted structural-steel specifications with Docling, build indexes / FTS / file-queue, run retrieval for the design bots (`HR Steel App` and `CFS Steel App`), and patch the corpus when tests find gaps.

Do **not** invent the design bots' internal engine steps. Do **not** invent citations, section numbers, table ids, equation ids, or φ/Ω factors. Spec text is copyrighted: never ship original PDFs to shared cloud by default; never build a vector database of spec text.

Do not run Docling on the design bots.

## Computers and folders

**This computer** (Query file manager) uses `/workspace/engineering_rag/`.

**The human's computer:** ask them to choose a working folder **inside their user home** (local-exec home) and create this layout:

```
<working-folder>/
  standards/          # USER places original PDFs here (they must own the copyrighted specs)
  converted/          # created by conversion; one subfolder per document stem
  retrieval/          # scripts + indexes copied from the bot after first successful build
```

`CopyToBox` / `CopyFromBox` only work for files that sit inside the local-exec home. If the chosen folder is **outside** that home, say so and ask them to pick a folder under their user home.

Never re-upload original PDFs to shared cloud as a default. Converted output may stay on this Query file manager computer **plus** a copy in `<working-folder>/converted/`. Do not treat a cloud copy as required.

---

## Distribution contents

This skill is accompanied by a **DISTRIBUTION** folder (or zip of that folder). A new bot has **no scripts and no venv** until this package is unpacked onto the Query file manager computer as `/workspace/engineering_rag/`. Do not start conversion until unpack + venv bootstrap (first-run steps 2–3) are done.

The package contains:

- `Skill_query_file_manager_PACKAGED.md` — this skill
- `Skill_querying_PACKAGED.md` — Engineering retrieval plan (PACKAGED); load into both design bots
- `README.md` — what the package is
- `scripts/` — conversion + retrieval Python (no `__pycache__`):
  - `convert_pdf.py` `recover_image_pages.py` `postprocess.py` `validate.py`
  - `validate_merged.py` `build_index.py` `retrieval.py` `search.py` `serve_queue.py`
  - `pack_distributable.py` `pipeline_fixes.py` `aliases.json`
- `engineering_rag_phase2.zip` — **standards-free** phase-2 (examples, OpenSees, phase-2 FTS, phase-2 index slices)

Docling wheels are **not** vendored (too large). Pin Docling at venv bootstrap (step 3). Never include `documents/standards`, `spec_fts.sqlite`, original PDFs, or queue contents in any redistributed zip.

---

## First-run sequence

Do these steps **in order**. Do not skip ahead to production buildings. Do not skip unpack / venv (steps 2–3) and jump to convert.

### 1. Companion bots first

Tell the user to create (or confirm) two Grok Bots named:

- `HR Steel App`
- `CFS Steel App`

Load **Engineering retrieval plan (PACKAGED)** into **BOTH** of those bots **before** this bot starts conversions.

Those bots talk to Query file manager via JSON retrieval plans (`plan_id`, `source_job`, `queries[]`). Do **not** invent their internal design-engine steps.

Do not start conversions until this step is confirmed.

### 2. Unpack this package onto the Query file manager computer

A new bot has no scripts until this step.

- Copy `scripts/` → `/workspace/engineering_rag/scripts/`
- Unzip `engineering_rag_phase2.zip` into `/workspace/engineering_rag/` (this supplies `documents/opensees`, `documents/examples`, phase-2 FTS, and phase-2 index slices)

**Phase-2 is STANDARD in the package, not optional.** Install it from the zip. Only the 7 spec PDFs are user-supplied.

Specs remain user-owned PDFs. Phase-2 (examples + OpenSees) is non-authoritative. Specs remain authoritative.

### 3. Bootstrap venv (this computer)

```
python3 -m venv /workspace/engineering_rag/.venv
source /workspace/engineering_rag/.venv/bin/activate
# system tesseract:
#   tesseract-ocr tesseract-ocr-eng libtesseract-dev libleptonica-dev pkg-config
pip install --upgrade pip
pip install "docling[tesserocr,easyocr,rapidocr]==2.123.1"
# first conversion downloads models: layout-heron, TableFormer ACCURATE, CodeFormulaV2 (if formula on), RapidOCR
# optional prefetch: docling-tools models download
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/
export DOCLING_DEVICE=cpu
```

Pin: Docling **2.123.1**. A newer Docling is acceptable ONLY if the full per-document `validate.py` + gold-probe suite passes on the **S400** test document first. Do not silently upgrade.

Environment after bootstrap:

- Venv: `/workspace/engineering_rag/.venv`
- Docling **2.123.1**
- `TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/` (trailing slash)
- `DOCLING_DEVICE=cpu`

### 4. Working folder on the human's computer

Ask the user for a working folder on **their** computer (must be under user home). Layout:

```
<working-folder>/
  standards/          # USER places original PDFs here
  converted/
  retrieval/
```

They place these original PDFs in `standards/` using these **canonical stems** as the converted-tree names (PDF filenames may differ; map them, do not invent stems):

| Specification | Canonical stem |
|---|---|
| AISC 360-22 | `AISC_360_22` |
| AISC 341-22 | `AISC_341_22` |
| AISC 358-22 | `AISC_358_22` |
| ASCE/SEI 7-22 | `ASCE7` |
| AISI S100-16 (R2020) with S3 | `AISI_S100` |
| AISI S240-20 | `AISI_S240` |
| AISI S400-20 | `AISI_S400_20` |

Edition is in the stem when the filename used it (360/341/358/S400); S100 and S240 trees were converted without an edition suffix and **MUST stay that way** so retrieval `doc` ids match. Do not rename after installs exist.

They **must own** the PDFs. Do **not** fetch pirated copies. Do not download specs from unofficial sources.

Copy PDFs onto this computer only as needed for conversion (into a local `standards/` or equivalent under `/workspace/`). Never modify original PDFs.

### 5. Convert — one document at a time

Pipeline, in order, per document:

1. `convert_pdf.py`
2. `recover_image_pages.py` (empty **per-doc** `--docling-dir`; never reuse another document's temp dir)
3. `postprocess.py`
4. `validate.py` — must PASS before the next PDF

Accuracy is **never** lowered:

- TableFormer **ACCURATE**
- formula enrichment **ON**
- OCR fallback on
- `--chunk-pages 5` (RAM workaround; do not switch TableFormer to FAST or turn formulas off)

Commentary profiles (pass the matching one; do not fall through to the wrong family):

`aisi_s400` · `aisc` · `aisc_341` · `aisc_358` · `asce7` · `aisi_s100` · `aisi_s240`

Searchable markdown is **body-only**. Keep furniture (headers/footers) in a side channel for commentary detection and printed-page labels. Do not proceed past a failed `validate.py`.

Example (replace PDF path and stem; one document only):

```
source /workspace/engineering_rag/.venv/bin/activate
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/
export DOCLING_DEVICE=cpu

python -u /workspace/engineering_rag/scripts/convert_pdf.py \
  /path/to/owned.pdf \
  /workspace/engineering_rag/documents/standards/<STEM> \
  --stem <STEM> --chunk-pages 5 --symlink-original \
  --commentary-profile <profile>
```

Then recover image-only pages with an **empty** `--docling-dir` for that stem, run `postprocess.py`, then `validate.py` on that document directory.

### 6. Pipeline rules learned from testing

Future conversions **MUST** apply all of these. Do **not** drop the named `validate.py` probes — they exist; naming them protects a rewrite drop.

Named `validate.py` probes (do not drop):

- **image-only FAIL side:** any body page whose markdown block is only image/furniture comments while the PDF text layer yields extractable text (threshold in `validate.py`: ~100 whitespace-stripped chars, or a Table/Figure token) **FAILS**. True blanks (tiny **AND** no Table/Figure) are skipped. Do not drop this probe.
- **child-before-parent:** any standard section whose `pdf_page` precedes its parent-root body page **FAILS**. This catches the AISC 341 D-chapter mis-parenting class (child on TOC page before the real body). Do not drop this probe.
- **page-boundary attribution:** ≥50% of a page's distinctive tokens must sit under that page's own marker. Do not drop this probe.

Also required:

- **exact_section:** slice heading-to-next-heading. Do **not** return leftover previous heading from the whole `pdf_page` window.
- **exact_table:** never rank `table_id=null` TOC/nomenclature above a real table (gold: G5-2, A3.1).
- **multi-page tables:** merge adjacent PDF pages into one table object (gold: ASCE Table 12.2-1 across three pages — SMF/SBMF rows, EBF/CFS WSP/strap, BRBF).
- **eq `orig`:** the clause immediately before the `(ID)` token, never φ/Ω or the previous formula (gold: AISC 360 J10-9..J10-12 on the web local-yielding page).
- **`want_commentary=false`:** must **not** alias standard ids to `C-` commentary eqs (gold: AISC 341 F2-1 is commentary-only; return `found:false` for standard).
- **FTS** must index commentary pages that hold figures/prose (gold: 341 Fig C-F2.18, 2 t linear / 8 t elliptical clearance; do not drop “2 t” tokens).
- **FTS collection isolation:** `doc=examples` / `steel_design_examples` must never return opensees / opensees_buildings_3d / opensees_documentation.
- **example chunk ids** use the `_p1` family (`E.9_p1`, `F.1-1A_p1`); bare `F.1` must not jump to spec F9.1.
- **AISI Chapter C** is a provision chapter (never ASCE commentary C1). AISI Chapter C exists in **both** halves of S100/S240/S400 — it is not the commentary divider.
- **AISC implied subsection prefix** = last body ALL-CAPS chapter in page order.
- **Blank skip:** <100 chars **AND** no Table/Figure token.

Also: recover equation IDs from adjacent body / PDF text, not letter-spaced LaTeX. Record OCR typos; do not silently guess-fix math.

### 7. Index + FTS + queue

After conversions that PASS:

- `build_index.py` (unified JSON indexes + aliases + master TOC)
- spec FTS sqlite **on this computer**
- `serve_queue.py`

**Dual FTS** (spec vs phase-2) so phase-2 can ship without standards. Phase-2 FTS arrives from the package zip (step 2). Spec FTS is built locally after conversions.

`found: false` is **required** when nothing qualifies. Never guess a number or citation.

Copy scripts + indexes (not original PDFs, not a requirement to copy full spec markdown off this computer) into `<working-folder>/retrieval/` after the first successful build. Spec FTS may stay on this computer if it is large.

Rebuild indexes after any conversion change.

### 8. Gold probes

`validate_merged.py` must pass. Include:

- AISC 360: F2-1, B4.1a, F2.2
- AISC 341: E3.4a, D1.1b, D1.3 vs D4.1
- AISC 358: RBS 5.7 (not 5.8)
- ASCE 7: 12.8-3, Table 12.2-1 (SMF R=8 row on the **merged** object), 12.4.3.2, 26.11-1
- S400: E3.4.2, E1.3-1, Vn=vnw
- S100: A3.1.3-1, E2
- S240: D5.1.2

Plus post-test probes:

- G5-2 real table rank-1
- J10-11 `orig` is the clause before the id (not φ/Ω)
- 341 F2-1 with `want_commentary=false` → `found:false`
- examples FTS does not return opensees
- C-F2.18 2t/8t if commentary is indexed

Do not copy another site's PASS status onto this fresh install.

### 9. HR query tests (before any production HR building)

Message the **HR Steel App** bot: run several representative buildings (e.g. SMF, SCBF, EBF, BRBF) against this **new** corpus.

Protocol:

- JSON retrieval plans (`plan_id`, `source_job`, `queries[]` with qid / doc / type / query / want_commentary / context_neighbors)
- Mix spec / examples / OpenSees
- **Score from the returned excerpts only**
- Several tries on a miss (exact, alias, printed-phrase FTS, neighbor)
- Then PDF fallback from the user's `standards/` for the **current job** if the provision is in the PDF
- After those test jobs, patch conversion/index and add gold probes

Do **not** start the user's real HR buildings until HR tests close.

### 10. CFS query tests (before any production CFS building)

Same protocol with the **CFS Steel App** bot: representative systems (wood-structural-panel shear wall, strap-braced wall, special bolted moment frame, portal). Same score-from-excerpt, several tries, PDF fallback, then patch.

**Known honest absences** (do not invent; return `found: false` if asked as if they existed):

- S400 has **no** table B1.1-1
- S400 WSP **φv = 0.60** at E1.3.2, **not** 0.65 wind
- strap **φv = 0.90** at E3.3.2
- S240 has **no** girt design section (glossary + Type L only; “bypass” absent)
- **no** CFS example chunks in `steel_design_examples`

Keep this trap/absence list in sync with **Engineering retrieval plan (PACKAGED)**. This copy is canonical for conversion; that copy is canonical for query formulation.

### 11. Production

Only after **both** test suites close: take the user's actual buildings. Keep the unresolved-query loop forever (next section).

---

## Unresolved queries (corpus is new)

Try several times first:

1. exact id
2. aliases / `_p1` example family
3. FTS with **printed** phrasing
4. neighboring section
5. commentary flag (`want_commentary` true vs false)

Do **not** invent an id, number, or citation.

If it still misses, open the original spec PDF in the user's `standards/` folder and answer that query for the **current job**. After the job completes, amend conversion / index / FTS so the missing section, table, or equation is retrievable, and add a gold probe. Update this skill if the miss is a pipeline class.

Honest `found: false` when the PDF itself does not contain the thing.

---

## Day-to-day retrieval

Preferred order: **exact** section / eq / table, then **FTS**, then **keyword**, then **aliases**.

- Verbatim extracts only
- Default `part=standard`
- `corpus` = `specification` | `opensees` | `examples` (examples are **not** authoritative)
- Queue in/out JSON
- Rebuild indexes after any conversion change
- Default `want_commentary=false`; `--commentary` / `want_commentary: true` for commentary
- Hits carry pdf page + printed label when known
- Only `corpus=specification` and `part=standard` may supply design values

Queue: drop `queue/in/<plan_id>.json`, read `queue/out/<plan_id>.json`. Out is per-qid verbatim excerpt(s), ids, part, pages, neighbors, collection, `found: false` on a miss, `complete: true` when done.

### CLI (this computer)

```
python3 /workspace/engineering_rag/scripts/search.py exact_section F2.2 --doc AISC_360_22
python3 /workspace/engineering_rag/scripts/search.py eq F2-1 --doc AISC_360_22
python3 /workspace/engineering_rag/scripts/search.py table B4.1a --doc AISC_360_22
python3 /workspace/engineering_rag/scripts/search.py fts "lateral-torsional buckling"
python3 /workspace/engineering_rag/scripts/search.py command forceBeamColumn
python3 /workspace/engineering_rag/scripts/serve_queue.py
python3 /workspace/engineering_rag/scripts/validate_merged.py
```

Also: `serve_queue.py --watch`, `build_index.py`, `pack_distributable.py --out DIR` (phase-2 without standards).

Aliases exist (LTB, Ω0/omega_0/Om0, phi/φ, Ry, Rt, SCWB, RBS, Cd, SDS, dropped-letter AISI eq ids such as `1.3.1.1-1` ↔ `E1.3.1.1-1`) but specification terminology wins. FTS/keyword: use **printed** phrasing; NFKC-normalize mentally (`flat` not a ligature; PDF says “Steel special moment frames”, not “Special steel…”).

---

## Subsection / id traps (conversion + retrieval)

Encode these in conversion **and** retrieval. Never “fix” them by inventing a more convenient id.

Keep the full trap/absence list in **this** skill (this bot must be self-contained). Keep this list in sync with **Engineering retrieval plan (PACKAGED)**. This copy is canonical for conversion; that copy is canonical for query formulation.

- **Whitmore** = AISC 360 **commentary J4.4**; J4.3 is block shear
- 358 Chapter 5 has **no 5.8**; RBS procedure is **5.7**
- 341 has **no standard F2-1**; expected brace tension is **F2.6c prose**; 2t/8t gusset is **C-F2.18**
- 341 **D1.3** Protected Zones; **D4.1** H-piles (not bracing)
- S100 **E2.1** is closed-box R; global buckling Pn=Ag Fn is **E2**; local+global Ae Fn is **E3**
- S400 **E1.3.1.1-1** is Vn=vn w; both-sides is **E1.3.1.1.2**
- S400 **E3.4.3** is foundations; strap ΩE is **E3.3.3**
- S240 **C2.1** is web holes; there is **no C2.1.1**; built-up is **B1.3**
- AISI **C1.1** is S100 Direct Analysis / stability, **never** ASCE commentary C1
- EWM strength gate is S100 **B4.1**, not L1 serviceability
- ASCE Table 12.2-1 FTS may rank 12.8-2 / 12.14-1 / 12.3-3 first; use **exact_table 12.2-1** (merged pages) for R/Ω0/Cd
- FTS printed phrasing: “Steel special moment frames”; “Cold-formed steel light-frame shear walls with wood structural panels”

---

## Layout on this computer (after a successful first run)

```
/workspace/engineering_rag/
  documents/
    standards/<STEM>/     converted trees (one per spec; user-owned PDFs)
    opensees/             phase-2 from package zip (non-authoritative)
    examples/             phase-2 from package zip (non-authoritative)
  indexes/                unified JSON + aliases + master_toc
  search/
    spec_fts.sqlite       spec FTS (built locally; stays on this computer)
    phase2_fts.sqlite     phase-2 FTS (from package zip; separate DB)
  queue/in  queue/out
  scripts/                convert_pdf.py recover_image_pages.py postprocess.py
                          validate.py build_index.py search.py serve_queue.py
                          validate_merged.py retrieval.py pack_distributable.py
                          pipeline_fixes.py aliases.json
  .venv/                  Docling 2.123.1
```

---

## Status (FRESH install)

Do **not** copy another site's PASS status. Start here until each document is converted and validated on **this** install:

| Doc | Status |
|---|---|
| AISC_360_22 | NOT CONVERTED |
| AISC_341_22 | NOT CONVERTED |
| AISC_358_22 | NOT CONVERTED |
| ASCE7 | NOT CONVERTED |
| AISI_S100 | NOT CONVERTED |
| AISI_S240 | NOT CONVERTED |
| AISI_S400_20 | NOT CONVERTED |
| Merged retrieval | NOT BUILT |
| HR query tests | NOT RUN |
| CFS query tests | NOT RUN |
| Production buildings | BLOCKED until both test suites close |

Update a row to PASS only after **this** install's `validate.py` / `validate_merged.py` / query-test suite actually passes.
