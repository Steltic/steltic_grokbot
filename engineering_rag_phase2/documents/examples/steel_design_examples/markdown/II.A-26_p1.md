<!-- chunk_id: II.A-26_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-26",
 "example_family": "II.A-26",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J2.4"
 ],
 "eqs": [],
 "tables": [
  "J2.5",
  "8"
 ],
 "title": "Eccentrically Loaded C-Shaped Weld Group, IC Method",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-26 — Eccentrically Loaded C-Shaped Weld Group, IC Method",
 "question": "# II.A-26 — Eccentrically loaded weld group, instantaneous-center (IC) method  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA bracket plate is attached to a support by a C-shaped (three-sided) fillet-weld\ngroup. The weld group consists of one vertical weld of length l = 10 in. plus two\nhorizontal welds, each of length kl = 5 in., returning toward the support at the top\nand bottom of the vertical weld (so k = kl/l = 0.5). All welds are 3⁄8-in. fillet\nwelds (weld size D = 6 sixteenths) made with 70-ksi electrodes (E70XX).\n\nA concentrated in-plane load P is applied to the bracket. Its line of action passes\nthrough a point on the horizontal welds, producing an eccentricity (measured from\nthe weld-group centroid to the load) characterized by a = 0.875 and ex = al = 8.75\nin., as found from the weld geometry.\n\nUsing the instantaneous-center-of-rotation (IC) method, determine the largest\neccentric force P that the available shear strength of the weld group can support\nfor (a) a vertical load (θ = 0°) and (b) a load inclined θ = 75° from vertical.\nReport both the LRFD design force and the ASD allowable force.\n\n## Given\n- Welds: 3⁄8-in. (D = 6) fillet welds, E70XX (FEXX = 70 ksi).\n- Geometry: vertical weld l = 10 in.; two horizontal welds kl = 5 in. each; k = 0.5; total weld length = 20 in.\n- From geometry: xl (centroid offset) = 1.25 in.; a = 0.875; ex = al = 8.75 in.\n- Load: in-plane eccentric force P at θ = 0° and θ = 75°.\n- Code basis: AISC 360-22 (fillet-weld available strength); IC weld-group coefficient C from AISC Manual Table 8-8.\n\n## Find\nThe maximum eccentric force P (LRFD and ASD) for θ = 0° and θ = 75°, governed by\nthe available shear strength of the weld group by the instantaneous-center method.",
 "has_figure": false,
 "stem": "II_A_26",
 "breadcrumb": "EXAMPLE II.A-26 · AISC 360-22 II.A (simple / shear connection) · §J2.4 · Eccentrically Loaded C-Shaped Weld Group, IC Method",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-26 · AISC 360-22 II.A (simple / shear connection) · §J2.4 · Eccentrically Loaded C-Shaped Weld Group, IC Method

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J2.4/Table J2.5 (fillet welds, Fnw = 0.60FEXX with directional strength); eccentric weld-group coefficients C by the instantaneous-center method (AISC Manual Table 8-8). Per the RAG extract provided.

---

### 1. Weld Group

C-shaped E70 group: vertical l = 10 in.; two horizontal returns kl = 5 in. (k = 0.5); total 20 in.; D = 6 (3/8-in. fillets). Centroid offset xl = 1.25 in.; load eccentricity ex = al = 8.75 in. (a = 0.875).

Strength basis: φRn = C·C1·D·l (LRFD) and Rn/Ω = (2/3)C·C1·D·l (ASD), with C1 = 1.0 for E70.

### 2. (a) Vertical Load (θ = 0°)

From Manual Table 8-8 (k = 0.5, a = 0.875, interpolated): **C ≈ 1.10**

- **LRFD:** Pu,max = 1.10(1.0)(6)(10) = **66 kips**
- **ASD:** Pa,max = 66(0.928/1.392) = **44 kips**

### 3. (b) Load Inclined θ = 75° from Vertical

With the load nearly aligned toward the group, torsional demand drops sharply and the tabulated coefficient roughly doubles: **C ≈ 2.3** (Table 8-8, 75° page, k = 0.5, a = 0.875):

- **LRFD:** Pu,max = 2.3(6)(10) = **138 kips**
- **ASD:** Pa,max = **92 kips**

### 4. Conclusion

The 3/8-in. C-shaped weld group supports approximately **66 kips (LRFD) / 44 kips (ASD)** for a vertical load at 8.75-in. eccentricity, and roughly **138 / 92 kips** when the load inclines 75° from vertical. The IC method (which underlies Table 8-8 and includes the fillet-weld directional strength increase and nonlinear deformation compatibility) yields ~40% more capacity for the vertical case than the elastic vector method (Example II.A-27) — the practical reason the Manual tables are preferred for eccentric weld groups. Base-metal shear at the bracket and support must also develop the tabulated strength.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
