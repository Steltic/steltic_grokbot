<!-- chunk_id: F.5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.5",
 "example_family": "F.5",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F6",
  "F6.1"
 ],
 "eqs": [
  "F6-1",
  "F6-2"
 ],
 "tables": [],
 "title": "W-Shape Bent About Its Minor Axis",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.5 — W-Shape Bent About Its Minor Axis",
 "question": "# F.5 — I-shaped beam in minor-axis bending  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported W-shape beam is loaded **about its minor (y) axis** by a uniformly\ndistributed load and is laterally braced only at its two ends. Select the lightest\nW-shape such that the member has adequate minor-axis flexural strength and the live-load\ndeflection does not exceed L/240. Report the available flexural strength (LRFD and ASD).\n(This is an uncommon design case used to illustrate minor-axis bending of an I-shape.)\n\n## Given\n- Material: ASTM A992/A992M (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, span L = 15 ft, bent about the minor axis,\n  braced only at the ends.\n- Loads (service, uniformly distributed): dead wD = 0.667 kip/ft, live wL = 2.0 kip/ft.\n- Serviceability: limit live-load deflection to L/240.\n- Member / section: to be selected (design problem).\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nSelect the lightest adequate W-shape and report φ_b M_n (LRFD) and M_n/Ω_b (ASD) for\nminor-axis bending.",
 "has_figure": false,
 "stem": "F_5",
 "breadcrumb": "EXAMPLE F.5 · AISC 360-22 Ch.F (beam flexure) · §F6 §F6.1 · W-Shape Bent About Its Minor Axis",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.5 · AISC 360-22 Ch.F (beam flexure) · §F6 §F6.1 · W-Shape Bent About Its Minor Axis

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F6 (I-shapes bent about the minor axis): Eq. F6-1 (yielding); FLB (Eqs. F6-2/3/4) not triggered (compact flange); LTB does not apply to minor-axis bending. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 15 ft, minor-axis bending; wD = 0.667 kip/ft, wL = 2.0 kip/ft:

- **LRFD:** wu = 1.2(0.667) + 1.6(2.0) = 4.00 kip/ft → Mu = 4.00(15)²/8 = **113 kip-ft**
- **ASD:** wa = 2.67 kip/ft → Ma = 2.67(15)²/8 = **75.0 kip-ft**

### 2. Serviceability Requirement (Δ_LL ≤ L/240 = 0.75 in.)

Iy,req = 5wL L⁴/(384EΔ) = 5(2.0/12)(180)⁴/[384(29,000)(0.75)] = **105 in.⁴**

### 3. Selection — W12x58 (A992)

Zy = 32.5 in.³; Sy = 21.4 in.³; Iy = 107 in.⁴ ≥ 105 ✓; bf/2tf = 7.82 ≤ λpf = 0.38√(E/Fy) = 9.15 → **compact flange** (FLB does not apply). LTB is not a limit state for minor-axis bending, so end-only bracing carries no penalty.

### 4. Yielding — §F6.1, Eq. F6-1

> Mn = Mp = FyZy ≤ 1.6FySy

FyZy = 50(32.5) = 1,630 kip-in.; 1.6FySy = 1.6(50)(21.4) = 1,710 kip-in. → **Mn = 1,630 kip-in. = 135 kip-ft**

### 5. Available Flexural Strength

- **LRFD:** φbMn = 0.90(135) = **122 kip-ft** ≥ 113 kip-ft ✓ (utilization 0.92)
- **ASD:** Mn/Ωb = 135/1.67 = **81.1 kip-ft** ≥ 75.0 kip-ft ✓ (utilization 0.92)

### 6. Conclusion

**Select W12x58 (ASTM A992).** For minor-axis bending the governing limit state is **yielding** (Eq. F6-1, with the 1.6FySy cap not controlling for this shape); LTB is inapplicable and the compact flanges exclude FLB. The selection also satisfies the L/240 live-load deflection limit (Iy = 107 ≥ 105 in.⁴), which nearly governs alongside strength.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
