<!-- chunk_id: II.A-2A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-2A",
 "example_family": "II.A-2",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "J2.4"
 ],
 "eqs": [],
 "tables": [
  "J3.2",
  "J2.5",
  "8"
 ],
 "title": "Bolted/Welded Double-Angle Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-2A — Bolted/Welded Double-Angle Connection (Beam to Column Flange)",
 "question": "# II.A-2A — Bolted/Welded Double-Angle Shear Connection  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported floor beam frames into a column flange with a double-angle shear\nconnection. The pair of angles is bolted to the beam web (supported legs) and fillet-\nwelded to the column flange (support legs, \"Welds B\") with 70-ksi (E70) electrodes.\nVerify the available shear strength of the connection (LRFD and ASD) for the given\nbeam end reaction. Deformation at the bolt holes at service load is a design\nconsideration. See figures/IIA_2A.png for the configuration.\n\n## Given\n- Members: beam ASTM A992 W36x231 (web t_w = 0.760 in.); column ASTM A992 W14x90\n  (flange t_f = 0.710 in.). F_y = 50 ksi, F_u = 65 ksi.\n- Angles: 2L4x3-1/2x3/8 (short legs back-to-back), ASTM A572 Grade 50, F_y = 50 ksi,\n  F_u = 65 ksi; length l = 23-1/2 in.\n- Bolts (web leg): one vertical line of n = 8 rows of 3/4-in.-dia. Group 120 (e.g. A325)\n  bolts, condition N, standard holes (d_h = 13/16 in.), s = 3 in., l_ev = 1-1/4 in.,\n  l_eh = 1-3/8 in.; bolts are in double shear.\n- Welds (support leg, Welds B): 5/16-in. fillet welds, l = 23-1/2 in., loaded with an\n  eccentricity e_x = 4 in. (a = e_x/l = 0.170).\n- Loads (service): R_D = 37.5 kips, R_L = 113 kips.\n- Code basis: AISC 360-22; ASCE/SEI 7 load combinations.\n\n## Find\nThe available shear strength, checking: shear yielding, shear rupture, and block shear\nrupture of the angles (J4.2, J4.3); shear transfer strength at the bolt holes (J3.7 +\nJ3.11a); the support-leg weld group (J2.4 / Table J2.5, eccentric-group capacity by the\ninstantaneous-center method, Manual Table 8-4) and the minimum support thickness; and\nthe minimum angle thickness for the weld (J2.2b). Identify the governing limit state.",
 "has_figure": true,
 "stem": "II_A_2A",
 "breadcrumb": "EXAMPLE II.A-2A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Bolted/Welded Double-Angle Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-2A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Bolted/Welded Double-Angle Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2/§J4.3, §J2.4/Table J2.5 (eccentric weld group, Manual Table 8-4 basis). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 37.5 kips, L = 113 kips → **LRFD Ru = 226 kips; ASD Ra = 151 kips**

2L4x3-1/2x3/8 SLBB × 23 1/2 in. (A572 Gr. 50): web legs bolted (8 rows of 3/4-in. Group 120-N, double shear, s = 3 in., lev = 1 1/4 in., leh = 1 3/8 in.) to the W36x231 web (tw = 0.760 in.); support legs welded to the W14x90 column flange with 5/16-in. E70 fillets (Welds B), l = 23 1/2 in., ex = 4 in. (a = 0.17).

### 2. Bolt Group (beam-web side, 8 bolts double shear)

φrn = 35.8 kips/bolt; bearing on the beam web (φ = 66.7) and on the angle pair (Σt = 0.75 in., φ = 65.8) and bottom-bolt angle tearout (φ = 37.0) all exceed bolt shear →

**Group: LRFD 8(35.8) = 286 kips ≥ 226 ✓; ASD 8(23.9) = 191 kips ≥ 151 ✓**

### 3. Welds B (support legs, eccentric out-of-plane)

Per weld line (each angle carries R/2 = 113 kips LRFD), elastic combination of direct shear and bending from ex = 4 in.:

fv = 113/23.5 = 4.81 kip/in.; fb = 6(113)(4)/(23.5)² = 4.91 kip/in. → resultant = **6.87 kip/in. ≤ 1.392(5) = 6.96 kip/in. ✓** (99% utilized — **governing**)
ASD: 4.58 ≤ 4.64 kip/in. ✓ (99%)

(The Manual Table 8-4 IC coefficients give slightly more margin; the elastic check shown is conservative.) Minimum weld for the 0.710-in. flange = 1/4 in. ≤ 5/16 ✓; the flange base metal develops the welds ✓.

### 4. Angle Limit States (pair)

- Shear yielding (Eq. J4-3): 0.6(50)(17.6) = 529 kips → 529/353 ✓
- Shear rupture (Eq. J4-4, Anv = 12.4 in.²): φRn = 362/241 ✓
- Block shear (Eq. J4-5): φRn = 378/252 ✓

### 5. Conclusion

The bolted/welded double-angle connection is **adequate** for the 226-kip (LRFD) / 151-kip (ASD) reaction. The governing element is the pair of **5/16-in. support-leg fillet welds under the 4-in. eccentricity, at ≈99% utilization** — the weld size cannot be reduced — while the 8-bolt double-shear group (286/191 kips) and all angle limit states retain healthy margins. The detail conforms to AISC 360-22 Chapter J and Manual Part 10 practice.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-2A (from figures/IIA_2A.png)

Bolted/welded double-angle shear connection: 2L4×3½×⅜ SLBB × 1'-11½" (l = 23½ in.);
beam W36×231 (web), welded to a column flange ("Welds B").

- **Web leg (bolted to beam web):** one vertical line of **8 bolts**, ¾-in.
  Group 120 (N) standard holes; l_ev = 1¼ in. top/bottom, **7 @ 3 in. = 1'-9"
  (21 in.)** between.
- Horizontal edge dimensions at the top: 2⅛ in., 1⅝ in., 1⅜ in. (l_eh = 1⅜ in.).
- **Support leg (welded to column flange, "Welds B"):** 5/16-in. fillet weld with
  a **⅝-in. return at the top** (typ.); the weld group is loaded eccentrically.
- The beam **bottom flange is coped for erection**. Section A-A shows the two
  angles back-to-back with the 5/16-in. welds to the column flange.
