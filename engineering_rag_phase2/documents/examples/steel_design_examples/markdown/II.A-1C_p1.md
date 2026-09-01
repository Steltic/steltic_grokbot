<!-- chunk_id: II.A-1C_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-1C",
 "example_family": "II.A-1",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "B3.9",
  "J3.7",
  "J3.11",
  "J4.1",
  "J4.3"
 ],
 "eqs": [
  "J3-6b",
  "J3-6d"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Double-Angle Connection: Structural Integrity Check (§B3.9)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-1C — Double-Angle Connection: Structural Integrity Check (§B3.9)",
 "question": "# II.A-1C — All-Bolted Double-Angle Connection, Structural Integrity Check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nThe all-bolted double-angle connection of Example II.A-1B (ASTM A992 W18x50 beam, 2L5x3-1/2x5/8\nASTM A572 Grade 50 angles, five rows of 7/8-in. Group 120 bolts) must additionally satisfy the\nstructural-integrity provisions of AISC 360-22 Section B3.9, which apply when the building code\nrequires design for structural integrity. Evaluate the connection both as a beam/girder end\nconnection (B3.9(b)) and as the end connection of a member bracing a column (B3.9(c)). These\nchecks are made on a nominal-strength basis, independently of the other strength requirements,\nand inelastic deformation of the connection is permitted. See figures/IIA_1C.png.\n\n## Given\n- Beam: ASTM A992 W18x50 (t_w = 0.355 in.), F_y = 50 ksi, F_u = 65 ksi.\n- Angles: 2L5x3-1/2x5/8, ASTM A572 Grade 50, l = 14-1/2 in.; outstanding-leg gage = 7-1/2 in.\n- Bolts: 7/8-in.-dia. Group 120, standard holes (d_h = 15/16 in.), A_b = 0.601 in.^2; n = 5 rows\n  on the web leg (double shear), 10 bolts total to the support; s = 3 in., l_ev = 1-1/4 in.;\n  beam-web horizontal edge distance 1-3/4 in. (use 1-1/2 in. with a 1/4-in. underrun allowance).\n- Required vertical shear (from II.A-1B): V_u = 75 kips (LRFD), V_a = 50 kips (ASD).\n- Code basis: AISC 360-22 Section B3.9.\n\n## Find\nThe minimum required nominal axial tie strength T per B3.9(b), then the controlling nominal\ntensile strength T_n of the connection from all applicable limit states (bolt shear, bolt\ntension, beam-web bearing and tearout using the inelastic-deformation forms J3-6b/J3-6d, bolt\nprying on the outstanding legs, angle tensile yielding and rupture, and beam-web block shear).\nConfirm T_n >= T. Also determine, per B3.9(c), the largest column axial force this connection\ncan brace.",
 "has_figure": true,
 "stem": "II_A_1C",
 "breadcrumb": "EXAMPLE II.A-1C · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 §J4.1 §J4.3 · Double-Angle Connection: Structural Integrity Check (§B3.9)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-1C · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 §J4.1 §J4.3 · Double-Angle Connection: Structural Integrity Check (§B3.9)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §B3.9 (nominal-strength basis, independent of other checks, inelastic deformation permitted), with §J3.7/Table J3.2 (bolt shear/tension), §J3.11 (Eqs. J3-6b/J3-6d — deformation NOT a consideration), §J4.1, §J4.3; prying per Manual Part 9 (nominal). Per the RAG extract provided.

---

### 1. Required Nominal Tie Strength — §B3.9(b)

From Example II.A-1B: Vu = 75 kips / Va = 50 kips.

T = max[(2/3)Vu, Va] = max[50.0, 50.0] = **50.0 kips**

### 2. Nominal Tensile Strength Tn (least of the applicable limit states)

**(a) Bolt shear, web-leg bolts (5, double shear):** Rn = 5(2)(54)(0.601) = **325 kips**

**(b) Bolt tension, OSL bolts (10):** Rn = 10(90)(0.601) = **541 kips**

**(c) Beam-web bearing/tearout (deformation not a consideration):**
tearout toward beam end, lc = 1.50 − (15/16)/2 = 1.03 in.: 1.5lctwFu = 35.7 kips/bolt; bearing 3.0dtwFu = 60.6 kips/bolt → 5(35.7) = **179 kips**

**(d) OSL bolts with prying (nominal):** B = FntAb = 54.1 kips; tc = √(4.44Bb′/(pFu)) = 1.79 in.; Q = (0.625/1.79)²(1.677) = 0.205
Tn = 10(54.1)(0.205) = **111 kips** ← **governs**

**(e) Angle tensile yielding/rupture (Eqs. J4-1/J4-2):** 906 / 772 kips — not governing

**(f) Beam-web block shear (axial pull toward beam end, Ubs = 1.0):** Rn = 0.6FuAnv + FuAnt = 28 + 190 = **219 kips** — not governing

**Controlling Tn = 111 kips ≥ T = 50.0 kips ✓ — §B3.9(b) satisfied** (utilization 0.45)

### 3. Column-Bracing Capacity — §B3.9(c)

Tn ≥ 0.01(2/3)Pu (LRFD) or 0.01Pa (ASD) →

- **LRFD:** Pu,max = 111(150) = **≈16,600 kips**; **ASD:** Pa,max = **≈11,100 kips**

### 4. Conclusion

On the nominal basis of §B3.9, the double-angle connection provides a tie capacity of **111 kips, governed by outstanding-leg bolt tension with prying**, more than twice the required 50-kip integrity tie force. The relaxed bearing/tearout forms (Eqs. J3-6b/d) and permitted inelastic angle deformation make all other limit states non-critical, and the connection can brace columns far heavier than any it would actually support. No design changes are required for structural integrity.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-1C (from figures/IIA_1C.png)

Same connection as II.A-1B (structural-integrity check): 2L5×3½×⅝ SLBB ×
1'-2½" (14½ in.) on a W18×50 web; ⅞-in. Group 120 (N) bolts, standard holes.

- Web leg: one vertical line of **5 bolts**, l_ev = 1¼ in. top/bottom,
  4 @ 3 in. = 12 in.
- Outstanding legs to the support: **gage = 7½ in.**, two bolts per row,
  10 bolts total.
- ½-in. setback; 1¾-in. beam-web edge distance; 2¼ in. and 3½ in. horizontal
  dimensions at the top; 3 in. to first row.
