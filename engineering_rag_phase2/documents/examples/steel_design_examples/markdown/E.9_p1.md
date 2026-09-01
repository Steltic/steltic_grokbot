<!-- chunk_id: E.9_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.9",
 "example_family": "E.9",
 "chapter": "E",
 "topic": "HSS / rectangular-pipe compression",
 "clauses": [
  "E2",
  "E3",
  "E1",
  "E7"
 ],
 "eqs": [
  "E3-1",
  "E3-2",
  "E3-4"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "Rectangular HSS Compression Member Without Slender Elements",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.9 — Rectangular HSS Compression Member Without Slender Elements",
 "question": "# E.9 — Rectangular HSS compression member without slender elements  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 20-ft-long rectangular HSS column has a fixed base and a pinned top (so the\neffective length factor may be taken as K = 0.80 about both axes). It must carry an\naxial service dead load of 85 kips and an axial service live load of 255 kips. Using\nASTM A500 Grade C steel (Fy = 50 ksi), select an economical rectangular HSS that has\nadequate available compressive strength, confirm that its walls are nonslender, and\nverify the selection by direct calculation of the AISC 360 provisions. Report the\nLRFD and ASD checks.\n\n## Given\n- Material: ASTM A500 Grade C rectangular HSS, Fy = 50 ksi, E = 29,000 ksi.\n- Geometry: length 20 ft; fixed base, pinned top, so Kx = Ky = 0.80; Lc = 0.80(20) = 16.0 ft.\n- Loads: axial service D = 85 kips, L = 255 kips.\n- Member / section: select a rectangular HSS (this solution verifies an HSS12×10×⅜:\n  Ag = 14.6 in.², rx = 4.61 in., ry = 4.01 in., b/t = 25.7, h/t = 31.4).\n- Code basis: AISC 360 (ASCE 7 load combinations).\n\n## Find\nThe selected rectangular HSS and its available compressive strength (φcPn for LRFD,\nPn/Ωc for ASD), with the wall-slenderness check.",
 "has_figure": false,
 "stem": "E_9",
 "breadcrumb": "EXAMPLE E.9 · AISC 360-22 Ch.E (HSS / rectangular-pipe compression) · §E2 §E3 §E1 §E7 · Rectangular HSS Compression Member Without Slender Elements",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.9 · AISC 360-22 Ch.E (HSS / rectangular-pipe compression) · §E2 §E3 §E1 §E7 · Rectangular HSS Compression Member Without Slender Elements

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E2, §E3 (Eqs. E3-1, E3-2, E3-4), Table B4.1a Case 6. φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(85) + 1.6(255) = **510 kips**
- **ASD:** Pa = 85 + 255 = **340 kips**

### 2. Trial Member and Effective Length

**HSS12x10x3/8** (A500 Gr. C, Fy = 50 ksi): Ag = 14.6 in.²; rx = 4.61 in.; ry = 4.01 in.; b/t = 25.7; h/t = 31.4.

Fixed base / pinned top → K = 0.80 both axes: Lc = 0.80(20) = 16.0 ft = 192 in. (§E2).

### 3. Wall Slenderness — Table B4.1a, Case 6

λr = 1.40√(E/Fy) = 1.40√(29,000/50) = **33.7**

b/t = 25.7 ≤ 33.7 ✓ and h/t = 31.4 ≤ 33.7 ✓ → **all walls nonslender**; §E3 applies with Ag (no §E7 reduction).

### 4. Critical Stress — §E3

Governing slenderness: Lc/ry = 192/4.01 = **47.9** (≤ 200 ✓)

Fe = π²E/(47.9)² = **125 ksi** (Eq. E3-4); 47.9 ≤ 4.71√(E/Fy) = 113 → inelastic, Eq. E3-2:

Fn = (0.658^(50/125))(50) = (0.658^0.400)(50) = **42.3 ksi**

### 5. Available Compressive Strength — Eq. E3-1

Pn = FnAg = 42.3(14.6) = **617 kips**

- **LRFD:** φcPn = 0.90(617) = **556 kips** ≥ 510 kips ✓ (utilization 0.92)
- **ASD:** Pn/Ωc = 617/1.67 = **370 kips** ≥ 340 kips ✓ (utilization 0.92)

### 6. Conclusion

**Select HSS12x10x3/8 (A500 Gr. C).** With Lc = 16.0 ft (K = 0.80 for the fixed-pinned condition), weak-axis flexural buckling at Lc/ry = 47.9 governs; all walls are nonslender (25.7, 31.4 ≤ 33.7), so the full gross area is effective. The available strength of **556 kips (LRFD) / 370 kips (ASD)** exceeds the required 510 / 340 kips with ~8% margin, verifying the selection by direct §E3 calculation.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
