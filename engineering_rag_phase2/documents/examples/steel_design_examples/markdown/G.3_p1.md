<!-- chunk_id: G.3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.3",
 "example_family": "G.3",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G3",
  "G2.2",
  "G1"
 ],
 "eqs": [
  "G3-1",
  "G2-9"
 ],
 "tables": [],
 "title": "Single-Angle Shear Strength",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.3 — Single-Angle Shear Strength",
 "question": "# G.3 -- Single Angle in Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A572/A572M Grade 50 single angle L5x3x1/4 is oriented with its long (5-in.)\nleg vertical and carries end shears of 5 kips from service dead load and 15 kips from\nservice live load in the plane of the long leg. There are no AISC *Manual* tables for\nangles in shear, so determine the available shear strength directly from AISC 360\nSection G3 and verify adequacy for LRFD and ASD.\n\n## Given\n- Material: ASTM A572/A572M Grade 50, Fy = 50 ksi.\n- Member: L5x3x1/4, long leg vertical; resisting leg b = 5.00 in., t = 1/4 in.\n- Loads (service end shear): D = 5 kips, L = 15 kips.\n- Code basis: AISC 360-22 Sections G1, G3, G2.2; loads per ASCE/SEI 7 Ch. 2.\n\n## Find\nphi_v*Vn, Vn/Omega_v, and adequacy.",
 "has_figure": false,
 "stem": "G_3",
 "breadcrumb": "EXAMPLE G.3 · AISC 360-22 Ch.G (beam shear) · §G3 §G2.2 §G1 · Single-Angle Shear Strength",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.3 · AISC 360-22 Ch.G (beam shear) · §G3 §G2.2 §G1 · Single-Angle Shear Strength

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G3 (Eq. G3-1) with Cv2 per §G2.2 (Eq. G2-9, kv = 1.2); φv = 0.90, Ωv = 1.67 (§G1). Per the RAG extract provided.

---

### 1. Required Shear Strength

D = 5 kips, L = 15 kips (in the plane of the long leg):

- **LRFD:** Vu = 1.2(5) + 1.6(15) = **30.0 kips**
- **ASD:** Va = 5 + 15 = **20.0 kips**

### 2. Shear Buckling Coefficient — §G2.2 with b/t and kv = 1.2

L5x3x1/4, long leg resisting: b = 5.00 in., t = 0.250 in. → b/t = 20.0

1.10√(kvE/Fy) = 1.10√(1.2 × 29,000/50) = **29.0** ≥ 20.0 → **Cv2 = 1.0** (Eq. G2-9) — shear yielding, no buckling reduction.

### 3. Nominal and Available Shear Strength — Eq. G3-1

Vn = 0.6Fy·b·t·Cv2 = 0.6(50)(5.00)(0.250)(1.0) = **37.5 kips**

- **LRFD:** φvVn = 0.90(37.5) = **33.8 kips** ≥ 30.0 kips ✓ (utilization 0.89)
- **ASD:** Vn/Ωv = 37.5/1.67 = **22.5 kips** ≥ 20.0 kips ✓ (utilization 0.89)

### 4. Conclusion

The L5x3x1/4 (A572 Gr. 50), with its 5-in. leg resisting the shear, yields in shear (Cv2 = 1.0) and provides φvVn = 33.8 kips (LRFD) and Vn/Ωv = 22.5 kips (ASD) — **adequate** for the 30 / 20 kip demands.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
