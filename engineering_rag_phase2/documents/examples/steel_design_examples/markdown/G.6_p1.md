<!-- chunk_id: G.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.6",
 "example_family": "G.6",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G6",
  "G2.2",
  "G1"
 ],
 "eqs": [
  "G6-1",
  "G2-9"
 ],
 "tables": [],
 "title": "W21x48 Minor-Axis Shear Strength",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.6 — W21x48 Minor-Axis Shear Strength",
 "question": "# G.6 -- Doubly Symmetric Shape in Minor-Axis Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W21x48 beam resists end shears of 20.0 kips from service dead load\nand 60.0 kips from service live load applied in the WEAK (minor-axis) direction.\nThere are no AISC *Manual* tables for minor-axis shear of W-shapes, so determine the\navailable minor-axis shear strength directly from AISC 360 Section G6 and verify\nadequacy for LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: W21x48; bf = 8.14 in., tf = 0.430 in.; loaded in minor-axis shear.\n- Loads (service end shear): D = 20.0 kips, L = 60.0 kips.\n- Code basis: AISC 360-22 Sections G1, G6, G2.2; loads per ASCE/SEI 7 Ch. 2.\n\n## Find\nphi_v*Vn, Vn/Omega_v, and adequacy.",
 "has_figure": false,
 "stem": "G_6",
 "breadcrumb": "EXAMPLE G.6 · AISC 360-22 Ch.G (beam shear) · §G6 §G2.2 §G1 · W21x48 Minor-Axis Shear Strength",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.6 · AISC 360-22 Ch.G (beam shear) · §G6 §G2.2 §G1 · W21x48 Minor-Axis Shear Strength

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G6 (Eq. G6-1, per shear-resisting element) with Cv2 per §G2.2 (Eq. G2-9, kv = 1.2, h/tw = bf/2tf); φv = 0.90, Ωv = 1.67 (§G1). Per the RAG extract provided.

---

### 1. Required Shear Strength (minor-axis direction)

D = 20.0 kips, L = 60.0 kips:

- **LRFD:** Vu = 1.2(20) + 1.6(60) = **120 kips**
- **ASD:** Va = 20 + 60 = **80.0 kips**

### 2. Shear Buckling Coefficient — §G2.2 via §G6

W21x48 (A992): bf = 8.14 in.; tf = 0.430 in. For I-shapes, h/tw is taken as bf/(2tf) = 9.47 with kv = 1.2:

1.10√(1.2 × 29,000/50) = **29.0** ≥ 9.47 → **Cv2 = 1.0** (Eq. G2-9; consistent with the §G6 User Note that Cv2 = 1.0 for all A6 W-shapes with Fy ≤ 70 ksi).

### 3. Nominal and Available Shear Strength — Eq. G6-1

Per flange (each shear-resisting element): Vn,fl = 0.6Fy·bf·tf·Cv2 = 0.6(50)(8.14)(0.430)(1.0) = 105 kips

Both flanges resist the minor-axis shear:

Vn = 2(105) = **210 kips**

- **LRFD:** φvVn = 0.90(210) = **189 kips** ≥ 120 kips ✓ (utilization 0.63)
- **ASD:** Vn/Ωv = 210/1.67 = **126 kips** ≥ 80.0 kips ✓ (utilization 0.64)

### 4. Conclusion

In weak-axis shear, the W21x48's two flanges act as the shear-resisting elements and yield (Cv2 = 1.0), providing φvVn = 189 kips (LRFD) and Vn/Ωv = 126 kips (ASD) — **adequate** for the 120 / 80 kip demands with ample reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
