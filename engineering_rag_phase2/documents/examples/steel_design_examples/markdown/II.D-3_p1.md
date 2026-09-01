<!-- chunk_id: II.D-3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.D-3",
 "example_family": "II.D-3",
 "chapter": "II.D",
 "topic": "connection",
 "clauses": [
  "J3.9",
  "J3.7",
  "J3.11a",
  "D2",
  "D3",
  "J4.1",
  "J4.3",
  "J2.4",
  "J10.2",
  "J3.10"
 ],
 "eqs": [],
 "tables": [],
 "title": "Slip-Critical Double-Angle Tension Connection to a Beam Flange",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.D-3 — Slip-Critical Double-Angle Tension Connection to a Beam Flange",
 "question": "# II.D-3 — Slip-Critical Connection with Oversized Holes  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 2L3×3×5⁄16 double-angle tension member is connected to the bottom flange of a\nW16×26 beam through a ½-in. gusset plate. The plate is welded to the underside of the\nbeam flange with fillet welds on each side and bolted to the angles with a single\nvertical line of ¾-in.-diameter, Group 120 high-strength bolts in double shear. The\nconnection is designed as slip-critical with Class A faying surfaces; the holes are\noversized in the ½-in. plate and standard in the angles. See figures/IID_3.png.\n\nVerify the connection for the applied tension: determine the required number of bolts\nfor slip resistance, then check the connection as a bearing-type connection (bolt\nshear, bearing, and tearout), the tensile yielding and rupture and block shear of both\nthe angles and the plate, the plate-to-beam fillet weld (including base-metal check),\nand web local yielding of the beam. Use 70-ksi electrodes.\n\n## Given\n- Beam: W16×26, ASTM A992/A992M, Fy = 50 ksi, Fu = 65 ksi.\n  tf = 0.345 in., tw = 0.250 in., kdes = 0.747 in.\n- Angles: 2L3×3×5⁄16, ASTM A572/A572M Grade 50, Fy = 50 ksi, Fu = 65 ksi.\n  A = 3.56 in.² (pair), x̄ = 0.860 in. (single angle).\n- Gusset plate: ½ in. × 6 in., ASTM A572/A572M Grade 50, Fy = 50 ksi, Fu = 65 ksi.\n- Bolts: ¾-in.-diameter, Group 120, slip-critical, Class A faying surfaces, threads\n  not excluded (condition N), double shear; standard holes in the angles, oversized\n  holes in the plate. Bolt line: edge distances lev = 1½ in. (vertical) and\n  leh = 1¼ in. (angles) / 3 in. (plate horizontal), spacing s = 3 in.\n- Hole diameters (Table J3.3): standard dh = 13⁄16 in.; oversized dh = 15⁄16 in.\n- Weld: ¼-in. fillet welds, l = 6 in. each side of the plate, FEXX = 70 ksi.\n- Loads (axial tension): PD = 15 kips, PL = 45 kips.\n- Code basis: AISC 360-22 (load combinations per ASCE/SEI 7).\n\n## Find\nThe required number of bolts for slip resistance and verification of every governing\nlimit state (bolt shear/bearing/tearout, angle and plate tensile yield/rupture and\nblock shear, plate-to-beam weld and base metal, beam web local yielding) in both LRFD\nand ASD. State whether the connection is adequate.",
 "has_figure": true,
 "stem": "II_D_3",
 "breadcrumb": "EXAMPLE II.D-3 · AISC 360-22 II.D (connection) · §J3.9 §J3.7 §J3.11a §D2 §D3 §J4.1 §J4.3 §J2.4 · Slip-Critical Double-Angle Tension Connection to a Beam Flange",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.D-3 · AISC 360-22 II.D (connection) · §J3.9 §J3.7 §J3.11a §D2 §D3 §J4.1 §J4.3 §J2.4 · Slip-Critical Double-Angle Tension Connection to a Beam Flange

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.9–J3.10 (slip resistance Rn = μDuhfTbns; φ = 0.85/Ω = 1.76 for oversized holes), §J3.7/§J3.11a (bearing-type back-checks), §D2/§D3, §J4.1–§J4.3, §J2.4, §J10.2. Per the RAG extract provided.

---

### 1. Required Strength

P: D = 15 kips, L = 45 kips → **LRFD Pu = 90.0 kips; ASD Pa = 60.0 kips** (tension)

2L3x3x5/16 (A = 3.56 in.², x̄ = 0.860 in.) bolted in double shear to a PL1/2 × 6 gusset (oversized holes in the plate, standard in the angles); plate welded under the W16x26 flange with 1/4-in. E70 fillets, 6 in. each side.

### 2. Slip Resistance (3/4-in. Group 120, Class A, ns = 2)

rn = μDuhfTbns = 0.30(1.13)(1.0)(28)(2) = 18.98 kips/bolt
Oversized holes → φ = 0.85: φrn = **16.1 kips**; rn/Ω = 18.98/1.76 = **10.8 kips**

Required bolts: 90.0/16.1 = 5.6 and 60.0/10.8 = 5.6 → **use 6 bolts** (single line @ 3 in.).

### 3. Bearing-Type Back-Checks (§J3.10)

Per bolt: double-shear φrn = 35.8 kips ≥ 15.0 ✓; bearing on the 1/2-in. plate φ = 43.9 kips ✓; angle bearing and tearout (lev = 1 1/2 in.) ✓ — slip governs, as intended.

### 4. Member and Plate Limit States

- Angles: yielding φ = 160 kips ✓; rupture (An = 3.01 in.², U = 1 − 0.860/15 = 0.94, Ae = 2.84 in.²) φ = **139 kips ≥ 90 ✓**; block shear ✓
- Plate: yielding φ = 0.9(50)(3.00) = 135 ✓; rupture (oversized hole + 1/16: An = 2.50 in.²) φ = **122 kips ≥ 90 ✓**; block shear ✓

### 5. Weld and Beam Checks

Plate-to-flange welds (transverse to the load, both sides, 6 in. each): φRn = 2(1.392)(4)(6)(1.5) = **100 kips ≥ 90 ✓**; Rn/Ω = 66.8 ≥ 60 ✓ (90% — **governing**).
Base metal: required 7.5 kip/in. per weld ≤ flange shear-rupture capacity 0.75(0.6)(65)(0.345) = 10.1 kip/in. ✓
Web local yielding (Eq. J10-2, lb = 6 in.): φRn = 50(0.250)(5 × 0.747 + 6) = **122 kips ≥ 90 ✓** (ASD 81.1 ≥ 60 ✓)

### 6. Conclusion

**Use six 3/4-in. Group 120 slip-critical bolts (Class A, oversized in the plate) and the PL1/2 × 6 gusset with 1/4-in. transverse fillets.** Slip resistance sets the bolt count (98% utilized); the welds are the next-tightest element at 90%; and all rupture, block-shear, and beam limit states pass. The connection satisfies AISC 360-22 §J3.9/J3.10 slip-critical requirements together with the full bearing-type strength back-checks.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.D-3 (from figures/IID_3.png)

Slip-critical connection with oversized holes: a 2L3×3×5⁄16 double-angle tension
member hung from the **bottom flange of a W16×26** beam through a **½-in. gusset
plate** (P_D = 15 kips, P_L = 45 kips, axial tension).

- **Gusset plate:** ½ in. × 6 in., fillet-welded to the underside of the beam flange
  with **¼-in. fillet welds, l = 6 in. each side** (¼ weld marks shown).
- **Bolts:** single vertical line of **¾-in. Group 120 slip-critical (Class A,
  cond. N)** bolts in **double shear**; the figure shows **5 @ 3 in. = 1'-3"
  (6 bolts)**, l_ev = 1½ in. top and bottom.
- **Holes:** standard (13⁄16 in.) in the angles, **oversized (15⁄16 in.) in the
  ½-in. plate**.
- Horizontal layout at the plate top: 3 in. + 3 in. dimensions; 1¾-in. and 3-in.
  edge dimensions (l_eh = 1¼ in. at the angles, 3 in. at the plate).
- The number of bolts is what the problem solves for (slip resistance); the figure's
  6-bolt line is the configuration shown.
