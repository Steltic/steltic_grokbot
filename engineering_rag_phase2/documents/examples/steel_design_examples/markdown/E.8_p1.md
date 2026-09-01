<!-- chunk_id: E.8_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.8",
 "example_family": "E.8",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E3",
  "E4",
  "E7",
  "E1",
  "E7.1"
 ],
 "eqs": [
  "E3-3",
  "E3-4",
  "E4-3",
  "E4-6",
  "E4-7",
  "E4-8",
  "E4-9",
  "E7-1",
  "E7-2"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "WT Compression Member with Slender Elements",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.8 — WT Compression Member with Slender Elements",
 "question": "# E.8 — WT compression member with slender elements (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect a lightweight ASTM A992/A992M WT-shape for a 20-ft, pin-ended axial compression\nmember carrying a service dead load of 6 kips and a service live load of 18 kips. The\ncandidate shape has a slender stem, so the effective-area provisions of §E7 must be\nchecked. Verify by hand calculation (AISC 360-22) that the available compressive\nstrength (LRFD and ASD) is adequate, considering flexural buckling about both axes,\nflexural-torsional buckling, and local buckling of the stem.\n\n## Given\n- Material: ASTM A992/A992M, F_y = 50 ksi, E = 29,000 ksi, G = 11,200 ksi.\n- Geometry / span: L = 20.0 ft, pinned both ends (K = 1.0), L_cx = L_cy = 20.0 ft.\n- Loads: P_D = 6 kips, P_L = 18 kips (axial).\n- Trial member (to verify): WT7×15, with A_g = 4.42 in.², I_x = 19.0 in.⁴,\n  I_y = 9.79 in.⁴, J = 0.190 in.⁴, r_x = 2.07 in., r_y = 1.49 in., t_w = 0.270 in.,\n  t_f = 0.385 in., ȳ = 1.58 in., C_w = 0.287 in.⁶, b_f/2t_f = 8.74, d/t_w = 25.6.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nClassify the elements, compute φ_cP_n and P_n/Ω_c (including any §E7 effective-area\nreduction), and confirm adequacy.",
 "has_figure": false,
 "stem": "E_8",
 "breadcrumb": "EXAMPLE E.8 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E4 §E7 §E1 §E7.1 · WT Compression Member with Slender Elements",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.8 · AISC 360-22 Ch.E (column / axial compression) · §E3 §E4 §E7 §E1 §E7.1 · WT Compression Member with Slender Elements

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E3 (Eqs. E3-3, E3-4), §E4 (Eq. E4-3 with E4-6/E4-7/E4-8/E4-9), §E7 (Eqs. E7-1, E7-2), Table B4.1a (Cases 1, 4). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(6) + 1.6(18) = **36.0 kips**
- **ASD:** Pa = 6 + 18 = **24.0 kips**

### 2. Trial Member and Classification — WT7x15 (A992)

Ag = 4.42 in.²; Ix = 19.0 in.⁴; Iy = 9.79 in.⁴; rx = 2.07 in.; ry = 1.49 in.; J = 0.190 in.⁴; Cw = 0.287 in.⁶; ȳ = 1.58 in.; tf = 0.385 in. Lc = 240 in. all axes.

Table B4.1a: flange (Case 1): 8.74 ≤ 13.5 ✓ nonslender; **stem (Case 4): d/tw = 25.6 > 0.75√(E/Fy) = 18.1 → slender** → member evaluated under §E7 (Pn = FnAe).

### 3. Buckling Modes

- **Flexural, x:** Lc/rx = 240/2.07 = 116 → Fe = π²E/(116)² = 21.3 ksi (Eq. E3-4)
- **Flexural, y:** Lc/ry = 240/1.49 = 161 → Fey = 11.0 ksi (Eq. E4-6)
- **Flexural-torsional (Eq. E4-3, y = axis of symmetry):**
  yo = 1.58 − 0.385/2 = 1.39 in.; r̄o² = yo² + (Ix + Iy)/Ag = 1.93 + 6.51 = 8.44 in.² (Eq. E4-9); H = 1 − 1.93/8.44 = 0.772 (Eq. E4-8)
  Fez = [π²ECw/Lcz² + GJ]/(Agr̄o²) = [1.4 + 11,200(0.190)]/[4.42(8.44)] = 57.1 ksi (Eq. E4-7)
  Fe = [(11.0 + 57.1)/(2 × 0.772)][1 − √(1 − 4(11.0)(57.1)(0.772)/(68.1)²)] = (44.1)(0.238) = **10.5 ksi** ← **governs**

### 4. Nominal Stress — §E3 (via §E7)

Fy/Fe = 50/10.5 = 4.77 > 2.25 → elastic, Eq. E3-3:

Fn = 0.877Fe = 0.877(10.5) = **9.20 ksi**

### 5. Effective Area — §E7.1, Eq. E7-2

Reduction is required only when λ > λr√(Fy/Fn):

λr√(Fy/Fn) = 18.1√(50/9.20) = **42.1** > λ = 25.6 → **stem fully effective at the governing (low) stress**; Ae = Ag = 4.42 in.²

### 6. Available Compressive Strength — Eq. E7-1

Pn = FnAe = 9.20(4.42) = **40.7 kips**

- **LRFD:** φcPn = 0.90(40.7) = **36.6 kips** ≥ 36.0 kips ✓ (utilization 0.98)
- **ASD:** Pn/Ωc = 40.7/1.67 = **24.4 kips** ≥ 24.0 kips ✓ (utilization 0.98)

### 7. Conclusion

**The WT7x15 is adequate**, governed by elastic flexural-torsional buckling (Fe = 10.5 ksi, Eq. E4-3). Although the stem is slender by classification (25.6 > 18.1), the §E7 stress-dependent check shows no effective-width reduction is required at the low governing stress (25.6 ≤ 42.1), so the full area is used. Margins are tight (≈2%) — any change in length or loads warrants reverification.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
