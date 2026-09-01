<!-- chunk_id: F.11A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.11A",
 "example_family": "F.11",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F10",
  "F10.2"
 ],
 "eqs": [
  "F10-1",
  "F10-2",
  "F10-5a",
  "F10-6"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "Single-Angle Flexural Member, Braced at Ends Only",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.11A — Single-Angle Flexural Member, Braced at Ends Only",
 "question": "# F.11A — Single-angle flexural member, braced at ends only  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect a **single equal-leg angle** to carry a uniform gravity load over a **6 ft simple span**.\nThe angle is **ASTM A572/A572M Grade 50** (Fy = 50 ksi). It is **simply supported and laterally\nbraced at the end points only** (no continuous lateral-torsional restraint). The angle is oriented\nwith one leg vertical and the **toe of the horizontal leg in compression**, and it bends about its\n**geometric x-x axis**. There are no horizontal loads and no deflection limit.\n\nService uniform loads (acting vertically): dead load wD = 0.05 kip/ft, live load wL = 0.15 kip/ft.\nConservatively design by directly applying the AISC 360-22 Specification for single angles\n(geometric-axis bending, no lateral-torsional restraint). Verify a trial **L4×4×1/4** and report the\navailable flexural strength (LRFD and ASD), identifying the controlling limit state.\n\n## Given\n- Material: ASTM A572/A572M Grade 50; Fy = 50 ksi; E = 29,000 ksi.\n- Span / bracing: L = 6 ft, simply supported, braced at ends only; no lateral-torsional restraint;\n  geometric x-x axis bending; toe of leg in compression.\n- Loads (service, vertical): wD = 0.05 kip/ft; wL = 0.15 kip/ft.\n- Trial member: L4×4×1/4 (equal-leg); geometric Sx = 1.03 in.³; leg width b = 4.00 in.; t = 1/4 in.\n- Cb = 1.14 (uniformly loaded angle braced at ends, AISC Manual Table 3-1).\n- Code basis: AISC 360-22.\n\n## Find\nThe available flexural strength of the L4×4×1/4 (φbMn for LRFD and Mn/Ωb for ASD) about the\ngeometric x-x axis, and whether it is adequate for the factored/required moment.",
 "has_figure": false,
 "stem": "F_11A",
 "breadcrumb": "EXAMPLE F.11A · AISC 360-22 Ch.F (beam flexure) · §F10 §F10.2 · Single-Angle Flexural Member, Braced at Ends Only",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.11A · AISC 360-22 Ch.F (beam flexure) · §F10 §F10.2 · Single-Angle Flexural Member, Braced at Ends Only

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F10 (Single Angles): Eqs. F10-1, F10-2, F10-5a, F10-6; Table B4.1b Case 12. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = Lb = 6 ft; wD = 0.05 kip/ft, wL = 0.15 kip/ft:

- **LRFD:** wu = 1.2(0.05) + 1.6(0.15) = 0.30 kip/ft → Mu = 0.30(6)²/8 = **1.35 kip-ft** (16.2 kip-in.)
- **ASD:** wa = 0.20 kip/ft → Ma = **0.90 kip-ft** (10.8 kip-in.)

### 2. Trial Member — L4x4x1/4 (A572 Gr. 50)

Equal-leg angle bent about the geometric x-x axis, no lateral-torsional restraint, toe of the horizontal leg in compression; geometric Sx = 1.03 in.³; b = 4.00 in.; t = 0.25 in.; Cb = 1.14.

Per §F10.2(2)(i), for geometric-axis bending without LT restraint, **My = 0.80FySx(geom)** = 0.80(50)(1.03) = **41.2 kip-in.**, and Sc = 0.80Sx for leg local buckling.

### 3. Yielding — Eq. F10-1

Mn = 1.5My = 1.5(41.2) = **61.8 kip-in.**

### 4. Lateral-Torsional Buckling — Eqs. F10-5a, F10-2

Maximum compression at the toe → Eq. F10-5a:

Mcr = [0.58Eb⁴tCb/Lb²]·[√(1 + 0.88(Lbt/b²)²) − 1]
Lbt/b² = 72(0.25)/16 = 1.125 → √(1 + 0.88(1.125)²) − 1 = 1.454 − 1 = 0.454
Mcr = [0.58(29,000)(256)(0.25)(1.14)/72²](0.454) = (237)(0.454) = **107 kip-in.**

My/Mcr = 41.2/107 = 0.383 ≤ 1.0 → Eq. F10-2:

Mn = (1.92 − 1.17√0.383)(41.2) = (1.196)(41.2) = **49.3 kip-in.** ≤ 1.5My = 61.8 ✓ ← **governs**

### 5. Leg Local Buckling — Eq. F10-6

b/t = 16; λp = 0.54√(E/Fy) = 13.0 < 16 < λr = 0.91√(E/Fy) = 21.9 → noncompact:

Mn = FySc[2.43 − 1.72(b/t)√(Fy/E)] = 50(0.80 × 1.03)[2.43 − 1.72(16)(0.0415)] = 50(0.824)(1.287) = **53.0 kip-in.**

### 6. Available Flexural Strength

Governing limit state: **lateral-torsional buckling**, Mn = 49.3 kip-in. = 4.11 kip-ft.

- **LRFD:** φbMn = 0.90(49.3) = 44.3 kip-in. = **3.70 kip-ft** ≥ 1.35 kip-ft ✓ (utilization 0.37)
- **ASD:** Mn/Ωb = 49.3/1.67 = 29.5 kip-in. = **2.46 kip-ft** ≥ 0.90 kip-ft ✓ (utilization 0.37)

### 7. Conclusion

The L4x4x1/4 (A572 Gr. 50), braced at its ends only and bent about the geometric axis with the toe in compression, is governed by **lateral-torsional buckling** (Eq. F10-5a with the 0.80My geometric-axis adjustment), giving φbMn = 3.70 kip-ft and Mn/Ωb = 2.46 kip-ft — comfortably above the required 1.35 / 0.90 kip-ft. **The angle is adequate**; leg local buckling (53.0 kip-in.) and yielding (61.8 kip-in.) do not control.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
