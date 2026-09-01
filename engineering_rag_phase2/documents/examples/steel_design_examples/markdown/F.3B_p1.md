<!-- chunk_id: F.3B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.3B",
 "example_family": "F.3",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F3.2",
  "F3"
 ],
 "eqs": [
  "F3-1"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "W21x48 Flexural Check, Noncompact Flange (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.3B — W21x48 Flexural Check, Noncompact Flange (Direct Specification)",
 "question": "# F.3B — W-shape flexural member with noncompact flanges, major-axis (check, direct Spec)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W21×48 of ASTM A992/A992M steel (Fy = 50 ksi) is used as a simply supported beam spanning\n40 ft, continuously braced against lateral-torsional buckling. The required flexural strength\nat midspan is Mu = 396 kip-ft (LRFD) and Ma = 250 kip-ft (ASD).\n\nThe W21×48 has a noncompact compression flange at Fy = 50 ksi. By directly applying the\nAISC 360 Specification (Table B4.1b flange classification and Section F3 compression flange\nlocal buckling), determine the available flexural strength and confirm the member is\nadequate in both LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Member: W21×48; Sx = 93.0 in³, Zx = 107 in³, bf/2tf = 9.47.\n- Geometry: simply supported, L = 40 ft; continuously braced (Lb = 0 ⇒ LTB does not apply).\n- Required strength: Mu = 396 kip-ft (LRFD), Ma = 250 kip-ft (ASD).\n- Code basis: AISC 360-22 (Chapter F).\n\n## Find\nClassify the compression flange, then compute the nominal flexural strength (Section F3) and\nthe available flexural strength (φ_b·Mn and Mn/Ω_b), and state whether the member is adequate.",
 "has_figure": false,
 "stem": "F_3B",
 "breadcrumb": "EXAMPLE F.3B · AISC 360-22 Ch.F (beam flexure) · §F3.2 §F3 · W21x48 Flexural Check, Noncompact Flange (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.3B · AISC 360-22 Ch.F (beam flexure) · §F3.2 §F3 · W21x48 Flexural Check, Noncompact Flange (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Table B4.1b Case 11 (flange classification) and §F3.2 (Eq. F3-1). φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Mu = **396 kip-ft** (LRFD); Ma = **250 kip-ft** (ASD). Continuous bracing → LTB does not apply.

### 2. Flange Classification — Table B4.1b, Case 11

λ = bf/2tf = 9.47; λpf = 0.38√(29,000/50) = 9.15; λrf = 1.0√(29,000/50) = 24.1

9.15 < 9.47 ≤ 24.1 → **noncompact compression flange** → §F3 (yielding capped by flange local buckling).

### 3. Nominal Flexural Strength — §F3.2, Eq. F3-1

Mp = FyZx = 50(107) = 5,350 kip-in.; 0.7FySx = 35(93.0) = 3,260 kip-in.

Mn = Mp − (Mp − 0.7FySx)[(λ − λpf)/(λrf − λpf)] = 5,350 − (2,090)(0.0214) = **5,310 kip-in. = 442 kip-ft**

### 4. Available Flexural Strength

- **LRFD:** φbMn = 0.90(442) = **398 kip-ft** ≥ 396 kip-ft ✓ (utilization 0.99)
- **ASD:** Mn/Ωb = 442/1.67 = **265 kip-ft** ≥ 250 kip-ft ✓ (utilization 0.94)

### 5. Conclusion

Direct application of Table B4.1b and Eq. F3-1 shows the continuously braced W21x48 is governed by **compression flange local buckling**, reducing the nominal strength about 1% below Mp to 442 kip-ft. Available strengths of 398 kip-ft (LRFD) and 265 kip-ft (ASD) exceed the required 396 / 250 kip-ft — **the member is adequate**, with essentially no spare LRFD margin (0.5%), underscoring the importance of including the noncompact-flange reduction.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
