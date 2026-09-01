<!-- chunk_id: F.7A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.7A",
 "example_family": "F.7",
 "chapter": "F",
 "topic": "HSS flexure",
 "clauses": [
  "F7",
  "F7.4"
 ],
 "eqs": [
  "F7-2",
  "F7-8",
  "F7-10",
  "F7-11"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "Rectangular HSS Beam Design (Noncompact Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.7A — Rectangular HSS Beam Design (Noncompact Flange)",
 "question": "# F.7A — Rectangular HSS beam selected for a noncompact-flange section  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect a rectangular HSS beam (strong-axis orientation) for a simply supported, single-span\nbeam carrying a uniformly distributed load. The beam is laterally braced at the end points\nonly, and the live-load deflection must not exceed L/240. The chosen section happens to have\na noncompact compression flange. Determine the required member and confirm its available\nflexural strength (LRFD and ASD) using the AISC 360-22 HSS flexural provisions.\n\n## Given\n- Material: ASTM A500/A500M Grade C (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, L = 21 ft, laterally braced at the ends only.\n- Loads (service, uniformly distributed): dead wD = 0.15 kip/ft, live wL = 0.40 kip/ft.\n- Serviceability: limit live-load deflection to L/240.\n- Member / section: to be selected (design problem); use a strong-axis rectangular HSS.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nSelect an adequate rectangular HSS satisfying both strength and the L/240 deflection limit,\nand report the governing limit state with φ_b M_n (LRFD) and M_n/Ω_b (ASD).",
 "has_figure": false,
 "stem": "F_7A",
 "breadcrumb": "EXAMPLE F.7A · AISC 360-22 Ch.F (HSS flexure) · §F7 §F7.4 · Rectangular HSS Beam Design (Noncompact Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.7A · AISC 360-22 Ch.F (HSS flexure) · §F7 §F7.4 · Rectangular HSS Beam Design (Noncompact Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F7: Eqs. F7-2 (flange local buckling), F7-8/F7-10/F7-11 (LTB); Table B4.1b Cases 17, 19. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 21 ft, braced at ends only; wD = 0.15 kip/ft, wL = 0.40 kip/ft:

- **LRFD:** wu = 1.2(0.15) + 1.6(0.40) = 0.82 kip/ft → Mu = 0.82(21)²/8 = **45.2 kip-ft**
- **ASD:** wa = 0.55 kip/ft → Ma = **30.3 kip-ft**

### 2. Serviceability Requirement (Δ_LL ≤ L/240 = 1.05 in.)

I_req = 5(0.40/12)(252)⁴/[384(29,000)(1.05)] = **57.5 in.⁴**

### 3. Selection and Classification — HSS10x6x3/16 (A500 Gr. C), strong-axis

Zx = 18.0 in.³; Sx = 14.9 in.³; Ix = 74.6 in.⁴ ≥ 57.5 ✓; ry = 2.52 in.; J = 73.8 in.⁴; Ag = 5.37 in.²; b/t = 31.5; h/t = 54.5.

- Flange (Case 17): λp = 27.0 < 31.5 < λr = 33.7 → **noncompact flange**
- Web (Case 19): 54.5 ≤ λpw = 58.3 → compact web

### 4. Flange Local Buckling — Eq. F7-2

Mp = FyZx = 900 kip-in.; FySx = 745 kip-in.

Mn = 900 − (900 − 745)[(31.5 − 27.0)/(33.7 − 27.0)] = 900 − 155(0.671) = **796 kip-in. = 66.3 kip-ft** ← **governs**

### 5. Lateral-Torsional Buckling — §F7.4

Lp = 0.13ErysJAg/Mp = 0.13(29,000)(2.52)√(73.8 × 5.37)/900 = 210 in. = 17.5 ft (Eq. F7-10)
Lr = 2Ery√(JAg)/(0.7FySx) = 5,580 in. (Eq. F7-11) — far beyond Lb = 21 ft = 252 in.

Lp < Lb ≤ Lr → Eq. F7-8 with Cb = 1.14: Mn = 1.14[900 − (900 − 521)(252 − 210)/(5,580 − 210)] = 1.14(897) = 1,022 → capped at Mp = 900 kip-in. → **LTB does not govern** (HSS are torsionally very stiff).

### 6. Available Flexural Strength (FLB governs, Mn = 796 kip-in.)

- **LRFD:** φbMn = 0.90(796) = 716 kip-in. = **59.7 kip-ft** ≥ 45.2 kip-ft ✓ (utilization 0.76)
- **ASD:** Mn/Ωb = 796/1.67 = 477 kip-in. = **39.7 kip-ft** ≥ 30.3 kip-ft ✓ (utilization 0.76)

### 7. Conclusion

**Select HSS10x6x3/16 (A500 Gr. C), strong-axis orientation.** The governing limit state is **flange local buckling of the noncompact 6-in. wall** (Eq. F7-2, ~12% below Mp); LTB is non-critical despite ends-only bracing because of the closed section's torsional stiffness. Strength and the L/240 deflection limit are both satisfied with comfortable margins.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
