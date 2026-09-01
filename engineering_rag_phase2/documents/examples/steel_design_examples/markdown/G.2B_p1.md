<!-- chunk_id: G.2B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.2B",
 "example_family": "G.2",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G2.1",
  "G1"
 ],
 "eqs": [
  "G2-1",
  "G2-3",
  "G2-5"
 ],
 "tables": [],
 "title": "C15x33.9 Shear Strength (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.2B — C15x33.9 Shear Strength (Direct Specification)",
 "question": "# G.2B -- Channel in Major-Axis Shear (direct from the Specification)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nFor the ASTM A992/A992M C15x33.9 channel of the previous problem, compute the\navailable major-axis shear strength directly from the AISC 360 Chapter G provisions.\nReport phi_v*Vn and Vn/Omega_v.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: C15x33.9 (d = 15.0 in., tw = 0.400 in.), major-axis shear.\n- Code basis: AISC 360-22 Chapter G.\n\n## Find\nphi_v*Vn and Vn/Omega_v from Section G2.1.",
 "has_figure": false,
 "stem": "G_2B",
 "breadcrumb": "EXAMPLE G.2B · AISC 360-22 Ch.G (beam shear) · §G2.1 §G1 · C15x33.9 Shear Strength (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.2B · AISC 360-22 Ch.G (beam shear) · §G2.1 §G1 · C15x33.9 Shear Strength (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G2.1(b) applied from first principles: Eqs. G2-1, G2-3, G2-5 (kv); §G1 factors. Per the RAG extract provided.

---

### 1. Classification — §G2.1(b)

C15x33.9 (A992): d = 15.0 in.; tw = 0.400 in. As a channel (not a rolled I-shape meeting §G2.1(a)), the general web provision applies: **φv = 0.90, Ωv = 1.67** (§G1).

Web without transverse stiffeners: **kv = 5.34** (§G2.1(b)(2)).

Slenderness threshold: 1.10√(kvE/Fy) = 1.10√(5.34 × 29,000/50) = **61.2**. The channel web (h/tw ≈ 30) is far below this → **Cv1 = 1.0** (Eq. G2-3) — shear yielding, no post-buckling reduction.

### 2. Nominal Shear Strength — Eq. G2-1

Aw = d·tw = 15.0(0.400) = 6.00 in.²

Vn = 0.6FyAwCv1 = 0.6(50)(6.00)(1.0) = **180 kips**

### 3. Available Shear Strength

- **LRFD:** φvVn = 0.90(180) = **162 kips**
- **ASD:** Vn/Ωv = 180/1.67 = **108 kips**

### 4. Conclusion

By direct §G2.1(b) calculation, the C15x33.9 develops its full web shear yield strength (Cv1 = 1.0), providing **162 kips (LRFD)** and **108 kips (ASD)** — matching the Manual values of Example G.2A and adequate for the stated 150 / 100 kip demands.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
