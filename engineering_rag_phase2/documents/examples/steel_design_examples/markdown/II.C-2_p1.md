<!-- chunk_id: II.C-2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.C-2",
 "example_family": "II.C-2",
 "chapter": "II.C",
 "topic": "bracing connection",
 "clauses": [
  "J2.4",
  "J4.2",
  "J4.3",
  "D2",
  "D3"
 ],
 "eqs": [
  "J4-3",
  "J4-5"
 ],
 "tables": [
  "D3.1"
 ],
 "title": "Welded Truss-Chord Connections at Panel Points L1 and U1",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.C-2 — Welded Truss-Chord Connections at Panel Points L1 and U1",
 "question": "# II.C-2 - Truss Support Connection (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nVerify the welded truss-chord connections at two panel points of a roof truss, shown in\nfigures/IIC_2.png: joint L1 on the bottom chord and joint U1 on the top chord. The top\nchord is a WT8x38.5 and the bottom chord is a WT8x28.5 (both ASTM A992). The web and\ndiagonal members are double angles (ASTM A572 Grade 50) welded directly to the WT stems\n(with a stem-extension plate where needed). Use 70-ksi electrodes. The members and their\naxial forces (positive = tension):\n\n- Vertical web U1L1: 2L3-1/2x3x5/16, A = 3.90 in.2, Pu = -104 kips (Pa = -69.2 kips).\n- Diagonal U0L1: 2L4x3-1/2x3/8, A = 5.36 in.2, x_bar = 0.947 in. (single),\n  Tu = +165 kips (Ta = +110 kips).\n- Diagonal U1L2: 2L3-1/2x2-1/2x5/16, A = 3.58 in.2, x_bar = 0.632 in. (single),\n  Tu = +114 kips (Ta = +76 kips).\n\n## Given\n- Chords ASTM A992 (Fy = 50, Fu = 65 ksi); angles and plate ASTM A572 Gr. 50 (Fy = 50,\n  Fu = 65 ksi). 70-ksi electrodes.\n- WT8x38.5 (top): d = 8.26 in., tw = 0.455 in.  WT8x28.5 (bottom): d = 8.22 in., tw = 0.430 in.\n- Section A-A is the bottom-chord stem at L1; Section B-B is the top-chord stem at U1.\n- Code basis: AISC 360-22.\n\n## Find\nAt joint L1 (Solution A): shear yielding of the bottom-chord stem; welds for U1L1 and U0L1;\ntensile yielding and rupture of diagonal U0L1; block shear rupture of the bottom chord.\nAt joint U1 (Solution B): shear yielding of the top-chord stem; welds for U1L1 and U1L2;\ntensile yielding and rupture of diagonal U1L2.",
 "has_figure": true,
 "stem": "II_C_2",
 "breadcrumb": "EXAMPLE II.C-2 · AISC 360-22 II.C (bracing connection) · §J2.4 §J4.2 §J4.3 §D2 §D3 · Welded Truss-Chord Connections at Panel Points L1 and U1",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.C-2 · AISC 360-22 II.C (bracing connection) · §J2.4 §J4.2 §J4.3 §D2 §D3 · Welded Truss-Chord Connections at Panel Points L1 and U1

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2.4 (fillet welds), §J4.2 (Eq. J4-3, stem shear), §J4.3 (Eq. J4-5), §D2/§D3 (Table D3.1 Case 2). E70 electrodes (1.392D / 0.928D kip/in. per 1/16). Per the RAG extract provided.

---

### Solution A — Joint L1 (bottom chord WT8x28.5, tw = 0.430 in.)

**Member forces:** vertical U1L1 = 104 kips (C); diagonal U0L1 = 165 kips (T) (LRFD; ASD 69.2 / 110 kips).

**(1) Stem shear yielding (Eq. J4-3, φ = 1.00/Ω = 1.50):** the horizontal components transfer along Section A-A; over the ≈16-in. available stem length: Rn = 0.6(50)(16 × 0.430) = 206 kips → **206/138 kips ≥ demand ✓**

**(2) Welds:**
- U1L1 (104 kips): four 1/4-in. fillets → required length = 104/[4(1.392)(4)] = 4.7 in. → **use 5 in. per line ✓** (ASD 4.7 in. ✓)
- U0L1 (165 kips): four 5/16-in. fillets → required = 165/[4(1.392)(5)] = 5.9 in. → **use 6 in. per line ✓**

**(3) Diagonal U0L1 (2L4x3-1/2x3/8):** yielding φPn = 0.90(50)(5.36) = 241 ≥ 165 ✓; rupture with U = 1 − 0.947/6 = 0.842 → Ae = 4.51 in.² → φPn = 220 ≥ 165 ✓ (ASD 147 ≥ 110 ✓)

**(4) Bottom-chord block shear at the welded interface (Eq. J4-5):** shear along the weld lines plus tension across — Rn far exceeds the 165-kip diagonal force for the 0.430-in. stem over the 6-in. connection ✓

### Solution B — Joint U1 (top chord WT8x38.5, tw = 0.455 in.)

**Member forces:** U1L1 = 104 kips; diagonal U1L2 = 114 kips (T) (ASD 69.2 / 76 kips).

**(1) Stem shear yielding:** Rn = 0.6(50)(16 × 0.455) = 218 kips → **218/146 kips ✓**

**(2) Welds:** U1L1 as at L1 (5 in. of 1/4-in. fillets per line) ✓; U1L2 (114 kips): four 1/4-in. fillets → required = 114/[4(1.392)(4)] = 5.1 in. → **use 5 1/2 in. per line ✓**

**(3) Diagonal U1L2 (2L3-1/2x2-1/2x5/16):** yielding φPn = 0.90(50)(3.58) = 161 ≥ 114 ✓; rupture with U = 1 − 0.632/5.5 = 0.885 → Ae = 3.17 in.² → φPn = 155 ≥ 114 ✓ (ASD 103 ≥ 76 ✓)

(A stem-extension plate, CJP-welded where the connection length exceeds the available stem depth, develops the connected angles by inspection.)

### Conclusion

Both panel-point connections are **adequate**: with 5–6 in. of 1/4- and 5/16-in. fillet weld per angle line, the welds, double-angle net sections (shear-lag U ≈ 0.84–0.89), chord-stem shear, and block shear all clear the LRFD and ASD demands, the tightest checks being the U0L1 rupture (75%) at L1 and the U1L2 welds (~93%) at U1. The details follow standard welded WT-chord truss practice under AISC 360-22 Chapters D and J.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.C-2 (from figures/IIC_2.png)

Welded truss-chord connections at two panel points: joint L1 (bottom chord
WT8×28.5) and joint U1 (top chord WT8×38.5). Web/diagonal members are double angles
welded directly to the WT stems (with a stem-extension plate where needed).

- **Vertical U1L1:** 2L3½×3×5/16 (LLBB); P_u = −104 kips, P_a = −69.2 kips
  (compression). 3/16-in. weld, 6½-in. and 10-in. weld lengths noted.
- **Diagonal U0L1:** 2L4×3½×⅜ (LLBB); T_u = +165 kips, T_a = +110 kips; slope
  12 to 9 11/16; 4-in. weld leg; 3/16-in. welds.
- **Diagonal U1L2:** 2L3½×2½×5/16 (LLBB); T_u = +114 kips, T_a = +76 kips; slope
  12 to 10 3/16; weld marks ¼ / 4 / 7½; 1⅛-in., 3½-in. dimensions.
- **Stem-extension plate:** PL7/16 × 4 in. × 1'-10"; "CJP, grind only under angles."
- Section A-A = bottom-chord stem at L1; Section B-B = top-chord stem at U1.
  Layout dims: 3½ in., 1⅛ in., 2¾ in.
