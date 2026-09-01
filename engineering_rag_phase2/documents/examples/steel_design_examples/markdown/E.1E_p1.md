<!-- chunk_id: E.1E_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.1E",
 "example_family": "E.1",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E3",
  "E7",
  "E1"
 ],
 "eqs": [
  "E3-2",
  "E3-3",
  "E3-4",
  "E7-1",
  "E7-2",
  "E7-3",
  "E7-5"
 ],
 "tables": [
  "E7.1",
  "B4.1a"
 ],
 "title": "W-Shape Compression Member with a Slender Web",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.1E — W-Shape Compression Member with a Slender Web",
 "question": "# E.1E — W-shape compression member with a slender web  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA pin-ended ASTM A992 W16x31 is used as an axially loaded compression member.\nDetermine its available compressive strength governed by the flexural-buckling\nlimit state for each of three effective lengths: Lc = 5 ft, 10 ft, and 15 ft\n(the same effective length applies about both axes, so the weak axis governs).\nNote that the W16x31 web is slender for axial compression at Fy = 50 ksi, so the\nmember must be evaluated with the slender-element provisions. Report φcPn (LRFD)\nand Pn/Ωc (ASD) for each length.\n\n## Given\n- Material: ASTM A992, Fy = 50 ksi, E = 29,000 ksi.\n- Section: W16x31 — Ag = 9.13 in.^2, ry = 1.17 in., bf/2tf = 6.28, h/tw = 51.6,\n  tw = 0.275 in., kdes = 0.842 in. (so h = d − 2·kdes = 14.2 in.).\n- Effective length: Lc = 5 ft, 10 ft, and 15 ft (governs about the y-y axis).\n- Loads: not specified; determine the available strength (capacity) only.\n- Code basis: AISC 360.\n\n## Find\nThe available compressive strength (LRFD φcPn and ASD Pn/Ωc) for Lc = 5, 10, and 15 ft,\nincluding the effective-area reduction for the slender web where applicable.",
 "has_figure": false,
 "stem": "E_1E",
 "breadcrumb": "EXAMPLE E.1E · AISC 360-22 Ch.E (column / axial compression) · §E3 §E7 §E1 · W-Shape Compression Member with a Slender Web",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.1E · AISC 360-22 Ch.E (column / axial compression) · §E3 §E7 §E1 · W-Shape Compression Member with a Slender Web

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E3 (Eqs. E3-2, E3-3, E3-4), §E7 (Eqs. E7-1, E7-2, E7-3, E7-5; Table E7.1(a)), Table B4.1a (Cases 1, 5). φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Member Data and Classification

W16x31 (A992, Fy = 50 ksi): Ag = 9.13 in.²; ry = 1.17 in. (governing axis); bf/2tf = 6.28; h/tw = 51.6; tw = 0.275 in.; h = 14.2 in.

Table B4.1a: flange (Case 1) λr = 0.56√(E/Fy) = 13.5 > 6.28 ✓ nonslender. Web (Case 5): λr = 1.49√(E/Fy) = 35.9 < 51.6 → **web slender for axial compression**; §E7 applies (Pn = FnAe), with the reduction needed only when λ > λr√(Fy/Fn) (Eq. E7-2).

### 2. Lc = 5 ft (60 in.)

Lc/ry = 51.3 → Fe = π²E/(51.3)² = 109 ksi (Eq. E3-4); inelastic (≤113): Fn = (0.658^(50/109))(50) = **41.2 ksi** (Eq. E3-2)

Web check: λr√(Fy/Fn) = 35.9√(50/41.2) = 39.5 < 51.6 → **reduce** (Eq. E7-3, Table E7.1(a): c1 = 0.18, c2 = 1.31):

Fel = (c2λr/λ)²Fy = [1.31(35.9)/51.6]²(50) = **41.5 ksi** (Eq. E7-5); √(Fel/Fn) = 1.003

he = h[1 − 0.18(1.003)](1.003) = 0.822h = 0.822(14.2) = 11.7 in. → ΔA = (14.2 − 11.7)(0.275) = 0.69 in.²

Ae = 9.13 − 0.69 = **8.44 in.²**; Pn = 41.2(8.44) = **348 kips**

- **LRFD: φcPn = 313 kips ASD: Pn/Ωc = 208 kips**

### 3. Lc = 10 ft (120 in.)

Lc/ry = 103 → Fe = 27.2 ksi; inelastic: Fn = (0.658^1.84)(50) = **23.2 ksi**

Web check: λr√(Fy/Fn) = 35.9√(50/23.2) = 52.7 ≥ 51.6 → **web fully effective** (Eq. E7-2); Ae = Ag = 9.13 in.²

Pn = 23.2(9.13) = **212 kips**

- **LRFD: φcPn = 190 kips ASD: Pn/Ωc = 127 kips**

### 4. Lc = 15 ft (180 in.)

Lc/ry = 154 > 113 → elastic (Eq. E3-3): Fe = π²E/(154)² = 12.1 ksi; Fn = 0.877(12.1) = **10.6 ksi**

Web check: λr√(Fy/Fn) = 35.9√(50/10.6) = 77.9 > 51.6 → fully effective; Ae = Ag.

Pn = 10.6(9.13) = **96.8 kips**

- **LRFD: φcPn = 87.1 kips ASD: Pn/Ωc = 58.0 kips**

### 5. Summary and Conclusion

| Lc | Fn (ksi) | Ae (in.²) | φcPn (LRFD) | Pn/Ωc (ASD) |
|---|---|---|---|---|
| 5 ft | 41.2 | 8.44 (web reduced) | **313 kips** | **208 kips** |
| 10 ft | 23.2 | 9.13 (full) | **190 kips** | **127 kips** |
| 15 ft | 10.6 | 9.13 (full) | **87.1 kips** | **58.0 kips** |

The slender-web reduction of §E7 matters only at short effective lengths, where the nominal stress Fn is high: at Lc = 5 ft the effective area drops about 8%, while at 10 ft and 15 ft the lower buckling stress means the full web is effective (Eq. E7-2) and the strength equals the §E3 value on the gross section. This illustrates the stress-dependence of the AISC 360-22 unified effective-width method.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
