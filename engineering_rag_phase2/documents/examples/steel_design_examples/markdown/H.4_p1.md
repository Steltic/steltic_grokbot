<!-- chunk_id: H.4_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.4",
 "example_family": "H.4",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "E3",
  "F2",
  "F6",
  "H1.1",
  "App8"
 ],
 "eqs": [
  "A-8-1",
  "A-8-3",
  "A-8-5",
  "F2-2",
  "F6-1",
  "H1-1b"
 ],
 "tables": [],
 "title": "W10x33 Under Axial Compression and Biaxial Bending with B1 Amplification",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.4 — W10x33 Under Axial Compression and Biaxial Bending with B1 Amplification",
 "question": "# H.4 - W-shape under combined axial compression + biaxial flexure with B1 amplification (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect an ASTM A992/A992M W-shape of 10 in. nominal depth for combined axial compression and biaxial\nbending. Axial compression is 5 kips dead + 15 kips live. First-order moments (no second-order effects yet)\nfrom uniformly distributed loads are MxD = 15, MxL = 45 kip-ft (major) and MyD = 2, MyL = 6 kip-ft (minor).\nThe unbraced length is 14 ft, pinned ends, with no sidesway (no lateral translation). Amplify the first-order\nmoments for P-delta using AISC 360-22 Appendix 8 (B1), then verify the member with Section H1.1 (Eq. H1-1b).\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Loads: axial D = 5 k, L = 15 k; MxD = 15, MxL = 45 k-ft; MyD = 2, MyL = 6 k-ft. No sidesway.\n- Geometry: Lcx = Lcy = 14 ft, pinned ends.\n- Trial member: W10x33 (Ag = 9.71 in^2, Sx = 35.0 in^3, Zx = 38.8 in^3, Ix = 171 in^4, rx = 4.19 in,\n  Sy = 9.20 in^3, Zy = 14.0 in^3, Iy = 36.6 in^4, ry = 1.94 in, Lp = 6.85 ft, Lr = 21.8 ft; compact).\n- Code basis: AISC 360-22 (+ ASCE/SEI 7 for load combinations).\n\n## Find\nFactored required strengths, B1-amplified moments, available strengths, and the H1 interaction ratio (LRFD/ASD).",
 "has_figure": false,
 "stem": "H_4",
 "breadcrumb": "EXAMPLE H.4 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §E3 §F2 §F6 §H1.1 §App8 · W10x33 Under Axial Compression and Biaxial Bending with B1 Amplification",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.4 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §E3 §F2 §F6 §H1.1 §App8 · W10x33 Under Axial Compression and Biaxial Bending with B1 Amplification

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Appendix 8 (Eqs. A-8-1, A-8-3, A-8-5; B2 = 0, no translation), §E3, §F2 (Eq. F2-2), §F6 (Eq. F6-1), §H1.1 (Eq. H1-1b). φc = φb = 0.90; Ωc = Ωb = 1.67. Per the RAG extract provided.

---

### 1. First-Order Required Strengths (no lateral translation → Mlt = 0)

- **LRFD:** Pu = 1.2(5) + 1.6(15) = **30.0 kips**; Mux,nt = 90.0 kip-ft; Muy,nt = 12.0 kip-ft
- **ASD:** Pa = **20.0 kips**; Max,nt = 60.0 kip-ft; May,nt = 8.00 kip-ft

Trial: **W10x33** (A992), Lcx = Lcy = Lb = 14 ft = 168 in., pinned, compact.

### 2. Second-Order Amplification — Appendix 8, B1 (Eq. A-8-3)

Cm = 1.0 (transversely loaded member, conservative); Pe1 = π²EI/Lc1² (Eq. A-8-5):
Pe1x = π²(29,000)(171)/(168)² = 1,730 kips; Pe1y = π²(29,000)(36.6)/(168)² = 371 kips

| | B1x | B1y | Mrx | Mry |
|---|---|---|---|---|
| LRFD (α = 1.0) | 1/(1 − 30/1,730) = 1.02 | 1/(1 − 30/371) = 1.09 | 1.02(90.0) = **91.6 kip-ft** | 1.09(12.0) = **13.1 kip-ft** |
| ASD (α = 1.6) | 1.02 | 1/(1 − 32/371) = 1.09 | 1.02(60.0) = **61.1 kip-ft** | 1.09(8.00) = **8.75 kip-ft** |

Pr = Pnt (Eq. A-8-2 with B2 term zero).

### 3. Available Strengths

**Compression (§E3):** Lc/ry = 168/1.94 = 86.6 → Fe = 38.2 ksi; Fn = (0.658^1.31)(50) = 28.9 ksi; Pn = 28.9(9.71) = 281 kips → **Pc = 253 kips (LRFD) / 168 kips (ASD)**

**Major-axis flexure (§F2):** Lp = 6.85 ft < Lb = 14 ft ≤ Lr = 21.8 ft → Eq. F2-2 with Cb = 1.14:
Mp = 50(38.8) = 1,940 kip-in.; 0.7FySx = 1,225 kip-in.; ratio = (14 − 6.85)/(21.8 − 6.85) = 0.478
Mn = 1.14[1,940 − 715(0.478)] = 1,820 kip-in. ≤ Mp → **Mcx = 137 kip-ft (LRFD) / 90.9 kip-ft (ASD)**

**Minor-axis flexure (§F6, Eq. F6-1):** Mny = FyZy = 700 kip-in. ≤ 1.6FySy = 736 ✓ → **Mcy = 52.5 kip-ft (LRFD) / 34.9 kip-ft (ASD)**

### 4. Interaction — §H1.1 (Pr/Pc = 0.12 < 0.2 → Eq. H1-1b)

Pr/(2Pc) + (Mrx/Mcx + Mry/Mcy) ≤ 1.0

- **LRFD:** 30.0/(2 × 253) + 91.6/137 + 13.1/52.5 = 0.059 + 0.671 + 0.249 = **0.98 ≤ 1.0 ✓**
- **ASD:** 20.0/(2 × 168) + 61.1/90.9 + 8.75/34.9 = 0.060 + 0.672 + 0.251 = **0.98 ≤ 1.0 ✓**

### 5. Conclusion

**The W10x33 is adequate**, with the §H1.1 interaction at 0.98 under both LRFD and ASD after amplifying the no-translation moments by B1 (1.02 strong axis, 1.09 weak axis). The margins are minimal (~2%); the member is efficiently sized, and any load growth or change in bracing should prompt reselection (the next heavier W10 would restore margin).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
