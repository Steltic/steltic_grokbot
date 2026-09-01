<!-- chunk_id: I.3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.3",
 "example_family": "I.3",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I6",
  "I6.4",
  "I2.2b",
  "I6.3",
  "I6.2",
  "I6.3c",
  "I6.3a"
 ],
 "eqs": [
  "I6-1",
  "I6-2",
  "I2-9a",
  "I6-3",
  "I6-5"
 ],
 "tables": [],
 "title": "Load Transfer in a Filled Composite Member",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.3 — Load Transfer in a Filled Composite Member",
 "question": "# I.3 — Filled Composite Member: Force Allocation and Load Transfer  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA rectangular HSS10×6×⅜ (ASTM A500 Grade C, Fy = 50 ksi) is filled with normal-weight\nconcrete (f′c = 5 ksi, wc = 145 lb/ft³) and used as a filled composite compression\nmember. The cross section is **compact** for composite axial compression. At a beam-\nto-column joint, an external factored axial force is introduced into the member.\n\nFor each of three force-introduction conditions —\n(a) the entire external force applied directly to the steel HSS,\n(b) the entire external force applied directly to the concrete fill, and\n(c) the force applied concurrently to steel and concrete in proportion to their\n    areas —\ndetermine the longitudinal shear force V′r that must be transferred across the\nsteel–concrete interface within the load-introduction region. Then size a load-\ntransfer mechanism: check whether an internal bearing plate (direct bearing) or\ndirect bond interaction is adequate to deliver V′r.\n\nRequired external axial force: dead load PD = 32 kips, live load PL = 84 kips.\n\n## Given\n- Material: HSS A500 Gr. C, Fy = 50 ksi; concrete f′c = 5 ksi, NW (wc = 145 lb/ft³).\n- Section: HSS10×6×⅜ — As = 10.4 in², design wall t = 0.349 in., concrete fill\n  Ac = 49.2 in²; section is compact for composite axial compression.\n- Loads: PD = 32 kips, PL = 84 kips →\n  LRFD Pr = 1.2(32) + 1.6(84) = 173 kips; ASD Pr = 32 + 84 = 116 kips.\n- Internal bearing plate (if used): loaded area A1 = 25.1 in².\n- Code basis: AISC 360-22 §I6 (load transfer), §I2.2b (filled compressive strength).\n\n## Find\nThe longitudinal shear V′r (LRFD and ASD) for force-introduction conditions (a),\n(b), and (c); and the available load-transfer strength by direct bearing on an\ninternal plate (Eq. I6-3) and by direct bond interaction (§I6.3c), identifying which\nmechanism is adequate.",
 "has_figure": false,
 "stem": "I_3",
 "breadcrumb": "EXAMPLE I.3 · AISC 360-22 Ch.I (composite member) · §I6 §I6.4 §I2.2b §I6.3 §I6.2 §I6.3c §I6.3a · Load Transfer in a Filled Composite Member",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.3 · AISC 360-22 Ch.I (composite member) · §I6 §I6.4 §I2.2b §I6.3 §I6.2 §I6.3c §I6.3a · Load Transfer in a Filled Composite Member

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §I6 (force allocation, Eqs. I6-1/I6-2; load-introduction length §I6.4) with §I2.2b (Pno for compact filled sections, Eq. I2-9a) and §I6.3 (transfer mechanisms: direct bearing Eq. I6-3, Rn = 1.7f′cA1, φB = 0.65; direct bond Eq. I6-5, Rn = pbLinFin, φ = 0.50/Ω = 3.00). Per the RAG extract provided.

---

### 1. Required Strength and Section Resistance Shares

Pr: **Pu = 1.2(32) + 1.6(84) = 173 kips; Pa = 116 kips**

HSS10x6x3/8 (As = 10.4 in.², t = 0.349 in.) filled with 5-ksi NW concrete (Ac ≈ 48.8 in.²), compact:

Pno = FyAs + 0.85f′cAc = 520 + 207 = **727 kips** (Eq. I2-9a) → steel share FyAs/Pno = **0.715**; concrete share = **0.285**

### 2. Longitudinal Shear to Be Transferred, V′r (§I6.2)

| Case | Allocation | V′r (LRFD) | V′r (ASD) |
|---|---|---|---|
| (a) all force to the steel (Eq. I6-1) | transfer the concrete's share | 173(0.285) = **49.3 kips** | 33.1 kips |
| (b) all force to the concrete (Eq. I6-2) | transfer the steel's share | 173(0.715) = **124 kips** | 82.9 kips |
| (c) applied in proportion to areas (As/Atot = 0.176 to steel) | transfer the mismatch to strength shares | 173(0.715 − 0.176) = **93.3 kips** | 62.5 kips |

### 3. Transfer Mechanism — Direct Bond (§I6.3c)

Fin = 12t/H² = 12(0.349)/(10)² = 0.0419 ksi; pb ≈ 30.6 in.; Lin = 2(min dimension)... using the §I6.4 introduction length ≈ 20 in.:

Rn = pbLinFin = 30.6(20)(0.0419) = 25.6 kips → φRn = **12.8 kips** (LRFD) / 8.5 kips (ASD)

**Bond is inadequate for all three cases** (12.8 ≪ 49.3 kips even for case (a)).

### 4. Transfer Mechanism — Internal Bearing Plate (§I6.3a, Eq. I6-3)

Rn = 1.7f′cA1; φB = 0.65 → required bearing area on the fill:

- Case (a): A1 ≥ 49.3/[0.65(1.7)(5)] = **8.9 in.²**
- Case (b): A1 ≥ **22.4 in.²**; Case (c): A1 ≥ **16.9 in.²**

A notched internal bearing plate engaging ≈9–23 in.² of the 48.8-in.² core (depending on the case) — e.g., a 1/2-in. plate with a central hole, fillet-welded inside the HSS within the load-introduction region — provides the transfer. (ASD requirements are proportionally smaller and are enveloped by the same plate.)

### 5. Conclusion

The interface must transfer **49.3, 124, or 93.3 kips (LRFD)** for cases (a), (b), and (c) respectively. **Direct bond is far too weak for this small HSS perimeter; an internal bearing plate sized per Eq. I6-3 (8.9–22.4 in.² of bearing on the fill) is the practical mechanism**, detailed within the §I6.4 load-introduction length below the joint. Case (b) — load delivered wholly to the concrete — is the governing transfer condition.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
