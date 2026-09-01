<!-- chunk_id: D.9_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.9",
 "example_family": "D.9",
 "chapter": "D",
 "topic": "tension member",
 "clauses": [
  "B4.3b",
  "D3",
  "J3.4",
  "J3.5"
 ],
 "eqs": [
  "D3-1"
 ],
 "tables": [
  "D3.1"
 ],
 "title": "Net Area of a Flat Plate with Staggered Bolt Holes",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.9 — Net Area of a Flat Plate with Staggered Bolt Holes",
 "question": "# D.9 — Net area of a flat plate with staggered bolt holes  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA flat rectangular steel plate carries a static tensile force P along its length and\nis bolted at one end. The plate is 14 in. wide (measured transverse to the load) and\n½ in. thick. The end connection uses ¾-in.-diameter bolts placed in standard\n13/16-in. holes. The holes are arranged in two longitudinal gage lines that are\noffset (staggered) from one another along the length of the plate, so that the\ngoverning tension failure chain may run diagonally from hole to hole.\n\nUsing the staggered geometry shown in figures/D_9.png, determine the controlling\nnet area of the plate and its effective net area. Geometry (Fig. D.9-1):\n\n- The plate is loaded by P acting along its length; the 14-in. dimension is the\n  width across which the net section is taken.\n- Two bolt gage lines are offset along the length by a longitudinal stagger (pitch)\n  s = 2½ in.\n- Measured across the 14-in. width from the top edge, the bolt holes and edges lie at:\n  top edge (0 in.); hole B at 2 in. (gage line 1); hole C at 5 in. (gage line 2);\n  hole D at 9 in. (gage line 2); hole E at 12 in. (gage line 1); bottom edge (14 in.).\n  Thus the transverse gages are: edge→B = 2 in., B→C = 3 in., C→D = 4 in.,\n  D→E = 3 in., E→edge = 2 in. (sum = 14 in.).\n- Holes B and E lie on one gage line; holes C and D lie on the other gage line,\n  displaced from the first line by the longitudinal stagger s = 2½ in.\n- Points A, F, and G denote where a failure chain reaches the top edge (A) or the\n  bottom edge (F on line 1, G on line 2).\n\n## Given\n- Material: structural steel plate (ASTM A36). The quantities requested (net area,\n  effective net area) are geometric and do not depend on Fy or Fu.\n- Geometry: plate 14 in. wide × ½ in. thick; bolt layout per Fig. D.9-1\n  (figures/D_9.png), longitudinal stagger s = 2½ in., transverse gages\n  2-3-4-3-2 in. across the width.\n- Fasteners / holes: ¾-in.-diameter bolts in standard 13/16-in. holes.\n- Loads: static axial tension P along the length of the plate.\n- Code basis: AISC 360 (Specification for Structural Steel Buildings).\n\n## Find\n1. The controlling net area, A_n, of the plate, considering every possible straight\n   and diagonal (zigzag) failure chain across the width.\n2. The effective net area, A_e.",
 "has_figure": true,
 "stem": "D_9",
 "breadcrumb": "EXAMPLE D.9 · AISC 360-22 Ch.D (tension member) · §B4.3b §D3 §J3.4 §J3.5 · Net Area of a Flat Plate with Staggered Bolt Holes",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.9 · AISC 360-22 Ch.D (tension member) · §B4.3b §D3 §J3.4 §J3.5 · Net Area of a Flat Plate with Staggered Bolt Holes

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §B4.3b (net area; 1/16-in. hole-damage allowance; s²/4g rule for staggered chains) and §D3 (Eq. D3-1, Table D3.1 Case 1). Per the RAG extract provided.

---

### 1. Geometry

| Item | Value |
|---|---|
| Plate | 14 in. wide × 1/2 in. thick; static tension P along length |
| Holes | 3/4-in. bolts, standard 13/16-in. holes |
| Transverse gages (top → bottom) | 2 (edge–B), 3 (B–C), 4 (C–D), 3 (D–E), 2 (E–edge) in. |
| Stagger | B, E on gage line 1; C, D on line 2, offset longitudinally s = 2.5 in. |

**Effective hole width (§B4.3b):** dh = 13/16 + 1/16 = **7/8 in. = 0.875 in.**

Gross area: Ag = 14(0.500) = 7.00 in.²

### 2. Failure Chains — §B4.3b (net width = gross width − Σdh + Σs²/4g)

The s²/4g term is added for each diagonal (staggered) segment of a chain.

**Chain 1 — straight through B and E (2 holes, no stagger):**
wn = 14 − 2(0.875) = **12.25 in.**

**Chain 2 — straight through C and D (2 holes):**
wn = 14 − 2(0.875) = **12.25 in.**

**Chain 3 — A–B–C–G (2 holes, one diagonal B→C, s = 2.5 in., g = 3 in.):**
wn = 14 − 2(0.875) + (2.5)²/[4(3)] = 12.25 + 0.521 = **12.77 in.** (not critical)

**Chain 4 — A–B–C–D–F′ (3 holes; diagonal B→C; straight C→D):**
wn = 14 − 3(0.875) + 0.521 = **11.90 in.**

**Chain 5 — A–B–C–D–E–F (all 4 holes; diagonals B→C and D→E, each s = 2.5 in., g = 3 in.; straight C→D):**
wn = 14 − 4(0.875) + (2.5)²/[4(3)] + (2.5)²/[4(3)] = 14 − 3.50 + 0.521 + 0.521 = **11.54 in.** ← **controls**

### 3. Controlling Net Area

An = wn · t = 11.54(0.500) = **5.77 in.²**

(Compare Ag = 7.00 in.²; the staggered 4-hole chain removes the equivalent of 2.46 in. of width.)

### 4. Effective Net Area — §D3, Eq. D3-1

The member is a flat plate and the tension load is transmitted directly to the (single) cross-sectional element by the fasteners → **Table D3.1, Case 1: U = 1.0**.

Ae = An U = 5.77(1.0) = **5.77 in.²** (Eq. D3-1)

### 5. Conclusion

Checking every straight and zigzag chain across the 14-in. width per §B4.3b, the controlling chain is the full zigzag A–B–C–D–E–F through all four holes, giving a net width of 11.54 in. and:

- **Controlling net area: An = 5.77 in.²**
- **Effective net area: Ae = 5.77 in.²** (U = 1.0, Table D3.1 Case 1)

These areas would be used with Eq. D2-2 (Pn = FuAe) for the tensile rupture check of the plate; bolt spacing/edge distances should also satisfy §J3.4/§J3.5 in the connection design.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — D.9 (from figures/D_9.png)

Flat plate in tension, force P applied along the length (both ends), plate ½ in.
thick. Bolt holes ¾-in. bolts in 13/16-in. standard holes.

- Across the 14-in. width (top edge → bottom edge), measured from the top edge:
  top edge A (0 in.) → hole B (2 in.) → hole C (5 in.) → hole D (9 in.) →
  hole E (12 in.) → bottom edge (14 in.). Transverse gages: 2, 3, 4, 3, 2 in.
- Two longitudinal gage lines offset (staggered) by pitch **s = 2½ in.**:
  holes B and E lie on one gage line; holes C and D lie on the other line,
  shifted along the length by s.
- Points F (on line 1) and G (on line 2) mark where a failure chain reaches the
  bottom edge; A is the top-edge start.
- Failure chains to check: straight across (B–E) and the zigzag A-B-C-D-E-F
  through all four holes.
