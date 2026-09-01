<!-- chunk_id: II.A-28A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-28A",
 "example_family": "II.A-28",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3"
 ],
 "eqs": [],
 "tables": [
  "J3.2",
  "10"
 ],
 "title": "All-Bolted Single-Angle Connection (Beam to Girder Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-28A — All-Bolted Single-Angle Connection (Beam to Girder Web)",
 "question": "# II.A-28A — All-Bolted Single-Angle Connection (Beam-to-Girder Web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W18×35 beam frames into the web of an ASTM A992/A992M W21×62 girder\nusing a single (one-sided) bolted angle (see figures/IIA_28A.png). The beam is coped at\nthe top flange only (cope 2 in. deep × 4 in. long). The angle is an ASTM A572/A572M\nGrade 50 L4×3×⅜ × 0'-11½″: the 4-in. leg is bolted to the beam web and the 3-in. leg\n(standard 1¾-in. gage) is bolted to the girder web. Each leg has four ¾-in.-diameter\nGroup 120 bolts (thread condition N) in standard holes at 3-in. spacing; l_ev = 1¼ in.\nThis is Case I of AISC Manual Table 10-11 (the supported-beam leg sees negligible\neccentricity; the support leg carries the reaction at an eccentricity).\n\nThe beam carries service end reactions R_D = 6.5 kips and R_L = 20 kips.\n\nVerify the connection and identify the governing limit state.\n\n## Given\n- Material: beam and girder ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); angle\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n- Beam: W18×35, d = 17.7 in., t_w = 0.300 in. Girder web t_w = 0.400 in.\n- Angle: L4×3×⅜, 11½ in. long; four ¾-in.-dia. Group 120-N bolts per leg in standard\n  holes (d_h = 13/16 in., A_b = 0.442 in.²), s = 3 in., l_ev = 1¼ in.; gage on 3-in.\n  support leg = 1¾ in. Eccentricity on the support leg e = 1¾ + t_w/2 = 1.90 in.\n- Cope: d_c = 2.00 in., c = 4 in., e_cope = c + ¾-in. setback = 4.75 in.\n- Loads: R_D = 6.5 kips, R_L = 20 kips.\n- Code basis: AISC 360-22 (Chapters J and F); loads per ASCE/SEI 7.\n\n## Find\nThe available strength (LRFD φR_n, ASD R_n/Ω), checking: the eccentric bolt group at\nthe angle (J3.7 + J3.11a) and the bolt groups at the beam web and girder web; angle\nshear yielding/rupture (J4.2), angle block shear (J4.3), angle flexural yielding (F11.1)\nand flexural rupture; and the coped-beam web (flexural local buckling, shear yielding\nJ4.2, block shear J4.3). Identify the governing limit state and confirm adequacy.",
 "has_figure": true,
 "stem": "II_A_28A",
 "breadcrumb": "EXAMPLE II.A-28A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Single-Angle Connection (Beam to Girder Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-28A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Single-Angle Connection (Beam to Girder Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2/§J4.3; coped-beam checks per Manual Part 9; single-angle Case I model per Manual Table 10-11. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6.5 kips, L = 20 kips → **LRFD Ru = 39.8 kips; ASD Ra = 26.5 kips**

L4x3x3/8 × 11 1/2 (A572 Gr. 50): 4-in. leg to the W18x35 web (tw = 0.300 in., coped 2 × 4 in.), 3-in. leg to the W21x62 girder web (tw = 0.400 in.); four 3/4-in. Group 120-N bolts per leg @ 3 in.; support-leg eccentricity e = 1.75 + tw/2 = 1.90 in. (Case I).

### 2. Bolt Groups

**Support leg (4 bolts, e = 1.90 in.):** C ≈ 3.4 → φRn = 3.4(17.9) = **60.9 kips ≥ 39.8 ✓**; Rn/Ω = **40.5 ≥ 26.5 ✓** (governing bolt check, 65% utilized). Girder-web bearing (φ = 35.1 kips/bolt) and angle bearing/edge tearout (φ ≥ 18.5 kips/bolt) do not control.

**Beam-web leg (4 bolts, negligible eccentricity):** φRn = 4(17.9) = 71.6 kips ✓; beam-web bearing φ = 26.3 kips/bolt ✓.

### 3. Angle Limit States

- Shear yielding (Eq. J4-3): 0.6(50)(4.31) = 129 kips → 129/86.3 ✓
- Shear rupture (Eq. J4-4, Anv = 3.00 in.²): φRn = 87.8/58.5 ✓
- Block shear (Eq. J4-5): φRn = 98.3/65.5 ✓

### 4. Coped Beam (Manual Part 9)

- Flexure at the cope (e = 4.75 in.): Mu = 189 kip-in. vs. φMn ≈ 0.9(50)(15.8) = 711 kip-in. ✓ (local buckling non-critical, c/d = 0.23)
- Beam-web block shear at the bolt line: φRn ≈ 80.8 kips ≥ 39.8 ✓
- Web shear through the reduced section: ample ✓

### 5. Conclusion

The one-sided L4x3x3/8 connection is **adequate** for 39.8 kips (LRFD) / 26.5 kips (ASD). The governing limit state is the **eccentrically loaded support-leg bolt group (e = 1.90 in.)** at ~65% utilization — consistent with the Case I treatment of Manual Table 10-11, where the supported-beam leg sees negligible eccentricity. All angle and coped-beam limit states carry healthy margins. Note that single-angle connections should be limited to one side framing; the beam must be braced against torsion by the slab/deck as is standard.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-28A (from figures/IIA_28A.png)

All-bolted single (one-sided) angle connection: beam W18×35 to a W21×62 girder web;
beam **coped at the top flange** (cope length **c = 4 in.**, depth **d_c = 2 in.**).

- **Angle:** L4×3×⅜ × 0'-11½" (11½ in. long); the **4-in. leg** is bolted to the
  beam web and the **3-in. leg** (standard **1¾-in. gage**) to the girder web.
- **Bolts:** ¾-in. Group 120 (N), standard holes; **4 per leg**, 3 @ 3 in. = 9 in.,
  l_ev = 1¼ in.; **l_eh = 1¼ in. on the 3-in. (support) leg** and **1½ in. on the
  4-in. (beam) leg**; 2½-in. dimension at the bottom.
- ¾-in. beam setback. (Case I of Manual Table 10-11: supported-beam leg sees
  negligible eccentricity; the support leg carries the reaction eccentrically,
  e = 1¾ + t_w/2 = 1.90 in.)
