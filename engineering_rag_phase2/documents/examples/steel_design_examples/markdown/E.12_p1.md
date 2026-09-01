<!-- chunk_id: E.12_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.12",
 "example_family": "E.12",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E3",
  "E4",
  "E1",
  "E7"
 ],
 "eqs": [
  "E3-2",
  "E3-4",
  "E4-1",
  "E4-3",
  "E4-6",
  "E4-7",
  "E4-8",
  "E4-9"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "Built-Up I-Shaped Member with Unequal Flanges",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.12 — Built-Up I-Shaped Member with Unequal Flanges",
 "question": "# E.12 — Built-up I-shaped member with unequal flanges  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA welded built-up, singly symmetric I-shaped compression member is fabricated from\nASTM A572 Grade 50 plate. The outside flange is a ¾ in. × 5 in. plate, the inside\nflange is a ¾ in. × 8 in. plate, and the web is a ⅜ in. × 10½ in. plate (overall\ndepth d = 12.0 in.). The member is 14 ft long with pinned ends. Because the two\nflanges differ in width, the shape is symmetric only about its y-y (web) axis, so\nflexural-torsional buckling must be evaluated. Compute the available compressive\nstrength of the member (LRFD φcPn and ASD Pn/Ωc).\n\n## Given\n- Material: ASTM A572 Grade 50, Fy = 50 ksi, E = 29,000 ksi, G = 11,200 ksi.\n- Cross section (welded, singly symmetric about y-y): outside flange PL ¾ in. × 5 in.;\n  inside flange PL ¾ in. × 8 in.; web PL ⅜ in. × 10½ in.; overall depth d = 12.0 in.\n- Geometry: length 14 ft; pinned ends, K = 1.0, so Lcx = Lcy = Lcz = 14.0 ft.\n- Loads: not specified; determine the available compressive strength (capacity).\n- Code basis: AISC 360; section properties (Ag, centroid, Ix, Iy, J, Cw, shear-center\n  location, polar radius of gyration) computed by hand, ignoring welds.\n\n## Find\nThe available compressive strength, governed by the lowest of flexural buckling (x-x)\nand flexural-torsional buckling, with the local-slenderness check of both flanges and web.",
 "has_figure": false,
 "stem": "E_12",
 "breadcrumb": "EXAMPLE E.12 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E4 §E1 §E7 · Built-Up I-Shaped Member with Unequal Flanges",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.12 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E4 §E1 §E7 · Built-Up I-Shaped Member with Unequal Flanges

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E3 (Eqs. E3-2, E3-4), §E4 (Eqs. E4-1, E4-3, E4-6, E4-7, E4-8, E4-9), Table B4.1a Cases 2 and 5. φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided. Section properties computed by hand, welds ignored.

---

### 1. Section Properties (hand calculation)

Plates (A572 Gr. 50, Fy = 50 ksi): outside flange PL 3/4 × 5; inside flange PL 3/4 × 8; web PL 3/8 × 10 1/2; d = 12.0 in. Lcx = Lcy = Lcz = 14.0 ft = 168 in. (pinned ends).

| Property | Value |
|---|---|
| Ag = 3.75 + 6.00 + 3.94 | **13.7 in.²** |
| Centroid (from outer face of 8-in. flange) | ȳ = 5.08 in. |
| Ix | 333 in.⁴ → rx = 4.94 in. |
| Iy = 32.0 + 7.81 + 0.05 | 39.9 in.⁴ → ry = 1.71 in. |
| J = Σbt³/3 | 2.01 in.⁴ |
| Cw = (tf h²/12)[b1³b2³/(b1³ + b2³)], h = 11.25 in. | 795 in.⁶ |
| Shear center (from inside-flange centroid, toward small flange) = h·Iy,out/(Iy,in + Iy,out) = 11.25(7.81)/39.8 | 2.21 in. → y0 = 5.08 − 0.375 − 2.21 = **2.49 in.**; x0 = 0 |
| r̄o² = x0² + y0² + (Ix + Iy)/Ag = 6.21 + 27.3 | **33.5 in.²** (Eq. E4-9) |
| H = 1 − y0²/r̄o² = 1 − 6.21/33.5 | **0.814** (Eq. E4-8) |

### 2. Local Slenderness — Table B4.1a

**Flanges (Case 2, built-up):** kc = 4/√(h/tw) = 4/√(10.5/0.375) = 4/√28.0 = 0.756 (0.35 ≤ kc ≤ 0.76 ✓)
λr = 0.64√(kcE/Fy) = 0.64√(0.756 × 29,000/50) = 13.4
b/t: outside = 2.50/0.75 = 3.33; inside = 4.00/0.75 = 5.33 — both ≤ 13.4 ✓ **nonslender**

**Web (Case 5):** λr = 1.49√(E/Fy) = 35.9; h/tw = 28.0 ≤ 35.9 ✓ **nonslender**

No §E7 reduction; §E3/§E4 apply with Ag.

### 3. Elastic Buckling Stresses

**Flexural buckling about x (non-symmetry axis), §E3:** Lcx/rx = 168/4.94 = 34.0 → Fe = π²(29,000)/(34.0)² = 247 ksi — not critical.

**Flexural-torsional buckling (§E4, singly symmetric, y = axis of symmetry):**

Fey = π²E/(Lcy/ry)² = π²(29,000)/(168/1.71)² = π²(29,000)/(98.5)² = **29.5 ksi** (Eq. E4-6)

Fez = [π²ECw/Lcz² + GJ]/(Ag r̄o²) = [π²(29,000)(795)/(168)² + 11,200(2.01)]/[13.7(33.5)]
Fez = [8,060 + 22,500]/458 = **66.8 ksi** (Eq. E4-7)

Fe = [(Fey + Fez)/(2H)]·[1 − √(1 − 4FeyFezH/(Fey + Fez)²)] (Eq. E4-3)
= [(29.5 + 66.8)/1.629]·[1 − √(1 − 4(29.5)(66.8)(0.814)/(96.3)²)]
= (59.1)(1 − √(1 − 0.693)) = (59.1)(1 − 0.554) = **26.3 ksi** ← governs

### 4. Nominal Stress and Strength — Eqs. E3-2, E4-1

Fy/Fe = 50/26.3 = 1.90 ≤ 2.25 → inelastic, Eq. E3-2:

Fn = (0.658^1.90)(50) = **22.6 ksi**

Pn = Fn Ag = 22.6(13.7) = **309 kips** (Eq. E4-1)

### 5. Available Compressive Strength

- **LRFD:** φcPn = 0.90(309) = **278 kips**
- **ASD:** Pn/Ωc = 309/1.67 = **185 kips**

### 6. Summary and Conclusion

| Mode | Fe | Reference |
|---|---|---|
| Flexural buckling, x-axis | 247 ksi | Eq. E3-4 |
| Flexural-torsional (y-flexure + torsion) | **26.3 ksi (governs)** | Eqs. E4-3/6/7/8/9 |

The built-up unequal-flange I-section is nonslender locally (Table B4.1a Cases 2, 5) and is governed by **flexural-torsional buckling** about its axis of symmetry, as required for singly symmetric members under §E4. The available compressive strength is **φcPn = 278 kips (LRFD)** and **Pn/Ωc = 185 kips (ASD)**. Note the FTB mode reduces Fe about 11% below the pure weak-axis flexural value (26.3 vs. 29.5 ksi) — ignoring §E4 would be unconservative for this shape.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
