<!-- chunk_id: F.9B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.9B",
 "example_family": "F.9",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F8"
 ],
 "eqs": [
  "F8-1"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "Pipe 8 x-Strong Flexural Verification (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.9B — Pipe 8 x-Strong Flexural Verification (Direct Specification)",
 "question": "# F.9B — Pipe (round HSS) beam, available strength by the Specification  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nUsing the AISC Specification directly, determine the available flexural strength of a\nPipe 8 x-Strong beam. The beam spans 16 ft, is simply supported, and is braced at the end\npoints only (there is no deflection limit). Confirm that the section is not subject to a\nlocal-buckling reduction, identify the governing limit state, and report φ_b M_n (LRFD) and\nM_n/Ω_b (ASD).\n\n## Given\n- Material: ASTM A53/A53M Grade B (Fy = 35 ksi, E = 29,000 ksi).\n- Member: Pipe 8 x-Strong (Z = 31.0 in.³, D/t = 18.5).\n- Required strength (uniform load, 16-ft span): M_u = 61.4 kip-ft, M_a = 41.0 kip-ft.\n- Code basis: AISC 360-22.\n\n## Find\nThe applicable slenderness limits, the governing nominal flexural strength M_n, and the\navailable strengths φ_b M_n and M_n/Ω_b.",
 "has_figure": false,
 "stem": "F_9B",
 "breadcrumb": "EXAMPLE F.9B · AISC 360-22 Ch.F (beam flexure) · §F8 · Pipe 8 x-Strong Flexural Verification (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.9B · AISC 360-22 Ch.F (beam flexure) · §F8 · Pipe 8 x-Strong Flexural Verification (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F8 (Round HSS) applied directly: Table B4.1b Case 20 classification; Eq. F8-1. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Mu = **61.4 kip-ft** (LRFD); Ma = **41.0 kip-ft** (ASD). Simple span 16 ft, braced at ends only.

### 2. Slenderness Limits — Table B4.1b, Case 20

Compact limit: λp = 0.07E/Fy = 0.07(29,000)/35 = **58.0**
Noncompact limit: λr = 0.31E/Fy = 257; §F8 applicability: D/t < 0.45E/Fy = 373.

D/t = 18.5 ≤ 58.0 → **compact wall — no local-buckling reduction applies** (Eqs. F8-2 through F8-4 not invoked). LTB is not a limit state for round HSS, so the ends-only bracing condition has no effect.

### 3. Governing Limit State: Yielding — Eq. F8-1

Mn = Mp = FyZ = 35(31.0) = **1,090 kip-in. = 90.4 kip-ft**

### 4. Available Flexural Strength

- **LRFD:** φbMn = 0.90(90.4) = **81.4 kip-ft** ≥ 61.4 kip-ft ✓ (utilization 0.75)
- **ASD:** Mn/Ωb = 90.4/1.67 = **54.1 kip-ft** ≥ 41.0 kip-ft ✓ (utilization 0.76)

### 5. Conclusion

Direct application of §F8 confirms the Pipe 8 x-Strong (A53 Gr. B) is governed by **yielding at the full plastic moment** (Eq. F8-1): the D/t of 18.5 is far below the compact limit of 58.0, so no local-buckling reduction applies, and round members are exempt from LTB. Available strengths of 81.4 kip-ft (LRFD) and 54.1 kip-ft (ASD) comfortably exceed the required moments — **the member is adequate**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
