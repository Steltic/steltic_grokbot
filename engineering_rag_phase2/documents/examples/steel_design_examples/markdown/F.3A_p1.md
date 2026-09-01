<!-- chunk_id: F.3A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.3A",
 "example_family": "F.3",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F3",
  "F3.2"
 ],
 "eqs": [
  "F3-1"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "W-Shape with Noncompact Flange, Continuously Braced (Selection)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.3A — W-Shape with Noncompact Flange, Continuously Braced (Selection)",
 "question": "# F.3A — W-shape flexural member with noncompact flanges, major-axis (design)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported beam spans 40 ft and carries a uniform service dead load of 0.05 kip/ft\nplus two equal concentrated service live loads of 18 kips each, applied at the third points\nof the span (i.e., at 13.33 ft and 26.67 ft from one support). The beam is continuously\nbraced against lateral-torsional buckling along its full length, and is ASTM A992/A992M steel\n(Fy = 50 ksi).\n\nSelect the lightest W-shape that provides adequate available flexural strength in both LRFD\nand ASD, and compute the maximum deflection. (A shape with a noncompact compression flange\nwill be selected, to demonstrate that the AISC Manual's tabulated flexural strengths already\ninclude the flange local-buckling reduction.)\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Geometry / span: simply supported, L = 40 ft; continuously braced (Lb = 0).\n- Loads (service): uniform dead wD = 0.05 kip/ft; two concentrated live loads P = 18 kips\n  each at the third points (a = L/3 = 13.33 ft).\n- Member / section: to be selected (a W-shape).\n- Code basis: AISC 360-22 (Chapter F); ASCE/SEI 7 load combinations.\n\n## Find\nSelect a W-shape with adequate available flexural strength (LRFD and ASD), confirming that\nthe tabulated strength accounts for a noncompact flange, and compute the maximum deflection.",
 "has_figure": false,
 "stem": "F_3A",
 "breadcrumb": "EXAMPLE F.3A · AISC 360-22 Ch.F (beam flexure) · §F3 §F3.2 · W-Shape with Noncompact Flange, Continuously Braced (Selection)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.3A · AISC 360-22 Ch.F (beam flexure) · §F3 §F3.2 · W-Shape with Noncompact Flange, Continuously Braced (Selection)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F3 (compression flange local buckling, Eq. F3-1), Table B4.1b Case 11. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

L = 40 ft; wD = 0.05 kip/ft; two concentrated live loads P = 18 kips at the third points (a = 13.33 ft):

- **LRFD:** Mu = 1.6(18)(13.33) + 1.2(0.05)(40)²/8 = 384 + 12 = **396 kip-ft**
- **ASD:** Ma = 18(13.33) + 0.05(40)²/8 = 240 + 10 = **250 kip-ft**

### 2. Selection — W21x48 (A992)

Sx = 93.0 in.³; Zx = 107 in.³; Ix = 959 in.⁴; bf/2tf = 9.47.

**Flange classification (Table B4.1b Case 11):** λpf = 0.38√(E/Fy) = 9.15; λrf = 1.0√(E/Fy) = 24.1 → 9.15 < 9.47 < 24.1 → **noncompact flange** → §F3 applies (LTB excluded by continuous bracing).

### 3. Flange Local Buckling — §F3.2, Eq. F3-1

Mn = Mp − (Mp − 0.7FySx)[(λ − λpf)/(λrf − λpf)]
Mp = FyZx = 5,350 kip-in.; 0.7FySx = 3,260 kip-in.
Mn = 5,350 − (2,090)[(9.47 − 9.15)/(24.1 − 9.15)] = 5,350 − 44.9 = **5,310 kip-in. = 442 kip-ft**

(The ~1% reduction below Mp is exactly the adjustment built into the AISC Manual's tabulated strengths for this shape.)

### 4. Available Flexural Strength

- **LRFD:** φbMn = 0.90(442) = **398 kip-ft** ≥ 396 kip-ft ✓ (utilization 0.99)
- **ASD:** Mn/Ωb = 442/1.67 = **265 kip-ft** ≥ 250 kip-ft ✓ (utilization 0.94)

### 5. Maximum Deflection (service)

Two third-point live loads: Δ = 23PL³/(648EIx) = 23(18)(480)³/[648(29,000)(959)] = **2.54 in.**
Uniform dead load adds 5wL⁴/(384EIx) = 0.10 in. → total ≈ **2.64 in. (≈ L/182)**. No deflection limit was specified; this value is reported for the record and should be reviewed against project serviceability criteria.

### 6. Conclusion

**Select W21x48 (ASTM A992).** With continuous bracing, the governing limit state is **compression flange local buckling (noncompact flange, Eq. F3-1)**, giving φbMn = 398 kip-ft and Mn/Ωb = 265 kip-ft against demands of 396 / 250 kip-ft. The LRFD margin is under 1%, so the noncompact-flange reduction is essential to the check — confirming that tabulated Manual strengths already embed it.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
