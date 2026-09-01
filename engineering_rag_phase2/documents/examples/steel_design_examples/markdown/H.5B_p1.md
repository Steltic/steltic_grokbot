<!-- chunk_id: H.5B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.5B",
 "example_family": "H.5",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "H3.1"
 ],
 "eqs": [
  "H3-1",
  "H3-2a",
  "H3-2b"
 ],
 "tables": [],
 "title": "Torsional Strength of a Round HSS",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.5B — Torsional Strength of a Round HSS",
 "question": "# H.5B - Round HSS torsional strength (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nDetermine the available torsional strength (LRFD and ASD) of an ASTM A500/A500M Grade C HSS5.000x0.250\nthat is 14 ft long, using AISC 360-22 Section H3.1 for round HSS.\n\n## Given\n- Material: ASTM A500/A500M Grade C, Fy = 50 ksi.\n- Member: HSS5.000x0.250; t = 0.233 in.; D/t = 21.5; C = 7.95 in^3; length L = 14 ft (= 168 in.); D = 5.00 in.\n- Code basis: AISC 360-22 Section H3.1.\n\n## Find\nphi_T*Tn (LRFD) and Tn/Omega_T (ASD).",
 "has_figure": false,
 "stem": "H_5B",
 "breadcrumb": "EXAMPLE H.5B · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.1 · Torsional Strength of a Round HSS",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.5B · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.1 · Torsional Strength of a Round HSS

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §H3.1: Eq. H3-1 with Fcr for round HSS as the larger of Eqs. H3-2a and H3-2b, not exceeding 0.6Fy. φT = 0.90, ΩT = 1.67. Per the RAG extract provided.

---

### 1. Member Data

HSS5.000x0.250 (A500 Gr. C, Fy = 50 ksi): t = 0.233 in.; D = 5.00 in.; D/t = 21.5; C = 7.95 in.³; L = 14 ft = 168 in.

### 2. Critical Stress — Eqs. H3-2a / H3-2b

- **Eq. H3-2a:** Fcr = 1.23E/[√(L/D)(D/t)^(5/4)] = 1.23(29,000)/[√(168/5.00)(21.5)^1.25] = 35,700/[5.80(46.3)] = **133 ksi**
- **Eq. H3-2b:** Fcr = 0.60E/(D/t)^(3/2) = 0.60(29,000)/(21.5)^1.5 = 17,400/99.7 = **175 ksi**

Larger = 175 ksi, but not to exceed 0.6Fy = 30.0 ksi → **Fcr = 30.0 ksi** (torsional shear yielding governs, as is typical for standard sections).

### 3. Nominal and Available Torsional Strength — Eq. H3-1

Tn = FcrC = 30.0(7.95) = **239 kip-in.**

- **LRFD:** φT·Tn = 0.90(239) = **215 kip-in.**
- **ASD:** Tn/ΩT = 239/1.67 = **143 kip-in.**

### 4. Conclusion

For the HSS5.000x0.250, both elastic torsional-buckling expressions far exceed the shear-yield ceiling, so the available torsional strength is governed by **yielding at Fcr = 0.6Fy**: **215 kip-in. (LRFD)** and **143 kip-in. (ASD)**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
