<!-- chunk_id: E.4A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.4A",
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
 "title": "W-Shape Column in a Moment Frame, Effective Length Method (Fixed Base)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.4A — W-Shape Column in a Moment Frame, Effective Length Method (Fixed Base)",
 "question": "# E.4A — W-shape column in a moment frame, effective length method (fixed base)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn interior column of a multi-bay, two-story moment frame is to be checked for the\ngravity loads using the effective length method (alignment-chart K factors). The\nframe is sidesway uninhibited in the plane considered (it resists lateral load by\nframe action, and the lateral system has already been shown adequate). Consider one\ncolumn line over two stories:\n\n- Lower segment A-B: from the foundation (A) up to the floor (B), height 14 ft.\n- Upper segment B-C: from the floor (B) up to the roof (C), height 14 ft.\n\nThe columns are W14×82 over both stories. Girders frame into the column from both\nsides (a bay on each side) at each level, spanning 35 ft: W24×55 girders at the floor\n(joint B) and W18×50 girders at the roof (joint C). The base at A is fixed about the\ncolumn x-x (strong) axis. Out of plane, the column is continuously braced (the y-y\naxis is fully supported), so only in-plane (x-x) flexural buckling with the\nalignment-chart effective length governs. All steel is ASTM A992/A992M.\n\nThe accumulated gravity loads at each story (already combined dead and live values\nfor that column segment) are:\n\n- Upper segment B-C: dead load D = 41.5 kips, live load L = 125 kips.\n- Lower segment A-B: dead load D = 100 kips, live load L = 300 kips.\n\nUsing the effective length method, determine whether the W14×82 column is adequate\nfor both segments (LRFD and ASD).\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Columns: W14×82 (Ag = 24.0 in.², Ix = 881 in.⁴, rx = 6.05 in., ry = 2.48 in.,\n  rx/ry = 2.44). Story height 14 ft each segment.\n- Girders (span 35 ft, two per joint): roof W18×50 (Ix = 800 in.⁴);\n  floor W24×55 (Ix = 1,350 in.⁴).\n- Boundary conditions: base at A fixed about x-x; column continuously braced about y-y.\n- Frame: sidesway uninhibited in the plane of the frame.\n- Loads (accumulated D and L per segment): B-C: D = 41.5, L = 125 kips;\n  A-B: D = 100, L = 300 kips.\n- Code basis: AISC 360 (effective length method, Appendix 7.2; loads per ASCE/SEI 7).\n\n## Find\nThe required compressive strength of each segment, the alignment-chart effective\nlength factors K, and the available compressive strength φcPn (LRFD) and Pn/Ωc (ASD);\ndetermine whether the W14×82 is adequate.",
 "has_figure": false,
 "stem": "E_4A",
 "breadcrumb": "EXAMPLE E.4A · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §App7 §7.2 · W-Shape Column in a Moment Frame, Effective Length Method (Fixed Base)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.4A · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §App7 §7.2 · W-Shape Column in a Moment Frame, Effective Length Method (Fixed Base)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Appendix 7 §7.2 (effective length method; K from the sidesway-uninhibited alignment chart, Commentary Fig. C-A-7.2 with G per Commentary Eq. C-A-7-3; G = 1.0 at a fixed base per the App. 7 Commentary); §E2, §E3 (Eqs. E3-1, E3-2, E3-4). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strengths

- **Segment B–C (upper):** Pu = 1.2(41.5) + 1.6(125) = **250 kips**; Pa = 41.5 + 125 = **167 kips**
- **Segment A–B (lower):** Pu = 1.2(100) + 1.6(300) = **600 kips**; Pa = 100 + 300 = **400 kips**

### 2. Alignment-Chart Stiffness Ratios (Comm. Eq. C-A-7-3)

Column W14x82: Ix/L = 881/14 = 62.9 (ft-units; E cancels). Girders (two per joint, 35-ft spans): roof W18x50: Σ = 2(800)/35 = 45.7; floor W24x55: Σ = 2(1,350)/35 = 77.1.

- **Joint C (roof):** G_C = 62.9/45.7 = **1.38**
- **Joint B (floor):** G_B = (62.9 + 62.9)/77.1 = **1.63**
- **Joint A (fixed base):** G_A = **1.0** (Commentary recommendation for a fixed support)

### 3. Effective Length Factors (sidesway-uninhibited chart)

Solving the sidesway-permitted alignment-chart relation [G_AG_B(π/K)² − 36]/[6(G_A + G_B)] = (π/K)/tan(π/K):

- **Segment B–C** (G = 1.63 / 1.38): **Kx ≈ 1.48** → Lcx = 1.48(14) = 20.7 ft
- **Segment A–B** (G = 1.0 / 1.63): **Kx ≈ 1.43** → Lcx = 1.43(14) = 20.0 ft

(Out of plane the column is continuously braced; only in-plane x-x buckling applies. Elastic G-values are used — conservative; the Commentary permits τb-reduced inelastic G.)

### 4. Available Strength — §E3 (W14x82: Ag = 24.0 in.², rx = 6.05 in.; nonslender)

**Segment B–C:** Lcx/rx = 20.7(12)/6.05 = 41.1 ≤ 113 → inelastic.
Fe = π²E/(41.1)² = 169 ksi (Eq. E3-4); Fn = (0.658^(50/169))(50) = 44.2 ksi (Eq. E3-2)
Pn = 44.2(24.0) = 1,061 kips → **φcPn = 955 kips; Pn/Ωc = 635 kips**

**Segment A–B:** Lcx/rx = 20.0(12)/6.05 = 39.7 → Fe = 182 ksi; Fn = 44.6 ksi
Pn = 44.6(24.0) = 1,069 kips → **φcPn = 963 kips; Pn/Ωc = 640 kips**

### 5. Adequacy Check

| Segment | Kx | φcPn vs Pu (LRFD) | Pn/Ωc vs Pa (ASD) |
|---|---|---|---|
| B–C | 1.48 | 955 ≥ 250 ✓ (0.26) | 635 ≥ 167 ✓ (0.26) |
| A–B | 1.43 | 963 ≥ 600 ✓ (0.62) | 640 ≥ 400 ✓ (0.63) |

### 6. Conclusion

Using the effective length method of Appendix 7 §7.2 with alignment-chart K-factors (Kx = 1.48 upper / 1.43 lower, reflecting the fixed base and girder restraints), the **W14x82 is adequate for both story segments** under LRFD and ASD, with the lower segment governing at about 62% utilization. In-plane flexural buckling per §E3 controls since the weak axis is continuously braced; the lateral system's adequacy (including B2 ≤ 1.5 applicability of §7.2.1) is per the problem statement.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
