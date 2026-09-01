<!-- chunk_id: D.3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.3",
 "example_family": "D.3",
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
  "D3.1"
 ],
 "title": "WT-Shape Tension Member, Strength Check (Welded Connection)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.3 — WT-Shape Tension Member, Strength Check (Welded Connection)",
 "question": "# D.3 — WT-shape tension member, strength check (welded connection)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA **WT6×20 of ASTM A992/A992M steel** is used as an axial tension member with a\nlength of **30 ft**. It carries a service axial **dead load of 40 kips** and a service\naxial **live load of 120 kips**. The member is connected to a gusset plate by\n**longitudinal fillet welds applied along each side of the tee stem (flange), each weld\n16 in. long** (connection length *l* = 16.0 in.); there are no bolt holes anywhere in\nthe member. Determine whether the WT6×20 has adequate available tensile strength by\nboth LRFD and ASD for the limit states of tensile yielding and tensile rupture, and\nconfirm the member satisfies the recommended slenderness limit. Assume the gusset\nplate and the welds themselves are adequate and do not govern.\n\n## Given\n- Material: ASTM A992/A992M, *F_y* = 50 ksi, *F_u* = 65 ksi.\n- Section: WT6×20, *A_g* = 5.84 in², *b_f* = 8.01 in., *t_f* = 0.515 in.,\n  *r_x* = 1.57 in., *ȳ* = 1.09 in. (distance from flange face to centroid).\n- Length: *L* = 30.0 ft.\n- Loads: *D* = 40 kips, *L* = 120 kips (axial tension).\n- Connection: longitudinal fillet welds only, one along each side of the connected\n  element, each *l* = 16.0 in.; no bolt holes (welded splice to a gusset).\n- Code basis: AISC 360-22 Chapter D (loads combined per ASCE/SEI 7).\n\n## Find\nThe governing limit state and the available tensile strengths (LRFD design and ASD\nallowable) versus the required strengths, and verification of the recommended\nslenderness ratio *L/r* ≤ 300.",
 "has_figure": false,
 "stem": "D_3",
 "breadcrumb": "EXAMPLE D.3 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §B4.3b · WT-Shape Tension Member, Strength Check (Welded Connection)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.3 · AISC 360-22 Ch.D (tension member) · §D1 §D2 §D3 §B4.3b · WT-Shape Tension Member, Strength Check (Welded Connection)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter D: §D1, §D2 (Eqs. D2-1, D2-2), §D3 (Eq. D3-1, Table D3.1 Case 4); net area per §B4.3b. Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Section | WT6x20, A992 (Fy = 50 ksi, Fu = 65 ksi); Ag = 5.84 in.²; bf = 8.01 in.; tf = 0.515 in.; rx = 1.57 in. (least r); ȳ = x̄ = 1.09 in. |
| Length | 30.0 ft |
| Connection | Longitudinal fillet welds only, each side of the connected flange, l = 16.0 in.; no holes |
| Loads | D = 40 kips, L = 120 kips (tension) |

- **LRFD:** Pu = 1.2(40) + 1.6(120) = **240 kips**
- **ASD:** Pa = 40 + 120 = **160 kips**

### 2. Tensile Yielding — §D2(a), Eq. D2-1

Pn = Fy Ag = 50(5.84) = 292 kips

- **LRFD (φt = 0.90):** φtPn = 0.90(292) = **263 kips** ≥ 240 kips ✓
- **ASD (Ωt = 1.67):** Pn/Ωt = 292/1.67 = **175 kips** ≥ 160 kips ✓

### 3. Effective Net Area — §D3, Eq. D3-1 and Table D3.1 Case 4

No holes anywhere in the member → An = Ag = 5.84 in.² (§B4.3b).

Tension is transmitted by **longitudinal welds only** to the flange (some but not all elements) → **Table D3.1, Case 4** (tees with connected elements, load by longitudinal welds only):

> U = [3l²/(3l² + w²)](1 − x̄/l)

with l = 16.0 in., w = width of connected element = bf = 8.01 in., x̄ = ȳ = 1.09 in.:

U = [3(16.0)²/(3(16.0)² + (8.01)²)](1 − 1.09/16.0) = (768/832.2)(0.932) = (0.923)(0.932) = **0.860**

Lower bound (§D3, open sections): U ≥ Ag,flange/Ag = (8.01 × 0.515)/5.84 = 0.71 — does not control.

Ae = An U = 5.84(0.860) = **5.02 in.²** (Eq. D3-1)

### 4. Tensile Rupture — §D2(b), Eq. D2-2

Pn = Fu Ae = 65(5.02) = 326 kips

- **LRFD (φt = 0.75):** φtPn = 0.75(326) = **245 kips** ≥ 240 kips ✓
- **ASD (Ωt = 2.00):** Pn/Ωt = 326/2.00 = **163 kips** ≥ 160 kips ✓

### 5. Slenderness — §D1

No mandatory limit (§D1); recommended L/r ≤ 300 with the least radius of gyration:

L/rx = 30.0(12)/1.57 = **229 ≤ 300 ✓**

### 6. Summary and Conclusion

| Limit state | LRFD available | LRFD required | ASD available | ASD required | Reference |
|---|---|---|---|---|---|
| Tensile yielding | 263 kips | 240 kips | 175 kips | 160 kips | Eq. D2-1 |
| Tensile rupture (governs) | 245 kips | 240 kips | 163 kips | 160 kips | Eqs. D2-2, D3-1 (Case 4) |

The WT6x20 (A992) is **adequate** by both LRFD and ASD. Tensile rupture through the effective net section governs, with modest margins (≈2% both methods) — the design is efficient but sensitive to the weld length; any reduction in l below 16 in. should trigger re-verification of U (Case 4). The member satisfies the recommended L/r ≤ 300 of §D1. Gusset and weld design are adequate by problem statement (Chapter J checks separate).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
