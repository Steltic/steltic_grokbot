<!-- chunk_id: II.B-3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.B-3",
 "example_family": "II.B-3",
 "chapter": "II.B",
 "topic": "FR moment connection",
 "clauses": [
  "J10.1",
  "J10.2",
  "J10.3",
  "J10.8"
 ],
 "eqs": [
  "J10-1",
  "J10-2",
  "J10-4"
 ],
 "tables": [
  "J2.5"
 ],
 "title": "Directly Welded Flange FR Moment Connection",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.B-3 — Directly Welded Flange FR Moment Connection",
 "question": "# II.B-3 — Directly welded flange fully restrained (FR) moment connection (beam-to-column flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA wide-flange beam frames into the flange of a wide-flange column with a directly\nwelded flange fully restrained (FR) moment connection: each beam flange is connected\nto the column flange with a complete-joint-penetration (CJP) groove weld, and the\nvertical shear is carried by a single bolted web plate (already verified separately).\nThe strong-axis moment is delivered as a tension/compression couple through the two\nbeam flanges.\n\nVerify that the directly welded flange FR moment connection is adequate for the given\nbeam end reactions, and check whether the column requires transverse stiffening for\nthe concentrated flange forces.\n\nConfiguration (see figures/IIB_3.png):\n- Beam: ASTM A992 W18×50 (Fy = 50 ksi, Fu = 65 ksi); d = 18.0 in., bf = 7.50 in.,\n  tf = 0.570 in., tw = 0.355 in.\n- Column: ASTM A992 W14×99 (Fy = 50 ksi, Fu = 65 ksi); d = 14.2 in., bf = 14.6 in.,\n  tf = 0.780 in.\n- Both beam flanges connected to the column flange with CJP groove welds. Web plate:\n  PL⅜ in. × 5 in. × 0 ft 9 in., ASTM A572 Gr. 50, three ⅞-in. Group 120 bolts\n  (thread cond. N), ¼-in. fillet welds to the column (verified in Example II.B-1).\n- Electrodes: 70-ksi (FEXX = 70 ksi), matching filler metal for the CJP welds.\n\n## Given\n- Material: beam and column ASTM A992 (Fy = 50, Fu = 65 ksi); web plate ASTM A572\n  Gr. 50 (Fy = 50, Fu = 65 ksi).\n- Geometry: as listed above and shown in figures/IIB_3.png.\n- Loads (service): vertical shear VD = 7 kips, VL = 21 kips; strong-axis moment\n  MD = 42 kip-ft, ML = 126 kip-ft.\n- Code basis: AISC 360-22 (Specification); ASCE/SEI 7 for load combinations.\n\n## Find\nVerify that the CJP groove welds of the beam flanges to the column flange transfer the\nflange tension and compression forces of the moment couple, and check the W14×99\ncolumn for the concentrated flange forces (flange local bending, web local yielding,\nweb local crippling). Report whether the connection is adequate (LRFD and ASD).",
 "has_figure": true,
 "stem": "II_B_3",
 "breadcrumb": "EXAMPLE II.B-3 · AISC 360-22 II.B (FR moment connection) · §J10.1 §J10.2 §J10.3 §J10.8 · Directly Welded Flange FR Moment Connection",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.B-3 · AISC 360-22 II.B (FR moment connection) · §J10.1 §J10.2 §J10.3 §J10.8 · Directly Welded Flange FR Moment Connection

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: Table J2.5 (CJP groove welds with matching filler — strength governed by base metal), §J10.1 (Eq. J10-1), §J10.2 (Eq. J10-2), §J10.3 (Eq. J10-4), §J10.8 (stiffener sizing). Per the RAG extract provided. (Web plate verified in Example II.B-1.)

---

### 1. Required Strengths

Mu = 252 kip-ft = 3,024 kip-in.; Ma = 168 kip-ft = 2,016 kip-in. Flange-couple arm = d − tf = 17.4 in. →

**Puf = 3,024/17.4 = 174 kips (LRFD); Paf = 116 kips (ASD)**; Vu = 42 / Va = 28 kips through the web plate.

### 2. CJP Flange Welds

With matching 70-ksi filler, the CJP groove welds develop the connected base metal (Table J2.5); the governing check is tensile yielding of the beam flange:

φRn = 0.90(50)(7.50 × 0.570) = **192 kips ≥ 174 ✓** (ASD 128 ≥ 116 ✓)

### 3. Column Concentrated-Force Checks (W14x99; lb = tf = 0.570 in.)

| Limit state | Available LRFD/ASD (kips) | Demand (kips) | Result |
|---|---|---|---|
| Flange local bending (Eq. J10-1): φ6.25Fytf² | 171 / 114 | 174 / 116 | **✗ (≈2% over)** |
| Web local yielding (Eq. J10-2) | 181 / 121 | 174 / 116 | ✓ (96%) |
| Web local crippling (Eq. J10-4) | 231 / 154 | 174 / 116 | ✓ |

**Flange local bending is exceeded** (by ~3 kips LRFD / 2 kips ASD) → **transverse stiffeners (continuity plates) are required opposite the tension flange** per §J10.1.

### 4. Continuity Plates — §J10.8

Required stiffener force = Puf − φRn,FLB = 174 − 171 = **3 kips (LRFD)** — nominal; dimensional minimums govern:
width ≥ bf,beam/3 − tw,col/2 = 7.50/3 − 0.24 = 2.26 in.; thickness ≥ tf,beam/2 = 0.29 in.; extend at least half the column depth.

**Provide a pair of PL5/16 × 2 1/2 continuity plates** (each side of the column web, both flange levels for symmetry of fabrication), welded to develop the (small) transferred force.

### 5. Conclusion

The directly welded flange FR connection is **adequate** for Mu = 252 kip-ft / Ma = 168 kip-ft: the CJP-welded flanges develop the beam flange (91% utilized), the previously verified web plate carries the 42-kip shear, and the column needs only **nominal continuity plates** because the higher flange force of the direct-welded detail (couple arm d − tf rather than d + tp) pushes column flange local bending ~2% past its available strength. Web yielding and crippling are satisfied without doublers.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.B-3 (from figures/IIB_3.png)

Directly-welded-flange FR moment connection: W18×50 beam to a W14×99 column flange.

- **Both beam flanges** connected to the column flange with **complete-joint-
  penetration (CJP) groove welds** ("CJP, both flanges").
- **Web plate (shear, verified in II.B-1):** PL⅜ × 5 in. × 0'-9", **3 ⅞-in.
  Group 120 (N)** bolts (standard holes), 2 @ 3 in. = 6 in., 3-in. to first bolt;
  ¼-in. fillet weld to the column flange.
- ½-in. beam setback. Moment delivered as a tension/compression couple through the
  two CJP-welded flanges.
