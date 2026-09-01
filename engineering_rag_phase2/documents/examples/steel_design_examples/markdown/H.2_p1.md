<!-- chunk_id: H.2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.2",
 "example_family": "H.2",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "H2"
 ],
 "eqs": [
  "H2-1"
 ],
 "tables": [],
 "title": "W14x99 Beam-Column, §H2 Combined-Stress Check",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.2 — W14x99 Beam-Column, §H2 Combined-Stress Check",
 "question": "# H.2 - W-shape under combined compression + biaxial bending by Section H2 (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W14x99 column has pinned ends and an unbraced length of 14 ft about both axes\n(Lcx = Lcy = 14.0 ft). A second-order analysis including P-delta effects gives the required strengths\nbelow. Using the AISC 360-22 Section H2 combined-stress equation (Eq. H2-1, the elastic stress\ninteraction permitted for any shape), verify the member at the extreme fiber.\n\n| Required strength | LRFD | ASD |\n|---|---|---|\n| Axial (compression) | Pu = 360 kips | Pa = 240 kips |\n| Major-axis moment | Mux = 250 kip-ft | Max = 167 kip-ft |\n| Minor-axis moment | Muy = 80.0 kip-ft | May = 53.3 kip-ft |\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: W14x99 (A = 29.1 in^2, Sx = 157 in^3, Sy = 55.2 in^3; for available strengths also\n  Zx = 173 in^3, Zy = 83.6 in^3, ry = 3.71 in, rts = 4.05 in, ho = 13.4 in, J = 5.37 in^4, bf/2tf = 9.36).\n- Geometry: Lcx = Lcy = 14.0 ft, pinned ends.\n- Loads: second-order required strengths (P-delta included).\n- Code basis: AISC 360-22.\n\n## Find\nWhether the combined stress ratio of Eq. H2-1 at the extreme fiber is <= 1.0 (LRFD and ASD).",
 "has_figure": false,
 "stem": "H_2",
 "breadcrumb": "EXAMPLE H.2 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H2 · W14x99 Beam-Column, §H2 Combined-Stress Check",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.2 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H2 · W14x99 Beam-Column, §H2 Combined-Stress Check

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §H2 (Eq. H2-1), with available stresses from Chapters E and F (per Example H.1B: φcPn = 1,130 kips / Pn,Ωc = 750 kips; φbMnx = 642 kip-ft / 427 kip-ft; φbMny = 311 kip-ft / 207 kip-ft). Per the RAG extract provided.

---

### 1. Required Strengths (second-order, P-δ included)

Pr = 360/240 kips; Mrx = 250/167 kip-ft; Mry = 80.0/53.3 kip-ft (LRFD/ASD). W14x99: A = 29.1 in.²; Sx = 157 in.³; Sy = 55.2 in.³

### 2. Required Stresses at the Critical Extreme Fiber (flange tip, all terms additive)

**LRFD:** fra = 360/29.1 = 12.4 ksi; frbw = 250(12)/157 = 19.1 ksi; frbz = 80.0(12)/55.2 = 17.4 ksi
**ASD:** fra = 240/29.1 = 8.25 ksi; frbw = 167(12)/157 = 12.8 ksi; frbz = 53.3(12)/55.2 = 11.6 ksi

### 3. Available Stresses (axial per Chapter E; flexure per Chapter F, at the same fiber)

**LRFD:** Fca = 1,130/29.1 = 38.7 ksi; Fcbw = 642(12)/157 = 49.1 ksi; Fcbz = 311(12)/55.2 = 67.6 ksi
**ASD:** Fca = 750/29.1 = 25.8 ksi; Fcbw = 427(12)/157 = 32.6 ksi; Fcbz = 207(12)/55.2 = 45.0 ksi

### 4. Interaction — Eq. H2-1

|fra/Fca + frbw/Fcbw + frbz/Fcbz| ≤ 1.0

- **LRFD:** 12.4/38.7 + 19.1/49.1 + 17.4/67.6 = 0.319 + 0.389 + 0.257 = **0.97 ≤ 1.0 ✓**
- **ASD:** 8.25/25.8 + 12.8/32.6 + 11.6/45.0 = 0.320 + 0.391 + 0.257 = **0.97 ≤ 1.0 ✓**

### 5. Conclusion

The W14x99 **satisfies Eq. H2-1 at 0.97** under both LRFD and ASD. Note that although the axial demand here (360/240 kips) is lower than in Examples H.1A/H.1B (400/267 kips), the §H2 elastic-stress interaction produces a higher ratio (0.97 vs. 0.93) — §H2 is the more conservative formulation because it linearly superposes extreme-fiber stresses without the partial-plastification benefit embedded in Eq. H1-1a. It remains a valid (and sometimes advantageous) alternative permitted for any shape, and the member is **adequate**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
