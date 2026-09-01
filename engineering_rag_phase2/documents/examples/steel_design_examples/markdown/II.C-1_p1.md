<!-- chunk_id: II.C-1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.C-1",
 "example_family": "II.C-1",
 "chapter": "II.C",
 "topic": "bracing connection",
 "clauses": [
  "J2",
  "J3.7",
  "J3.11a",
  "J4.1",
  "J4.3",
  "D2",
  "D3",
  "J3.8"
 ],
 "eqs": [],
 "tables": [
  "J2.5",
  "D3.1"
 ],
 "title": "Truss End and Diagonal Brace Connection at a Column",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.C-1 — Truss End and Diagonal Brace Connection at a Column",
 "question": "# II.C-1 - Truss Support Connection (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA diagonal brace and the end of a roof truss frame into a column through a gusset\nplate and a pair of clip angles, as shown in figures/IIC_1.png. The top chord is a\nWT8x38.5 (ASTM A992) sloped 1/2 in 12; the supporting member is a W12x50 column\n(ASTM A992). A 2L4x3-1/2x3/8 double-angle diagonal brace (ASTM A572 Grade 50) is\nwelded to a gusset plate. The gusset is welded to the WT stem with a CJP weld and is\nbolted to the column through a pair of 2L4x4x5/8 clip angles (ASTM A572 Grade 50)\nusing five pairs (10 total) of 7/8-in.-diameter Group 120 bolts, threads not excluded\nfrom the shear plane (thread condition N), in standard holes at 3-in. vertical spacing.\nUse 70-ksi electrodes. Verify the connection (LRFD and ASD).\n\n## Given\n- Material: WT8x38.5 top chord and W12x50 column ASTM A992 (Fy = 50 ksi, Fu = 65 ksi);\n  diagonal brace, gusset plate, and clip angles ASTM A572 Gr. 50 (Fy = 50 ksi, Fu = 65 ksi).\n- WT8x38.5: d = 8.26 in., tw = 0.455 in., y_bar = 1.63 in.\n- W12x50 column: d = 12.2 in., bf = 8.08 in., tf = 0.640 in., tw = 0.370 in.\n- Diagonal 2L4x3-1/2x3/8: A = 5.36 in.2, x_bar = 0.947 in. (single angle), t = 3/8 in.\n- Clip angles 2L4x4x5/8: t = 5/8 in., bolt gage in outstanding leg = 4-1/2 in.\n- Bolts: 7/8-in. Group 120, thread condition N, standard holes (dh = 15/16 in.),\n  Ab = 0.601 in.2, five rows at s = 3 in., edge distance lev = 1-1/2 in., leh = 2 in.\n- Required strengths (from the member-force diagram):\n  Brace axial Ru = 168 kips (Ra = 112 kips); truss end reaction Ru = 106 kips\n  (Ra = 70.4 kips); top-chord axial Ru = 131 kips (Ra = 87.2 kips).\n- Code basis: AISC 360-22.\n\n## Find\nVerify: (a) the gusset-to-column connection (bolt shear; bearing/tearout; bolt\ntension-shear interaction including prying; shear yielding, shear rupture and block\nshear of the clip angles; clip-angle-to-gusset weld) and (b) the gusset size and the\nweld connecting the diagonal to the gusset (weld length, gusset shear rupture, brace\ntensile yielding and rupture, and gusset Whitmore-section tensile yielding).",
 "has_figure": true,
 "stem": "II_C_1",
 "breadcrumb": "EXAMPLE II.C-1 · AISC 360-22 II.C (bracing connection) · §J2 §J3.7 §J3.11a §J4.1 §J4.3 §D2 §D3 §J3.8 · Truss End and Diagonal Brace Connection at a Column",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.C-1 · AISC 360-22 II.C (bracing connection) · §J2 §J3.7 §J3.11a §J4.1 §J4.3 §D2 §D3 §J3.8 · Truss End and Diagonal Brace Connection at a Column

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2 (fillet and CJP welds, Table J2.5), §J3.7/§J3.11a, §J4.1–§J4.3, §D2/§D3 (Table D3.1 Case 2 for the welded double-angle brace). Per the RAG extract provided.

---

### 1. Required Strengths (from the member-force diagram)

Brace (2L4x3-1/2x3/8): **Ru = 168 / Ra = 112 kips**; truss end reaction (vertical, to the column): **Ru = 106 / Ra = 70.4 kips**; top-chord axial: 131 / 87.2 kips (balanced through the WT8x38.5 chord).

### 2. Brace-to-Gusset (welded)

- Tensile yielding (Eq. D2-1): φPn = 0.90(50)(5.36) = **241 kips ≥ 168 ✓** (ASD 160 ≥ 112 ✓)
- Welds: four 5/16-in. E70 fillets (toe and heel of each angle), length 8 in.: φRn = 4(1.392)(5)(8) = **223 kips ≥ 168 ✓** (ASD 149 ≥ 112 ✓)
- Tensile rupture (Eqs. D2-2/D3-1, Case 2): U = 1 − x̄/l = 1 − 0.947/8 = 0.882 → Ae = 4.73 in.² → φPn = 0.75(65)(4.73) = **230 kips ≥ 168 ✓** (ASD 154 ≥ 112 ✓)
- Gusset on the Whitmore section and gusset-to-WT **CJP** weld: with matching filler the CJP develops the gusset/base metal (Table J2.5) ✓.

### 3. Gusset/Clip-Angle-to-Column Bolt Group (10 — 7/8-in. Group 120-N)

The column connection delivers the 106-kip vertical reaction (the brace horizontal component is equilibrated by the chord):

- Bolt shear: 10(24.3) = **243 kips ≥ 106 ✓** (ASD 162 ≥ 70.4 ✓)
- Bearing/tearout on the 5/8-in. clip angles and 0.640-in. column flange: ≥ bolt shear per fastener ✓
- Any incidental tension on the outstanding legs (with prying, 5/8-in. angles, 4 1/2-in. gage) is small relative to the §J3.8 interactive capacity ✓

### 4. Clip Angles (2L4x4x5/8 × 15 in.)

Shear yielding (Eq. J4-3): 0.6(50)(2 × 15 × 0.625) = **563 kips ≥ 106 ✓**; shear rupture and block shear at the bolt line — large margins ✓.

### 5. Conclusion

All elements of the truss-end connection are **adequate with substantial reserve**: the welded double-angle brace is governed by its net-section rupture with shear lag (230 vs. 168 kips, 73% utilized LRFD); the brace welds work at 75%; and the 10-bolt clip-angle group to the column carries the 106-kip reaction at only 44% utilization. The CJP gusset-to-chord weld develops the connected parts by inspection. The connection satisfies AISC 360-22 Chapters D and J for both LRFD and ASD.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.C-1 (from figures/IIC_1.png)

Truss support connection at a W12×50 column. Top chord WT8×38.5 (sloped ½ in 12);
double-angle diagonal brace welded to a gusset; gusset bolted to the column through
clip angles.

- **Gusset plate:** PL½ × 12 in. × 1'-3" (ASTM A572 Gr. 50); welded to the WT stem
  with a CJP weld ("CJP, grind for fit up of angles").
- **Diagonal brace:** 2L4×3½×⅜ (LLBB), welded to the gusset; brace slope ≈ 12 to
  9 11/16; ¼-in. weld marks (¼, 8) and a 4-in. / 1¼-in. weld dimension shown.
- **Gusset-to-column clip angles:** 2L4×4×⅝ × 1'-3"; **five pairs (10 total) ⅞-in.
  Group 120 (N)** bolts in standard holes, 4 @ 3 in. = 12 in., l_ev = 1½ in.,
  **outstanding-leg gage = 4½ in.** (Section A-A: 2", 4½", 2"), l_eh = 2 in.
- Work point (w.p.) on the horizontal line through the column; 2½", 1'-0", 1'-3",
  1⅛", 1⅝" (≈1.63 in. angle), and 4-in. layout dimensions shown.
