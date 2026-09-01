<!-- chunk_id: I.4_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.4",
 "example_family": "I.4",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I2.2"
 ],
 "eqs": [
  "I2-9a",
  "I2-12",
  "I2-13",
  "I2-2",
  "I2-3"
 ],
 "tables": [
  "I1.1a"
 ],
 "title": "Filled Composite Column in Axial Compression",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.4 — Filled Composite Column in Axial Compression",
 "question": "# I.4 — Filled (concrete-filled HSS) composite column in axial compression  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 14-ft-long concrete-filled rectangular HSS is used as an axially loaded,\npin-ended interior column. The steel section is an ASTM A500/A500M Grade C\nHSS10×6×3/8 (Fy = 50 ksi). The HSS is completely filled with normal-weight\nconcrete (wc = 145 lb/ft³) with a specified compressive strength f′c = 5 ksi.\nThere is no longitudinal reinforcement in the fill (Asr = 0). The member is\npinned top and bottom about both axes (K = 1.0), so the effective length is\nLc = 14 ft for both the x-x and y-y axes.\n\nThe column carries an axial dead load D = 32 kips and an axial live load\nL = 84 kips, both in compression. Determine whether the filled composite\ncolumn is adequate, i.e. compute the available compressive strength (LRFD\ndesign strength φcPn and ASD allowable strength Pn/Ωc) by direct application\nof the AISC 360 Chapter I provisions (not the Manual capacity tables) and\ncompare it to the required strength.\n\n## Given\n- Material: steel ASTM A500/A500M Gr. C, Fy = 50 ksi, Es = 29,000 ksi;\n  concrete normal weight wc = 145 lb/ft³, f′c = 5 ksi; Asr = 0.\n- Section: HSS10×6×3/8 — As = 10.4 in.², H = 10.0 in., B = 6.00 in.,\n  design wall t = 0.349 in., h/t = 25.7, b/t = 14.2, Isx = 137 in.⁴,\n  Isy = 61.8 in.⁴. Concrete fill: Ac = 49.2 in.², Icx = 353 in.⁴,\n  Icy = 115 in.⁴; gross Ag = 59.6 in.².\n- Geometry / span: length 14 ft, pinned-pinned, K = 1.0, Lc = 14 ft both axes.\n- Loads: axial D = 32 kips, L = 84 kips (compression).\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nThe available axial compressive strength of the filled composite column\n(φcPn for LRFD and Pn/Ωc for ASD) and whether it is adequate for the\nrequired compressive strength.",
 "has_figure": false,
 "stem": "I_4",
 "breadcrumb": "EXAMPLE I.4 · AISC 360-22 Ch.I (composite member) · §I2.2 · Filled Composite Column in Axial Compression",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.4 · AISC 360-22 Ch.I (composite member) · §I2.2 · Filled Composite Column in Axial Compression

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §I2.2: Table I1.1a (compactness), Eq. I2-9a (Pno, compact), Eqs. I2-12/I2-13 (EIeff with C3), Eqs. I2-2/I2-3 (column curve); φc = 0.75, Ωc = 2.00. Direct calculation (no Manual tables). Per the RAG extract provided.

---

### 1. Required Strength

D = 32 kips, L = 84 kips → **Pu = 173 kips; Pa = 116 kips**. Lc = 14 ft = 168 in., both axes.

### 2. Section and Classification

HSS10x6x3/8 (A500 Gr. C): As = 10.4 in.²; t = 0.349 in.; Iy,s = 61.8 in.⁴; fill: f′c = 5 ksi, Ac ≈ 48.8 in.², Icy ≈ 112 in.⁴; Ec = 3,900 ksi.

Wall slenderness: h/t = 25.7, b/t = 14.2 ≤ λp = 2.26√(E/Fy) = 54.4 → **compact** (Table I1.1a).

### 3. Nominal Axial Capacity

Pno = FyAs + 0.85f′cAc = 520 + 207 = **727 kips** (Eq. I2-9a)
C3 = 0.45 + 3[(As + Asr)/Ag] = 0.45 + 0.53 → capped at **0.90**
EIeff = EsIsy + C3EcIcy = 29,000(61.8) + 0.90(3,900)(112) = 2.19 × 10⁶ kip-in.² (Eq. I2-12)
Pe = π²EIeff/Lc² = **764 kips**; Pno/Pe = 0.95 ≤ 2.25 → Pn = 727(0.658^0.95) = **488 kips** (Eq. I2-2)

### 4. Available Strength and Check

- **LRFD:** φcPn = 0.75(488) = **366 kips ≥ 173 ✓** (utilization 0.47)
- **ASD:** Pn/Ωc = 488/2.00 = **244 kips ≥ 116 ✓** (utilization 0.48)

### 5. Conclusion

The 14-ft concrete-filled HSS10x6x3/8 provides **366 kips (LRFD) / 244 kips (ASD)** — governed by weak-axis flexural buckling of the composite section (Pno/Pe ≈ 0.95, mid-slenderness range) — and carries the 173/116-kip demands at under half capacity. The compact walls allow the full plastic Pno, and the concrete contributes ~28% of the squash load and ~18% of the effective stiffness.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
