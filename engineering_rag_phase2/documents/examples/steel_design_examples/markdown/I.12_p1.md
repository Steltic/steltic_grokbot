<!-- chunk_id: I.12_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.12",
 "example_family": "I.12",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I8.3",
  "I8.3c",
  "I8.3b"
 ],
 "eqs": [],
 "tables": [],
 "title": "Steel Headed Stud Anchor Under Combined Shear and Tension",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.12 — Steel Headed Stud Anchor Under Combined Shear and Tension",
 "question": "# I.12 — Steel Anchors in Composite Components (shear + tension interaction)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA single ¾-in.-diameter steel headed stud anchor (AWS D1.1 Type B, Fu = 65 ksi,\nAsa = 0.442 in²) is used as a load-transfer anchor in a **composite component** — for\nexample, in the load-introduction region of an encased composite column — embedded in\nnormal-weight concrete (f′c = 5 ksi, wc = 145 lb/ft³). The concrete is uncracked under\nservice loads and the anchor is located away from free edges (the nearest free edge\nand the nearest neighboring anchor are at least 24 in. away), so concrete breakout in\nshear is **not** a governing limit state.\n\nThe anchor is subjected simultaneously to direct shear and tension from the connection:\n- shear: dead load 2 kips, live load 5 kips;\n- tension: dead load 3 kips, live load 7.5 kips.\n\nDetermine whether one ¾-in. stud is adequate. Select the required stud height and\ncheck the available shear strength, available tensile strength, and the shear–tension\ninteraction, by LRFD and by ASD.\n\n## Given\n- Material: stud Fu = 65 ksi, ¾-in. dia. (Asa = 0.442 in²); concrete f′c = 5 ksi, NW.\n- Condition: composite component (not a composite beam), uncracked NW concrete, no\n  governing edge/breakout effects (free edge / neighbor ≥ 24 in.).\n- Required loads (service): shear PD = 2 k, PL = 5 k; tension PD = 3 k, PL = 7.5 k.\n  → LRFD: Quv = 1.2(2) + 1.6(5) = 10.4 k; Qut = 1.2(3) + 1.6(7.5) = 15.6 k.\n  → ASD: Qav = 2 + 5 = 7.00 k; Qat = 3 + 7.5 = 10.5 k.\n- Code basis: AISC 360-22 §I8.3 (steel anchors in composite components).\n\n## Find\nThe minimum stud height (h/dsa limits); the available shear strength (§I8.3a,\nEq. I8-3) and tensile strength (§I8.3b, Eq. I8-4) of one anchor; and the shear–tension\ninteraction check (§I8.3c, Eq. I8-5), by LRFD and ASD — concluding whether one\n¾-in. stud is adequate.",
 "has_figure": false,
 "stem": "I_12",
 "breadcrumb": "EXAMPLE I.12 · AISC 360-22 Ch.I (composite member) · §I8.3 §I8.3c §I8.3b · Steel Headed Stud Anchor Under Combined Shear and Tension",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.12 · AISC 360-22 Ch.I (composite member) · §I8.3 §I8.3c §I8.3b · Steel Headed Stud Anchor Under Combined Shear and Tension

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §I8.3 (anchors in composite components): shear Qnv = FuAsa (φv = 0.65, Ωv = 2.31); tension Qnt = FuAsa (φt = 0.75, Ωt = 2.00) with the h/d ≥ 8 height requirement; interaction per the §I8.3c 5/3-power equation. Per the RAG extract provided.

---

### 1. Required Strengths (one 3/4-in. Type B stud, Fu = 65 ksi, Asa = 0.442 in.²)

- **LRFD:** shear Qvu = 1.2(2) + 1.6(5) = **10.4 kips**; tension Qtu = 1.2(3) + 1.6(7.5) = **15.6 kips**
- **ASD:** Qva = **7.0 kips**; Qta = **10.5 kips**

Concrete breakout is excluded by the stated edge/spacing conditions (≥ 24 in.), so the steel limit states of §I8.3 govern.

### 2. Stud Height Selection

For tension (and interaction), §I8.3b/c requires h/d ≥ 8 → h ≥ 8(0.75) = 6.0 in. → **specify a stud with ≥ 6 in. embedded length after weld (e.g., a 6 1/2-in. nominal stud)**.

### 3. Available Strengths

Qn = FuAsa = 65(0.442) = **28.7 kips** (both shear and tension nominal values)

- Shear: φvQnv = 0.65(28.7) = **18.7 ≥ 10.4 ✓**; Qnv/Ωv = 12.4 ≥ 7.0 ✓
- Tension: φtQnt = 0.75(28.7) = **21.5 ≥ 15.6 ✓**; Qnt/Ωt = 14.4 ≥ 10.5 ✓

### 4. Shear–Tension Interaction — §I8.3c

[(Qrt/Qct)^(5/3) + (Qrv/Qcv)^(5/3)] ≤ 1.0

- **LRFD:** (15.6/21.5)^(5/3) + (10.4/18.7)^(5/3) = 0.586 + 0.376 = **0.96 ≤ 1.0 ✓**
- **ASD:** (10.5/14.4)^(5/3) + (7.0/12.4)^(5/3) = 0.591 + 0.386 = **0.98 ≤ 1.0 ✓**

### 5. Conclusion

A single **3/4-in. Type B headed stud with at least 6 in. of embedded height (h/d ≥ 8)** is adequate for the combined 10.4-kip shear and 15.6-kip tension (LRFD) — but only just: the 5/3-power interaction is at 96–98% utilization. The individual shear and tension checks have margin; it is the combination that governs. Any load growth should prompt a second stud or a larger diameter, and the stated edge distances must be maintained to keep concrete breakout non-governing.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
