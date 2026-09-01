<!-- chunk_id: II.A-12A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-12A",
 "example_family": "II.A-12",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J10.2",
  "J10.3",
  "J3.7",
  "J4.2",
  "J3.11"
 ],
 "eqs": [
  "J10-3",
  "J10-5a"
 ],
 "tables": [
  "J3.2",
  "10"
 ],
 "title": "All-Bolted Unstiffened Seated Connection (Beam to Column Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-12A — All-Bolted Unstiffened Seated Connection (Beam to Column Web)",
 "question": "# II.A-12A — All-Bolted Unstiffened Seated Connection (Beam-to-Column Web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W16×50 beam frames into the **web** of an ASTM A992/A992M W14×90\ncolumn and is supported on an unstiffened bolted seat (a single angle bolted to the\ncolumn web with its horizontal outstanding leg under the beam bottom flange). A top\n(\"stability\") angle holds the beam in position but is not counted on for vertical\nstrength. The seat and top angles are ASTM A572/A572M Grade 50. All bolts are\n¾-in.-diameter Group 120 (e.g., A325) in standard holes, thread condition N (threads\nnot excluded from the shear plane). The connection geometry is shown in\nfigures/IIA_12A.png.\n\nThe beam delivers a service dead-load reaction R_D = 9 kips and a service live-load\nreaction R_L = 27.5 kips to the seat.\n\nVerify that an 8-in.-long L6×4×⅝ seat angle (4-in. outstanding leg, 5½-in. bolt gage,\nfour ¾-in. bolts to the column web — \"Connection Type B\") is adequate, and confirm that\nthe supplied bearing length satisfies the beam-web limit states.\n\n## Given\n- Material: beam and column ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); seat and\n  top angles ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n- Beam: W16×50 — d = 16.3 in., t_w = 0.380 in., b_f = 7.07 in., t_f = 0.630 in.,\n  k_des = 1.03 in.\n- Column: W14×90 — web t_w = 0.440 in.\n- Seat angle: 8-in.-long L6×4×⅝, 4-in. outstanding (horizontal) leg, 5½-in. gage,\n  four ¾-in.-dia. Group 120 (N) bolts in standard holes (d_h = 13/16 in.);\n  A_b = 0.442 in.² Top angle L4×4×¼ with two ¾-in. bolts per leg.\n- Loads (service): R_D = 9 kips, R_L = 27.5 kips.\n- Code basis: AISC 360-22 (load combinations from ASCE/SEI 7).\n\n## Find\nThe required bearing length for the beam web (limit states of web local yielding and\nweb local crippling), and the available strength of the seat — bolt shear of the\ncolumn-web bolts (J3.7) plus the outstanding-leg shear/flexural-yielding capacity —\nconfirming each exceeds the required reaction.",
 "has_figure": true,
 "stem": "II_A_12A",
 "breadcrumb": "EXAMPLE II.A-12A · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J3.7 §J4.2 §J3.11 · All-Bolted Unstiffened Seated Connection (Beam to Column Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-12A · AISC 360-22 II.A (simple / shear connection) · §J10.2 §J10.3 §J3.7 §J4.2 §J3.11 · All-Bolted Unstiffened Seated Connection (Beam to Column Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (web local yielding, Eq. J10-3 — end reaction), §J10.3 (web local crippling, Eq. J10-5a), §J3.7/Table J3.2 (bolt shear), §J4.2 (angle leg shear); seated-connection model per AISC Manual Part 10 (Table 10-6 basis). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 9 kips, L = 27.5 kips → **LRFD Ru = 1.2(9) + 1.6(27.5) = 54.8 kips; ASD Ra = 36.5 kips**

Seat: L6x4x5/8 × 8 in. (A572 Gr. 50), 4-in. OSL, gage 5 1/2 in., four 3/4-in. Group 120-N bolts to the W14x90 column web (tw = 0.440 in.). Beam W16x50: tw = 0.380 in., tf = 0.630 in., kdes = 1.03 in., d = 16.3 in.; 1/2-in. setback.

### 2. Required Bearing Length — Beam Web Limit States

**Web local yielding (Eq. J10-3, end reaction; φ = 1.00, Ω = 1.50):**
Rn = Fywtw(2.5kdes + lb) → lb,req = Ru/(Fywtw) − 2.5kdes = 54.8/[50(0.380)] − 2.58 = **0.31 in.** (ASD identical: 1.50(36.5)/19.0 − 2.58 = 0.31 in.)

**Web local crippling (Eq. J10-5a, lb/d ≤ 0.2; φ = 0.75, Ω = 2.00):**
At even lb → 0: Rn = 0.40tw²√(EFywtf/tw) = 0.40(0.380)²(1,550) = 89.6 kips → φRn = 67.2 ≥ 54.8 ✓; Rn/Ω = 44.8 ≥ 36.5 ✓ — **not governing**.

Provided bearing ≈ 4.0 − 0.5 = 3.5 in. ≥ lb,req = 0.31 in. ✓ → **the supplied seat satisfies the beam-web limit states.**

### 3. Seat Angle — Outstanding Leg

Reaction position (Manual seated-connection model): from the column face, e = setback + lb,req/2 − (t + 3/8) = 0.50 + 0.16 − 1.00 < 0 → the reaction resultant falls **inside** the critical section at the toe of the angle fillet; flexural yielding of the OSL does not control.

Leg shear (Eq. J4-3, φ = 1.00/Ω = 1.50): Rn = 0.6Fy(L·t) = 0.6(50)(8)(0.625) = 150 kips → **150 / 100 kips ≥ 54.8 / 36.5 ✓**

### 4. Bolts to the Column Web (Type B, 4 bolts)

Bolt shear (Fnv = 54 ksi, Ab = 0.442 in.²): φRn = 4(0.75)(54)(0.442) = **71.6 kips ≥ 54.8 ✓**; Rn/Ω = 4(11.9) = **47.7 kips ≥ 36.5 ✓**
Bearing (§J3.11): on 5/8-in. angle, 2.4dtFu = 73.1 kips/bolt (φ = 54.8) and on 0.440-in. column web 51.5 kips/bolt (φ = 38.6) — both exceed bolt shear per fastener; **bolt shear controls the group.**

### 5. Stability (Top) Angle

L4x4x1/4 with two 3/4-in. Group 120-N bolts per leg is provided solely for lateral stability of the beam end, per standard seated-connection practice; it carries no calculated vertical load.

### 6. Conclusion

**The 8-in. L6x4x5/8 seat (Type B, four 3/4-in. Group 120-N bolts at 5 1/2-in. gage) is adequate**: the beam web requires only a 0.31-in. bearing length (web local yielding; crippling not governing), well within the 4-in. outstanding leg; the angle leg is not flexure-critical because the reaction falls inside the fillet critical section; and the governing transfer — bolt shear at 71.6 kips (LRFD) / 47.7 kips (ASD) — exceeds the 54.8 / 36.5 kip reactions. A top stability angle completes the detail per Manual practice.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-12A (from figures/IIA_12A.png)

All-bolted unstiffened seated connection to a **column web** (W14×90); beam W16×50
sits on the seat.

- **Seat angle:** L6×4×⅝ × 0'-8" (8 in. long), **4-in. outstanding (horizontal)
  leg (OSL)**; ¾-in. Group 120 (N) bolts in standard holes.
- **Bolts to the column web ("Type B" = 2 rows of bolts):** **4 bolts total**, on a
  **gage = 5½ in.** (overall seat width 8 in.); vertical spacing shown as 2 in. then
  3 in. The horizontal dimension from the column face to the bolt line is 2½ in.
- **Top ("stability") angle:** L4×4×¼ loose angle, (2) ¾-in. Group 120 (N) bolts in
  each leg; ⅛-in. to ¼-in. erection clearance; not counted for vertical strength.
- ½-in. nominal beam setback. Section/Type-B detail at right shows the 8-in.-wide
  seat with the two bolt rows on the 5½-in. gage.
