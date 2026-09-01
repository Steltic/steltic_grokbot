<!-- chunk_id: E.13_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.13",
 "example_family": "E.13",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E6",
  "E3",
  "E4",
  "E7",
  "E6.2",
  "E6.1"
 ],
 "eqs": [
  "E6-2a",
  "E6-2b",
  "E3-2",
  "E3-4",
  "E4-2",
  "E7-1",
  "E7-2",
  "E7-3",
  "E7-5"
 ],
 "tables": [
  "E7.1",
  "B4.1a"
 ],
 "title": "Double-WT Compression Member",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.13 — Double-WT Compression Member",
 "question": "# E.13 — Double-WT compression member (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA built-up compression member is formed from two ASTM A992/A992M WT9×20 tees placed\nflange-to-flange (a cruciform double-WT) with a ½-in. gap between the flange faces,\njoined by ½-in.-thick connectors welded at the ends and at equal intervals \"a\" along\na 9-ft length. The ends are pinned (K = 1.0). Using the minimum number of intermediate\nconnectors needed to make the two tees act as a single built-up member, determine the\navailable compressive strength (LRFD and ASD) per AISC 360-22 by hand calculation.\n(The WT9×20 stem is slender, so §E7 applies.)\n\n## Given\n- Material: ASTM A992/A992M, F_y = 50 ksi, E = 29,000 ksi, G = 11,200 ksi.\n- Single WT9×20: A_g = 5.88 in.², d = 8.95 in., t_w = 0.315 in., I_x = 44.8 in.⁴,\n  I_y = 9.55 in.⁴, r_x = 2.76 in., r_y = 1.27 in., ȳ = 2.29 in., J = 0.404 in.⁴,\n  C_w = 0.788 in.⁶, d/t_w = 28.4.\n- Combined double-WT (flange-to-flange, ½-in. gap): A = 11.8 in.², I_x = 165 in.⁴,\n  r_x = 3.74 in., I_y = 19.1 in.⁴, r_y = 1.27 in., J = 0.808 in.⁴, C_w ≈ 0 (cruciform).\n- Geometry: L = 9.0 ft, pinned (K = 1.0); ½-in. welded connectors at ends + interior.\n- Code basis: AISC 360-22.\n\n## Find\nMinimum number/spacing of intermediate connectors, the governing elastic buckling\nmode, F_n, the effective area A_e, and φ_cP_n and P_n/Ω_c.",
 "has_figure": false,
 "stem": "E_13",
 "breadcrumb": "EXAMPLE E.13 · AISC 360-22 Ch.E (column / axial compression) · §E6 §E3 §E4 §E7 §E6.2 §E6.1 · Double-WT Compression Member",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.13 · AISC 360-22 Ch.E (column / axial compression) · §E6 §E3 §E4 §E7 §E6.2 §E6.1 · Double-WT Compression Member

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E6 (built-up members, Eqs. E6-2a/E6-2b and General Requirements), §E3 (Eqs. E3-2, E3-4), §E4 (Eq. E4-2, torsional buckling), §E7 (Eqs. E7-1, E7-2, E7-3, E7-5; Table E7.1), Table B4.1a Case 4. φc = 0.90, Ωc = 1.67. Per the RAG extract provided.

---

### 1. Design Data

| Item | Value |
|---|---|
| Member | 2-WT9x20 (A992) flange-to-flange, 1/2-in. gap; welded 1/2-in. connectors |
| Single WT | A = 5.88 in.²; rx = 2.76 in.; ry = 1.27 in. (= min ri); d/tw = 28.4; tw = 0.315 in.; d = 8.95 in. |
| Built-up | A = 11.8 in.²; Ix = 165 in.⁴ (rx = 3.74 in.); Iy = 19.1 in.⁴ (ry = 1.27 in.); J = 0.808 in.⁴; Cw ≈ 0 |
| Geometry | L = 9.0 ft = 108 in., pinned (K = 1.0) |

### 2. Minimum Intermediate Connectors — §E6.2(a)

Requirement: a/ri ≤ (3/4) × governing built-up slenderness. Governing slenderness = Lc/ry = 108/1.27 = 85.0 → a/ri ≤ 0.75(85.0) = 63.8 → a ≤ 63.8(1.27) = 81.0 in.

- Ends only (a = 108 in.): a/ri = 85.0 > 63.8 ✗
- **One intermediate connector at midlength (a = 54 in.): a/ri = 54/1.27 = 42.5 ≤ 63.8 ✓**

**Minimum: one intermediate connector (a = 54 in.).**

### 3. Modified Slenderness — §E6.1

Buckling about the **x-axis** (deflection in the plane of the stems) produces relative slip/shear in the connectors; the **y-axis** mode does not. Connectors are welded, a/ri = 42.5 > 40 → Eq. E6-2b with Ki = 0.86 ("all other cases"):

(Lc/rx)m = √[(108/3.74)² + (0.86 × 42.5)²] = √[(28.9)² + (36.6)²] = **46.6**

y-axis (unmodified): Lc/ry = **85.0** ← governs flexure.

### 4. Elastic Buckling Stresses

- **Flexural, y-axis (Eq. E3-4):** Fe = π²(29,000)/(85.0)² = **39.6 ksi** ← **governs**
- **Flexural, x-axis (modified):** Fe = π²(29,000)/(46.6)² = 132 ksi
- **Torsional (doubly symmetric cruciform, Eq. E4-2, Cw ≈ 0):** Fe = GJ/(Ix + Iy) = 11,200(0.808)/(165 + 19.1) = **49.2 ksi**

### 5. Nominal Stress — Eq. E3-2

Fy/Fe = 50/39.6 = 1.26 ≤ 2.25 → Fn = (0.658^1.26)(50) = **29.5 ksi**

### 6. Slender Stems and Effective Area — §E7

Table B4.1a Case 4 (tee stems): λr = 0.75√(E/Fy) = 18.1; d/tw = 28.4 > 18.1 → **slender**, §E7 applies.

Check Eq. E7-2: λr√(Fy/Fn) = 18.1√(50/29.5) = 23.5 < 28.4 → reduce per Eq. E7-3, Table E7.1(c) (all other elements): c1 = 0.22, c2 = 1.49.

Fel = (c2λr/λ)²Fy = [1.49(18.1)/28.4]²(50) = (0.948)²(50) = **44.9 ksi** (Eq. E7-5)

√(Fel/Fn) = √(44.9/29.5) = 1.234

de = d[1 − c1(1.234)](1.234) = d(0.728)(1.234) = 0.899d = 0.899(8.95) = **8.05 in.**

Area reduction (two stems): 2(8.95 − 8.05)(0.315) = 0.57 in.²

Ae = 11.8 − 0.57 = **11.2 in.²**

### 7. Available Compressive Strength — Eq. E7-1

Pn = Fn Ae = 29.5(11.2) = **331 kips**

- **LRFD:** φcPn = 0.90(331) = **298 kips**
- **ASD:** Pn/Ωc = 331/1.67 = **198 kips**

### 8. Summary and Conclusion

| Item | Value | Reference |
|---|---|---|
| Connectors | 1 intermediate (a = 54 in.), welded | §E6.2(a), E6-2b |
| Governing mode | Flexural, y-axis, Lc/r = 85.0 (Fe = 39.6 ksi) | Eq. E3-4 |
| Torsional check | Fe = 49.2 ksi (not governing) | Eq. E4-2 |
| Fn; Ae | 29.5 ksi; 11.2 in.² | Eqs. E3-2, E7-3/5 |
| **φcPn / Pn,Ωc** | **298 kips / 198 kips** | Eq. E7-1 |

With one welded intermediate connector, the double-WT acts as a single built-up member; y-axis flexural buckling governs (the connector-shear-modified x-axis slenderness and the cruciform torsional mode are both higher), and the slender WT stems reduce the area about 5%. Available strength: **298 kips (LRFD) / 198 kips (ASD)**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
