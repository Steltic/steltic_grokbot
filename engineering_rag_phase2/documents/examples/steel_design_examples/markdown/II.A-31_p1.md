<!-- chunk_id: II.A-31_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-31",
 "example_family": "II.A-31",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J2.4",
  "J4.2",
  "J4.3"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Bolted/Welded Tee Shear Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-31 — Bolted/Welded Tee Shear Connection (Beam to Column Flange)",
 "question": "# II.A-31 — Bolted/Welded Tee Connection (Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simple beam-end shear connection uses a structural tee whose stem is bolted to the beam web\nand whose flange is welded to the column flange.\n\nThe supported beam is an ASTM A992 W16×50 (Fy = 50 ksi, Fu = 65 ksi; tw = 0.380 in., d = 16.3 in.,\ntf = 0.630 in.). The supporting member is an ASTM A992 W14×90 column (flange tf = 0.710 in.).\nThe connecting tee is an ASTM A992 WT5×22.5 (Fy = 50 ksi, Fu = 65 ksi; depth d = 5.05 in.,\nstem thickness tsw = 0.350 in., flange width bf = 8.02 in., flange thickness tf = 0.620 in.,\nk1 = 13/16 in.).\n\nThrough the tee stem to the beam web there are four ¾-in.-diameter Group 120 bolts (thread\ncondition N) in standard holes (dh = 13/16 in., Ab = 0.442 in.²) in a single vertical line at\n3-in. pitch (3 @ 3 in. = 9 in.; stem length l = 11½ in.), with lev = leh = 1¼ in. The tee flange\nis welded to the column flange with ¼-in. fillet welds (one along each vertical flange edge,\nlength l = 11½ in.) using 70-ksi electrodes (FEXX = 70 ksi). The distance from the face of the\nsupport to the stem bolt line is a = d − leh = 5.05 − 1.25 = 3.80 in., producing eccentricity on\nthe stem bolt group. The geometry is shown in figures/IIA_31.png.\n\n## Given\n- Material: beam, column, tee all ASTM A992 (Fy = 50 ksi, Fu = 65 ksi). Weld 70-ksi electrodes.\n- Geometry: WT5×22.5, stem length l = 11½ in.; 4 bolts ¾-in. Group 120 (N) std. holes at 3-in. pitch through stem; ¼-in. fillet welds (both flange edges) to column; leh = lev = 1¼ in.; eccentricity a = 3.80 in.\n- Members: W16×50 beam (tw = 0.380 in.); W14×90 column (tf = 0.710 in.).\n- Loads (service): dead reaction RD = 6 kips, live reaction RL = 18 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nDetermine the available strength (LRFD φRn and ASD Rn/Ω) of the bolted/welded tee connection,\nconsidering the governing limit states — the flange-to-column fillet welds, the eccentrically\nloaded stem bolt group (shear, bearing/tearout), flexural yielding and rupture of the stem, and\nshear yielding, shear rupture and block shear rupture of the stem — and confirm adequacy for the\nrequired end reaction.",
 "has_figure": true,
 "stem": "II_A_31",
 "breadcrumb": "EXAMPLE II.A-31 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J2.4 §J4.2 §J4.3 · Bolted/Welded Tee Shear Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-31 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J2.4 §J4.2 §J4.3 · Bolted/Welded Tee Shear Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J2.4/Tables J2.4–J2.5, §J4.2/§J4.3; Manual Part 10 tee-connection model (stem bolts carry e = d − leh; welded flange carries direct shear; ductility limits on the tee). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6 kips, L = 18 kips → **LRFD Ru = 36.0 kips; ASD Ra = 24.0 kips**

WT5x22.5 (A992): stem bolted to the W16x50 web (four 3/4-in. Group 120-N @ 3 in.; e = a = 3.80 in.); flange welded to the W14x90 column flange with two vertical 1/4-in. E70 fillets, l = 11 1/2 in.

### 2. Stem Bolt Group (eccentric, e = 3.80 in.)

C ≈ 2.45 → φRn = 2.45(17.9) = **43.9 kips ≥ 36.0 ✓**; Rn/Ω = **29.2 kips ≥ 24.0 ✓** (**governing**, 82% utilized). Stem bearing/tearout and beam-web bearing as in Example II.A-30 — not controlling.

### 3. Flange Welds

Direct shear per inch: fv = 36.0/(2 × 11.5) = 1.57 kip/in. ≪ 1.392(4) = 5.57 kip/in. ✓ — ample margin even allowing for incidental flexure from the simple-beam end rotation, which the flexible tee flange (bending between the weld lines and the k1 region) accommodates per the Part 10 ductility model.

Weld size limits (Table J2.4): minimum for the thinner part (0.620-in. tee flange) = 1/4 in. = provided ✓; column-flange base metal develops the welds ✓.

### 4. Tee Limit States

Stem shear yielding 121 kips, shear rupture φ = 81.9 kips, block shear φ ≈ 70 kips, stem flexure φMn = 521 kip-in. vs. 137 kip-in. — all ✓ (as in Example II.A-30).

### 5. Conclusion

The bolted-stem/welded-flange WT5x22.5 connection is **adequate** for 36.0 kips (LRFD) / 24.0 kips (ASD), governed — as in the all-bolted version — by the **eccentric stem bolt group at ~82% utilization**. The 1/4-in. flange welds are very lightly stressed; their size is dictated by the Table J2.4 minimum, and the tee flange flexibility supplies the simple-connection rotation capacity.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-31 (from figures/IIA_31.png)

Bolted/welded tee connection: WT5×22.5 stem bolted to a W16×50 beam web; tee
flange **welded** to a W14×90 column flange.

- **Stem to beam web:** single vertical line of **4 bolts**, ¾-in. Group 120 (N),
  standard holes, 3 @ 3 in. = 9 in., l_ev = l_eh = 1¼ in.; tee length l = 11½ in.;
  **a = 3.80 in.** from support face to stem bolt line (eccentricity on the group).
- **Flange to column flange:** ¼-in. fillet weld along each vertical flange edge,
  length l = 11½ in. (weld marks ¼ and ½ shown on the section).
