<!-- chunk_id: I.8_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.8",
 "example_family": "I.8",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I6",
  "I6.4",
  "I6.3a",
  "I6.3b",
  "I8.3",
  "I6.2",
  "I8.3a"
 ],
 "eqs": [
  "I6-1",
  "I6-2",
  "I6-3"
 ],
 "tables": [],
 "title": "Load Transfer in an Encased Composite Member",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.8 — Load Transfer in an Encased Composite Member",
 "question": "# I.8 — Encased Composite Member: Force Allocation and Load Transfer  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W10×45 (ASTM A992, Fy = 50 ksi) is encased in a 24 in. × 24 in. normal-weight\nreinforced-concrete column (f′c = 5 ksi). Longitudinal reinforcement is 8 No. 8 bars\n(Asr = 6.32 in², Fyr = 60 ksi). The encased section is used as a composite\ncompression member. At a beam-to-column joint, an external factored axial force is\nintroduced.\n\nFor each force-introduction condition —\n(a) the entire external force applied directly to the steel W-shape,\n(b) the entire external force applied directly to the concrete, and\n(c) the force applied concurrently to steel and concrete —\ndetermine the longitudinal shear V′r to be transferred across the steel–concrete\ninterface in the load-introduction region. Then size a load-transfer mechanism for\nthe governing concrete-applied case: check direct bearing on internal plates and,\nalternatively, shear connection using ¾-in. steel headed stud anchors.\n\nRequired external axial force: dead load PD = 260 kips, live load PL = 780 kips.\n\n## Given\n- Material: steel A992, Fy = 50 ksi; bars Fyr = 60 ksi (Asr = 6.32 in²);\n  concrete f′c = 5 ksi, NW; studs ¾-in. dia. (Asa = 0.442 in², Fu = 65 ksi).\n- Section: W10×45 (As = 13.3 in²) encased in 24×24 (Ag = 576 in²), concrete area\n  Ac = 556 in²; 8 No. 8 longitudinal bars.\n- Loads: PD = 260 kips, PL = 780 kips →\n  LRFD Pr = 1.2(260) + 1.6(780) = 1,560 kips; ASD Pr = 260 + 780 = 1,040 kips.\n- Internal bearing plates (if used): total loaded area A1 = 134 in².\n- Code basis: AISC 360-22 §I6 (load transfer), §I2.1b (encased compressive\n  strength, Eq. I2-7), §I8.3a (anchor shear in composite components).\n\n## Find\nThe longitudinal shear V′r (LRFD and ASD) for conditions (a), (b), and (c); and the\navailable load-transfer strength by direct bearing on internal plates (Eq. I6-3) and\nby shear connection with ¾-in. studs (Eq. I6-4 / §I8.3a), including the number of\nstuds required for the governing concrete-applied case.",
 "has_figure": false,
 "stem": "I_8",
 "breadcrumb": "EXAMPLE I.8 · AISC 360-22 Ch.I (composite member) · §I6 §I6.4 §I6.3a §I6.3b §I8.3 §I6.2 §I8.3a · Load Transfer in an Encased Composite Member",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.8 · AISC 360-22 Ch.I (composite member) · §I6 §I6.4 §I6.3a §I6.3b §I8.3 §I6.2 §I8.3a · Load Transfer in an Encased Composite Member

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §I6 (Eqs. I6-1/I6-2; load-introduction length §I6.4 = 2 × 24 = 48 in. above and below the joint), §I6.3a (direct bearing, Eq. I6-3, φB = 0.65) and §I6.3b/§I8.3 (steel headed stud anchors, φv = 0.65/Ωv = 2.31). Per the RAG extract provided.

---

### 1. Required Strength and Resistance Shares

Pr: **Pu = 1.2(260) + 1.6(780) = 1,560 kips; Pa = 1,040 kips**

From Example I.9: Pno = 3,410 kips; steel share = FyAs/Pno = 665/3,410 = **0.195**.

### 2. Longitudinal Shear V′r (§I6.2)

| Case | V′r (LRFD) | V′r (ASD) |
|---|---|---|
| (a) all force to the steel shape (Eq. I6-1): transfer (1 − 0.195)Pr | **1,260 kips** | 838 kips |
| (b) all force to the concrete (Eq. I6-2): transfer 0.195Pr | **304 kips** | 203 kips |
| (c) concurrent application: transfer only the mismatch between applied and resisted shares | between (a) and (b); ≈ 0 if applied in proportion to Pno shares | — |

Case (a) is rarely practical (it would demand transferring 1,260 kips); standard detailing introduces most of the force to the concrete, making **case (b), V′r = 304/203 kips, the governing design condition** as posed.

### 3. Transfer Mechanism for Case (b)

**Option 1 — direct bearing (Eq. I6-3, Rn = 1.7f′cA1):**
A1,req = 304/[0.65(1.7)(5)] = **55.0 in.²** (ASD: 203(2.31)/(1.7 × 5) = 55.2 in.²) → e.g., bearing plates between the W10x45 flanges (2 plates × 8 × 3.5 in. ≈ 56 in.²) within the 48-in. introduction length ✓

**Option 2 — 3/4-in. headed stud anchors (§I8.3a, Qnv = FuAsa = 28.7 kips):**
φQnv = 0.65(28.7) = 18.7 kips/stud → n = 304/18.7 = 16.3 → **18 studs** (9 per flange, spaced within 48 in. above/below the joint; h/d ≥ 5 for shear ✓). ASD: 203/12.4 = 16.4 → 18 studs (identical).

### 4. Conclusion

For the 1,560-kip (LRFD) external force, the steel–concrete interface must transfer **304 kips (LRFD) / 203 kips (ASD)** when the force is delivered to the concrete (case (b)) — the practical governing case. Either **≈55 in.² of internal bearing plate** or **eighteen 3/4-in. studs distributed over the §I6.4 load-introduction length** satisfies the requirement; direct bond is not permitted for encased members. Case (a) detailing (all load to the steel core) should be avoided as it would quadruple the transfer demand.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
