<!-- chunk_id: F.2-2B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.2-2B",
 "example_family": "F.2-2",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2"
 ],
 "eqs": [
  "F2-2",
  "F2-5",
  "F2-6",
  "F2-7",
  "F2-8b",
  "F1-1"
 ],
 "tables": [],
 "title": "C15x33.9 Flexural Check, Braced at Fifth Points (Direct Specification)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.2-2B — C15x33.9 Flexural Check, Braced at Fifth Points (Direct Specification)",
 "question": "# F.2-2B — Compact channel flexural member, braced at ends and fifth points (check, direct Spec)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA C15×33.9 American Standard channel of ASTM A992/A992M steel (Fy = 50 ksi) spans 25 ft as\na simply supported, uniformly loaded beam. It is laterally braced at the supports and at the\nfifth points, producing five equal 5.00-ft unbraced segments. The required flexural strength\nat midspan is Mu = 108 kip-ft (LRFD) and Ma = 71.9 kip-ft (ASD).\n\nBy directly applying the AISC 360 Specification equations of Section F2 (including the\nchannel form of the lateral-torsional-buckling coefficient), compute the nominal and\navailable flexural strength of the channel for the center (governing) unbraced segment.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Member: C15×33.9 channel; Sx = 42.0 in³, Zx = 50.8 in³, ry = 0.901 in, Iy = 8.07 in⁴,\n  J = 1.01 in⁴, Cw = 492 in⁶, d = 15.0 in, tf = 0.650 in (ho = d − tf = 14.4 in).\n- Geometry: simply supported, L = 25 ft; braced at ends and fifth points ⇒ Lb = 5.00 ft.\n- Moment gradient: center segment governs, Cb = 1.00.\n- Required strength: Mu = 108 kip-ft (LRFD), Ma = 71.9 kip-ft (ASD).\n- Code basis: AISC 360-22 (Chapter F).\n\n## Find\nThe nominal flexural strength Mn (Section F2) and the available flexural strength\n(φ_b·Mn and Mn/Ω_b), and whether the member is adequate.",
 "has_figure": false,
 "stem": "F_2_2B",
 "breadcrumb": "EXAMPLE F.2-2B · AISC 360-22 Ch.F (beam flexure) · §F2 · C15x33.9 Flexural Check, Braced at Fifth Points (Direct Specification)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.2-2B · AISC 360-22 Ch.F (beam flexure) · §F2 · C15x33.9 Flexural Check, Braced at Fifth Points (Direct Specification)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 computed directly: Eqs. F2-2, F2-5, F2-6, F2-7, with the channel LTB coefficient c per Eq. F2-8b; Cb per Eq. F1-1. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Mu = **108 kip-ft** (LRFD); Ma = **71.9 kip-ft** (ASD). Lb = 5.00 ft = 60 in.; governing center segment, Cb = 1.00.

### 2. Direct Specification Calculation

**Channel coefficient (Eq. F2-8b):**
c = (ho/2)√(Iy/Cw) = (14.4/2)√(8.07/492) = 7.20(0.128) = **0.919**

**Effective radius of gyration (Eq. F2-7):** rts² = √(IyCw)/Sx = √(3,970)/42.0 = 1.50 → **rts = 1.22 in.**

**Limiting lengths:**
Lp = 1.76(0.901)√(29,000/50) = **38.2 in.** (Eq. F2-5)
Jc/(Sxho) = (1.01)(0.919)/[42.0(14.4)] = 1.54 × 10⁻³
Lr = 1.95(1.22)(29,000/35)√[1.54 × 10⁻³ + √((1.54 × 10⁻³)² + 6.76(35/29,000)²)] = 1,979(0.0710) = **140 in.** (Eq. F2-6)

**Classification:** Lp = 38.2 in. < Lb = 60 in. ≤ Lr = 140 in. → inelastic LTB, Eq. F2-2:

Mn = 1.00[2,540 − (2,540 − 1,470)((60 − 38.2)/(140 − 38.2))] = 2,540 − 228 = **2,310 kip-in. = 193 kip-ft**

### 3. Available Flexural Strength

- **LRFD:** φbMn = 0.90(193) = **173 kip-ft** ≥ 108 kip-ft ✓
- **ASD:** Mn/Ωb = 193/1.67 = **115 kip-ft** ≥ 71.9 kip-ft ✓

### 4. Conclusion

Direct application of §F2 — including the channel-specific coefficient c = 0.919 (Eq. F2-8b), which reduces the torsional contribution relative to a doubly symmetric I-shape (c = 1) — gives Mn = 193 kip-ft governed by **inelastic LTB** of the 5-ft center segment. The C15x33.9 is **adequate** at 62% utilization under both LRFD and ASD, matching the design-aid result of Example F.2-2A.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
