<!-- chunk_id: F.8B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.8B",
 "example_family": "F.8",
 "chapter": "F",
 "topic": "HSS flexure",
 "clauses": [
  "F7",
  "F7.2"
 ],
 "eqs": [
  "F7-4",
  "F7-3"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "HSS8x8x3/16 Effective Section Modulus (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.8B — HSS8x8x3/16 Effective Section Modulus (Direct Specification)",
 "question": "# F.8B — Square HSS beam with slender flanges (effective section modulus)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nUsing the AISC Specification directly, compute the available major-axis flexural strength of\na square HSS8×8×3/16 beam by accounting for its **slender** compression flange through an\neffective section modulus. Classify the flange and web, evaluate the flange-local-buckling\nstrength, and report φ_b M_n (LRFD) and M_n/Ω_b (ASD). The beam is simply supported,\ncontinuously braced, and spans 21 ft.\n\n## Given\n- Material: ASTM A500/A500M Grade C (Fy = 50 ksi, E = 29,000 ksi).\n- Member: HSS8×8×3/16. Properties: I = 54.4 in.⁴, Z = 15.7 in.³, S = 13.6 in.³,\n  design wall t = 0.174 in., b/t = h/t = 43.0, outside dimension H = 8.00 in.\n- Required strength (uniform load, 21-ft span): M_u = 41.3 kip-ft, M_a = 27.6 kip-ft.\n- Code basis: AISC 360-22.\n\n## Find\nThe effective section modulus S_e, the nominal flexural strength M_n (flange local\nbuckling), and the available strengths φ_b M_n and M_n/Ω_b.",
 "has_figure": false,
 "stem": "F_8B",
 "breadcrumb": "EXAMPLE F.8B · AISC 360-22 Ch.F (HSS flexure) · §F7 §F7.2 · HSS8x8x3/16 Effective Section Modulus (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.8B · AISC 360-22 Ch.F (HSS flexure) · §F7 §F7.2 · HSS8x8x3/16 Effective Section Modulus (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F7 applied directly: Table B4.1b Cases 17/19 classification; Eqs. F7-4 (effective width) and F7-3 (Mn = FySe). φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Classification

HSS8x8x3/16 (A500 Gr. C): b/t = h/t = 43.0, t = 0.174 in., H = 8.00 in., I = 54.4 in.⁴, S = 13.6 in.³, Z = 15.7 in.³

- Flange (Case 17): λr = 1.40√(29,000/50) = 33.7 < 43.0 → **slender** → §F7.2(c), Mn = FySe (Eq. F7-3)
- Web (Case 19): 43.0 ≤ 2.42√(E/Fy) = 58.3 → compact (no web reduction)

### 2. Effective Width of the Compression Flange — Eq. F7-4

be = 1.92t√(E/Fy)[1 − (0.38/(b/t))√(E/Fy)]
= 1.92(0.174)(24.08)[1 − (0.38/43.0)(24.08)] = 8.05(0.787) = **6.33 in.** ≤ b = 7.48 in. ✓

Ineffective width = 7.48 − 6.33 = 1.15 in. → ΔA = 1.15(0.174) = 0.200 in.² removed at the compression face (y = +3.91 in. from the gross centroid).

### 3. Effective Section Modulus

Neutral-axis shift: Δȳ = ΔA(3.91)/(5.37 − 0.200) = 0.151 in. (toward the tension face)
Effective inertia: Ie = 54.4 − 0.200(3.91)² − 5.17(0.151)² = 54.4 − 3.06 − 0.12 = **51.2 in.⁴**
Extreme compression fiber: c = 4.00 + 0.151 = 4.15 in.

**Se = Ie/c = 51.2/4.15 = 12.3 in.³**

### 4. Nominal and Available Flexural Strength — Eq. F7-3

Mn = FySe = 50(12.3) = **617 kip-in. = 51.4 kip-ft**

- **LRFD:** φbMn = 0.90(51.4) = **46.3 kip-ft** ≥ Mu = 41.3 kip-ft ✓ (utilization 0.89)
- **ASD:** Mn/Ωb = 51.4/1.67 = **30.8 kip-ft** ≥ Ma = 27.6 kip-ft ✓ (utilization 0.90)

### 5. Conclusion

Direct application of §F7 quantifies the slender-flange penalty for the HSS8x8x3/16: the effective width (Eq. F7-4) trims 1.15 in. from the compression flange, shifting the neutral axis and reducing the section modulus from S = 13.6 to Se = 12.3 in.³ Governing limit state: **flange local buckling, Mn = FySe = 51.4 kip-ft** — adequate for the stated demands under both LRFD and ASD, consistent with Example F.8A.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
