<!-- chunk_id: K.9_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.9",
 "example_family": "K.9",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J8"
 ],
 "eqs": [],
 "tables": [],
 "title": "HSS Column Base Plate on a Spread Footing",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.9 — HSS Column Base Plate on a Spread Footing",
 "question": "# K.9 — Base plate for a concentrically loaded rectangular HSS column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA square HSS column carries a concentric axial compression load and bears, through a\nsteel base plate, on a square concrete spread footing. Verify that the trial base\nplate is adequate: check the concrete bearing (crushing) strength beneath the plate\nand determine the required base-plate thickness from the cantilever bending of the\nplate outside the HSS perimeter.\n\nThe column is an ASTM A500 Grade C HSS6×6×1/2. The base plate is ASTM A572 Grade 50,\n13 in. × 13 in. (extending 3-1/2 in. beyond each face of the HSS), trial thickness\n1 in. The footing is 7 ft 6 in. × 7 ft 6 in. with concrete strength f′c = 3,000 psi\n(3 ksi). The plate is concentric on the footing.\n\n## Given\n- Material: column ASTM A500 Gr. C (Fy = 50 ksi, Fu = 62 ksi); base plate ASTM A572\n  Gr. 50 (Fy = 50 ksi, Fu = 65 ksi); concrete f′c = 3 ksi.\n- Column HSS6×6×1/2: B = H = 6.00 in.\n- Base plate: N = B(plate) = 13 in.; trial thickness tp = 1 in.\n- Footing: 7.5 ft × 7.5 ft (= 90 in. × 90 in.); plate concentric.\n- Service axial loads: dead PD = 40 kips, live PL = 120 kips.\n- Code basis: AISC 360 §J8 (+ ASCE/SEI 7 for the load combinations; plate-thickness\n  cantilever method per AISC Manual Part 14 / Design Guide 1).\n\n## Find\nThe required axial load (LRFD and ASD); the available concrete bearing strength of\nthe footing under the plate (§J8, Eq. J8-2); and the required base-plate thickness\nfrom the cantilever moment outside the HSS perimeter (plate bending limited by the\nplastic moment, §F11 Eq. F11-1). State whether the 13 × 13 × 1-in. base plate is\nadequate.",
 "has_figure": false,
 "stem": "K_9",
 "breadcrumb": "EXAMPLE K.9 · AISC 360-22 Ch.K (HSS connection) · §J8 · HSS Column Base Plate on a Spread Footing",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.9 · AISC 360-22 Ch.K (HSS connection) · §J8 · HSS Column Base Plate on a Spread Footing

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J8 (Pp = 0.85f′cA1√(A2/A1) ≤ 1.7f′cA1; φc = 0.65, Ωc = 2.31); plate thickness from cantilever bending beyond the HSS perimeter (Manual Part 14, m = [N − 0.95B]/2 for HSS). Per the RAG extract provided.

---

### 1. Required Strength

P: D = 40 kips, L = 120 kips → **LRFD Pu = 240 kips; ASD Pa = 160 kips**

HSS6x6x1/2 on a 13 × 13 plate (A1 = 169 in.²) centered on a 90 × 90 in. footing (f′c = 3 ksi).

### 2. Concrete Bearing — §J8

√(A2/A1) = √(8,100/169) = 6.9 → **capped at 2.0**:

Pp = 0.85(3)(169)(2.0) = 862 kips = 1.7f′cA1 (upper bound reached)

- **LRFD:** φcPp = 0.65(862) = **560 kips ≥ 240 ✓** (utilization 0.43)
- **ASD:** Pp/Ωc = 862/2.31 = **373 kips ≥ 160 ✓** (utilization 0.43)

### 3. Plate Thickness (cantilever beyond the HSS)

m = (N − 0.95B)/2 = (13 − 0.95 × 6)/2 = **3.65 in.**; bearing pressure fpu = 240/169 = 1.42 ksi (fpa = 0.95 ksi)

- **LRFD:** t_req = m√(2fpu/(0.9Fy)) = 3.65√(2 × 1.42/45) = **0.92 in.**
- **ASD:** t_req = 3.65√(3.34 × 0.95/50) = **0.92 in.**

**Trial 1-in. plate ≥ 0.92 in. ✓**

### 4. Conclusion

The **PL1 × 13 × 13 (A572 Gr. 50)** base plate is adequate: the heavily confined footing develops the §J8 upper-bound bearing (560 kips LRFD / 373 kips ASD vs. 240/160 required), and the 3.65-in. plate cantilevers need 0.92 in. of thickness — satisfied by the 1-in. trial with ~8% margin. Anchor rods are sized for erection/stability forces separately, as the loading is concentric compression.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
