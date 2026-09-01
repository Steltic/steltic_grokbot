<!-- chunk_id: II.B-1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.B-1",
 "example_family": "II.B-1",
 "chapter": "II.B",
 "topic": "FR moment connection",
 "clauses": [
  "F13.1",
  "J3.7",
  "J3.8",
  "J3.11a",
  "J4.1",
  "J4.3",
  "J2.4",
  "J10.1",
  "J10.2",
  "J10.3"
 ],
 "eqs": [
  "J10-1",
  "J10-2",
  "J10-4"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Bolted Flange-Plated FR Moment Connection",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.B-1 — Bolted Flange-Plated FR Moment Connection",
 "question": "# II.B-1 — Bolted flange-plated fully restrained (FR) moment connection (beam-to-column flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA wide-flange beam frames into the flange of a wide-flange column and is connected\nwith a bolted flange-plated fully restrained (FR) moment connection. The strong-axis\nmoment is carried by a pair of bolted flange plates (one at the top flange, one at the\nbottom flange of the beam) that are bolted to the beam flanges and fillet-welded to\nthe column flange; the vertical shear is carried by a single web plate that is bolted\nto the beam web and fillet-welded to the column flange.\n\nVerify that the connection shown below is adequate for the given beam end reactions,\nand check whether the column requires transverse stiffening (continuity plates) for\nthe concentrated flange forces.\n\nConfiguration (see figures/IIB_1.png):\n- Beam: ASTM A992 W18×50 (Fy = 50 ksi, Fu = 65 ksi); d = 18.0 in., bf = 7.50 in.,\n  tf = 0.570 in., tw = 0.355 in., Sx = 88.9 in.³\n- Column: ASTM A992 W14×99 (Fy = 50 ksi, Fu = 65 ksi); d = 14.2 in., bf = 14.6 in.,\n  tf = 0.780 in.\n- Web plate: PL⅜ in. × 5 in. × 0 ft 9 in., ASTM A572 Grade 50 (Fy = 50, Fu = 65),\n  three ⅞-in.-diameter Group 120 bolts (thread condition N) in standard holes at\n  3 in. vertical spacing, vertical edge distance lev = 1½ in., horizontal edge\n  distance leh = 2 in.; fillet-welded to the column flange with ¼-in. welds.\n- Flange plates: PL¾ in. × 7 in. × 1 ft 0½ in. (one at each flange), ASTM A572\n  Grade 50. Each plate is attached to the beam flange with eight ⅞-in.-diameter\n  Group 120 bolts (thread condition N) in standard holes, arranged in two rows of\n  four bolts on a 4-in. gage, at 3 in. spacing along the length, with end (edge)\n  distance lev = 1½ in. and side edge distance leh = 1½ in.; each plate is\n  fillet-welded to the column flange (weld size to be verified).\n- Electrodes: 70-ksi (FEXX = 70 ksi).\n- Hole diameter for a ⅞-in. bolt in a standard hole: dh = 15/16 in.\n\n## Given\n- Material: beam and column ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); all plates ASTM\n  A572 Gr. 50 (Fy = 50 ksi, Fu = 65 ksi).\n- Geometry: as listed above and shown in figures/IIB_1.png.\n- Loads (service): vertical shear VD = 7 kips, VL = 21 kips; strong-axis moment\n  MD = 42 kip-ft, ML = 126 kip-ft.\n- Code basis: AISC 360-22 (Specification); ASCE/SEI 7 for load combinations.\n\n## Find\nVerify each governing limit state of the connection — beam flange flexural rupture\nat the bolt holes; the bolted web (single-plate) connection (bolt shear / bearing /\ntearout, plate shear yielding and rupture, plate block shear, weld to the column,\ncolumn-flange rupture); the bolted flange-plate connection (bolt shear / bearing /\ntearout, flange-plate tensile yielding and rupture, flange-plate and beam-flange\nblock shear, fillet weld to the column flange, and compression-plate strength) — and\ndetermine whether the column needs transverse stiffeners for flange local bending,\nweb local yielding, and web local crippling. Report whether the connection is\nadequate (LRFD and ASD).",
 "has_figure": true,
 "stem": "II_B_1",
 "breadcrumb": "EXAMPLE II.B-1 · AISC 360-22 II.B (FR moment connection) · §F13.1 §J3.7 §J3.8 §J3.11a §J4.1 §J4.3 §J2.4 §J10.1 · Bolted Flange-Plated FR Moment Connection",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.B-1 · AISC 360-22 II.B (FR moment connection) · §F13.1 §J3.7 §J3.8 §J3.11a §J4.1 §J4.3 §J2.4 §J10.1 · Bolted Flange-Plated FR Moment Connection

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §F13.1 (flange rupture at holes), §J3.7/§J3.8/Table J3.2, §J3.11a, §J4.1–§J4.3, §J2.4, §J10.1 (Eq. J10-1), §J10.2 (Eq. J10-2), §J10.3 (Eq. J10-4). Per the RAG extract provided.

---

### 1. Required Strengths

V: D = 7, L = 21 kips → **Vu = 42.0 / Va = 28.0 kips**. M: D = 42, L = 126 kip-ft → **Mu = 252 kip-ft (3,024 kip-in.) / Ma = 168 kip-ft (2,016 kip-in.)**

Flange force (arm = d + tp = 18.75 in.): **Puf = 3,024/18.75 = 161 kips; Paf = 108 kips**

### 2. Beam Flange Flexural Rupture at the Bolt Holes — §F13.1

Afg = 4.28 in.²; Afn = 4.28 − 2(1.0)(0.570) = 3.14 in.²; Fy/Fu = 0.77 < 0.8 → Yt = 1.0.
FuAfn = 204 < YtFyAfg = 214 → reduced Mn = (FuAfn/Afg)Sx = 47.7(88.9) = 4,240 kip-in.
**φMn = 3,810 ≥ 3,024 ✓; Mn/Ω = 2,540 ≥ 2,016 ✓**

### 3. Web (Single-Plate) Shear Connection — PL3/8 × 5 × 9

Bolts (3 — 7/8-in. Gr.120-N): group = φ[22.6 + 2(24.3)] = **71.2 kips ≥ 42 ✓** (ASD 47.4 ≥ 28 ✓; bottom-bolt tearout included). Plate shear yielding 101 kips / rupture φ65.8 / block shear — all ✓. Weld to column (two 1/4-in. fillets × 9 in.): φRn = 100 kips ≥ 42 ✓. Column-flange base metal ample ✓.

### 4. Flange-Plate Connection (PL3/4 × 7 × 12 1/2, 8 bolts per flange)

- Bolt shear: 8(24.3) = **194 kips ≥ 161 ✓** (ASD 130 ≥ 108 ✓); bearing/tearout on plate and beam flange — bolt shear governs ✓
- Plate tensile yielding (Eq. J4-1): φ = 0.9(50)(5.25) = **236 ≥ 161 ✓** (ASD 157 ≥ 108 ✓)
- Plate tensile rupture (Eq. J4-2): Ae = 3.75 in.² → φ = **183 ≥ 161 ✓** (ASD 122 ≥ 108 ✓)
- Plate and beam-flange block shear (Eq. J4-5): ✓ with margin
- Compression plate: short unbraced length → φPn ≈ φFyAg = 236 kips ✓
- Plate-to-column transverse fillets (both faces, ≈14 in. total, θ = 90°): required D = 161/[14(1.392)(1.5)] = 5.5 → **use 3/8-in. fillets** ✓ (ASD identical size)

### 5. Column Concentrated-Force Checks (W14x99)

| Limit state | Available (LRFD/ASD) | Demand | |
|---|---|---|---|
| Flange local bending (Eq. J10-1): 6.25Fytf² | 171 / 114 kips | 161 / 108 | ✓ (94%) |
| Web local yielding (Eq. J10-2): Fytw(5k + lb) | 186 / 124 kips | 161 / 108 | ✓ |
| Web local crippling (Eq. J10-4) | 232 / 155 kips | 161 / 108 | ✓ |

**No transverse stiffeners (continuity plates) are required**, though flange local bending is the tightest check at 94% (LRFD).

### 6. Conclusion

The bolted flange-plated FR connection is **adequate for Mu = 252 kip-ft with Vu = 42 kips (LRFD; ASD likewise)**. Every limit state passes: the closest margins are column flange local bending (94%), flange-plate tensile rupture (88%), and the 8-bolt flange groups (83%). Use 3/8-in. transverse fillets at the flange plates and 1/4-in. at the web plate; no column stiffening is needed.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.B-1 (from figures/IIB_1.png)

Bolted flange-plated fully-restrained (FR) moment connection: W18×50 beam to a
W14×99 column flange. Moment carried by top and bottom flange plates; shear by a
web plate.

- **Flange plates (one each flange):** PL¾ × 7 in. × 1'-0½", ASTM A572 Gr. 50.
  Each bolted to the beam flange with **8 ⅞-in. Group 120 (N)** bolts (standard
  holes) — **two rows of four on a 4-in. gage**, 3 @ 3 in. = 9 in. along the
  length, 2-in. end distance, 1½-in. side edge; each plate fillet-welded to the
  column flange (⅜-in. weld marks shown).
- **Web plate:** PL⅜ × 5 in. × 0'-9", with **3 ⅞-in. Group 120 (N)** bolts,
  2 @ 3 in. = 6 in., 3-in. dimension to first bolt; ¼-in. fillet weld to the
  column flange; l_ev = 1½ in., l_eh = 2 in.
- "Shim top or bottom as required" noted. ½-in. setback; ⅜ weld marks on flange
  plates.
