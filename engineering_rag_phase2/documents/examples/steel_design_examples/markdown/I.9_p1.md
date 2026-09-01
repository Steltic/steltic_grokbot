<!-- chunk_id: I.9_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.9",
 "example_family": "I.9",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I2.1",
  "I2.1a"
 ],
 "eqs": [
  "I2-4",
  "I2-6",
  "I2-7",
  "I2-2",
  "I2-3"
 ],
 "tables": [],
 "title": "Encased Composite Column in Axial Compression",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.9 — Encased Composite Column in Axial Compression",
 "question": "# I.9 — Encased composite column in axial compression  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 14-ft-long, pin-ended interior column is a concrete-encased composite member:\nan ASTM A992/A992M W10×45 steel shape (Fy = 50 ksi) is encased in a 24 in. ×\n24 in. normal-weight (wc = 145 lb/ft³) reinforced-concrete section with a\nspecified compressive strength f′c = 5 ksi. The longitudinal reinforcement is\neight No. 8 bars (total Asr = 6.32 in.², ASTM A615/A615M, Fyr = 60 ksi) — three\nnear each face plus one at each side mid-height, with 2.5 in. cover to bar\ncenters — and No. 3 ties at 12 in. on center. The member is pinned about both\naxes (K = 1.0), so Lc = 14 ft for both axes.\n\nThe column carries an axial dead load D = 260 kips and an axial live load\nL = 780 kips, both in compression. Using AISC 360 Chapter I, determine the\navailable compressive strength of the encased composite column (LRFD φcPn and\nASD Pn/Ωc) by direct calculation and verify that the member is adequate.\n\n## Given\n- Material: steel ASTM A992/A992M, Fy = 50 ksi, Es = 29,000 ksi; concrete\n  normal weight wc = 145 lb/ft³, f′c = 5 ksi, Ec = 3,900 ksi; bars ASTM A615,\n  Fyr = 60 ksi.\n- Section: W10×45 encased in 24 in. × 24 in. concrete (h1 = h2 = 24 in.).\n  As = 13.3 in.², d = 10.1 in., bf = 8.02 in., tf = 0.620 in.,\n  Isx = 248 in.⁴, Isy = 53.4 in.⁴. Reinforcement: 8 No. 8 bars,\n  Asr = 6.32 in.² (each bar 0.790 in.²), arranged 6 bars at e = 9.50 in. from\n  the centroidal axis and 2 bars at the axis. Gross Ag = 576 in.²,\n  Ac = 556 in.². Isr = 428 in.⁴ (both axes by symmetry);\n  Icx = 27,000 in.⁴, Icy = 27,200 in.⁴.\n- Geometry / span: length 14 ft, pinned-pinned, K = 1.0, Lc = 14 ft both axes.\n- Loads: axial D = 260 kips, L = 780 kips (compression).\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7; detailing per ACI 318).\n\n## Find\nThe available axial compressive strength of the encased composite column\n(φcPn for LRFD and Pn/Ωc for ASD), and whether it is adequate for the required\ncompressive strength.",
 "has_figure": false,
 "stem": "I_9",
 "breadcrumb": "EXAMPLE I.9 · AISC 360-22 Ch.I (composite member) · §I2.1 §I2.1a · Encased Composite Column in Axial Compression",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.9 · AISC 360-22 Ch.I (composite member) · §I2.1 §I2.1a · Encased Composite Column in Axial Compression

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §I2.1: detailing limits §I2.1a (ρsr = 6.32/576 = 1.1% ≥ 0.4%; ties ✓; cover ✓), Pno (Eq. I2-4), EIeff (Eqs. I2-6/I2-7 with C1), column curve (Eqs. I2-2/I2-3); φc = 0.75, Ωc = 2.00. Per the RAG extract provided.

---

### 1. Required Strength

D = 260 kips, L = 780 kips → **Pu = 1,560 kips; Pa = 1,040 kips**. Lc = 14 ft = 168 in., both axes.

### 2. Squash Load and Effective Stiffness

W10x45 (As = 13.3 in.², Isy = 53.4/Isx = 248 in.⁴) in 24 × 24 (Ag = 576 in.²) with 8 No. 8 (Asr = 6.32 in.²):

Pno = FyAs + FyrAsr + 0.85f′cAc = 665 + 379 + 0.85(5)(556) = **3,410 kips** (Eq. I2-4)
C1 = 0.25 + 3(As + Asr)/Ag = **0.35** ≤ 0.7 (Eq. I2-7)
Weak (y) axis governs buckling: EIeff = EsIsy + EsIsr + C1EcIc = 29,000(53.4) + 29,000(≈340) + 0.35(3,900)(≈27,200) = **4.85 × 10⁷ kip-in.²** (Eq. I2-6)

### 3. Column Strength

Pe = π²EIeff/Lc² = π²(4.85 × 10⁷)/(168)² = **16,960 kips**; Pno/Pe = 0.20 ≤ 2.25 →

Pn = Pno(0.658^(Pno/Pe)) = 3,410(0.658^0.20) = **3,140 kips** (Eq. I2-2)

### 4. Available Strength and Check

- **LRFD:** φcPn = 0.75(3,140) = **2,360 kips ≥ 1,560 ✓** (utilization 0.66)
- **ASD:** Pn/Ωc = 3,140/2.00 = **1,570 kips ≥ 1,040 ✓** (utilization 0.66)

### 5. Conclusion

The encased W10x45 composite column is **adequate** with one-third reserve: the heavily confined section is so stiff (Pno/Pe = 0.20) that the slenderness knock-down is only ~8%, and the concrete and reinforcement together supply ~80% of the 3,410-kip squash load. Detailing satisfies all §I2.1a minimums. Load-introduction shear transfer at the joint is addressed in Example I.8.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
