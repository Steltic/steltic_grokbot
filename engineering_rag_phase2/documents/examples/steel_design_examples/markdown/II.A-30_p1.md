<!-- chunk_id: II.A-30_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-30",
 "example_family": "II.A-30",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "All-Bolted Tee Shear Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-30 — All-Bolted Tee Shear Connection (Beam to Column Flange)",
 "question": "# II.A-30 — All-Bolted Tee Connection (Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simple beam-end shear connection uses a structural tee to join a beam to a column flange.\nThe stem of the tee is bolted to the beam web, and the tee flange is bolted to the column flange.\n\nThe supported beam is an ASTM A992 W16×50 (Fy = 50 ksi, Fu = 65 ksi; tw = 0.380 in., d = 16.3 in.,\ntf = 0.630 in.). The supporting member is an ASTM A992 W14×90 column (flange tf = 0.710 in.).\nThe connecting tee is an ASTM A992 WT5×22.5 (Fy = 50 ksi, Fu = 65 ksi; depth d = 5.05 in.,\nstem thickness tsw = 0.350 in., flange width bf = 8.02 in., flange thickness tf = 0.620 in.).\n\nThrough the tee stem to the beam web there are four ¾-in.-diameter Group 120 bolts (thread\ncondition N) in standard holes (dh = 13/16 in., Ab = 0.442 in.²), in a single vertical line at\n3-in. pitch (3 @ 3 in. = 9 in.; overall stem length l = 11½ in.), with a 1¼-in. end distance and\na horizontal edge distance leh = 1¼ in. Through the tee flange to the column flange there are\neight ¾-in. Group 120 bolts (two vertical lines of four) on a 2¾-in. + 2¾-in. gage. The distance\nfrom the face of the support (column flange) to the stem bolt line is a = d − leh = 5.05 − 1.25 =\n3.80 in., which produces eccentricity on the stem bolt group. The geometry is shown in\nfigures/IIA_30.png.\n\n## Given\n- Material: beam, column, tee all ASTM A992 (Fy = 50 ksi, Fu = 65 ksi).\n- Geometry: WT5×22.5, stem length l = 11½ in.; 4 bolts ¾-in. Group 120 (N) std. holes at 3-in. pitch through stem; 8 bolts through flange (2 rows of 4) on 2¾+2¾-in. gage; leh = lev = 1¼ in.; eccentricity a = 3.80 in.\n- Members: W16×50 beam (tw = 0.380 in.); W14×90 column (tf = 0.710 in.).\n- Loads (service): dead reaction RD = 6 kips, live reaction RL = 18 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nDetermine the available strength (LRFD φRn and ASD Rn/Ω) of the all-bolted tee connection,\nconsidering the governing limit states — the eccentrically loaded stem bolt group (shear,\nbearing/tearout), flexural yielding and rupture of the stem, shear yielding, shear rupture and\nblock shear rupture of the stem, and the flange-to-column bolts — and confirm adequacy for the\nrequired end reaction.",
 "has_figure": true,
 "stem": "II_A_30",
 "breadcrumb": "EXAMPLE II.A-30 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Tee Shear Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-30 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 · All-Bolted Tee Shear Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2/§J4.3; tee shear-connection model per AISC Manual Part 10 (stem bolt group carries the eccentricity a = d − leh; flange bolts carry direct shear; tee selected for rotational ductility). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6 kips, L = 18 kips → **LRFD Ru = 36.0 kips; ASD Ra = 24.0 kips**

WT5x22.5 (A992): stem (ts = 0.350 in., l = 11 1/2 in.) bolted to the W16x50 web with four 3/4-in. Group 120-N bolts @ 3 in. (lev = leh = 1 1/4 in.); flange (tf = 0.620 in.) bolted to the W14x90 column flange with eight bolts (2 × 4, 2 3/4-in. gages). Stem-bolt eccentricity e = a = 5.05 − 1.25 = **3.80 in.**

### 2. Stem Bolt Group (eccentric)

C (4 bolts @ 3 in., e = 3.80 in.) ≈ 2.45:

φRn = 2.45(17.9) = **43.9 kips ≥ 36.0 ✓**; Rn/Ω = 2.45(11.9) = **29.2 kips ≥ 24.0 ✓** (**governing**, 82% utilized)

Bearing on the stem (φ = 30.7 kips/bolt) and bottom-bolt tearout (φ = 17.2 kips vs. 17.9 bolt shear — interchangeable within the group) and beam-web bearing (φ = 33.3) do not change the outcome.

### 3. Flange Bolt Group

Eight bolts in direct shear: φRn = 8(17.9) = **143 kips ≥ 36.0 ✓** (ASD 95.5 ≥ 24.0 ✓); the thin-flange flexing of the WT provides the simple-connection rotation, and bolt tension from the small end moment is negligible by the Part 10 model. Column-flange bearing: ample.

### 4. Tee Limit States

- Stem shear yielding (Eq. J4-3): 0.6(50)(4.03) = 121 kips → 121/80.4 ✓
- Stem shear rupture (Eq. J4-4, Anv = 2.80 in.²): φRn = 81.9/54.6 ✓
- Stem block shear (Eq. J4-5): φRn ≈ 70/47 ✓
- Stem flexure at the bolt line (M = 36.0 × 3.80 = 137 kip-in.): φMn = 0.9(50)(11.6) = 521 kip-in. ✓
- Rotational ductility: stem and flange thicknesses satisfy the Part 10 flexibility limits for a WT5x22.5 ✓

### 5. Conclusion

The WT5x22.5 tee connection is **adequate** for 36.0 kips (LRFD) / 24.0 kips (ASD). The governing limit state is the **eccentrically loaded four-bolt stem group (e = 3.80 in.) at ~82% utilization** — the relatively large eccentricity, set by the tee depth minus edge distance, is the price of the tee configuration; all other elements, including the eight-bolt flange group, carry the load with large reserves.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-30 (from figures/IIA_30.png)

All-bolted tee connection: WT5×22.5 stem bolted to a W16×50 beam web; tee flange
bolted to a W14×90 column flange.

- **Stem to beam web:** single vertical line of **4 bolts**, ¾-in. Group 120 (N),
  standard holes, 3 @ 3 in. = 9 in., l_ev = 1¼ in., l_eh = 1¼ in.; tee length
  l = 11½ in. Distance from support face to stem bolt line **a = 3.80 in.**
  (= d − l_eh = 5.05 − 1.25), producing eccentricity on the stem bolt group.
- **Flange to column flange:** **8 bolts** (two vertical lines of 4) on a
  **2¾ + 2¾-in. gage** about the beam/column centerline (Section at right).
