<!-- chunk_id: E.1C_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.1C",
 "example_family": "E.1",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E2",
  "E3",
  "E1"
 ],
 "eqs": [
  "E3-1",
  "E3-2",
  "E3-4"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "W14x132 Available Compressive Strength",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.1C — W14x132 Available Compressive Strength",
 "question": "# E.1C — W14x132 available compressive strength  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nDetermine the available axial compressive strength (LRFD design strength and ASD\nallowable strength) of an ASTM A992/A992M W14x132 column whose unbraced length is\n30 ft for buckling about BOTH principal axes, with pinned ends (Kx = Ky = 1.0).\nConfirm whether the column is adequate for a concentric axial service dead load of\n140 kips plus service live load of 420 kips.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Member: W14x132; Ag = 38.8 in.^2, rx = 6.28 in., ry = 3.76 in., bf/2tf = 7.15, h/tw = 17.7.\n- Geometry: Lx = Ly = 30 ft; pinned ends, Kx = Ky = 1.0.\n- Loads: axial service D = 140 kips, L = 420 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe available compressive strength (phi_c*Pn and Pn/Omega_c) and the adequacy check.",
 "has_figure": false,
 "stem": "E_1C",
 "breadcrumb": "EXAMPLE E.1C · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 · W14x132 Available Compressive Strength",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.1C · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 · W14x132 Available Compressive Strength

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E2, §E3 (Eqs. E3-1, E3-2, E3-4), Table B4.1a (Cases 1, 5). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(140) + 1.6(420) = **840 kips**
- **ASD:** Pa = 140 + 420 = **560 kips**

### 2. Member Data and Classification

W14x132 (A992): Ag = 38.8 in.²; rx = 6.28 in.; ry = 3.76 in.; bf/2tf = 7.15; h/tw = 17.7. Lcx = Lcy = 30.0 ft = 360 in. (K = 1.0).

Table B4.1a: flange (Case 1) λr = 0.56√(E/Fy) = 13.5 > 7.15 ✓; web (Case 5) λr = 1.49√(E/Fy) = 35.9 > 17.7 ✓ → **nonslender**; §E3 governs with Ag.

### 3. Critical Stress — §E3

Governing slenderness (weak axis): Lc/ry = 360/3.76 = **95.7** ≤ 200 ✓

Fe = π²E/(95.7)² = **31.2 ksi** (Eq. E3-4)

95.7 ≤ 4.71√(E/Fy) = 113 → inelastic, Eq. E3-2:

Fn = (0.658^(50/31.2))(50) = **25.6 ksi**

### 4. Available Strength — Eq. E3-1

Pn = 25.6(38.8) = **993 kips**

- **LRFD:** φcPn = 0.90(993) = **893 kips** ≥ 840 kips ✓ (utilization 0.94)
- **ASD:** Pn/Ωc = 993/1.67 = **594 kips** ≥ 560 kips ✓ (utilization 0.94)

### 5. Conclusion

The W14x132 at Lc = 30 ft about both axes provides **φcPn = 893 kips (LRFD)** and **Pn/Ωc = 594 kips (ASD)**, governed by weak-axis inelastic flexural buckling (Eq. E3-2). The column is **adequate** for D = 140 kips and L = 420 kips by both methods, confirming the selection of Example E.1A by direct calculation.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
