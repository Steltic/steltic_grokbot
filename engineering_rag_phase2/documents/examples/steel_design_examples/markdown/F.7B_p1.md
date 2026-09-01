<!-- chunk_id: F.7B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.7B",
 "example_family": "F.7",
 "chapter": "F",
 "topic": "HSS flexure",
 "clauses": [
  "F7"
 ],
 "eqs": [
  "F7-1",
  "F7-2",
  "F7-8",
  "F7-10",
  "F7-11"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "HSS10x6x3/16 Flexural Verification (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.7B — HSS10x6x3/16 Flexural Verification (Direct Specification)",
 "question": "# F.7B — Rectangular HSS beam with a noncompact flange (spec calculation)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nVerify, by directly applying the AISC Specification, the available major-axis flexural\nstrength of a rectangular HSS10×6×3/16 beam oriented in the strong direction. The beam\nspans 21 ft, is simply supported, and is laterally braced at the end points only. Classify\nthe flange and web, identify which limit state governs (yielding, flange local buckling,\nweb local buckling, or lateral-torsional buckling), and report φ_b M_n (LRFD) and\nM_n/Ω_b (ASD).\n\n## Given\n- Material: ASTM A500/A500M Grade C (Fy = 50 ksi, E = 29,000 ksi).\n- Member: HSS10×6×3/16, bent about the strong (x) axis.\n  Geometric properties: A_g = 5.37 in.², Z_x = 18.0 in.³, S_x = 14.9 in.³,\n  r_y = 2.52 in., J = 73.8 in.⁴, b/t = 31.5, h/t = 54.5.\n- Geometry / span: simply supported, L = 21 ft, laterally braced at the ends only\n  (uniformly loaded, so for C_b the moment diagram is parabolic).\n- Code basis: AISC 360-22.\n\n## Find\nThe governing nominal flexural strength M_n and the available strengths φ_b M_n and\nM_n/Ω_b.",
 "has_figure": false,
 "stem": "F_7B",
 "breadcrumb": "EXAMPLE F.7B · AISC 360-22 Ch.F (HSS flexure) · §F7 · HSS10x6x3/16 Flexural Verification (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.7B · AISC 360-22 Ch.F (HSS flexure) · §F7 · HSS10x6x3/16 Flexural Verification (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F7 applied directly: Eqs. F7-1, F7-2, F7-8, F7-10, F7-11; Table B4.1b Cases 17, 19. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Member and Classification

HSS10x6x3/16 (A500 Gr. C), strong-axis bending: Ag = 5.37 in.²; Zx = 18.0 in.³; Sx = 14.9 in.³; ry = 2.52 in.; J = 73.8 in.⁴; b/t = 31.5; h/t = 54.5. L = Lb = 21 ft = 252 in. (braced at ends only; uniform load → Cb = 1.14).

- **Flange (Table B4.1b Case 17):** λp = 1.12√(E/Fy) = 27.0; λr = 1.40√(E/Fy) = 33.7 → 27.0 < 31.5 ≤ 33.7 → **noncompact**
- **Web (Case 19):** λpw = 2.42√(E/Fy) = 58.3 ≥ 54.5 → **compact** (web local buckling does not apply)

### 2. Yielding — Eq. F7-1

Mp = FyZx = 50(18.0) = **900 kip-in.**

### 3. Flange Local Buckling — Eq. F7-2 (noncompact flange)

Mn = Mp − (Mp − FySx)[(λ − λp)/(λr − λp)] = 900 − (900 − 745)[(31.5 − 27.0)/(33.7 − 27.0)]
= 900 − 155(0.671) = **796 kip-in. = 66.3 kip-ft** ← **governing limit state**

### 4. Lateral-Torsional Buckling — Eqs. F7-10, F7-11, F7-8

√(JAg) = √(73.8 × 5.37) = 19.9
Lp = 0.13Ery√(JAg)/Mp = 0.13(29,000)(2.52)(19.9)/900 = **210 in.** (Eq. F7-10)
Lr = 2Ery√(JAg)/(0.7FySx) = 2(29,000)(2.52)(19.9)/521 = **5,580 in.** (Eq. F7-11)

Lp < Lb = 252 in. ≤ Lr → Eq. F7-8:
Mn = 1.14[900 − (900 − 521)(252 − 210)/(5,580 − 210)] = 1.14(897) = 1,022 kip-in. → **capped at Mp = 900 kip-in.; LTB does not govern.**

### 5. Available Flexural Strength

Governing Mn = 796 kip-in. (flange local buckling):

- **LRFD:** φbMn = 0.90(796) = 716 kip-in. = **59.7 kip-ft**
- **ASD:** Mn/Ωb = 796/1.67 = 477 kip-in. = **39.7 kip-ft**

### 6. Conclusion

By direct §F7 calculation, the HSS10x6x3/16 is governed by **flange local buckling of its noncompact compression flange (Eq. F7-2)**, giving Mn = 796 kip-in. — about 12% below the plastic moment. Web local buckling does not apply (compact web), and lateral-torsional buckling is non-critical even with 21 ft unbraced (Lr ≈ 465 ft for this torsionally stiff closed shape). Available strengths: **φbMn = 59.7 kip-ft (LRFD); Mn/Ωb = 39.7 kip-ft (ASD)** — consistent with, and confirming, the selection in Example F.7A.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
