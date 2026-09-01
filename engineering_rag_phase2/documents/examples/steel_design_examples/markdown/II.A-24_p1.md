<!-- chunk_id: II.A-24_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-24",
 "example_family": "II.A-24",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7"
 ],
 "eqs": [],
 "tables": [
  "J3.2",
  "7"
 ],
 "title": "Eccentrically Loaded Bolt Group, Instantaneous-Center Method",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-24 — Eccentrically Loaded Bolt Group, Instantaneous-Center Method",
 "question": "# II.A-24 — Eccentrically loaded bolt group, instantaneous-center (IC) method  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA steel bracket plate is bolted to a supporting member with a vertical group of\nhigh-strength bolts. The bolt group consists of two vertical rows (lines) of six\nbolts each — 12 bolts total. The two rows are spaced at a 5½-in. gage (so each row\nlies 2.75 in. either side of the group's vertical centerline), and within each row\nthe six bolts are spaced 3 in. on center vertically. A concentrated service-type\nload P is applied to the bracket in the plane of the faying surface, acting through\na point located 16 in. horizontally from the centroid of the bolt group (i.e., the\nload eccentricity is ex = 16 in.).\n\nThe bolts are 7⁄8-in.-diameter Group 120 (e.g., ASTM A325) high-strength bolts in a\nbearing-type connection, with threads not excluded from the shear plane (thread\ncondition N) and acting in single shear. Bolt shear is assumed to control over bolt\nbearing and tearout in the connected material.\n\nUsing the instantaneous-center-of-rotation (IC) method, determine the largest\neccentric force P that the available bolt shear strength can support for two load\norientations: (a) the load acting vertically (θ = 0° from vertical), and (b) the\nload inclined at θ = 15° from vertical. Report both the LRFD design force and the\nASD allowable force.\n\n## Given\n- Material / fasteners: 7⁄8-in.-dia. Group 120 bolts, thread condition N, single shear; bearing-type connection.\n- Geometry: 12 bolts in two vertical rows; gage = 5½ in. (x = ±2.75 in.); s = 3 in. vertical spacing; 6 rows.\n- Load: in-plane eccentric force P, eccentricity ex = 16 in. (θ = 0°); for θ = 15°, ex is reduced by the geometry of the inclined line of action.\n- Assumption: bolt shear controls (bearing/tearout not critical).\n- Code basis: AISC 360-22 (bolt shear strength); IC group coefficient from AISC Manual Table 7-8.\n\n## Find\nThe maximum eccentric force P (LRFD design force and ASD allowable force) for\nθ = 0° and θ = 15°, governed by the available shear strength of the bolt group\nevaluated by the instantaneous-center method.",
 "has_figure": false,
 "stem": "II_A_24",
 "breadcrumb": "EXAMPLE II.A-24 · AISC 360-22 II.A (simple / shear connection) · §J3.7 · Eccentrically Loaded Bolt Group, Instantaneous-Center Method",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-24 · AISC 360-22 II.A (simple / shear connection) · §J3.7 · Eccentrically Loaded Bolt Group, Instantaneous-Center Method

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J3.7/Table J3.2 (Fnv = 54 ksi, Group 120-N; φ = 0.75, Ω = 2.00); eccentric group analysis by the instantaneous-center-of-rotation (IC) method (AISC Manual Part 7, Table 7-8 basis). Bolt shear assumed to control. Per the RAG extract provided.

---

### 1. Bolt Group and Single-Bolt Strength

Twelve 7/8-in. Group 120-N bolts in single shear: two rows at x = ±2.75 in. (5 1/2-in. gage); six per row at y = ±1.5, ±4.5, ±7.5 in. (s = 3 in.). Eccentricity ex = 16 in.

φrn = 0.75(54)(0.601) = **24.3 kips/bolt**; rn/Ω = 54(0.601)/2.00 = **16.2 kips/bolt**

### 2. IC Method — Load Vertical (θ = 0°)

The IC method satisfies equilibrium with each bolt force directed perpendicular to its radius from the instantaneous center and scaled by the load-deformation relationship R = Rult(1 − e^(−10Δ))^0.55. For this 2 × 6 group with ex = 16 in. (Manual Table 7-8 basis):

**C ≈ 3.6**

- **LRFD:** Pu,max = C(φrn) = 3.6(24.3) = **87 kips**
- **ASD:** Pa,max = C(rn/Ω) = 3.6(16.2) = **58 kips**

### 3. IC Method — Load Inclined θ = 15° from Vertical

The inclined line of action both shortens the effective lever arm and shifts the IC, increasing the coefficient:

**C ≈ 4.0**

- **LRFD:** Pu,max = 4.0(24.3) = **97 kips**
- **ASD:** Pa,max = 4.0(16.2) = **65 kips**

### 4. Conclusion

By the IC method, the 12-bolt bracket group supports a maximum eccentric force of approximately **87 kips (LRFD) / 58 kips (ASD)** for a vertical load at ex = 16 in., increasing to about **97 / 65 kips** when the load inclines 15° from vertical. The ~11% gain with inclination reflects the more favorable force distribution about the shifted instantaneous center. These values assume bolt shear governs; bearing/tearout on the bracket and support must separately exceed C × (per-bolt strength), as stipulated.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
