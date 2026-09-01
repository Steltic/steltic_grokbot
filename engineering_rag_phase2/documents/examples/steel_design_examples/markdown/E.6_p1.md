<!-- chunk_id: E.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.6",
 "example_family": "E.6",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E6",
  "E6.2",
  "E3",
  "E4",
  "E7",
  "E1"
 ],
 "eqs": [
  "E6-2a",
  "E6-2b",
  "E3-2",
  "E3-4",
  "E4-3",
  "E4-6",
  "E4-7",
  "E7-1",
  "E7-2",
  "E7-3",
  "E7-5"
 ],
 "tables": [
  "E7.1",
  "B4.1a"
 ],
 "title": "Double-Angle Strut with Slender Elements",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.6 — Double-Angle Strut with Slender Elements",
 "question": "# E.6 — Double-angle strut with slender elements (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 2L5×3×¼ long-legs-back-to-back (LLBB) double-angle strut spans 8 ft with pinned\nends and is built up from two angles separated by ¾ in., connected with welded or\npretensioned-bolted intermediate connectors. The steel is ASTM A572/A572M Grade 50\n(F_y = 50 ksi). The strut must carry an axial service dead load of 10 kips and an\naxial service live load of 30 kips. Determine whether the available compressive\nstrength is adequate (LRFD and ASD) and the minimum number of intermediate\nconnectors required. (The ¼-in.-thick angle legs are slender in compression, so the\neffective-area provisions of §E7 apply.)\n\n## Given\n- Material: ASTM A572/A572M Grade 50, F_y = 50 ksi, E = 29,000 ksi, G = 11,200 ksi.\n- Member: 2L5×3×¼ LLBB, ¾-in. separation, welded/pretensioned-bolted connectors.\n- Single-angle props (L5×3×¼): r_z = 0.652 in., J = 0.0438 in.⁴, C_w = 0.0606 in.⁶.\n- Combined props (2L, ¾-in. sep): A_g = 3.88 in.², r_x = 1.62 in., r_y = 1.33 in.,\n  r̄_o = 2.59 in., H = 0.657.\n- Geometry / span: L = 8.0 ft, pinned both ends (K = 1.0), L_cx = L_cy = 8.0 ft.\n- Loads: P_D = 10 kips, P_L = 30 kips (axial).\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe available compressive strength (φ_cP_n, P_n/Ω_c), whether it is adequate, and the\nminimum number of intermediate connectors.",
 "has_figure": false,
 "stem": "E_6",
 "breadcrumb": "EXAMPLE E.6 · AISC 360-22 Ch.E (column / axial compression) · §E6 §E6.2 §E3 §E4 §E7 §E1 · Double-Angle Strut with Slender Elements",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.6 · AISC 360-22 Ch.E (column / axial compression) · §E6 §E6.2 §E3 §E4 §E7 §E1 · Double-Angle Strut with Slender Elements

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E6 (Eqs. E6-2a/E6-2b, Ki = 0.50; §E6.2(a)), §E3 (Eqs. E3-2, E3-4), §E4 (Eq. E4-3 with E4-6/E4-7), §E7 (Eqs. E7-1, E7-2, E7-3, E7-5; Table E7.1(c)), Table B4.1a Case 3. φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(10) + 1.6(30) = **60 kips**
- **ASD:** Pa = 10 + 30 = **40 kips**

### 2. Data and Classification

2L5x3x1/4 LLBB (3/4-in. sep.), A572 Gr. 50; Ag = 3.88 in.²; rx = 1.62 in.; ry = 1.33 in.; r̄o = 2.59 in.; H = 0.657; per angle: rz = 0.652 in., J = 0.0438 in.⁴, Cw = 0.0606 in.⁶. L = 96 in., K = 1.0.

Table B4.1a Case 3: λr = 0.45√(E/Fy) = 10.8. Long leg b/t = 5.0/0.25 = 20.0 > 10.8; short leg = 12.0 > 10.8 → **slender elements; §E7 applies.**

### 3. Minimum Intermediate Connectors — §E6.2(a)

With 2 intermediate connectors (a = 32 in.): a/ri = 32/0.652 = 49.1 > 40 → modified slenderness (Eq. E6-2b, Ki = 0.50):
(Lc/ry)m = √[(96/1.33)² + (0.50 × 49.1)²] = √[(72.2)² + (24.5)²] = **76.2**

Governing member slenderness = 76.2 → limit a/ri ≤ 0.75(76.2) = 57.2 ≥ 49.1 ✓.
(One connector, a = 48 in.: a/ri = 73.6 > 0.75 × 81.0 = 60.8 ✗.) → **Minimum 2 intermediate connectors.**

### 4. Buckling Modes

- **Flexural, x-axis:** Lc/rx = 96/1.62 = 59.3 → Fe = π²E/(59.3)² = 81.5 ksi (Eq. E3-4)
- **Flexural-torsional (Eq. E4-3):**
  Fey = π²E/(76.2)² = 49.2 ksi (Eq. E4-6, modified slenderness)
  Fez = [π²E(0.121)/(96)² + 11,200(0.0876)]/[3.88(2.59)²] = [3.8 + 981]/26.0 = 37.8 ksi (Eq. E4-7)
  Fe = [(49.2 + 37.8)/(2 × 0.657)][1 − √(1 − 4(49.2)(37.8)(0.657)/(87.1)²)] = (66.3)(0.405) = **26.8 ksi** ← **governs**

### 5. Nominal Stress and Effective Area

Fy/Fe = 50/26.8 = 1.86 ≤ 2.25 → Fn = (0.658^1.86)(50) = **22.9 ksi** (Eq. E3-2)

§E7 check: λr√(Fy/Fn) = 10.8√(50/22.9) = **16.0**
- Short legs: λ = 12.0 ≤ 16.0 → fully effective (Eq. E7-2)
- Long legs: λ = 20.0 > 16.0 → reduce (Eq. E7-3, Table E7.1(c): c1 = 0.22, c2 = 1.49):
  Fel = [1.49(10.8)/20.0]²(50) = **32.6 ksi** (Eq. E7-5); √(Fel/Fn) = 1.193
  be = 5.00[1 − 0.22(1.193)](1.193) = **4.40 in.**

Ae = 3.88 − 2(5.00 − 4.40)(0.25) = 3.88 − 0.30 = **3.58 in.²**

### 6. Available Compressive Strength — Eq. E7-1

Pn = FnAe = 22.9(3.58) = **82.0 kips**

- **LRFD:** φcPn = 0.90(82.0) = **73.8 kips** ≥ 60 kips ✓ (utilization 0.81)
- **ASD:** Pn/Ωc = 82.0/1.67 = **49.1 kips** ≥ 40 kips ✓ (utilization 0.81)

### 7. Conclusion

With the required **minimum of two intermediate connectors**, the 2L5x3x1/4 LLBB strut is governed by flexural-torsional buckling (Fe = 26.8 ksi, Eq. E4-3) including the §E6 connector-shear modification, with a §E7 effective-width reduction of the slender 5-in. legs (~8% of area). Available strength **73.8 kips (LRFD) / 49.1 kips (ASD)** exceeds the required 60 / 40 kips — **the member is adequate**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
