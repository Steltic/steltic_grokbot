<!-- chunk_id: II.A-8_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-8",
 "example_family": "II.A-8",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Double-Angle Connections, Beams Two Sides of a Girder Web",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-8 — Double-Angle Connections, Beams Two Sides of a Girder Web",
 "question": "# II.A-8 — All-Bolted Double-Angle Connections (Beams-to-Girder Web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nTwo beams frame into opposite sides of the web of an ASTM A992/A992M W30×99 girder\nusing all-bolted double-angle connections (see figures/IIA_8.png). Beam A is an\nASTM A992/A992M W12×40; Beam B is an ASTM A992/A992M W21×50. Both beams are coped at\nthe top flange only (cope d_c = 2 in. deep, c = 5 in. long; ½-in. setback, so the\neccentricity e = 5.50 in.). All connection angles are ASTM A572/A572M Grade 50\n2L5×3½×¼ (short legs back-to-back), bolted with ¾-in.-diameter Group 120 bolts,\nthread condition N, in standard holes at 3-in. vertical spacing. Beam A uses 2 rows\nof bolts (angles 5½ in. long); Beam B uses 5 rows of bolts (angles 14½ in. long).\nVertical edge distance on the beam web l_ev = 2 in.; angle l_ev = 1¼ in.;\nl_eh = 1⅝ in. The four girder-web bolts shared between the two beam reactions carry\nload from both connections.\n\nService end reactions: Beam A — R_D = 4.17 kips, R_L = 12.5 kips. Beam B —\nR_D = 18.3 kips, R_L = 55 kips.\n\nVerify each connection (angles, beam-web bolt-hole shear transfer, coped-beam web\nlimit states) and the shared girder-web bolts for the LRFD and ASD demands.\n\n## Given\n- Material: beams and girder ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); angles\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n- Beam A: W12×40, d = 11.9 in., t_w = 0.295 in. Beam B: W21×50, d = 20.8 in.,\n  t_w = 0.380 in. Girder: W30×99, web t_w = 0.520 in.\n- Bolts: ¾-in.-dia. Group 120, cond. N, standard holes (d_h = 13/16 in.,\n  A_b = 0.442 in.²); double shear through the two angle legs.\n- Cope (both beams): d_c = 2.00 in., c = 5 in., e = 5.50 in.\n- Loads: Beam A R_D = 4.17, R_L = 12.5 kips; Beam B R_D = 18.3, R_L = 55 kips.\n- Code basis: AISC 360-22 (Chapter J); loads per ASCE/SEI 7.\n\n## Find\nFor each beam: the available strength of the angles (J4.2/J4.3), the effective\nshear-transfer strength at the beam-web bolt holes (J3.7 + J3.11a), and the\ncoped-beam web strength (block shear J4.3 and flexural local web buckling). For the\ngirder, verify the shared bolts (bolt shear J3.7 and bearing/tearout J3.11a on the\ngirder web). Confirm adequacy and identify the governing limit state for each beam.",
 "has_figure": true,
 "stem": "II_A_8",
 "breadcrumb": "EXAMPLE II.A-8 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · Double-Angle Connections, Beams Two Sides of a Girder Web",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-8 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · Double-Angle Connections, Beams Two Sides of a Girder Web

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2/§J4.3; coped-section checks per Manual Part 9. Per the RAG extract provided.

---

### 1. Required Strengths

- **Beam A (W12x40, tw = 0.295 in.):** Ru = 1.2(4.17) + 1.6(12.5) = **25.0 kips**; Ra = **16.7 kips**
- **Beam B (W21x50, tw = 0.380 in.):** Ru = 1.2(18.3) + 1.6(55) = **110 kips**; Ra = **73.3 kips**

Both coped 2 × 5 in. (e = 5.50 in.); angles 2L5x3-1/2x1/4 (A572 Gr. 50): A — 2 rows (5 1/2 in.); B — 5 rows (14 1/2 in.); 3/4-in. Group 120-N bolts @ 3 in.; girder W30x99 (tw = 0.520 in.), four web bolts shared by both connections.

### 2. Beam A Connection (25.0 / 16.7 kips)

Web bolts (2, double shear): per-bolt min[35.8; web bearing 25.9; angle tearout 24.7] → group **50.6 kips (LRFD) / 33.7 (ASD) ✓**. Angles: shear yield 82.5 kips, rupture φ54.8 ✓. Coped web: block shear φ48.9 ≥ 25.0 ✓; cope flexure Mu = 138 kip-in. ≪ φMn ≈ 405 ✓.

### 3. Beam B Connection (110 / 73.3 kips)

Web bolts (5, double shear): per-bolt min[35.8; web bearing 33.3; bottom angle tearout 24.7] → group **4(33.3) + 24.7 = 158 kips / 105 kips ✓**. Angles: shear yield 218 kips; rupture φ148; block shear φ ≈ 120 — all ✓. Coped web: block shear φRn = **134 kips ≥ 110 ✓** (governing for Beam B, 82%); cope flexure Mu = 605 kip-in. ≤ φMn ≈ 945 ✓ (buckling non-critical, c/ho ≈ 0.27).

### 4. Shared Girder-Web Bolts

Each shared bolt is in double shear with unequal plane forces: Beam A side ≈ 6.3 kips/plane, Beam B side ≈ 11.0 kips/plane (LRFD):

- Shear per plane: 11.0 ≤ φrn = 17.9 kips ✓ (ASD 7.3 ≤ 11.9 ✓)
- Bearing on the 0.520-in. girder web (sum of both planes): 6.3 + 11.0 = 17.3 kips ≤ φ(2.4dtFu) = 45.6 kips ✓ (ASD 11.5 ≤ 30.4 ✓)

### 5. Conclusion

Both connections and the shared fasteners are **adequate**: Beam A works with ≥50% reserve throughout; Beam B is governed by **block shear of its coped web at ~82% utilization (LRFD)**; and the four shared girder-web bolts comfortably carry the simultaneous, unequal plane forces from the two reactions, with girder-web bearing summing both. The detail satisfies AISC 360-22 Chapter J and Manual Part 9/10 practice for back-to-back framing.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-8 (from figures/IIA_8.png)

Supplements the question text with information that is only in the figure (the text
describes the two opposed beam connections and the four shared girder-web bolts, but
omits the horizontal bolt gage on the girder web):

- **Girder-web bolt gage = 6¼ in.** (horizontal spacing between the two vertical bolt
  lines passing through the W30×99 web; the two beams' angles share these bolts).
- Section dimensions across the girder web: outer faces at ~2⅞ in. and 2½ in. as
  dimensioned, consistent with the 6¼-in. gage and entering/tightening clearances
  per AISC Manual Table 7-15.
- Cope (both beams, top flange only): d_c = 2 in., c = 5 in., ½-in. setback
  (e = 5.50 in.); beam-web vertical edge distance l_ev = 2 in.; angle l_ev = 1¼ in.,
  l_eh = 1⅝ in.
- Both connections use 2L5×3½×¼ (SLBB): Beam A 2 rows (angle 5½ in.), Beam B 5 rows
  (angle 14½ in.), ¾-in. Group 120 (N) bolts at s = 3 in.
