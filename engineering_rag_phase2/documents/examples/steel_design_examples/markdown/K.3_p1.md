<!-- chunk_id: K.3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.3",
 "example_family": "K.3",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "J2.4"
 ],
 "eqs": [],
 "tables": [],
 "title": "Double-Angle Connection of a Heavy Beam to an HSS Column Face",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.3 — Double-Angle Connection of a Heavy Beam to an HSS Column Face",
 "question": "# K.3 — Double-Angle Connection to an HSS Column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nDesign a bolted/welded double-angle (clip-angle) simple shear connection that frames a\nheavy wide-flange beam into the face of a square HSS column. The pair of angles is welded\nto the column face and bolted (in double shear) to the supported beam web. The beam is\ncoped at the bottom flange only (for erection clearance), so coped-web limit states of the\nbeam at the top flange do not apply.\n\nThe supported beam is an ASTM A992/A992M W36×231. The column is an ASTM A500/A500M Grade C\nHSS14×14×1/2. The clip angles are ASTM A572/A572M Grade 50. Use 70-ksi (E70XX) electrodes,\n3/4-in.-diameter Group 120 bolts (thread condition N) in standard holes at s = 3 in. with a\nvertical edge distance l_ev = 1-1/4 in.\n\nSelect the bolt rows, angle size/length/thickness, and weld size, and verify the connection\nfor the following service vertical shear (beam end reaction):\n\n  Dead load   P_D = 37.5 kips\n  Live load   P_L = 113 kips\n\n## Given\n- Materials: beam ASTM A992 (F_y = 50 ksi, F_u = 65 ksi); column ASTM A500 Grade C\n  (F_y = 50 ksi, F_u = 62 ksi); angles ASTM A572 Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n  Electrodes E70XX.\n- Beam W36×231: t_w = 0.760 in., T = 31-3/8 in.\n- Column HSS14×14×1/2: design wall t = 0.465 in., B = 14.0 in., workable flat ≈ 11-3/4 in.\n- Bolts: 3/4-in. Group 120 (N), standard holes (d_h = 13/16 in.), s = 3 in., l_ev = 1-1/4 in.,\n  double shear (one line through both angles and the beam web).\n- Code basis: AISC 360-22 (Chapter J); ASCE/SEI 7 load combinations.\n\n## Find\nChoose a bolt layout and angles (size, thickness, length); verify the available angle strength\n(shear yielding, shear rupture, block shear), the available shear-transfer strength at the bolt\nholes (least of bolt double shear, angle bearing/tearout ×2, and beam-web bearing/tearout), and\nthe weld strength; confirm minimum support thickness, minimum angle thickness/length, and that\nthe connection fits the HSS workable flat. Compare available to required strength (LRFD and ASD).",
 "has_figure": false,
 "stem": "K_3",
 "breadcrumb": "EXAMPLE K.3 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Double-Angle Connection of a Heavy Beam to an HSS Column Face",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.3 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Double-Angle Connection of a Heavy Beam to an HSS Column Face

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/§J3.11a, §J4.2/§J4.3, §J2.4 (eccentric weld groups), HSS-wall development (3.09D/Fu). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 37.5 kips, L = 113 kips → **LRFD Ru = 226 kips; ASD Ra = 151 kips**

W36x231 (tw = 0.760 in., coped bottom flange only — top-flange coped-web limit states N/A) to HSS14x14x1/2 (t = 0.465 in., Fu = 62 ksi).

### 2. Selection

**2L4x3-1/2x3/8 SLBB × 23 1/2 in. (A572 Gr. 50); eight rows of 3/4-in. Group 120-N bolts @ 3 in. (double shear) to the beam web; 5/16-in. E70 fillet welds (vertical, with top returns) to the HSS face.**

### 3. Bolt Group (8 bolts, double shear)

Per bolt: min[35.8 bolt shear; beam-web bearing 66.7; angle-pair bearing (Σt = 0.75) 65.8; bottom-bolt angle tearout 37.0] →
**LRFD: 7(35.8) + 35.8 ≈ 286 kips ≥ 226 ✓; ASD: 191 kips ≥ 151 ✓**

### 4. Welds to the HSS Face

Per weld line (each angle carries R/2 = 113 kips at ex ≈ 3 in.):
fv = 113/23.5 = 4.81 kip/in.; fb = 6(113)(3)/(23.5)² = 3.68 kip/in. → resultant = **6.06 kip/in. ≤ 1.392(5) = 6.96 ✓** (LRFD, 87%); ASD 4.04 ≤ 4.64 ✓

**HSS wall development:** each weld line one-sided locally: 3.09D/Fu = 3.09(5)/62 = **0.25 in. ≤ 0.465 in. ✓**; the 1/2-in. wall also precludes face-plastification concerns at this shear-dominant loading.

### 5. Angle Limit States (pair)

Shear yielding 0.6(50)(17.6) = 529 kips ✓; shear rupture φ = 362 ✓; block shear φ = 378 ✓ — all ≥ 226/151 with wide margins.

### 6. Conclusion

The selected detail — **2L4x3-1/2x3/8 × 23 1/2 in. with eight 3/4-in. Group 120-N bolts and 5/16-in. fillets to the HSS14x14x1/2 face** — is **adequate** for the 226-kip (LRFD) / 151-kip (ASD) reaction. The welds govern at ≈87% utilization, with the bolt group at 80%; the heavy 1/2-in. HSS wall comfortably develops the welds. The bottom-flange cope serves erection only and introduces no governing limit state.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
