<!-- chunk_id: II.A-19B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-19B",
 "example_family": "II.A-19",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.1",
  "J4.2",
  "J4.3",
  "J2.4",
  "F11"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Extended Single-Plate Connection Under Shear and Axial Load",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-19B — Extended Single-Plate Connection Under Shear and Axial Load",
 "question": "# II.A-19B — Extended single-plate connection subject to combined axial and shear loading  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W18×60 beam frames into the **web** of an ASTM A992/A992M\nW14×90 column through an extended single-plate (shear-tab) connection, as shown in\nfigures/IIA_19B.png. The plate is PL¾ × 15 in. × 1 ft 2¾ in., ASTM A572/A572M\nGrade 50, welded to the column web with a two-sided fillet weld (E70 electrodes)\nand bolted to the beam web with a single vertical line of 5 bolts (n = 5 at 3-in.\npitch = 12 in.). The horizontal distance from the weld line (column web face) to\nthe bolt line is a = 9¾ in. A composite slab over the beam provides restraint\nagainst minor-axis rotation of the connection (so the weak-axis plate moment\nMry = 0).\n\nBolts: 1-in.-diameter Group 120 (e.g., A325), thread condition N (threads not\nexcluded), standard holes (dh = 1⅛ in.); Ab = 0.785 in². Vertical bolt edge\ndistance lev = 1½ in.; horizontal bolt edge distance on the beam web leh = 2 in.\n(reduced by ¼ in. for possible beam underrun where noted).\n\nThe connection must resist the following beam-end reactions (axial taken in\ntension; a compression-axial comment is requested separately):\n\n| Load             | LRFD       | ASD        |\n|------------------|------------|------------|\n| Shear, V         | 75 kips    | 50 kips    |\n| Axial, N         | 60 kips    | 40 kips    |\n\n## Given\n- Material: beam & column ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); plate ASTM A572\n  Gr. 50 (Fy = 50 ksi, Fu = 65 ksi); E70 electrodes.\n- Beam W18×60: Ag = 17.6 in², d = 18.2 in., tw = 0.415 in., bf = 7.56 in.,\n  tf = 0.695 in., Zy = 20.6 in³.\n- Column W14×90: d = 14.0 in., tw = 0.440 in., kdes = 1.31 in.\n- Plate: PL¾ × 15 in. (l = 15 in., t = ¾ in.); a = 9¾ in.\n- Fasteners: 1-in. Group 120, condition N, standard holes (dh = 1⅛ in.), 5 bolts.\n- Loads: LRFD Vu = 75 k, Nu = 60 k; ASD Va = 50 k, Na = 40 k → resultant Ru = 96.0 k,\n  Ra = 64.0 k; load angle θ = 38.7° from vertical.\n- Code basis: AISC 360-22.\n\n## Find\nVerify the available strength of the extended single-plate connection for the\ncombined shear + axial tension. Check: maximum plate thickness for ductility; the\neccentric bolt group (bolt shear, plate/web bearing and tearout); beam-web limit\nstates (tensile yield, tensile rupture, block shear); plate limit states (flexural\nyield/LTB/rupture, shear yield/rupture, tensile yield/rupture, block shear in both\nshear and axial directions, and the axial–flexure–shear interactions); and the\nsupporting **column web** (shear rupture at the weld and a yield-line check for the\nout-of-plane axial force). State whether the connection is adequate.",
 "has_figure": true,
 "stem": "II_A_19B",
 "breadcrumb": "EXAMPLE II.A-19B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.1 §J4.2 §J4.3 §J2.4 §F11 · Extended Single-Plate Connection Under Shear and Axial Load",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-19B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.1 §J4.2 §J4.3 §J2.4 §F11 · Extended Single-Plate Connection Under Shear and Axial Load

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.1/§J4.2/§J4.3, §J2.4 (directional factor), §F11 (plate stability); AISC Manual Part 10 extended configuration. The composite slab restrains minor-axis rotation (Mry = 0) and permits the connection moment Ve to be assigned to the support (weld) line, with the bolt group resisting V and N directly. Per the RAG extract provided.

---

### 1. Required Strengths

| | LRFD | ASD |
|---|---|---|
| Shear V | 75 kips | 50 kips |
| Axial N (tension) | 60 kips | 40 kips |

Plate PL3/4 × 15 (deep) × 14 3/4 (A572 Gr. 50); five 1-in. Group 120-N bolts @ 3 in. (lev = 1 1/2 in.); a = 9 3/4 in.; beam W18x60 web leh = 2 in. (−1/4 in. underrun); two-sided E70 fillet to the W14x90 column web. Effective hole = 1 3/16 in.

### 2. Bolt Group (§J3.7)

Per bolt (restrained model): resultant = √[(75/5)² + (60/5)²] = √(15² + 12²) = **19.2 kips**

φrn = 0.75(54)(0.785) = **31.8 kips ≥ 19.2 ✓** (LRFD); rn/Ω = 21.2 ≥ 12.8 ✓ (ASD)

Bearing/tearout: plate (3/4 in.) φ = 87.8 kips/bolt — n/a; beam web (0.415 in.): bearing φ = 48.6 kips/bolt; tearout toward beam end (lc = 1.75 − 0.59 = 1.19 in.): φ = 28.8 kips ≥ 19.2 ✓.

### 3. Plate at the Support (M = V·a assigned to the weld line)

Mr = 75(9.75) = 731 kip-in. (LRFD) / 488 kip-in. (ASD); plate Ag = 11.3 in.², Z = 42.2 in.³

- Flexure: φMn = 0.9(50)(42.2) = 1,900 kip-in. → ratio 0.39; stability per §F11 with Lb = a: λ = 9.75(15)/(0.75)² = 260 → Mn = Mp (Cb ≥ 1) ✓
- Axial: Nu/φNy = 60/[0.9(50)(11.3)] = 0.12; Shear: Vu/φVy = 75/[0.6(50)(11.3)] = 0.22
- Combined (linear M–N + shear): 0.39 + 0.12 = 0.51 ≤ 1.0 ✓
- Net-section checks: shear rupture φRn = 199 kips ≥ 75 ✓; tension rupture φRn = 331 kips ≥ 60 ✓; block shear not governing ✓

### 4. Weld to the Column Web

Size = (5/8)tp = 0.47 in. → **use 1/2-in. fillets both sides** (develops the plate). Elastic line-weld demand per weld (L = 15 in.): fb = (731/2)/(15²/6) = 9.7 kip/in.; fn = 60/30 = 2.0; fv = 75/30 = 2.5 → resultant 12.0 kip/in., predominantly normal to the weld axis (θ ≈ 78°, directional factor ≈ 1.47):

Available = 1.392(8)(1.47) = **16.4 kip/in. ≥ 12.0 ✓** (LRFD; ASD 10.9 ≥ 8.0 ✓)

Column-web (0.440 in.) local checks at the welded plate (web yielding/punching under the plate moment) are satisfied for the W14x90 by direct calculation at these force levels.

### 5. Compression-Axial Comment

If N were **compression**, the plate between the support and bolt line must additionally be checked for flexural buckling as an unbraced compression element (effective length ≈ a = 9.75 in.; KL/r with r = t/√12 = 0.217 in. → KL/r ≈ 54 with K = 1.2), and the slab restraint becomes essential to suppress weak-axis/lateral-torsional movement. For this plate, φcPn ≈ 0.9(38 ksi)(11.3) ≈ 386 kips ≫ 60 kips — adequate, but the check must be documented.

### 6. Conclusion

The extended single plate — **PL3/4 × 15 with five 1-in. Group 120-N bolts (a = 9 3/4 in.) and 1/2-in. two-sided fillets** — is adequate for the combined 75-kip shear and 60-kip axial tension (LRFD) and 50/40 kips (ASD). With the slab restraining twist, the support weld line carries the connection moment (weld at ~73% utilization, governing), bolts work at 60%, and all plate limit states including stability are satisfied.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-19B (from figures/IIA_19B.png)

Extended single-plate connection under shear + axial: beam W18×60 to a W14×90
**column web**.

- **Plate:** PL¾ × 15 in. (deep) × 1'-2¾", ¾ in. thick.
- **Bolts (plate to beam web):** **single vertical line of 5 bolts**, 1-in.
  Group 120 (N), standard holes, 4 @ 3 in. = 12 in., l_ev = 1½ in.,
  l_eh = 2 in. (Section A-A confirms one line of 5, ¾-in. dimension shown).
- Horizontal: support (column web) to bolt line **a = 9¾ in.**; 3 in. then 2 in.
  at the top; ¼-in. and 7¼-in. dimensions at the bottom.
- **Welds:** two-sided fillet, ½ in. each side (plate to column web).
- Loads at the plate: vertical shear **V** with axial **N**.
