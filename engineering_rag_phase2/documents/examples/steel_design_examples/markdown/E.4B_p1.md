<!-- chunk_id: E.4B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.4B",
 "example_family": "E.4",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E2",
  "E3",
  "E1",
  "App7",
  "7.2"
 ],
 "eqs": [
  "A-7-3",
  "E3-1",
  "E3-2",
  "E3-4"
 ],
 "tables": [],
 "title": "W-Shape Column in a Moment Frame, Effective Length Method (Pinned Base)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.4B — W-Shape Column in a Moment Frame, Effective Length Method (Pinned Base)",
 "question": "# E.4B — W-shape column in a moment frame, effective length method (pinned base)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nReconsider the interior moment-frame column of the two-story, sidesway-uninhibited\nframe, but with the column base pinned (rather than fixed) about the column x-x\n(strong) axis. Everything else is unchanged. Consider the same column line:\n\n- Lower segment A-B: foundation (A, pinned about x-x) to floor (B), height 14 ft.\n- Upper segment B-C: floor (B) to roof (C), height 14 ft.\n\nColumns are W14×82 over both stories. Girders frame in from both sides, spanning\n35 ft: W24×55 at the floor (joint B) and W18×50 at the roof (joint C). Out of plane,\nthe column is continuously braced (y-y fully supported), so in-plane (x-x) flexural\nbuckling with the alignment-chart effective length governs. Steel is ASTM A992/A992M.\n\nAccumulated gravity loads per segment: B-C: D = 41.5 kips, L = 125 kips;\nA-B: D = 100 kips, L = 300 kips.\n\nUsing the effective length method, determine whether the W14×82 column is adequate\n(LRFD and ASD). The change of base fixity affects only the lower segment A-B.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Columns: W14×82 (Ag = 24.0 in.², Ix = 881 in.⁴, rx = 6.05 in., ry = 2.48 in.,\n  rx/ry = 2.44). Story height 14 ft each.\n- Girders (span 35 ft, two per joint): roof W18×50 (Ix = 800 in.⁴);\n  floor W24×55 (Ix = 1,350 in.⁴).\n- Boundary conditions: base at A **pinned** about x-x; column continuously braced\n  about y-y.\n- Frame: sidesway uninhibited in the plane of the frame.\n- Loads (accumulated D and L per segment): B-C: D = 41.5, L = 125 kips;\n  A-B: D = 100, L = 300 kips.\n- Code basis: AISC 360 (effective length method, Appendix 7.2; loads per ASCE/SEI 7).\n\n## Find\nThe alignment-chart effective length factor K for the lower segment with a pinned\nbase, the available compressive strength φcPn (LRFD) and Pn/Ωc (ASD), and whether the\nW14×82 remains adequate.",
 "has_figure": false,
 "stem": "E_4B",
 "breadcrumb": "EXAMPLE E.4B · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §App7 §7.2 · W-Shape Column in a Moment Frame, Effective Length Method (Pinned Base)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.4B · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §App7 §7.2 · W-Shape Column in a Moment Frame, Effective Length Method (Pinned Base)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Appendix 7 §7.2 (effective length method; sidesway-uninhibited alignment chart, Commentary Fig. C-A-7.2, G per Comm. Eq. C-A-7-3; G = 10 at a pinned support per the App. 7 Commentary); §E2, §E3 (Eqs. E3-1, E3-2, E3-4). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strengths (unchanged from E.4A)

- **Segment B–C:** Pu = **250 kips**; Pa = **167 kips**
- **Segment A–B:** Pu = 1.2(100) + 1.6(300) = **600 kips**; Pa = **400 kips**

### 2. Stiffness Ratios and K (only A–B changes)

G_C = 1.38 and G_B = 1.63 as in E.4A. At the pinned base: **G_A = 10** (Commentary recommendation).

- **Segment B–C:** Kx ≈ **1.48** (unchanged) → Lcx = 20.7 ft
- **Segment A–B** (G = 10 / 1.63), from the sidesway-permitted chart relation: **Kx ≈ 2.05** → Lcx = 2.05(14) = **28.7 ft**

The pinned base substantially increases the lower-story effective length (Kx from 1.43 to ≈2.05).

### 3. Available Strength — §E3 (W14x82: Ag = 24.0 in.², rx = 6.05 in.; nonslender; y-y continuously braced)

**Segment A–B:** Lcx/rx = 28.7(12)/6.05 = **56.9** ≤ 113 → inelastic.
Fe = π²E/(56.9)² = **88.4 ksi** (Eq. E3-4)
Fn = (0.658^(50/88.4))(50) = (0.658^0.566)(50) = **39.5 ksi** (Eq. E3-2)
Pn = 39.5(24.0) = **947 kips** → **φcPn = 852 kips; Pn/Ωc = 567 kips**

**Segment B–C** (unchanged from E.4A): φcPn = 955 kips; Pn/Ωc = 635 kips.

### 4. Adequacy Check

| Segment | Kx | φcPn vs Pu (LRFD) | Pn/Ωc vs Pa (ASD) |
|---|---|---|---|
| B–C | 1.48 | 955 ≥ 250 ✓ (0.26) | 635 ≥ 167 ✓ (0.26) |
| A–B | 2.05 | 852 ≥ 600 ✓ (0.70) | 567 ≥ 400 ✓ (0.71) |

### 5. Conclusion

With the base pinned about the strong axis, the alignment-chart effective length factor of the lower segment increases to **Kx ≈ 2.05**, reducing its available strength about 11% relative to the fixed-base case (852 vs. 963 kips LRFD). The **W14x82 remains adequate for both segments** under LRFD and ASD, with the lower segment now at ~70% utilization. As in E.4A, in-plane §E3 flexural buckling governs because the weak axis is continuously braced; elastic G-values are used conservatively (inelastic τb reduction is permitted by the Commentary).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
