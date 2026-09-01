<!-- chunk_id: C.1A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "C.1A",
 "example_family": "C.1",
 "chapter": "C",
 "topic": "frame stability (Direct Analysis Method)",
 "clauses": [
  "C1",
  "C2.2b",
  "C2.3",
  "C3",
  "C2.1"
 ],
 "eqs": [
  "C2-1",
  "C2-2a"
 ],
 "tables": [],
 "title": "Moment Frame Column Strengths by the Direct Analysis Method",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE C.1A — Moment Frame Column Strengths by the Direct Analysis Method",
 "question": "# C.1A — Moment frame column strengths by the Direct Analysis Method  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA one-story steel framing line consists of four equal bays. Five columns sit on\ngrid lines A, B, C, D, and E, spaced 30.0 ft on center (total width 120 ft), and\neach column is 20.0 ft tall measured from its pinned base to the roof. A roof\ngirder runs continuously across the top. Lateral stability of the line is provided\nby a **single moment-resisting bay between grid lines B and C**: the two columns at\nB and C are rigidly (moment) connected to the beam spanning B–C. Every other\nconnection in the line is a simple (pinned) connection, so the columns at A, D, and\nE and the beams in the outer bays are \"leaning\"/gravity members that carry vertical\nload but contribute nothing to lateral stability. All columns are unbraced over\ntheir full 20.0 ft height about both principal axes and have pinned bases.\n\nMembers: the columns are **W12×65** and the beams are **W18×40**. All steel is\nASTM A992/A992M. A uniform gravity load acts along the roof girder: dead\n*w_D* = 0.400 kip/ft (this value already includes beam self-weight plus an\nallowance for column self-weight) and live *w_L* = 1.20 kip/ft.\n\nUsing the **direct analysis method** of AISC 360-22 Chapter C, determine, for the\nmaximum gravity load combination, the required axial and flexural strengths of the\nmoment-frame columns and the effective-length factors (and effective lengths) to be\nused in their compression-strength check. Provide results for both LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, *F_y* = 50 ksi, *E* = 29,000 ksi.\n- Geometry: 4 bays @ 30.0 ft (120 ft total); story height 20.0 ft; pinned column\n  bases; moment frame only between grid lines B and C; all other members pinned.\n- Members: columns W12×65 (*A_g* = 19.1 in², *I_x* = 533 in⁴); beams W18×40\n  (*I_x* = 612 in⁴).\n- Loads (uniform on girder): *w_D* = 0.400 kip/ft, *w_L* = 1.20 kip/ft.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nRequired column strengths (axial *P_r* and moment *M_r*) and the effective-length\nfactors *K_x*, *K_y* (and *L_cx*, *L_cy*) for the moment-frame columns under the\nmaximum gravity combination, using the direct analysis method, for LRFD and ASD.",
 "has_figure": false,
 "stem": "C_1A",
 "breadcrumb": "EXAMPLE C.1A · AISC 360-22 Ch.C (frame stability (Direct Analysis Method)) · §C1 §C2.2b §C2.3 §C3 §C2.1 · Moment Frame Column Strengths by the Direct Analysis Method",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE C.1A · AISC 360-22 Ch.C (frame stability (Direct Analysis Method)) · §C1 §C2.2b §C2.3 §C3 §C2.1 · Moment Frame Column Strengths by the Direct Analysis Method

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter C (Direct Analysis Method): §C1, §C2.2b (Eq. C2-1), §C2.3 (Eqs. C2-2a/b), §C3. Per the RAG extract provided.

---

### 1. Design Data

| Item | Value |
|---|---|
| Geometry | 4 bays @ 30 ft (120 ft); story height h = 20 ft = 240 in.; pinned bases |
| Lateral system | Single moment bay B–C; columns A, D, E are leaning (gravity) columns |
| Columns | W12x65 (A992): Ag = 19.1 in.², Ix = 533 in.⁴ |
| Beams | W18x40: Ix = 612 in.⁴ |
| Loads | wD = 0.400 kip/ft, wL = 1.20 kip/ft (uniform on girder) |

### 2. Load Combinations (maximum gravity)

- **LRFD:** wu = 1.2(0.400) + 1.6(1.20) = 2.40 kip/ft → total story gravity Yi = 2.40(120) = 288 kips
- **ASD:** wa = 0.400 + 1.20 = 1.60 kip/ft → Yi = 1.60(120) = 192 kips

Per §C1, all load-dependent effects are calculated at LRFD load level or **1.6 × ASD** load level; for ASD the analysis is run at 1.6(192) = 307.2 kips and results divided by 1.6.

### 3. Direct Analysis Method Requirements Applied

**(a) Notional loads (system imperfections), §C2.2b, Eq. C2-1:** Ni = 0.002αYi

- **LRFD (α = 1.0):** Ni = 0.002(1.0)(288) = **0.576 kips**
- **ASD (α = 1.6):** Ni = 0.002(1.6)(192) = **0.614 kips** (applied at the 1.6× analysis level)

Notional load is applied at the roof, distributed as the gravity load, in the destabilizing direction (§C2.2b(b)). Because (as verified below) the second-order/first-order drift ratio ≤ 1.7, Ni is required only in gravity-only combinations (§C2.2b(d)) — which is the combination considered here.

**(b) Stiffness reductions, §C2.3:** 0.80 applied to all stiffnesses (§C2.3(a)), plus τb on flexural stiffness (§C2.3(b)):

Pns = FyAg = 50(19.1) = 955 kips.
- LRFD: αPr/Pns ≈ 1.0(72.0)/955 = 0.075 ≤ 0.5 → **τb = 1.0** (Eq. C2-2a)
- ASD: αPr/Pns = 1.6(48.0)/955 = 0.080 ≤ 0.5 → **τb = 1.0** (Eq. C2-2a)

Analysis stiffness = 0.8EI and 0.8EA throughout (E* = 0.8 × 29,000 = 23,200 ksi).

### 4. Required Axial Strength, Pr

The moment-frame columns at B and C support an approximately 30-ft tributary width of girder (interior supports; continuous-beam effects on reaction distribution are small relative to design margins and are neglected here, consistent with the gravity load allowance stated in the Given):

- **LRFD:** Pr = Pu = 2.40(30) = **72.0 kips** (plus ≈0.4 kip notional overturning component, negligible)
- **ASD:** Pr = Pa = 1.60(30) = **48.0 kips**

### 5. Required Flexural Strength, Mr (second-order analysis with reduced stiffness)

**First-order sway analysis (portal B–C, pinned bases, reduced stiffness):**
Each moment-frame column resists half the story shear; with pinned bases the column top moment is M1 = (H/2)h.

Story drift (slope-deflection, E* = 23,200 ksi): column term 3E*Ic/h = 154,600 kip-in./rad; beam term 6E*Ib/Lb = 236,600 kip-in./rad. For H = 0.576 kips (LRFD): Δ1 = 0.177 in. → story lateral stiffness K = H/Δ1 = 3.25 kip/in.

**P-Δ amplification (rigorous second-order effect, §C1(b)):**
Story sidesway capacity Pe,story = K·h = 3.25(240) = 779 kips.

- **LRFD:** ΣP = 288 kips → amplifier = 1/(1 − 288/779) = **1.59** (≤ 1.7 ✓, validating §C2.2b(d))
  M1 = (0.576/2)(240) = 69.1 kip-in. → Mr = 1.59(69.1) = 110 kip-in. = **9.2 kip-ft**
- **ASD (at 1.6× level):** ΣP = 307.2 kips → amplifier = 1/(1 − 307.2/779) = **1.65** (≤ 1.7 ✓)
  M1 = (0.614/2)(240) = 73.7 kip-in. → M(1.6×) = 1.65(73.7) = 122 kip-in.; Mr = 122/1.6 = 76 kip-in. = **6.3 kip-ft**

(Leaning columns A, D, E carry gravity only; their destabilizing P-Δ effect is included in ΣP above, as required by §C1.)

### 6. Effective Lengths for the Compression Check — §C3

Section C3: "the available strengths of members and connections shall be calculated in accordance with the provisions of Chapters D through K … with no further consideration of overall structure stability. The effective length for flexural buckling of all members shall be taken as the unbraced length unless a smaller value is justified by rational analysis."

Therefore, for the W12x65 moment-frame columns:

- **Kx = Ky = 1.0**
- **Lcx = Lcy = 20.0 ft** (unbraced full height, both axes)

No sidesway-uninhibited K-factor (K > 1) is required — this is the central benefit of the direct analysis method.

### 7. Summary

| Quantity | LRFD | ASD | Spec. Reference |
|---|---|---|---|
| Notional load Ni | 0.576 kips | 0.614 kips | Eq. C2-1, §C2.2b |
| Stiffness used in analysis | 0.8EI, 0.8EA (τb = 1.0) | same | §C2.3, Eq. C2-2a |
| Pr (columns B, C) | 72.0 kips | 48.0 kips | — |
| Second-order amplification | 1.59 | 1.65 | §C1(b), §C2.1 |
| Mr (columns B, C) | 9.2 kip-ft | 6.3 kip-ft | — |
| Kx = Ky; Lcx = Lcy | 1.0; 20.0 ft | 1.0; 20.0 ft | §C3 |

### 8. Conclusion

By the direct analysis method, the moment-frame columns shall be designed as beam-columns (Chapter H interaction) for Pr = 72.0 kips with Mr = 9.2 kip-ft (LRFD), or Pr = 48.0 kips with Mr = 6.3 kip-ft (ASD), using K = 1.0 and Lc = 20.0 ft about both axes per §C3. All Chapter C requirements — second-order effects including leaning-column P-Δ (§C1), notional loads per Eq. C2-1 (§C2.2b), and the 0.8τb stiffness reductions per Eqs. C2-2a/b (§C2.3) — are satisfied; the drift ratio ≤ 1.7 permits notional loads in gravity-only combinations per §C2.2b(d).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
