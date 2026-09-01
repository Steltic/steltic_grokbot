<!-- chunk_id: F.1-2B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.1-2B",
 "example_family": "F.1-2",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2"
 ],
 "eqs": [
  "F2-1",
  "F2-2",
  "F2-5",
  "F2-6",
  "F2-8a",
  "F1-1"
 ],
 "tables": [],
 "title": "W18x50 Flexural Check, Braced at Third Points (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.1-2B — W18x50 Flexural Check, Braced at Third Points (Direct Specification)",
 "question": "# F.1-2B — W18x50 flexural check, braced at third points (direct Specification)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W18x50 of ASTM A992/A992M steel (Fy = 50 ksi) is a simply supported beam spanning 35 ft and\ncarries uniformly distributed service loads of 0.45 kip/ft dead and 0.75 kip/ft live over the full\nspan. Lateral and torsional bracing is provided only at the supports and at the two third points,\ngiving three equal unbraced segments of length 11.7 ft. By directly applying the AISC 360-22\nSpecification equations (Section F2, with Cb from Section F1) — not design-aid tables — compute the\nnominal and available flexural strength of the member and verify adequacy for LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Section: W18x50; Zx = 101 in.^3, Sx = 88.9 in.^3, ry = 1.65 in., rts = 1.98 in., J = 1.24 in.^4,\n  ho = 17.4 in. (compact at Fy = 50 ksi).\n- Geometry / span: simple span L = 35 ft; lateral/torsional braces at ends and third points,\n  Lb = 11.7 ft.\n- Loads (service, uniform): wD = 0.45 kip/ft, wL = 0.75 kip/ft.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe nominal flexural strength Mn from the governing limit state and the available flexural strength\n(phi_b*Mn for LRFD, Mn/Omega_b for ASD), computed directly from the Specification.",
 "has_figure": false,
 "stem": "F_1_2B",
 "breadcrumb": "EXAMPLE F.1-2B · AISC 360-22 Ch.F (beam flexure) · §F2 · W18x50 Flexural Check, Braced at Third Points (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.1-2B · AISC 360-22 Ch.F (beam flexure) · §F2 · W18x50 Flexural Check, Braced at Third Points (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 computed directly: Eqs. F2-1, F2-2, F2-5, F2-6 (c = 1, Eq. F2-8a); Cb per Eq. F1-1. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Mu = 1.74(35)²/8 = **266 kip-ft** (LRFD); Ma = 1.20(35)²/8 = **184 kip-ft** (ASD).

### 2. Direct Specification Calculation (W18x50, A992, compact)

**Limiting lengths:**
Lp = 1.76ry√(E/Fy) = 1.76(1.65)√(29,000/50) = **69.9 in. (5.83 ft)** (Eq. F2-5)

Jc/(Sxho) = 1.24(1)/[88.9(17.4)] = 8.02 × 10⁻⁴
Lr = 1.95rts(E/0.7Fy)√[8.02 × 10⁻⁴ + √((8.02 × 10⁻⁴)² + 6.76(35/29,000)²)]
= 1.95(1.98)(828.6)√(4.04 × 10⁻³) = 3,199(0.0636) = **203 in. (17.0 ft)** (Eq. F2-6)

**Segment classification:** Lb = 140 in.; Lp = 69.9 < 140 ≤ 203 → Eq. F2-2 (inelastic LTB).

**Cb (Eq. F1-1), governing center segment** (x = 11.67 ft to 23.33 ft; symmetric about midspan):
Quarter-point moments as fractions of Mmax give Cb = 12.5Mmax/(2.5Mmax + 3MA + 4MB + 3MC) = **1.01**.

**Nominal strength (Eq. F2-2):**
Mp = FyZx = 50(101) = 5,050 kip-in.; 0.7FySx = 3,110 kip-in.
Mn = 1.01[5,050 − (5,050 − 3,110)(140 − 69.9)/(203 − 69.9)] = 1.01(4,030) = **4,070 kip-in. = 339 kip-ft ≤ Mp ✓**

### 3. Available Flexural Strength

- **LRFD:** φbMn = 0.90(339) = **305 kip-ft** ≥ 266 kip-ft ✓
- **ASD:** Mn/Ωb = 339/1.67 = **203 kip-ft** ≥ 184 kip-ft ✓

### 4. Conclusion

Computed directly from §F2 (no design aids), the W18x50 braced at third points has Mn = 339 kip-ft governed by **inelastic LTB (Eq. F2-2) in the center segment with Cb = 1.01**. Available strengths of 305 kip-ft (LRFD) and 203 kip-ft (ASD) confirm adequacy at 87% / 91% utilization — identical to the design-aid result of Example F.1-2A, as expected.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
