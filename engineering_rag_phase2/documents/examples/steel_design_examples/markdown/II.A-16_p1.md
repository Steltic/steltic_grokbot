<!-- chunk_id: II.A-16_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-16",
 "example_family": "II.A-16",
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
  "J2.4"
 ],
 "title": "Offset Unstiffened Seated Connection (Beam to Column Flange)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-16 — Offset Unstiffened Seated Connection (Beam to Column Flange)",
 "question": "# II.A-16 — Offset Unstiffened Seated Connection (Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W14×38 beam is supported on an unstiffened seat welded to the\n**flange** of an ASTM A992/A992M W12×65 column, but the beam is **offset 5½ in.** from\nthe centerline of the seat so that the two vertical seat-angle welds are loaded\nunequally (the reaction is eccentric to the weld group). The seat angle is welded to the\ncolumn flange with 70-ksi electrodes and the beam is bolted to the horizontal\noutstanding leg with two ¾-in.-diameter Group 120 (thread condition N) bolts. A top\nangle provides lateral stability. The angle is ASTM A572/A572M Grade 50. The geometry is\nshown in figures/IIA_16.png.\n\nThe beam delivers a service dead-load reaction R_D = 5 kips and a service live-load\nreaction R_L = 15 kips.\n\nDetermine the seat angle and weld size required, accounting for the eccentricity created\nby the offset, and confirm the beam-web limit states.\n\n## Given\n- Material: beam and column ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); angle ASTM\n  A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); weld electrodes 70 ksi.\n- Beam: W14×38 — d = 14.1 in., k_des = 0.915 in.\n- Column: W12×65 — flange t_f = 0.605 in.\n- Offset of beam from seat centerline: 5½ in.; the two weld lines are at a 3.00-in. and\n  3.50-in. lever arm about the far weld (per the connection geometry).\n- Loads (service): R_D = 5 kips, R_L = 15 kips.\n- Code basis: AISC 360-22 (load combinations from ASCE/SEI 7).\n\n## Find\nThe minimum required bearing length (web local yielding and web local crippling), the\neccentric force on the more heavily loaded weld line, the seat-angle size and fillet-weld\nsize required (designing the seat conservatively for twice the heavier weld force), and\nthe maximum top-angle fillet-weld size permitted by §J2.2b.",
 "has_figure": true,
 "stem": "II_A_16",
 "breadcrumb": "EXAMPLE II.A-16 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Offset Unstiffened Seated Connection (Beam to Column Flange)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-16 · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J2 §J4.2 · Offset Unstiffened Seated Connection (Beam to Column Flange)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (Eq. J10-3), §J10.3 (Eq. J10-5a), §J2 (fillet welds; Table J2.4; AWS return restriction per figure Note A), §J4.2; Manual Part 10 seated-connection model. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 5 kips, L = 15 kips → **LRFD Ru = 30.0 kips; ASD Ra = 20.0 kips**

Beam W14x38 (tw = 0.310 in., tf = 0.515 in., kdes = 0.915 in.) offset 5 1/2 in. from the seat centerline; seat L7x4x5/8 × 6 in. (A572 Gr. 50) welded to the W12x65 column flange with 5/16-in. E70 fillets on its two vertical edges.

### 2. Beam-Web Limit States (bearing length)

- **Web local yielding (Eq. J10-3):** lb,req = 30.0/[50(0.310)] − 2.5(0.915) = 1.94 − 2.29 < 0 → contact bearing suffices ✓
- **Web local crippling (Eq. J10-5a, lb → 0):** Rn = 0.40(0.310)²√(EFywtf/tw) = 59.7 kips → φRn = 44.7 ≥ 30.0 ✓; Rn/Ω = 29.8 ≥ 20.0 ✓

Use the practical minimum lb = 3/4 in. ≤ 3.5 in. provided ✓.

### 3. Eccentric Distribution to the Weld Lines

With the beam offset, the reaction sits 3.00 in. from the near weld and 3.50 in. from the far weld (weld lines 6.50 in. apart). By statics the **near weld carries R(3.50/6.50) = 0.538R**:

- LRFD: heavier weld force = 0.538(30.0) = **16.2 kips**; ASD: **10.8 kips**

Per the conservative Manual practice for offset seats, the seat and welds are designed for **twice the heavier weld force**, i.e., an equivalent concentric reaction R′ = **32.3 kips (LRFD) / 21.5 kips (ASD)**.

### 4. Seat Welds (two 5/16-in. fillets × 7 in. vertical leg)

Elastic line-weld stresses per weld under R′, with the reaction conservatively at the OSL bearing midpoint (e = 2.25 in.):

fv = 32.3/(2 × 7) = 2.31 kip/in.; fh = 3R′e/L² = 3(32.3)(2.25)/49 = 4.45 kip/in. → resultant = **5.01 kip/in.**

Available: 1.392D = 1.392(5) = **6.96 kip/in. ≥ 5.01 ✓** (LRFD); ASD: 3.34 ≤ 4.64 ✓. Minimum weld for the 0.605-in. flange = 1/4 in. ≤ 5/16 ✓. End returns are omitted at the seat heel per AWS (figure Note A).

### 5. Seat Angle

OSL flexure: critical-section eccentricity = setback + lb/2 − (t + 3/8) = 0.50 + 0.38 − 1.00 < 0 → not critical. Vertical-leg shear (Eq. J4-3): 0.6(50)(6)(0.625) = 113 kips ≥ R′ ✓. Two 3/4-in. Group 120-N bolts position the beam; L4x4x1/4 top angle provides stability.

### 6. Conclusion

**Use an L7x4x5/8 × 6 in. seat with 5/16-in. E70 fillet welds.** Accounting for the 5 1/2-in. offset by designing for twice the heavier weld-line force (32.3 kips LRFD / 21.5 kips ASD), the welds work at ~72% utilization and all beam-web and angle limit states are satisfied. The connection complies with AISC 360-22 Chapter J and Manual Part 10 practice for offset seats.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-16 (from figures/IIA_16.png)

Offset unstiffened seated connection welded to a **column flange** (W12×65);
beam W14×38, **offset 5½ in.** from the seat centerline so the two vertical seat
welds are loaded unequally.

- **Seat angle:** L7×4×⅝ × 6 in. long, **4-in. outstanding leg (OSL)**.
- **Beam-to-seat bolts:** ¾-in. Group 120 (N), standard holes.
- **Weld of seat to column flange:** 5/16-in. fillet on the two vertical edges
  (Section A-A); a ⅝-in. weld mark also shown. End return omitted at the column
  flange toe / seat heel (Note A — AWS does not permit the return there).
- The offset puts the reaction eccentric to the weld group; the two weld lines are
  at **3.00-in. and 3.50-in. lever arms** about the far weld (the 3½-in.
  dimensions top and bottom in Section A-A).
- ½-in. nominal beam setback (Note C). Beam and top angle omitted from the section
  for clarity (Note B).
