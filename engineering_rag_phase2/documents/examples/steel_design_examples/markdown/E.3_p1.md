<!-- chunk_id: E.3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.3",
 "example_family": "E.3",
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
  "E7-2"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "Built-Up I-Shaped Column with Slender Flanges",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.3 — Built-Up I-Shaped Column with Slender Flanges",
 "question": "# E.3 — Built-up I-shaped column with slender flanges  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA welded built-up I-shaped column is made from ASTM A572 Grade 50 plate with two\nflange plates each ⅜ in. thick by 10½ in. wide and a single web plate ¼ in. thick\nby 7¼ in. deep (overall depth d = 8.00 in.). The column is 15 ft long and pinned\nabout both axes. Determine whether it has adequate available compressive strength\nto carry an axial service dead load of 40 kips and an axial service live load of\n120 kips. Evaluate flange and web local slenderness and apply the slender-element\nprovisions as needed.\n\n## Given\n- Material: ASTM A572 Grade 50, Fy = 50 ksi, E = 29,000 ksi.\n- Cross section (welded built-up I): flanges PL ⅜ in. × 10½ in. (two); web PL ¼ in. × 7¼ in.;\n  d = 8.00 in.; bf = 10½ in.; tf = ⅜ in.; h = 7¼ in.; tw = ¼ in.\n- Geometry: length 15 ft; pinned–pinned both axes (Kx = Ky = 1.0).\n- Loads: axial service D = 40 kips, L = 120 kips.\n- Code basis: AISC 360 (ASCE 7 load combinations); properties computed by hand (ignoring welds).\n\n## Find\nWhether φcPn (LRFD) and Pn/Ωc (ASD) meet the required strength, accounting for the\nflange local-buckling slenderness check.",
 "has_figure": false,
 "stem": "E_3",
 "breadcrumb": "EXAMPLE E.3 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E7 §E1 §E7.1 · Built-Up I-Shaped Column with Slender Flanges",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.3 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E7 §E1 §E7.1 · Built-Up I-Shaped Column with Slender Flanges

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E3 (Eqs. E3-2, E3-4), §E7 (Eqs. E7-1, E7-2), Table B4.1a (Cases 2, 5). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided. Section properties by hand, welds ignored.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(40) + 1.6(120) = **240 kips**
- **ASD:** Pa = 40 + 120 = **160 kips**

### 2. Section Properties (hand calculation)

Flanges 2 × PL 3/8 × 10 1/2; web PL 1/4 × 7 1/4; d = 8.00 in.

Ag = 2(3.94) + 1.81 = **9.69 in.²**
Iy = 2(0.375)(10.5)³/12 + 7.25(0.25)³/12 = 72.4 in.⁴ → ry = **2.73 in.**
Ix = 2[10.5(0.375)³/12 + 3.94(3.81)²] + 0.25(7.25)³/12 = 123 in.⁴ → rx = 3.56 in.

Lc = 15 ft = 180 in. (K = 1.0) → governing Lc/ry = 180/2.73 = **65.9**.

### 3. Local Slenderness — Table B4.1a

**Web (Case 5):** h/tw = 7.25/0.25 = 29.0 ≤ λr = 1.49√(E/Fy) = 35.9 ✓ nonslender.

**Flanges (Case 2, built-up):** kc = 4/√(h/tw) = 4/√29.0 = 0.743 (0.35–0.76 ✓)
λr = 0.64√(kcE/Fy) = 0.64√(0.743 × 29,000/50) = **13.3**
b/t = (10.5/2)/0.375 = **14.0 > 13.3 → flanges classified slender**; member evaluated under §E7.

### 4. Nominal Stress — §E3

Fe = π²E/(65.9)² = **66.0 ksi** (Eq. E3-4); 65.9 ≤ 113 → inelastic, Eq. E3-2:

Fn = (0.658^(50/66.0))(50) = (0.658^0.758)(50) = **36.4 ksi**

### 5. Effective Width Check — §E7.1, Eq. E7-2

A slender element requires reduction only when λ > λr√(Fy/Fn):

λr√(Fy/Fn) = 13.3√(50/36.4) = **15.6**

λ = 14.0 ≤ 15.6 → **be = b (Eq. E7-2); the flanges are fully effective at the governing stress level.** No reduction; Ae = Ag = 9.69 in.²

### 6. Available Compressive Strength — Eq. E7-1 (= E3-1 here)

Pn = FnAe = 36.4(9.69) = **353 kips**

- **LRFD:** φcPn = 0.90(353) = **317 kips** ≥ 240 kips ✓ (utilization 0.76)
- **ASD:** Pn/Ωc = 353/1.67 = **211 kips** ≥ 160 kips ✓ (utilization 0.76)

### 7. Conclusion

Although the 3/8 × 10 1/2 in. flanges are **slender by the Table B4.1a Case 2 classification** (14.0 > 13.3), at the member's actual critical stress (Fn = 36.4 ksi < Fy) the §E7 stress-dependent check shows the full flange width is effective (14.0 ≤ 15.6, Eq. E7-2). The available strength is therefore computed on the gross area: **317 kips (LRFD) / 211 kips (ASD)** — the column is **adequate** for the 240 / 160 kip demands. This example illustrates that the AISC 360-22 effective-width method only penalizes slender elements when the applied stress is high enough to mobilize local buckling.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
