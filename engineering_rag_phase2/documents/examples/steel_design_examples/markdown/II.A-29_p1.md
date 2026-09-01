<!-- chunk_id: II.A-29_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-29",
 "example_family": "II.A-29",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J2.4",
  "J4.2",
  "J4.3"
 ],
 "eqs": [],
 "tables": [
  "J3.2",
  "J2.5",
  "10"
 ],
 "title": "Bolted/Welded Single-Angle Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-29 — Bolted/Welded Single-Angle Connection (Beam to Column Flange)",
 "question": "# II.A-29 — Bolted/Welded Single-Angle Connection (Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simple (shear) beam-end connection uses a single angle to join the web of a wide-flange\nbeam to the flange of a wide-flange column. The supported beam is an ASTM A992 W16×50\n(Fy = 50 ksi, Fu = 65 ksi; web thickness tw = 0.380 in., depth d = 16.3 in.). The supporting\nmember is an ASTM A992 W14×90 column (flange thickness tf = 0.710 in.). The connecting\nelement is a single angle L4×3×3/8, 11½ in. long, of ASTM A572 Grade 50 steel\n(Fy = 50 ksi, Fu = 65 ksi). The 4-in. leg is field-bolted to the beam web and the 3-in. leg\nis shop-welded to the column flange.\n\nThe bolts are four ¾-in.-diameter Group 120 bolts (e.g., A325) in standard holes, with the\nthreads NOT excluded from the shear plane (thread condition N). They are in a single vertical\nline at 3-in. pitch (3 spaces @ 3 in. = 9 in.), with a 1¼-in. end (vertical edge) distance top\nand bottom. The bolt area is Ab = 0.442 in.² and the standard hole diameter is dh = 13/16 in.\nThe bolt-group eccentricity on the beam-web (4-in.) leg is e = 2¾ in. The weld to the column\nflange is a 3/16-in. fillet weld (D = 3 sixteenths) along each vertical edge of the 3-in. leg,\nmade with 70-ksi electrodes (FEXX = 70 ksi); the weld length is l = 11½ in. The connection\ngeometry is shown in figures/IIA_29.png.\n\nThe beam is uncoped, so block shear and shear rupture of the beam web are not limit states here.\n\n## Given\n- Material: beam/column ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); angle ASTM A572 Gr. 50 (Fy = 50, Fu = 65). Weld 70-ksi electrodes.\n- Geometry: single angle L4×3×3/8 × 11½ in.; 4 bolts at 3-in. pitch, lev = 1¼ in.; bolt eccentricity e = 2¾ in.; weld 3/16-in. fillet, l = 11½ in.\n- Members: W16×50 beam (tw = 0.380 in.); W14×90 column (tf = 0.710 in.).\n- Loads (service): dead reaction RD = 9 kips, live reaction RL = 27 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nDetermine the available strength of the single-angle connection (LRFD design strength φRn and\nASD allowable strength Rn/Ω) considering the governing limit states — bolt shear, bolt\nbearing/tearout, weld shear, and shear yielding, shear rupture, and block shear rupture of\nthe angle — and confirm it is adequate for the required end reaction.",
 "has_figure": true,
 "stem": "II_A_29",
 "breadcrumb": "EXAMPLE II.A-29 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J2.4 §J4.2 §J4.3 · Bolted/Welded Single-Angle Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-29 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J2.4 §J4.2 §J4.3 · Bolted/Welded Single-Angle Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J2.4/Table J2.5, §J4.2/§J4.3; single-angle connection model per AISC Manual Part 10 (Table 10-12 basis: the rigid welded support leg resists the connection eccentricity; the bolt group resists direct shear). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 9 kips, L = 27 kips → **LRFD Ru = 54.0 kips; ASD Ra = 36.0 kips**

L4x3x3/8 × 11 1/2 (A572 Gr. 50): 4-in. leg bolted to the W16x50 web (four 3/4-in. Group 120-N @ 3 in., lev = 1 1/4 in.; bolt line e = 2 3/4 in. from the column face); 3-in. leg welded to the W14x90 column flange with 3/16-in. E70 fillets along both vertical edges (l = 11 1/2 in. each).

### 2. Bolt Group (direct shear; eccentricity carried by the welded leg)

φRn = 4(17.9) = **71.6 kips ≥ 54.0 ✓**; Rn/Ω = 4(11.9) = **47.7 kips ≥ 36.0 ✓**

Bearing on the beam web (0.380 in.): φ = 33.3 kips/bolt; on the 3/8-in. angle: φ = 32.9 kips/bolt; bottom-bolt angle tearout: φ = 18.5 kips — none control below the per-bolt demand of 13.5 kips ✓. (Beam uncoped — web block shear/rupture not applicable.)

### 3. Weld Group (out-of-plane eccentric moment, e = 2 3/4 in.)

Two vertical 3/16-in. fillets, l = 11.5 in., bending about the group's horizontal axis plus direct shear:

fv = Ru/(2l) = 54.0/23.0 = 2.35 kip/in.; fb = 6Rue/(2l²) = 6(54.0)(2.75)/(2 × 132.3) = 3.37 kip/in.
Resultant = √(2.35² + 3.37²) = **4.11 kip/in. ≤ 1.392D = 4.18 kip/in. ✓** (LRFD, 98% utilized)
ASD: 2.74 ≤ 0.928D = 2.78 kip/in. ✓ (98%)

Minimum weld for the 0.710-in. column flange = 1/4 in.? Per Table J2.4 the minimum is based on the **thinner** part joined (3/8-in. angle → 3/16 in.) ✓. Column-flange base metal ample.

### 4. Angle Limit States

Shear yielding 0.6(50)(4.31) = 129 kips → 129/86.3 ✓; shear rupture φRn = 87.8/58.5 ✓; block shear at the bolted leg φRn = 98.3/65.5 ✓.

### 5. Conclusion

The bolted/welded single-angle connection is **adequate** for 54.0 kips (LRFD) / 36.0 kips (ASD), but the governing element — the **pair of 3/16-in. vertical fillet welds under the out-of-plane eccentric moment — is essentially fully utilized (98%)**. Consistent with Manual Table 10-12 practice, the welds, not the bolts, absorb the connection eccentricity; any increase in reaction requires a 1/4-in. weld. All other limit states have ≥25% reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-29 (from figures/IIA_29.png)

Bolted/welded single-angle connection: beam W16×50 web to a W14×90 column flange.

- **Angle:** L4×3×⅜ × 0'-11½" (11½ in. long).
- **Beam-web leg (4-in. leg), bolted:** four ¾-in. Group 120 (N) bolts, standard
  holes, one vertical line, 3 @ 3 in. = 9 in., l_ev = 1¼ in.; **bolt-group
  eccentricity e = 2¾ in.**; 4-in. and l_eh = 1¼-in. horizontal dimensions; 3 in.
  to first row.
- **Column-flange leg (3-in. leg), welded:** 3/16-in. fillet weld along each
  vertical edge of the leg, length l = 11½ in. (weld marks 3/16 and ⅝ shown).
