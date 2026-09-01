<!-- chunk_id: II.A-23_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-23",
 "example_family": "II.A-23",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J2.4",
  "J4.2"
 ],
 "eqs": [],
 "tables": [],
 "title": "Welded Pair of Triangular Bracket Plates",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-23 — Welded Pair of Triangular Bracket Plates",
 "question": "# II.A-23 — Welded bracket plate design  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA pair of triangular bracket plates is welded to the flange of a column and\ntogether support a vertical service load applied at the outer tip of the brackets.\nDetermine whether the two bracket plates shown in figures/IIA_23.png are adequate.\nEach plate is ASTM A572/A572M Grade 50 (Fy = 50 ksi, Fu = 65 ksi), ⅜ in. thick;\nthe load is resisted equally by the two plates. Welds use 70-ksi electrodes\n(FEXX = 70 ksi). The column is assumed to have sufficient strength.\n\nGeometry (per the figure): each triangular plate has a vertical edge a = 18 in. at\nthe column and a sloped free edge that drops b = 11½ in.; the applied load acts\nvertically at a horizontal distance e = 8¼ in. from Section A-A (the vertical\nsection at the column face). Each plate is attached to the column by a C-shaped\nfillet weld with a vertical leg l = 18 in. and 3-in. horizontal returns top and\nbottom (kl = 3 in.). Section B-B is the critical section along the sloped free edge.\n\n## Given\n- Material: bracket plates ASTM A572/A572M Grade 50, Fy = 50 ksi, Fu = 65 ksi;\n  weld electrodes 70-ksi (FEXX = 70 ksi).\n- Plates: two ⅜-in.-thick triangular brackets; a = 18 in. (vertical edge),\n  b = 11½ in. (drop of sloped edge), load eccentricity e = 8¼ in.\n- Weld: C-shaped fillet weld per plate, l = 18 in. vertical, kl = 3-in. returns.\n- Loads (service, total resisted by the two plates): dead PD = 9 kips,\n  live PL = 27 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7); bracket-plate\n  procedure per AISC Manual Part 15; eccentric weld group per AISC Manual Part 8.\n\n## Find\nVerify the welded bracket plates are adequate: check shear yielding and flexural\nyielding of the plates on Section A-A, size the eccentrically loaded C-shaped weld\ngroup, confirm minimum/maximum fillet weld sizes, and check the\nshear / normal-force / flexure interaction on the sloped Section B-B (including\nlocal yielding/buckling).",
 "has_figure": true,
 "stem": "II_A_23",
 "breadcrumb": "EXAMPLE II.A-23 · AISC 360-22 II.A (simple / shear connection) · §J2.4 §J4.2 · Welded Pair of Triangular Bracket Plates",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-23 · AISC 360-22 II.A (simple / shear connection) · §J2.4 §J4.2 · Welded Pair of Triangular Bracket Plates

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2.4 (eccentric C-shaped fillet weld groups, Manual Part 8 coefficients), §J4.2; bracket-plate free-edge procedure per AISC Manual Part 15. Per the RAG extract provided.

---

### 1. Required Strength

Total P: D = 9 kips, L = 27 kips → **LRFD Pu = 54.0 kips; ASD Pa = 36.0 kips**, shared equally:
**per plate: 27.0 kips (LRFD) / 18.0 kips (ASD)**, at e = 8 1/4 in. from Section A-A.

Each plate: PL3/8 (A572 Gr. 50), a = 18 in. vertical edge, b = 11 1/2 in. drop; C-shaped E70 fillet weld, l = 18 in. vertical + 3-in. returns (k = 0.167).

### 2. Weld Group (per plate) — Manual Part 8 / §J2.4

Group centroid offset x̄l = k²l/(1 + 2k) = 0.375 in. → load eccentricity al = 8.25 + 0.38 = 8.63 in. (a ≈ 0.48). Eccentric coefficient C ≈ 1.3. Using **1/4-in. fillets (D = 4)** (≥ Table J2.4 minimum for the column flange):

φRn = C·C1·D·l = 1.3(4)(18) = **93.6 kips ≥ 27.0 ✓**; Rn/Ω = **62.4 kips ≥ 18.0 ✓** (utilization 0.29)

### 3. Section A-A (per plate)

V = 27.0 kips; M = 27.0(8.25) = 223 kip-in. Plate d = 18 in., t = 3/8 in.:
Flexural yielding φMn = 0.9(50)(0.375 × 18²/4) = 1,370 kip-in. ✓; shear yielding 0.6(50)(6.75) = 203 kips ✓.

### 4. Section B-B (sloped free edge) — Manual Part 15

λ = (b/t)√Fy/[5√(475 + 1,120(b/a)²)] = 30.7(7.07)/[5√(475 + 457)] = **1.42 ≈ 1.41 boundary**
→ Fcr = 1.30Fy/λ² = **32.2 ksi**; φFcr = 29.0 ksi / Fcr,Ω = 19.3 ksi

Maximum combined stress on the 21.4-in. inclined section per plate: f ≈ 3.4 (direct) + ≈6.6 (flexural) ≈ **10 ksi ≤ 29.0 ksi ✓** (ASD ≈6.7 ≤ 19.3 ✓)

### 5. Conclusion

**The pair of 3/8-in. welded bracket plates with 1/4-in. C-shaped E70 fillet welds (18-in. legs, 3-in. returns) is adequate** for the 54-kip (LRFD) / 36-kip (ASD) tip load. All elements carry the per-plate share of 27/18 kips with large margins — welds at ~29% utilization and the sloped free edge at ~35% of its Part 15 buckling stress. Splitting the load between two plates makes this detail considerably more robust than the single bolted bracket of Example II.A-22.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-23 (from figures/IIA_23.png)

Welded triangular bracket plates — a **pair** of ⅜-in. plates (2 PL⅜ × 14½ × 1'-6"
shaped) welded to a W14×90 column flange; load resisted equally by the two plates
(P_D = 9 kips, P_L = 27 kips total).

- **Bracket geometry (each plate):** vertical edge at the column **a = 18 in.**;
  sloped free edge drops **b = 11½ in.**; load eccentricity **e = 8¼ in.** from
  Section A-A. Top horizontal extent 7⅞ in. to the load; b' and a' are the
  sloped-edge resultant directions at angle θ.
- **Weld (each plate to column):** 3/16-in. C-shaped fillet — vertical leg
  l = 18 in. with **3-in. returns top and bottom** (kl = 3 in.); "min." weld noted.
- Dimensions at base: 3 in., 3⅜ in., and b = 14½ in. (overall). **Section B-B** is
  the critical section along the sloped free edge.
