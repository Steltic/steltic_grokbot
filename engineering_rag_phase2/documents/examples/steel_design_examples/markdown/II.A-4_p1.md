<!-- chunk_id: II.A-4_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-4",
 "example_family": "II.A-4",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
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
  "J3.2"
 ],
 "title": "All-Bolted Double-Angle Connection (Coped Beam to Girder Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-4 — All-Bolted Double-Angle Connection (Coped Beam to Girder Web)",
 "question": "# II.A-4 — All-Bolted Double-Angle Connection in a Coped Beam  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W18×50 beam frames into the web of an ASTM A992/A992M W21×62\ngirder using an all-bolted double-angle connection. The beam is coped at the top\nflange only; the cope is 2 in. deep and 4 in. long. The angles are a pair of\nASTM A572/A572M Grade 50 L5×3½×¼ (short legs back-to-back), 8½ in. long, attached\nwith three rows of ¾-in.-diameter Group 120 (e.g., A325) bolts, threads not excluded\nfrom the shear plane (thread condition N), in standard holes. Bolt vertical spacing\nis 3 in.; the vertical edge distance on the angles and beam web is l_ev = 1¼ in., and\nthe horizontal edge distance to the tension face on the beam web is l_eh = 1⅝ in.\nAssume a beam setback of ¾ in. (½ in. nominal plus ¼ in. tolerance for mill underrun).\n\nThe beam carries the following service end reactions: dead load R_D = 10 kips and\nlive load R_L = 30 kips.\n\nVerify that the connection has adequate available shear strength for the factored\n(LRFD) and service (ASD) end reactions, and identify the governing limit state.\n\n## Given\n- Material: beam and girder ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); angles\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n- Beam: W18×50, d = 18.0 in., t_w = 0.355 in. Girder web: t_w = 0.400 in.\n- Cope: d_c = 2.00 in. deep, c = 4 in. long; setback ½ in.; e = c + setback = 4.50 in.\n- Angles: 2L5×3½×¼ (SLBB), length 8½ in., three rows of bolts at s = 3 in.,\n  l_ev = 1¼ in., l_eh = 1⅝ in.\n- Bolts: ¾-in.-dia. Group 120, thread condition N, standard holes (d_h = 13/16 in.,\n  A_b = 0.442 in.²). Bolts are in double shear through the two angle legs / beam web.\n- Loads: R_D = 10 kips, R_L = 30 kips.\n- Code basis: AISC 360-22 (Chapter J), loads combined per ASCE/SEI 7.\n\n## Find\nThe available shear strength of the connection (LRFD φR_n and ASD R_n/Ω), checking\nthe limit states of the angles (shear yielding, shear rupture, block shear), the\nshear-transfer/effective strength at the bolt holes in the beam web and girder web,\nand the coped-beam web limit states (flexural local web buckling, shear yielding,\nblock shear rupture). Confirm adequacy for R_u and R_a and state which limit state\ncontrols.",
 "has_figure": false,
 "stem": "II_A_4",
 "breadcrumb": "EXAMPLE II.A-4 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Double-Angle Connection (Coped Beam to Girder Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-4 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Double-Angle Connection (Coped Beam to Girder Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a (Eqs. J3-6a/c), §J4.2 (Eqs. J4-3/J4-4), §J4.3 (Eq. J4-5); coped-section flexure per Manual Part 9. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 10 kips, L = 30 kips → **LRFD Ru = 60.0 kips; ASD Ra = 40.0 kips**

2L5x3-1/2x1/4 SLBB × 8 1/2 in. (A572 Gr. 50); three rows of 3/4-in. Group 120-N bolts @ 3 in.; lev = 1 1/4 in.; beam-web leh = 1 5/8 in.; W18x50 (tw = 0.355 in.) coped 2 × 4 in. (e = 4.50 in.); girder W21x62 (tw = 0.400 in.). Effective hole = 7/8 in.

### 2. Bolt Groups

**Beam-web side (3 bolts, double shear):** per-bolt effective strength = min[bolt shear 35.8; web bearing 31.1; angle-pair bearing 43.9; bottom-bolt angle tearout 24.7] →
Group: **LRFD 2(31.1) + 24.7 = 86.9 kips ≥ 60 ✓; ASD 2(20.7) + 16.5 = 57.9 kips ≥ 40 ✓**

**Girder side (6 bolts, single shear):** min[17.9; angle bearing 21.9; bottom-bolt tearout 12.3] →
Group: **LRFD 4(17.9) + 2(12.3) = 96.2 kips ✓; ASD 64.2 kips ✓**

### 3. Angle Limit States (pair, t = 1/4 in.)

Shear yielding 0.6(50)(4.25) = 128 kips → 128/85.0 ✓; shear rupture (Anv = 2.94 in.²) φRn = 85.9/57.3 ✓; block shear φRn = 93.8/62.6 ✓.

### 4. Coped-Beam Limit States

- **Block shear of the web at the bolt line (Eq. J4-5, Ubs = 1.0):** Agv = 2.57 in.², Anv = 1.80 in.², Ant = 0.42 in.² → Rn = 70.1 + 27.4 = 97.5 kips (≤ 105) → **φRn = 73.1 kips ≥ 60 ✓; Rn/Ω = 48.8 ≥ 40 ✓** ← **governing limit state**
- Flexure of the coped section (e = 4.50 in.): Mu = 270 kip-in. ≪ φMn ≈ 1,050 kip-in. (Snet ≈ 23.4 in.³; buckling non-critical, c/ho = 0.25) ✓
- Web shear through the reduced depth: 0.6(50)(16.0 × 0.355) = 170 kips ✓

### 5. Conclusion

The connection is **adequate** for 60.0 kips (LRFD) / 40.0 kips (ASD); the governing limit state is **block shear rupture of the coped beam web** at 82% utilization (LRFD), followed by the double-shear bolt group limited by web bearing. All angle limit states and the coped-section flexural checks carry comfortable margins.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
