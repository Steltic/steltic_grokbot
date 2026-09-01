<!-- chunk_id: D.1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.1",
 "example_family": "D.1",
 "chapter": "D",
 "topic": "tension member",
 "clauses": [
  "D1",
  "D2",
  "D3",
  "B4.3b",
  "J4.3"
 ],
 "eqs": [
  "D2-1",
  "D2-2",
  "D3-1"
 ],
 "tables": [
  "D3.1"
 ],
 "title": "W-Shape Tension Member, Selection and Strength Check",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.1 — W-Shape Tension Member, Selection and Strength Check",
 "question": "# D.1 — W-shape tension member, selection and strength check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect the lightest **ASTM A992/A992M W-shape of 8 in. nominal depth** to carry an\naxial tension dead load of 30 kips and live load of 90 kips. The member is 25.0 ft\nlong. The member is connected at each end through **both flanges** by 3⁄4-in.-diameter\nbolts in standard holes; the bolt group is arranged so that the critical net section\nremoves **four bolt holes** (one through each half-flange, both flanges), the\nconnection length along the member is **l = 9.00 in.** with three or more bolts per\nline in the direction of loading, and the shear-lag eccentricity for the flange\nconnection is **x̄ = 0.831 in.** (the centroid distance of the matching WT). Verify the\nchosen shape by both LRFD and ASD for the limit states of tensile yielding and\ntensile rupture, and confirm the member satisfies the recommended slenderness limit.\nAssume the connection limit states (bolt shear, bearing, block shear) do not govern.\n\n## Given\n- Material: ASTM A992/A992M, *F_y* = 50 ksi, *F_u* = 65 ksi.\n- Loads: *D* = 30 kips, *L* = 90 kips (axial tension).\n- Member length: 25.0 ft.\n- End connection: both flanges bolted with 3⁄4-in. bolts in standard holes; net\n  section removes four holes through the flange thickness; connection length\n  *l* = 9.00 in.; flange shear-lag eccentricity *x̄* = 0.831 in.\n- Code basis: AISC 360-22 Chapter D (loads combined per ASCE/SEI 7).\n\n## Find\nA satisfactory 8-in.-deep W-shape, with the controlling limit state identified, and\nthe available tensile strengths (LRFD design and ASD allowable) compared to the\nrequired strengths; plus a check of the recommended *L/r* ≤ 300 slenderness limit.",
 "has_figure": false,
 "stem": "D_1",
 "breadcrumb": "EXAMPLE D.1 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §B4.3b §J4.3 · W-Shape Tension Member, Selection and Strength Check",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.1 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §B4.3b §J4.3 · W-Shape Tension Member, Selection and Strength Check

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter D: §D1 (Slenderness), §D2 (Eqs. D2-1, D2-2), §D3 (Eq. D3-1, Table D3.1); net area per §B4.3b. Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Material | ASTM A992/A992M, Fy = 50 ksi, Fu = 65 ksi |
| Loads | D = 30 kips, L = 90 kips (tension); member length 25.0 ft |
| Connection | Both flanges bolted, 3/4-in. bolts in standard holes; 4 holes at critical net section; l = 9.00 in.; x̄ = 0.831 in.; ≥3 bolts per line |

- **LRFD:** Pu = 1.2(30) + 1.6(90) = **180 kips**
- **ASD:** Pa = 30 + 90 = **120 kips**

### 2. Preliminary Sizing

Tensile yielding (Eq. D2-1, φt = 0.90 / Ωt = 1.67): Ag ≥ 180/(0.90 × 50) = 4.00 in.² (LRFD); Ag ≥ 1.67(120)/50 = 4.01 in.² (ASD).
Tensile rupture (Eq. D2-2, φt = 0.75 / Ωt = 2.00): Ae ≥ 180/(0.75 × 65) = 3.69 in.²

**Try W8x21:** Ag = 6.16 in.², d = 8.28 in., bf = 5.27 in., tf = 0.400 in., ry = 1.26 in.

### 3. Tensile Yielding — §D2(a), Eq. D2-1

Pn = Fy Ag = 50(6.16) = 308 kips

- **LRFD:** φtPn = 0.90(308) = **277 kips** ≥ 180 kips ✓
- **ASD:** Pn/Ωt = 308/1.67 = **184 kips** ≥ 120 kips ✓

### 4. Net Area — §B4.3b

Per §B4.3b, 1/16 in. is added to the nominal hole diameter for damage. Standard hole for a 3/4-in. bolt = 13/16 in.; effective hole = 13/16 + 1/16 = 7/8 in.

An = Ag − 4(dh)(tf) = 6.16 − 4(0.875)(0.400) = **4.76 in.²**

### 5. Effective Net Area — §D3, Eq. D3-1 and Table D3.1

Shear lag factor U (flanges connected, web not connected):

- **Case 7** (W-shape, flange connected, ≥3 fasteners per line): bf = 5.27 in. < (2/3)d = 5.52 in. → U = 0.85
- **Case 2** (permitted alternative; larger value may be used): U = 1 − x̄/l = 1 − 0.831/9.00 = **0.908** ← governs
- Lower bound (§D3, open sections): U ≥ Agross,connected/Ag = 2(5.27)(0.400)/6.16 = 0.68 — does not control

Ae = An U = 4.76(0.908) = **4.32 in.²** ≥ 3.69 in.² ✓ (Eq. D3-1)

### 6. Tensile Rupture — §D2(b), Eq. D2-2

Pn = Fu Ae = 65(4.32) = 281 kips

- **LRFD:** φtPn = 0.75(281) = **211 kips** ≥ 180 kips ✓
- **ASD:** Pn/Ωt = 281/2.00 = **140 kips** ≥ 120 kips ✓

### 7. Slenderness — §D1

§D1: no maximum slenderness limit for tension members; the User Note recommends L/r ≤ 300.

L/ry = 25.0(12)/1.26 = **238 ≤ 300 ✓**

### 8. Summary and Conclusion

| Limit state | LRFD available | LRFD required | ASD available | ASD required | Reference |
|---|---|---|---|---|---|
| Tensile yielding | 277 kips | 180 kips | 184 kips | 120 kips | Eq. D2-1 |
| Tensile rupture (governs) | 211 kips | 180 kips | 140 kips | 120 kips | Eqs. D2-2, D3-1 |

**Select W8x21 (ASTM A992).** Tensile rupture in the net section governs the design (211 kips LRFD / 140 kips ASD available vs. 180 / 120 kips required). The member also satisfies the recommended L/r ≤ 300 slenderness guideline of §D1. Connection limit states (bolt shear, bearing, block shear per §J4.3) are assumed not to govern, per the problem statement, and shall be verified in the connection design.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
