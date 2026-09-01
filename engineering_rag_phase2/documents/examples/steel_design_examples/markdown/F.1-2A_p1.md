<!-- chunk_id: F.1-2A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.1-2A",
 "example_family": "F.1-2",
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
  "F1-1"
 ],
 "tables": [],
 "title": "W18x50 Flexural Check, Braced at Third Points",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.1-2A — W18x50 Flexural Check, Braced at Third Points",
 "question": "# F.1-2A — W18x50 flexural check, braced at third points  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W18x50 of ASTM A992/A992M steel (Fy = 50 ksi) is used as a simply supported beam spanning 35 ft,\ncarrying uniformly distributed service loads of 0.45 kip/ft dead and 0.75 kip/ft live over the full\nspan. The beam is braced against lateral displacement and twist at the supports and at the two\nthird points only (three equal unbraced segments). Determine the available flexural strength of the\nW18x50 (LRFD and ASD) accounting for the moment-gradient effect, and verify adequacy.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Section: W18x50; Zx = 101 in.^3, Sx = 88.9 in.^3, ry = 1.65 in., rts = 1.98 in., J = 1.24 in.^4,\n  ho = 17.4 in. (compact at Fy = 50 ksi).\n- Geometry / span: simple span L = 35 ft; lateral braces at ends and third points -> Lb = 11.7 ft.\n- Loads (service, uniform): wD = 0.45 kip/ft, wL = 0.75 kip/ft.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nThe available flexural strength (phi_b*Mn for LRFD, Mn/Omega_b for ASD), including the lateral-\ntorsional buckling limit state and the Cb moment-gradient factor, and confirm it exceeds the\nrequired strength.",
 "has_figure": false,
 "stem": "F_1_2A",
 "breadcrumb": "EXAMPLE F.1-2A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · W18x50 Flexural Check, Braced at Third Points",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.1-2A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · W18x50 Flexural Check, Braced at Third Points

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 (Eqs. F2-1, F2-2, F2-5, F2-6) with Cb per §F1 (Eq. F1-1). φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** wu = 1.74 kip/ft → Mu = 1.74(35)²/8 = **266 kip-ft**
- **ASD:** wa = 1.20 kip/ft → Ma = **184 kip-ft**

### 2. LTB Parameters — W18x50 (compact, A992)

Zx = 101 in.³; Sx = 88.9 in.³; ry = 1.65 in.; rts = 1.98 in.; J = 1.24 in.⁴; ho = 17.4 in. Lb = 35/3 = 11.7 ft = 140 in.

Lp = 1.76ry√(E/Fy) = 1.76(1.65)√580 = 69.9 in. = **5.83 ft** (Eq. F2-5)
Lr = 1.95rts(E/0.7Fy)√[Jc/(Sxho) + √((Jc/(Sxho))² + 6.76(0.7Fy/E)²)] = 203 in. = **17.0 ft** (Eq. F2-6, c = 1)

Lp < Lb = 11.7 ft ≤ Lr → **inelastic LTB, Eq. F2-2.**

### 3. Moment Gradient Factor

For a uniformly loaded simple span braced at the third points, the **center segment governs** (highest moment, flattest gradient): Cb = 1.01 (Eq. F1-1). (The outer segments have Cb = 1.46 with lower moment — not critical.)

### 4. Nominal Strength — Eq. F2-2

Mp = FyZx = 5,050 kip-in.; 0.7FySx = 35(88.9) = 3,110 kip-in.

Mn = Cb[Mp − (Mp − 0.7FySx)((Lb − Lp)/(Lr − Lp))] ≤ Mp
= 1.01[5,050 − (1,940)((140 − 69.9)/(203 − 69.9))] = 1.01[5,050 − 1,940(0.525)] = 1.01(4,030) = **4,070 kip-in. = 339 kip-ft** (≤ Mp ✓)

### 5. Available Flexural Strength

- **LRFD:** φbMn = 0.90(339) = **305 kip-ft** ≥ 266 kip-ft ✓ (utilization 0.87)
- **ASD:** Mn/Ωb = 339/1.67 = **203 kip-ft** ≥ 184 kip-ft ✓ (utilization 0.91)

### 6. Conclusion

With bracing at the ends and third points (Lb = 11.7 ft, between Lp and Lr), the W18x50 is governed by **inelastic lateral-torsional buckling in the center segment** (Cb = 1.01), giving φbMn = 305 kip-ft and Mn/Ωb = 203 kip-ft. **The member is adequate** for the 266 / 184 kip-ft demands.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
