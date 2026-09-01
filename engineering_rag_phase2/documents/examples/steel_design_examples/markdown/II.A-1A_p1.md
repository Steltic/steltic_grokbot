<!-- chunk_id: II.A-1A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-1A",
 "example_family": "II.A-1",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3"
 ],
 "eqs": [
  "J3-6a",
  "J4-3",
  "J4-4",
  "J4-5"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "All-Bolted Double-Angle Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-1A — All-Bolted Double-Angle Connection (Beam to Column Flange)",
 "question": "# II.A-1A — All-Bolted Double-Angle Shear Connection  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported floor beam frames into the flange of a column with an all-bolted\ndouble-angle shear connection. The pair of angles is bolted to the beam web on one\nleg and to the column flange on the other leg, using 3/4-in.-diameter Group 120\n(e.g., ASTM F3125 Grade A325) high-strength bolts in standard holes, installed snug-\ntight, with the threads not excluded from the shear plane (condition N). Deformation\nat the bolt holes at service load is a design consideration.\n\nVerify that the connection has adequate available shear strength (both LRFD and ASD)\nfor the given beam end reaction.\n\n## Given\n- Members: beam ASTM A992 W36x231 (web thickness t_w = 0.760 in.); column ASTM A992\n  W14x90 (flange thickness t_f = 0.710 in.). F_y = 50 ksi, F_u = 65 ksi.\n- Connection angles: 2L5x3-1/2x5/16 (short legs back-to-back), ASTM A572 Grade 50,\n  F_y = 50 ksi, F_u = 65 ksi. Each angle length L = 23-1/2 in.\n- Fasteners: one vertical line of 8 bolts per angle leg (n = 8 rows), 3/4-in.-dia.\n  Group 120, condition N, standard holes (d_h = 13/16 in.). Bolts through the beam web\n  are in double shear; at the column flange there are two bolts per row.\n- Bolt layout: row spacing s = 3 in.; vertical edge distance l_ev = 1-1/4 in.;\n  horizontal edge distance on the angle leg at the beam-web side l_eh = 1-3/8 in., and\n  at the column-flange side 1-1/2 in.\n- Beam is uncoped.\n- Loads (service): dead-load reaction R_D = 37.5 kips; live-load reaction R_L = 113 kips.\n- Code basis: AISC 360-22; load combinations per ASCE/SEI 7.\n\n## Find\nThe available shear strength of the connection, checking the governing limit states:\nshear yielding, shear rupture, and block shear rupture of the angles; and the shear\ntransfer strength at the bolt holes (bolt shear together with bearing/tearout of the\nangles, beam web, and column flange). Confirm the connection is adequate for the\nrequired reaction.",
 "has_figure": false,
 "stem": "II_A_1A",
 "breadcrumb": "EXAMPLE II.A-1A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Double-Angle Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-1A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Double-Angle Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2 (bolt shear), §J3.11a (Eqs. J3-6a/c, deformation considered), §J4.2 (Eqs. J4-3/J4-4), §J4.3 (Eq. J4-5). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 37.5 kips, L = 113 kips → **LRFD Ru = 1.2(37.5) + 1.6(113) = 226 kips; ASD Ra = 151 kips**

2L5x3-1/2x5/16 SLBB × 23 1/2 in. (A572 Gr. 50); 8 rows @ 3 in.; lev = 1 1/4 in.; leh = 1 3/8 in. (web side) / 1 1/2 in. (support side); 3/4-in. Group 120-N bolts, standard holes (effective hole = 7/8 in.). Beam W36x231 (tw = 0.760 in.), uncoped; column flange tf = 0.710 in.

### 2. Bolt Group — Beam-Web Side (8 bolts, double shear)

Bolt shear: φrn = 0.75(54)(0.442)(2) = 35.8 kips/bolt; rn/Ω = 23.9 kips.
Bearing: beam web φ = 66.7 kips/bolt; angle pair (Σt = 0.625 in.) φ = 54.8 kips/bolt — not governing.
Bottom-bolt tearout on the angles (lc = 0.844 in.): φ = 30.8 kips ← controls that bolt.

**Group: LRFD 30.8 + 7(35.8) = 281 kips; ASD 20.6 + 7(23.9) = 188 kips** ≥ 226/151 ✓

### 3. Bolt Group — Support Side (16 bolts, single shear)

Bolt shear φrn = 17.9 kips; angle bearing φ = 27.4 kips/bolt; bottom-bolt tearout φ = 15.4 kips (controls 2 bolts). Column flange not critical.

**Group: LRFD 2(15.4) + 14(17.9) = 281 kips; ASD 188 kips** ≥ 226/151 ✓

### 4. Angle Limit States (pair)

| Limit state | Rn | LRFD avail. | ASD avail. |
|---|---|---|---|
| Shear yielding (Eq. J4-3) | 0.6(50)(14.7) = 441 | 441 | 294 |
| Shear rupture (Eq. J4-4, Anv = 10.3 in.²) | 402 | 302 | 201 |
| Block shear (Eq. J4-5, Ubs = 1.0) | 420 (≤ 455) | 315 | 210 |

All comfortably exceed the demand. Beam-web limit states (uncoped, tw = 0.760 in.) are non-critical by inspection.

### 5. Conclusion

The all-bolted double-angle connection (8 rows of 3/4-in. Group 120-N bolts; 2L5x3-1/2x5/16 × 23 1/2 in.) is **adequate** for the 226-kip (LRFD) / 151-kip (ASD) reaction. The governing elements are the bolt groups on both sides, each providing 281 kips (LRFD) / 188 kips (ASD) — about 80% utilized — with the bottom-bolt tearout (1 1/4-in. edge distance) limiting one fastener per group. All Chapter J angle limit states have substantial reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
