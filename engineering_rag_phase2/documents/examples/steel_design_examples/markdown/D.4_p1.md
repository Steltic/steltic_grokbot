<!-- chunk_id: D.4_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.4",
 "example_family": "D.4",
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
 "title": "Rectangular HSS Tension Member, Strength Check",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.4 — Rectangular HSS Tension Member, Strength Check",
 "question": "# D.4 — Rectangular HSS tension member, strength check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA **rectangular HSS6×4×3⁄8 of ASTM A500/A500M Grade C** is used as an axial tension\nmember **30.0 ft long**. It carries a service axial **dead load of 40 kips** and a\nservice axial **live load of 110 kips**. At each end the HSS is connected by a single,\nconcentric **½-in.-thick gusset plate** that passes through slots in the HSS and is\nattached with fillet welds; the **weld (connection) length is l = 16.0 in.** The 6-in.\nside lies in the plane of the connection (the gusset is parallel to the 6-in. faces).\nVerify the available tensile strength by both LRFD and ASD for the limit states of\ntensile yielding and tensile rupture, and confirm the recommended slenderness limit.\nAssume the gusset plate and welds are adequate and do not govern.\n\n## Given\n- Material: ASTM A500/A500M Grade C (rectangular HSS), *F_y* = 50 ksi, *F_u* = 62 ksi.\n- Section: HSS6×4×3⁄8, *A_g* = 6.18 in², design wall thickness *t* = 0.349 in.,\n  *r_y* = 1.55 in. (governing least radius of gyration). Overall dimensions:\n  *H* = 6 in. (in the plane of the connection), *B* = 4 in.\n- Loads: *D* = 40 kips, *L* = 110 kips (axial tension).\n- Member length: 30.0 ft.\n- End connection: single concentric ½-in. gusset through slots; weld length\n  *l* = 16.0 in.; *t_p* = ½ in.\n- Code basis: AISC 360-22 Chapter D (loads combined per ASCE/SEI 7).\n\n## Find\nThe controlling limit state and the available tensile strengths (LRFD design and ASD\nallowable) compared to the required strengths, and a check of the recommended\n*L/r* ≤ 300 slenderness limit.",
 "has_figure": false,
 "stem": "D_4",
 "breadcrumb": "EXAMPLE D.4 · AISC 360-22 Ch.D (HSS tension member) · §D1 §D2 §D3 §B4.3b · Rectangular HSS Tension Member, Strength Check",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.4 · AISC 360-22 Ch.D (HSS tension member) · §D1 §D2 §D3 §B4.3b · Rectangular HSS Tension Member, Strength Check

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter D: §D1, §D2 (Eqs. D2-1, D2-2), §D3 (Eq. D3-1, Table D3.1 Case 5); net area per §B4.3b. Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Section | HSS6x4x3/8, A500/A500M Gr. C (Fy = 50 ksi, Fu = 62 ksi); Ag = 6.18 in.²; t = 0.349 in.; ry = 1.55 in. |
| Geometry | H = 6 in. (in plane of connection), B = 4 in.; L = 30.0 ft |
| Connection | Single concentric 1/2-in. gusset (tp = 0.500 in.) through slots, fillet welded; l = 16.0 in. |
| Loads | D = 40 kips, L = 110 kips (tension) |

- **LRFD:** Pu = 1.2(40) + 1.6(110) = **224 kips**
- **ASD:** Pa = 40 + 110 = **150 kips**

### 2. Tensile Yielding — §D2(a), Eq. D2-1

Pn = Fy Ag = 50(6.18) = 309 kips

- **LRFD (φt = 0.90):** φtPn = 0.90(309) = **278 kips** ≥ 224 kips ✓
- **ASD (Ωt = 1.67):** Pn/Ωt = 309/1.67 = **185 kips** ≥ 150 kips ✓

### 3. Net Area at the Slotted Section — §B4.3b

The slots remove two wall segments; allowing a 1/16-in. fit-up clearance per slotted face (§B4.3b allowance, applied per the RAG note):

An = Ag − 2(tp + 1/16)(t) = 6.18 − 2(0.500 + 0.0625)(0.349) = 6.18 − 0.393 = **5.79 in.²**

### 4. Shear Lag Factor — Table D3.1, Case 5 (Rectangular HSS, single concentric gusset)

> x̄ = b − (2b² + tH − 2t²)/(2H + 4b − 4t); U = 1 − x̄/l

with b = B/2 = 2.00 in., H = 6.00 in., t = 0.349 in.:

x̄ = 2.00 − [2(2.00)² + 0.349(6.00) − 2(0.349)²]/[2(6.00) + 4(2.00) − 4(0.349)]
x̄ = 2.00 − (8.00 + 2.09 − 0.24)/(12.0 + 8.00 − 1.40) = 2.00 − 9.85/18.6 = **1.47 in.**

U = 1 − x̄/l = 1 − 1.47/16.0 = **0.908**

(Note: the §D3 lower-bound provision on U for open sections does not apply to closed sections such as HSS.)

Ae = An U = 5.79(0.908) = **5.26 in.²** (Eq. D3-1)

### 5. Tensile Rupture — §D2(b), Eq. D2-2

Pn = Fu Ae = 62(5.26) = 326 kips

- **LRFD (φt = 0.75):** φtPn = 0.75(326) = **245 kips** ≥ 224 kips ✓
- **ASD (Ωt = 2.00):** Pn/Ωt = 326/2.00 = **163 kips** ≥ 150 kips ✓

### 6. Slenderness — §D1

Recommended (non-mandatory) L/r ≤ 300:

L/ry = 30.0(12)/1.55 = **232 ≤ 300 ✓**

### 7. Summary and Conclusion

| Limit state | LRFD available | LRFD required | ASD available | ASD required | Reference |
|---|---|---|---|---|---|
| Tensile yielding | 278 kips | 224 kips | 185 kips | 150 kips | Eq. D2-1 |
| Tensile rupture (governs) | 245 kips | 224 kips | 163 kips | 150 kips | Eqs. D2-2, D3-1 (Case 5) |

The HSS6x4x3/8 (A500 Gr. C) is **adequate** by both LRFD and ASD; tensile rupture through the slotted net section governs. The recommended slenderness guideline of §D1 is satisfied. Gusset and weld adequacy are by problem statement (Chapter J checks separate).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
