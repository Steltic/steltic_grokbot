<!-- chunk_id: J.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.6",
 "example_family": "J.6",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J8"
 ],
 "eqs": [],
 "tables": [],
 "title": "Column Base Plate in Axial Compression",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.6 — Column Base Plate in Axial Compression",
 "question": "# J.6 — Base Plate Bearing on Concrete  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W12×96 column (ASTM A992/A992M) is supported on a square concrete pedestal and\ndelivers a concentric axial compression of 115 kips dead load plus 345 kips live\nload. The pedestal is 24 in. × 24 in. with a specified concrete strength\nf′c = 3 ksi; a grout bed (f′c = 4 ksi) is placed between the base plate and the\npedestal. A square ASTM A572/A572M Grade 50 base plate is to be checked, sized so\nthat its anchor-rod pattern allows N ≥ d + 2(3 in.) and B ≥ bf + 2(3 in.).\n\nVerify that a 22 in. × 22 in. base plate is adequate for (a) the required bearing\narea, (b) the concrete bearing strength, and determine (c) the required base-plate\nthickness, for both LRFD and ASD.\n\n## Given\n- Column: W12×96, A992 (Fy = 50 ksi); d = 12.7 in., bf = 12.2 in., tf = 0.900 in.,\n  tw = 0.550 in.\n- Base plate: A572/A572M Gr. 50 (Fy = 50 ksi).\n- Concrete pedestal: 24 in. × 24 in., f′c = 3 ksi (grout f′c = 4 ksi, conservatively\n  neglected).\n- Loads: PD = 115 kips, PL = 345 kips (concentric axial compression).\n- Code basis: AISC 360-22 §J8 (bearing) with AISC Manual Part 14 for plate thickness;\n  loads per ASCE/SEI 7.\n\n## Find\n(a) Required base-plate bearing area A1(req); (b) concrete bearing strength of the\n22×22 plate; (c) required plate thickness (select a practical plate).",
 "has_figure": false,
 "stem": "J_6",
 "breadcrumb": "EXAMPLE J.6 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J8 · Column Base Plate in Axial Compression",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.6 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J8 · Column Base Plate in Axial Compression

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J8 (concrete bearing: Pp = 0.85f′cA1√(A2/A1) ≤ 1.7f′cA1; φc = 0.65, Ωc = 2.31); plate thickness per the AISC Manual Part 14 cantilever method (m, n, λn′). Per the RAG extract provided.

---

### 1. Required Strength

P: D = 115 kips, L = 345 kips → **LRFD Pu = 690 kips; ASD Pa = 460 kips**

W12x96 (d = 12.7 in., bf = 12.2 in.) on a 22 × 22 plate (A1 = 484 in.²) over a 24 × 24 pedestal (A2 = 576 in.², f′c = 3 ksi; the 4-ksi grout is stronger and does not govern).

### 2. (a) Required Bearing Area

√(A2/A1) = √(576/484) = 1.09 ≤ 2 ✓

A1,req = Pu/[φc(0.85f′c)√(A2/A1)] = 690/[0.65(2.55)(1.09)] = **382 in.² ≤ 484 in.² ✓** (ASD: 460(2.31)/(2.55 × 1.09) = 382 in.² ✓). Geometry also satisfies N ≥ d + 6 and B ≥ bf + 6 ✓.

### 3. (b) Concrete Bearing Strength

Pp = 0.85(3)(484)(1.09) = 1,350 kips ≤ 1.7(3)(484) = 2,470 ✓

- **LRFD:** φcPp = 0.65(1,350) = **875 kips ≥ 690 ✓** (utilization 0.79)
- **ASD:** Pp/Ωc = 1,350/2.31 = **583 kips ≥ 460 ✓** (utilization 0.79)

### 4. (c) Required Plate Thickness (Manual Part 14)

m = (N − 0.95d)/2 = (22 − 12.07)/2 = 4.97 in.; n = (B − 0.8bf)/2 = (22 − 9.76)/2 = **6.12 in.** ← governs; λn′ = √(dbf)/4 = 3.11 in. (λ ≤ 1)

Bearing pressure: fpu = 690/484 = 1.43 ksi; fpa = 0.950 ksi

- **LRFD:** t = l√(2fpu/(0.9Fy)) = 6.12√(2 × 1.43/45) = **1.54 in.**
- **ASD:** t = l√(3.34fpa/Fy) = 6.12√(3.34 × 0.950/50) = **1.54 in.**

**Use PL 1 5/8 × 22 × 1′-10 (A572 Gr. 50).**

### 5. Conclusion

The 22 × 22 in. base plate is adequate: the confined-bearing strength of the 24-in. pedestal (875 kips LRFD / 583 kips ASD) exceeds the 690/460-kip demands with ~21% reserve, the required bearing area (382 in.²) is well within the plate, and bending of the governing 6.12-in. plate cantilever sets the thickness at **1 5/8 in.** for both design methods.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
