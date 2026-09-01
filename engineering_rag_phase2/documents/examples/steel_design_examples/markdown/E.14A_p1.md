<!-- chunk_id: E.14A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.14A",
 "example_family": "E.14",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E5",
  "E3",
  "E4",
  "E1",
  "E7"
 ],
 "eqs": [
  "E5-1",
  "E3-1",
  "E3-3",
  "E3-4"
 ],
 "tables": [
  "B4.1a"
 ],
 "title": "Axially Loaded Single-Angle Compression Member",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.14A — Axially Loaded Single-Angle Compression Member",
 "question": "# E.14A — Axially loaded single-angle compression member  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA single-angle strut carries axial compression. The angle is an L5×3×½ of ASTM\nA572/A572M Grade 50 steel and is 5 ft long between its end connections. It is\nconnected at both ends through the same leg — the longer (5-in.) leg — using a\nminimum of two bolts per connection. The y-y geometric axis of the angle is parallel\nto the attached (long) leg. There are no transverse loads between the ends.\n\nDetermine the available axial compressive strength of the member (LRFD design\nstrength φcPn and ASD allowable strength Pn/Ωc), accounting for the eccentricity of\nthe single-angle connection through the AISC single-angle effective-slenderness\nprovisions.\n\n## Given\n- Material: ASTM A572/A572M Grade 50, Fy = 50 ksi, E = 29,000 ksi.\n- Member: L5×3×½ single angle. Section properties (AISC Manual Table 1-7):\n  Ag = 3.75 in.², rx = 1.58 in., ry = 0.824 in., rz = 0.642 in.\n  (The y-y axis is parallel to the connected long leg, so ra = ry = 0.824 in.)\n- Length: L = 5 ft = 60 in. between end connections.\n- Connection: loaded in compression at the ends through the same one (longer) leg,\n  with at least two bolts per connection; no intermediate transverse loads.\n- Code basis: AISC 360.\n\n## Find\nThe available compressive strength of the single angle: φcPn (LRFD) and Pn/Ωc (ASD).",
 "has_figure": false,
 "stem": "E_14A",
 "breadcrumb": "EXAMPLE E.14A · AISC 360-22 Ch.E (column / axial compression) · §E5 §E3 §E4 §E1 §E7 · Axially Loaded Single-Angle Compression Member",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.14A · AISC 360-22 Ch.E (column / axial compression) · §E5 §E3 §E4 §E1 §E7 · Axially Loaded Single-Angle Compression Member

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §E5 (single-angle effective slenderness, Eq. E5-1), §E3 (Eqs. E3-1, E3-3, E3-4), §E4 (FTB exemption), Table B4.1a Case 3. φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Design Data

| Item | Value |
|---|---|
| Section | L5x3x1/2, A572/A572M Gr. 50 (Fy = 50 ksi); Ag = 3.75 in.²; rx = 1.58 in.; ry = 0.824 in.; rz = 0.642 in. |
| Length | L = 5 ft = 60 in. between end connections |
| Connection | Both ends through the same (longer, 5-in.) leg; ≥ 2 bolts per end; ra = ry = 0.824 in. |

### 2. Eligibility for §E5 Effective-Slenderness Treatment

§E5 permits neglecting connection eccentricity provided: (1) loaded at the ends through the same one leg ✓; (2) attached with minimum two bolts ✓; (3) no intermediate transverse loads ✓; (4) resulting Lc/r ≤ 200 (verified below) ✓; (5) for unequal legs, bl/bs < 1.7: 5/3 = 1.67 < 1.7 ✓.

**All conditions met** — the angle may be evaluated as axially loaded with the §E5(a) effective slenderness (individual member, connected through the longer leg).

### 3. Effective Slenderness — §E5(a)(1)

L/ra = 60/0.824 = 72.8 ≤ 80 → Eq. E5-1:

Lc/r = 72 + 0.75(L/ra) = 72 + 0.75(72.8) = **127** (≤ 200 ✓, condition (4))

### 4. Local Buckling and FTB Screens

- Table B4.1a Case 3: λr = 0.45√(E/Fy) = 0.45√(29,000/50) = 10.8; b/t = 5.0/0.5 = 10.0 ≤ 10.8 → **nonslender** (§E3 applies, no §E7 reduction).
- §E5: FTB need not be considered when b/t ≤ 0.71√(E/Fy) = 17.1; 10.0 ≤ 17.1 → **FTB exempt** (§E4 not required).

### 5. Critical Stress and Strength — §E3

Fe = π²E/(Lc/r)² = π²(29,000)/(127)² = **17.9 ksi** (Eq. E3-4)

4.71√(E/Fy) = 113 < 127 → elastic buckling, Eq. E3-3:

Fn = 0.877Fe = 0.877(17.9) = **15.7 ksi**

Pn = Fn Ag = 15.7(3.75) = **58.7 kips** (Eq. E3-1)

### 6. Available Compressive Strength

- **LRFD:** φcPn = 0.90(58.7) = **52.8 kips**
- **ASD:** Pn/Ωc = 58.7/1.67 = **35.2 kips**

### 7. Conclusion

Because the L5x3x1/2 strut is end-loaded through its longer leg with two-bolt connections and satisfies all five §E5 conditions (including bl/bs = 1.67 < 1.7), the connection eccentricity is accounted for entirely through the effective slenderness Lc/r = 127 of Eq. E5-1. The leg is nonslender and FTB is exempt, so elastic flexural buckling (Eq. E3-3) governs, giving an available strength of **φcPn = 52.8 kips (LRFD)** and **Pn/Ωc = 35.2 kips (ASD)**.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
