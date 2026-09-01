<!-- chunk_id: II.A-2B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-2B",
 "example_family": "II.A-2",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.8",
  "J3.11a",
  "J2.4",
  "J4.1",
  "J4.2"
 ],
 "eqs": [
  "J3-2"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Bolted/Welded Double-Angle Connection Under Shear and Axial Tension",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-2B — Bolted/Welded Double-Angle Connection Under Shear and Axial Tension",
 "question": "# II.A-2B — Bolted/Welded Double-Angle Connection, Axial + Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA double-angle connection joins an ASTM A992 W18x50 beam to a support under combined shear and\naxial tension. The angles are fillet-welded to the beam web (supported legs) with 70-ksi (E70)\nelectrodes and bolted to the support through the outstanding legs. Verify the available strength\n(LRFD and ASD). Deformation at the bolt holes at service load is a design consideration. See\nfigures/IIA_2B.png.\n\n## Given\n- Beam: ASTM A992 W18x50 (A_g = 14.7 in.^2, d = 18.0 in., t_w = 0.355 in., b_f = 7.50 in.,\n  t_f = 0.570 in.), F_y = 50 ksi, F_u = 65 ksi; uncoped.\n- Angles: 2L4x3-1/2x1/2 (short legs back-to-back), ASTM A572 Grade 50; length l = 14-1/2 in.;\n  outstanding-leg gage = 5-1/2 in.\n- Bolts (outstanding legs): 7/8-in.-dia. Group 120, condition N, standard holes (d_h = 15/16 in.),\n  A_b = 0.601 in.^2; n = 5 rows, 10 bolts total; s = 3 in., l_ev = 1-1/4 in.\n- Welds (web legs): E70 electrodes; one vertical fillet each side, l = 14-1/2 in., loaded at the\n  resultant angle (beam setback 1/2 in. + 1/4-in. underrun allowance = 3/4 in.).\n- Loads: shear V_u = 75 kips / V_a = 50 kips; axial tension N_u = 60 kips / N_a = 40 kips;\n  resultant R_u = 96.0 kips / R_a = 64.0 kips.\n- Code basis: AISC 360-22; ASCE/SEI 7 load combinations.\n\n## Find\nVerify all governing limit states: bolt shear, bearing, and tearout at the outstanding legs\n(J3.7, J3.11a); bolt shear-tension interaction (J3.8) and prying (Manual Part 9); the web-leg\nweld group (J2.4/Table J2.5, eccentric capacity from Manual Table 8-8) with the required weld\nsize and minimum beam-web thickness; shear yielding/rupture and tensile yielding/rupture of the\nangles (J4.1, J4.2, B4.3b); block shear of the angle outstanding legs and of the beam web (J4.3);\nbeam shear and tensile yielding/rupture (J4.1, J4.2, with the shear-lag factor U from D3/Table\nD3.1 Case 2). Confirm adequacy.",
 "has_figure": true,
 "stem": "II_A_2B",
 "breadcrumb": "EXAMPLE II.A-2B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.8 §J3.11a §J2.4 §J4.1 §J4.2 · Bolted/Welded Double-Angle Connection Under Shear and Axial Tension",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-2B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.8 §J3.11a §J2.4 §J4.1 §J4.2 · Bolted/Welded Double-Angle Connection Under Shear and Axial Tension

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.8 (Eq. J3-2), §J3.11a, §J2.4 (directional factor), §J4.1/§J4.2; prying per Manual Part 9. Per the RAG extract provided.

---

### 1. Required Strengths

Vu = 75 / Va = 50 kips with Nu = 60 / Na = 40 kips → resultant **96.0 / 64.0 kips at 38.7° from vertical.**

2L4x3-1/2x1/2 SLBB × 14 1/2 in. (A572 Gr. 50): web legs welded to the W18x50 web (tw = 0.355 in.) with one vertical E70 fillet per side; outstanding legs bolted with ten 7/8-in. Group 120-N bolts (5 rows @ 3 in., gage 5 1/2 in., lev = 1 1/4 in.).

### 2. Outstanding-Leg Bolts (shear + tension, §J3.7/§J3.8)

Per bolt: shear 7.5/5.0 kips (frv = 12.5/8.32 ksi); tension 6.0/4.0 kips. frv/(φFnv) = 0.31 > 0.30 →

F′nt = 1.3(90) − (90/40.5)(12.5) = **89.3 ksi**; available tension = **40.3 kips (LRFD) / 26.8 kips (ASD)** ≥ demand ✓

**Prying (Part 9, t = 1/2 in.):** b′ = (5.5 − 0.355)/2 − 0.50 − 0.44 = 1.64 in.; a′ = 1.87 in.; ρ = 0.877; p = 2.9 in.; δ = 0.677; tc = 1.25 in. → Q = (0.5/1.25)²(1.677) = 0.270 → available tension incl. prying = **10.9 kips ≥ 6.0 ✓** (ASD 10.9 ≥ 4.0 ✓)

Bearing/tearout on the 1/2-in. legs and the support: not governing relative to per-bolt demands ✓.

### 3. Web-Leg Welds (one vertical fillet per angle, l = 14 1/2 in.)

Per weld line: vertical 37.5/14.5 = 2.59 kip/in.; horizontal (axial share + bending from the 3/4-in. setback/underrun eccentricity) ≈ 3.10 kip/in. → resultant ≈ **4.03 kip/in. at θ ≈ 50°** → directional factor ≈ 1.33.

**Use 3/16-in. fillets (D = 3, also the Table J2.4 minimum for the 0.355-in. web):**
Available = 1.392(3)(1.33) = **5.55 kip/in. ≥ 4.03 ✓** (LRFD); 3.70 ≥ 2.69 ✓ (ASD). The beam web develops the single-sided welds ✓.

### 4. Angle Limit States

Shear yielding 0.6(50)(14.5) = 435 kips ≥ 75 ✓; tension yielding φ = 653 kips ≥ 60 ✓; OSL net shear/tension rupture and block shear — all non-critical at these demands ✓.

### 5. Conclusion

The welded/bolted double-angle connection is **adequate for the combined 75-kip shear and 60-kip tension (LRFD)** and 50/40 kips (ASD). As in the all-bolted version (II.A-1B), the critical behavior is at the **outstanding-leg bolts in combined shear-tension with prying** — the 1/2-in. angles hold the prying reduction to Q = 0.27, leaving an ≈80% margin on the per-bolt tension — while the 3/16-in. web-leg welds work at ~73% with the directional strength increase.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-2B (from figures/IIA_2B.png)

Bolted/welded double-angle connection under shear + axial: 2L4×3½×½ SLBB ×
1'-2½" (l = 14½ in.) on a W18×50 web.

- **Outstanding legs (bolted to support):** ⅞-in. Group 120 (N) standard holes,
  **5 rows**, l_ev = 1¼ in. top/bottom, 4 @ 3 in. = 12 in.; **gage = 5½ in.**;
  10 bolts total. Top horizontal dims 3½ in., 3 in. to first row.
- **Web legs (welded to beam web):** one vertical 3/16-in. fillet weld each side,
  l = 14½ in.; ½-in. setback.
- Loads at the web/weld line: vertical shear **V** and axial **N**, giving the
  inclined resultant noted in the question.
