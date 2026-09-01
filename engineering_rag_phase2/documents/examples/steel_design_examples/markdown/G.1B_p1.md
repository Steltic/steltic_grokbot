<!-- chunk_id: G.1B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.1B",
 "example_family": "G.1",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G2.1"
 ],
 "eqs": [
  "G2-1",
  "G2-2"
 ],
 "tables": [],
 "title": "W24x62 Shear Strength (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.1B — W24x62 Shear Strength (Direct Specification)",
 "question": "# G.1B -- W-Shape in Major-Axis Shear (direct from the Specification)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nFor the same ASTM A992/A992M W24x62 beam of the previous problem, determine the\navailable major-axis shear strength by directly applying the provisions and equations\nof AISC 360 Chapter G (rather than reading a Manual table). Report phi_v*Vn (LRFD)\nand Vn/Omega_v (ASD).\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: W24x62 (d = 23.7 in., tw = 0.430 in.), major-axis shear.\n- Code basis: AISC 360-22 Chapter G.\n\n## Find\nphi_v*Vn and Vn/Omega_v from first principles (Section G2.1).",
 "has_figure": false,
 "stem": "G_1B",
 "breadcrumb": "EXAMPLE G.1B · AISC 360-22 Ch.G (beam shear) · §G2.1 · W24x62 Shear Strength (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.1B · AISC 360-22 Ch.G (beam shear) · §G2.1 · W24x62 Shear Strength (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G2.1 applied from first principles: Eqs. G2-1, G2-2. Per the RAG extract provided.

---

### 1. Web Slenderness Check — §G2.1(a)

W24x62 (A992): d = 23.7 in.; tw = 0.430 in.; h/tw = 50.1.

2.24√(E/Fy) = 2.24√(29,000/50) = **53.9**

h/tw = 50.1 ≤ 53.9 → rolled I-shape qualifying for §G2.1(a): **φv = 1.00 (LRFD), Ωv = 1.50 (ASD), and Cv1 = 1.0 (Eq. G2-2)** — shear yielding, no buckling reduction.

### 2. Nominal Shear Strength — Eq. G2-1

Aw = d·tw = 23.7(0.430) = 10.2 in.²

Vn = 0.6FyAwCv1 = 0.6(50)(10.2)(1.0) = **306 kips**

### 3. Available Shear Strength

- **LRFD:** φvVn = 1.00(306) = **306 kips**
- **ASD:** Vn/Ωv = 306/1.50 = **204 kips**

### 4. Conclusion

Computed directly from §G2.1, the W24x62 web yields in shear (Cv1 = 1.0) with available strengths of **306 kips (LRFD)** and **204 kips (ASD)** — identical to the Manual-table values used in Example G.1A, as expected, since the tables implement Eqs. G2-1/G2-2 with the enhanced φv = 1.00 / Ωv = 1.50 applicable to stocky rolled-I webs.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
