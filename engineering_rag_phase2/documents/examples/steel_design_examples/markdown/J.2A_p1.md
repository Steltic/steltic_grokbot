<!-- chunk_id: J.2A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.2A",
 "example_family": "J.2",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J2.4"
 ],
 "eqs": [],
 "tables": [
  "J2.5"
 ],
 "title": "Fillet Weld Loaded at an Angle (Required Length)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.2A — Fillet Weld Loaded at an Angle (Required Length)",
 "question": "# J.2A — Fillet Weld Loaded at an Angle  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA gusset plate is connected to a beam flange by a two-sided fillet weld (one weld\nalong each face of the gusset). The connection transfers a concentrated force whose\nline of action makes an angle of 60° with the longitudinal axis of the welds. The\nfillet weld size is 5/16 in. and 70-ksi (E70XX) electrodes are used. The beam flange\nand gusset plate thicknesses and lengths have already been sized; assume the flange\nthickness exceeds 3/4 in. so that the 5/16-in. weld satisfies the minimum-size rule.\n\nThe connection carries a service dead load of 50 kips and a service live load of\n150 kips. Determine the required total weld length, l (rounded up to a practical\nwhole inch), based on weld-metal shear rupture, for both LRFD and ASD.\n\n## Given\n- Material: E70XX electrodes (FEXX = 70 ksi); members already sized (A992 / A572 Gr. 50).\n- Geometry: two-sided fillet weld, 5/16-in. leg; load at θ = 60° to the weld axis.\n- Loads: PD = 50 kips, PL = 150 kips.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nThe required fillet weld length l, using the directional strength increase factor.",
 "has_figure": false,
 "stem": "J_2A",
 "breadcrumb": "EXAMPLE J.2A · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J2.4 · Fillet Weld Loaded at an Angle (Required Length)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.2A · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J2.4 · Fillet Weld Loaded at an Angle (Required Length)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J2.4/Table J2.5: Fnw = 0.60FEXX with the directional strength increase (1.0 + 0.50sin^1.5θ); φ = 0.75, Ω = 2.00. Per the RAG extract provided.

---

### 1. Required Strength

P: D = 50 kips, L = 150 kips → **LRFD Pu = 300 kips; ASD Pa = 200 kips**, at θ = 60° to the weld axis.

### 2. Weld Strength per Inch (two-sided 5/16-in. E70 fillets)

Directional factor: 1 + 0.5sin^1.5(60°) = 1 + 0.5(0.866)^1.5 = **1.40**

- **LRFD:** 2(1.392)(5)(1.40) = **19.5 kip/in.**
- **ASD:** 2(0.928)(5)(1.40) = **13.0 kip/in.**

### 3. Required Length

- **LRFD:** l = 300/19.5 = 15.4 in. → **use l = 16 in.**
- **ASD:** l = 200/13.0 = 15.4 in. → **use l = 16 in.**

### 4. Conclusion

A **16-in.-long, two-sided 5/16-in. E70 fillet weld** transfers the 300-kip (LRFD) / 200-kip (ASD) force applied at 60° to the weld axis. The directional strength increase (40% at this angle) reduces the required length from 22 in. (if neglected) to 16 in. — a substantial economy available under §J2.4. The 5/16-in. size satisfies Table J2.4 for the >3/4-in. flange, and base-metal checks are satisfied by the pre-sized members.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
