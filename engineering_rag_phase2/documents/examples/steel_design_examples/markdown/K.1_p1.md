<!-- chunk_id: K.1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.1",
 "example_family": "K.1",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "J2",
  "J2.1a",
  "K"
 ],
 "eqs": [],
 "tables": [],
 "title": "Wide-Tee Shear Connection to an HSS Column Face",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.1 — Wide-Tee Shear Connection to an HSS Column Face",
 "question": "# K.1 — Welded/Bolted Wide-Tee Connection to an HSS Column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simple (shear-only) beam-to-column connection is made with a structural tee that\nis bolted to the supported beam web and welded to the face of a square HSS column.\nThe supported beam is an ASTM A992/A992M W16×50. The column is an ASTM A500/A500M\nGrade C HSS8×8×1/4. The connecting tee is an ASTM A992/A992M WT5×24.5, chosen with a\nflange wide enough (b_f = 10.0 in. > B = 8.00 in.) that flare-bevel-groove welds can be\nplaced on both sides of the column face while the tee stem stays centered on the beam.\n\nThe tee stem is bolted to the beam web with one vertical line of four 3/4-in.-diameter\nGroup 120 bolts (thread condition N) in standard holes, spaced s = 3 in., with a\nvertical edge distance l_ev = 1-1/4 in. and a horizontal edge distance l_eh ≈ 2 in.\nThe bolt line is offset e = 3 in. from the column face (the eccentricity for the bolt\ngroup and the tee stem). The tee is l = 11.5 in. long. Use 70-ksi (E70XX) electrodes.\nTreat the support as flexible (the bolt group and welds carry the full beam reaction\nacting at their own centroid).\n\nDetermine whether the connection is adequate for the following service vertical shear\n(beam end reaction), and identify the governing limit state:\n\n  Dead load   P_D = 6.2 kips\n  Live load   P_L = 18.5 kips\n\n## Given\n- Materials: beam and tee ASTM A992 (F_y = 50 ksi, F_u = 65 ksi); column ASTM A500\n  Grade C (F_y = 50 ksi, F_u = 62 ksi). Electrodes E70XX (F_EXX = 70 ksi).\n- Beam W16×50: t_w = 0.380 in., d = 16.3 in., t_f = 0.630 in., T = 13-5/8 in.\n- Tee WT5×24.5: stem t_sw = 0.340 in., d = 4.99 in., flange t_f = 0.560 in.,\n  b_f = 10.0 in., k_1 = 13/16 in.\n- Column HSS8×8×1/4: design wall t = 0.233 in., B = 8.00 in.\n- Bolts: four 3/4-in. Group 120 (N), standard holes (d_h = 13/16 in.), s = 3 in.,\n  l_ev = 1-1/4 in., l_eh ≈ 2 in.; bolt-line eccentricity e = 3 in.\n- Tee length l = 11.5 in. Flexible (simple) support assumption.\n- Loads: P_D = 6.2 kips, P_L = 18.5 kips (vertical shear).\n- Code basis: AISC 360-22 (Chapters J and F); ASCE/SEI 7 load combinations.\n\n## Find\nVerify the connection: confirm the bolt group, the tee-stem limit states (shear\nyielding, shear rupture, block shear rupture, flexure), and the flare-bevel-groove\nweld to the HSS, together with the HSS wall adequacy at the weld. State the governing\navailable strength and compare it to the required strength (LRFD and ASD).",
 "has_figure": false,
 "stem": "K_1",
 "breadcrumb": "EXAMPLE K.1 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2 §J2.1a §K · Wide-Tee Shear Connection to an HSS Column Face",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.1 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2 §J2.1a §K · Wide-Tee Shear Connection to an HSS Column Face

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/§J3.11a, §J4.2/§J4.3, §J2 (flare-bevel-groove welds at the HSS corners), Chapter K HSS wall checks. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6.2 kips, L = 18.5 kips → **LRFD Ru = 37.0 kips; ASD Ra = 24.7 kips**

WT5x24.5 (A992; ts = 0.350 in., l = 11 1/2 in., bf = 10.0 in. > B = 8.00 in.) welded to the HSS8x8x1/4 (t = 0.233 in.) with flare-bevel-groove welds at the two column corners; four 3/4-in. Group 120-N bolts @ 3 in. to the W16x50 web; bolt-line eccentricity e = 3 in. (flexible support — the connection carries R at e).

### 2. Stem Bolt Group (4 bolts, e = 3.0 in.)

C ≈ 2.81 → φRn = 2.81(17.9) = **50.3 kips ≥ 37.0 ✓**; Rn/Ω = **33.4 kips ≥ 24.7 ✓** (**governing**, 74%)
Stem bearing (0.350 in.) and beam-web bearing (0.380 in.): not controlling; bottom-bolt stem tearout φ = 17.2 — interchangeable within the group ✓.

### 3. Tee Stem and Flange

Stem shear yielding 0.6(50)(4.03) = 121 kips ✓; shear rupture φ = 81.9 ✓; block shear ✓; stem flexure at e = 3 in. (Mu = 111 kip-in. ≤ φMn = 521) ✓. The wide flange spans the full HSS face, delivering the load to the stiff corners.

### 4. Welds and HSS Wall

Flare-bevel-groove welds at both corners, effective throat per §J2.1a, total length 2 × 11.5 in.: available strength ≥ 2(11.5)(0.75 × 0.6 × 70 × 0.20) ≈ 145 kips ≥ 37.0 ✓. Because the welds land at the **corners** of the HSS — the stiffest part of the wall — wall plastification of the 1/4-in. face is not a governing limit state, and the wall develops the weld locally (3.09D/Fu basis satisfied) ✓.

### 5. Conclusion

The wide-tee detail is **adequate** for 37.0 kips (LRFD) / 24.7 kips (ASD), governed by the eccentric stem bolt group at ~74% utilization. Placing the 10-in. tee flange across the 8-in. column face moves the welds to the HSS corners, sidestepping face-plastification limits — the defining advantage of this configuration (compare the narrow-tee variant of Example K.2).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
