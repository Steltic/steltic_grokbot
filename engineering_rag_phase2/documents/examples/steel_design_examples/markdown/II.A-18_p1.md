<!-- chunk_id: II.A-18_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-18",
 "example_family": "II.A-18",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "J2.4"
 ],
 "eqs": [
  "J4-3",
  "J4-4",
  "J4-5"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Single-Plate Connection (Beam to Girder Web, Coped Beam)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-18 — Single-Plate Connection (Beam to Girder Web, Coped Beam)",
 "question": "# II.A-18 — Single-Plate Connection (Beam-to-Girder Web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W18×35 floor beam frames into the web of an ASTM A992/A992M\nW21×62 girder through a conventional single-plate (\"shear tab\") connection. A\nrectangular plate is shop-welded to the girder web with a pair of fillet welds (one\nalong each vertical edge of the plate) and field-bolted to the beam web in a single\nvertical line of four bolts. The plate is ASTM A572/A572M Grade 50 (F_y = 50 ksi,\nF_u = 65 ksi), ¼ in. thick. The four ¾-in.-diameter Group 120 bolts (thread condition\nN, threads not excluded), in standard holes (d_h = 13/16 in.), are spaced 3 in.\nvertically with a vertical edge distance l_ev = 1¼ in. (plate length ≈ 11½ in.). The\nweld is a 3/16-in. fillet (D = 3) using 70-ksi electrodes. The beam top flange is coped\n2 in. deep × 4 in. long; the beam-web vertical edge distance at the cope is l_ev = 1½ in.\nThe beam web is t_w = 0.300 in.; the girder web is t_w = 0.400 in. The configuration\nis shown in figures/IIA_18.png.\n\nThe beam delivers a service dead-load reaction R_D = 6.5 kips and a service live-load\nreaction R_L = 20 kips.\n\n## Given\n- Material: beam and girder ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); plate\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); E70 (F_EXX = 70 ksi).\n- Members: beam W18×35 (d = 17.7 in., t_w = 0.300 in., t_f = 0.425 in.); girder W21×62\n  (t_w = 0.400 in.).\n- Plate: ¼ in. thick, ≈ 11½ in. long, single vertical bolt line.\n- Fasteners: 4 × ¾-in.-dia. Group 120, thread N, standard holes (d_h = 13/16 in.);\n  A_b = 0.442 in²; s = 3 in.; l_ev = 1¼ in. (plate), 1½ in. (beam web at cope).\n- Weld: 3/16-in. fillet (D = 3), E70, one along each vertical edge of the plate.\n- Cope: top flange coped 2 in. deep × 4 in. long.\n- Loads (service): R_D = 6.5 kips, R_L = 20 kips.\n- Code basis: AISC 360-22 (load combinations from ASCE/SEI 7).\n\n## Find\nThe available shear strength of the connection, checking: the shear-transfer strength\nat the bolt holes (bolt shear J3.7 plus bearing/tearout of plate and beam web J3.11,\nwith the bolt-group eccentricity accounted for); shear yielding and shear rupture of\nthe plate (J4.2); block shear rupture of the plate (J4.3); the weld and girder-web\nstrength (J2.4, J4.2); and the coped-beam web (J4.3 block shear). Confirm the available\nstrength exceeds the required reaction for both LRFD and ASD.",
 "has_figure": true,
 "stem": "II_A_18",
 "breadcrumb": "EXAMPLE II.A-18 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Single-Plate Connection (Beam to Girder Web, Coped Beam)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-18 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Single-Plate Connection (Beam to Girder Web, Coped Beam)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2 (Eqs. J4-3/J4-4), §J4.3 (Eq. J4-5), §J2.4; coped-section checks per AISC Manual Part 9. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6.5 kips, L = 20 kips → **LRFD Ru = 39.8 kips; ASD Ra = 26.5 kips**

Plate PL1/4 × 4 1/2 × 11 1/2 (A572 Gr. 50); four 3/4-in. Group 120-N bolts @ 3 in. (lev = 1 1/4 in., leh = 1 1/2 in.); a = 3 in. (e = a/2 = 1.5 in.); 3/16-in. E70 fillets both vertical edges to the W21x62 girder web (tw = 0.400 in.). Beam W18x35 (tw = 0.300 in.) coped 2 in. × 4 in. Effective hole = 7/8 in.

### 2. Bolt Group and Shear Transfer

Eccentric bolt-group coefficient (4 @ 3 in., e = 1.5 in.): C ≈ 3.43 → φRn = 3.43(17.9) = **61.4 kips** / Rn,Ω = **40.8 kips**.
Plate bearing/tearout (vertical): bottom-bolt tearout φ = 12.3 kips; group = 12.3 + 3(17.9) = 66.0 kips — not governing. Beam-web (0.300 in.) bearing: 2.4dtFu = 35.1 kips/bolt (φ = 26.3) > bolt shear ✓.

### 3. Plate Limit States (as Example II.A-17A geometry)

- Shear yielding (Eq. J4-3): φRn = 86.3 / 57.5 kips ✓
- **Shear rupture (Eq. J4-4): φRn = 58.5 / 39.0 kips** ← governing connection limit
- Block shear (Eq. J4-5): φRn = 65.5 / 43.7 kips ✓
- Flexure at e: trivial (Mu = 59.7 kip-in. ≪ φMn = 372 kip-in.) ✓

### 4. Weld

Two 3/16-in. fillets × 11.5 in.: φRn = 2(1.392)(3)(11.5) = **96.0 kips** / 64.1 kips ✓. 3/16 ≥ (5/8)tp = 5/32 → develops the plate; girder-web base metal (0.400 in.) adequate for the two-sided weld (3.09D/Fu × 2 = 0.29 in. ≤ 0.400) ✓.

### 5. Coped Beam Checks (Manual Part 9)

- Flexure of the coped section (cope 2 × 4 in.; e = c + setback = 4.5 in.): Mu = 39.8(4.5) = 179 kip-in.; with Snet ≈ 18.2 in.³ and local buckling non-critical for c/d = 0.23, φMn = 0.9(50)(18.2) = 819 kip-in. ✓ (ASD likewise)
- Block shear of the beam web at the bolt line (Ubs = 1.0): φRn ≈ 88 kips ≥ 39.8 ✓
- Web shear yielding/rupture through the reduced depth: φRn = 1.0(0.6)(50)(15.7 × 0.300) = 141 kips ✓

### 6. Summary and Conclusion

| Element | LRFD (kips) | ASD (kips) |
|---|---|---|
| Bolt group (eccentric) | 61.4 | 40.8 |
| **Plate shear rupture (governs)** | **58.5** | **39.0** |
| Weld | 96.0 | 64.1 |
| Coped-beam checks | ≥ 88 | ≥ 59 |
| **Available / required** | **58.5 / 39.8 ✓** | **39.0 / 26.5 ✓** |

The conventional shear tab to the girder web is **adequate** at 68% utilization, governed by plate shear rupture; the 2 × 4 in. top cope does not control. The detail complies with AISC 360-22 Chapter J and Manual Parts 9/10.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-18 (from figures/IIA_18.png)

Supplements the question text with information that is only in the figure (the text
gives plate thickness/length and a, but not the plate width or the bolt-to-edge
distance needed for plate block shear):

- **Single plate: PL¼ × 4½ in. wide × 0'-11½ in. long.** (Width = 4½ in.)
- Horizontal: weld line (girder-web face) to bolt line a = 3 in.; bolt line to the
  plate free edge l_eh = 1½ in. (3 + 1½ = 4½ in.).
- Vertical bolt layout: l_ev = 1¼ in., 3 @ 3 in. = 9 in., l_ev = 1¼ in.
  (four bolts in a single line; plate length 11½ in.).
- Beam top flange coped d_c = 2 in. deep × c = 4 in. long; beam-web vertical edge
  distance at the cope l_ev = 1½ in.
- Weld: 3/16-in. fillet (D = 3), E70, one along each vertical edge of the plate.
