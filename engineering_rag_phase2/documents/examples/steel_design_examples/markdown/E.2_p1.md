<!-- chunk_id: E.2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.2",
 "example_family": "E.2",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E3",
  "E7",
  "E1",
  "E7.1"
 ],
 "eqs": [
  "E3-2",
  "E3-4",
  "E7-1",
  "E7-2",
  "E7-3",
  "E7-5"
 ],
 "tables": [
  "E7.1",
  "B4.1a"
 ],
 "title": "Built-Up I-Shaped Column with a Slender Web",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.2 — Built-Up I-Shaped Column with a Slender Web",
 "question": "# E.2 — Built-up I-shaped column with a slender web  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA welded built-up I-shaped column is fabricated from ASTM A572 Grade 50 plate:\ntwo flange plates each 1 in. thick by 8 in. wide, and a single web plate ¼ in.\nthick by 15 in. deep (overall depth d = 17.0 in.). The column is 15 ft long and\npinned about both axes. Verify that the member has adequate available compressive\nstrength to carry an axial service dead load of 70 kips and an axial service live\nload of 210 kips. Check local slenderness of the flanges and web, and include the\nslender-web effective-area reduction if required.\n\n## Given\n- Material: ASTM A572 Grade 50, Fy = 50 ksi, E = 29,000 ksi.\n- Cross section (welded built-up I): flanges PL 1 in. × 8 in. (two); web PL ¼ in. × 15 in.;\n  d = 17.0 in.; h = 15.0 in.; tw = ¼ in.; bf = 8.00 in.; tf = 1.00 in.\n- Geometry: length 15 ft; pinned–pinned both axes (Kx = Ky = 1.0).\n- Loads: axial service D = 70 kips, L = 210 kips.\n- Code basis: AISC 360 (ASCE 7 load combinations); section properties computed by hand\n  (ignoring fillet welds).\n\n## Find\nWhether φcPn (LRFD) and Pn/Ωc (ASD) equal or exceed the required strength, treating the\nslender web per the slender-element provisions.",
 "has_figure": false,
 "stem": "E_2",
 "breadcrumb": "EXAMPLE E.2 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E7 §E1 §E7.1 · Built-Up I-Shaped Column with a Slender Web",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.2 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E7 §E1 §E7.1 · Built-Up I-Shaped Column with a Slender Web

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E3 (Eqs. E3-2, E3-4), §E7 (Eqs. E7-1, E7-2, E7-3, E7-5; Table E7.1(a)), Table B4.1a (Cases 2, 5). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided. Section properties by hand, welds ignored.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(70) + 1.6(210) = **420 kips**
- **ASD:** Pa = 70 + 210 = **280 kips**

### 2. Section Properties (hand calculation)

Flanges 2 × PL 1 × 8; web PL 1/4 × 15; d = 17.0 in.

Ag = 2(8.00) + 3.75 = **19.8 in.²**
Iy = 2(1)(8)³/12 + 15(0.25)³/12 = 85.4 in.⁴ → ry = √(85.4/19.8) = **2.08 in.**
Ix = 2[8(1)³/12 + 8(8.0)²] + 0.25(15)³/12 = 1,096 in.⁴ → rx = 7.45 in.

Lc = 15 ft = 180 in. both axes (K = 1.0) → governing Lc/ry = 180/2.08 = **86.6**.

### 3. Local Slenderness — Table B4.1a

**Flanges (Case 2, built-up):** kc = 4/√(h/tw) = 4/√60 = 0.516 (0.35–0.76 ✓)
λr = 0.64√(kcE/Fy) = 0.64√(0.516 × 29,000/50) = 11.1 > b/t = 4.00/1.00 = 4.0 ✓ **nonslender**

**Web (Case 5):** λr = 1.49√(E/Fy) = 35.9 < h/tw = 60.0 → **slender** → §E7

### 4. Nominal Stress — §E3

Fe = π²E/(86.6)² = **38.2 ksi** (Eq. E3-4); 86.6 ≤ 113 → inelastic (Eq. E3-2):

Fn = (0.658^(50/38.2))(50) = (0.658^1.31)(50) = **28.9 ksi**

### 5. Effective Area — §E7.1

Web check: λr√(Fy/Fn) = 35.9√(50/28.9) = 47.2 < 60 → reduce (Eq. E7-3) with Table E7.1(a) (stiffened elements other than HSS walls): c1 = 0.18, c2 = 1.31.

Fel = (c2λr/λ)²Fy = [1.31(35.9)/60.0]²(50) = (0.783)²(50) = **30.7 ksi** (Eq. E7-5)

√(Fel/Fn) = √(30.7/28.9) = 1.030

he = h[1 − 0.18(1.030)](1.030) = 15.0(0.815)(1.030) = **12.6 in.**

Ae = 19.8 − (15.0 − 12.6)(0.25) = 19.8 − 0.60 = **19.1 in.²**

### 6. Available Compressive Strength — Eq. E7-1

Pn = FnAe = 28.9(19.1) = **553 kips**

- **LRFD:** φcPn = 0.90(553) = **498 kips** ≥ 420 kips ✓ (utilization 0.84)
- **ASD:** Pn/Ωc = 553/1.67 = **331 kips** ≥ 280 kips ✓ (utilization 0.85)

### 7. Conclusion

The welded built-up I-section (PL 1×8 flanges, PL 1/4×15 web) at Lc = 15 ft is governed by weak-axis inelastic flexural buckling with a slender-web effective-area reduction of about 3%. Available strength: **498 kips (LRFD) / 331 kips (ASD)** versus required 420 / 280 kips — **the member is adequate** with comfortable margin. Flanges are nonslender by the built-up-element limit (Case 2 with kc = 0.516).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
