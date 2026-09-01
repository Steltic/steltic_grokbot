<!-- chunk_id: D.8_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "D.8",
 "example_family": "D.8",
 "chapter": "D",
 "topic": "tension member",
 "clauses": [
  "D6",
  "D6.1",
  "D6.2",
  "D2"
 ],
 "eqs": [
  "D2-1"
 ],
 "tables": [],
 "title": "Eyebar Tension Member, Strength Check",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE D.8 — Eyebar Tension Member, Strength Check",
 "question": "# D.8 — Eyebar tension member, strength check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn **eyebar tension member of ASTM A572/A572M Grade 50 steel**, **5∕8 in. thick**, has a\nbody width of **3.00 in.** and a circular head at each end. It carries a service axial\n**dead load of 25 kips** and a service axial **live load of 15 kips** in tension. The\n**pin diameter is 3.00 in.**, the **pin-hole diameter is 3.03 in.**, the head diameter\nis *d_head* = 7.50 in., and the radius of transition between head and body is\n*R* = 8.00 in. The width from the hole edge to the plate edge (normal to the load) is\n*b* = 2.23 in. Verify the available tensile strength of the eyebar by both LRFD and ASD,\nincluding the eyebar detailing requirements.\n\n## Given\n- Material: ASTM A572/A572M Gr. 50, *F_y* = 50 ksi, *F_u* = 65 ksi.\n- Eyebar body: thickness *t* = 5∕8 in., width *w* = 3.00 in.\n- Head/pin: head diameter *d_head* = 7.50 in.; transition radius *R* = 8.00 in.;\n  pin diameter *d* = 3.00 in.; pin-hole diameter *d_h* = 3.03 in.; *b* = 2.23 in.\n- Loads: *D* = 25 kips, *L* = 15 kips (axial tension).\n- Code basis: AISC 360-22 §D6 (eyebars) and §D2 (loads combined per ASCE/SEI 7).\n\n## Find\nConfirm the §D6.1 and §D6.2 dimensional requirements are satisfied, then determine the\navailable tensile strength of the eyebar (governed by tensile yielding of the body) by\nLRFD and ASD versus the required strength.",
 "has_figure": false,
 "stem": "D_8",
 "breadcrumb": "EXAMPLE D.8 · AISC 360-22 Ch.D (tension member) · §D6 §D6.1 §D6.2 §D2 · Eyebar Tension Member, Strength Check",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE D.8 · AISC 360-22 Ch.D (tension member) · §D6 §D6.1 §D6.2 §D2 · Eyebar Tension Member, Strength Check

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §D6 (Eyebars: §D6.1 tensile strength, §D6.2 dimensional requirements) and §D2(a) (Eq. D2-1). Per the RAG extract provided.

---

### 1. Design Data and Required Strength

| Item | Value |
|---|---|
| Material | A572/A572M Gr. 50, Fy = 50 ksi, Fu = 65 ksi |
| Body | t = 5/8 in.; w = 3.00 in. |
| Head/pin | d_head = 7.50 in.; R = 8.00 in.; d = 3.00 in.; dh = 3.03 in.; b = 2.23 in. |
| Loads | D = 25 kips, L = 15 kips (tension) |

- **LRFD:** Pu = 1.2(25) + 1.6(15) = **54.0 kips**
- **ASD:** Pa = 25 + 15 = **40.0 kips**

### 2. Dimensional Requirements — §D6.1 and §D6.2

| Requirement | Limit | Provided | Check |
|---|---|---|---|
| §D6.1: calculation width ≤ 8t | 8(0.625) = 5.00 in. | w = 3.00 in. | ✓ |
| §D6.2(a): uniform t, unreinforced circular head concentric with hole | — | as detailed | ✓ |
| §D6.2(b): R ≥ head diameter | ≥ 7.50 in. | R = 8.00 in. | ✓ |
| §D6.2(c): d ≥ (7/8)w | ≥ 0.875(3.00) = 2.63 in. | d = 3.00 in. | ✓ |
| §D6.2(c): dh ≤ d + 1/32 in. | ≤ 3.03 in. | dh = 3.03 in. | ✓ |
| §D6.2(d): Fy > 70 ksi provisions | N/A (Fy = 50 ksi) | — | ✓ |
| §D6.2(e): t ≥ 1/2 in. (else external nuts) | ≥ 0.50 in. | t = 0.625 in. | ✓ |
| §D6.2(f): (2/3)w < b; b ≤ (3/4)w for calculation | 2.00 in. < b ≤ 2.25 in. | b = 2.23 in. | ✓ |

**All §D6.1/§D6.2 dimensional requirements are satisfied**, so the eyebar head and transition proportions ensure the body governs the strength.

### 3. Tensile Strength — §D6.1 with §D2(a), Eq. D2-1

Per §D6.1, the available tensile strength is determined per §D2 with Ag taken as the gross area of the eyebar body:

Ag = w·t = 3.00(0.625) = 1.88 in.²

Pn = Fy Ag = 50(1.875) = 93.8 kips (Eq. D2-1)

- **LRFD (φt = 0.90):** φtPn = 0.90(93.8) = **84.4 kips** ≥ 54.0 kips ✓
- **ASD (Ωt = 1.67):** Pn/Ωt = 93.8/1.67 = **56.1 kips** ≥ 40.0 kips ✓

### 4. Conclusion

The eyebar satisfies every dimensional requirement of §D6.2 (and the §D6.1 width-to-thickness calculation limit), so its available tensile strength is governed by **tensile yielding of the body** per Eq. D2-1: 84.4 kips (LRFD) and 56.1 kips (ASD), comfortably exceeding the required 54.0 kips and 40.0 kips respectively. The member is **adequate** by both design methods.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
