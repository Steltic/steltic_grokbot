<!-- chunk_id: E.1D_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.1D",
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
 "title": "W14x90 Available Compressive Strength (Unequal Unbraced Lengths)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.1D — W14x90 Available Compressive Strength (Unequal Unbraced Lengths)",
 "question": "# E.1D — W14x90 available compressive strength (unequal unbraced lengths)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nCalculate the available axial compressive strength (LRFD design strength and ASD\nallowable strength) of an ASTM A992/A992M W14x90 compression member that has an\nx-x (strong) axis unbraced length of 30 ft and y-y (weak) axis and torsional\nunbraced lengths of 15 ft, with K = 1.0 for all. Confirm adequacy for a concentric\naxial service dead load of 140 kips plus live load of 420 kips.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Member: W14x90; Ag = 26.5 in.^2, rx = 6.14 in., ry = 3.70 in., bf/2tf = 10.2, h/tw = 25.9.\n- Geometry: Lx = 30 ft; Ly = Lz = 15 ft; K = 1.0 all axes.\n- Loads: axial service D = 140 kips, L = 420 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe available compressive strength (phi_c*Pn and Pn/Omega_c) computed directly from\nthe AISC 360 equations, and the adequacy check.",
 "has_figure": false,
 "stem": "E_1D",
 "breadcrumb": "EXAMPLE E.1D · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 · W14x90 Available Compressive Strength (Unequal Unbraced Lengths)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.1D · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 · W14x90 Available Compressive Strength (Unequal Unbraced Lengths)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E2, §E3 (Eqs. E3-1, E3-2, E3-4), Table B4.1a (Cases 1, 5). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(140) + 1.6(420) = **840 kips**
- **ASD:** Pa = 140 + 420 = **560 kips**

### 2. Member Data and Classification

W14x90 (A992): Ag = 26.5 in.²; rx = 6.14 in.; ry = 3.70 in.; bf/2tf = 10.2; h/tw = 25.9.
Lcx = 30.0 ft = 360 in.; Lcy = Lcz = 15.0 ft = 180 in. (K = 1.0 all axes).

Table B4.1a: flange (Case 1) λr = 13.5 > 10.2 ✓; web (Case 5) λr = 35.9 > 25.9 ✓ → **nonslender**, §E3 applies. With Lcz = Lcy ≤ Lcx, torsional buckling does not govern this doubly symmetric shape (§E3 User Note).

### 3. Governing Slenderness and Critical Stress — §E3

- Lcx/rx = 360/6.14 = **58.6** ← governs
- Lcy/ry = 180/3.70 = 48.6

Fe = π²E/(58.6)² = **83.3 ksi** (Eq. E3-4); 58.6 ≤ 113 → inelastic, Eq. E3-2:

Fn = (0.658^(50/83.3))(50) = (0.658^0.600)(50) = **38.9 ksi**

### 4. Available Strength — Eq. E3-1

Pn = 38.9(26.5) = **1,030 kips**

- **LRFD:** φcPn = 0.90(1,030) = **928 kips** ≥ 840 kips ✓ (utilization 0.91)
- **ASD:** Pn/Ωc = 1,030/1.67 = **617 kips** ≥ 560 kips ✓ (utilization 0.91)

### 5. Conclusion

Computed directly from Eqs. E3-1, E3-2, and E3-4, the W14x90 with Lx = 30 ft and Ly = Lz = 15 ft provides **φcPn = 928 kips (LRFD)** and **Pn/Ωc = 617 kips (ASD)**, governed by strong-axis flexural buckling (Lc/rx = 58.6). The member is **adequate** for the 840-kip (LRFD) / 560-kip (ASD) demands, confirming Example E.1B by direct calculation.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
