<!-- chunk_id: II.A-27_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-27",
 "example_family": "II.A-27",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J2.4"
 ],
 "eqs": [],
 "tables": [
  "J2.5"
 ],
 "title": "Eccentrically Loaded C-Shaped Weld Group, Elastic Method",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-27 — Eccentrically Loaded C-Shaped Weld Group, Elastic Method",
 "question": "# II.A-27 — Eccentrically loaded weld group, elastic (vector) method  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA bracket plate is attached to a support by a C-shaped (three-sided) fillet-weld\ngroup. The group consists of one vertical weld of length l = 10 in. plus two\nhorizontal welds of length kl = 5 in. each at the top and bottom (k = kl/l = 0.5),\nfor a total weld length of 20 in. All welds are 3⁄8-in. fillet welds (weld size\nD = 6 sixteenths) made with 70-ksi electrodes (E70XX).\n\nA concentrated vertical in-plane load P is applied to the bracket. From the weld\ngeometry, the centroid of the weld group lies xl = 1.25 in. horizontally from the\nvertical weld, and the load acts at an eccentricity ex = al = 8.75 in. from the\ncentroid.\n\nUsing the elastic (vector) method, determine the largest eccentric force P that the\navailable shear strength of the weld group can support. Report the LRFD design force\nand the ASD allowable force, and compare with the instantaneous-center result of\nExample II.A-26.\n\n## Given\n- Welds: 3⁄8-in. (D = 6) fillet welds, E70XX (FEXX = 70 ksi).\n- Geometry: vertical weld l = 10 in.; two horizontal welds kl = 5 in. each; total length 20 in.; k = 0.5.\n- From geometry: centroid offset xl = 1.25 in.; a = 0.875; ex = 8.75 in.\n- Critical-point distances from centroid: cx = 3.75 in., cy = 5.0 in.\n- Load: vertical in-plane eccentric force P.\n- Code basis: AISC 360-22 (fillet-weld available strength); elastic vector analysis for the eccentric distribution.\n\n## Find\nThe maximum eccentric force P (LRFD and ASD) governed by the available shear\nstrength per inch of the most heavily loaded point of the weld group, using the\nelastic (vector) method.",
 "has_figure": false,
 "stem": "II_A_27",
 "breadcrumb": "EXAMPLE II.A-27 · AISC 360-22 II.A (simple / shear connection) · §J2.4 · Eccentrically Loaded C-Shaped Weld Group, Elastic Method",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-27 · AISC 360-22 II.A (simple / shear connection) · §J2.4 · Eccentrically Loaded C-Shaped Weld Group, Elastic Method

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J2.4/Table J2.5 (fillet weld available strength: 1.392D kip/in. LRFD, 0.928D kip/in. ASD per 1/16-in. leg); elastic (vector) analysis of the eccentric weld group. Per the RAG extract provided.

---

### 1. Weld Group Section Properties (unit throat, line treatment)

Vertical l = 10 in. plus two horizontal kl = 5 in. returns (k = 0.5); total L = 20 in.; centroid 1.25 in. from the vertical weld.

Ix = 10³/12 + 2(5)(5.0)² = 83.3 + 250 = 333 in.³
Iy = 10(1.25)² + 2[5³/12 + 5(1.25)²] = 15.6 + 36.5 = 52.1 in.³
**J = Ix + Iy = 385 in.³**; critical point at the ends of the horizontal welds: (cx, cy) = (3.75, 5.0) in.

### 2. Critical Weld Force per Inch (vertical P at ex = 8.75 in.)

Direct: fv = P/20 = 0.0500P
Torsion (M = 8.75P): fx = Mcy/J = 0.1135P; fy = Mcx/J = 0.0851P

Resultant: f = √[(0.1135P)² + (0.0500P + 0.0851P)²] = **0.1765P kip/in.**

### 3. Maximum Eccentric Force (D = 6)

- **LRFD:** 1.392(6) = 8.35 kip/in. → Pu,max = 8.35/0.1765 = **47.3 kips**
- **ASD:** 0.928(6) = 5.57 kip/in. → Pa,max = **31.5 kips**

(Equivalent coefficient C = P/(D·l) ≈ 0.79.)

### 4. Comparison with the IC Method (Example II.A-26)

| Method | LRFD Pmax | ASD Pmax |
|---|---|---|
| Elastic (vector) | 47.3 kips | 31.5 kips |
| Instantaneous center (Table 8-8) | ≈66 kips | ≈44 kips |

The elastic method is roughly **30% conservative**: it ignores both the directional (transverse) strength increase of fillet welds and the nonlinear redistribution captured by the IC solution.

### 5. Conclusion

By the elastic vector method, the 3/8-in. C-shaped weld group supports **47.3 kips (LRFD) / 31.5 kips (ASD)** at the 8.75-in. eccentricity. The method is simple and always conservative; the Manual Table 8-8 IC coefficients should be used where the extra capacity is needed.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
