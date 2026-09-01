<!-- chunk_id: II.A-11A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-11A",
 "example_family": "II.A-11",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J2.4",
  "J3.7",
  "J3.11",
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
  "J2.5",
  "J3.2"
 ],
 "title": "Shear End-Plate Connection (Beam to Girder Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-11A — Shear End-Plate Connection (Beam to Girder Web)",
 "question": "# II.A-11A — Shear End-Plate Connection (Beam-to-Girder Web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W18×50 floor beam frames into the web of an ASTM A992/A992M\nW21×62 girder using a shear end-plate connection. A rectangular end plate is shop-\nwelded to the end of the beam web with a pair of fillet welds (one each side of the\nweb) and field-bolted to the girder web. The plate is 8½ in. long × ¼ in. thick,\nASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi). It carries three rows of\n¾-in.-diameter Group 120 bolts (e.g., A325), thread condition N (threads not excluded\nfrom the shear plane), in standard holes (d_h = 13/16 in.), arranged in two vertical\ncolumns (two bolts per row) at a 3-in. vertical pitch; the vertical edge distance is\nl_ev = 1¼ in. and the horizontal edge distance to each bolt line is l_eh = 1¼ in.\nThe fillet welds use 70-ksi electrodes (E70) and are 3/16 in. (D = 3 sixteenths).\nThe beam web is t_w = 0.355 in.; the girder web is t_w = 0.400 in. The configuration\nis shown in figures/IIA_11a.png.\n\nThe beam delivers a service dead-load reaction R_D = 10 kips and a service live-load\nreaction R_L = 30 kips.\n\n## Given\n- Material: beam and girder ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); end plate\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); E70 electrodes (F_EXX = 70 ksi).\n- Members: beam W18×50 (t_w = 0.355 in.); girder W21×62 (t_w = 0.400 in.).\n- End plate: 8½ in. long × ¼ in. thick.\n- Fasteners: ¾-in.-dia. Group 120, thread condition N, standard holes (d_h = 13/16 in.);\n  A_b = π(¾)²/4 = 0.442 in². Three rows at 3-in. pitch, two columns; l_ev = l_eh = 1¼ in.\n- Welds: 3/16-in. fillet (D = 3), E70, one each side of the beam web.\n- Loads (service): R_D = 10 kips, R_L = 30 kips.\n- Code basis: AISC 360-22 (load combinations from ASCE/SEI 7).\n\n## Find\nThe available shear strength of the connection, checking the governing limit states:\nshear yielding and shear rupture of the end plate (J4.2), block shear rupture of the\nend plate (J4.3), the shear-transfer strength at the bolt holes (bolt shear J3.7 plus\nbearing/tearout J3.11), and the weld plus beam-web strength (J2.4, J4.2). Confirm the\navailable strength exceeds the required reaction for both LRFD and ASD.",
 "has_figure": true,
 "stem": "II_A_11A",
 "breadcrumb": "EXAMPLE II.A-11A · AISC 360-22 II.A (simple / shear connection) · §J2.4 §J3.7 §J3.11 §J4.2 §J4.3 · Shear End-Plate Connection (Beam to Girder Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-11A · AISC 360-22 II.A (simple / shear connection) · §J2.4 §J3.7 §J3.11 §J4.2 §J4.3 · Shear End-Plate Connection (Beam to Girder Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2.4/Table J2.5 (fillet welds), §J3.7/Table J3.2 (bolt shear), §J3.11 (Eqs. J3-6a/c), §J4.2 (Eqs. J4-3, J4-4), §J4.3 (Eq. J4-5). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 10 kips, L = 30 kips → **LRFD Ru = 1.2(10) + 1.6(30) = 60.0 kips; ASD Ra = 40.0 kips**

Geometry (per figure): PL 1/4 × 6 × 8 1/2 (A572 Gr. 50); six 3/4-in. Group 120-N bolts (2 columns @ g = 3 1/2 in., 3 rows @ 3 in.; lev = leh = 1 1/4 in.); 3/16-in. E70 fillets both sides of the W18x50 web (tw = 0.355 in.); girder web tw = 0.400 in. Effective hole = 13/16 + 1/16 = 7/8 in.

### 2. End-Plate Limit States (two shear planes, one each side of the web)

**Shear yielding (Eq. J4-3, φ = 1.00/Ω = 1.50):** Agv = 2(8.5)(0.25) = 4.25 in.² → Rn = 0.6(50)(4.25) = 128 kips → **128 / 85.0 kips**

**Shear rupture (Eq. J4-4, φ = 0.75/Ω = 2.00):** Anv = 2[8.5 − 3(0.875)](0.25) = 2.94 in.² → Rn = 0.6(65)(2.94) = 115 kips → **85.9 / 57.3 kips**

**Block shear (Eq. J4-5, Ubs = 1.0; one L-block per bolt column):** per block Agv = 1.81 in.², Anv = 1.27 in.², Ant = 0.203 in.²:
Rn = 0.6(65)(1.27) + 65(0.203) = 62.6 ≤ 0.6(50)(1.81) + 13.2 = 67.6 → 62.6 kips/block × 2 = 125 kips → **93.8 / 62.6 kips**

### 3. Bolt Shear-Transfer at the Girder Web

Bolt shear (Fnv = 54 ksi, Ab = 0.442 in.²): φrn = 17.9 kips; rn/Ω = 11.9 kips.
Plate bearing (interior bolts): 2.4dtFu = 29.3 kips → φ = 21.9 > 17.9 → bolt shear controls.
Plate tearout (bottom-row bolts, lc = 1.25 − 0.875/2 = 0.844 in.): 1.2lctFu = 16.5 kips → **φ = 12.3 kips / Ω-based 8.23 kips controls those two bolts**. Girder-web bearing (t = 0.400 in.): φ = 35.1 kips — not controlling.

Group: **LRFD 2(12.3) + 4(17.9) = 96.2 kips; ASD 2(8.23) + 4(11.9) = 64.2 kips**

### 4. Weld and Beam Web

Two 3/16-in. E70 fillets × 8.5 in.: φRn = 2(1.392)(3)(8.5) = **71.0 kips**; Rn/Ω = 2(0.928)(3)(8.5) = **47.3 kips**. Minimum size 1/8 in. for the 1/4-in. plate ✓ (Table J2.4).
Beam web shear at the connection (Eq. J4-3): 0.6(50)(8.5)(0.355) = 90.5 kips → 90.5 / 60.4 kips ✓.

### 5. Summary

| Limit state | LRFD (kips) | ASD (kips) |
|---|---|---|
| Plate shear yielding | 128 | 85.0 |
| Plate shear rupture | 85.9 | 57.3 |
| Plate block shear | 93.8 | 62.6 |
| Bolt shear + bearing/tearout | 96.2 | 64.2 |
| **Weld (governs)** | **71.0** | **47.3** |
| Beam web shear | 90.5 | 60.4 |
| **Connection available** | **71.0 ≥ 60.0 ✓** | **47.3 ≥ 40.0 ✓** |

### 6. Conclusion

The shear end-plate connection is **adequate**: the governing limit state is the pair of 3/16-in. fillet welds (71.0 kips LRFD / 47.3 kips ASD, ~85% utilized), with bolt-group strength next (edge-bolt tearout limiting the bottom row). All AISC 360-22 Chapter J checks are satisfied for the 60-kip (LRFD) / 40-kip (ASD) reaction.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-11A (from figures/IIA_11a.png)

Supplements the question text with information that is only in the figure (the text
gives the plate length and thickness and l_eh, but not the plate width or the bolt
gage, leaving the end-plate block-shear geometry underdetermined):

- **End plate: PL¼ × 6 in. wide × 0'-8½ in. long.** (Width = 6 in.)
- **Bolt gage g = 3½ in.** between the two vertical bolt lines, with horizontal edge
  distance l_eh = 1¼ in. on each side (1¼ + 3½ + 1¼ = 6 in.).
- Vertical bolt layout: l_ev = 1¼ in., 2 @ 3 in. = 6 in., l_ev = 1¼ in.
  (three rows; plate length 8½ in.).
- The beam top flange is coped c = 4 in. long × d_c = 2 in. deep to clear the girder
  flange. (The cope is shown for context; it is not itself a required limit state for
  the end-plate checks in this example.)
