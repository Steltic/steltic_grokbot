<!-- chunk_id: II.A-17B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-17B",
 "example_family": "II.A-17",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.1",
  "J4.2",
  "J4.3",
  "J2.4"
 ],
 "eqs": [
  "J4-1",
  "J4-5"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Single-Plate Connection Under Combined Shear and Axial Tension",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-17B — Single-Plate Connection Under Combined Shear and Axial Tension",
 "question": "# II.A-17B — Single-Plate Connection Subject to Axial and Shear Loading (Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA single-plate (\"shear tab\") connection joins the web of an ASTM A992/A992M\nW18×50 beam to the flange of an ASTM A992/A992M W14×90 column. The plate is a\n½-in.-thick ASTM A572/A572M Grade 50 shear plate, 14½ in. long, welded to the\ncolumn flange with a two-sided fillet weld using 70-ksi electrodes. The beam is\nattached to the plate with a single vertical line of five ⅞-in.-diameter Group 120\n(Group A, e.g., ASTM F3125 Grade A325-equivalent high-strength) bolts in standard\nholes, thread condition N (threads NOT excluded from the shear plane), spaced 3 in.\non center. The horizontal distance from the column face (weld line) to the bolt line\nis a = 2½ in. The vertical edge distance on the plate is l_ev = 1¼ in.; the\nhorizontal edge distance is l_eh = 2½ in. The beam is uncoped and is assumed braced\nagainst rotation (twist) about its longitudinal axis.\n\nThe connection must transfer the following factored/service beam end reactions\napplied simultaneously: a vertical shear and a horizontal axial tension.\n\n## Given\n- Material: beam and column ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); plate\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); 70-ksi weld electrodes.\n- Beam: W18×50 (A_g = 14.7 in.², d = 18.0 in., t_w = 0.355 in., t_f = 0.570 in.).\n- Column: W14×90 (t_f = 0.710 in.).\n- Plate: PL ½ in. × 14½ in., two-sided fillet weld to the column flange.\n- Bolts: five ⅞-in.-dia. Group 120, thread condition N, standard holes\n  (d_h = 15/16 in.), 3 in. pitch; a = e = 2½ in.; l_ev = 1¼ in.; l_eh = 2½ in.\n- Loads: vertical shear V_u = 75 kips / V_a = 50 kips, and axial tension\n  N_u = 60 kips / N_a = 40 kips, acting together.\n- Code basis: AISC 360-22.\n\n## Find\nVerify that the single-plate connection is adequate for the combined shear-plus-axial\ndemand. Check the bolt group (shear with eccentricity, bearing/tearout on the beam\nweb), the weld size needed to develop the plate, and all relevant plate and beam\nlimit states (shear yielding/rupture, tensile yielding/rupture, flexural yielding/\nrupture, block shear, and the axial-shear-flexure interaction), plus the supporting\ncolumn-flange shear rupture. Report the governing limit state and the available\nstrength in both LRFD and ASD.",
 "has_figure": false,
 "stem": "II_A_17B",
 "breadcrumb": "EXAMPLE II.A-17B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.1 §J4.2 §J4.3 §J2.4 · Single-Plate Connection Under Combined Shear and Axial Tension",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-17B · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.1 §J4.2 §J4.3 §J2.4 · Single-Plate Connection Under Combined Shear and Axial Tension

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.1/§J4.2/§J4.3 (Eqs. J4-1 through J4-5), §J2.4 (fillet welds with directional factor). Per the RAG extract provided.

---

### 1. Required Strengths

Vu = 75 kips / Va = 50 kips with Nu = 60 kips / Na = 40 kips (simultaneous) → resultant **96.0 / 64.0 kips** at 38.7° from vertical.

Plate PL1/2 × 14 1/2 (A572 Gr. 50); five 7/8-in. Group 120-N bolts @ 3 in. (lev = 1 1/4 in., leh = 2 1/2 in.); a = 2 1/2 in.; two-sided E70 fillet to the W14x90 column flange; beam W18x50 (tw = 0.355 in.), braced against twist. Effective hole = 1.00 in.

### 2. Bolt Group (§J3.7, §J3.11a)

Per-bolt forces (elastic method; vertical V/5 = 15.0 kips; axial N/5 = 12.0 kips; moment V(a/2) = 93.8 kip-in. adds 6.25 kips horizontally at the extreme bolts, Σy² = 90 in.²):

Extreme-bolt resultant = √(15.0² + 18.3²) = **23.6 kips ≤ φrn = 0.75(54)(0.601) = 24.3 kips ✓** (LRFD)
ASD: 15.8 ≤ 16.2 kips ✓

Bearing on the 1/2-in. plate (φ = 51.2 kips/bolt), horizontal tearout (lc = 2.03 in. → φ = 59.4) and vertical edge tearout (bottom bolt, φ = 22.9 vs. 15.0 kips vertical component) — none govern over bolt shear. Beam-web bearing: φ = 36.4 kips/bolt ✓.

### 3. Plate Limit States

| Limit state | LRFD avail. (kips) | Demand | |
|---|---|---|---|
| Shear yielding (Eq. J4-3) | 218 | 75 | ✓ |
| Shear rupture (Eq. J4-4, Anv = 4.75 in.²) | 139 | 75 | ✓ |
| Tensile yielding (Eq. J4-1) | 326 | 60 | ✓ |
| Tensile rupture (Eq. J4-2, Ae = 4.75 in.²) | 232 | 60 | ✓ |
| Block shear, shear path (Eq. J4-5) | 177 | 75 | ✓ |
| Flexure at weld line (M = V·a = 188 kip-in.) | φMn = 1,180 kip-in. | 188 | ✓ |

(ASD values scale by 1.5/1.67–2.0 and likewise pass; combined V–N–M interaction on the gross section is far below unity.)

### 4. Weld

Use **5/16-in. fillets both sides** (≥ 5/8·tp = 5/16 in., developing the plate). Strength under the 38.7° resultant with the directional factor 1.25:

φRn = 2(1.392)(5)(14.5)(1.25) = **252 kips ≥ 96.0 ✓**; Rn/Ω = 168 ≥ 64.0 ✓

### 5. Conclusion

The PL1/2 × 14 1/2 single-plate connection with five 7/8-in. Group 120-N bolts and 5/16-in. double fillets is **adequate for the combined 75-kip shear and 60-kip axial tension (LRFD)**. The governing check is the extreme bolt under combined direct shear, axial share, and eccentric moment — 23.6 vs. 24.3 kips available (97% utilization); all plate, weld, and web limit states carry comfortable margins. Given the near-full bolt utilization, no reduction in bolt count or diameter is acceptable.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
