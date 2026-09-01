<!-- chunk_id: E.1A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.1A",
 "example_family": "E.1",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E2",
  "E3",
  "E1",
  "E7"
 ],
 "eqs": [
  "E3-1",
  "E3-4"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "W-Shape Column Design, Pinned Ends",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.1A — W-Shape Column Design, Pinned Ends",
 "question": "# E.1A — W-shape column design, pinned ends  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA building interior column is 30 ft long and is pinned at both the top and bottom\nfor buckling about both principal axes (no intermediate bracing). It carries a\nconcentric axial service dead load of 140 kips and a concentric axial service live\nload of 420 kips. Using ASTM A992/A992M steel (Fy = 50 ksi), select the lightest\nW-shape that satisfies the AISC 360 available compressive strength, limiting the\nselection to a nominal 14 in. (W14) shape. Report both the LRFD and ASD checks.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Geometry / span: 30 ft long column; pinned top and bottom about both axes; Kx = Ky = 1.0.\n- Loads: axial service D = 140 kips, L = 420 kips (concentric).\n- Member / section: to be selected; limit to a nominal 14 in. (W14) shape.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nSelect the lightest adequate W14 shape and verify its available compressive\nstrength against the required strength, in both LRFD and ASD.",
 "has_figure": false,
 "stem": "E_1A",
 "breadcrumb": "EXAMPLE E.1A · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §E7 · W-Shape Column Design, Pinned Ends",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.1A · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §E7 · W-Shape Column Design, Pinned Ends

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E2, §E3 (Eqs. E3-1 through E3-4), Table B4.1a (Cases 1, 5). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

D = 140 kips, L = 420 kips (concentric axial):

- **LRFD:** Pu = 1.2(140) + 1.6(420) = **840 kips**
- **ASD:** Pa = 140 + 420 = **560 kips**

Geometry: L = 30 ft; pinned both ends, both axes → Kx = Ky = 1.0; Lcx = Lcy = 30.0 ft = 360 in.

### 2. Trial Section — W14x132 (A992, Fy = 50 ksi)

Ag = 38.8 in.²; rx = 6.28 in.; ry = 3.76 in.; bf/2tf = 7.15; h/tw = 17.7.

**Local slenderness (Table B4.1a):** flanges, Case 1: λr = 0.56√(E/Fy) = 13.5 > 7.15 ✓; web, Case 5: λr = 1.49√(E/Fy) = 35.9 > 17.7 ✓ → **nonslender; §E3 applies.**

### 3. Critical Stress — §E3

Governing slenderness (weak axis): Lc/ry = 360/3.76 = **95.7** (≤ 200 ✓, §E2 User Note)

Fe = π²E/(Lc/r)² = π²(29,000)/(95.7)² = **31.2 ksi** (Eq. E3-4)

4.71√(E/Fy) = 113 > 95.7 → inelastic buckling, Eq. E3-2:

Fn = (0.658^(50/31.2))(50) = (0.658^1.60)(50) = **25.6 ksi**

### 4. Available Compressive Strength — Eq. E3-1

Pn = Fn Ag = 25.6(38.8) = **993 kips**

- **LRFD:** φcPn = 0.90(993) = **893 kips** ≥ 840 kips ✓
- **ASD:** Pn/Ωc = 993/1.67 = **594 kips** ≥ 560 kips ✓

### 5. Confirmation of Lightest W14

Next lighter shape, W14x120 (Ag = 35.3 in.², ry = 3.74 in.): Lc/ry = 96.3 → Fe = 30.9 ksi → Fn = 25.4 ksi → φcPn = 0.90(25.4)(35.3) = 807 kips < 840 kips ✗ (and Pn/Ωc = 537 kips < 560 kips ✗). **W14x132 is the lightest adequate W14.**

### 6. Summary and Conclusion

| Quantity | LRFD | ASD | Reference |
|---|---|---|---|
| Required | 840 kips | 560 kips | ASCE/SEI 7 combos |
| Available (W14x132) | 893 kips | 594 kips | Eqs. E3-1/2/4 |
| Utilization | 0.94 | 0.94 | — |

**Select W14x132 (ASTM A992).** Weak-axis flexural buckling at Lc/ry = 95.7 governs; the section is nonslender so no §E7 reduction applies. The selection is verified adequate by both LRFD and ASD with ~6% margin, and the next lighter W14 fails both checks.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
