<!-- chunk_id: II.A-15_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-15",
 "example_family": "II.A-15",
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
 "tables": [],
 "title": "Stiffened Seated Connection (Beam to Column Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-15 — Stiffened Seated Connection (Beam to Column Web)",
 "question": "# II.A-15 — Stiffened seated connection, welded stiffener to a column web  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA stiffened seated connection carries the end reaction of an ASTM A992/A992M\nW21×68 beam onto the WEB of an ASTM A992/A992M W14×90 column, as shown in\nfigures/IIA_15.png. The seat is built from a seat plate and a triangular stiffener\nplate, both ASTM A572/A572M Grade 50 (Fy = 50 ksi, Fu = 65 ksi), all-welded to the\ncolumn web with 70-ksi electrodes (FEXX = 70 ksi). A top angle stabilizes the beam.\nVerify the connection and confirm the seat geometry, weld sizes, and plate\nthicknesses are adequate. Assume a ½-in. nominal beam setback and a ¼-in. underrun\ntolerance.\n\nConfiguration (per the figure): the stiffener and seat plate are fillet-welded to\nthe column web; a top angle L4×4×¼ is used (two ¾-in.-dia. Group 120 bolts, thread\ncondition N, in the beam leg; toe of the angle welded to the column web). The seat\nplate is a PL⅝×7×9 and the stiffener a PL⅝×7×1′-3″ (length l = 15 in.), connected\nwith ⁵⁄₁₆-in. fillet welds.\n\n## Given\n- Beam: W21×68, ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); d = 21.1 in.,\n  tw = 0.430 in., bf = 8.27 in., tf = 0.685 in., kdes = 1.19 in.\n- Column: W14×90, ASTM A992; web tw = 0.440 in., T = 10 in. Seat is on the column WEB.\n- Seat/stiffener/angle plate: ASTM A572 Grade 50 (Fy = 50, Fu = 65); welds 70-ksi.\n- Loads (service): dead RD = 21 kips, live RL = 62.5 kips.\n- Detailing tolerances: ½-in. setback, ¼-in. underrun.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7); stiffened-seat\n  procedure per AISC Manual Part 10 with Part 9 concentrated-force aids.\n\n## Find\nDetermine the required stiffener width W (governed by beam web local yielding and\nweb local crippling), confirm the stiffener length/weld combination has adequate\nstrength, check the seat-plate welds, the stiffener-plate minimum thickness, and\nthe column-web base-metal limit for the welded seat (one-sided vs. two-sided).",
 "has_figure": true,
 "stem": "II_A_15",
 "breadcrumb": "EXAMPLE II.A-15 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Stiffened Seated Connection (Beam to Column Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-15 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Stiffened Seated Connection (Beam to Column Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (Eq. J10-3), §J10.3 (Eqs. J10-5a/b), §J2/Tables J2.4–J2.5, §J4.2 (base metal); AISC Manual Part 10 stiffened-seat procedure (e = 0.8W; one-sided/two-sided web minimums 3.09D/Fu and 6.19D/Fu). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 21 kips, L = 62.5 kips → **LRFD Ru = 125 kips; ASD Ra = 83.5 kips**

Seat (per figure): PL5/8 × 7 × 9 seat plate; PL5/8 × 7 × 15 triangular stiffener (fit to bear); 5/16-in. E70 fillets to the W14x90 **column web** (tw = 0.440 in., T = 10 in.); L4x4x1/4 top angle; setback 1/2 in. + underrun 1/4 in.

### 2. Required Stiffener Width — Beam Web (W21x68)

As in Example II.A-14 (identical beam and reaction):
- Web local yielding (Eq. J10-3): lb,req = 125/[50(0.430)] − 2.5(1.19) = **2.84 in.**
- Web local crippling (Eq. J10-5b governs): **lb,req = 6.2 in.** ← controls

W ≥ 6.2 + 0.75 (setback + underrun) = 6.9 in. → **W = 7 in. provided ✓** (seat fits the T = 10 in. web depth ✓).

### 3. Stiffener-to-Web Welds (two vertical 5/16-in. fillets, l = 15 in.)

Reaction at e = 0.8W = 5.6 in.; a/l = 0.37 → eccentric out-of-plane weld coefficient C ≈ 1.68:

- **LRFD:** φRn = 1.68(5)(15) = **126 kips ≥ 125 ✓** **ASD:** Rn/Ω = **84.0 kips ≥ 83.5 ✓**

Minimum weld for 0.440-in. web = 3/16 in. ≤ 5/16 ✓.

### 4. Column-Web Base Metal (one-sided vs. two-sided seats)

Minimum web thickness to develop the pair of 5/16-in. (D = 5) fillets:

- **Seat on one side of the web (this case):** tw,min = 3.09D/Fu = 3.09(5)/65 = **0.24 in. ≤ 0.440 in. ✓**
- If identical seats were placed on **both** sides of the web at the same location: tw,min = 6.19D/Fu = **0.48 in. > 0.440 in. ✗** — not permitted without reducing weld size/demand.

The present one-sided seat is acceptable; a future mirrored connection at this location would require re-design.

### 5. Stiffener Thickness and Seat Plate

Develop the welds in Gr. 50 plate (§J4.2): t ≥ 2(1.392D)/(0.6Fy) ≈ 0.46 in. and ≥ beam tw = 0.43 in. → **5/8 in. provided ✓**. Seat plate PL5/8 × 7 × 9 with 5/16-in. welds to the stiffener and web positions the beam (two 3/4-in. Group 120-N bolts at 5 1/2-in. gage) and is adequate by inspection; the fitted stiffener bears per Eq. J7-1.

### 6. Conclusion

**The all-welded stiffened seat on the column web is adequate** for 125 kips (LRFD) / 83.5 kips (ASD): beam-web crippling fixes the 7-in. stiffener width, the 15-in. stiffener with 5/16-in. fillets is at ≈100% utilization (do not shorten), the 5/8-in. plate develops the welds, and the 0.440-in. column web satisfies the one-sided base-metal minimum (0.24 in.) — though it could not support seats on both faces simultaneously. Detail with the top stability angle as shown.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-15 (from figures/IIA_15.png)

Stiffened seated connection welded to a **column web** (W14×90, T = 10 in.);
beam W21×68. (Same seat build-up as II.A-14, but attached to the column web.)

- **Seat plate:** PL⅝ × 7 in. × 9 in.; **triangular stiffener plate:** PL⅝ × 7 in.
  × 1'-3" (length **l = 15 in.**); stiffener "fit to bear." Stiffener width
  **W = 7 in.**
- **Welds:** 5/16-in. fillet welds to the column web; "weld toe only" at top;
  ⅝-in. return; 5/16 and "3" weld marks on the section. Because it attaches to the
  web, the column-web base-metal limit (one-sided vs two-sided) is checked.
- **Top angle:** L4×4×¼, shop-attached to beam ("optional location" shown); (2)
  ¾-in. Group 120 (N) bolts, standard holes; 5½-in. gage; "4 in. (min./optional)".
- 9-in. seat projection; 3-in. and 1-in. dimensions at the column; ½-in. setback;
  optional trim lines on the stiffener.
