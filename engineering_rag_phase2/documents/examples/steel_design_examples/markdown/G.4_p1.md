<!-- chunk_id: G.4_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.4",
 "example_family": "G.4",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G4",
  "G2.2",
  "G1",
  "B4.1"
 ],
 "eqs": [
  "G2-9"
 ],
 "tables": [],
 "title": "Rectangular HSS Shear Strength",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.4 — Rectangular HSS Shear Strength",
 "question": "# G.4 -- Rectangular HSS in Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A500/A500M Grade C rectangular HSS6x4x3/8, oriented with its 6-in. (wide)\nwalls vertical, is used as a beam carrying end shears of 11 kips from service dead\nload and 33 kips from service live load. Determine the available shear strength by\ndirectly applying AISC 360 Section G4 and verify adequacy for LRFD and ASD.\n\n## Given\n- Material: ASTM A500/A500M Grade C, Fy = 50 ksi.\n- Member: HSS6x4x3/8, wide walls vertical; H = 6.00 in., B = 4.00 in.,\n  design wall thickness t = 0.349 in.\n- Loads (service end shear): D = 11 kips, L = 33 kips.\n- Code basis: AISC 360-22 Sections G1, G4, G2.2; loads per ASCE/SEI 7 Ch. 2.\n\n## Find\nphi_v*Vn, Vn/Omega_v, and adequacy.",
 "has_figure": false,
 "stem": "G_4",
 "breadcrumb": "EXAMPLE G.4 · AISC 360-22 Ch.G (beam shear) · §G4 §G2.2 §G1 §B4.1 · Rectangular HSS Shear Strength",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.4 · AISC 360-22 Ch.G (beam shear) · §G4 §G2.2 §G1 §B4.1 · Rectangular HSS Shear Strength

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G4 (Vn = 0.6FyAwCv2, with Aw = 2ht and kv = 5) with Cv2 per §G2.2 (Eq. G2-9); φv = 0.90, Ωv = 1.67 (§G1). Per the RAG extract provided.

---

### 1. Required Shear Strength

D = 11 kips, L = 33 kips:

- **LRFD:** Vu = 1.2(11) + 1.6(33) = **66.0 kips**
- **ASD:** Va = 11 + 33 = **44.0 kips**

### 2. Web Geometry and Buckling Coefficient

HSS6x4x3/8 (A500 Gr. C), 6-in. walls vertical; t = 0.349 in. (design wall). Flat web depth (corner radius unknown → outside dimension minus 3t, per §B4.1 note):

h = H − 3t = 6.00 − 3(0.349) = 4.95 in. → h/t = 14.2

1.10√(kvE/Fy) = 1.10√(5 × 29,000/50) = **59.2** ≥ 14.2 → **Cv2 = 1.0** (Eq. G2-9)

### 3. Nominal and Available Shear Strength — §G4

Aw = 2ht = 2(4.95)(0.349) = 3.46 in.²

Vn = 0.6FyAwCv2 = 0.6(50)(3.46)(1.0) = **104 kips**

- **LRFD:** φvVn = 0.90(104) = **93.3 kips** ≥ 66.0 kips ✓ (utilization 0.71)
- **ASD:** Vn/Ωv = 104/1.67 = **62.1 kips** ≥ 44.0 kips ✓ (utilization 0.71)

### 4. Conclusion

The HSS6x4x3/8 webs (the two 6-in. walls) yield in shear (Cv2 = 1.0; h/t = 14.2 far below the buckling threshold) and provide φvVn = 93.3 kips (LRFD) and Vn/Ωv = 62.1 kips (ASD) — **adequate** for the 66 / 44 kip end shears with ~30% reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
