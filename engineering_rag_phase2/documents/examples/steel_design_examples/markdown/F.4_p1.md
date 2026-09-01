<!-- chunk_id: F.4_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.4",
 "example_family": "F.4",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2.1",
  "F1"
 ],
 "eqs": [
  "F2-1"
 ],
 "tables": [],
 "title": "W-Shape Selection with Deflection Limit, Continuously Braced",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.4 — W-Shape Selection with Deflection Limit, Continuously Braced",
 "question": "# F.4 — W-shape beam selected by required moment of inertia (major-axis)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect the lightest available rolled W-shape to carry a uniformly distributed load on a\nsimply supported, single-span beam. The beam is **continuously braced** against\nlateral-torsional buckling along its full length. In addition to having adequate flexural\nstrength, the selected section must keep the live-load deflection at or below 1.00 in.\nDetermine the required member and confirm its available flexural strength in both LRFD\nand ASD.\n\n## Given\n- Material: ASTM A992/A992M (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, span L = 30 ft, continuously (laterally) braced.\n- Loads (service, uniformly distributed): dead wD = 0.8 kip/ft, live wL = 2.0 kip/ft.\n- Serviceability: limit live-load midspan deflection to Δ_allow = 1.00 in.\n- Member / section: to be selected (design problem).\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nSelect the lightest W-shape that satisfies both the strength requirement and the\n1.00-in. live-load deflection limit, and report φ_b M_n (LRFD) and M_n/Ω_b (ASD).",
 "has_figure": false,
 "stem": "F_4",
 "breadcrumb": "EXAMPLE F.4 · AISC 360-22 Ch.F (beam flexure) · §F2.1 §F1 · W-Shape Selection with Deflection Limit, Continuously Braced",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.4 · AISC 360-22 Ch.F (beam flexure) · §F2.1 §F1 · W-Shape Selection with Deflection Limit, Continuously Braced

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2.1 (Eq. F2-1; LTB precluded by continuous bracing). φb = 0.90, Ωb = 1.67 (§F1). Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 30 ft; wD = 0.8 kip/ft, wL = 2.0 kip/ft:

- **LRFD:** wu = 1.2(0.8) + 1.6(2.0) = 4.16 kip/ft → Mu = 4.16(30)²/8 = **468 kip-ft**
- **ASD:** wa = 2.8 kip/ft → Ma = 2.8(30)²/8 = **315 kip-ft**

### 2. Serviceability Requirement (Δ_LL ≤ 1.00 in.)

I_req = 5wL L⁴/(384EΔ) = 5(2.0/12)(360)⁴/[384(29,000)(1.00)] = **1,260 in.⁴**

### 3. Selection — W24x55 (A992)

Zx = 134 in.³; Ix = 1,350 in.⁴ ≥ 1,260 in.⁴ ✓; compact at Fy = 50 ksi (bf/2tf = 6.94, h/tw = 54.6 within Table B4.1b limits).

Lighter/shallower alternatives fail the deflection limit (e.g., W21x55: Ix = 1,140 in.⁴ < 1,260 in.⁴).

### 4. Flexural Strength — Eq. F2-1

Mn = Mp = FyZx = 50(134) = 6,700 kip-in. = **558 kip-ft**

- **LRFD:** φbMn = 0.90(558) = **502 kip-ft** ≥ 468 kip-ft ✓ (utilization 0.93)
- **ASD:** Mn/Ωb = 558/1.67 = **334 kip-ft** ≥ 315 kip-ft ✓ (utilization 0.94)

### 5. Deflection Check

Δ_LL = 1.00(1,260/1,350) = **0.93 in. ≤ 1.00 in. ✓**

### 6. Conclusion

**Select W24x55 (ASTM A992).** With full lateral bracing the member reaches its plastic moment (Eq. F2-1), providing φbMn = 502 kip-ft (LRFD) and Mn/Ωb = 334 kip-ft (ASD) against demands of 468 / 315 kip-ft, and limiting the live-load deflection to 0.93 in. Both strength (utilization ≈ 0.93–0.94) and stiffness requirements are met by the lightest qualifying W-shape.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
