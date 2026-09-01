<!-- chunk_id: H.1A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.1A",
 "example_family": "H.1",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "H1.1"
 ],
 "eqs": [
  "H1-1a"
 ],
 "tables": [],
 "title": "W14x99 Beam-Column, §H1.1 Interaction via Design Parameters",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.1A — W14x99 Beam-Column, §H1.1 Interaction via Design Parameters",
 "question": "# H.1A - W-shape under combined compression + biaxial bending, braced frame (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA braced-frame column is an ASTM A992/A992M W14x99 with pinned ends and an unbraced length of\n14 ft about both axes (Lcx = Lcy = 14.0 ft, K = 1.0). A second-order analysis that already includes\nP-delta effects gives the following required strengths. Verify the member is adequate by checking the\ncombined axial-flexural interaction of AISC 360-22 Section H1.1, organized with the available-strength\n\"design parameters\" p = 1/Pc, bx = (8/9)/Mcx, by = (8/9)/Mcy so the check reads p*Pr + bx*Mrx + by*Mry <= 1.0.\n\n| Required strength | LRFD | ASD |\n|---|---|---|\n| Axial (compression) | Pu = 400 kips | Pa = 267 kips |\n| Major-axis moment | Mux = 250 kip-ft | Max = 167 kip-ft |\n| Minor-axis moment | Muy = 80.0 kip-ft | May = 53.3 kip-ft |\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: W14x99 (A = 29.1 in^2, Zx = 173 in^3, Sx = 157 in^3, Zy = 83.6 in^3, Sy = 55.2 in^3,\n  Iy = 402 in^4, ry = 3.71 in, rts = 4.05 in, ho = 13.4 in, J = 5.37 in^4, bf/2tf = 9.36).\n- Geometry: Lcx = Lcy = 14.0 ft, pinned ends.\n- Loads: second-order required strengths listed above (P-delta already included).\n- Code basis: AISC 360-22.\n\n## Find\nWhether the W14x99 satisfies the Section H1.1 combined-force interaction (LRFD and ASD).",
 "has_figure": false,
 "stem": "H_1A",
 "breadcrumb": "EXAMPLE H.1A · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H1.1 · W14x99 Beam-Column, §H1.1 Interaction via Design Parameters",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.1A · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H1.1 · W14x99 Beam-Column, §H1.1 Interaction via Design Parameters

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §H1.1 (Eq. H1-1a), expressed with the available-strength parameters p = 1/Pc, bx = (8/9)/Mcx, by = (8/9)/Mcy. Available strengths per Chapters E and F (see companion Example H.1B for the first-principles derivation). Per the RAG extract provided.

---

### 1. Required Strengths (second-order, P-δ included)

| | LRFD | ASD |
|---|---|---|
| Pr | 400 kips | 267 kips |
| Mrx | 250 kip-ft | 167 kip-ft |
| Mry | 80.0 kip-ft | 53.3 kip-ft |

### 2. Available Strengths (W14x99, A992, Lc = Lb = 14.0 ft)

From Chapters E and F (computed in Example H.1B): Pc = φcPn = 1,130 kips / Pn,Ωc = 750 kips; Mcx = 642 kip-ft / 427 kip-ft; Mcy = 311 kip-ft / 207 kip-ft.

**Design parameters:**

| Parameter | LRFD | ASD |
|---|---|---|
| p = 1/Pc | 0.887 × 10⁻³ (kips)⁻¹ | 1.33 × 10⁻³ |
| bx = (8/9)/Mcx | 1.39 × 10⁻³ (kip-ft)⁻¹ | 2.08 × 10⁻³ |
| by = (8/9)/Mcy | 2.86 × 10⁻³ (kip-ft)⁻¹ | 4.29 × 10⁻³ |

### 3. Interaction Check — Eq. H1-1a (Pr/Pc = 0.355 ≥ 0.2 → H1-1a governs)

p·Pr + bx·Mrx + by·Mry ≤ 1.0

- **LRFD:** (0.887 × 10⁻³)(400) + (1.39 × 10⁻³)(250) + (2.86 × 10⁻³)(80.0) = 0.355 + 0.347 + 0.229 = **0.93 ≤ 1.0 ✓**
- **ASD:** (1.33 × 10⁻³)(267) + (2.08 × 10⁻³)(167) + (4.29 × 10⁻³)(53.3) = 0.356 + 0.348 + 0.229 = **0.93 ≤ 1.0 ✓**

### 4. Conclusion

The W14x99 braced-frame column **satisfies the §H1.1 combined-force interaction** with a ratio of 0.93 under both LRFD and ASD (Eq. H1-1a applicable since the axial term exceeds 0.2). The p–bx–by formulation reproduces the standard interaction check exactly while streamlining the arithmetic for repeated design passes.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
