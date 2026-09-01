<!-- chunk_id: II.A-17C_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-17C",
 "example_family": "II.A-17",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "B3.9",
  "J3.7",
  "J3.11",
  "J4.1",
  "J2.4"
 ],
 "eqs": [
  "J3-6b"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Single-Plate Connection: Structural Integrity Check (§B3.9)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-17C — Single-Plate Connection: Structural Integrity Check (§B3.9)",
 "question": "# II.A-17C — Single-Plate Connection — Structural Integrity Check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA conventional single-plate (\"shear tab\") shear connection joins the web of an\nASTM A992/A992M W16×50 beam to the flange of a column. The plate is a ¼-in.-thick\nASTM A572/A572M Grade 50 shear plate, 11½ in. long, attached to the supported beam\nwith a single vertical line of four ¾-in.-diameter Group 120 high-strength bolts in\nstandard holes (d_h = 13/16 in.), at a 3-in. pitch (3 spaces at 3 in. = 9 in.), and\nwelded to the support with a two-sided 3/16-in. fillet weld of 70-ksi electrodes. The\nplate horizontal edge distance is l_eh = 1½ in.; the beam-web horizontal edge distance\nis l_eh = 2½ in. (allowing for a possible ¼-in. beam underrun); the vertical edge\ndistance is 1¼ in. This connection was designed for a vertical shear of V_u = 49.6\nkips (LRFD) / V_a = 33.0 kips (ASD).\n\nThe applicable building code requires design for structural integrity. Verify the\nconnection for the structural-integrity provisions of AISC 360-22 Section B3.9, both\nas a beam/girder end connection (B3.9(b)) and as the end connection of a member\nbracing a column (B3.9(c)).\n\n## Given\n- Material: beam ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); plate ASTM A572/A572M\n  Grade 50 (F_y = 50 ksi, F_u = 65 ksi); 70-ksi weld electrodes.\n- Beam: W16×50 (t_w = 0.380 in.).\n- Plate: PL ¼ in. × 11½ in., two-sided 3/16-in. fillet weld to the support.\n- Bolts: four ¾-in.-dia. Group 120, standard holes (d_h = 13/16 in.), 3-in. pitch;\n  plate l_eh = 1½ in., beam-web l_eh = 2½ in. (with ¼-in. underrun), l_ev = 1¼ in.\n- Design shear (from the parent connection): V_u = 49.6 kips / V_a = 33.0 kips.\n- Code basis: AISC 360-22, Section B3.9 (structural integrity), evaluated\n  independently of, and not combined with, the ordinary strength checks.\n\n## Find\nUsing B3.9, determine (a) the minimum required axial tie strength for the beam end\nconnection and verify the connection's available tensile strength against it,\nconsidering all applicable tension limit states (bolt shear, bolt bearing/tearout,\nplate tensile yielding and rupture, plate and beam-web block shear, and weld), with\ninelastic deformation permitted; and (b) the maximum column axial force this\nconnection is able to brace under B3.9(c).",
 "has_figure": false,
 "stem": "II_A_17C",
 "breadcrumb": "EXAMPLE II.A-17C · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 §J4.1 §J2.4 · Single-Plate Connection: Structural Integrity Check (§B3.9)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-17C · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 §J4.1 §J2.4 · Single-Plate Connection: Structural Integrity Check (§B3.9)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §B3.9 (nominal strengths; checks independent of ordinary strength design; inelastic deformation permitted), with §J3.7/Table J3.2 (bolt shear), §J3.11 (bearing/tearout with deformation NOT a consideration, Eqs. J3-6b/d), §J4.1 (plate tension), §J2.4 (weld, transverse). Per the RAG extract provided.

---

### 1. Required Integrity Tie Force — §B3.9(b)

Parent design (Example II.A-17A): Vu = 49.6 kips / Va = 33.0 kips.

Tn,min = max[(2/3)Vu, Va, 10 kips] = max[33.1, 33.0, 10] = **33.1 kips**

### 2. Available Nominal Tensile Strength (least of the following)

Tie path: beam web → four 3/4-in. Group 120 bolts (shear) → PL1/4 × 11 1/2 (tension) → two-sided 3/16-in. weld (tension).

**(a) Bolt shear (§J3.7):** Rn = 4FnvAb = 4(54)(0.442) = **95.5 kips** ← **governs**

**(b) Bearing/tearout, deformation not a consideration (§B3.9 / Eqs. J3-6b, J3-6d):**
Plate (leh = 1 1/2 in.): tearout lc = 1.50 − (13/16)/2 = 1.09 in. → 1.5lctFu = 26.7 kips/bolt; bearing 3.0dtFu = 36.6 kips/bolt → group = 4(26.7) = **107 kips**
Beam web (leh = 2 1/2 in. incl. 1/4-in. underrun): lc = 2.09 in. → 1.5lctFu = 77.5 kips/bolt — not governing.

**(c) Plate tension (§J4.1):** yielding FyAg = 50(11.5 × 0.25) = 144 kips; rupture FuAn = 65[(11.5 − 4 × 0.875)(0.25)] = **130 kips**

**(d) Weld tension (§J2.4, transverse, ×1.5):** Rn = 1.5(0.6 × 70)(2 × 0.707 × 0.1875 × 11.5) = **192 kips**

**Controlling Tn = 95.5 kips ≥ 33.1 kips ✓ — §B3.9(b) satisfied** (utilization 0.35).

### 3. Column-Bracing Capacity — §B3.9(c)

Tn ≥ 0.01(2/3)Pu (LRFD) or 0.01Pa (ASD) →

- **LRFD:** Pu,max = 95.5(150) = **≈14,300 kips**; **ASD:** Pa,max = **≈9,550 kips**

### 4. Conclusion

The conventional shear tab of Example II.A-17A satisfies the structural-integrity provisions with large margin: its nominal tie capacity of **95.5 kips (governed by bolt shear)** is nearly three times the 33.1-kip requirement of §B3.9(b), and per §B3.9(c) it can act as the bracing-member end connection for columns with required strengths into the tens of thousands of kips. Single-plate connections are inherently robust tie elements; no modification is required.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
