---
name: Check and clean converted PDFs
description: >-
  Procedure for an LLM agent (Claude, Grok, GPT, local) to verify a converted specification
  corpus before the design agents use it, and to clean what the checks find. Run after every
  Convert PDF, Re-process or Rebuild index. Works on any standard the pipeline converts, not
  only the seven it was written for.
---

# Check and clean converted PDFs

You are checking the corpus that `steltic_grokbot` built from the user's licensed PDFs. The
design agents cite it verbatim and are allowed to take design values only from records tagged
`corpus=specification, part=standard`. A converted corpus can be wrong in ways **no query
reveals**: the index answers, the answer looks plausible, and the text under an AISC 358
heading is AISC 341's. This procedure exists because that happened, and four rounds of retrieval
fixes were applied to the wrong layer before anyone looked at the records themselves.

Read the whole file before running anything. Do not paraphrase spec text in your report; quote
ids, page labels and counts.

## 0. Where things are

```
<workspace>/                     %LOCALAPPDATA%\Steltic\grokbot on the hub; /workspace/engineering_rag elsewhere
  structured/chunks/<stem>_pNNN_NNN.json   Docling output, 5 pages per file -- the expensive artefact, never edit
  markdown/<stem>.search.md                searchable body text (what the FTS holds), with pdf_page/printed_label/part markers
  markdown/pages_search/<stem>/page_NNN.md the same, one file per page
  tables/<stem>_*.md|csv|json              every table Docling found
  indexes/converted/*.json                 the CONVERTER's records (postprocess.py output), one set for all documents
  indexes/*.json                           the BUILDER's output (build_index.py): canonical ids, what retrieval reads
  indexes/build_stats.json, audit_report.md|json
  search/spec_fts.sqlite                   the FTS index
scripts/                                   audit_corpus.py  postprocess.py  build_index.py  search.py  validate.py
```

Two naming systems coexist. **Stems** are the PDF's filename (`A360_22`, `asce41_23`); **canonical
ids** are what queries use (`AISC_360_22`, `ASCE_41_23`). The converter writes stems; the builder
re-keys to canonical ids and remembers the stem in `converted_stem`. Never mix them up in a purge.

## 1. Run the audit first

```
python scripts/audit_corpus.py --root <workspace> --pdf-dir <folder with the source PDFs>
```

(or the hub's **Audit corpus** tab; **Rebuild index** also runs it). It prints and writes
`indexes/audit_report.md`. Exit status 1 means at least one **FAIL**.

| level | meaning | what you do |
|---|---|---|
| FAIL | the index will serve wrong records | fix before anyone designs against it (section 3) |
| WARN | retrieval works but misses text or shows noise | fix if the document matters; note otherwise |
| INFO | known limitation, nothing to do | mention in the report |

Do not argue with a FAIL. If you believe a FAIL is a false positive, prove it with the records
(section 2) and say so explicitly with the evidence.

## 2. Look at the records yourself

The audit is fast and generic; it cannot know a given standard. Spend ten minutes per document
on these, with Python on the JSON files, not by querying:

1. **Provenance.** Every section record has a `chunk` field naming the Docling file it came
   from. For document `X` with stem `S`, every chunk must start with `S_`. Count the ones that
   do not, and which stem they name. Anything above zero is contamination, whatever the label
   says.
2. **Duplicates.** Group section records by `(section_id, title, pdf_page, chunk, part)`.
   Any group larger than one means a re-process appended instead of replacing.
3. **Part vs boundary.** `documents.json` → `commentary_boundary.cover_pdf_page`. No record
   tagged `standard` may sit on or after that page; none tagged `commentary` before it. Open
   the cover page's text (`markdown/pages_search/<stem>/page_<cover>.md`, or `pdftotext -f N -l N`)
   and confirm it *is* the commentary cover ("COMMENTARY on the …", "CHAPTER C1"). If the
   standard has no separate commentary (inline C-sections), the boundary may legitimately be
   absent — say which case applies.
4. **Chapter coverage.** List the distinct chapter prefixes of `standard` section ids and compare
   with the document's own table of contents (front matter pages, or `pdftotext -l 15`). A
   missing chapter or a chapter with 3 records where the TOC shows 40 headings means headings
   were not captured (run-in headings, unqualified "1. / 2a." subsections, or a profile that does
   not know the document).
5. **Equation ids vs the PDF.** `pdftotext <pdf> - | grep -oE '\((C-?)?[A-Z]?[0-9]{1,2}(\.[0-9]+)*-[0-9]{1,3}[a-z]?\)' | sort -u`
   gives the ids the PDF prints. Compare with the unique `eq_id` values for that document. Big
   gaps mean the id grammar does not know the numbering style (`(7-1)` vs `(F2-1)` vs `(12.8-3)`).
   Then open five identified equations and compare `latex` with `orig`: they must be the same
   equation. If `latex` carries a printed id token like `( F 2 - 5 )` that differs from `eq_id`,
   the LaTeX belongs to another equation.
6. **Tables.** `TABLE X` captions in `markdown/<stem>.search.md` vs `table_id` values. Tables on
   roman-numbered pages (TOC, symbols, glossary) must have **no** id. Open the three most-cited
   tables of the standard (for AISC 341: A3.2, D1.1; AISC 360: B4.1b, J3.2) in `tables/` and read
   the cells against the PDF page: coefficients, φ/Ω, units.
7. **Text hygiene** in `markdown/<stem>.search.md`: control characters (`grep -cP '[\x00-\x08\x0b-\x1f]'`),
   split ligatures (`grep -c ' fi '`, `' fl '`), watermark or copyright lines, running headers
   (a line that opens most pages), Latin-1 letters standing in for operators (`þ ð Þ` for `+ ( )`),
   and stacked fractions read as two digits ("1 2 in." for 1½ in.).
8. **Document record.** `title`, `standard`, `edition`, `page_label_scheme`, `unvalidated`. A title
   naming another standard means the document matched no profile and inherited a fall-through.
   `unvalidated` means nobody has checked the page-label scheme or boundary against the PDF: do
   it now (steps 3 and the printed labels on three pages) and report what you found.
9. **Retrieval smoke.** For each document, three `exact_section` lookups (first, middle, last
   id), one `exact_equation`, one `exact_table`:
   `python scripts/search.py exact_section 5.7 --doc AISC_358_22 --root <workspace> --no-cache`.
   The hit must be that document, that id, and `part=standard` first. Then two prose queries the
   design agents actually send (the hub's `queue/` log has them): the top hits must be clauses,
   not table-of-contents pages (`spec-page:…` at a roman page label).

Record the numbers. "Looks fine" is not a finding.

## 3. Clean

Never edit `indexes/*.json` by hand, and never touch `structured/chunks/`. Everything below is
a re-process plus a rebuild; both are minutes, not hours, and neither needs Docling.

| finding | cause | fix |
|---|---|---|
| foreign chunks, duplicates, commentary-as-standard | stale record layers from earlier runs | **Re-process** the document (hub tab, or `postprocess.py <workspace> --stem <stem> --pdf <pdf> --indexes-dir <workspace>/indexes/converted`), then **Rebuild index**. With current code a re-process *replaces* the document's records; if the counts do not drop, the code is old — check `scripts/postprocess.py` has `purge_document` |
| no commentary split, or the split is on the wrong page | the commentary profile does not know this document | pass `--profile` (`aisc`, `aisc_341`, `aisc_358`, `aisc_342`, `asce7`, `asce41`, `aisi_s100`, `aisi_s240`, `aisi_s400`); if none fits, add a `CommentaryProfile` in `postprocess.py` with the cover-page regex you read on the PDF, and an `is_<doc>_doc()` sniffer for the title/edition |
| title/edition belong to another standard | no sniffer matched the stem | same: add the sniffer and the `write_indexes` branch; re-process |
| chapters missing, few sections for the page count | headings run into paragraphs, or "1. / 2a." subsections not qualified | run-in headings: extend `synthesize_asce_subsections` to the document; AISC-style numbered subsections: add the document to the gate in `synthesize_aisc_subsections`; re-process |
| few equation ids vs the PDF | the id grammar does not know the numbering | add a parenthesised-id regex for the style (see `ASCE41_EQ_PARENS_RE`, enabled per document in `run()`); re-process **with the PDF** — the census reads it |
| LaTeX printed with another id | Docling shifted enrichment across a batch | re-process; `realign_latex_by_printed_id` moves each block to the id printed inside it. Rows whose LaTeX names no id and is still wrong: leave, `orig` is right, note it |
| table ids missing although captions exist | table markdown recorded by a dead absolute path, or a caption form the regex does not know | re-process (paths are resolved by name now); for a new caption form extend `TABLE_ID_LINE_RE` |
| TOC/symbols tables carry an id | front matter treated as body | re-process; `is_front_matter_label` drops those ids. If the document's front matter is not roman-numbered, extend that function |
| split ligatures, control characters, watermark, `þ ð Þ` | Docling text layer | re-process **with the PDF** (the ligature repair uses the PDF's vocabulary); for a new watermark wording add a regex to `ASCE_WATERMARK_RES` or the document's running-title list |
| running header in the body text | furniture classified as body | add its regex to the document's `*_RUNNING_TITLE_RES` and the strip function; re-process |
| stacked fractions as two digits, math flattened in table cells, `=` dropped in LaTeX | Docling, not fixable here | report them; tell the design agents `orig` and the metric value are authoritative; use the PDF page for width-to-thickness tables |

After cleaning, **run the audit again** and repeat section 2 for the document you changed. Then
delete nothing until the user has seen the report; the converted chunks are their licensed
material and hours of Docling time.

## 4. Report

One markdown file per audit, beside the report the script wrote, with:

1. The audit summary table and the FAIL/WARN lines, verbatim.
2. Per document: chunk provenance count, duplicates, boundary page and what is printed on it,
   chapter list vs TOC, equation ids indexed vs printed, table ids vs captions, hygiene counts,
   and the five spot checks with the values you read on the PDF page next to the values in the
   record.
3. What you changed (which document re-processed with which profile/PDF, which code touched),
   and the audit result after.
4. What remains and why it cannot be fixed here.

State the acceptance criterion at the top: **zero FAIL, every document's boundary page verified,
spot checks agree with the PDF.** Below that line the corpus is not ready for design work.

## 5. Things that look wrong and are not

* A section id that exists in an older edition but not in the index (AISC 358-16 §5.8 vs 358-22
  §5.7): check the edition's own numbering before calling it a gap.
* Two records for the same id on the chapter's first page (`E3` at 16.1-38 and 16.1-40): AISC
  chapters open with a list of their sections. Retrieval prefers the body occurrence; harmless.
* Chapter-level records with an empty title (`5`, `6`): cosmetic.
* Equation rows with `source: pdf_text` and no LaTeX: the PDF prints the id where Docling found
  no formula item; the row carries the surrounding text so the id is still findable.
* A commentary that is inline (C-prefixed sections following each chapter): no boundary page
  exists; the C-sections should still be `part=commentary`.
