<!-- chunk_id: II.A-13_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-13",
 "example_family": "II.A-13",
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
 "title": "Bolted/Welded Unstiffened Seated Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-13 — Bolted/Welded Unstiffened Seated Connection (Beam to Column Flange)",
 "question": "# II.A-13 — Bolted/Welded Unstiffened Seated Connection (Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W21×62 beam is supported on an unstiffened seat welded to the\n**flange** of an ASTM A992/A992M W14×61 column. The seat is a single angle whose\nvertical leg is fillet-welded (70-ksi electrodes) to the column flange and whose\nhorizontal outstanding leg carries the beam bottom flange; the beam is bolted to the\nseat with two ¾-in.-diameter Group 120 (thread condition N) bolts. A top angle holds\nthe beam laterally. Angles are ASTM A572/A572M Grade 50. The geometry is shown in\nfigures/IIA_13.png.\n\nThe beam delivers a service dead-load reaction R_D = 9 kips and a service live-load\nreaction R_L = 27.5 kips.\n\nVerify that an 8-in.-long L8×4×⅝ seat angle (4-in. outstanding leg) welded with 5/16-in.\nfillet welds is adequate, and confirm that the supplied bearing length satisfies the\nbeam-web limit states.\n\n## Given\n- Material: beam and column ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); angles ASTM\n  A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); weld electrodes 70 ksi (F_EXX = 70).\n- Beam: W21×62 — d = 21.0 in., t_w = 0.400 in., b_f = 8.24 in., t_f = 0.615 in.,\n  k_des = 1.12 in.\n- Column: W14×61 — flange t_f = 0.645 in.\n- Seat angle: 8-in.-long L8×4×⅝ (4-in. OSL), 5/16-in. fillet welds to the column flange;\n  two ¾-in.-dia. Group 120 (N) bolts beam-to-seat. Top angle L4×4×¼.\n- Loads (service): R_D = 9 kips, R_L = 27.5 kips.\n- Code basis: AISC 360-22 (load combinations from ASCE/SEI 7).\n\n## Find\nThe minimum required bearing length for the beam web (web local yielding and web local\ncrippling), and the available strength of the seat — outstanding-leg capacity and the\nfillet-weld capacity — confirming each exceeds the required reaction.",
 "has_figure": true,
 "stem": "II_A_13",
 "breadcrumb": "EXAMPLE II.A-13 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Bolted/Welded Unstiffened Seated Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-13 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Bolted/Welded Unstiffened Seated Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (Eq. J10-3), §J10.3 (Eq. J10-5a), §J2 (fillet welds, Table J2.4/J2.5), §J4.2; seated-connection model per AISC Manual Part 10 (Table 10-8 basis). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 9 kips, L = 27.5 kips → **LRFD Ru = 54.8 kips; ASD Ra = 36.5 kips**

Seat: L8x4x5/8 × 8 in. (A572 Gr. 50), 4-in. OSL; vertical leg welded to the W14x61 column flange with two 5/16-in. E70 fillets × 8 in. (plus 5/8-in. top returns); beam W21x62 (tw = 0.400 in., tf = 0.615 in., kdes = 1.12 in.) bolted to the seat with two 3/4-in. Group 120-N bolts; 1/2-in. setback.

### 2. Required Bearing Length — Beam Web

**Web local yielding (Eq. J10-3):** lb,req = Ru/(Fywtw) − 2.5kdes = 54.8/[50(0.400)] − 2.80 = 2.74 − 2.80 < 0 → **any contact bearing suffices** (ASD identical).

**Web local crippling (Eq. J10-5a, lb/d ≤ 0.2):** at lb → 0: Rn = 0.40tw²√(EFywtf/tw) = 0.40(0.160)(1,493) = 95.6 kips → φRn = 71.7 ≥ 54.8 ✓; Rn/Ω = 47.8 ≥ 36.5 ✓.

Use the practical minimum lb = 3/4 in.; provided OSL bearing ≈ 3.5 in. ✓ — **beam-web limit states satisfied.**

### 3. Seat Angle (Outstanding Leg)

Reaction eccentricity to the angle critical section: e = setback + lb/2 − (t + 3/8) = 0.50 + 0.38 − 1.00 < 0 → flexural yielding of the OSL is not critical. Leg shear (Eq. J4-3): 0.6(50)(8)(0.625) = 150 kips ≥ demands ✓.

### 4. Welds to the Column Flange

Two vertical 5/16-in. fillets (D = 5), L = 8 in. each; reaction at e = setback + lb/2 = 0.875 in. from the weld plane. Elastic line-weld stresses per weld:

fv = Ru/(2L) = 54.8/16 = 3.43 kip/in.; fh = 6(Ru e/2)/L² = 6(24.0)/64 = 2.25 kip/in. → resultant = **4.10 kip/in.**

Available (E70, per 1/16 leg): 1.392D = **6.96 kip/in. ≥ 4.10 ✓** (LRFD); 0.928D = 4.64 ≥ 2.73 ✓ (ASD).

(Even with the reaction conservatively placed at the midpoint of the OSL bearing, e = 2.25 in., the resultant is 6.72 ≤ 6.96 kip/in. — still adequate.) Minimum weld size for the 0.645-in. column flange = 1/4 in. ≤ 5/16 in. ✓ (Table J2.4).

### 5. Bolts and Top Angle

The two 3/4-in. Group 120-N beam-to-seat bolts position the beam and transfer nominal horizontal forces (φrn = 17.9 kips each in shear — far above any calculated demand). The L4x4x1/4 top angle provides lateral stability only, per Manual practice.

### 6. Conclusion

**The welded 8-in. L8x4x5/8 seat with 5/16-in. E70 fillets is adequate** for the 54.8-kip (LRFD) / 36.5-kip (ASD) reaction: the W21x62 web needs essentially no bearing length beyond contact (yielding) and passes crippling at the minimum bearing, the angle leg is not flexure-critical, and the eccentrically loaded vertical welds work at ~59% utilization. The connection complies with AISC 360-22 Chapters J and applicable Manual seated-connection practice.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-13 (from figures/IIA_13.png)

Bolted/welded unstiffened seated connection to a **column flange** (W14×61);
beam W21×62 on the seat.

- **Seat angle:** L8×4×⅝ × 0'-8" (8 in. long), **4-in. outstanding leg (OSL)**.
- **Beam-to-seat bolts:** (2) ¾-in. Group 120 (N) bolts in standard holes.
- **Weld of seat to column flange:** 5/16-in. fillet along the two vertical edges
  of the seat's vertical leg, with a **⅝-in. return at the top**; the seat outline
  is 8 in. wide × 8 in. (vertical leg), per the elevation/section.
- **Top angle:** L4×4×¼ (an "optional top angle location" is also indicated);
  provides lateral stability only.
- ½-in. nominal beam setback.
