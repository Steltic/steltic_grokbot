<!-- chunk_id: II.A-3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-3",
 "example_family": "II.A-3",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J2.2b",
  "J2.4",
  "J4.2"
 ],
 "eqs": [],
 "tables": [
  "J2.4",
  "J2.5",
  "10"
 ],
 "title": "All-Welded Double-Angle Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-3 — All-Welded Double-Angle Connection (Beam to Column Flange)",
 "question": "# II.A-3 — All-Welded Double-Angle Shear Connection  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported floor beam frames into the flange of a column with an all-welded\ndouble-angle shear connection. A pair of angles is fillet-welded to the beam web on\none set of legs (\"Welds A\") and to the column flange on the other set of legs\n(\"Welds B\"), using 70-ksi (E70) electrodes. Each vertical weld line is l = 24 in. long.\nThe web-side welds are 3/16-in. fillets and the support-side welds are 1/4-in. fillets.\n\nVerify (LRFD and ASD) that the connection provides adequate available shear strength\nfor the given beam end reaction, and confirm the chosen weld sizes and angle thickness\nsatisfy the AISC 360-22 weld-size limitations.\n\n## Given\n- Members: beam ASTM A992 W36x231 (web t_w = 0.760 in.); column ASTM A992 W14x90\n  (flange t_f = 0.710 in.). F_y = 50 ksi, F_u = 65 ksi.\n- Connection angles: 2L4x3-1/2x5/16 (short legs back-to-back), ASTM A572 Grade 50,\n  F_y = 50 ksi, F_u = 65 ksi; weld length per line l = 24 in.\n- Welds: E70 electrodes (F_EXX = 70 ksi). Welds A (beam web to angles) = 3/16-in.\n  fillets; Welds B (column flange to angles) = 1/4-in. fillets. Both weld groups are\n  loaded eccentrically (the beam reaction acts at an eccentricity from the weld line).\n- Loads (service): dead-load reaction R_D = 37.5 kips; live-load reaction R_L = 113 kips.\n- Code basis: AISC 360-22; load combinations per ASCE/SEI 7. The available strengths of\n  the two eccentric fillet-weld groups are obtained from AISC Manual Table 10-3\n  (instantaneous-center method): Welds A -> phi R_n = 257 kips (LRFD) / 171 kips (ASD);\n  Welds B -> phi R_n = 260 kips (LRFD) / 173 kips (ASD).\n\n## Find\nThe available shear strength of the connection: check the two fillet-weld groups\n(weld-metal strength grounded in AISC 360-22 J2.4 / Table J2.5, eccentric-group capacity\nfrom Manual Table 10-3), the minimum and maximum permitted fillet-weld sizes and the\nrequired minimum angle thickness (J2.2b, Table J2.4), the minimum base-metal thicknesses,\nand shear yielding / shear rupture of the angles (J4.2). Identify the governing limit\nstate and confirm adequacy.",
 "has_figure": false,
 "stem": "II_A_3",
 "breadcrumb": "EXAMPLE II.A-3 · AISC 360-22 II.A (simple / shear connection) · §J2.2b §J2.4 §J4.2 · All-Welded Double-Angle Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-3 · AISC 360-22 II.A (simple / shear connection) · §J2.2b §J2.4 §J4.2 · All-Welded Double-Angle Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2.2b/Table J2.4 (weld size limits), §J2.4/Table J2.5 (eccentric fillet-weld groups — Manual Table 10-3 IC coefficients), §J4.2. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 37.5 kips, L = 113 kips → **LRFD Ru = 226 kips; ASD Ra = 151 kips**

2L4x3-1/2x5/16 SLBB × 24 in. (A572 Gr. 50); E70 electrodes: Welds A (angles to W36x231 web, tw = 0.760 in.) = 3/16-in. fillets; Welds B (angles to W14x90 column flange, tf = 0.710 in.) = 1/4-in. fillets. Both groups eccentrically loaded.

### 2. Eccentric Weld Groups (Manual Table 10-3, IC method)

- **Welds A (3/16 in., l = 24 in.):** φRn = **257 kips ≥ 226 ✓**; Rn/Ω = **171 kips ≥ 151 ✓** (88% utilized — **governing**)
- **Welds B (1/4 in., l = 24 in.):** φRn = **260 kips ≥ 226 ✓**; Rn/Ω = **173 kips ≥ 151 ✓**

### 3. Weld Size Limitations (§J2.2b / Table J2.4)

- Maximum along the 5/16-in. angle edges: t − 1/16 = 1/4 in. → Welds B = 1/4 ✓; Welds A = 3/16 ✓
- Minimum (thinner part = 5/16-in. angle): 3/16 in. → both ✓
- Base metal: beam web with welds both sides: tw,min = 6.19D/Fu = 6.19(3)/65 = 0.29 in. ≤ 0.760 ✓; column flange (one-sided per angle): 3.09(4)/65 = 0.19 in. ≤ 0.710 ✓

### 4. Angle Limit States

Shear yielding (Eq. J4-3): 0.6(50)(2 × 24 × 0.3125) = 450 kips → **450 / 300 kips** ≥ 226/151 ✓ (no holes — rupture and block shear not applicable to the welded legs).

### 5. Conclusion

The all-welded double-angle connection is **adequate** for the 226-kip (LRFD) / 151-kip (ASD) reaction: Welds A govern at 88% utilization (257/171 kips available per Table 10-3), Welds B at 87%, and the angles and base metal satisfy every Chapter J size and strength limitation. The 3/16-in. and 1/4-in. weld sizes are at the maximum permitted along the 5/16-in. angle edges, so any higher reaction requires thicker angles.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
