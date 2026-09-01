<!-- chunk_id: II.A-5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-5",
 "example_family": "II.A-5",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J2.2b",
  "J2.4",
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3"
 ],
 "eqs": [],
 "tables": [
  "J2.4",
  "J2.5",
  "10"
 ],
 "title": "Welded/Bolted Double-Angle Connection (Coped Beam to Girder Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-5 — Welded/Bolted Double-Angle Connection (Coped Beam to Girder Web)",
 "question": "# II.A-5 — Welded/Bolted Double-Angle Connection in a Coped Beam  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992 W18x50 beam, coped at the top flange, frames into the web of an ASTM A992\nW21x62 girder with a double-angle shear connection. The angles are fillet-welded to the\nbeam web (Welds A, 70-ksi electrodes) and bolted to the girder web. Verify the available\nshear strength of the connection (LRFD and ASD). Deformation at the bolt holes at service\nload is a design consideration. See figures/IIA_5.png.\n\n## Given\n- Beam: ASTM A992 W18x50 (d = 18.0 in., t_w = 0.355 in.); coped at the top flange,\n  cope depth d_c = 2 in., cope length c = 8-1/2 in. F_y = 50 ksi, F_u = 65 ksi.\n- Girder: ASTM A992 W21x62 (web t_w = 0.400 in.).\n- Angles: 2L4x3-1/2x1/4 (short legs back-to-back), ASTM A572 Grade 50; length l = 8-1/2 in.\n- Welds (beam web, Welds A): 3/16-in. fillets, l = 8-1/2 in. (E70).\n- Bolts (girder web): 3/4-in.-dia. Group 120, condition N, standard holes (d_h = 13/16 in.);\n  n = 3 rows in two vertical lines (6 bolts), s = 3 in., l_ev = 1-1/4 in.\n- Loads (service): R_D = 10 kips, R_L = 30 kips.\n- Code basis: AISC 360-22; ASCE/SEI 7 load combinations.\n\n## Find\nVerify the connection: the web-leg weld group (J2.4/Table J2.5; eccentric capacity from\nManual Table 10-2) and minimum beam-web thickness; minimum angle thickness for the weld\n(J2.2b); shear yielding/rupture and block shear of the angles (J4.2, J4.3); shear transfer\nstrength at the girder-web bolt holes (J3.7 + J3.11a); and the beam-web limit states at the\ncope — block shear (J4.3) and shear yielding (J4.2 with A_gv = (d - d_c)t_w), noting that\nflexural local-web buckling of the coped section is a separate AISC Manual Part 9 check.\nIdentify the governing limit state.",
 "has_figure": true,
 "stem": "II_A_5",
 "breadcrumb": "EXAMPLE II.A-5 · AISC 360-22 II.A (simple / shear connection) · §J2.2b §J2.4 §J3.7 §J3.11a §J4.2 §J4.3 · Welded/Bolted Double-Angle Connection (Coped Beam to Girder Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-5 · AISC 360-22 II.A (simple / shear connection) · §J2.2b §J2.4 §J3.7 §J3.11a §J4.2 §J4.3 · Welded/Bolted Double-Angle Connection (Coped Beam to Girder Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2.2b/Table J2.4, §J2.4/Table J2.5 (Welds A capacity per Manual Table 10-2), §J3.7/§J3.11a, §J4.2/§J4.3; coped-section checks per Manual Part 9. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 10 kips, L = 30 kips → **LRFD Ru = 60.0 kips; ASD Ra = 40.0 kips**

2L4x3-1/2x1/4 SLBB × 8 1/2 in. (A572 Gr. 50): web legs **welded** to the W18x50 web (Welds A, 3/16-in. E70, l = 8 1/2 in.); outstanding legs **bolted** to the W21x62 girder web with six 3/4-in. Group 120-N bolts (3 rows × 2, s = 3 in., lev = 1 1/4 in.). Beam coped 2 in. × 8 1/2 in. (e = 9.0 in.).

### 2. Welds A (Manual Table 10-2 IC values)

For l = 8 1/2 in., 3/16-in. welds: **φRn = 76.7 kips ≥ 60.0 ✓; Rn/Ω = 51.1 kips ≥ 40.0 ✓** (78% utilized — **governing**)

Supporting checks: minimum beam-web thickness for the two-sided Welds A = 6.19D/Fu = 6.19(3)/65 = 0.29 in. ≤ 0.355 ✓; minimum angle thickness = weld size + 1/16 = 1/4 in. = provided ✓ (§J2.2b).

### 3. Girder-Side Bolt Group (6 bolts, single shear)

Per bolt: min[17.9 bolt shear; 21.9 angle bearing; 12.3 bottom-bolt tearout] →
**LRFD 4(17.9) + 2(12.3) = 96.2 kips ✓; ASD 64.2 kips ✓**. Girder web bearing not critical.

### 4. Angle Limit States (pair)

Shear yielding 128 kips → 128/85.0 ✓; shear rupture (bolted legs) φRn = 85.9/57.3 ✓; block shear φRn = 93.8/62.6 ✓.

### 5. Coped-Beam Limit States (cope 2 in. × 8 1/2 in.)

No bolts in the beam web (welded) → web block shear is not a limit state. Flexure at the long cope (e = 9.0 in.): Mu = 540 kip-in.; with Snet ≈ 23.4 in.³ and the Part 9 buckling adjustment for c/d = 0.47, φMn ≈ 740 kip-in. ≥ 540 ✓ (ASD ≈ 492 ≥ 360 ✓). Web shear through the reduced depth: 170 kips ✓.

### 6. Conclusion

The welded/bolted double-angle connection is **adequate** for 60.0 kips (LRFD) / 40.0 kips (ASD), governed by the **Welds A eccentric weld group (76.7/51.1 kips, ~78% utilized)**, with the long 8 1/2-in. cope's flexural check next at ~73%. Replacing web bolts with Welds A removes the beam-web block-shear limit that governed the all-bolted version (Example II.A-4) but lengthens the cope, shifting attention to coped-section flexure — a classic trade-off in this detail.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-5 (from figures/IIA_5.png)

Supplements the question text with information that is only in the figure, and
corrects an apparent conflict:

- **Cope length c = 4 in.** The figure dimensions the top-flange cope as
  c = 4 in. with cope depth d_c = 2.00 in.
  NOTE: the question's "## Given" lists "cope length c = 8-1/2 in.", which appears
  to be a transcription error — 8½ in. is the angle / connection length l, not the
  cope length. Use **c = 4 in.** for the coped-beam-web checks (block shear and
  shear yielding), with A_gv = (d − d_c)·t_w.
- Beam-web (Welds A) vertical layout: 1¼ in. top, 2 @ 3 in. = 6 in., 1¼ in. bottom
  (angle length l = 8½ in.); beam-web vertical edge distance at the cope
  l_ev = 1⅝ in.
- Girder-web bolts: ¾-in. Group 120 (N), std. holes, two vertical lines of three
  (6 bolts), s = 3 in., l_ev = 1¼ in.; ½-in. beam setback.
