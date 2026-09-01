<!-- chunk_id: H.1B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.1B",
 "example_family": "H.1",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "E3",
  "F2",
  "F3",
  "F6",
  "H1.1"
 ],
 "eqs": [
  "E3-1",
  "E3-2",
  "E3-4",
  "F2-2",
  "F2-5",
  "F2-6",
  "F3-1",
  "F6-1",
  "F6-2",
  "H1-1a"
 ],
 "tables": [],
 "title": "W14x99 Beam-Column, §H1.1 from First Principles",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.1B — W14x99 Beam-Column, §H1.1 from First Principles",
 "question": "# H.1B - W-shape under combined compression + biaxial bending, direct H1-1a (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W14x99 braced-frame column has pinned ends and an unbraced length of 14 ft about\nboth axes (Lcx = Lcy = 14.0 ft, K = 1.0). A second-order analysis including P-delta effects yields the\nrequired strengths below. Compute the available compressive and flexural strengths from first principles\n(AISC 360 Chapters E and F) and verify the member directly with the AISC 360-22 Section H1.1 interaction\nequation (Eq. H1-1a / H1-1b).\n\n| Required strength | LRFD | ASD |\n|---|---|---|\n| Axial (compression) | Pu = 400 kips | Pa = 267 kips |\n| Major-axis moment | Mux = 250 kip-ft | Max = 167 kip-ft |\n| Minor-axis moment | Muy = 80.0 kip-ft | May = 53.3 kip-ft |\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: W14x99 (A = 29.1 in^2, Zx = 173 in^3, Sx = 157 in^3, Zy = 83.6 in^3, Sy = 55.2 in^3,\n  Iy = 402 in^4, ry = 3.71 in, rts = 4.05 in, ho = 13.4 in, J = 5.37 in^4, bf/2tf = 9.36).\n- Geometry: Lcx = Lcy = 14.0 ft, pinned ends.\n- Loads: second-order required strengths (P-delta included).\n- Code basis: AISC 360-22.\n\n## Find\nWhether the W14x99 satisfies Section H1.1 (LRFD and ASD), computing Pc, Mcx, Mcy explicitly.",
 "has_figure": false,
 "stem": "H_1B",
 "breadcrumb": "EXAMPLE H.1B · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §E3 §F2 §F3 §F6 §H1.1 · W14x99 Beam-Column, §H1.1 from First Principles",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.1B · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §E3 §F2 §F3 §F6 §H1.1 · W14x99 Beam-Column, §H1.1 from First Principles

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §E3 (Eqs. E3-1, E3-2, E3-4), §F2/§F3 (Eqs. F2-2, F2-5, F2-6; F3-1), §F6 (Eqs. F6-1, F6-2), §H1.1 (Eq. H1-1a). φc = φb = 0.90; Ωc = Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strengths (second-order, P-δ included)

Pr = 400/267 kips; Mrx = 250/167 kip-ft; Mry = 80.0/53.3 kip-ft (LRFD/ASD). W14x99 (A992), Lcx = Lcy = Lb = 14.0 ft = 168 in.

### 2. Compressive Strength — §E3

Lc/ry = 168/3.71 = 45.3 → Fe = π²E/(45.3)² = 140 ksi (Eq. E3-4); inelastic (≤113):
Fn = (0.658^(50/140))(50) = **43.0 ksi** (Eq. E3-2); elements nonslender (bf/2tf = 9.36 ≤ 13.5; web ≤ 35.9).

Pn = 43.0(29.1) = 1,250 kips → **Pc = φcPn = 1,130 kips (LRFD); Pn/Ωc = 750 kips (ASD)**

### 3. Major-Axis Flexural Strength — §F2/§F3

Lp = 1.76(3.71)√580 = 157 in. = 13.1 ft (Eq. F2-5); Lr = 531 in. = 44.3 ft (Eq. F2-6, with Jc/(Sxho) = 2.55 × 10⁻³, rts = 4.05 in.)

Lp < Lb = 168 in. ≤ Lr → inelastic LTB (Eq. F2-2, Cb = 1.0 conservatively):
Mp = 50(173) = 8,650 kip-in.; 0.7FySx = 5,500 kip-in.
Mn,LTB = 8,650 − (3,160)[(168 − 157)/(531 − 157)] = 8,650 − 90 = **8,560 kip-in.**

Flange noncompact (9.36 > λpf = 9.15): Mn,FLB = 8,650 − 3,160(0.0141) = 8,610 kip-in. (Eq. F3-1) — LTB governs.

**Mnx = 8,560 kip-in. = 713 kip-ft → Mcx = 642 kip-ft (LRFD) / 427 kip-ft (ASD)**

### 4. Minor-Axis Flexural Strength — §F6

Yielding: Mn = FyZy ≤ 1.6FySy: 50(83.6) = 4,180 ≤ 4,420 → 4,180 kip-in. (Eq. F6-1)
FLB (noncompact flange, Eq. F6-2): Mn = 4,180 − (4,180 − 1,930)(0.0141) = **4,150 kip-in. = 346 kip-ft** ← governs

**Mcy = 311 kip-ft (LRFD) / 207 kip-ft (ASD)**

### 5. Interaction — §H1.1

Pr/Pc = 400/1,130 = 0.355 (LRFD); 267/750 = 0.356 (ASD) — both ≥ 0.2 → **Eq. H1-1a**:

Pr/Pc + (8/9)(Mrx/Mcx + Mry/Mcy) ≤ 1.0

- **LRFD:** 0.355 + (8/9)(250/642 + 80.0/311) = 0.355 + (8/9)(0.389 + 0.257) = 0.355 + 0.574 = **0.93 ≤ 1.0 ✓**
- **ASD:** 0.356 + (8/9)(167/427 + 53.3/207) = 0.356 + (8/9)(0.391 + 0.257) = 0.356 + 0.576 = **0.93 ≤ 1.0 ✓**

### 6. Conclusion

Computing Pc, Mcx, and Mcy explicitly from Chapters E and F — including the inelastic-LTB reduction about the strong axis (Lb just beyond Lp) and the noncompact-flange reduction about the weak axis — the W14x99 satisfies **Eq. H1-1a at 0.93** under both LRFD and ASD. **The member is adequate**, confirming the design-parameter check of Example H.1A.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
