<!-- chunk_id: J.2B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.2B",
 "example_family": "J.2",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J2.4",
  "J4.2"
 ],
 "eqs": [],
 "tables": [
  "J2.5"
 ],
 "title": "PJP Groove Weld Loaded at an Angle (Required Length)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.2B — PJP Groove Weld Loaded at an Angle (Required Length)",
 "question": "# J.2B — Partial-Joint-Penetration (PJP) Groove Weld Loaded at an Angle  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA gusset plate is joined to the flange of a W18×86 beam by a two-sided partial-joint-\npenetration (PJP) groove weld (one weld on each side of the gusset). Each PJP groove\nweld has an effective throat (groove weld size) of 1/4 in. The connection transfers a\nconcentrated force whose line of action makes an angle of 60° with the longitudinal\naxis of the welds. The gusset plate is ASTM A572/A572M Grade 50 and is 3/4 in. thick;\nthe beam is ASTM A992/A992M; 70-ksi (E70XX) electrodes are used. The beam flange\nthickness is tf = 0.770 in.\n\nThe connection carries a service dead load of 50 kips and a service live load of\n150 kips. Determine the required weld length, l, considering both the available weld\nstrength and the available base-metal strength at the PJP weld, for LRFD and ASD.\n\n## Given\n- Material: gusset A572/A572M Gr. 50 (Fy = 50, Fu = 65 ksi); beam A992 (Fy = 50,\n  Fu = 65 ksi); E70XX (FEXX = 70 ksi).\n- Geometry: two-sided PJP groove weld, 1/4-in. effective throat each; load at θ = 60°;\n  gusset 3/4 in. thick; W18×86 flange tf = 0.770 in.\n- Loads: PD = 50 kips, PL = 150 kips.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nRequired PJP groove weld length l, governed by the lesser of weld-metal strength and\nbase-metal strength (using the Manual combined shear/tension interaction at θ = 60°).",
 "has_figure": false,
 "stem": "J_2B",
 "breadcrumb": "EXAMPLE J.2B · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J2.4 §J4.2 · PJP Groove Weld Loaded at an Angle (Required Length)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.2B · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J2.4 §J4.2 · PJP Groove Weld Loaded at an Angle (Required Length)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J2.4/Table J2.5: PJP groove welds in shear — Fnw = 0.60FEXX on the effective throat, φ = 0.75/Ω = 2.00, with **no directional strength increase** (the (1 + 0.5sin^1.5θ) factor applies to fillet welds only); base metal per §J4.2. Per the RAG extract provided.

---

### 1. Required Strength

P: D = 50 kips, L = 150 kips → **LRFD Pu = 300 kips; ASD Pa = 200 kips**, at 60° to the weld axis.

Two-sided PJP groove welds, effective throat E = 1/4 in. each; gusset 3/4 in. (A572 Gr. 50); W18x86 flange tf = 0.770 in.

### 2. Weld Metal (shear on the effective area)

- **LRFD:** φrn = 0.75(0.6 × 70)(2 × 0.25) = **15.8 kip/in.**
- **ASD:** rn/Ω = (0.6 × 70)(2 × 0.25)/2.00 = **10.5 kip/in.**

Required length: l = 300/15.8 = 19.0 in. (LRFD); l = 200/10.5 = 19.0 in. (ASD)

### 3. Base Metal at the Weld — §J4.2

Gusset (t = 3/4 in.) shear at the fused interface: φrn = 0.75(0.6)(65)(0.75) = 21.9 kip/in.; shear yielding 1.00(0.6)(50)(0.75) = 22.5 kip/in. — both exceed the 15.8-kip/in. weld value; flange (0.770 in.) similar → **weld metal governs.**

### 4. Required Length

**Use l = 20 in.** of two-sided 1/4-in.-throat PJP groove weld (LRFD and ASD give the same requirement).

### 5. Conclusion

The PJP option requires **20 in.** versus 16 in. for the 5/16-in. fillet of Example J.2A, despite similar deposited metal: PJP groove welds receive **no directional strength increase**, so the 60° load angle gives them no benefit. The comparison illustrates why fillet welds are usually the economical choice for inclined gusset forces, while PJPs may still be preferred for fit-up or appearance. Base-metal strength does not control.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
