<!-- chunk_id: G.7_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.7",
 "example_family": "G.7",
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
 "title": "C9x20 Minor-Axis Shear Strength",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.7 — C9x20 Minor-Axis Shear Strength",
 "question": "# G.7 -- Singly Symmetric Shape in Minor-Axis Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M C9x20 channel resists end shears of 7.5 kips from service dead load\nand 22.5 kips from service live load applied in the WEAK (minor-axis) direction. No\nAISC *Manual* tables cover minor-axis shear of channels, so determine the available\nminor-axis shear strength directly from AISC 360 Section G6 and verify adequacy.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: C9x20; bf = 2.65 in., tf = 0.413 in.; loaded in minor-axis shear.\n- Loads (service end shear): D = 7.5 kips, L = 22.5 kips.\n- Code basis: AISC 360-22 Sections G1, G6, G2.2; loads per ASCE/SEI 7 Ch. 2.\n\n## Find\nphi_v*Vn, Vn/Omega_v, and adequacy.",
 "has_figure": false,
 "stem": "G_7",
 "breadcrumb": "EXAMPLE G.7 · AISC 360-22 Ch.G (beam shear) · §G6 §G2.2 §G1 · C9x20 Minor-Axis Shear Strength",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.7 · AISC 360-22 Ch.G (beam shear) · §G6 §G2.2 §G1 · C9x20 Minor-Axis Shear Strength

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G6 (Eq. G6-1, per shear-resisting element) with Cv2 per §G2.2 (Eq. G2-9, kv = 1.2, h/tw = bf/tf for channels); φv = 0.90, Ωv = 1.67 (§G1). Per the RAG extract provided.

---

### 1. Required Shear Strength (minor-axis direction)

D = 7.5 kips, L = 22.5 kips:

- **LRFD:** Vu = 1.2(7.5) + 1.6(22.5) = **45.0 kips**
- **ASD:** Va = 7.5 + 22.5 = **30.0 kips**

### 2. Shear Buckling Coefficient — §G2.2 via §G6

C9x20 (A992): bf = 2.65 in.; tf = 0.413 in. For channels, h/tw is taken as bf/tf = 6.42 with kv = 1.2:

1.10√(1.2 × 29,000/50) = **29.0** ≥ 6.42 → **Cv2 = 1.0** (Eq. G2-9)

### 3. Nominal and Available Shear Strength — Eq. G6-1

Per flange: Vn,fl = 0.6Fy·bf·tf·Cv2 = 0.6(50)(2.65)(0.413)(1.0) = 32.8 kips

Both flanges resist the minor-axis shear:

Vn = 2(32.8) = **65.7 kips**

- **LRFD:** φvVn = 0.90(65.7) = **59.1 kips** ≥ 45.0 kips ✓ (utilization 0.76)
- **ASD:** Vn/Ωv = 65.7/1.67 = **39.3 kips** ≥ 30.0 kips ✓ (utilization 0.76)

### 4. Conclusion

The C9x20 channel flanges, evaluated per §G6 with the channel-specific slenderness bf/tf, are stocky enough to yield in shear (Cv2 = 1.0). Available minor-axis shear strengths of 59.1 kips (LRFD) and 39.3 kips (ASD) exceed the required 45 / 30 kips — **the channel is adequate**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
