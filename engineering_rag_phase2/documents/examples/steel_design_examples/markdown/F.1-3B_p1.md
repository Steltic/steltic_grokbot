<!-- chunk_id: F.1-3B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.1-3B",
 "example_family": "F.1-3",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2"
 ],
 "eqs": [
  "F2-3",
  "F2-4",
  "F2-5",
  "F2-6",
  "F2-8a",
  "F1-1"
 ],
 "tables": [],
 "title": "W18x50 Flexural Check, Braced at Midspan (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.1-3B — W18x50 Flexural Check, Braced at Midspan (Direct Specification)",
 "question": "# F.1-3B — W18x50 flexural check, braced at midspan (direct Specification)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W18x50 of ASTM A992/A992M steel (Fy = 50 ksi) is a simply supported beam spanning 35 ft and\ncarries uniformly distributed service loads of 0.45 kip/ft dead and 0.75 kip/ft live over the full\nspan. Lateral and torsional bracing is provided only at the supports and at midspan, producing two\nequal unbraced segments of 17.5 ft. By directly applying the AISC 360-22 Specification (Section F2\nelastic lateral-torsional buckling, with Cb from Section F1) — not design-aid tables — compute the\nnominal and available flexural strength of the member and verify adequacy for LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Section: W18x50; Zx = 101 in.^3, Sx = 88.9 in.^3, ry = 1.65 in., rts = 1.98 in., J = 1.24 in.^4,\n  ho = 17.4 in. (compact at Fy = 50 ksi).\n- Geometry / span: simple span L = 35 ft; lateral/torsional braces at ends and midspan,\n  Lb = 17.5 ft.\n- Loads (service, uniform): wD = 0.45 kip/ft, wL = 0.75 kip/ft.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe nominal flexural strength Mn from the governing limit state and the available flexural strength\n(phi_b*Mn for LRFD, Mn/Omega_b for ASD), computed directly from the Specification.",
 "has_figure": false,
 "stem": "F_1_3B",
 "breadcrumb": "EXAMPLE F.1-3B · AISC 360-22 Ch.F (beam flexure) · §F2 · W18x50 Flexural Check, Braced at Midspan (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.1-3B · AISC 360-22 Ch.F (beam flexure) · §F2 · W18x50 Flexural Check, Braced at Midspan (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 computed directly: Eqs. F2-3, F2-4, F2-5, F2-6 (c = 1, Eq. F2-8a); Cb per Eq. F1-1. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Mu = 1.74(35)²/8 = **266 kip-ft** (LRFD); Ma = 1.20(35)²/8 = **184 kip-ft** (ASD).

### 2. Direct Specification Calculation (W18x50, A992, compact)

**Limiting lengths:**
Lp = 1.76(1.65)√(29,000/50) = 69.9 in. = **5.83 ft** (Eq. F2-5)
Lr = 1.95(1.98)(29,000/35)√[8.02 × 10⁻⁴ + √((8.02 × 10⁻⁴)² + 6.76(35/29,000)²)] = 203 in. = **17.0 ft** (Eq. F2-6)

Lb = 17.5 ft > Lr → **elastic LTB (Eqs. F2-3/F2-4).**

**Cb (Eq. F1-1):** half-span segment, M = 0 at the support rising parabolically to Mmax at midspan: quarter-point values give Cb = **1.30**.

**Critical stress (Eq. F2-4):** Lb/rts = 210/1.98 = 106

Fcr = 1.30π²(29,000)/(106)² × √[1 + 0.078(1.24/(88.9 × 17.4))(106)²] = (33.1)(1.305) = **43.2 ksi**

**Nominal strength (Eq. F2-3):** Mn = FcrSx = 43.2(88.9) = **3,840 kip-in. = 320 kip-ft** ≤ Mp = FyZx = 421 kip-ft ✓

### 3. Available Flexural Strength

- **LRFD:** φbMn = 0.90(320) = **288 kip-ft** ≥ 266 kip-ft ✓ (0.93)
- **ASD:** Mn/Ωb = 320/1.67 = **192 kip-ft** ≥ 184 kip-ft ✓ (0.96)

### 4. Conclusion

By direct §F2 calculation, the midspan-braced W18x50 (Lb = 17.5 ft > Lr = 17.0 ft) is governed by **elastic lateral-torsional buckling**, Mn = 320 kip-ft with Cb = 1.30. The member is **adequate** for LRFD and ASD (utilizations 0.93 / 0.96), matching the design-aid evaluation of Example F.1-3A. The comparison across F.1-1/2/3 quantifies the strength penalty of reduced bracing: 421 → 339 → 320 kip-ft nominal.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
