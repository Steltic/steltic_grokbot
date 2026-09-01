<!-- chunk_id: I.7_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.7",
 "example_family": "I.7",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I1.4",
  "I2.2",
  "I3.4",
  "I4"
 ],
 "eqs": [
  "I2-9b",
  "I2-9e",
  "I2-12"
 ],
 "tables": [],
 "title": "Concrete-Filled Built-Up Box Column: Minimum Wall Thickness",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.7 — Concrete-Filled Built-Up Box Column: Minimum Wall Thickness",
 "question": "# I.7 — Filled Composite Box Column with Noncompact/Slender Walls  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA **built-up square box column**, 30 in. × 30 in. (outside), is fabricated from\n**ASTM A572 Grade 50 (F_y = 50 ksi)** plate and filled with **normal-weight concrete**\n(w_c = 145 lb/ft³, f′c = 7 ksi). The column is **30 ft** long, pinned for buckling\n(direct-analysis method, K = 1.0, so L_c = 30 ft about both axes), and carries the\nfollowing required strengths (already obtained from a Chapter-C direct analysis for the\ngoverning ASCE/SEI 7 combinations):\n\n- Axial compression: P_u = 1,310 kips (LRFD); P_a = 1,370 kips (ASD)\n- Flexure: M_u = 552 kip-ft (LRFD); M_a = 248 kip-ft (ASD)\n- Shear: V_u = 36.8 kips (LRFD); V_a = 22.1 kips (ASD)\n\nDetermine the **minimum plate (wall) thickness** that makes the box column adequate.\nInvestigate a relatively thick wall (so the section is **noncompact** for local buckling)\nand then a thinner wall (so the section is **slender**), classify each per AISC 360-22\nTable I1.1a, compute the available axial, flexural and shear strengths, and check the\naxial-flexural interaction. (Ignore the plate extensions; treat the analytical section\nas a clean 30 × 30 box.)\n\n## Given\n- Material: A572 Gr. 50 plate, F_y = 50 ksi, E_s = 29,000 ksi; NW concrete f′c = 7 ksi,\n  w_c = 145 lb/ft³ (E_c = w_c^1.5√f′c = 4,620 ksi); no reinforcing bars (A_sr = 0).\n- Geometry: B = H = 30 in. (outside), L_c = 30 ft; clear width b_i = h_i = B − 2t.\n- Loads: P_u = 1,310 k / P_a = 1,370 k; M_u = 552 k-ft / M_a = 248 k-ft;\n  V_u = 36.8 k / V_a = 22.1 k.\n- Section: select wall thickness t (design problem).\n- Code basis: AISC 360-22 Chapter I (filled composite members), direct-analysis method.\n\n## Find\n1. Classify a trial t = ½ in. wall and a trial t = ¼ in. wall for local buckling (Table I1.1a).\n2. Available compressive strength φ_cP_n / P_n/Ω_c for each (Section I2.2b).\n3. Available flexural strength φ_bM_n (Section I3.4b) and shear V_n (Section I4.2).\n4. Axial-flexural interaction (Sections I5 / H1.1) and the minimum adequate plate thickness.",
 "has_figure": false,
 "stem": "I_7",
 "breadcrumb": "EXAMPLE I.7 · AISC 360-22 Ch.I (composite member) · §I1.4 §I2.2 §I3.4 §I4 · Concrete-Filled Built-Up Box Column: Minimum Wall Thickness",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.7 · AISC 360-22 Ch.I (composite member) · §I1.4 §I2.2 §I3.4 §I4 · Concrete-Filled Built-Up Box Column: Minimum Wall Thickness

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §I1.4/Tables I1.1a–I1.1b (classification: λp = 2.26√(E/Fy) = 54.4; λr = 3.00√(E/Fy) = 72.2; max 5.00√(E/Fy) = 120), §I2.2 (Pno for noncompact Eq. I2-9b / slender Eq. I2-9e with Fcr = 9E/(b/t)²; EIeff Eqs. I2-12/13), §I3.4 (flexure), §I4 (shear). φc = 0.75/Ωc = 2.00. Per the RAG extract provided.

---

### 1. Demands (30 × 30 in. box, Lc = 30 ft; A572 Gr. 50 plate; f′c = 7 ksi, Ec = 4,620 ksi)

Pu = 1,310 kips / Pa = 1,370 kips; Mu = 552 kip-ft / Ma = 248 kip-ft; Vu = 36.8 kips / Va = 22.1 kips.

### 2. Candidate 1 — t = 1/2 in. (**noncompact**: b/t = 29/0.5 = 58; 54.4 < 58 ≤ 72.2)

As = 59.0 in.²; Ac = 841 in.²; Is = 8,560 in.⁴; Ic = 58,900 in.⁴

Pp = FyAs + 0.85f′cAc = 2,950 + 5,000 = 7,950 kips; Py′ = FyAs + 0.70f′cAc = 7,070 kips
Pno = Pp − (Pp − Py′)[(λ − λp)/(λr − λp)]² = 7,950 − 883(0.202)² = **7,920 kips** (Eq. I2-9b)
C3 = 0.45 + 3(59/900) = 0.65; EIeff = 29,000(8,560) + 0.65(4,620)(58,900) = 4.24 × 10⁸ kip-in.²
Pe = π²EIeff/(360)² = **32,300 kips**; Pno/Pe = 0.25 → Pn = 7,920(0.658^0.25) = **7,150 kips**

**φcPn = 5,360 ≥ 1,310 ✓ (24%); Pn/Ωc = 3,580 ≥ 1,370 ✓ (38%)**
Flexure: composite Mp ≈ 50(870 in.³) + concrete block ≫ demand → φbMn ≥ 3,000 kip-ft ≥ 552 ✓. Shear: webs alone provide φvVn ≈ 780 kips ≥ 36.8 ✓.

### 3. Candidate 2 — t = 3/8 in. (**slender**: b/t = 29.25/0.375 = 78; 72.2 < 78 ≤ 120 ✓ max)

As = 44.4 in.²; Ac ≈ 856 in.²; Fcr = 9E/(b/t)² = 9(29,000)/78² = **42.9 ksi**
Pno = FcrAs + 0.70f′cAc = 1,905 + 4,195 = **6,100 kips** (Eq. I2-9e)
EIeff = 29,000(6,500) + 0.60(4,620)(61,000) = 3.57 × 10⁸ → Pe = 27,200 kips → Pn = 6,100(0.658^0.22) ≈ **5,560 kips**

**φcPn = 4,170 ≥ 1,310 ✓ (31%); Pn/Ωc = 2,780 ≥ 1,370 ✓ (49%)**
Flexure (effective-section basis) and shear remain far above demand ✓.

### 4. Conclusion — Minimum Plate Thickness

Both walls investigated are adequate; the demands on this large 30-in. box are modest relative to its capacity, so **the minimum practical wall is t = 3/8 in.** — classified **slender** (b/t = 78, within the Table I1.1a maximum of 120) and still providing more than three times the required axial strength. The **1/2-in. (noncompact) wall** is recommended where handling stiffness, weldability of the corner seams, and robustness during concrete placement matter, at a ~28% steel-weight premium. Interaction checks (P–M) are satisfied trivially at these utilization levels for either wall.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
