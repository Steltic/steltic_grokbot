<!-- chunk_id: F.2-1B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.2-1B",
 "example_family": "F.2-1",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2.1",
  "F1"
 ],
 "eqs": [
  "F2-1"
 ],
 "tables": [],
 "title": "C15x33.9 Flexural Check, Continuously Braced (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.2-1B — C15x33.9 Flexural Check, Continuously Braced (Direct Specification)",
 "question": "# F.2-1B — Compact channel flexural member, continuously braced (check)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA C15×33.9 American Standard channel of ASTM A992/A992M steel (Fy = 50 ksi) is used as a\nsimply supported beam spanning 25 ft. Its compression flange is continuously braced along\nthe full length. The beam carries a required (factored/service) flexural demand of\nMu = 108 kip-ft (LRFD) and Ma = 71.9 kip-ft (ASD) at midspan.\n\nBy directly applying the AISC 360 Specification (not design-aid tables), determine the\navailable flexural strength of the C15×33.9 and confirm it is adequate in both LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Member: C15×33.9 channel; Zx = 50.8 in³.\n- Geometry: simply supported, L = 25 ft; compression flange continuously braced (Lb = 0).\n- Required strength: Mu = 108 kip-ft (LRFD), Ma = 71.9 kip-ft (ASD).\n- Code basis: AISC 360-22 (Chapter F).\n\n## Find\nThe available flexural strength (φ_b·Mn for LRFD and Mn/Ω_b for ASD) and whether the\nmember is adequate.",
 "has_figure": false,
 "stem": "F_2_1B",
 "breadcrumb": "EXAMPLE F.2-1B · AISC 360-22 Ch.F (beam flexure) · §F2.1 §F1 · C15x33.9 Flexural Check, Continuously Braced (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.2-1B · AISC 360-22 Ch.F (beam flexure) · §F2.1 §F1 · C15x33.9 Flexural Check, Continuously Braced (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2.1 (Eq. F2-1; channels bent about the major axis). φb = 0.90, Ωb = 1.67 (§F1). Per the RAG extract provided.

---

### 1. Required Strength

Given: Mu = **108 kip-ft** (LRFD); Ma = **71.9 kip-ft** (ASD).

### 2. Nominal Flexural Strength — Eq. F2-1

C15x33.9 (A992): compact channel bent about its major axis with the compression flange continuously braced → lateral-torsional buckling does not apply; the yielding limit state governs:

> Mn = Mp = FyZx (Eq. F2-1)

Mn = 50(50.8) = 2,540 kip-in. = **212 kip-ft**

### 3. Available Flexural Strength

- **LRFD:** φbMn = 0.90(212) = **190 kip-ft** ≥ 108 kip-ft ✓ (utilization 0.57)
- **ASD:** Mn/Ωb = 212/1.67 = **127 kip-ft** ≥ 71.9 kip-ft ✓ (utilization 0.57)

### 4. Conclusion

By direct application of Eq. F2-1, the continuously braced C15x33.9 provides φbMn = 190 kip-ft (LRFD) and Mn/Ωb = 127 kip-ft (ASD), comfortably exceeding the required strengths. **The member is adequate**, governed by yielding (full plastic moment).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
