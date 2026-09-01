<!-- chunk_id: E.7_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.7",
 "example_family": "E.7",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E3",
  "E4",
  "E1",
  "E7"
 ],
 "eqs": [
  "E3-1",
  "E3-3",
  "E3-4",
  "E4-3",
  "E4-6",
  "E4-7",
  "E4-8",
  "E4-9"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "WT Compression Member Without Slender Elements",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.7 — WT Compression Member Without Slender Elements",
 "question": "# E.7 — WT compression member without slender elements (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect the lightest ASTM A992/A992M WT-shape with no slender elements to serve as a\n20-ft, pin-ended axial compression member carrying a service dead load of 20 kips and\na service live load of 60 kips. After selecting a trial shape, verify by hand\ncalculation (AISC 360-22) that its available compressive strength (LRFD and ASD) is\nadequate, considering flexural buckling about both axes and flexural-torsional\nbuckling.\n\n## Given\n- Material: ASTM A992/A992M, F_y = 50 ksi, E = 29,000 ksi, G = 11,200 ksi.\n- Geometry / span: L = 20.0 ft, pinned both ends (K = 1.0), L_cx = L_cy = 20.0 ft.\n- Loads: P_D = 20 kips, P_L = 60 kips (axial).\n- Trial member (to verify): WT7×34, with A_g = 10.0 in.², I_x = 32.6 in.⁴,\n  I_y = 60.7 in.⁴, J = 1.50 in.⁴, r_x = 1.81 in., r_y = 2.46 in., t_f = 0.720 in.,\n  ȳ = 1.29 in., C_w = 3.21 in.⁶, b_f/2t_f = 6.97, d/t_w = 16.9.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nConfirm WT7×34 is nonslender, compute φ_cP_n and P_n/Ω_c, and confirm adequacy for the\nrequired strength.",
 "has_figure": false,
 "stem": "E_7",
 "breadcrumb": "EXAMPLE E.7 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E4 §E1 §E7 · WT Compression Member Without Slender Elements",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.7 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E4 §E1 §E7 · WT Compression Member Without Slender Elements

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E3 (Eqs. E3-1, E3-3, E3-4), §E4 (Eq. E4-3 with E4-6, E4-7, E4-8, E4-9), Table B4.1a (Cases 1, 4). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(20) + 1.6(60) = **120 kips**
- **ASD:** Pa = 20 + 60 = **80 kips**

### 2. Trial Member and Classification — WT7x34 (A992)

Ag = 10.0 in.²; Ix = 32.6 in.⁴; Iy = 60.7 in.⁴; rx = 1.81 in.; ry = 2.46 in.; J = 1.50 in.⁴; Cw = 3.21 in.⁶; ȳ = 1.29 in.; tf = 0.720 in. Lc = 20 ft = 240 in. all axes.

Table B4.1a: flange (Case 1): bf/2tf = 6.97 ≤ 0.56√(E/Fy) = 13.5 ✓; stem (Case 4): d/tw = 16.9 ≤ 0.75√(E/Fy) = 18.1 ✓ → **nonslender** (no §E7 reduction), as required by the selection.

### 3. Buckling Modes

**(a) Flexural about x-axis (§E3):** Lc/rx = 240/1.81 = **133** → Fe = π²E/(133)² = **16.3 ksi** (Eq. E3-4) ← **governs**

**(b) Flexural about y-axis:** Lc/ry = 240/2.46 = 97.6 → Fey = **30.1 ksi** (Eq. E4-6)

**(c) Flexural-torsional (§E4, Eq. E4-3, y = axis of symmetry):**
Shear center at flange mid-thickness: yo = ȳ − tf/2 = 1.29 − 0.36 = 0.93 in.
r̄o² = yo² + (Ix + Iy)/Ag = 0.865 + 93.3/10.0 = **10.2 in.²** (Eq. E4-9); H = 1 − yo²/r̄o² = **0.915** (Eq. E4-8)
Fez = [π²ECw/Lcz² + GJ]/(Ag r̄o²) = [16.0 + 11,200(1.50)]/[10.0(10.2)] = **165 ksi** (Eq. E4-7; Cw term negligible per User Note)
Fe = [(30.1 + 165)/(2 × 0.915)][1 − √(1 − 4(30.1)(165)(0.915)/(195.1)²)] = (107)(0.277) = **29.5 ksi**

### 4. Critical Stress and Strength

Governing Fe = 16.3 ksi (x-axis flexural buckling). Fy/Fe = 50/16.3 = 3.07 > 2.25 → elastic, Eq. E3-3:

Fn = 0.877Fe = 0.877(16.3) = **14.3 ksi**

Pn = FnAg = 14.3(10.0) = **143 kips** (Eq. E3-1)

- **LRFD:** φcPn = 0.90(143) = **129 kips** ≥ 120 kips ✓ (utilization 0.93)
- **ASD:** Pn/Ωc = 143/1.67 = **85.5 kips** ≥ 80 kips ✓ (utilization 0.94)

### 5. Conclusion

**Select WT7x34 (A992).** The shape is fully nonslender, and elastic flexural buckling about the x-axis (Lc/rx = 133) governs — the flexural-torsional mode (29.5 ksi) and y-axis mode (30.1 ksi) are nearly twice the governing elastic stress. The available strength of **129 kips (LRFD) / 85.5 kips (ASD)** confirms adequacy for the 120 / 80 kip demands with ~6% margin, making the WT7x34 the lightest nonslender WT satisfying the requirement.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
