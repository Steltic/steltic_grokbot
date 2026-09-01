<!-- chunk_id: II.A-14_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-14",
 "example_family": "II.A-14",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J10.2",
  "J10.3",
  "J2",
  "J4.2"
 ],
 "eqs": [
  "J10-3",
  "J10-5a"
 ],
 "tables": [
  "J2.4",
  "10"
 ],
 "title": "Stiffened Seated Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-14 — Stiffened Seated Connection (Beam to Column Flange)",
 "question": "# II.A-14 — Stiffened Seated Connection — Welded Stiffening Element (Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W21×68 beam is supported on a **stiffened** seat welded to the\n**flange** of an ASTM A992/A992M W14×90 column. The seat consists of a horizontal seat\nplate with a vertical stiffener plate beneath it; the stiffener is fillet-welded (70-ksi\nelectrodes) to the column flange, and the seat plate is welded to both the stiffener and\nthe column flange. A top angle provides lateral stability. Plate and angle material is\nASTM A572/A572M Grade 50. The geometry is shown in figures/IIA_14.png.\n\nThe beam delivers a service dead-load reaction R_D = 21 kips and a service live-load\nreaction R_L = 62.5 kips.\n\nDetermine the minimum seat (stiffener) width required by the beam-web limit states, and\nverify a stiffener length of 15 in. with 5/16-in. fillet welds, the seat-plate\ndimensions, and the minimum stiffener-plate thickness.\n\n## Given\n- Material: beam and column ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); angle and\n  plates ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); weld electrodes 70 ksi.\n- Beam: W21×68 — d = 21.1 in., t_w = 0.430 in., b_f = 8.27 in., t_f = 0.685 in.,\n  k_des = 1.19 in.\n- Column: W14×90 — flange t_f = 0.710 in.\n- Trial seat: seat plate PL⅝×7×9, stiffener PL⅝×7×1'-3\" (l = 15 in.), 5/16-in. fillet\n  welds; ¾-in.-dia. Group 120 (N) bolts (5½-in. gage) beam-to-seat; top angle L4×4×¼.\n- Loads (service): R_D = 21 kips, R_L = 62.5 kips. Setback ½ in., underrun ¼ in.\n- Code basis: AISC 360-22 (load combinations from ASCE/SEI 7).\n\n## Find\nThe minimum stiffener (seat) width W from web local yielding and web local crippling of\nthe beam; verification that the 7-in. seat with a 15-in. stiffener and 5/16-in. fillet\nwelds develops the required reaction; and the minimum stiffener-plate thickness to\ndevelop the seat-plate weld.",
 "has_figure": true,
 "stem": "II_A_14",
 "breadcrumb": "EXAMPLE II.A-14 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Stiffened Seated Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-14 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Stiffened Seated Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (Eq. J10-3), §J10.3 (Eqs. J10-5a/b), §J2 (fillet welds; Table J2.4/J2.5), §J4.2 (base-metal development); stiffened-seat model per AISC Manual Part 10 (e = 0.8W; Table 10-9 basis). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 21 kips, L = 62.5 kips → **LRFD Ru = 1.2(21) + 1.6(62.5) = 125 kips; ASD Ra = 83.5 kips**

Beam W21x68: tw = 0.430 in., tf = 0.685 in., kdes = 1.19 in., d = 21.1 in. Setback 1/2 in. + underrun 1/4 in. = 3/4 in. effective.

### 2. Minimum Seat (Stiffener) Width — Beam Web Limit States

**Web local yielding (Eq. J10-3):** lb,req = Ru/(Fywtw) − 2.5kdes = 125/[50(0.430)] − 2.98 = **2.84 in.** (ASD the same)

**Web local crippling:** at lb/d = 0.2 the Eq. J10-5a capacity is φRn = 110 kips < 125 → solve Eq. J10-5b (lb/d > 0.2):
125 = 0.75(0.40)(0.430)²[1 + (4lb/21.1 − 0.2)(0.430/0.685)^1.5]√(EFywtf/tw) → **lb,req = 6.2 in.** ← governs (ASD identical)

Required width: W ≥ lb,req + setback + underrun = 6.2 + 0.75 = 6.9 in. → **W = 7 in. ✓ (trial seat adequate in width).**

### 3. Stiffener-to-Column Welds (two vertical 5/16-in. E70 fillets, l = 15 in.)

Per Manual stiffened-seat practice the reaction acts at e = 0.8W = 5.6 in. from the weld plane; a/l = 0.37. Using the out-of-plane eccentric weld-group coefficients (Manual Table 8-4 basis, k = 0): C ≈ 1.68:

- **LRFD:** φRn = C·C1·D·l = 1.68(1.0)(5)(15) = **126 kips ≥ 125 kips ✓**
- **ASD:** Rn/Ω = 126(0.928/1.392) = **84.0 kips ≥ 83.5 kips ✓**

The 15-in. stiffener with 5/16-in. fillets is adequate (essentially fully utilized). Minimum weld for the 0.710-in. column flange = 1/4 in. ≤ 5/16 ✓ (Table J2.4).

### 4. Minimum Stiffener Thickness

To develop the pair of 5/16-in. welds in the Gr. 50 stiffener (§J4.2 base metal matching):
shear yielding: t ≥ 2(1.392D)/(0.6Fy) = 13.9/30 = 0.46 in.; shear rupture: t ≥ 2(1.392D)/(0.75 × 0.6Fu) = 0.48 in.
Also t_st ≥ beam tw = 0.43 in. → **t_st = 5/8 in. ✓** (PL5/8 trial OK). The fitted stiffener bearing (Eq. J7-1) and seat-plate welds are satisfied by the PL5/8 × 7 × 9 seat with the detailed welds.

### 5. Conclusion

**The trial stiffened seat — PL5/8 × 7 × 9 seat plate over a PL5/8 × 7 × 15 stiffener, 5/16-in. E70 fillets, with two 3/4-in. Group 120-N positioning bolts and an L4x4x1/4 top angle — is adequate** for the 125-kip (LRFD) / 83.5-kip (ASD) reaction. Web local crippling of the W21x68 sets the 7-in. seat width (lb,req = 6.2 in. ≫ the 2.8 in. from web yielding), and the eccentrically loaded stiffener welds (e = 0.8W) are the governing seat check at ≈100% utilization — the 15-in. stiffener length should not be reduced.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-14 (from figures/IIA_14.png)

Stiffened seated connection welded to a **column flange** (W14×90); beam W21×68.

- **Seat plate:** PL⅝ × 7 in. × 9 in.; **stiffener plate:** PL⅝ × 7 in. × 1'-3"
  (length **l = 15 in.**), fitted to bear under the seat plate. Stiffener width
  **W = 7 in.**
- **Welds:** 5/16-in. fillet welds (stiffener to column flange down both vertical
  edges; seat plate to stiffener and to column). "Weld toe only" noted at the top;
  ⅝-in. return; the "3" weld-size designator and 5/16 marks appear on the section.
- **Top angle:** L4×4×¼, shop-attached to the beam (with an "optional" alternate
  location); (2) ¾-in. Group 120 (N) bolts, standard holes; 5½-in. gage; "4 in.
  (min.)" / "4 in. (optional)" top-angle dimensions.
- 9-in. seat projection; 3-in. dimension and 1-in. dimension at the column;
  ½-in. nominal setback; "optional trim lines" shown on the stiffener.
