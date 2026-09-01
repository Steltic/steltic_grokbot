<!-- chunk_id: E.5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.5",
 "example_family": "E.5",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E6",
  "E6.2",
  "E3",
  "E4",
  "E1",
  "E7"
 ],
 "eqs": [
  "E6-2a",
  "E6-2b",
  "E3-1",
  "E3-2",
  "E3-4",
  "E4-3",
  "E4-6",
  "E4-7"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "Double-Angle Strut Without Slender Elements",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.5 — Double-Angle Strut Without Slender Elements",
 "question": "# E.5 — Double-angle strut without slender elements (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 2L4×3½×⅜ long-legs-back-to-back (LLBB) double-angle strut is used as an 8-ft\npin-ended compression member. The two angles are separated by a ⅜-in. gusset/filler\ngap (i.e., a ¾-in. back-to-back separation as tabulated for the equivalent r_y),\njoined by welded or pretensioned-bolted intermediate connectors. The steel is\nASTM A572/A572M Grade 50 (F_y = 50 ksi). The member carries an axial service dead\nload of 20 kips and an axial service live load of 60 kips. Determine whether the\nmember has adequate available compressive strength (LRFD and ASD), and find the\nminimum number of intermediate connectors required.\n\n## Given\n- Material: ASTM A572/A572M Grade 50, F_y = 50 ksi, E = 29,000 ksi, G = 11,200 ksi.\n- Member: 2L4×3½×⅜ LLBB, ¾-in. separation, welded/pretensioned-bolted connectors.\n- Single-angle props (L4×3½×⅜): r_z = 0.719 in., J = 0.132 in.⁴, C_w = 0.134 in.⁶.\n- Combined props (2L, ¾-in. sep): A_g = 5.36 in.², r_x = 1.25 in., r_y = 1.69 in.,\n  r̄_o = 2.33 in., H = 0.813.\n- Geometry / span: length L = 8.0 ft, pinned both ends (K = 1.0), L_cx = L_cy = 8.0 ft.\n- Loads: P_D = 20 kips, P_L = 60 kips (axial).\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe available compressive strength (φ_cP_n for LRFD, P_n/Ω_c for ASD), confirm it is\nadequate for the required strength, and determine the minimum number of intermediate\nconnectors.",
 "has_figure": false,
 "stem": "E_5",
 "breadcrumb": "EXAMPLE E.5 · AISC 360-22 Ch.E (column / axial compression) · §E6 §E6.2 §E3 §E4 §E1 §E7 · Double-Angle Strut Without Slender Elements",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.5 · AISC 360-22 Ch.E (column / axial compression) · §E6 §E6.2 §E3 §E4 §E1 §E7 · Double-Angle Strut Without Slender Elements

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E6 (Eqs. E6-2a/E6-2b, Ki = 0.50; §E6.2(a) connector spacing), §E3 (Eqs. E3-1, E3-2, E3-4), §E4 (Eq. E4-3 with E4-6, E4-7), Table B4.1a Case 3. φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(20) + 1.6(60) = **120 kips**
- **ASD:** Pa = 20 + 60 = **80 kips**

### 2. Data and Classification

2L4x3 1/2x3/8 LLBB (3/4-in. separation), A572 Gr. 50; Ag = 5.36 in.²; rx = 1.25 in.; ry = 1.69 in.; r̄o = 2.33 in.; H = 0.813; per angle: rz = 0.719 in. (= min ri), J = 0.132 in.⁴, Cw = 0.134 in.⁶. L = 8.0 ft = 96 in., K = 1.0.

Legs (Table B4.1a Case 3): b/t = 4.00/0.375 = 10.7 ≤ λr = 0.45√(E/Fy) = 10.8 → **nonslender** (no §E7 reduction).

### 3. Minimum Intermediate Connectors — §E6.2(a)

Requirement: a/ri ≤ (3/4)(governing member slenderness). Governing slenderness = Lc/rx = 96/1.25 = 76.8 → limit = 0.75(76.8) = 57.6.

- 1 connector (a = 48 in.): a/ri = 48/0.719 = 66.8 > 57.6 ✗
- **2 connectors (a = 32 in.): a/ri = 32/0.719 = 44.5 ≤ 57.6 ✓ → minimum 2 intermediate connectors**

### 4. Buckling Modes

**(a) Flexural about x (no connector shear):** Lc/rx = 76.8 → Fe = π²E/(76.8)² = **48.5 ksi** (Eq. E3-4) ← **governs**

**(b) Flexural-torsional (y-symmetry axis + torsion), with §E6 modified slenderness:**
Connectors welded/pretensioned, a/ri = 44.5 > 40 → Eq. E6-2b, Ki = 0.50 (angles back-to-back):
(Lc/ry)m = √[(96/1.69)² + (0.50 × 44.5)²] = √[(56.8)² + (22.3)²] = 61.0
Fey = π²E/(61.0)² = 76.9 ksi (Eq. E4-6)
Fez = [π²ECw/Lcz² + GJ]/(Ag r̄o²) = [π²(29,000)(0.268)/(96)² + 11,200(0.264)]/[5.36(2.33)²] = [8.3 + 2,957]/29.1 = 101.9 ksi (Eq. E4-7; Cw term negligible per User Note)
Fe = [(Fey + Fez)/(2H)][1 − √(1 − 4FeyFezH/(Fey + Fez)²)] = (110.0)(0.550) = **60.5 ksi** (Eq. E4-3)

Governing Fe = **48.5 ksi** (x-axis flexural buckling).

### 5. Strength — §E3

Fy/Fe = 50/48.5 = 1.03 ≤ 2.25 → Fn = (0.658^1.03)(50) = **32.5 ksi** (Eq. E3-2)

Pn = FnAg = 32.5(5.36) = **174 kips** (Eq. E3-1)

- **LRFD:** φcPn = 0.90(174) = **157 kips** ≥ 120 kips ✓ (utilization 0.77)
- **ASD:** Pn/Ωc = 174/1.67 = **104 kips** ≥ 80 kips ✓ (utilization 0.77)

### 6. Conclusion

With the required **minimum of two welded/pretensioned intermediate connectors** (a = 32 in., satisfying §E6.2(a)), the 2L4x3 1/2x3/8 LLBB strut is governed by x-axis flexural buckling (Fe = 48.5 ksi); the flexural-torsional mode, even with the §E6 connector-shear penalty on Fey, is well above it (60.5 ksi). The member provides **157 kips (LRFD) / 104 kips (ASD)** and is **adequate** for the 120 / 80 kip demands.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
