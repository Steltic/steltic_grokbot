<!-- chunk_id: E.11_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.11",
 "example_family": "E.11",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E2",
  "E3",
  "E7.2",
  "B4.2",
  "E1"
 ],
 "eqs": [
  "E3-1",
  "E3-4"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "Pipe Compression Member",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.11 — Pipe Compression Member",
 "question": "# E.11 — Pipe compression member  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 30-ft-long pipe column is pin-connected at both ends about both axes and is also\nbraced laterally at its midheight in the y-y direction only (so the y-y unbraced\nlength is 15 ft while the x-x unbraced length is the full 30 ft). It must carry an\naxial service dead load of 35 kips and an axial service live load of 105 kips. Using\nan ASTM A53 Grade B pipe (Fy = 35 ksi), select an economical standard-weight pipe\nthat has adequate available compressive strength, confirm the wall is nonslender,\nand verify the choice by direct AISC 360 calculation. Report LRFD and ASD checks.\n\n## Given\n- Material: ASTM A53 Grade B pipe, Fy = 35 ksi, E = 29,000 ksi.\n- Geometry: length 30 ft; pinned both axes (K = 1.0); braced at midheight about y-y only,\n  so Lcx = 30.0 ft and Lcy = 15.0 ft → x-x buckling controls.\n- Loads: axial service D = 35 kips, L = 105 kips.\n- Member / section: select a standard-weight pipe (this solution verifies a Pipe 10 Std:\n  Ag = 11.5 in.², r = 3.68 in., D/t = 31.6).\n- Code basis: AISC 360 (ASCE 7 load combinations).\n\n## Find\nThe selected pipe and its available compressive strength (φcPn for LRFD, Pn/Ωc for ASD),\nincluding the round-HSS wall-slenderness check.",
 "has_figure": false,
 "stem": "E_11",
 "breadcrumb": "EXAMPLE E.11 · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E7.2 §B4.2 §E1 · Pipe Compression Member",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.11 · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E7.2 §B4.2 §E1 · Pipe Compression Member

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E2, §E3 (Eqs. E3-1 through E3-4), §E7.2/Table B4.1a Case 9 (round HSS wall slenderness); §B4.2 (A53 Gr. B pipe designed as round HSS). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Material | ASTM A53 Gr. B, Fy = 35 ksi, E = 29,000 ksi |
| Geometry | L = 30 ft, pinned ends (K = 1.0); midheight y-y brace → Lcx = 30.0 ft = 360 in., Lcy = 15.0 ft = 180 in. |
| Loads | D = 35 kips, L = 105 kips |

- **LRFD:** Pu = 1.2(35) + 1.6(105) = **210 kips**
- **ASD:** Pa = 35 + 105 = **140 kips**

**Try Pipe 10 Std:** Ag = 11.5 in.², r = 3.68 in., D/t = 31.6.

### 2. Wall Slenderness — Table B4.1a, Case 9

λr = 0.11E/Fy = 0.11(29,000)/35 = 91.1

D/t = 31.6 ≤ 91.1 → **wall is nonslender**; §E3 applies with Ae = Ag (equivalently Eq. E7-6 gives Ae = Ag). Per §B4.2, an A53 Gr. B pipe may be designed as a round HSS.

### 3. Governing Slenderness — §E2

- x-axis: Lcx/r = 360/3.68 = **97.8** ← governs
- y-axis: Lcy/r = 180/3.68 = 48.9

(97.8 ≤ 200, §E2 User Note ✓)

### 4. Critical Stress — §E3

4.71√(E/Fy) = 4.71√(29,000/35) = 136 > 97.8 → inelastic buckling, Eq. E3-2.

Fe = π²E/(Lc/r)² = π²(29,000)/(97.8)² = **29.9 ksi** (Eq. E3-4)

Fn = (0.658^(Fy/Fe))Fy = (0.658^(35/29.9))(35) = (0.658^1.17)(35) = **21.4 ksi** (Eq. E3-2)

### 5. Available Compressive Strength — Eq. E3-1

Pn = Fn Ag = 21.4(11.5) = **247 kips**

- **LRFD:** φcPn = 0.90(247) = **222 kips** ≥ 210 kips ✓
- **ASD:** Pn/Ωc = 247/1.67 = **148 kips** ≥ 140 kips ✓

### 6. Summary and Conclusion

| Quantity | Value | Reference |
|---|---|---|
| Wall check | D/t = 31.6 ≤ 91.1 (nonslender) | Table B4.1a Case 9 |
| Governing Lc/r | 97.8 (x-axis, 30 ft) | §E2 |
| Fe; Fn | 29.9 ksi; 21.4 ksi | Eqs. E3-4, E3-2 |
| φcPn / Pn,Ωc | **222 kips / 148 kips** | Eq. E3-1 |

**Select Pipe 10 Std (A53 Gr. B).** The full-height x-axis buckling mode governs (the midheight brace only assists the y-y direction). The pipe is nonslender, and its available compressive strength of 222 kips (LRFD) / 148 kips (ASD) exceeds the required 210 / 140 kips. The selection is the lightest standard-weight pipe satisfying the demand by direct §E3 calculation.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
