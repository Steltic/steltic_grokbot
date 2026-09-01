<!-- chunk_id: II.A-20_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-20",
 "example_family": "II.A-20",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "F11"
 ],
 "eqs": [
  "J4-3",
  "J4-4"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "All-Bolted Single-Plate Shear Splice",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-20 — All-Bolted Single-Plate Shear Splice",
 "question": "# II.A-20 — All-Bolted Single-Plate Shear Splice  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nTwo ASTM A992/A992M beams (a W24×55 and a W24×68) are spliced end-to-end with a single\nshear plate bolted across the joint (see figures/IIA_20.png). The splice plate is an\nASTM A572/A572M Grade 50 PL⅜×8×1'-0″ (12 in. deep). On each side of the splice line the\nplate is bolted to the beam web with one vertical line of four ⅞-in.-diameter Group 120\nbolts (thread condition N) in standard holes at 3-in. spacing; the two bolt groups are\ne = 5 in. apart (their centroids), with vertical edge distance l_ev = 1½ in. and\nhorizontal edge distance l_eh = 1½ in. Because the splice is symmetrical, each bolt group\nresists the full shear R plus one-half of the eccentric moment, i.e. an eccentricity of\ne/2 = 2.50 in.\n\nThe beams carry service end reactions R_D = 10 kips and R_L = 30 kips across the splice.\n\nVerify the splice and identify the governing limit state.\n\n## Given\n- Material: beams ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); plate ASTM A572/A572M\n  Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n- Beams: W24×55 (t_w = 0.395 in.) and W24×68 (t_w = 0.415 in.).\n- Plate: PL⅜ × 8 in. × 12 in. deep; per side, 4 bolts ⅞-in.-dia. Group 120-N in standard\n  holes (d_h = 15/16 in., A_b = 0.601 in.²), s = 3 in., l_ev = l_eh = 1½ in.; bolt-group\n  eccentricity e/2 = 2.50 in.\n- Loads: R_D = 10 kips, R_L = 30 kips.\n- Code basis: AISC 360-22 (Chapters J and F); loads per ASCE/SEI 7.\n\n## Find\nThe available strength (LRFD φR_n, ASD R_n/Ω) of the splice, checking the eccentric\nbolt group (J3.7 bolt shear + J3.11a bearing/tearout), plate flexural yielding (F11.1)\nand flexural rupture, plate shear yielding/rupture (J4.2), and plate block shear (J4.3).\nConfirm adequacy and identify the governing limit state.",
 "has_figure": true,
 "stem": "II_A_20",
 "breadcrumb": "EXAMPLE II.A-20 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §F11 · All-Bolted Single-Plate Shear Splice",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-20 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §F11 · All-Bolted Single-Plate Shear Splice

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2 (Eqs. J4-3/J4-4), §J4.3; plate flexure per §F11 basis. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 10 kips, L = 30 kips → **LRFD Ru = 60.0 kips; ASD Ra = 40.0 kips**

Splice: PL3/8 × 8 × 12 (A572 Gr. 50); each side, four 7/8-in. Group 120-N bolts @ 3 in. (lev = leh = 1 1/2 in.); group centroids 5 in. apart → by symmetry each group resists R at **e/2 = 2.50 in.** Effective hole = 1.00 in.

### 2. Eccentric Bolt Groups (each side)

C (4 bolts @ 3 in., e = 2.50 in.) ≈ 3.0:

φRn = 3.0(0.75 × 54 × 0.601) = 3.0(24.3) = **72.9 kips ≥ 60.0 ✓**; Rn/Ω = 3.0(16.2) = **48.7 kips ≥ 40.0 ✓** (utilization 0.82 — **governing**)

Bearing/tearout: webs (0.395/0.415 in.) φ ≥ 40.4 kips/bolt; plate interior bearing φ = 38.4 kips/bolt; bottom-bolt plate tearout (lc = 1.03 in.) φ = 22.6 kips — slightly below the 24.3-kip bolt shear for one fastener; the group value with this substitution (≈71 kips LRFD) still exceeds the demand ✓.

### 3. Splice Plate

- Shear yielding (Eq. J4-3): 0.6(50)(4.50) = 135 kips → 135/90.0 ✓
- Shear rupture (Eq. J4-4): Anv = (12 − 4 × 1.0)(0.375) = 3.00 in.² → φRn = 87.8/58.5 ✓
- Flexure at the splice line: M = R(e/2) = 150 kip-in. (LRFD); φMn = 0.9(50)(13.5) = 608 kip-in. ✓ (net-section flexural rupture likewise non-critical)
- Block shear (Eq. J4-5): not governing ✓

### 4. Conclusion

The symmetric single-plate splice — **PL3/8 × 8 × 12 with four 7/8-in. Group 120-N bolts each side at e/2 = 2.5 in.** — is **adequate** for the 60-kip (LRFD) / 40-kip (ASD) shear. The eccentrically loaded bolt groups govern at ~82% utilization; all plate limit states have large margins. Because the splice is symmetric, each group sees only half the joint eccentricity, which is what makes the compact 4-bolt arrangement work.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-20 (from figures/IIA_20.png)

All-bolted single-plate shear splice between two beams (W24×55 and W24×68).

- **Splice plate:** PL⅜ × 8 in. × 1'-0" (12 in. deep, ⅜ in. thick).
- **Bolts (each side of the splice line):** one vertical line of **4 bolts**,
  ⅞-in. Group 120 (N), standard holes, 3 @ 3 in. = 9 in., l_ev = 1½ in.,
  l_eh = 1½ in.
- The two bolt groups (one per beam) are **e = 5 in. apart** (centroid to
  centroid); ½-in. gap at the splice line; **2½ in.** from the splice line to each
  bolt group. Each group resists the full shear R plus half the moment
  (**M = Re/2**, eccentricity e/2 = 2½ in.).
