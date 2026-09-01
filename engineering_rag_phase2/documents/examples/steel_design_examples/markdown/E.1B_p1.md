<!-- chunk_id: E.1B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.1B",
 "example_family": "E.1",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E2",
  "E3",
  "E1",
  "E4"
 ],
 "eqs": [
  "E3-1",
  "E3-2",
  "E3-4"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "W-Shape Column with Intermediate Bracing",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.1B — W-Shape Column with Intermediate Bracing",
 "question": "# E.1B — W-shape column with intermediate bracing  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 30 ft long column is pinned at the top and bottom for buckling about both\nprincipal axes. At its mid-height (15 ft) it is braced against translation about the\nweak (y-y) axis and against twist (torsional bracing), but it is unbraced over the\nfull 30 ft about the strong (x-x) axis. The column carries a concentric axial\nservice dead load of 140 kips and live load of 420 kips. Using ASTM A992/A992M\nsteel, verify whether a W14x90 is adequate per AISC 360.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Member: W14x90; Ag = 26.5 in.^2, rx = 6.14 in., ry = 3.70 in., bf/2tf = 10.2, h/tw = 25.9.\n- Geometry: total length 30 ft, pinned ends both axes (K = 1.0); braced at mid-height\n  about the y-y axis and torsionally. Hence Lx = 30 ft and Ly = Lz = 15 ft.\n- Loads: axial service D = 140 kips, L = 420 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nVerify that the available compressive strength of the W14x90 equals or exceeds the\nrequired strength (LRFD and ASD).",
 "has_figure": false,
 "stem": "E_1B",
 "breadcrumb": "EXAMPLE E.1B · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §E4 · W-Shape Column with Intermediate Bracing",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.1B · AISC 360-22 Ch.E (column / axial compression) · §E2 §E3 §E1 §E4 · W-Shape Column with Intermediate Bracing

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E2, §E3 (Eqs. E3-1, E3-2, E3-4), Table B4.1a (Cases 1, 5). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Required Strength

- **LRFD:** Pu = 1.2(140) + 1.6(420) = **840 kips**
- **ASD:** Pa = 140 + 420 = **560 kips**

### 2. Member and Effective Lengths

W14x90 (A992): Ag = 26.5 in.²; rx = 6.14 in.; ry = 3.70 in.; bf/2tf = 10.2; h/tw = 25.9.

Pinned ends (K = 1.0); midheight brace restrains y-y translation and twist:
Lcx = 30.0 ft = 360 in.; Lcy = Lcz = 15.0 ft = 180 in.

Since the torsional unbraced length does not exceed the lateral unbraced lengths, torsional buckling (§E4) does not control for this doubly symmetric shape (§E3 User Note); flexural buckling per §E3 governs.

### 3. Local Slenderness — Table B4.1a

Flange (Case 1): λr = 0.56√(E/Fy) = 13.5 > 10.2 ✓. Web (Case 5): λr = 1.49√(E/Fy) = 35.9 > 25.9 ✓.
**Nonslender** — §E3 applies with Ag.

### 4. Governing Slenderness and Critical Stress — §E3

- x-axis: Lcx/rx = 360/6.14 = **58.6** ← governs
- y-axis: Lcy/ry = 180/3.70 = 48.6

Fe = π²E/(58.6)² = π²(29,000)/3,434 = **83.3 ksi** (Eq. E3-4)

4.71√(E/Fy) = 113 > 58.6 → inelastic, Eq. E3-2:

Fn = (0.658^(50/83.3))(50) = (0.658^0.600)(50) = **38.9 ksi**

### 5. Available Compressive Strength — Eq. E3-1

Pn = Fn Ag = 38.9(26.5) = **1,030 kips**

- **LRFD:** φcPn = 0.90(1,030) = **928 kips** ≥ 840 kips ✓
- **ASD:** Pn/Ωc = 1,030/1.67 = **617 kips** ≥ 560 kips ✓

### 6. Conclusion

| Quantity | LRFD | ASD |
|---|---|---|
| Required | 840 kips | 560 kips |
| Available (W14x90) | 928 kips | 617 kips |
| Utilization | 0.91 | 0.91 |

**The W14x90 is adequate.** With the midheight weak-axis/torsional brace, strong-axis buckling over the full 30 ft governs (Lc/rx = 58.6 > Lc/ry = 48.6). Compared with Example E.1A (unbraced W14x132 required), a single intermediate brace permits a section roughly 30% lighter — illustrating the efficiency of weak-axis bracing.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
