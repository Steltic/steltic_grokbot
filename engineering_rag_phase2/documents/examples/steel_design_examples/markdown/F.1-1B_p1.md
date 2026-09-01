<!-- chunk_id: F.1-1B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.1-1B",
 "example_family": "F.1-1",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2.1",
  "F2.2",
  "F1",
  "F2"
 ],
 "eqs": [
  "F2-1"
 ],
 "tables": [],
 "title": "W18x50 Flexural Check, Continuously Braced (F2 Yielding)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.1-1B — W18x50 Flexural Check, Continuously Braced (F2 Yielding)",
 "question": "# F.1-1B — W18x50 flexural check, continuously braced (F2 yielding)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W18x50 of ASTM A992/A992M steel (Fy = 50 ksi) is used as a simply supported beam spanning 35 ft.\nIt carries uniformly distributed service loads of 0.45 kip/ft dead and 0.75 kip/ft live over the\nfull span, and it is continuously braced against lateral displacement and twist along its entire\nlength. By directly applying the AISC 360-22 Specification (not design-aid tables), determine the\navailable flexural strength of the W18x50 and verify that it is adequate for both LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Section: W18x50; Zx = 101 in.^3 (compact at Fy = 50 ksi).\n- Geometry / span: simple span L = 35 ft; continuously (fully) laterally braced.\n- Loads (service, uniform): wD = 0.45 kip/ft, wL = 0.75 kip/ft.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe available flexural strength (phi_b*Mn for LRFD and Mn/Omega_b for ASD), and confirm it exceeds\nthe required flexural strength.",
 "has_figure": false,
 "stem": "F_1_1B",
 "breadcrumb": "EXAMPLE F.1-1B · AISC 360-22 Ch.F (beam flexure) · §F2.1 §F2.2 §F1 §F2 · W18x50 Flexural Check, Continuously Braced (F2 Yielding)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.1-1B · AISC 360-22 Ch.F (beam flexure) · §F2.1 §F2.2 §F1 §F2 · W18x50 Flexural Check, Continuously Braced (F2 Yielding)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2.1 (Eq. F2-1); LTB not applicable for continuous bracing (§F2.2(a)). φb = 0.90, Ωb = 1.67 (§F1). Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 35 ft; wD = 0.45 kip/ft, wL = 0.75 kip/ft:

- **LRFD:** wu = 1.2(0.45) + 1.6(0.75) = 1.74 kip/ft → Mu = 1.74(35)²/8 = **266 kip-ft**
- **ASD:** wa = 1.20 kip/ft → Ma = **184 kip-ft**

### 2. Nominal Flexural Strength — §F2.1

W18x50 (A992) is a doubly symmetric compact I-shape (§F2 applicability ✓). With continuous lateral and torsional bracing, lateral-torsional buckling does not apply; the strength is the full plastic moment:

> Mn = Mp = FyZx (Eq. F2-1)

Mn = 50(101) = 5,050 kip-in. = **421 kip-ft**

### 3. Available Flexural Strength

- **LRFD:** φbMn = 0.90(421) = **379 kip-ft** ≥ 266 kip-ft ✓ (utilization 0.70)
- **ASD:** Mn/Ωb = 421/1.67 = **252 kip-ft** ≥ 184 kip-ft ✓ (utilization 0.73)

### 4. Conclusion

By direct application of Eq. F2-1, the continuously braced W18x50 provides φbMn = 379 kip-ft (LRFD) and Mn/Ωb = 252 kip-ft (ASD), exceeding the required 266 and 184 kip-ft. **The member is adequate**, governed by the yielding limit state.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
