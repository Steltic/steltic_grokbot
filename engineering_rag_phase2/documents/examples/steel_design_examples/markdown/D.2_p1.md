<!-- chunk_id: D.2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.2",
 "example_family": "D.2",
 "chapter": "D",
 "topic": "tension member",
 "clauses": [
  "D1",
  "D2",
  "D3",
  "B4.3b"
 ],
 "eqs": [
  "D2-1",
  "D2-2",
  "D3-1"
 ],
 "tables": [
  "D3.1",
  "J3.3"
 ],
 "title": "Single-Angle Tension Member, Strength Check and Slenderness",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.2 — Single-Angle Tension Member, Strength Check and Slenderness",
 "question": "# D.2 — Single-angle tension member, strength check and slenderness  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA single **ASTM A572/A572M Grade 50 angle, L4×4×½**, is used as an axial tension\nmember. It carries a service axial **dead load of 20 kips** and a service axial\n**live load of 60 kips**. The angle is connected at its ends through **one leg only**,\nusing **one line of four 3⁄4-in.-diameter bolts in standard holes**, spaced 3 in. on\ncenter so the connection length in the direction of loading is **l = 9.00 in.**\nVerify the tensile strength of the angle by both LRFD and ASD for the limit states of\ntensile yielding and tensile rupture. In addition, determine the maximum member length\nat which the angle would still satisfy the recommended slenderness limit. Assume that\nall connection limit states (bolt shear, bearing/tearout, block shear) are adequate\nand do not govern.\n\n## Given\n- Material: ASTM A572/A572M Grade 50, *F_y* = 50 ksi, *F_u* = 65 ksi.\n- Section: L4×4×½, *A_g* = 3.75 in², least radius of gyration *r_z* = 0.776 in.,\n  single-angle centroid distance *x̄* = 1.18 in.\n- Loads: *D* = 20 kips, *L* = 60 kips (axial tension).\n- End connection: one leg bolted; one line of four 3⁄4-in. bolts in standard holes\n  (≥4 fasteners per line) at 3 in. spacing; connection length *l* = 9.00 in.;\n  leg thickness *t* = ½ in.\n- Code basis: AISC 360-22 Chapter D (loads combined per ASCE/SEI 7).\n\n## Find\nThe controlling limit state and the available tensile strengths (LRFD design and ASD\nallowable) compared to the required strengths, and the maximum member length *L_max*\nconsistent with the recommended *L/r* ≤ 300 slenderness limit.",
 "has_figure": false,
 "stem": "D_2",
 "breadcrumb": "EXAMPLE D.2 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §B4.3b · Single-Angle Tension Member, Strength Check and Slenderness",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.2 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §B4.3b · Single-Angle Tension Member, Strength Check and Slenderness

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter D: §D1, §D2 (Eqs. D2-1, D2-2), §D3 (Eq. D3-1, Table D3.1 Cases 2 and 8); net area per §B4.3b and Table J3.3. Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Section | L4x4x1/2, A572/A572M Gr. 50 (Fy = 50 ksi, Fu = 65 ksi); Ag = 3.75 in.²; rz = 0.776 in.; x̄ = 1.18 in. |
| Connection | One leg, one line of four 3/4-in. bolts in standard holes @ 3 in.; l = 9.00 in. |
| Loads | D = 20 kips, L = 60 kips (tension) |

- **LRFD:** Pu = 1.2(20) + 1.6(60) = **120 kips**
- **ASD:** Pa = 20 + 60 = **80 kips**

### 2. Tensile Yielding — §D2(a), Eq. D2-1

Pn = Fy Ag = 50(3.75) = 188 kips

- **LRFD (φt = 0.90):** φtPn = 0.90(187.5) = **169 kips** ≥ 120 kips ✓
- **ASD (Ωt = 1.67):** Pn/Ωt = 187.5/1.67 = **112 kips** ≥ 80 kips ✓

### 3. Net Area — §B4.3b and Table J3.3

Standard hole for 3/4-in. bolt = 13/16 in. (Table J3.3); add 1/16 in. for damage (§B4.3b): effective hole = 7/8 in.

An = Ag − dh·t = 3.75 − (0.875)(0.500) = **3.31 in.²**

### 4. Effective Net Area — §D3, Eq. D3-1 and Table D3.1

One leg connected → shear lag applies:

- **Case 8** (single angle, four or more fasteners per line): U = 0.80
- **Case 2** (alternative; larger value permitted): U = 1 − x̄/l = 1 − 1.18/9.00 = **0.869** ← governs
- Lower bound (§D3): U ≥ Ag,connected leg/Ag = (4.0 × 0.5)/3.75 = 0.53 — does not control

Ae = An U = 3.31(0.869) = **2.88 in.²** (Eq. D3-1)

### 5. Tensile Rupture — §D2(b), Eq. D2-2

Pn = Fu Ae = 65(2.88) = 187 kips

- **LRFD (φt = 0.75):** φtPn = 0.75(187) = **140 kips** ≥ 120 kips ✓
- **ASD (Ωt = 2.00):** Pn/Ωt = 187/2.00 = **93.6 kips** ≥ 80 kips ✓

### 6. Maximum Length for Recommended Slenderness — §D1

§D1 sets no mandatory limit; the User Note recommends L/r ≤ 300 using the least radius of gyration (rz for a single angle):

L_max = 300 rz = 300(0.776) = 232.8 in. = **19.4 ft**

### 7. Summary and Conclusion

| Limit state | LRFD available | LRFD required | ASD available | ASD required | Reference |
|---|---|---|---|---|---|
| Tensile yielding | 169 kips | 120 kips | 112 kips | 80 kips | Eq. D2-1 |
| Tensile rupture (governs) | 140 kips | 120 kips | 93.6 kips | 80 kips | Eqs. D2-2, D3-1 |

The L4x4x1/2 (A572 Gr. 50) is **adequate** by both LRFD and ASD; tensile rupture in the net section governs. Using Table D3.1 Case 2 (U = 0.869) rather than Case 8 (U = 0.80) — as permitted — gains roughly 9% rupture strength. The member should preferably not exceed **19.4 ft** in fabricated length to respect the recommended L/r ≤ 300 of §D1. Connection limit states are adequate by problem statement.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
