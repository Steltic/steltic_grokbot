<!-- chunk_id: F.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.6",
 "example_family": "F.6",
 "chapter": "F",
 "topic": "HSS flexure",
 "clauses": [
  "F7",
  "F7.2"
 ],
 "eqs": [
  "F7-1",
  "F7-2"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "Square HSS Flexural Member, Continuously Braced",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.6 — Square HSS Flexural Member, Continuously Braced",
 "question": "# F.6 — Square HSS flexural member with compact (near-limit) flanges  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported floor beam spans 7.5 ft and is laterally braced continuously along its\nlength. It carries a uniform service dead load of 0.145 kip/ft and a uniform service live\nload of 0.435 kip/ft (the dead load includes the beam self-weight). The member is a square\nHSS of ASTM A500/A500M Grade C steel bent about its geometric (major) axis. The live-load\ndeflection is limited to L/240.\n\nSelect the lightest adequate square HSS, then, applying the AISC 360 Specification directly,\nclassify the flange and web, determine the governing flexural limit state, and report the\navailable flexural strengths φ_b M_n (LRFD) and M_n/Ω_b (ASD). Also confirm the live-load\ndeflection limit.\n\n## Given\n- Material: ASTM A500/A500M Grade C (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simple span L = 7.5 ft; continuously braced (L_b = 0).\n- Loads (service, uniform): w_D = 0.145 kip/ft, w_L = 0.435 kip/ft.\n- Live-load deflection limit: L/240.\n- Member: select a square HSS (major-axis bending).\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe required strengths M_u and M_a, the minimum required moment of inertia, a suitable\nsquare HSS, its flange/web classification, the nominal moment M_n and the available\nstrengths φ_b M_n and M_n/Ω_b, plus a deflection check.",
 "has_figure": false,
 "stem": "F_6",
 "breadcrumb": "EXAMPLE F.6 · AISC 360-22 Ch.F (HSS flexure) · §F7 §F7.2 · Square HSS Flexural Member, Continuously Braced",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.6 · AISC 360-22 Ch.F (HSS flexure) · §F7 §F7.2 · Square HSS Flexural Member, Continuously Braced

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F7 (Square and Rectangular HSS): Eqs. F7-1, F7-2; Table B4.1b Cases 17 (flange) and 19 (web). φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 7.5 ft, continuously braced; wD = 0.145 kip/ft, wL = 0.435 kip/ft:

- **LRFD:** wu = 1.2(0.145) + 1.6(0.435) = 0.870 kip/ft → Mu = 0.870(7.5)²/8 = **6.12 kip-ft** (73.4 kip-in.)
- **ASD:** wa = 0.580 kip/ft → Ma = **4.08 kip-ft** (48.9 kip-in.)

### 2. Serviceability Requirement (Δ_LL ≤ L/240 = 0.375 in.)

I_req = 5(0.435/12)(90)⁴/[384(29,000)(0.375)] = **2.85 in.⁴**

### 3. Selection and Classification — HSS3-1/2x3-1/2x1/8 (A500 Gr. C)

Z = 1.93 in.³; S = 1.66 in.³; I = 2.90 in.⁴ ≥ 2.85 ✓; b/t = h/t = 27.2 (t = 0.116 in. design).

- **Flange (Table B4.1b Case 17):** λp = 1.12√(E/Fy) = 27.0; λr = 1.40√(E/Fy) = 33.7 → 27.0 < 27.2 < 33.7 → **noncompact flange**
- **Web (Case 19):** λpw = 2.42√(E/Fy) = 58.3 > 27.2 → compact web
- LTB: square section, continuously braced → not applicable.

### 4. Flange Local Buckling — §F7.2, Eq. F7-2

Mp = FyZ = 50(1.93) = 96.5 kip-in.; FyS = 50(1.66) = 83.0 kip-in.

Mn = Mp − (Mp − FyS)[(λ − λp)/(λr − λp)] = 96.5 − (13.5)[(27.2 − 27.0)/(33.7 − 27.0)] = 96.5 − 0.4 = **96.1 kip-in. = 8.01 kip-ft** (≤ Mp ✓)

### 5. Available Flexural Strength

- **LRFD:** φbMn = 0.90(96.1) = 86.5 kip-in. = **7.21 kip-ft** ≥ 6.12 kip-ft ✓ (utilization 0.85)
- **ASD:** Mn/Ωb = 96.1/1.67 = 57.5 kip-in. = **4.79 kip-ft** ≥ 4.08 kip-ft ✓ (utilization 0.85)

### 6. Deflection Check

Δ_LL = 0.375(2.85/2.90) = **0.37 in. ≤ 0.375 in. ✓**

### 7. Conclusion

**Select HSS3-1/2x3-1/2x1/8 (A500 Gr. C).** The walls are just past the compact limit (27.2 vs. 27.0), so the governing limit state is **flange local buckling per Eq. F7-2**, though the reduction from Mp is under 1%. Available strengths of 7.21 kip-ft (LRFD) and 4.79 kip-ft (ASD) exceed the demands, and the L/240 deflection limit is met essentially exactly — both stiffness and strength are efficiently utilized.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
