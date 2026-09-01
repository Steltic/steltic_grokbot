<!-- chunk_id: D.5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.5",
 "example_family": "D.5",
 "chapter": "D",
 "topic": "HSS tension member",
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
  "D3.1"
 ],
 "title": "Round HSS Tension Member, Strength Check",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.5 — Round HSS Tension Member, Strength Check",
 "question": "# D.5 — Round HSS tension member, strength check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA **round HSS6.000×0.500 of ASTM A500/A500M Grade C** is used as an axial tension\nmember **30.0 ft long**. It carries a service axial **dead load of 40 kips** and a\nservice axial **live load of 120 kips**. At each end the round HSS is connected by a\nsingle, concentric **½-in.-thick gusset plate** inserted through a slot in the HSS and\nattached with fillet welds; the **weld (connection) length is l = 16.0 in.** Verify the\navailable tensile strength by both LRFD and ASD for the limit states of tensile\nyielding and tensile rupture, and confirm the recommended slenderness limit. Assume\nthe gusset plate and welds are adequate and do not govern.\n\n## Given\n- Material: ASTM A500/A500M Grade C (round HSS), *F_y* = 50 ksi, *F_u* = 62 ksi.\n- Section: HSS6.000×0.500, *A_g* = 8.09 in², design wall thickness *t* = 0.465 in.,\n  radius of gyration *r* = 1.96 in.; outside diameter *D* = 6.00 in. (*R* = 3.00 in.).\n- Loads: *D* = 40 kips, *L* = 120 kips (axial tension).\n- Member length: 30.0 ft.\n- End connection: single concentric ½-in. gusset through a slot; weld length\n  *l* = 16.0 in.; *t_p* = ½ in.\n- Code basis: AISC 360-22 Chapter D (loads combined per ASCE/SEI 7).\n\n## Find\nThe controlling limit state and the available tensile strengths (LRFD design and ASD\nallowable) compared to the required strengths, a verification that *A_e*/*A_g* ≥ 0.75,\nand a check of the recommended *L/r* ≤ 300 slenderness limit.",
 "has_figure": false,
 "stem": "D_5",
 "breadcrumb": "EXAMPLE D.5 · AISC 360-22 Ch.D (HSS tension member) · §D1 §D2 §D3 §B4.3b · Round HSS Tension Member, Strength Check",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.5 · AISC 360-22 Ch.D (HSS tension member) · §D1 §D2 §D3 §B4.3b · Round HSS Tension Member, Strength Check

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter D: §D1, §D2 (Eqs. D2-1, D2-2), §D3 (Eq. D3-1, Table D3.1 Case 5, round); net area per §B4.3b. Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Section | HSS6.000x0.500, A500/A500M Gr. C (Fy = 50 ksi, Fu = 62 ksi); Ag = 8.09 in.²; t = 0.465 in.; r = 1.96 in.; D = 6.00 in. (R = 3.00 in.) |
| Connection | Single concentric 1/2-in. gusset (tp = 0.500 in.) through a slot, fillet welded; l = 16.0 in. |
| Loads | D = 40 kips, L = 120 kips (tension); member length 30.0 ft |

- **LRFD:** Pu = 1.2(40) + 1.6(120) = **240 kips**
- **ASD:** Pa = 40 + 120 = **160 kips**

### 2. Tensile Yielding — §D2(a), Eq. D2-1

Pn = Fy Ag = 50(8.09) = 405 kips

- **LRFD (φt = 0.90):** φtPn = 0.90(405) = **364 kips** ≥ 240 kips ✓
- **ASD (Ωt = 1.67):** Pn/Ωt = 405/1.67 = **242 kips** ≥ 160 kips ✓

### 3. Net Area at the Slotted Section — §B4.3b

The slot removes two wall segments; allowing 1/16-in. fit-up clearance each side of the gusset (§B4.3b allowance, per the RAG note):

An = Ag − 2(tp + 1/16)(t) = 8.09 − 2(0.500 + 0.0625)(0.465) = 8.09 − 0.523 = **7.57 in.²**

### 4. Shear Lag Factor — Table D3.1, Case 5 (Round HSS, single concentric gusset)

> x̄ = (R sin θ)/θ − ½tp (θ in rad); U = [1 + (x̄/l)^3.2]^(−10)

The gusset bisects the section, so each connected half subtends θ = π/2:

x̄ = R sin(π/2)/(π/2) − ½tp = 2R/π − 0.250 = 2(3.00)/π − 0.250 = 1.910 − 0.250 = **1.66 in.**

x̄/l = 1.66/16.0 = 0.104 → U = [1 + (0.104)^3.2]^(−10) = [1.00071]^(−10) = **0.993**

Ae = An U = 7.57(0.993) = **7.51 in.²** (Eq. D3-1)

**Effective-area ratio check:** Ae/Ag = 7.51/8.09 = **0.93 ≥ 0.75 ✓** — the slotted connection does not excessively penalize the section.

### 5. Tensile Rupture — §D2(b), Eq. D2-2

Pn = Fu Ae = 62(7.51) = 466 kips

- **LRFD (φt = 0.75):** φtPn = 0.75(466) = **349 kips** ≥ 240 kips ✓
- **ASD (Ωt = 2.00):** Pn/Ωt = 466/2.00 = **233 kips** ≥ 160 kips ✓

### 6. Slenderness — §D1

Recommended (non-mandatory) L/r ≤ 300:

L/r = 30.0(12)/1.96 = **184 ≤ 300 ✓**

### 7. Summary and Conclusion

| Limit state | LRFD available | LRFD required | ASD available | ASD required | Reference |
|---|---|---|---|---|---|
| Tensile yielding | 364 kips | 240 kips | 242 kips | 160 kips | Eq. D2-1 |
| Tensile rupture (governs) | 349 kips | 240 kips | 233 kips | 160 kips | Eqs. D2-2, D3-1 (Case 5) |

The HSS6.000x0.500 (A500 Gr. C) is **adequate** by both LRFD and ASD, with tensile rupture at the slotted section governing by a comfortable margin. With l = 16 in. the shear lag penalty is negligible (U = 0.993), Ae/Ag = 0.93 ≥ 0.75, and the §D1 slenderness guideline is satisfied. Gusset and weld design per Chapter J are separate and assumed adequate per the problem statement.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
