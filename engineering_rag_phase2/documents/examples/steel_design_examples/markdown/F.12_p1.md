<!-- chunk_id: F.12_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.12",
 "example_family": "F.12",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F11",
  "F11.2"
 ],
 "eqs": [
  "F11-1",
  "F11-3"
 ],
 "tables": [],
 "title": "Rectangular Bar in Major-Axis Bending",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.12 — Rectangular Bar in Major-Axis Bending",
 "question": "# F.12 — Rectangular bar in major-axis bending  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect a **solid rectangular bar** to span **12 ft** as a simply supported beam carrying uniform\ngravity load, bending about its **major (strong) axis**. The bar is **ASTM A572/A572M Grade 50**\n(Fy = 50 ksi). It is **simply supported and laterally braced at the end points and at midspan**;\nconservatively take **Cb = 1.0**. The **depth of the bar is limited to 5 in.**\n\nService uniform loads (vertical): dead load wD = 0.44 kip/ft, live load wL = 1.32 kip/ft.\nDirectly applying the AISC 360-22 Specification (Section F11 for rectangular bars), verify a trial\n**bar 5 in. (deep) × 3 in. (wide)** and report the available flexural strength (LRFD and ASD),\nidentifying the controlling limit state.\n\n## Given\n- Material: ASTM A572/A572M Grade 50; Fy = 50 ksi; E = 29,000 ksi.\n- Span / bracing: L = 12 ft, simply supported, braced at ends and midspan ⇒ Lb = 6 ft; Cb = 1.0;\n  depth limited to 5 in.\n- Loads (service, vertical): wD = 0.44 kip/ft; wL = 1.32 kip/ft.\n- Trial member: rectangular bar, depth d = 5.00 in., width (thickness) t = 3.00 in.;\n  Sx = bd²/6 = 12.5 in.³; Zx = bd²/4 = 18.8 in.³\n- Code basis: AISC 360-22.\n\n## Find\nThe available major-axis flexural strength of the 5 in. × 3 in. bar (φbMn for LRFD and Mn/Ωb for ASD),\nand whether it is adequate for the required moment.",
 "has_figure": false,
 "stem": "F_12",
 "breadcrumb": "EXAMPLE F.12 · AISC 360-22 Ch.F (beam flexure) · §F11 §F11.2 · Rectangular Bar in Major-Axis Bending",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.12 · AISC 360-22 Ch.F (beam flexure) · §F11 §F11.2 · Rectangular Bar in Major-Axis Bending

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F11 (Rectangular Bars and Rounds): Eq. F11-1 and the LTB applicability limit Lbd/t² ≤ 0.08E/Fy (Eqs. F11-3/4/5 not triggered). φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 12 ft; braced at ends and midspan (Lb = 6 ft = 72 in.), Cb = 1.0. wD = 0.44, wL = 1.32 kip/ft:

- **LRFD:** wu = 1.2(0.44) + 1.6(1.32) = 2.64 kip/ft → Mu = 2.64(12)²/8 = **47.5 kip-ft** (570 kip-in.)
- **ASD:** wa = 1.76 kip/ft → Ma = 1.76(12)²/8 = **31.7 kip-ft** (380 kip-in.)

### 2. Trial Member — Bar 5 in. × 3 in. (A572 Gr. 50)

d = 5.00 in. (≤ 5 in. depth limit ✓); t = 3.00 in.; Sx = td²/6 = 12.5 in.³; Zx = td²/4 = 18.8 in.³

### 3. Lateral-Torsional Buckling Applicability — §F11.2

Lbd/t² = 72(5.00)/(3.00)² = **40.0**

Limit: 0.08E/Fy = 0.08(29,000)/50 = **46.4**

40.0 ≤ 46.4 → **the LTB limit state does not apply**; yielding governs (Eqs. F11-3 through F11-5 not invoked).

### 4. Yielding — Eq. F11-1

> Mn = Mp = FyZ ≤ 1.5FySx

FyZx = 50(18.75) = 938 kip-in.; cap = 1.5(50)(12.5) = 938 kip-in. (rectangular shape factor = exactly 1.5)

**Mn = 938 kip-in. = 78.1 kip-ft**

### 5. Available Flexural Strength

- **LRFD:** φbMn = 0.90(938) = 844 kip-in. = **70.3 kip-ft** ≥ 47.5 kip-ft ✓ (utilization 0.68)
- **ASD:** Mn/Ωb = 938/1.67 = 561 kip-in. = **46.8 kip-ft** ≥ 31.7 kip-ft ✓ (utilization 0.68)

### 6. Conclusion

**The 5 in. × 3 in. rectangular bar (A572 Gr. 50) is adequate.** With midspan bracing the slenderness parameter Lbd/t² = 40.0 falls below the 0.08E/Fy threshold, so lateral-torsional buckling is precluded and the full plastic moment is available (Eq. F11-1, governing limit state: **yielding**). Available strength is 70.3 kip-ft (LRFD) / 46.8 kip-ft (ASD) against required 47.5 / 31.7 kip-ft.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
