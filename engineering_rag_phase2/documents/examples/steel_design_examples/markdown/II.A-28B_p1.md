<!-- chunk_id: II.A-28B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-28B",
 "example_family": "II.A-28",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "B3.9",
  "J3.7",
  "J3.11",
  "J4.1"
 ],
 "eqs": [
  "J3-6b"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Single-Angle Connection: Structural Integrity Check (§B3.9)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-28B — Single-Angle Connection: Structural Integrity Check (§B3.9)",
 "question": "# II.A-28B — All-Bolted Single-Angle Connection: Structural-Integrity Check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simple beam-end connection uses a single angle bolted to a girder web to support a beam.\nWe must verify that this connection satisfies the structural-integrity (tie-force) provisions\nof AISC 360-22 Section B3.9, as required when design for structural integrity is mandated by\nthe applicable building code.\n\nThe connection: an ASTM A572 Grade 50 single angle L4×3×3/8, 11½ in. long, is shop-attached to\nthe web of an ASTM A992 W21×62 girder (Fy = 50 ksi, Fu = 65 ksi; d = 21.0 in., tw = 0.400 in.),\nand field-bolted to the web of an ASTM A992 W18×35 supported beam (Fy = 50 ksi, Fu = 65 ksi;\ntw = 0.300 in.). Four ¾-in.-diameter Group 120 bolts (thread condition N) in standard holes\n(dh = 13/16 in., Ab = 0.442 in.²) are in a single vertical line at 3-in. pitch (3 @ 3 in. = 9 in.).\nOn the angle, the horizontal edge distance to the bolt line is leh = 1½ in. and the vertical end\ndistance is lev = 1¼ in.; on the beam web the horizontal edge distance is leh = 1¾ in.\n(reduced by a ¼-in. beam-underrun tolerance). The gage on the support leg is 1¾ in.\nThe geometry is shown in figures/IIA_28B.png.\n\nThe required vertical shear strength of this beam-end connection (from the companion strength\ncheck of the same connection) is Vu = 39.8 kips (LRFD) / Va = 26.5 kips (ASD).\n\n## Given\n- Material: beam, girder ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); angle ASTM A572 Gr. 50 (Fy = 50, Fu = 65).\n- Geometry: L4×3×3/8 × 11½ in.; 4 bolts ¾-in. Group 120 (N) std. holes at 3-in. pitch; leh,angle = 1½ in., lev = 1¼ in.; leh,web = 1¾ in.; support-leg gage 1¾ in.\n- Members: W18×35 beam (tw = 0.300 in.); W21×62 girder (tw = 0.400 in.).\n- Required connection shear: Vu = 39.8 kips (LRFD), Va = 26.5 kips (ASD).\n- Code basis: AISC 360-22, Section B3.9 (structural integrity).\n\n## Find\nDetermine the minimum required nominal axial tie strength T per AISC 360-22 Section B3.9(b),\nthen determine the available nominal tensile (tie) strength Tn of the connection from the\ngoverning limit state, and confirm Tn ≥ T. Per B3.9, inelastic deformation of the connection\nis permitted in evaluating these requirements.",
 "has_figure": true,
 "stem": "II_A_28B",
 "breadcrumb": "EXAMPLE II.A-28B · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 §J4.1 · Single-Angle Connection: Structural Integrity Check (§B3.9)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-28B · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 §J4.1 · Single-Angle Connection: Structural Integrity Check (§B3.9)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §B3.9 (nominal-strength basis; inelastic deformation permitted), with §J3.7/Table J3.2, §J3.11 (Eqs. J3-6b/d — deformation not a consideration), §J4.1. Per the RAG extract provided.

---

### 1. Required Nominal Tie Force — §B3.9(b)

From the companion strength check: Vu = 39.8 kips / Va = 26.5 kips.

T = max[(2/3)(39.8), 26.5] = **26.5 kips**

### 2. Nominal Tensile Strength Tn (least of the applicable limit states)

Tie path: beam web → four 3/4-in. Group 120 bolts (shear) → angle (bending of the 1 3/4-in.-gage support leg) → support-leg bolts (tension) → girder web.

**(a) Bolt shear, beam-web leg:** Rn = 4(54)(0.442) = **95.5 kips**

**(b) Bolt tension, support leg:** Rn = 4(90)(0.442) = **159 kips**

**(c) Bearing/tearout (deformation not a consideration):**
Beam web (leh = 1 3/4 − 1/4 underrun = 1 1/2 in.; lc = 1.09 in.): 1.5lctwFu = 31.9 kips/bolt → 4(31.9) = **128 kips**
Angle (leh = 1 1/2 in.): 1.5lctFu = 39.9 kips/bolt → **160 kips**

**(d) Angle-leg flexure (support leg bending across the 1 3/4-in. gage, double-curvature mechanism, nominal):**
m = Fyt²/4 = 50(0.375)²/4 = 1.76 kip-in./in.; b′ ≈ 1.0 in.; over l = 11.5 in.:
Tn = 2ml/b′ = 2(1.76)(11.5)/1.0 = **40.4 kips** ← **governs**

**(e) Angle tension rupture (Eq. J4-2 basis):** FuAn = 65(3.00) = **195 kips**

**Controlling Tn = 40.4 kips ≥ T = 26.5 kips ✓ — §B3.9(b) satisfied** (utilization 0.66)

### 3. Column-Bracing Capacity — §B3.9(c)

- **LRFD:** Pu,max = 40.4/[0.01(2/3)] = **≈6,060 kips**; **ASD:** Pa,max = **≈4,040 kips**

### 4. Conclusion

The single-angle connection satisfies the structural-integrity provisions: its nominal tie capacity of **40.4 kips — governed by bending of the thin support leg across the short 1 3/4-in. gage** — exceeds the required 26.5-kip tie force by ~50%. Bolts, bearing/tearout (using the relaxed Eqs. J3-6b/d), and angle rupture are all far stronger. Under §B3.9(c), the connection could brace columns up to several thousand kips — well beyond practical demand. No modification is required.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-28B (from figures/IIA_28B.png)

Same single-angle connection as II.A-28A (structural-integrity check): beam W18×35
to W21×62 girder web; top-flange cope **c = 4 in.**, **d_c = 2 in.**

- **Angle:** L4×3×⅜ × 0'-11½" (11½ in.); 4-in. leg to beam web, 3-in. leg
  (**1¾-in. gage**) to girder web.
- **Bolts:** ¾-in. Group 120 (N), standard holes; 4 per leg, 3 @ 3 in. = 9 in.,
  l_ev = 1¼ in.; l_eh = 1¼ in. on the 3-in. leg, 1½ in. on the 4-in. leg;
  2½-in. dimension at the bottom; ¾-in. setback.
