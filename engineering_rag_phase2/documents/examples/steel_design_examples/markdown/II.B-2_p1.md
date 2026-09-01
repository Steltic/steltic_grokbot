<!-- chunk_id: II.B-2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.B-2",
 "example_family": "II.B-2",
 "chapter": "II.B",
 "topic": "FR moment connection",
 "clauses": [
  "J4.1",
  "J2.4",
  "J4.2"
 ],
 "eqs": [
  "J4-1",
  "J2-6"
 ],
 "tables": [
  "J2.5"
 ],
 "title": "Welded Flange-Plated FR Moment Connection",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.B-2 — Welded Flange-Plated FR Moment Connection",
 "question": "# II.B-2 — Welded flange-plated fully restrained (FR) moment connection (beam-to-column flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA wide-flange beam frames into the flange of a wide-flange column with a welded\nflange-plated fully restrained (FR) moment connection. The strong-axis moment is\ndelivered through a top and a bottom flange plate; each flange plate is fillet-welded\nto the beam flange (longitudinal welds along the sides, plus a transverse weld across\nthe end at the top plate) and fillet-welded to the column flange. The vertical shear\nis carried by a single bolted web plate (already verified separately). The top flange\nplate is in tension under the applied moment.\n\nVerify that the flange plates and their welds are adequate for the given beam end\nreactions.\n\nConfiguration (see figures/IIB_2.png):\n- Beam: ASTM A992 W18×50 (Fy = 50 ksi, Fu = 65 ksi); d = 18.0 in., bf = 7.50 in.,\n  tf = 0.570 in., tw = 0.355 in., Zx = 101 in.³\n- Column: ASTM A992 W14×99 (Fy = 50 ksi, Fu = 65 ksi); d = 14.2 in., bf = 14.6 in.,\n  tf = 0.780 in.\n- Top (tension) flange plate: PL1 in. × 6 in. × 0 ft 10½ in., ASTM A572 Gr. 50\n  (Fy = 50, Fu = 65). It provides a ¾-in. shelf on each side of the 7.50-in.-wide\n  beam flange. Welded to the beam flange with ⁵⁄₁₆-in. longitudinal fillet welds along\n  both sides plus a ⁵⁄₁₆-in. transverse fillet across the end; welded to the column\n  flange with fillet welds (size to be determined).\n- Bottom (compression) flange plate: PL¾ in. × 8¾ in. × 1 ft 2½ in., ASTM A572 Gr. 50.\n  Welded to the beam flange with ⁵⁄₁₆-in. longitudinal fillet welds, and to the column\n  flange with fillet welds.\n- Electrodes: 70-ksi (FEXX = 70 ksi).\n\n## Given\n- Material: beam and column ASTM A992 (Fy = 50, Fu = 65 ksi); plates ASTM A572 Gr. 50\n  (Fy = 50, Fu = 65 ksi).\n- Geometry: as listed above and shown in figures/IIB_2.png.\n- Loads (service): vertical shear VD = 7 kips, VL = 21 kips; strong-axis moment\n  MD = 42 kip-ft, ML = 126 kip-ft.\n- Code basis: AISC 360-22 (Specification); ASCE/SEI 7 for load combinations.\n\n## Find\nVerify: tensile yielding of the top flange plate; the fillet weld group joining the\ntop flange plate to the beam flange (combined longitudinal + transverse fillet welds);\nconnecting-element rupture (minimum base-metal thickness) at the top-flange welds; the\nfillet weld of the top flange plate to the column flange; the compressive strength of\nthe bottom flange plate; the fillet weld of the bottom flange plate to the beam flange;\nbeam bottom-flange shear rupture at those welds; and the fillet weld of the bottom\nflange plate to the column flange. Report whether the connection is adequate (LRFD and\nASD). (The single-plate web connection is verified in Example II.B-1.)",
 "has_figure": true,
 "stem": "II_B_2",
 "breadcrumb": "EXAMPLE II.B-2 · AISC 360-22 II.B (FR moment connection) · §J4.1 §J2.4 §J4.2 · Welded Flange-Plated FR Moment Connection",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.B-2 · AISC 360-22 II.B (FR moment connection) · §J4.1 §J2.4 §J4.2 · Welded Flange-Plated FR Moment Connection

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J4.1 (Eq. J4-1), §J2.4/Table J2.5 (Eq. J2-6 for combined longitudinal + transverse fillet groups; directional factor 1.5 for transverse welds), §J4.2 (base-metal development). Per the RAG extract provided. (Web connection verified in Example II.B-1.)

---

### 1. Required Strengths

Mu = 252 kip-ft = 3,024 kip-in.; Ma = 168 kip-ft = 2,016 kip-in. Moment arm ≈ d + (tp,top + tp,bot)/2 = 18.0 + 0.875 = 18.9 in. →

**Flange force: Puf ≈ 160 kips (LRFD); Paf ≈ 107 kips (ASD)**

### 2. Top (Tension) Flange Plate — PL1 × 6 × 10 1/2

**Tensile yielding (Eq. J4-1):** φRn = 0.90(50)(6.00) = **270 kips ≥ 160 ✓**; Rn/Ω = 180 ≥ 107 ✓ (no holes — rupture not applicable).

**Weld to the beam flange (5/16-in. fillets: two longitudinal ≈9 in. + one transverse 6 in.), Eq. J2-6:**
φRn = 1.392D[0.85(2 × 9) + 1.5(6)] = 6.96(15.3 + 9.0) = **169 kips ≥ 160 ✓** (ASD 113 ≥ 107 ✓)

**Connecting-element rupture (minimum base metal at the longitudinal welds):** tmin = 3.09D/Fu = 3.09(5)/65 = 0.24 in. ≤ tf = 0.570 in. and ≤ tp = 1.00 in. ✓

**Weld to the column flange (transverse, both faces of the plate, ≈12 in. total):**
required D = 160/[12(1.392)(1.5)] = 6.4 → **use 7/16-in. fillets**: φRn = 175 kips ≥ 160 ✓ (ASD 117 ≥ 107 ✓)

### 3. Bottom (Compression) Flange Plate — PL3/4 × 8 3/4 × 14 1/2

**Compressive strength:** unbraced length ≈ setback only → KL/r ≈ 6 → φPn ≈ 0.90(50)(6.56) = **295 kips ≥ 160 ✓**

**Weld to the beam flange (two longitudinal 5/16-in. fillets):** required length per side = 160/[2(6.96)] = 11.5 in. ≤ available ≈ 12 in. ✓ (ASD: 11.5 in. ✓)

**Beam bottom-flange shear rupture along the weld pair:** tmin = 6.19D/Fu = 0.48 in. ≤ tf = 0.570 in. ✓

**Weld to the column flange (transverse, ≈17.5 in. total across the 8 3/4-in. plate):**
required D = 160/[17.5(1.392)(1.5)] = 4.4 → **use 5/16-in. fillets**: φRn = 183 kips ≥ 160 ✓ (ASD 122 ≥ 107 ✓)

### 4. Conclusion

The welded flange-plated FR connection is **adequate for Mu = 252 kip-ft / Ma = 168 kip-ft**. The governing checks are the top-plate weld group to the beam flange (95% utilized, helped by the 1.5× transverse weld term of Eq. J2-6) and the 7/16-in. transverse welds at the column face (91%). The wider bottom plate spreads the compression force and allows 5/16-in. welds throughout. Column stiffening requirements, checked in Example II.B-1 for the same flange force, remain satisfied.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.B-2 (from figures/IIB_2.png)

Welded flange-plated FR moment connection: W18×50 beam to a W14×99 column flange.

- **Top (tension) flange plate:** PL1 × 6 in. × 0'-10½" (gives a ¾-in. shelf each
  side of the 7.50-in. beam flange). Fillet-welded to the beam flange with
  **5/16-in. longitudinal welds both sides plus a 5/16-in. transverse weld across
  the end**; welded to the column flange (7/16-in. weld marks shown). 1-in.
  dimension at the column.
- **Bottom (compression) flange plate:** PL¾ × 8¾ in. × 1'-2½"; 5/16-in.
  longitudinal fillet welds (5/16, 12½ typ. mark); welded to the column flange.
- **Web plate (shear, verified separately):** PL⅜ × 5 in. × 0'-9", **3 ⅞-in.
  Group 120 (N)** bolts, 2 @ 3 in. = 6 in., 3-in. to first bolt; ¼-in. fillet weld.
- "Shim top or bottom as required" noted.
