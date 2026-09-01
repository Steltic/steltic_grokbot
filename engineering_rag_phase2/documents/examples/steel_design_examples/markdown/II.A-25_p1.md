<!-- chunk_id: II.A-25_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-25",
 "example_family": "II.A-25",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Eccentrically Loaded Bolt Group, Elastic (Vector) Method",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-25 — Eccentrically Loaded Bolt Group, Elastic (Vector) Method",
 "question": "# II.A-25 — Eccentrically loaded bolt group, elastic (vector) method  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA steel bracket plate is bolted to a supporting member with a vertical group of\nhigh-strength bolts. The bolt group has two vertical rows of six bolts each — 12\nbolts total. The rows are at a 5½-in. gage (each row 2.75 in. from the group's\nvertical centerline), and within each row the six bolts are spaced 3 in. on center,\nso the bolts occupy vertical positions y = ±1.5, ±4.5, and ±7.5 in. relative to the\ngroup centroid. A concentrated in-plane load P acts vertically (θ = 0°) through a\npoint 16 in. horizontally from the centroid of the bolt group (eccentricity\nex = 16 in.).\n\nThe bolts are 7⁄8-in.-diameter Group 120 high-strength bolts in a bearing-type\nconnection, thread condition N (threads not excluded from the shear plane), acting\nin single shear. Bolt shear is assumed to control over bearing and tearout.\n\nUsing the elastic (vector) method, determine the largest eccentric force P that the\navailable bolt shear strength can support. Report the LRFD design force and the ASD\nallowable force, and compare with the instantaneous-center result of Example II.A-24.\n\n## Given\n- Fasteners: 7⁄8-in.-dia. Group 120 bolts, thread condition N, single shear; bearing-type.\n- Geometry: 12 bolts; two rows at x = ±2.75 in.; six rows at y = ±1.5, ±4.5, ±7.5 in. (s = 3 in.).\n- Load: vertical in-plane force P (θ = 0°) at eccentricity ex = 16 in. from the group centroid.\n- Assumption: bolt shear controls (bearing/tearout not critical).\n- Code basis: AISC 360-22 (bolt shear strength); elastic vector analysis for the eccentric distribution.\n\n## Find\nThe maximum eccentric force P (LRFD design force and ASD allowable force) governed\nby the available shear strength of the most heavily loaded bolt, using the elastic\n(vector) method.",
 "has_figure": false,
 "stem": "II_A_25",
 "breadcrumb": "EXAMPLE II.A-25 · AISC 360-22 II.A (simple / shear connection) · §J3.7 · Eccentrically Loaded Bolt Group, Elastic (Vector) Method",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-25 · AISC 360-22 II.A (simple / shear connection) · §J3.7 · Eccentrically Loaded Bolt Group, Elastic (Vector) Method

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J3.7/Table J3.2 (Fnv = 54 ksi, Group 120-N; φ = 0.75, Ω = 2.00); elastic vector analysis of the eccentric bolt group. Per the RAG extract provided.

---

### 1. Group Properties

Twelve 7/8-in. Group 120-N bolts, single shear; x = ±2.75 in.; y = ±1.5, ±4.5, ±7.5 in.; vertical load P at ex = 16 in.

Polar property: J = Σ(x² + y²) = 12(2.75)² + 4(1.5² + 4.5² + 7.5²) = 90.8 + 315 = **406 in.²**

### 2. Critical Bolt Force (elastic superposition)

Direct shear (vertical): rv = P/12 = 0.0833P
Torsional components at the critical corner bolt (x = 2.75, y = 7.5), M = 16P:
- horizontal: rH = My/J = 16P(7.5)/406 = 0.296P
- vertical: rV = Mx/J = 16P(2.75)/406 = 0.108P

Resultant: r = √[(0.296P)² + (0.0833P + 0.108P)²] = √(0.0875 + 0.0368)·P = **0.352P**

Equivalent group coefficient: C = 1/0.352 = **2.84**

### 3. Maximum Eccentric Force

φrn = 24.3 kips; rn/Ω = 16.2 kips:

- **LRFD:** Pu,max = 2.84(24.3) = **69 kips**
- **ASD:** Pa,max = 2.84(16.2) = **46 kips**

### 4. Comparison with the IC Method (Example II.A-24)

| Method | C | LRFD Pmax | ASD Pmax |
|---|---|---|---|
| Elastic (vector) | 2.84 | 69 kips | 46 kips |
| Instantaneous center | ≈3.6 | 87 kips | 58 kips |

The elastic method is about **21% conservative** because it assumes a linear force–deformation response about the group centroid and ignores the redistribution captured by the IC method's nonlinear bolt model.

### 5. Conclusion

By the elastic vector method, the bracket bolt group supports **69 kips (LRFD) / 46 kips (ASD)** at ex = 16 in. The method remains a quick, always-conservative check; where the additional capacity matters, the IC method (Example II.A-24) is preferred and is the basis of the AISC Manual coefficient tables.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
