<!-- chunk_id: C.1C_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "C.1C",
 "example_family": "C.1",
 "chapter": "C",
 "topic": "frame stability (Direct Analysis Method)",
 "clauses": [
  "App7",
  "App8",
  "7.3",
  "7.3.1",
  "7.3.2",
  "7.3.3"
 ],
 "eqs": [
  "A-7-1",
  "A-7-2",
  "A-7-3",
  "A-8-3",
  "A-8-8"
 ],
 "tables": [],
 "title": "Moment Frame Column Strengths by the First-Order Analysis Method",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE C.1C — Moment Frame Column Strengths by the First-Order Analysis Method",
 "question": "# C.1C — Moment frame column strengths by the First-Order Analysis Method  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA one-story steel framing line consists of four equal bays. Five columns sit on\ngrid lines A, B, C, D, and E, spaced 30.0 ft on center (total width 120 ft), and\neach column is 20.0 ft tall from its pinned base to the roof. Lateral stability of\nthe line is provided by a **single moment-resisting bay between grid lines B and C**\n(columns at B and C moment-connected to the beam between them); all other\nconnections are simple, so the columns at A, D, and E and the outer-bay beams are\nleaning/gravity members. All columns are unbraced over the full 20.0 ft height about\nboth axes and have pinned bases.\n\nMembers: columns **W12×65**, beams **W18×40**, all ASTM A992/A992M. The roof girder\ncarries uniform dead load *w_D* = 0.400 kip/ft (including beam self-weight and a\ncolumn self-weight allowance) and live load *w_L* = 1.20 kip/ft.\n\nUsing the **first-order analysis method** of AISC 360-22 Appendix 7, Section 7.3,\ndetermine, for the maximum gravity load combination, the additional lateral load\n*N_i* to be applied, verify that the method's limitations are satisfied, and give the\neffective-length factors (and effective lengths) for the moment-frame columns.\nProvide LRFD and ASD results and state for which the method is valid.\n\n## Given\n- Material: ASTM A992/A992M, *F_y* = 50 ksi, *E* = 29,000 ksi.\n- Geometry: 4 bays @ 30.0 ft (120 ft total); story height 20.0 ft; pinned column\n  bases; moment frame only between B and C; all other members pinned.\n- Members: columns W12×65 (*A_g* = 19.1 in², *I_x* = 533 in⁴); beams W18×40\n  (*I_x* = 612 in⁴).\n- Loads: *w_D* = 0.400 kip/ft, *w_L* = 1.20 kip/ft.\n- Code basis: AISC 360-22 Appendix 7 §7.3 + Appendix 8 (B₁, B₂); loads per ASCE/SEI 7.\n\n## Find\nThe additional lateral load *N_i* (Eq. A-7-3), verification of the §7.3.1 limitations\n(Eqs. A-7-1, A-7-2 and the 1.5 drift-ratio limit), the B₁/B₂ amplifiers, and the\neffective-length factors *K_x*, *K_y* (and *L_cx*, *L_cy*) for the moment-frame\ncolumns under the maximum gravity combination. State validity for LRFD vs ASD.",
 "has_figure": false,
 "stem": "C_1C",
 "breadcrumb": "EXAMPLE C.1C · AISC 360-22 Ch.C (frame stability (Direct Analysis Method)) · §App7 §App8 §7.3 §7.3.1 §7.3.2 §7.3.3 · Moment Frame Column Strengths by the First-Order Analysis Method",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE C.1C · AISC 360-22 Ch.C (frame stability (Direct Analysis Method)) · §App7 §App8 §7.3 §7.3.1 §7.3.2 §7.3.3 · Moment Frame Column Strengths by the First-Order Analysis Method

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Appendix 7, Section 7.3 (First-Order Analysis Method): §7.3.1 (Limitations, Eqs. A-7-1, A-7-2), §7.3.2 (Eq. A-7-3, B1 requirement), §7.3.3 (Available Strengths); Appendix 8 (Eqs. A-8-3 through A-8-8). Per the RAG extract provided.

---

### 1. Design Data

Same frame as Examples C.1A/C.1B: 4 bays @ 30 ft; h = L = 20 ft = 240 in.; pinned bases; moment bay B–C only; columns W12x65 (Ag = 19.1 in.², Ix = 533 in.⁴); beams W18x40 (Ix = 612 in.⁴); A992. wD = 0.400 kip/ft, wL = 1.20 kip/ft.

- **LRFD:** wu = 2.40 kip/ft; Yi = 288 kips; Pr (cols B, C) = 72.0 kips
- **ASD:** wa = 1.60 kip/ft; Yi = 192 kips; Pr = 48.0 kips

### 2. Verification of Limitations — §7.3.1

**(a) Gravity supported by nominally vertical columns:** satisfied ✓

**(b) Axial force in nominally horizontal moment-frame members, Eq. A-7-1 (αPr ≤ 0.08Pe):**
The W18x40 girder of the moment bay carries negligible axial force under gravity (≈ the small notional shear only). Pe = π²EI/L² = π²(29,000)(612)/(360)² = 1,352 kips; 0.08Pe = 108 kips >> αPr ≈ 0 ✓

**(c) Drift ratio ≤ 1.5 (stiffness not adjusted):** Taken as B2 per the User Note, using Appendix 8 Eqs. A-8-6/A-8-7/A-8-8 with nominal stiffness. From the frame analysis (see C.1B): HL/ΔH = 974 kips; Pmf/Pstory = 0.50 → RM = 1 − 0.15(0.50) = 0.925 (Eq. A-8-8); Pe,story = 0.925(974) = 901 kips (Eq. A-8-7).

- **LRFD (α = 1.0):** B2 = 1/(1 − 288/901) = **1.47 ≤ 1.5 ✓**
- **ASD (α = 1.6):** B2 = 1/(1 − 1.6(192)/901) = 1/(1 − 307.2/901) = **1.52 > 1.5 ✗**

**(d) Eq. A-7-2 (αPr ≤ 0.5Pns):** Pns = FyAg = 50(19.1) = 955 kips; 0.5Pns = 478 kips.
LRFD: 1.0(72.0) = 72.0 ≤ 478 ✓; ASD: 1.6(48.0) = 76.8 ≤ 478 ✓

**Conclusion on validity: the first-order analysis method is permitted for LRFD but is NOT permitted for ASD** — limitation (c) is exceeded (1.52 > 1.5). For ASD, the direct analysis method (Example C.1A) must be used. ASD values below are reported for comparison only.

### 3. Additional Lateral Load — Eq. A-7-3 (§7.3.2(a))

> Ni = 2.1α(Δ/L)Yi ≥ 0.0042Yi  (Eq. A-7-3)

For the gravity-only combination the first-order drift Δ ≈ 0 (symmetric frame and loading), so the minimum governs:

- **LRFD:** Ni = 0.0042(288) = **1.21 kips**
- **ASD:** Ni = 0.0042(192) = **0.806 kips** (no 1.6 amplification of the analysis per the §7.3.2 User Note)

Ni is applied at the roof, distributed as the gravity load, in the destabilizing direction, in combination with the gravity loads.

### 4. Required Strengths (First-Order Analysis + B1)

First-order analysis (nominal stiffness): each moment-frame column resists Ni/2; with pinned bases the column top moment is M = (Ni/2)h:

- **LRFD:** M = (1.21/2)(240) = 145 kip-in. = 12.1 kip-ft
- **ASD:** M = (0.806/2)(240) = 96.8 kip-in. = 8.06 kip-ft

**B1 amplifier (§7.3.2(b); Eqs. A-8-3, A-8-4, A-8-5):** Cm = 0.6 − 0.4(M1/M2) = 0.6 (M1 = 0 at the pinned base); Pe1 = π²EI/Lc1² = π²(29,000)(533)/(240)² = 2,650 kips (EI* = EI for this method, per Eq. A-8-5 definition).

- LRFD: B1 = 0.6/(1 − 72.0/2,650) = 0.62 → **B1 = 1.0** (≥ 1 floor governs)
- ASD: B1 = 0.6/(1 − 1.6(48.0)/2,650) = 0.62 → **B1 = 1.0**

**Required strengths of columns B and C:**

- **LRFD:** Pr = 72.0 kips; Mr = 1.0(12.1) = **12.1 kip-ft**
- **ASD (comparison only):** Pr = 48.0 kips; Mr = **8.06 kip-ft**

### 5. Effective Lengths — §7.3 / §7.3.3

Section 7.3 permits design "using a first-order elastic analysis with the effective length, Lc, taken as the laterally unbraced length with K = 1.0," and §7.3.3 takes the effective length as the unbraced length:

- **Kx = Ky = 1.0; Lcx = Lcy = 20.0 ft** (all columns)

### 6. Summary

| Quantity | LRFD | ASD | Spec. Reference |
|---|---|---|---|
| Limitation (b), Eq. A-7-1 | ✓ | ✓ | §7.3.1(b) |
| Limitation (c), drift ratio ≤ 1.5 | 1.47 ✓ | 1.52 ✗ | §7.3.1(c); Eqs. A-8-6/7/8 |
| Limitation (d), Eq. A-7-2 | ✓ | ✓ | §7.3.1(d) |
| Ni | 1.21 kips | 0.806 kips | Eq. A-7-3 (0.0042Yi min.) |
| B1 | 1.0 | 1.0 | Eqs. A-8-3/4/5 |
| Pr; Mr | 72.0 kips; 12.1 kip-ft | 48.0 kips; 8.06 kip-ft* | §7.3.2 |
| K; Lc (both axes) | 1.0; 20.0 ft | 1.0; 20.0 ft | §7.3, §7.3.3 |

*Method not permitted for ASD; values for comparison only.

### 7. Conclusion

The first-order analysis method is **valid for the LRFD design** of this frame: the columns at B and C are designed for Pr = 72.0 kips and Mr = 12.1 kip-ft with K = 1.0 and Lc = 20.0 ft about both axes. Note that the built-in conservatism of Eq. A-7-3 (which assumes B2 = 1.5) yields a higher design moment (12.1 kip-ft) than the direct analysis method (9.2 kip-ft, Example C.1A). For **ASD the method is not permitted**, because the sidesway amplification at 1.6× ASD loads (B2 = 1.52) exceeds the 1.5 limit of §7.3.1(c); the direct analysis method of Chapter C shall be used instead.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
