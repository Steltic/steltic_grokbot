<!-- chunk_id: H.3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.3",
 "example_family": "H.3",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "H1.2",
  "D2",
  "F2",
  "F6"
 ],
 "eqs": [
  "H1-1b",
  "D2-1",
  "F2-2",
  "F6-1"
 ],
 "tables": [],
 "title": "W14x82 Under Axial Tension and Biaxial Bending",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.3 — W14x82 Under Axial Tension and Biaxial Bending",
 "question": "# H.3 - W-shape under combined axial tension + biaxial flexure (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect an ASTM A992/A992M W-shape of 14 in. nominal depth to carry combined axial tension and biaxial\nbending. The axial tension is 29 kips dead + 87 kips live. The member also carries moments from uniformly\ndistributed loads: MxD = 32 kip-ft, MxL = 96 kip-ft (major axis) and MyD = 11.3 kip-ft, MyL = 33.8 kip-ft\n(minor axis). The unbraced length is 30 ft with pinned ends; connections have no holes. Verify the trial\nmember with the AISC 360-22 Section H1.2 interaction (Eq. H1-1a/H1-1b), taking advantage of the Cb increase\npermitted for members in axial tension.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Loads (ASCE/SEI 7): tension D = 29 k, L = 87 k; MxD = 32, MxL = 96 k-ft; MyD = 11.3, MyL = 33.8 k-ft.\n- Geometry: Lb = 30 ft, pinned ends; no holes (Ae = Ag).\n- Trial member: W14x82 (Ag = 24.0 in^2, Sx = 123 in^3, Zx = 139 in^3, Sy = 29.3 in^3, Zy = 44.8 in^3,\n  Iy = 148 in^4, Lp = 8.76 ft, Lr = 33.2 ft; compact section).\n- Code basis: AISC 360-22 (+ ASCE/SEI 7 for load combinations).\n\n## Find\nFactored required strengths, available tensile/flexural strengths, and the H1 interaction ratio (LRFD and ASD).",
 "has_figure": false,
 "stem": "H_3",
 "breadcrumb": "EXAMPLE H.3 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H1.2 §D2 §F2 §F6 · W14x82 Under Axial Tension and Biaxial Bending",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.3 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H1.2 §D2 §F2 §F6 · W14x82 Under Axial Tension and Biaxial Bending

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §H1.2 (Eq. H1-1b with the Cb modification √(1 + αPr/Pey) for tension), §D2 (Eq. D2-1), §F2 (Eq. F2-2), §F6 (Eq. F6-1). φ = 0.90 (φt, φb); Ω = 1.67. Per the RAG extract provided.

---

### 1. Required Strengths

- **LRFD:** Pu = 1.2(29) + 1.6(87) = **174 kips (T)**; Mux = 1.2(32) + 1.6(96) = **192 kip-ft**; Muy = 1.2(11.3) + 1.6(33.8) = **67.6 kip-ft**
- **ASD:** Pa = **116 kips (T)**; Max = **128 kip-ft**; May = **45.1 kip-ft**

Trial: **W14x82** (A992), Lb = 30 ft, pinned; no holes → Ae = Ag (rupture not governing).

### 2. Available Tensile Strength — §D2(a), Eq. D2-1

Pn = FyAg = 50(24.0) = 1,200 kips → **Pc = 1,080 kips (LRFD) / 719 kips (ASD)**

### 3. Major-Axis Flexure — §F2 with the §H1.2 Cb Increase

Lp = 8.76 ft < Lb = 30 ft ≤ Lr = 33.2 ft → Eq. F2-2. Basic Cb = 1.14 (uniform load, ends braced).

§H1.2 permits Cb to be multiplied by √(1 + αPr/Pey), where Pey = π²EIy/Lb² = π²(29,000)(148)/(360)² = **327 kips**:

- LRFD (α = 1.0): factor = √(1 + 174/327) = 1.24 → Cb* = 1.41
- ASD (α = 1.6): factor = √(1 + 1.6(116)/327) = 1.25 → Cb* = 1.43

Mp = 50(139) = 6,950 kip-in.; 0.7FySx = 4,310 kip-in.; (Lb − Lp)/(Lr − Lp) = 0.869:

Mn = Cb*[6,950 − (2,640)(0.869)] = Cb*(4,650) → LRFD: 1.41(4,650) = 6,560 kip-in. ≤ Mp ✓; ASD: 1.43(4,650) = 6,640 kip-in. ≤ Mp ✓

**Mcx = 0.90(6,560)/12 = 492 kip-ft (LRFD); (6,640/1.67)/12 = 331 kip-ft (ASD)**

### 4. Minor-Axis Flexure — §F6, Eq. F6-1

Mny = FyZy = 50(44.8) = 2,240 kip-in. ≤ 1.6FySy = 2,340 ✓ → **Mcy = 168 kip-ft (LRFD) / 112 kip-ft (ASD)**

### 5. Interaction — §H1.2 (Eq. H1-1b; Pr/Pc = 0.16 < 0.2)

Pr/(2Pc) + (Mrx/Mcx + Mry/Mcy) ≤ 1.0

- **LRFD:** 174/(2 × 1,080) + 192/492 + 67.6/168 = 0.081 + 0.390 + 0.402 = **0.87 ≤ 1.0 ✓**
- **ASD:** 116/(2 × 719) + 128/331 + 45.1/112 = 0.081 + 0.386 + 0.403 = **0.87 ≤ 1.0 ✓**

### 6. Conclusion

**The W14x82 is adequate** for the combined tension-plus-biaxial-bending demand, with an interaction ratio of 0.87 (LRFD and ASD). The §H1.2 tension-stabilization factor raises Cb from 1.14 to ≈1.41–1.43, increasing the usable LTB strength about 24% — without it the major-axis term would rise appreciably; the axial tension genuinely helps the 30-ft unbraced member.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
