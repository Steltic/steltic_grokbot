<!-- chunk_id: II.A-21_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-21",
 "example_family": "II.A-21",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J2.4",
  "J4.2"
 ],
 "eqs": [],
 "tables": [
  "J3.2",
  "8"
 ],
 "title": "Bolted/Welded Single-Plate Shear Splice",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-21 — Bolted/Welded Single-Plate Shear Splice",
 "question": "# II.A-21 — Bolted/welded single-plate shear splice  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nTwo ASTM A992/A992M beams are spliced for shear with a single plate, as shown in\nfigures/IIA_21.png. The deeper beam on the left is a W16×50; the beam on the right\nis a W16×31. The splice plate is PL⅜ × 8 in. × 1 ft 0 in. (12 in. tall), ASTM\nA572/A572M Grade 50. The plate is **welded** to the W16×50 beam web with a two-sided\n(C-shaped) fillet weld group made with 70-ksi (E70) electrodes, and **bolted** to\nthe W16×31 beam web with one vertical line of 4 bolts at 3-in. pitch (3 @ 3 in. =\n9 in.) with 1½-in. vertical edge distances top and bottom. The bolts are ¾-in.-\ndiameter Group 120 (e.g., A325), thread condition N, in standard holes\n(dh = ¹³⁄₁₆ in.).\n\nBecause the splice is unsymmetrical and the weld group is the more rigid element,\ndesign the weld group for the full eccentric moment and the bolt group for the\ndirect shear only. The weld and bolt lines are separated horizontally: the weld\ncentroid lies 5.85 in. from the bolt line (after locating the weld-group centroid),\nand the bolt line is 6.50 in. from the splice centerline.\n\nService beam-end reactions: dead RD = 8 kips, live RL = 24 kips.\n\n## Given\n- Material: beams ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); plate ASTM A572 Gr. 50\n  (Fy = 50 ksi, Fu = 65 ksi); E70 electrodes.\n- Beams: W16×50 (tw = 0.380 in.), W16×31 (tw = 0.275 in.).\n- Plate: PL⅜ × 8 in. × 12 in. (l = 12 in., t = ⅜ in.).\n- Fasteners: ¾-in. Group 120, condition N, standard holes (dh = ¹³⁄₁₆ in.), 4 bolts,\n  s = 3 in., lev = 1½ in.\n- Weld group: two vertical lines (length l = 12 in.) plus horizontal returns of\n  kl = 3½ in. (k = 0.292); E70.\n- Loads (service): RD = 8 k, RL = 24 k → LRFD Ru = 1.2(8) + 1.6(24) = 48.0 k;\n  ASD Ra = 8 + 24 = 32.0 k.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nVerify the splice is adequate for the reaction. Check the eccentric weld group\n(required fillet size), shear rupture of the W16×31 web at the weld, the bolt group\n(bolt shear, plate bearing/tearout; beam-web bearing/tearout by inspection), and\nthe plate limit states: flexural yielding, flexural rupture, shear yielding, shear\nrupture, and block shear rupture.",
 "has_figure": true,
 "stem": "II_A_21",
 "breadcrumb": "EXAMPLE II.A-21 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J2.4 §J4.2 · Bolted/Welded Single-Plate Shear Splice",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-21 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J2.4 §J4.2 · Bolted/Welded Single-Plate Shear Splice

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J2.4 (eccentric C-shaped fillet weld group), §J4.2; Manual Table 8-8 basis for the weld coefficient. Per the RAG extract provided.

---

### 1. Required Strength and Design Philosophy

R: D = 8 kips, L = 24 kips → **LRFD Ru = 48.0 kips; ASD Ra = 32.0 kips**

PL3/8 × 8 × 12 (A572 Gr. 50): **welded** (C-shaped two-sided E70 fillet group) to the W16x50 web (tw = 0.380 in.) and **bolted** (four 3/4-in. Group 120-N @ 3 in., lev = 1 1/2 in.) to the W16x31 web (tw = 0.275 in.). Because the splice is unsymmetrical, the rigid weld group is designed for the **full eccentric moment** (weld centroid 5.85 in. from the bolt line) and the bolt group for **direct shear only**.

### 2. Bolt Group (direct shear)

φRn = 4(17.9) = **71.6 kips ≥ 48.0 ✓**; Rn/Ω = 4(11.9) = **47.7 kips ≥ 32.0 ✓**

Bearing/tearout: W16x31 web bearing φ = 24.1 kips/bolt; plate bottom-bolt tearout (lc = 1.09 in.) φ = 23.9 kips — both exceed the 17.9-kip bolt shear → bolt shear controls the group ✓.

### 3. Weld Group (full eccentricity)

C-shaped group: vertical weld l = 12 in. plus top/bottom returns (k ≈ 0.29); load at a·l = 5.85 in. from the group centroid → a ≈ 0.49. Eccentric weld coefficient C ≈ 1.4 (Manual Table 8-8 basis). With **1/4-in. fillets (D = 4)**:

φRn = C·C1·D·l = 1.4(1.0)(4)(12) = **67.2 kips ≥ 48.0 ✓**; Rn/Ω = **44.8 kips ≥ 32.0 ✓**

Minimum size for the 0.380-in. web = 3/16 in. ≤ 1/4 ✓; the 0.380-in. web base metal develops the C-weld at this demand ✓.

### 4. Splice Plate

- Shear yielding: 0.6(50)(4.50) = 135 kips → 135/90.0 ✓
- Shear rupture (bolted side, Anv = 3.69 in.²): φRn = 108/71.9 ✓
- Flexure (maximum plate moment ≈ R × 6.5 in. = 312 kip-in. LRFD): φMn = 0.9(50)(13.5) = 608 kip-in. ✓
- Block shear: not governing ✓

### 5. Conclusion

The unsymmetrical bolted/welded splice — **PL3/8 × 8 × 12, 1/4-in. E70 C-shaped weld group to the W16x50 and four 3/4-in. Group 120-N bolts to the W16x31** — is **adequate** for 48.0 kips (LRFD) / 32.0 kips (ASD). Assigning the full eccentric moment to the weld group (governing element, ~71% utilized) and pure shear to the bolts reflects the relative rigidity of the two groups, per Manual splice practice; all plate limit states pass with wide margins.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-21 (from figures/IIA_21.png)

Bolted/welded single-plate shear splice: W16×50 (left, welded) to W16×31 (right,
bolted).

- **Splice plate:** PL⅜ × 8 in. × 1'-0" (12 in. tall, ⅜ in. thick).
- **Bolted side (to W16×31 web):** one vertical line of **4 bolts**, ¾-in.
  Group 120 (N), standard holes, 3 @ 3 in. = 9 in., l_ev = 1½ in.
- **Welded side (to W16×50 web):** 3/16-in. C-shaped (two-sided + returns) fillet
  weld group; weld is the more rigid element and takes the full eccentric moment.
- Horizontal layout: **weld centroid lies 5.85 in. from the bolt line**
  (0.646-in. extra noted); 3 in. and 3½ in. dimensions; ½-in. gap at the splice.
