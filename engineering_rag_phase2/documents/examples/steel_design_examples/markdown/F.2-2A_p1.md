<!-- chunk_id: F.2-2A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.2-2A",
 "example_family": "F.2-2",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2",
  "F1"
 ],
 "eqs": [
  "F2-1",
  "F2-2",
  "F2-5",
  "F2-6",
  "F2-8b"
 ],
 "tables": [],
 "title": "C15x33.9 Flexural Check, Braced at Fifth Points",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.2-2A — C15x33.9 Flexural Check, Braced at Fifth Points",
 "question": "# F.2-2A — Compact channel flexural member, braced at ends and fifth points (check)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA C15×33.9 American Standard channel of ASTM A992/A992M steel (Fy = 50 ksi) is a simply\nsupported beam spanning 25 ft, carrying uniform dead and live load. It is laterally braced\nat the two supports and at the fifth points of the span, giving five equal unbraced\nsegments of 5.00 ft each. The required flexural strength at midspan is Mu = 108 kip-ft\n(LRFD) and Ma = 71.9 kip-ft (ASD).\n\nDetermine the available flexural strength of the C15×33.9 for this bracing condition. (This\n\"A\" variant is the version the AISC Manual solves using its beam design-aid tables; here we\nreproduce that result by applying the AISC 360 Specification directly and comparing to the\ndesign-aid values.)\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Member: C15×33.9 channel; Sx = 42.0 in³, Zx = 50.8 in³.\n- Geometry: simply supported, L = 25 ft; braced at ends and fifth points ⇒ Lb = 25/5 = 5.00 ft.\n- Moment gradient: uniform load, center segment governs; Cb ≈ 1.00.\n- Required strength: Mu = 108 kip-ft (LRFD), Ma = 71.9 kip-ft (ASD).\n- Code basis: AISC 360-22 (Chapter F).\n\n## Find\nThe available flexural strength (LRFD and ASD) and whether the member is adequate, with the\nresult compared to the AISC Manual beam design-aid (Table 3-11) values.",
 "has_figure": false,
 "stem": "F_2_2A",
 "breadcrumb": "EXAMPLE F.2-2A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · C15x33.9 Flexural Check, Braced at Fifth Points",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.2-2A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · C15x33.9 Flexural Check, Braced at Fifth Points

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 (Eqs. F2-1, F2-2, F2-5, F2-6 with the channel coefficient c per Eq. F2-8b); Cb per §F1. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Mu = **108 kip-ft** (LRFD); Ma = **71.9 kip-ft** (ASD). Bracing at ends and fifth points → Lb = 5.00 ft = 60 in.; center segment governs with **Cb = 1.00**.

### 2. LTB Parameters — C15x33.9

ry = 0.901 in.; Iy = 8.07 in.⁴; Cw = 492 in.⁶; J = 1.01 in.⁴; ho = 14.4 in.; Sx = 42.0 in.³; Zx = 50.8 in.³

Lp = 1.76ry√(E/Fy) = 1.76(0.901)√580 = 38.2 in. = **3.18 ft** (Eq. F2-5)

Channel coefficient (Eq. F2-8b): c = (ho/2)√(Iy/Cw) = (14.4/2)√(8.07/492) = **0.919**
rts² = √(IyCw)/Sx = √(8.07 × 492)/42.0 = 1.50 → rts = 1.22 in. (Eq. F2-7)
Jc/(Sxho) = 1.01(0.919)/[42.0(14.4)] = 1.54 × 10⁻³
Lr = 1.95rts(E/0.7Fy)√[1.54 × 10⁻³ + √((1.54 × 10⁻³)² + 6.76(35/29,000)²)] = 140 in. = **11.7 ft** (Eq. F2-6)

Lp = 3.18 ft < Lb = 5.00 ft ≤ Lr = 11.7 ft → **inelastic LTB, Eq. F2-2.**

### 3. Nominal Strength — Eq. F2-2

Mp = FyZx = 50(50.8) = 2,540 kip-in.; 0.7FySx = 35(42.0) = 1,470 kip-in.

Mn = Cb[Mp − (Mp − 0.7FySx)((Lb − Lp)/(Lr − Lp))] = 1.00[2,540 − (1,070)(60 − 38.2)/(140 − 38.2)]
= 2,540 − 1,070(0.213) = **2,310 kip-in. = 193 kip-ft** (≤ Mp ✓)

### 4. Available Flexural Strength

- **LRFD:** φbMn = 0.90(193) = **173 kip-ft** ≥ 108 kip-ft ✓ (utilization 0.62)
- **ASD:** Mn/Ωb = 193/1.67 = **115 kip-ft** ≥ 71.9 kip-ft ✓ (utilization 0.62)

### 5. Conclusion

With fifth-point bracing (Lb = 5.00 ft between Lp and Lr), the C15x33.9 is governed by **inelastic lateral-torsional buckling** of the center segment (Cb = 1.00), giving φbMn = 173 kip-ft and Mn/Ωb = 115 kip-ft — consistent with the AISC Manual design-aid values and adequate for the required 108 / 71.9 kip-ft with ~38% reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
