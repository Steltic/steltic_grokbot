<!-- chunk_id: F.11B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.11B",
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
 "title": "Single-Angle Beam Braced at Ends and Midspan (Geometric-Axis Bending)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.11B — Single-Angle Beam Braced at Ends and Midspan (Geometric-Axis Bending)",
 "question": "# F.11B — Single-angle beam braced at ends and midspan (geometric-axis bending)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nUsing the AISC Specification directly, select an equal-leg single angle for a simply\nsupported, single-span beam carrying a uniformly distributed vertical load. The angle is\noriented with its vertical leg up so that the **toe is in compression**, it bends about the\n**geometric x-x axis**, there are no horizontal loads, and there is no deflection limit. The\nmember is braced at the ends and at midspan, with lateral-torsional restraint provided at\nthe midspan (point of maximum moment) and the ends only. Determine an adequate angle,\nidentify the governing limit state, and report φ_b M_n (LRFD) and M_n/Ω_b (ASD).\n\n## Given\n- Material: ASTM A572/A572M Grade 50 (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, L = 6 ft, braced at ends and midspan\n  (unbraced length L_b = 3 ft); geometric x-x bending; equal-leg angle, toe in compression.\n- Loads (service, uniformly distributed, vertical): dead wD = 0.05 kip/ft, live wL = 0.15 kip/ft.\n- C_b = 1.30 (for the end-to-midspan segment).\n- Member / section: to be selected.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nSelect an adequate equal-leg angle and report the governing limit state with φ_b M_n\n(LRFD) and M_n/Ω_b (ASD).",
 "has_figure": false,
 "stem": "F_11B",
 "breadcrumb": "EXAMPLE F.11B · AISC 360-22 Ch.F (beam flexure) · §F10 §F10.2 · Single-Angle Beam Braced at Ends and Midspan (Geometric-Axis Bending)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.11B · AISC 360-22 Ch.F (beam flexure) · §F10 §F10.2 · Single-Angle Beam Braced at Ends and Midspan (Geometric-Axis Bending)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F10: Eqs. F10-1, F10-2, F10-5a (with the §F10.2(2)(ii) 1.25 multiplier), F10-6; Table B4.1b Case 12. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

L = 6 ft simple span; braced at ends and midspan (Lb = 3 ft); wD = 0.05, wL = 0.15 kip/ft:

- **LRFD:** wu = 0.30 kip/ft → Mu = **1.35 kip-ft** (16.2 kip-in.)
- **ASD:** wa = 0.20 kip/ft → Ma = **0.90 kip-ft** (10.8 kip-in.)

### 2. Trial Member — L4x4x1/4 (A572 Gr. 50)

Geometric Sx = 1.03 in.³; b = 4.00 in.; t = 0.25 in.; Cb = 1.30 (end-to-midspan segment).

Per §F10.2(2)(ii) — lateral-torsional restraint at the point of maximum moment (midspan) — **Mcr = 1.25× Eq. F10-5a** and **My = full FySx** (the 0.80 geometric-axis penalty does not apply); likewise Sc = full Sx for leg local buckling.

My = FySx = 50(1.03) = **51.5 kip-in.**

### 3. Yielding — Eq. F10-1

Mn = 1.5My = 1.5(51.5) = **77.3 kip-in.**

### 4. Lateral-Torsional Buckling — Eqs. F10-5a (×1.25), F10-2

Lbt/b² = 36(0.25)/16 = 0.563 → √(1 + 0.88(0.563)²) − 1 = 0.131

Mcr = 1.25 × [0.58(29,000)(4.00)⁴(0.25)(1.30)/(36)²](0.131) = 1.25(141) = **176 kip-in.**

My/Mcr = 51.5/176 = 0.292 ≤ 1.0 → Eq. F10-2:

Mn = (1.92 − 1.17√0.292)(51.5) = (1.288)(51.5) = **66.3 kip-in.** ≤ 1.5My = 77.3 ✓

### 5. Leg Local Buckling — Eq. F10-6

b/t = 16; λp = 13.0 < 16 < λr = 21.9 (Table B4.1b Case 12) → noncompact:

Mn = FySc[2.43 − 1.72(b/t)√(Fy/E)] = 50(1.03)(1.287) = **66.3 kip-in.**

### 6. Available Flexural Strength

Governing: **LTB and leg local buckling are essentially coincident at Mn = 66.3 kip-in. = 5.53 kip-ft.**

- **LRFD:** φbMn = 0.90(66.3) = 59.7 kip-in. = **4.97 kip-ft** ≥ 1.35 kip-ft ✓
- **ASD:** Mn/Ωb = 66.3/1.67 = 39.7 kip-in. = **3.31 kip-ft** ≥ 0.90 kip-ft ✓

### 7. Conclusion

**Select L4x4x1/4 (A572 Gr. 50).** With midspan lateral-torsional restraint, §F10.2(2)(ii) permits the 1.25 Mcr enhancement and full My, raising the available strength about 34% over the ends-only-braced case (Example F.11A: 49.3 kip-in.). The governing limit state is leg local buckling/LTB at Mn = 66.3 kip-in., and the member is adequate with large margin (utilization ≈ 0.27).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
