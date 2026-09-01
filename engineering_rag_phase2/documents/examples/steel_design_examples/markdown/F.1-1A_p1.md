<!-- chunk_id: F.1-1A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.1-1A",
 "example_family": "F.1-1",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2",
  "F1",
  "F2.1"
 ],
 "eqs": [
  "F2-1"
 ],
 "tables": [],
 "title": "W-Shape Flexural Member Design, Major Axis, Continuously Braced",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.1-1A — W-Shape Flexural Member Design, Major Axis, Continuously Braced",
 "question": "# F.1-1A — W-shape flexural member design, major-axis, continuously braced  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported floor beam spans 35 ft and carries uniformly distributed service loads of\n0.45 kip/ft dead load and 0.75 kip/ft live load over the full span. The beam is continuously\nbraced against lateral displacement and twist along its entire length (e.g., by a composite or\nmechanically fastened floor slab), so lateral-torsional buckling is not a concern. Architectural\nclearance limits the member to a maximum nominal depth of 18 in. The live-load deflection must not\nexceed L/360. Using AISC 360-22, select the lightest available rolled W-shape that satisfies both\nstrength (LRFD and ASD) and the live-load deflection limit. The steel is ASTM A992/A992M\n(Fy = 50 ksi, Fu = 65 ksi).\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Geometry / span: simple span L = 35 ft; continuously (fully) laterally braced.\n- Loads (service, uniform): wD = 0.45 kip/ft, wL = 0.75 kip/ft.\n- Constraints: maximum nominal depth = 18 in.; live-load deflection limit = L/360.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nSelect the lightest W-shape (nominal depth <= 18 in.) such that the available flexural strength\nexceeds the required flexural strength (both LRFD and ASD) and the live-load deflection <= L/360.",
 "has_figure": false,
 "stem": "F_1_1A",
 "breadcrumb": "EXAMPLE F.1-1A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 §F2.1 · W-Shape Flexural Member Design, Major Axis, Continuously Braced",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.1-1A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 §F2.1 · W-Shape Flexural Member Design, Major Axis, Continuously Braced

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 (Eq. F2-1; LTB not applicable — continuous bracing). φb = 0.90, Ωb = 1.67 (§F1). Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 35 ft; wD = 0.45 kip/ft, wL = 0.75 kip/ft:

- **LRFD:** wu = 1.2(0.45) + 1.6(0.75) = 1.74 kip/ft → Mu = 1.74(35)²/8 = **266 kip-ft**
- **ASD:** wa = 1.20 kip/ft → Ma = 1.20(35)²/8 = **184 kip-ft**

### 2. Serviceability Requirement

Δ_LL ≤ L/360 = 35(12)/360 = 1.17 in. For a uniform load:

I_req = 5wL L⁴/(384EΔ) = 5(0.75/12)(420)⁴/[384(29,000)(1.17)] = **749 in.⁴**

### 3. Selection — W18x50 (A992; nominal depth 18 in. ≤ limit ✓)

Zx = 101 in.³; Ix = 800 in.⁴; the shape is compact for Fy = 50 ksi (flange and web satisfy Table B4.1b), and continuous bracing eliminates lateral-torsional buckling, so yielding governs.

### 4. Flexural Strength — §F2.1, Eq. F2-1

Mn = Mp = FyZx = 50(101) = 5,050 kip-in. = **421 kip-ft**

- **LRFD:** φbMn = 0.90(421) = **379 kip-ft** ≥ 266 kip-ft ✓ (utilization 0.70)
- **ASD:** Mn/Ωb = 421/1.67 = **252 kip-ft** ≥ 184 kip-ft ✓ (utilization 0.73)

### 5. Deflection Check

Ix = 800 in.⁴ ≥ 749 in.⁴ ✓ → Δ_LL = 1.17(749/800) = **1.09 in. ≤ 1.17 in. ✓**

### 6. Lightest-Shape Confirmation

W18x46 (next lighter 18-in. shape): Ix = 712 in.⁴ < 749 in.⁴ — fails the deflection limit, despite adequate strength. Shallower shapes meeting Ix ≥ 749 in.⁴ are heavier (e.g., W16x57). **W18x50 is the lightest shape satisfying both criteria — deflection, not strength, controls the selection.**

### 7. Conclusion

**Select W18x50 (ASTM A992).** With full lateral bracing, the governing strength limit state is yielding (Eq. F2-1, φbMn = 379 kip-ft / Mn,Ωb = 252 kip-ft, both well above demand), and the live-load deflection criterion L/360 governs the design, requiring Ix ≥ 749 in.⁴.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
