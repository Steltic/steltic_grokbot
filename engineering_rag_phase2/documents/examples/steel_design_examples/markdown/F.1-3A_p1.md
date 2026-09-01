<!-- chunk_id: F.1-3A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.1-3A",
 "example_family": "F.1-3",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2",
  "F1"
 ],
 "eqs": [
  "F2-3",
  "F2-4",
  "F2-5",
  "F2-6",
  "F1-1"
 ],
 "tables": [],
 "title": "W18x50 Flexural Check, Braced at Midspan",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.1-3A — W18x50 Flexural Check, Braced at Midspan",
 "question": "# F.1-3A — W18x50 flexural check, braced at midspan  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W18x50 of ASTM A992/A992M steel (Fy = 50 ksi) is a simply supported beam spanning 35 ft, carrying\nuniformly distributed service loads of 0.45 kip/ft dead and 0.75 kip/ft live over the full span.\nThe beam is braced against lateral displacement and twist only at the supports and at midspan,\ngiving two equal unbraced segments of 17.5 ft. Determine the available flexural strength of the\nW18x50 (LRFD and ASD), accounting for the moment-gradient factor Cb, and verify adequacy.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Section: W18x50; Zx = 101 in.^3, Sx = 88.9 in.^3, ry = 1.65 in., rts = 1.98 in., J = 1.24 in.^4,\n  ho = 17.4 in. (compact at Fy = 50 ksi).\n- Geometry / span: simple span L = 35 ft; lateral/torsional braces at ends and midspan,\n  Lb = 17.5 ft.\n- Loads (service, uniform): wD = 0.45 kip/ft, wL = 0.75 kip/ft.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe available flexural strength (phi_b*Mn for LRFD, Mn/Omega_b for ASD), including the controlling\nlateral-torsional buckling limit state with Cb, and confirm it exceeds the required strength.",
 "has_figure": false,
 "stem": "F_1_3A",
 "breadcrumb": "EXAMPLE F.1-3A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · W18x50 Flexural Check, Braced at Midspan",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.1-3A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · W18x50 Flexural Check, Braced at Midspan

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 (Eqs. F2-3, F2-4, F2-5, F2-6) with Cb per §F1 (Eq. F1-1). φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Mu = 1.74(35)²/8 = **266 kip-ft**
- **ASD:** Ma = 1.20(35)²/8 = **184 kip-ft**

### 2. Segment Classification

W18x50 (A992, compact): Lp = 5.83 ft (Eq. F2-5); Lr = 17.0 ft (Eq. F2-6).

Lb = 35/2 = **17.5 ft > Lr = 17.0 ft → elastic LTB, Eqs. F2-3/F2-4.**

### 3. Moment Gradient Factor

Each half-span segment runs from a support (M = 0) to midspan (Mmax) under uniform load; per Eq. F1-1, **Cb = 1.30**.

### 4. Elastic LTB — Eqs. F2-4, F2-3

Lb/rts = 17.5(12)/1.98 = 106; Jc/(Sxho) = 1.24/[88.9(17.4)] = 8.02 × 10⁻⁴

Fcr = Cbπ²E/(Lb/rts)² × √[1 + 0.078(Jc/(Sxho))(Lb/rts)²]
= 1.30π²(29,000)/(106)² × √[1 + 0.078(8.02 × 10⁻⁴)(106)²] = 33.1√1.70 = **43.2 ksi** (Eq. F2-4)

Mn = FcrSx = 43.2(88.9) = 3,840 kip-in. = **320 kip-ft ≤ Mp = 421 kip-ft ✓** (Eq. F2-3)

### 5. Available Flexural Strength

- **LRFD:** φbMn = 0.90(320) = **288 kip-ft** ≥ 266 kip-ft ✓ (utilization 0.93)
- **ASD:** Mn/Ωb = 320/1.67 = **192 kip-ft** ≥ 184 kip-ft ✓ (utilization 0.96)

### 6. Conclusion

With bracing only at the supports and midspan, the 17.5-ft unbraced length slightly exceeds Lr, so the W18x50 is governed by **elastic lateral-torsional buckling** (Eqs. F2-3/F2-4 with Cb = 1.30). Available strengths of 288 kip-ft (LRFD) and 192 kip-ft (ASD) still exceed the required 266 / 184 kip-ft — **adequate**, though the ASD margin is only ~4%; any increase in load or loss of the midspan brace effectiveness would require re-evaluation.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
