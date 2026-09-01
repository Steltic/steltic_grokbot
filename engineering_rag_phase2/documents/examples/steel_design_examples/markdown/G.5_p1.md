<!-- chunk_id: G.5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.5",
 "example_family": "G.5",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G5",
  "G1"
 ],
 "eqs": [
  "G5-1",
  "G5-2a",
  "G5-2b"
 ],
 "tables": [],
 "title": "Round HSS Shear Strength",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.5 — Round HSS Shear Strength",
 "question": "# G.5 -- Round HSS in Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A500/A500M Grade C round HSS16.000x0.375 spans 32 ft as a simply supported\nbeam under uniform load, producing end shears of 30 kips from service dead load and\n90 kips from service live load. Determine the available shear strength directly from\nAISC 360 Section G5 and verify adequacy for LRFD and ASD. (Take the distance from\nmaximum to zero shear, Lv, as half the span.)\n\n## Given\n- Material: ASTM A500/A500M Grade C round HSS, Fy = 50 ksi.\n- Member: HSS16.000x0.375; Ag = 17.2 in.^2, D = 16.0 in., D/t = 45.8.\n- Span: 32 ft, simply supported, uniform load; Lv = 16 ft = 192 in.\n- Loads (service end shear): D = 30 kips, L = 90 kips.\n- Code basis: AISC 360-22 Sections G1, G5; loads per ASCE/SEI 7 Ch. 2.\n\n## Find\nphi_v*Vn, Vn/Omega_v, and adequacy.",
 "has_figure": false,
 "stem": "G_5",
 "breadcrumb": "EXAMPLE G.5 · AISC 360-22 Ch.G (beam shear) · §G5 §G1 · Round HSS Shear Strength",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.5 · AISC 360-22 Ch.G (beam shear) · §G5 §G1 · Round HSS Shear Strength

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G5 (Eqs. G5-1, G5-2a, G5-2b; Fcr ≤ 0.6Fy); φv = 0.90, Ωv = 1.67 (§G1). Per the RAG extract provided.

---

### 1. Required Shear Strength

D = 30 kips, L = 90 kips:

- **LRFD:** Vu = 1.2(30) + 1.6(90) = **180 kips**
- **ASD:** Va = 30 + 90 = **120 kips**

### 2. Critical Shear Stress — §G5

HSS16.000x0.375 (A500 Gr. C): Ag = 17.2 in.²; D = 16.0 in.; D/t = 45.8; Lv = 16 ft = 192 in. (distance from maximum to zero shear).

Fcr is the larger of:

- **Eq. G5-2a:** Fcr = 1.60E/[√(Lv/D)(D/t)^(5/4)] = 1.60(29,000)/[√12 (45.8)^1.25] = 46,400/[3.46(119)] = **112 ksi**
- **Eq. G5-2b:** Fcr = 0.78E/(D/t)^(3/2) = 0.78(29,000)/(45.8)^1.5 = 22,600/310 = **73.0 ksi**

but not greater than 0.6Fy = 30 ksi → **Fcr = 30.0 ksi** (shear yielding controls, as the User Note anticipates for standard sections).

### 3. Nominal and Available Shear Strength — Eq. G5-1

Vn = FcrAg/2 = 30.0(17.2)/2 = **258 kips**

- **LRFD:** φvVn = 0.90(258) = **232 kips** ≥ 180 kips ✓ (utilization 0.78)
- **ASD:** Vn/Ωv = 258/1.67 = **154 kips** ≥ 120 kips ✓ (utilization 0.78)

### 4. Conclusion

For the HSS16.000x0.375, both shear-buckling expressions far exceed the 0.6Fy ceiling, so **shear yielding on half the gross area governs** (Eq. G5-1 with Fcr = 0.6Fy). The available strengths of 232 kips (LRFD) and 154 kips (ASD) exceed the required 180 / 120 kips — **the member is adequate in shear**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
