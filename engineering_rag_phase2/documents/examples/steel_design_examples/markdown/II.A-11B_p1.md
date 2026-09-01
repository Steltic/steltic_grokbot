<!-- chunk_id: II.A-11B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-11B",
 "example_family": "II.A-11",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.8",
  "J3.11",
  "J4.1",
  "J4.2",
  "J4.3",
  "J2.4"
 ],
 "eqs": [
  "J3-2",
  "J3-6a",
  "J4-1",
  "J4-2",
  "J4-3",
  "J4-4",
  "J4-5"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "End-Plate Connection Under Combined Shear and Axial Tension",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-11B — End-Plate Connection Under Combined Shear and Axial Tension",
 "question": "# II.A-11B — End-plate connection subject to combined axial and shear loading  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported ASTM A992/A992M W18×50 beam frames into a support through a\nbolted/welded end-plate (shear tab welded to the beam end, bolted to the support).\nThe end plate is a PL½×8½ in. by 1 ft 2½ in. (14½ in.) long, ASTM A572/A572M\nGrade 50. The plate is attached to the beam web by a pair of ³⁄₁₆-in. fillet welds\n(one each side of the web) made with 70-ksi (E70) electrodes, and bolted to the\nsupport with two vertical lines of bolts (a pair per row) using ⅞-in.-diameter\nGroup 120 (e.g., A325) bolts, thread condition N (threads not excluded), in\nstandard holes.\n\nBolt layout (see figures/IIA_11B.png): 5 rows at 3 in. pitch (4 spaces @ 3 in. =\n1 ft 0 in.) with a 1¼-in. vertical edge distance top and bottom (overall plate\nlength 14½ in.); gage between the two bolt lines = 5½ in.; horizontal edge distance\nto each plate edge = 1½ in. (plate width 8½ in.). The connection must resist a\nbeam-end reaction consisting of a vertical shear combined with axial tension:\n\n| Load              | LRFD       | ASD        |\n|-------------------|------------|------------|\n| Shear, V          | 75 kips    | 50 kips    |\n| Axial tension, N  | 60 kips    | 40 kips    |\n\n## Given\n- Material: beam ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); plate ASTM A572 Gr. 50\n  (Fy = 50 ksi, Fu = 65 ksi); E70 weld electrodes.\n- Beam: W18×50 — Ag = 14.7 in.², d = 18.0 in., tw = 0.355 in.\n- Plate: PL½ × 8½ in. × 14½ in.\n- Fasteners: ⅞-in. Group 120 bolts, condition N, standard holes (dh = ¹⁵⁄₁₆ in.);\n  Ab = 0.601 in.²; 10 bolts total (5 rows × 2).\n- Welds: ³⁄₁₆-in. fillet, both sides of web, E70.\n- Loads: LRFD Vu = 75 k, Nu = 60 k; ASD Va = 50 k, Na = 40 k (combined → resultant\n  Ru = 96.0 k, Ra = 64.0 k).\n- Code basis: AISC 360-22.\n\n## Find\nVerify the connection is adequate for the combined shear and axial tension. Check\nthe governing limit states: bolt shear; bolt bearing/tearout on the plate; bolt\ncombined tension–shear (with prying action of the end plate); the beam-web fillet\nweld (and required beam-web thickness); shear yielding, shear rupture, and block\nshear rupture of the plate; and shear yielding, tensile yielding and tensile\nrupture of the beam.",
 "has_figure": true,
 "stem": "II_A_11B",
 "breadcrumb": "EXAMPLE II.A-11B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.8 §J3.11 §J4.1 §J4.2 §J4.3 §J2.4 · End-Plate Connection Under Combined Shear and Axial Tension",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-11B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.8 §J3.11 §J4.1 §J4.2 §J4.3 §J2.4 · End-Plate Connection Under Combined Shear and Axial Tension

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.8 (Eq. J3-2, combined tension and shear in bolts), §J3.11 (Eqs. J3-6a/c), §J4.1 (Eqs. J4-1, J4-2), §J4.2 (Eqs. J4-3, J4-4), §J4.3 (Eq. J4-5), §J2.4 (fillet welds with directional factor). Prying per AISC Manual Part 9. Per the RAG extract provided.

---

### 1. Required Strengths

| | LRFD | ASD |
|---|---|---|
| Shear V | 75 kips | 50 kips |
| Tension N | 60 kips | 40 kips |
| Resultant R | 96.0 kips | 64.0 kips |

PL 1/2 × 8 1/2 × 14 1/2 (A572 Gr. 50); ten 7/8-in. Group 120-N bolts (2 lines @ g = 5 1/2 in., 5 rows @ 3 in., lev = 1 1/4 in., leh = 1 1/2 in.); 3/16-in. E70 fillets both sides of the W18x50 web (tw = 0.355 in.). Effective hole = 1.00 in.

### 2. Bolts — Shear, Combined Tension/Shear (§J3.7, §J3.8)

Per bolt: shear = 7.5/5.0 kips → frv = 12.5/8.32 ksi; tension = 6.0/4.0 kips.

frv/(φFnv) = 12.5/40.5 = 0.31 > 0.30 → combined check required (§J3.8 User Note):

F′nt = 1.3Fnt − (Fnt/φFnv)frv = 1.3(90) − 2.22(12.5) = **89.3 ksi ≤ 90** (LRFD; ASD identical, 89.3 ksi)

Available bolt tension: φF′ntAb = 0.75(89.3)(0.601) = **40.3 kips** ≥ 6.0 ✓ (ASD 26.8 ≥ 4.0 ✓). Bolt shear φrn = 24.3 kips ≥ 7.5 ✓.

**Prying action (Manual Part 9):** b′ = (g − tw)/2 − d/2 = 2.14 in.; a′ = 1.94 in.; ρ = 1.10; p = 3 in.; δ = 0.688; tc = 1.40 in. → Q = (t/tc)²(1 + δ) = 0.216 → available tension per bolt incl. prying = 40.3(0.216) = **8.7 kips ≥ 6.0 ✓** (ASD 8.7 ≥ 4.0 ✓).

### 3. Bearing/Tearout on the Plate (§J3.11, vertical shear)

Interior bolts: 2.4dtFu = 68.3 kips (φ = 51.2) → bolt shear governs (24.3). Bottom-row bolts: lc = 1.25 − 0.50 = 0.781 in. → 1.2lctFu = 30.5 kips, φ = 22.9 kips.
Group: 2(22.9) + 8(24.3) = **240 kips (LRFD)** / 160 kips (ASD) ≥ 75/50 ✓✓.

### 4. Plate Limit States

- Shear yielding (Eq. J4-3, two planes): Rn = 0.6(50)(2 × 14.5 × 0.5) = 435 kips → 435/290 ✓
- Shear rupture (Eq. J4-4): Anv = 2(14.5 − 5 × 1.0)(0.5) = 9.5 in.² → φRn = 278 ✓
- Tensile yielding (Eq. J4-1): Rn = 50(7.25) = 363 → 326/217 ≥ 60/40 ✓
- Tensile rupture (Eq. J4-2): An = (8.5 − 2 × 1.0)(0.5) = 3.25 in.² → φRn = 158/106 ✓
- Block shear (Eq. J4-5, 2 blocks): per block Anv = 4.38 in.², Ant = 0.50 in.², Agv = 6.63 in.² → Rn = 203 kips/block → φRn = 305 ✓

### 5. Weld and Beam Web

Resultant 96.0/64.0 kips at θ = tan⁻¹(60/75) = 38.7° to the weld axis; directional factor (1 + 0.5sin^1.5θ) = 1.25 (§J2.4 Eq. J2-5):

φRn = 2(1.392)(3)(14.5)(1.25) = **151 kips ≥ 96.0 ✓**; Rn/Ω = 2(0.928)(3)(14.5)(1.25) = **101 kips ≥ 64.0 ✓**

Beam web: shear yield 0.6(50)(14.5)(0.355) = 154 kips ≥ 75 ✓; tension yield 50(14.5)(0.355) → φ = 232 kips ≥ 60 ✓.

### 6. Conclusion

The end-plate connection is **adequate for the combined 75-kip shear + 60-kip tension (LRFD)** and 50 + 40 kips (ASD). The interactive bolt check (Eq. J3-2 with frv at 31% of available) and prying action on the 1/2-in. plate are the most consequential checks — prying reduces the per-bolt tension capacity to 8.7 kips, still 45% above demand. Welds (with the directional strength increase) and all plate limit states pass with margin. The connection complies with AISC 360-22 Chapter J.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-11B (from figures/IIA_11B.png)

End-plate connection under shear + axial: **PL½ × 8½ in. × 1'-2½" (14½ in. long)**
welded to the end of a W18×50 beam web and bolted to the support.

- **Bolts:** ⅞-in. Group 120 (N), standard holes; two vertical lines (a pair per
  row), **5 rows**: l_ev = 1¼ in. top/bottom, 4 @ 3 in. = 1'-0" (12 in.).
- **Gage between the two bolt lines = 5½ in.**; 3 in. from the top edge to the
  first row; ½-in. dimension at the plate edge (setback side).
- **Welds:** 3/16-in. fillet, one each side of the beam web.
- Loads at the plate: vertical shear **V** combined with axial tension **N**.
