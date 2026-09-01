<!-- chunk_id: D.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.6",
 "example_family": "D.6",
 "chapter": "D",
 "topic": "tension member",
 "clauses": [
  "D1",
  "D2",
  "D3",
  "D4",
  "B4.3b"
 ],
 "eqs": [
  "D2-1",
  "D2-2",
  "D3-1"
 ],
 "tables": [
  "D3.1"
 ],
 "title": "Double-Angle Tension Member, Strength Check",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.6 — Double-Angle Tension Member, Strength Check",
 "question": "# D.6 — Double-angle tension member, strength check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA **double-angle 2L4×4×½ of ASTM A572/A572M Grade 50** (the two angles separated by a\n3⁄8-in. gusset) is used as an axial tension member **25.0 ft long**. It carries a\nservice axial **dead load of 40 kips** and a service axial **live load of 120 kips**.\nThe double angle is connected to a gusset plate with **one line of eight 3⁄4-in.-\ndiameter bolts in standard holes**, spaced 3 in. on center so the connection length in\nthe direction of loading is **l = 21.0 in.** (each angle is connected through one leg).\nVerify the member's tensile strength by both LRFD and ASD for the limit states of\ntensile yielding and tensile rupture, and confirm the recommended slenderness limit.\nAssume the gusset plate and bolts are adequate and do not govern.\n\n## Given\n- Material: ASTM A572/A572M Grade 50, *F_y* = 50 ksi, *F_u* = 65 ksi.\n- Section: 2L4×4×½ with 3⁄8-in. separation; single-angle centroid distance\n  *x̄* = 1.18 in.; built-up *A_g* = 7.50 in², *r_y* = 1.83 in., *r_x* = 1.21 in.\n  (*r_x* is the least radius of gyration here); leg thickness *t* = ½ in.\n- Loads: *D* = 40 kips, *L* = 120 kips (axial tension).\n- Member length: 25.0 ft.\n- End connection: one line of eight 3⁄4-in. bolts in standard holes (≥4 fasteners per\n  line) at 3 in. spacing; connection length *l* = 21.0 in.\n- Code basis: AISC 360-22 Chapter D (loads combined per ASCE/SEI 7).\n\n## Find\nThe controlling limit state and the available tensile strengths (LRFD design and ASD\nallowable) compared to the required strengths, and a check of the recommended\n*L/r* ≤ 300 slenderness limit.",
 "has_figure": false,
 "stem": "D_6",
 "breadcrumb": "EXAMPLE D.6 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §D4 §B4.3b · Double-Angle Tension Member, Strength Check",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.6 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §D4 §B4.3b · Double-Angle Tension Member, Strength Check

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter D: §D1, §D2 (Eqs. D2-1, D2-2), §D3 (Eq. D3-1, Table D3.1 Cases 2 and 8), §D4 (built-up members); net area per §B4.3b. Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Section | 2L4x4x1/2 (3/8-in. separation), A572/A572M Gr. 50 (Fy = 50 ksi, Fu = 65 ksi); Ag = 7.50 in.²; rx = 1.21 in. (least); ry = 1.83 in.; x̄ = 1.18 in.; t = 1/2 in. |
| Connection | Each angle: one leg, one line of eight 3/4-in. bolts in standard holes @ 3 in.; l = 21.0 in. |
| Loads | D = 40 kips, L = 120 kips (tension); length 25.0 ft |

- **LRFD:** Pu = 1.2(40) + 1.6(120) = **240 kips**
- **ASD:** Pa = 40 + 120 = **160 kips**

### 2. Tensile Yielding — §D2(a), Eq. D2-1

Pn = Fy Ag = 50(7.50) = 375 kips

- **LRFD (φt = 0.90):** φtPn = 0.90(375) = **338 kips** ≥ 240 kips ✓
- **ASD (Ωt = 1.67):** Pn/Ωt = 375/1.67 = **225 kips** ≥ 160 kips ✓

### 3. Net Area — §B4.3b

Effective hole = 13/16 + 1/16 = 7/8 in. One hole per angle at the critical section:

An = 7.50 − 2(0.875)(0.500) = **6.63 in.²**

### 4. Effective Net Area — §D3, Eq. D3-1 and Table D3.1

One leg of each angle connected → shear lag applies:

- **Case 8** (double angles, ≥4 fasteners per line): U = 0.80
- **Case 2** (alternative; larger value permitted): U = 1 − x̄/l = 1 − 1.18/21.0 = **0.944** ← governs
- Lower bound (§D3): U ≥ 2(4.0 × 0.5)/7.50 = 0.53 — does not control

Ae = An U = 6.63(0.944) = **6.25 in.²** (Eq. D3-1)

### 5. Tensile Rupture — §D2(b), Eq. D2-2

Pn = Fu Ae = 65(6.25) = 406 kips

- **LRFD (φt = 0.75):** φtPn = 0.75(406) = **305 kips** ≥ 240 kips ✓
- **ASD (Ωt = 2.00):** Pn/Ωt = 406/2.00 = **203 kips** ≥ 160 kips ✓

### 6. Slenderness and Built-Up Member Requirements — §D1, §D4

L/rx = 25.0(12)/1.21 = **248 ≤ 300 ✓** (recommended limit, §D1 User Note)

Per §D4 (User Note), intermediate connectors between the two angles should be spaced so the single-angle slenderness between connectors (using rz = 0.776 in. of the individual angle) does not exceed 300; e.g., connector spacing ≤ 300(0.776) = 233 in. — readily satisfied with standard stitch-fill details.

### 7. Summary and Conclusion

| Limit state | LRFD available | LRFD required | ASD available | ASD required | Reference |
|---|---|---|---|---|---|
| Tensile yielding | 338 kips | 240 kips | 225 kips | 160 kips | Eq. D2-1 |
| Tensile rupture (governs) | 305 kips | 240 kips | 203 kips | 160 kips | Eqs. D2-2, D3-1 |

The 2L4x4x1/2 (A572 Gr. 50) is **adequate** by both LRFD and ASD; tensile rupture governs. The long 8-bolt connection makes the Case 2 shear lag factor (0.944) substantially better than the Case 8 default (0.80). Slenderness and built-up member guidelines of §D1/§D4 are satisfied. Connection limit states are adequate by problem statement.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
