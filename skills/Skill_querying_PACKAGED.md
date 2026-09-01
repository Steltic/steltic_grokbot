---
name: Engineering retrieval plan (PACKAGED)
description: >-
  PACKAGED skill for HR Steel App and CFS Steel App Grok Bots. Use when those
  design bots must retrieve provisions from Query file manager: JSON plans,
  exact ids, no invented citations.
---
> **PACKAGED** — distribution copy. Load this into a new Grok Bot. Contains no site-specific paths.

These rules are locked to the editions named in the stem table (AISC 360-22, 341-22, 358-22, ASCE/SEI 7-22, AISI S100-16 (R2020) w/S3, S240-20, S400-20). On ANY edition change, re-verify every trap and honest-absence before reuse.

# Engineering retrieval plan (PACKAGED)

Load this on **HR Steel App**, **CFS Steel App**, and any steel-design Grok Bot that must retrieve provisions.

This is **NOT** the conversion skill. Do **not** run Docling. Do **not** convert PDFs. Do **not** invent citations, section numbers, table ids, equation ids, or φ/Ω factors.

**Query file manager** is a **separate** Grok Bot. Send **one JSON plan per wave**. Do **not** wait. Keep working. When results arrive, compute from the returned excerpts only.

Keep this trap/absence list in sync with **Query file manager (PACKAGED)**. That copy is canonical for conversion; this copy is canonical for query formulation.

Phase-2 (examples + OpenSees) ships with the Query file manager package and will be present after that bot's bootstrap. Design bots still must **not** invent if a lookup misses.

---

## Two stages (keep them separate)

- **STAGE 1 — this plan.** Write a JSON retrieval plan. Hand it to Query file manager. Continue other work.
- **STAGE 2 — compute.** Use only verbatim excerpts returned for this session. If a clause is missing, write a new plan. Do not fill gaps from memory.

Flow: what am I calculating → limit state → section → equation → variables → table → exceptions → example → **one JSON plan** → hand off → keep working → compute from verbatim text → verification plan → finalize.

---

## How to hand off

Send one JSON object per wave to Query file manager (message the bot, or drop the same JSON on the queue). Do not send a prose paragraph of the whole design problem.

Required fields:

- `plan_id` — unique id for this wave
- `source_job` — the building / job this wave belongs to
- `queries[]` — list of query objects

Each query:

| Field | Rules |
|---|---|
| `qid` | unique within the plan |
| `doc` | **one** canonical stem (see table). Do not search all seven blindly. |
| `type` | `exact_section` \| `exact_equation` \| `exact_table` \| `fts` \| `keyword` \| `command` \| `id` |
| `query` | for exact lookups: **id only**. Not a sentence. Not the document name. |
| `purpose` | why you need it (short) |
| `want_commentary` | default **false** (provisions). Set true only for intent/background. |
| `context_neighbors` | 0–2 typical; widen when the equation needs the surrounding “where:” |

```
good:  {"type":"exact_equation","doc":"AISC_360_22","query":"F2-1"}
bad:   {"type":"exact_equation","query":"AISC 360-22 Equation F2-1 Mn for compact I-shapes"}
```

FTS/keyword: specification terminology, one idea per query. Use **printed** phrasing (see traps). NFKC-normalize mentally (`flat` not a ligature; PDF says “Steel special moment frames”, not “Special steel…”).

Several plans may be in flight. Do not block on retrieval.

---

## Canonical `doc` ids

Aliases like `AISC 360-22` may work; **prefer the stem**. One `doc` per query.

| Cite as | `doc` |
|---|---|
| AISC 360-22 | `AISC_360_22` |
| AISC 341-22 | `AISC_341_22` |
| AISC 358-22 | `AISC_358_22` |
| AISI S100-16 (R2020) w/S3 | `AISI_S100` |
| AISI S240-20 | `AISI_S240` |
| AISI S400-20 | `AISI_S400_20` |
| ASCE/SEI 7-22 | `ASCE7` |
| phase-2 examples | `examples` or `steel_design_examples` |
| OpenSeesPy | `opensees` / `openseespy_documentation` |
| OpenSees Tcl/theory | `opensees_documentation` |

Edition is in the stem when the filename used it (360/341/358/S400); S100 and S240 trees were converted without an edition suffix and **MUST stay that way** so retrieval `doc` ids match. Do not rename after installs exist.

`type` values: `exact_section` | `exact_equation` | `exact_table` | `fts` | `keyword` | `command` | `id`

---

## What you get back

Per `qid`: verbatim excerpt(s), `corpus` (`specification` | `opensees` | `examples`), `part` (`standard` | `commentary` or `n/a`), section/eq/table ids, pdf + printed pages, neighbors, or **`found: false`** with nearest-ids / alias suggestions.

- `found: false` is **honest**. Do not fabricate a number or citation.
- Only `corpus=specification` and `part=standard` may supply design values.
- Examples / OpenSees are **not** authoritative. If they disagree with the spec, follow the spec.
- Commentary **ids** still resolve (`C26.5-5`, commentary `E3.4.2`, `C-F2.18`) when you ask for them. Default `want_commentary: false` must **not** silently alias a standard id to a `C-` commentary equation.

---

## HR vs CFS routing

Do **not** search all seven documents blindly — **one `doc` per query**.

| Bot | Search these | Do not default-search |
|---|---|---|
| **HR Steel App** | AISC 360 / 341 / 358 + ASCE7 + examples / OpenSees | AISI S100 / S240 / S400 unless the job is mixed |
| **CFS Steel App** | AISI S100 / S240 / S400 + ASCE7 + examples / OpenSees | AISC 360 / 341 / 358 unless the job is mixed |

Loads, combinations, R/Ω0/Cd, wind, seismic parameters → `ASCE7` for **both** bots.

---

## Corpus routing (what governs)

| Document | Governs |
|---|---|
| ASCE/SEI 7-22 | Loads, combinations, wind, seismic, R/Ω0/Cd (Table 12.2-1) |
| AISC 360-22 | Hot-rolled member/connection capacity, stability, B4.1 slenderness |
| AISC 341-22 | Hot-rolled seismic systems, SCWB, protected zones, capacity design |
| AISC 358-22 | Prequalified SMF/IMF connections; one chapter per type; **RBS is Chapter 5, procedure §5.7** (not 5.8) |
| AISI S100 | CFS member capacity, as-amended S2/S3 |
| AISI S240 | CFS framing (non-seismic system/QC) |
| AISI S400 | CFS seismic walls / SBMF; Table E1.3-1 |

Phase-2 (same interface, **not authoritative**): OpenSeesPy `command forceBeamColumn` / `Steel02`; Tcl/theory in `opensees_documentation`; `eq E3-2` finds worked examples that use that AISC equation. Example chunk ids use the **`_p1` family** (`E.9_p1`, `F.1-1A_p1`). Bare `F.1` must not be treated as spec F9.1. Phase-2 ships with the Query file manager package and will be present after that bot's bootstrap — still must not invent if a lookup misses.

AISI Chapter C is a **provision** chapter (stability / installation / seismic load effects) in **both** halves of S100/S240/S400. It is not the commentary divider. Do not treat it as ASCE commentary C1/C11.

---

## Formulate queries — 10 rules

1. **Never one giant question.** Batch the whole first wave into one plan.
2. **Material → system → member → loading → method → one `doc`.** Do not search all seven.
3. **Exact id when known.** If unknown: one navigation FTS or TOC, then exact in the next wave. Never invent an id.
4. **Spec words, not chat** (“lateral-torsional buckling”, not “bends sideways”). Aliases exist (LTB, Ω0/omega_0, phi/φ, SCWB, RBS) but spec terms win. Prefer **printed** phrasing.
5. **One type per query:** provision, definition, equation, limits, table, procedure, example, OpenSees command. For every equation you will compute: same plan also gets its “where:” variables, applicability, exceptions.
6. **Examples check sequence only.** If they disagree with the spec, follow the spec. Example ids: `_p1` family.
7. **`found: false` is honest.** Narrow if too broad; parent section / alias suggestions if too narrow. Do not fabricate.
8. **Waves:** (1) navigation + core provisions → (2) definitions, limits, cross-refs named in results → (3) digit-by-digit verification of every factor that entered the calc.
9. **Prefer F2 + F2-1 + B4.1a** over “all of Chapter F”. Widen with `context_neighbors` when the equation is unusable without the surrounding “where:”.
10. **Every number in the calculation must come from a verbatim excerpt this session.** Cite document, edition, provision|commentary, section, eq/table id, printed page.

---

## Id formats (`query` field)

```
ASCE7        section 12.4.3.2 · eq 12.8-3 · table 12.2-1 · table 26.11-1 · table C26.5-5
AISC_360_22  section F2.2 · eq F2-1 · table B4.1a
AISC_341_22  section E3.4a · table D1.1b · section D1.3 (Protected Zones) · section D4.1 (H-piles, not bracing)
AISC_358_22  section 5.7 · eq 5.7-4 · eq 15.6-1 (DuraFuse)   // not 5.8-x
AISI_S100    section E2 · eq A3.1.3-1
AISI_S240    section D5.1.2
AISI_S400_20 section E3.4.2 · table E1.3-1 · eq E1.3.1.1-1 (dropped-letter 1.3.1.1-1 also works)
```

Commentary uses a **`C-` prefix** on many equation/figure ids (AISC 341 `C-F2.18`, ASCE `C26.5-5`). Do not request a `C-` id with `want_commentary: false` and then invent a standard counterpart.

---

## Id traps (do not invent a “better” id)

Keep the full trap + honest-absence lists in **this** skill (this bot must be self-contained). Keep in sync with **Query file manager (PACKAGED)**; that copy is canonical for conversion, this copy is canonical for query formulation.

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
- Example chunks: `E.9_p1`, `F.1-1A_p1` — bare `F.1` must not jump to spec F9.1

### CFS honest absences (do not invent)

- S400 has **no** table B1.1-1
- S400 WSP **φv = 0.60** at E1.3.2, **not** 0.65 wind
- strap **φv = 0.90** at E3.3.2
- S240 has **no** girt design section (glossary + Type L only; “bypass” absent)
- **no** CFS example chunks in `steel_design_examples`

---

## Unresolved (after several tries)

Try, in order: exact id → aliases / `_p1` → FTS with printed phrasing → neighboring section → flip `want_commentary`.

If it still misses: **flag Query file manager**. Do **not** invent. Query file manager will PDF-fallback from the user's `standards/` for the current job and patch conversion/index after the job.

---

## Complete example JSON plan

```json
{
  "plan_id": "EX12-wave1",
  "source_job": "hr-smf-test-01",
  "submitted": "2026-09-01T05:00:00Z",
  "queries": [
    {
      "qid": "q1",
      "doc": "AISC_360_22",
      "type": "exact_section",
      "query": "F2",
      "purpose": "governing flexure procedure, compact I-shapes",
      "want_commentary": false,
      "context_neighbors": 1
    },
    {
      "qid": "q2",
      "doc": "AISC_360_22",
      "type": "exact_equation",
      "query": "F2-1",
      "purpose": "Mn yielding",
      "want_commentary": false,
      "context_neighbors": 1
    },
    {
      "qid": "q3",
      "doc": "AISC_360_22",
      "type": "exact_table",
      "query": "B4.1a",
      "purpose": "flange/web compactness",
      "want_commentary": false,
      "context_neighbors": 0
    },
    {
      "qid": "q4",
      "doc": "ASCE7",
      "type": "exact_table",
      "query": "12.2-1",
      "purpose": "R / Ω0 / Cd for steel SMF row on merged table object",
      "want_commentary": false,
      "context_neighbors": 0
    },
    {
      "qid": "q5",
      "doc": "AISC_341_22",
      "type": "exact_section",
      "query": "D1.3",
      "purpose": "Protected Zones (not D4.1 H-piles)",
      "want_commentary": false,
      "context_neighbors": 1
    },
    {
      "qid": "q6",
      "doc": "AISC_358_22",
      "type": "exact_section",
      "query": "5.7",
      "purpose": "RBS procedure (there is no 5.8)",
      "want_commentary": false,
      "context_neighbors": 1
    },
    {
      "qid": "q7",
      "doc": "examples",
      "type": "id",
      "query": "F.1-1A_p1",
      "purpose": "example sequence check; non-authoritative; _p1 family",
      "want_commentary": false,
      "context_neighbors": 0
    },
    {
      "qid": "q8",
      "doc": "opensees",
      "type": "command",
      "query": "forceBeamColumn",
      "purpose": "OpenSeesPy element command",
      "want_commentary": false,
      "context_neighbors": 0
    }
  ]
}
```

Query file manager is a separate Grok Bot. Send one JSON plan per wave. Do not wait. Do not run Docling. Do not invent citations.
