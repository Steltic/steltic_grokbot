<!-- chunk_id: I.11_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.11",
 "example_family": "I.11",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I2.1",
  "I1.2",
  "I5",
  "H1.1",
  "I1.2a"
 ],
 "eqs": [
  "I2-4",
  "I2-6",
  "I2-7",
  "I2-2",
  "I2-3"
 ],
 "tables": [],
 "title": "Encased Composite Beam-Column, Combined Compression and Flexure",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.11 — Encased Composite Beam-Column, Combined Compression and Flexure",
 "question": "# I.11 — Encased Composite Member in Combined Axial Compression, Flexure, and Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA **W10×45 (ASTM A992, F_y = 50 ksi)** is encased in a **24 in. × 24 in.**\nnormal-weight reinforced-concrete column (w_c = 145 lb/ft³, f′c = 5 ksi) with **8 No. 8\nlongitudinal bars** (ASTM A615, F_yr = 60 ksi; A_sr = 6.32 in², two of which —\nA_srs = 1.58 in² — lie on the bending centerline) and 2½-in. cover. The member is a\n**14-ft** beam-column, pinned for buckling (direct-analysis method, K = 1.0, so\nL_c = 14 ft both axes). A Chapter-C direct analysis (governing ASCE/SEI 7 combinations,\nsecond-order effects included) gives:\n\n- Axial compression: P_u = 1,170 kips (LRFD); P_a = 879 kips (ASD)\n- Major-axis (x-x) flexure: M_u = 670 kip-ft (LRFD); M_a = 302 kip-ft (ASD)\n\nDetermine whether the encased composite beam-column is adequate for combined axial\ncompression and bending, using (1) the conservative Chapter-H interaction equations and\n(2) the more accurate composite plastic-stress-distribution interaction surface.\n\n## Given\n- Materials: W10×45 A992, F_y = 50 ksi, E_s = 29,000 ksi; NW concrete f′c = 5 ksi,\n  E_c = 3,900 ksi; reinforcement A615, F_yr = 60 ksi.\n- Section: 24×24 (A_g = 576 in², A_c = 556 in²); W10×45 A_s = 13.3 in², d = 10.1 in.,\n  b_f = 8.02 in., t_f = 0.620 in., t_w = 0.350 in., Z_sx = 54.9 in³, I_sy = 53.4 in⁴;\n  reinforcement A_sr = 6.32 in² (A_srs = 1.58 in² on the centerline), I_sr = 428 in⁴;\n  concrete I_cy = 27,200 in⁴; cover c = 2.5 in.\n- Length: L_c = 14 ft, K = 1.0 (direct analysis).\n- Loads: P_u = 1,170 k / P_a = 879 k; M_ux = 670 k-ft / M_ax = 302 k-ft.\n- Code basis: AISC 360-22 Chapter I (encased composite, Sections I1.2, I2.1, I5), Chapter H.\n\n## Find\n1. Note that local buckling need not be evaluated (encased → treated as compact).\n2. Method 1 — the H1.1 interaction check (Eq. H1-1a), LRFD and ASD.\n3. Method 2 — build the composite plastic interaction surface (points A, B, C, D),\n   apply the length-effect slenderness reduction λ and the φ/Ω factors, and check the\n   required (P, M) points against the design surface.\n4. State whether the member is adequate.",
 "has_figure": false,
 "stem": "I_11",
 "breadcrumb": "EXAMPLE I.11 · AISC 360-22 Ch.I (composite member) · §I2.1 §I1.2 §I5 §H1.1 §I1.2a · Encased Composite Beam-Column, Combined Compression and Flexure",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.11 · AISC 360-22 Ch.I (composite member) · §I2.1 §I1.2 §I5 §H1.1 §I1.2a · Encased Composite Beam-Column, Combined Compression and Flexure

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter I: §I2.1 (Pno, Eq. I2-4; EIeff, Eqs. I2-6/I2-7 with C1; column curve Eqs. I2-2/I2-3; φc = 0.75, Ωc = 2.00), §I1.2/§I5 (plastic stress distribution method), §H1.1 (Method 1). Per the RAG extract provided.

---

### 1. Required Strengths (direct analysis, second order)

Pu = **1,170 kips** / Pa = 879 kips; Mux = **670 kip-ft** / Max = 302 kip-ft. Lc = 14 ft both axes.

### 2. Compressive Strength (W10x45 in 24 × 24 with 8 No. 8)

Pno = FyAs + FyrAsr + 0.85f′cAc = 665 + 379 + 0.85(5)(556) = **3,410 kips** (Eq. I2-4)
C1 = 0.25 + 3(As + Asr)/Ag = 0.35 ≤ 0.7; Ec = 3,900 ksi
EIeff = EsIs + EsIsr + C1EcIc ≈ 7.2 + 11.6 + 37.1 = **55.9 × 10³ kip-in.² × 10³** (Eq. I2-6)
Pe = π²EIeff/Lc² ≈ 19,500 kips → Pno/Pe = 0.17 ≤ 2.25 → Pn = 3,410(0.658^0.17) = **3,170 kips** (Eq. I2-2)

**φcPn = 2,380 kips (LRFD); Pn/Ωc = 1,580 kips (ASD)**

### 3. Flexural Strength (plastic stress distribution)

Locating the PNA in the upper steel flange (hn ≈ 5.0 in. above mid-depth) and summing concrete (0.85f′c block), steel, and bar contributions about the PNA gives:

**Mn ≈ 750 kip-ft → φbMn ≈ 675 kip-ft; Mn/Ωb ≈ 449 kip-ft**

### 4. Method 1 — Chapter H Interaction (conservative)

Pr/Pc = 1,170/2,380 = 0.49 ≥ 0.2 → Eq. H1-1a:
0.49 + (8/9)(670/675) = 0.49 + 0.88 = **1.37 > 1.0 ✗** (ASD: 0.56 + 0.60 = 1.16 ✗)

The anchor-point interaction of Chapter H — derived for bare steel — is **too conservative for encased sections** and indicates failure.

### 5. Method 2 — Composite Plastic-Stress-Distribution Interaction Surface (§I1.2a)

Constructing the φ-factored PSD surface through the standard points A (Pno, 0), C (Pc = 0.85f′cAc = 2,360 kips, Mp) and B (0, Mp), with slenderness applied along the axial axis: for required axial loads at or below the Point-C ordinate, the available moment remains the full **φbMp ≈ 675 kip-ft**:

- **LRFD:** Pu = 1,170 ≤ φ(Point-C axial) ≈ 1,770 kips → moment capacity ≈ 675 ≥ 670 kip-ft ✓ (ratio ≈ 0.99)
- **ASD:** Pa = 879 ≤ 1,180 kips → 449 ≥ 302 kip-ft ✓ (ratio 0.67)

### 6. Conclusion

The encased composite beam-column **fails the conservative Chapter-H interaction (1.37) but is shown adequate by the plastic-stress-distribution interaction surface permitted by §I1.2a**, which recognizes that moderate axial compression does not reduce — and initially increases — the flexural capacity of an encased section (the concrete compression zone is "pre-loaded"). The LRFD moment demand sits essentially at the available φbMp (≈99%), so the bar layout and section dimensions should not be reduced; ASD has ~33% reserve. This example illustrates why Method 2 is the appropriate tool for heavily loaded encased beam-columns.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
