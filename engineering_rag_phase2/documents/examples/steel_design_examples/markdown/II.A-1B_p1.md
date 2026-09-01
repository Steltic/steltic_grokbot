<!-- chunk_id: II.A-1B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-1B",
 "example_family": "II.A-1",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.8",
  "J3.11a",
  "J4.1",
  "J4.2",
  "J4.3"
 ],
 "eqs": [
  "J3-2",
  "J3-6a"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "All-Bolted Double-Angle Connection Under Shear and Axial Tension",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-1B — All-Bolted Double-Angle Connection Under Shear and Axial Tension",
 "question": "# II.A-1B — All-Bolted Double-Angle Connection, Axial + Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn all-bolted double-angle connection joins the web of an ASTM A992 W18x50 beam to a\nsupport. The beam end delivers both a vertical shear and an axial tension (e.g., a drag/\ncollector force). The angles are shop-bolted to the beam web (one vertical line of bolts\nin double shear) and field-bolted to the support through the outstanding legs (two bolts\nper row, loaded in shear plus tension from the axial force). Verify the available\nstrength of the connection for the combined loading (LRFD and ASD). Deformation at the\nbolt holes at service load is a design consideration. See figures/IIA_1B.png.\n\n## Given\n- Beam: ASTM A992 W18x50 (A_g = 14.7 in.^2, d = 18.0 in., t_w = 0.355 in., t_f = 0.570 in.),\n  F_y = 50 ksi, F_u = 65 ksi; uncoped.\n- Angles: 2L5x3-1/2x5/8 (short legs back-to-back), ASTM A572 Grade 50, F_y = 50 ksi,\n  F_u = 65 ksi; length l = 14-1/2 in.\n- Bolts: 7/8-in.-dia. Group 120 (e.g. A325), condition N, standard holes (d_h = 15/16 in.),\n  A_b = 0.601 in.^2. n = 5 rows; s = 3 in.; l_ev = 1-1/4 in. Web-leg bolts in double shear\n  (5 bolts); outstanding-leg bolts are 10 total (two per row). Outstanding-leg gage = 7-1/2 in.\n  Angle horizontal edge distance (web side) l_eh = 1-1/4 in.; outstanding-leg l_eh = 1-1/16 in.;\n  beam-web horizontal edge distance 1-3/4 in. (use 1-1/2 in. with a 1/4-in. underrun allowance).\n- Loads (factored / service): shear V_u = 75 kips / V_a = 50 kips; axial tension N_u = 60 kips /\n  N_a = 40 kips.\n- Code basis: AISC 360-22; ASCE/SEI 7 load combinations.\n\n## Find\nVerify all governing limit states for the combined shear + axial tension: bolt shear and\nbearing/tearout at the angles and beam web with the inclined resultant (J3.7, J3.11a);\nbolt shear-tension interaction on the outstanding legs (J3.8, Eq. J3-2/J3-3a/J3-3b);\nprying action on the outstanding legs (Manual Part 9); shear yielding/rupture and tensile\nyielding/rupture of the angles and beam (J4.1, J4.2, B4.3b, D3); and block shear rupture\nof the angles (for shear, and for axial in L- and U-shapes) and beam web (J4.3), including\nthe shear-axial interaction. Confirm the connection is adequate.",
 "has_figure": true,
 "stem": "II_A_1B",
 "breadcrumb": "EXAMPLE II.A-1B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.8 §J3.11a §J4.1 §J4.2 §J4.3 · All-Bolted Double-Angle Connection Under Shear and Axial Tension",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-1B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.8 §J3.11a §J4.1 §J4.2 §J4.3 · All-Bolted Double-Angle Connection Under Shear and Axial Tension

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.8 (Eq. J3-2), §J3.11a (Eqs. J3-6a/c), §J4.1/§J4.2/§J4.3; prying per AISC Manual Part 9. Per the RAG extract provided.

---

### 1. Required Strengths

Vu = 75 kips / Va = 50 kips with Nu = 60 kips / Na = 40 kips → resultant **96.0 / 64.0 kips**.

2L5x3-1/2x5/8 SLBB × 14 1/2 in. (A572 Gr. 50); five rows of 7/8-in. Group 120-N bolts @ 3 in. through the W18x50 web (double shear); ten OSL bolts to the support (gage 7 1/2 in.); lev = 1 1/4 in.; beam-web end distance 1 1/2 in. (with underrun). Effective hole = 1.00 in.

### 2. Web-Leg Bolts (5, double shear)

Per-bolt resultant = 96.0/5 = **19.2 kips** ≤ φrn = 0.75(54)(0.601)(2) = 48.7 kips ✓ (ASD 12.8 ≤ 32.5 ✓)
Beam-web bearing: φ = 36.4 kips/bolt ✓; tearout toward the beam end (lc = 1.03 in.): φ = 21.4 kips ≥ 19.2 ✓ (the controlling fastener check).

### 3. Outstanding-Leg Bolts (10, shear + tension)

Per bolt: shear 7.5/5.0 kips (frv = 12.5/8.32 ksi); tension 6.0/4.0 kips. frv/(φFnv) = 0.31 > 0.30 → §J3.8:

F′nt = 1.3(90) − (90/40.5)(12.5) = **89.3 ksi** → available tension φF′ntAb = **40.3 kips** (LRFD) / 26.8 kips (ASD)

**Prying (Manual Part 9):** b′ = (7.5 − 0.355)/2 − 0.625 − 0.44 = 2.51 in.; a′ = 1.86 in.; ρ = 1.35; p = 2.9 in.; δ = 0.677; tc = 1.54 in. → Q = (0.625/1.54)²(1.677) = 0.275 → available tension incl. prying = 40.3(0.275) = **11.1 kips ≥ 6.0 ✓** (ASD 11.1 ≥ 4.0 ✓)

### 4. Angle and Web Limit States

- Angles, shear yielding/rupture (Eqs. J4-3/J4-4): 544 / 463 kips nominal → far above 75 kips ✓
- Angles, tension yielding/rupture (Eqs. J4-1/J4-2): φ = 816 / 579 kips ≥ 60 ✓
- Angles, block shear (Eq. J4-5, vertical): φRn = 366 kips ✓
- Beam-web block shear toward the beam end (axial direction, Ubs = 1.0): φRn ≈ 164 kips ≥ 60 ✓; web tension/shear at the connection non-critical for the W18x50 ✓

### 5. Conclusion

The all-bolted double-angle connection is **adequate for the combined 75-kip shear and 60-kip axial tension (LRFD)** and 50/40 kips (ASD). The governing checks are the outstanding-leg bolts in combined shear-plus-tension with prying (per-bolt tension capacity 11.1 vs. 6.0 kips demand) and beam-web tearout at the web bolts (21.4 vs. 19.2 kips). The thick 5/8-in. angles keep prying losses acceptable; thinner angles would not satisfy the tension demand.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-1B (from figures/IIA_1B.png)

All-bolted double-angle connection: 2L5×3½×⅝ SLBB × 1'-2½" (l = 14½ in.) on the
web of a W18×50 beam; ⅞-in. Group 120 (N) bolts in standard holes.

- **Web leg (shop-bolted to beam web):** one vertical line of **5 bolts**,
  l_ev = 1¼ in. top and bottom, 4 @ 3 in. = 12 in. between (Bolt 1 = top,
  Bolt 2 = bottom). These bolts are in double shear.
- **Outstanding legs (field-bolted to support):** **two bolts per row → 10 total**,
  on a **gage = 7½ in.** (see Section A-A, the two angle legs straddling the
  support with the 7½-in. gage between the two vertical bolt lines).
- Horizontal dimensions at the beam end: 2¼ in., 3½ in., 1¼ in. across the top;
  ½-in. beam setback; 1¾ in. beam-web horizontal edge distance; 3 in. from top
  to first bolt row.
- Loads applied at the web bolt line: vertical shear **V** and axial **N**
  (drag/collector), giving an inclined resultant.
