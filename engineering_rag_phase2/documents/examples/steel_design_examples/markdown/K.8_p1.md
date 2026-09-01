<!-- chunk_id: K.8_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.8",
 "example_family": "K.8",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "K"
 ],
 "eqs": [],
 "tables": [],
 "title": "Transverse Load on a Longitudinal Plate Welded to a Round HSS",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.8 — Transverse Load on a Longitudinal Plate Welded to a Round HSS",
 "question": "# K.8 — Longitudinal plate loaded perpendicular to the axis of a round HSS  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA round HSS member is used as a tension chord. A longitudinal gusset plate is welded\nflat onto the side of the round HSS (the plate lies in a plane containing the HSS\naxis) and is loaded by a transverse force applied perpendicular to the HSS axis—for\nexample, a hanger or web member pulling on the plate. Verify the local strength of the\nround HSS wall under this transverse load (the limit state of HSS plastification),\nand determine the minimum end distance from the plate to the end of the HSS.\n\nThe chord is an ASTM A500 Grade C HSS6.000×0.375 carrying axial tension; the\nconnecting surface is therefore in tension. The plate is ASTM A572 Grade 50, 1/4 in.\nthick, welded to the HSS along a contact length of lb = 4 in. measured parallel to the\nHSS axis, with the transverse load applied at θ = 90° to the chord axis.\n\n## Given\n- Material: chord ASTM A500 Gr. C (Fy = 50 ksi, Fu = 62 ksi); plate ASTM A572 Gr. 50\n  (Fy = 50 ksi, Fu = 65 ksi).\n- Chord HSS6.000×0.375: D = 6.00 in., design wall t = 0.349 in., D/t = 17.2.\n- Plate: thickness Bb = 1/4 in.; bearing length along the HSS axis lb = 4 in.;\n  load angle θ = 90°.\n- Chord connecting surface is in tension (axial tension chord).\n- Transverse service loads: dead PD = 4 kips, live PL = 12 kips.\n- Code basis: AISC 360 Chapter K (+ ASCE/SEI 7 for the load combinations).\n\n## Find\nThe required transverse load (LRFD and ASD); confirmation that the connection is\nwithin the Table K2.1A limits of applicability; the available strength of the round\nHSS wall for the limit state of HSS plastification (Table K2.1, Eq. K2-2a); and the\nminimum end distance (§K1.4, Eq. K1-8). State whether the chord is adequate.",
 "has_figure": false,
 "stem": "K_8",
 "breadcrumb": "EXAMPLE K.8 · AISC 360-22 Ch.K (HSS connection) · §K · Transverse Load on a Longitudinal Plate Welded to a Round HSS",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.8 · AISC 360-22 Ch.K (HSS connection) · §K · Transverse Load on a Longitudinal Plate Welded to a Round HSS

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter K (round-HSS plastification under a longitudinal plate loaded transverse to the chord): Rn·sinθ = 5.5Fyt²(1 + 0.25lb/D)Qf; φ = 0.90, Ω = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

P: D = 4 kips, L = 12 kips → **LRFD Pu = 24.0 kips; ASD Pa = 16.0 kips**, applied at θ = 90° to the chord axis through the 1/4-in. plate (contact length lb = 4 in.).

### 2. HSS Wall Plastification

HSS6.000x0.375 (t = 0.349 in., D = 6.00 in., Fy = 50 ksi). The connecting surface is in **tension** → the chord-stress interaction factor Qf = **1.0**.

Rn = 5.5Fyt²(1 + 0.25lb/D)Qf/sinθ = 5.5(50)(0.349)²(1 + 0.25 × 4/6)(1.0) = 33.5(1.17) = **39.1 kips**

- **LRFD:** φRn = 0.90(39.1) = **35.2 kips ≥ 24.0 ✓** (utilization 0.68)
- **ASD:** Rn/Ω = 39.1/1.67 = **23.4 kips ≥ 16.0 ✓** (utilization 0.68)

### 3. Minimum End Distance

To develop the full plastification yield-line pattern, the plate must be set back from the open end of the HSS by at least the distance required for the wall mechanism — **end distance ≥ D = 6 in.**; closer placements require a reduced strength or an end cap.

### 4. Welds and Plate

The 1/4-in. plate and its longitudinal fillet welds along lb = 4 in. (two lines) develop the 24-kip force at modest weld sizes (3/16-in. fillets give 2 × 1.392 × 3 × 4 = 33.4 kips ≥ 24.0 ✓), and the plate's tensile capacity 0.9(50)(1.0) = 45 kips/in.-width basis is ample ✓.

### 5. Conclusion

The 1/4-in. longitudinal plate on the HSS6.000x0.375 tension chord can deliver **35.2 kips (LRFD) / 23.4 kips (ASD)** before the round wall plastifies — comfortably above the 24/16-kip demands (68% utilized) — provided the plate is at least **6 in. (one diameter)** from the member end. Because the chord is in tension, no Qf reduction applies; a compression chord would require re-evaluation.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
