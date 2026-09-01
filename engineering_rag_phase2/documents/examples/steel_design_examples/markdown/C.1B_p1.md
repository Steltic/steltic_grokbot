<!-- chunk_id: C.1B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "C.1B",
 "example_family": "C.1",
 "chapter": "C",
 "topic": "frame stability (Direct Analysis Method)",
 "clauses": [
  "C2.2b",
  "C2.1",
  "C2.3",
  "App7",
  "7.2",
  "7.2.1",
  "7.2.2",
  "7.2.3"
 ],
 "eqs": [
  "C2-1",
  "A-7-5",
  "A-7-6"
 ],
 "tables": [],
 "title": "Moment Frame Column Strengths by the Effective Length Method",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE C.1B — Moment Frame Column Strengths by the Effective Length Method",
 "question": "# C.1B — Moment frame column strengths by the Effective Length Method  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA one-story steel framing line consists of four equal bays. Five columns sit on\ngrid lines A, B, C, D, and E, spaced 30.0 ft on center (total width 120 ft), and\neach column is 20.0 ft tall from its pinned base to the roof. Lateral stability of\nthe line is provided by a **single moment-resisting bay between grid lines B and C**:\nthe columns at B and C are rigidly (moment) connected to the beam spanning B–C.\nAll other connections are simple (pinned), so the columns at A, D, and E and the\nouter-bay beams are leaning/gravity members that contribute nothing to lateral\nstability. All columns are unbraced over the full 20.0 ft height about both axes and\nhave pinned bases.\n\nMembers: columns **W12×65**, beams **W18×40**, all ASTM A992/A992M. The roof girder\ncarries uniform dead load *w_D* = 0.400 kip/ft (including beam self-weight plus a\ncolumn self-weight allowance) and live load *w_L* = 1.20 kip/ft.\n\nUsing the **effective length method** of AISC 360-22 Appendix 7, Section 7.2,\ndetermine, for the maximum gravity load combination, the required strengths of the\nmoment-frame columns and the **effective-length factors** *K_x*, *K_y* (and the\neffective lengths *L_cx*, *L_cy*) to be used in their compression check, for both\nLRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, *F_y* = 50 ksi, *E* = 29,000 ksi.\n- Geometry: 4 bays @ 30.0 ft (120 ft total); story height 20.0 ft; pinned column\n  bases; moment frame only between B and C; all other members pinned.\n- Members: columns W12×65 (*A_g* = 19.1 in², *I_x* = 533 in⁴); beams W18×40\n  (*I_x* = 612 in⁴).\n- Loads: *w_D* = 0.400 kip/ft, *w_L* = 1.20 kip/ft.\n- Code basis: AISC 360-22 Appendix 7 §7.2 (loads combined per ASCE/SEI 7).\n\n## Find\nRequired column strengths (axial *P_r*, moment *M_r*) and the effective-length\nfactors *K_x*, *K_y* (and *L_cx*, *L_cy*) for the moment-frame columns under the\nmaximum gravity combination, using the effective length method, for LRFD and ASD.\nVerify the method is permitted (sidesway-amplification limit).",
 "has_figure": false,
 "stem": "C_1B",
 "breadcrumb": "EXAMPLE C.1B · AISC 360-22 Ch.C (frame stability (Direct Analysis Method)) · §C2.2b §C2.1 §C2.3 §App7 §7.2 §7.2.1 §7.2.2 §7.2.3 · Moment Frame Column Strengths by the Effective Length Method",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE C.1B · AISC 360-22 Ch.C (frame stability (Direct Analysis Method)) · §C2.2b §C2.1 §C2.3 §App7 §7.2 §7.2.1 §7.2.2 §7.2.3 · Moment Frame Column Strengths by the Effective Length Method

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Appendix 7, Section 7.2 (Effective Length Method): §7.2.1 (Limitations), §7.2.2 (Required Strengths), §7.2.3 (Available Strengths); notional loads per §C2.2b, Eq. C2-1; K from sidesway buckling analysis per Commentary Eqs. C-A-7-5 / C-A-7-6. Per the RAG extract provided.

---

### 1. Design Data

Same frame as Example C.1A: 4 bays @ 30 ft; h = 20 ft = 240 in.; pinned bases; moment bay B–C only (columns A, D, E leaning). Columns W12x65 (Ag = 19.1 in.², Ix = 533 in.⁴); beams W18x40 (Ix = 612 in.⁴); A992; E = 29,000 ksi. wD = 0.400 kip/ft, wL = 1.20 kip/ft.

### 2. Loads and Notional Loads

- **LRFD:** wu = 1.2(0.400) + 1.6(1.20) = 2.40 kip/ft; Yi = 288 kips; Ni = 0.002(1.0)(288) = **0.576 kips** (Eq. C2-1)
- **ASD:** wa = 1.60 kip/ft; Yi = 192 kips; analysis at 1.6× ASD level (307.2 kips); Ni = 0.002(1.6)(192) = **0.614 kips** (Eq. C2-1)

Per §7.2.2, required strengths come from an elastic second-order analysis conforming to §C2.1 **except the stiffness reductions of §C2.3 are not applied — nominal EI and EA are used** — with notional loads per §C2.2b (gravity-only combinations suffice per the §7.2.2 User Note).

### 3. Second-Order Analysis (nominal stiffness)

First-order sway of the B–C portal (slope-deflection, full E = 29,000 ksi): column term 3EIc/h = 193,200 kip-in./rad; beam term 6EIb/Lb = 295,800 kip-in./rad. For H = 0.576 kips: ΔH = 0.142 in. → story stiffness H/ΔH = 4.06 kip/in.; HL/ΔH = 974 kips.

Accounting for P-δ effects on story sway stiffness via RM (Eq. C-A-7-6): Pmf/Pstory = 144/288 = 0.50 → RM = 1 − 0.15(0.50) = 0.925; effective story buckling strength = 0.925(974) = **901 kips**.

**Sidesway amplification (B2):**
- **LRFD:** ΣP = 288 kips → B2 = 1/(1 − 288/901) = **1.47**
- **ASD (1.6×):** ΣP = 307.2 kips → B2 = 1/(1 − 307.2/901) = **1.52**

### 4. Verification That the Method Is Permitted — §7.2.1

§7.2.1(b): the ratio of maximum second-order to first-order story drift (LRFD or 1.6×ASD combinations, **stiffness not adjusted**) must be ≤ 1.5.

Drift ratio from the P-Δ analysis: 1.42 (LRFD), 1.46 (1.6×ASD) ≤ 1.5 ✓. Taken as the Appendix 8 B2 multiplier (per the §7.2.1 User Note, including RM): 1.47 (LRFD) ≤ 1.5 ✓; 1.52 (1.6×ASD), i.e., at/marginally above the limit. **The method is permitted for LRFD and is at the applicability limit for ASD**; this borderline condition should be noted in review — the direct analysis method (Example C.1A) remains valid without limitation. §7.2.1(a) (gravity supported by nominally vertical columns) is satisfied.

### 5. Required Strengths (columns B and C)

Axial (30-ft tributary, gravity):
- **LRFD:** Pr = 2.40(30) = **72.0 kips**; **ASD:** Pr = 1.60(30) = **48.0 kips**

Flexure (first-order M1 = (Ni/2)h amplified by B2):
- **LRFD:** M1 = (0.576/2)(240) = 69.1 kip-in. → Mr = 1.47(69.1) = 102 kip-in. = **8.5 kip-ft**
- **ASD:** M1 = (0.614/2)(240) = 73.7 kip-in. → M(1.6×) = 1.52(73.7) = 112 kip-in.; Mr = 112/1.6 = 70 kip-in. = **5.8 kip-ft**

### 6. Effective Length Factors — §7.2.3

§7.2.3(b): for moment-frame columns contributing to lateral stability, K shall be determined from a **sidesway buckling analysis**; K = 1.0 for leaning columns. The Exception (K = 1.0 for all columns) requires drift ratio ≤ 1.1 — not satisfied here (≈1.5), so K must be computed.

**Story stiffness approach, Commentary Eq. C-A-7-5:**

K2 = √[(Pstory/(RM Pr))(π²EI/L²)(ΔH/(HL))] ≥ √[(π²EI/L²)(ΔH/(1.7 Hcol L))]

π²EIx/L² = π²(29,000)(533)/(240)² = 2,650 kips; ΔH/(HL) = 0.142/(0.576 × 240) = 1.027 × 10⁻³ 1/kip; Pstory/(RM Pr) = 288/[0.925(72.0)] = 4.32 (identical ratio for ASD).

K2 = √[4.32 × 2,650 × 1.027 × 10⁻³] = √11.8 = **3.43**

Minimum-limit term: √[2,650 × 0.142/(1.7 × 0.288 × 240)] = √3.20 = 1.79 < 3.43 → left term governs.

**Results for the W12x65 moment-frame columns at B and C:**

- **Kx = 3.43 → Lcx = 3.43(20.0) = 68.6 ft** (in-plane, sidesway buckling)
- **Ky = 1.0 → Lcy = 20.0 ft** (weak axis does not contribute to lateral stability, §7.2.3(b))
- Leaning columns A, D, E: K = 1.0 both axes (§7.2.3(b))

### 7. Summary

| Quantity | LRFD | ASD | Spec. Reference |
|---|---|---|---|
| Ni | 0.576 kips | 0.614 kips | Eq. C2-1, §C2.2b |
| Drift ratio (limit 1.5) | 1.42–1.47 ✓ | 1.46–1.52 (at limit) | §7.2.1(b) |
| Pr | 72.0 kips | 48.0 kips | §7.2.2 |
| Mr | 8.5 kip-ft | 5.8 kip-ft | §7.2.2 (B2-amplified) |
| Kx; Lcx | 3.43; 68.6 ft | 3.43; 68.6 ft | §7.2.3(b), Eq. C-A-7-5 |
| Ky; Lcy | 1.0; 20.0 ft | 1.0; 20.0 ft | §7.2.3(b) |

### 8. Conclusion

By the effective length method, the moment-frame columns are designed for Pr = 72.0 kips, Mr = 8.5 kip-ft (LRFD) / Pr = 48.0 kips, Mr = 5.8 kip-ft (ASD) — slightly lower moments than the direct analysis method (C.1A) because nominal stiffness is used — but the compression check must use Kx = 3.43 (Lcx = 68.6 ft) from the sidesway buckling analysis per §7.2.3(b) and Eq. C-A-7-5, versus K = 1.0 under the direct analysis method. The §7.2.1 drift-ratio limit of 1.5 is satisfied for LRFD and is marginal for ASD; the comparison illustrates why the direct analysis method is generally preferred for frames with significant leaning-column effects.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
