<!-- chunk_id: H.5A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.5A",
 "example_family": "H.5",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "H3.1"
 ],
 "eqs": [
  "H3-1",
  "H3-3"
 ],
 "tables": [],
 "title": "Torsional Strength of a Rectangular HSS",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.5A — Torsional Strength of a Rectangular HSS",
 "question": "# H.5A - Rectangular HSS torsional strength (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nDetermine the available torsional strength (LRFD design and ASD allowable) of an ASTM A500/A500M Grade C\nHSS6x4x1/4, using AISC 360-22 Section H3.1 for rectangular HSS.\n\n## Given\n- Material: ASTM A500/A500M Grade C, Fy = 50 ksi.\n- Member: HSS6x4x1/4; design wall thickness t = 0.233 in.; b/t = 14.2; h/t = 22.8; torsional constant C = 10.1 in^3.\n- Code basis: AISC 360-22 Section H3.1.\n\n## Find\nphi_T*Tn (LRFD) and Tn/Omega_T (ASD).",
 "has_figure": false,
 "stem": "H_5A",
 "breadcrumb": "EXAMPLE H.5A · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.1 · Torsional Strength of a Rectangular HSS",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.5A · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.1 · Torsional Strength of a Rectangular HSS

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §H3.1: Eq. H3-1 (Tn = FcrC) with Fcr per Eq. H3-3 for rectangular HSS. φT = 0.90, ΩT = 1.67. Per the RAG extract provided.

---

### 1. Member Data

HSS6x4x1/4 (A500 Gr. C, Fy = 50 ksi): t = 0.233 in.; b/t = 14.2; h/t = 22.8; torsional constant C = 10.1 in.³

### 2. Critical Stress — Eq. H3-3

Wall slenderness limit: 2.45√(E/Fy) = 2.45√(29,000/50) = **59.0**

h/t = 22.8 ≤ 59.0 → **Fcr = 0.6Fy = 30.0 ksi** (Eq. H3-3) — torsional yielding, no wall-buckling reduction (Eqs. H3-4/H3-5 not invoked).

### 3. Nominal and Available Torsional Strength — Eq. H3-1

Tn = FcrC = 30.0(10.1) = **303 kip-in.**

- **LRFD:** φT·Tn = 0.90(303) = **273 kip-in.**
- **ASD:** Tn/ΩT = 303/1.67 = **181 kip-in.**

### 4. Conclusion

The HSS6x4x1/4 develops its full torsional yield strength (stocky walls, h/t well below 2.45√(E/Fy)), giving an available torsional strength of **273 kip-in. (LRFD)** and **181 kip-in. (ASD)**. These values feed directly into the combined-force check of Example H.5C (Eq. H3-6).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
