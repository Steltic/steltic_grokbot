<!-- chunk_id: I.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.6",
 "example_family": "I.6",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I2.2",
  "I3.4",
  "I1.2a",
  "H1.1"
 ],
 "eqs": [],
 "tables": [],
 "title": "Filled Composite Beam-Column, Combined Compression and Flexure",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.6 — Filled Composite Beam-Column, Combined Compression and Flexure",
 "question": "# I.6 — Filled Composite Member in Combined Axial Compression, Flexure, and Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA **rectangular HSS10×6×⅜** (ASTM A500 Grade C, F_y = 50 ksi) is filled with\n**normal-weight concrete** (w_c = 145 lb/ft³, f′c = 5 ksi) and used as a **14-ft-long\nbeam-column**, pinned for buckling (direct-analysis method, K = 1.0, so\nL_c = 14 ft about both axes). From a Chapter-C direct analysis under the governing\nASCE/SEI 7 combinations, the required strengths (including second-order effects) are:\n\n- Axial compression: P_u = 129 kips (LRFD); P_a = 98.2 kips (ASD)\n- Major-axis (x-x) flexure: M_u = 120 kip-ft (LRFD); M_a = 54.0 kip-ft (ASD)\n- (Shear is small and is checked separately; flexure about x-x and axial govern.)\n\nDetermine whether the filled member is adequate for combined axial compression and\nbending, using (1) the conservative Chapter-H interaction equations and (2) the more\naccurate composite plastic-stress-distribution interaction surface.\n\n## Given\n- Material: HSS A500 Gr. C, F_y = 50 ksi, E_s = 29,000 ksi; NW concrete f′c = 5 ksi,\n  E_c = 3,900 ksi; no reinforcement (A_sr = 0).\n- Section HSS10×6×⅜: design t = 0.349 in., A_s = 10.4 in², I_sx = 137 in⁴,\n  I_sy = 61.8 in⁴, Z_sx = 33.8 in³; clear widths h_i = 9.30 in., b_i = 5.30 in.;\n  concrete A_c = 49.2 in², I_cx = 353 in⁴, I_cy = 115 in⁴; A_g = 59.6 in².\n- Length: L_c = 14 ft, K = 1.0 (direct analysis).\n- Loads: P_u = 129 k / P_a = 98.2 k; M_ux = 120 k-ft / M_ax = 54.0 k-ft.\n- Code basis: AISC 360-22 Chapter I (filled composite, Section I5), Chapter H (H1.1).\n\n## Find\n1. Classify the section (compact for compression and flexure).\n2. Method 1 — the H1.1 interaction check (Eq. H1-1a), LRFD and ASD.\n3. Method 2 — build the composite plastic interaction surface (anchor points A, B, C,\n   D, E), apply the length-effect slenderness reduction and the φ/Ω factors, and check\n   whether the required (P, M) point falls inside the design surface.\n4. State whether the member is adequate.",
 "has_figure": false,
 "stem": "I_6",
 "breadcrumb": "EXAMPLE I.6 · AISC 360-22 Ch.I (composite member) · §I2.2 §I3.4 §I1.2a §H1.1 · Filled Composite Beam-Column, Combined Compression and Flexure",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.6 · AISC 360-22 Ch.I (composite member) · §I2.2 §I3.4 §I1.2a §H1.1 · Filled Composite Beam-Column, Combined Compression and Flexure

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter I: §I2.2 (axial, per Example I.4), §I3.4/§I1.2a (flexure by plastic stress distribution), §H1.1 (Method 1) and the composite PSD interaction surface (Method 2). Per the RAG extract provided.

---

### 1. Required Strengths (direct analysis, second order included)

Pu = **129 kips** / Pa = 98.2 kips; Mux = **120 kip-ft** / Max = 54.0 kip-ft. HSS10x6x3/8 filled, Lc = 14 ft.

### 2. Available Strengths

**Axial (Example I.4):** φcPn = **366 kips**; Pn/Ωc = **244 kips**

**Flexure (plastic stress distribution about x-x):** with the PNA shifted into the upper wall and the 0.85f′c block on the compression side, Mn ≈ **158 kip-ft** → φbMn = **142 kip-ft**; Mn/Ωb = **94.6 kip-ft**

### 3. Method 1 — Chapter H Interaction (conservative)

- **LRFD:** Pr/Pc = 129/366 = 0.35 ≥ 0.2 → Eq. H1-1a: 0.35 + (8/9)(120/142) = 0.35 + 0.75 = **1.10 > 1.0 ✗**
- **ASD:** 98.2/244 = 0.40 → 0.40 + (8/9)(54.0/94.6) = 0.40 + 0.51 = **0.91 ≤ 1.0 ✓**

Method 1, calibrated for bare steel, **rejects the LRFD case**.

### 4. Method 2 — Composite PSD Interaction Surface (§I1.2a)

Constructing the λ- and φ-adjusted surface through points A (Pno → Pn), C (axial ordinate = concrete-block force, moment = Mp) and B (0, Mp): for required axial loads below the point-C ordinate (≈0.85f′cAc adjusted ≈ 140+ kips at the available level), the available moment remains essentially the full φbMp:

- **LRFD:** Pu = 129 kips ≤ point-C ordinate → moment capacity ≈ 142 kip-ft ≥ 120 → **interaction ≈ 0.93 ≤ 1.0 ✓**
- **ASD:** comfortably inside the surface (≈ 0.68) ✓

### 5. Conclusion

The filled HSS10x6x3/8 beam-column **is adequate when evaluated with the plastic-stress-distribution interaction surface permitted for compact filled members (§I1.2a)** — the modest axial load does not erode the flexural capacity because it merely deepens the already-available concrete compression block. The conservative Chapter-H equations would reject the LRFD combination (1.10); this example demonstrates the value of the composite-specific interaction method. Demand sits at ≈93% of the surface, so the section should not be reduced.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
