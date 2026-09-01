<!-- chunk_id: D.7_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.7",
 "example_family": "D.7",
 "chapter": "D",
 "topic": "tension member",
 "clauses": [
  "D5",
  "D5.2",
  "J7",
  "D2",
  "D5.1"
 ],
 "eqs": [
  "D5-1",
  "D5-2",
  "J7-1",
  "D2-1"
 ],
 "tables": [],
 "title": "Pin-Connected Tension Member, Strength Check",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.7 — Pin-Connected Tension Member, Strength Check",
 "question": "# D.7 — Pin-connected tension member, strength check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA flat **pin-connected plate tension member of ASTM A572/A572M Grade 50 steel** is\n**½ in. thick** and **4.25 in. wide** at the pin region. It is connected by a single\npin and carries a service axial **dead load of 4 kips** and **live load of 12 kips** in\ntension. The **pin diameter is 1.00 in.**, fitted in a **1∕32-in.-oversized pin hole**\n(*d_h* = 1.03 in.) located on the member centerline. The relevant detailing dimensions\nof the symmetric pin plate are: edge distance parallel to the load beyond the hole\n*a* = 2.25 in.; net width from the hole edge to the plate edge measured normal to the\nload *b* = 1.61 in.; and distance from the hole center to the member end *c* = 2.50 in. Assume the pin itself is adequate. Verify the available tensile strength\nof the member by both LRFD and ASD, checking the limit states required for\npin-connected members.\n\n## Given\n- Material: ASTM A572/A572M Gr. 50, *F_y* = 50 ksi, *F_u* = 65 ksi.\n- Plate: thickness *t* = ½ in., width at pin *w* = 4.25 in.\n- Pin/hole: pin diameter *d* = 1.00 in.; hole diameter *d_h* = 1.03 in.\n  (1∕32-in. oversize); hole centered on member.\n- Detailing dimensions: *a* = 2.25 in. (edge distance parallel to force beyond hole),\n  *b* = 1.61 in. (hole-edge to plate-edge normal to force), *c* = 2.50 in.\n- Loads: *D* = 4 kips, *L* = 12 kips (axial tension).\n- Code basis: AISC 360-22 §D5 and §J7 (loads combined per ASCE/SEI 7).\n\n## Find\nConfirm the §D5.2 dimensional requirements are met, then determine the governing limit\nstate among tensile rupture, shear rupture, bearing, and tensile yielding, and report\nthe available tensile strength (LRFD and ASD) versus the required strength.",
 "has_figure": false,
 "stem": "D_7",
 "breadcrumb": "EXAMPLE D.7 · AISC 360-22 Ch.D (tension member) · §D5 §D5.2 §J7 §D2 §D5.1 · Pin-Connected Tension Member, Strength Check",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.7 · AISC 360-22 Ch.D (tension member) · §D5 §D5.2 §J7 §D2 §D5.1 · Pin-Connected Tension Member, Strength Check

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §D5 (Pin-Connected Members: Eqs. D5-1, D5-2; §D5.2 dimensional requirements), §J7 (Eq. J7-1, bearing), §D2(a) (Eq. D2-1, yielding). Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Plate | A572/A572M Gr. 50 (Fy = 50 ksi, Fu = 65 ksi); t = 0.500 in.; w = 4.25 in. at pin |
| Pin/hole | d = 1.00 in.; dh = 1.03 in. (1/32-in. oversize), centered |
| Detailing | a = 2.25 in.; b = 1.61 in.; c = 2.50 in. |
| Loads | D = 4 kips, L = 12 kips (tension) |

- **LRFD:** Pu = 1.2(4) + 1.6(12) = **24.0 kips**
- **ASD:** Pa = 4 + 12 = **16.0 kips**

### 2. Effective Width and Dimensional Requirements — §D5.2

be = 2t + 0.63 = 2(0.500) + 0.63 = 1.63 in., but not more than the actual distance b = 1.61 in. → **be = 1.61 in.**

| §D5.2 requirement | Check |
|---|---|
| (a) Hole midway between edges normal to force | Centered ✓ |
| (b) dh − d ≤ 1/32 in. (pin < 3 in.) | 1.03 − 1.00 = 1/32 in. ✓ |
| (c) Width ≥ 2be + d = 2(1.61) + 1.00 = 4.22 in. | w = 4.25 in. ✓ |
| (c) a ≥ 1.33be = 1.33(1.61) = 2.14 in. | a = 2.25 in. ✓ |
| (d) Corner cuts | None; c = 2.50 in. provided ✓ |

**All dimensional requirements of §D5.2 are satisfied.**

### 3. Limit States — §D5.1

**(a) Tensile rupture — Eq. D5-1 (φt = 0.75, Ωt = 2.00):**
Pn = Fu(2t·be) = 65[2(0.500)(1.61)] = 105 kips
LRFD: 0.75(105) = **78.5 kips**; ASD: 105/2.00 = **52.3 kips**

**(b) Shear rupture — Eq. D5-2 (φsf = 0.75, Ωsf = 2.00):**
Asf = 2t(a + d/2) = 2(0.500)(2.25 + 0.50) = 2.75 in.²
Cr = 1.0 (dh − d ≤ 1/32 in.)
Pn = 0.6CrFuAsf = 0.6(1.0)(65)(2.75) = 107 kips
LRFD: 0.75(107) = **80.4 kips**; ASD: 107/2.00 = **53.6 kips**

**(c) Bearing on projected pin area — §J7, Eq. J7-1 (φ = 0.75, Ω = 2.00):**
Apb = d·t = 1.00(0.500) = 0.500 in.²
Rn = 1.8FyApb = 1.8(50)(0.500) = 45.0 kips
LRFD: 0.75(45.0) = **33.8 kips**; ASD: 45.0/2.00 = **22.5 kips**

**(d) Yielding on gross section — §D2(a), Eq. D2-1 (φt = 0.90, Ωt = 1.67):**
Ag = 4.25(0.500) = 2.13 in.²; Pn = 50(2.13) = 106 kips
LRFD: 0.90(106) = **95.6 kips**; ASD: 106/1.67 = **63.6 kips**

### 4. Summary and Conclusion

| Limit state | LRFD available | ASD available | Reference |
|---|---|---|---|
| Tensile rupture | 78.5 kips | 52.3 kips | Eq. D5-1 |
| Shear rupture | 80.4 kips | 53.6 kips | Eq. D5-2 |
| **Bearing (governs)** | **33.8 kips** | **22.5 kips** | Eq. J7-1 |
| Tensile yielding | 95.6 kips | 63.6 kips | Eq. D2-1 |

Available strength = **33.8 kips (LRFD) ≥ 24.0 kips ✓** and **22.5 kips (ASD) ≥ 16.0 kips ✓**.

The pin-connected plate satisfies all §D5.2 dimensional requirements, and its tensile strength is governed by **bearing on the projected area of the pin (Eq. J7-1)**, with adequate margin under both LRFD and ASD. The pin itself is adequate by problem statement.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
