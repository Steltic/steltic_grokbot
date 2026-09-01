<!-- chunk_id: F.8A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.8A",
 "example_family": "F.8",
 "chapter": "F",
 "topic": "HSS flexure",
 "clauses": [
  "F7"
 ],
 "eqs": [
  "F7-3",
  "F7-4"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "Square HSS8x8x3/16 Beam with Slender Flange, Continuously Braced",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.8A — Square HSS8x8x3/16 Beam with Slender Flange, Continuously Braced",
 "question": "# F.8A — Square HSS beam with slender flanges (strength and deflection check)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nVerify that a square HSS8×8×3/16 beam is adequate for a simply supported, single-span beam\ncarrying a uniformly distributed load, where the beam is continuously braced and the\nlive-load deflection must not exceed L/240. The section has a slender compression flange.\nConfirm both the flexural strength (LRFD and ASD) and the deflection.\n\n## Given\n- Material: ASTM A500/A500M Grade C (Fy = 50 ksi, E = 29,000 ksi).\n- Member: HSS8×8×3/16 (I = 54.4 in.⁴, b/t = h/t = 43.0, t = 0.174 in., S = 13.6 in.³).\n- Geometry / span: simply supported, L = 21 ft, continuously braced.\n- Loads (service, uniformly distributed): dead wD = 0.125 kip/ft, live wL = 0.375 kip/ft.\n- Serviceability: limit live-load deflection to L/240.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nConfirm the HSS8×8×3/16 has adequate flexural strength (report φ_b M_n and M_n/Ω_b) and\nsatisfies the L/240 live-load deflection limit.",
 "has_figure": false,
 "stem": "F_8A",
 "breadcrumb": "EXAMPLE F.8A · AISC 360-22 Ch.F (HSS flexure) · §F7 · Square HSS8x8x3/16 Beam with Slender Flange, Continuously Braced",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.8A · AISC 360-22 Ch.F (HSS flexure) · §F7 · Square HSS8x8x3/16 Beam with Slender Flange, Continuously Braced

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F7: Eqs. F7-3 and F7-4 (slender flange, effective section modulus); Table B4.1b Cases 17, 19. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 21 ft, continuously braced; wD = 0.125 kip/ft, wL = 0.375 kip/ft:

- **LRFD:** wu = 0.75 kip/ft → Mu = 0.75(21)²/8 = **41.3 kip-ft**
- **ASD:** wa = 0.50 kip/ft → Ma = **27.6 kip-ft**

### 2. Classification — HSS8x8x3/16 (A500 Gr. C)

b/t = h/t = 43.0; t = 0.174 in. Flange (Case 17): λr = 1.40√(E/Fy) = 33.7 < 43.0 → **slender compression flange**. Web (Case 19): 43.0 ≤ λpw = 58.3 → compact. Continuous bracing → LTB N/A.

### 3. Effective Width and Section Modulus — Eq. F7-4

be = 1.92t√(E/Fy)[1 − (0.38/(b/t))√(E/Fy)] = 1.92(0.174)(24.08)[1 − (0.38/43.0)(24.08)] = 8.05(0.787) = **6.33 in.** ≤ b = 43.0(0.174) = 7.48 in.

Removing the ineffective compression-flange width (7.48 − 6.33 = 1.15 in.; ΔA = 0.200 in.²) and recomputing about the shifted neutral axis (shift = 0.151 in.): Ie = 51.2 in.⁴; c = 4.15 in. →

**Se = 51.2/4.15 = 12.3 in.³**

### 4. Flange Local Buckling — Eq. F7-3

Mn = FySe = 50(12.3) = **617 kip-in. = 51.4 kip-ft**

### 5. Available Flexural Strength

- **LRFD:** φbMn = 0.90(51.4) = **46.3 kip-ft** ≥ 41.3 kip-ft ✓ (utilization 0.89)
- **ASD:** Mn/Ωb = 51.4/1.67 = **30.8 kip-ft** ≥ 27.6 kip-ft ✓ (utilization 0.90)

### 6. Deflection Check (Δ_LL ≤ L/240 = 1.05 in.)

I_req = 5(0.375/12)(252)⁴/[384(29,000)(1.05)] = 53.9 in.⁴ ≤ I = 54.4 in.⁴ → Δ_LL = **1.04 in. ≤ 1.05 in. ✓** (gross I appropriate at service stress levels)

### 7. Conclusion

The HSS8x8x3/16 is **adequate**: the slender compression flange limits the strength to Mn = FySe = 51.4 kip-ft via Eqs. F7-3/F7-4 (about 19% below FyZ), yet this still exceeds the demands with ~10% margin, and the L/240 deflection limit is satisfied essentially exactly. Governing limit state: **flange local buckling (slender wall, effective-width method)**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
