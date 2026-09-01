<!-- chunk_id: II.D-2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.D-2",
 "example_family": "II.D-2",
 "chapter": "II.D",
 "topic": "connection",
 "clauses": [
  "J10.2",
  "J10.3",
  "J8"
 ],
 "eqs": [
  "J10-3",
  "J10-5a"
 ],
 "tables": [],
 "title": "Beam Bearing on a Concrete Wall (Bearing-Plate Design)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.D-2 — Beam Bearing on a Concrete Wall (Bearing-Plate Design)",
 "question": "# II.D-2 — Beam Bearing Plate (W18×50 on a Concrete Wall)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W18×50 floor beam rests on a 10-in.-thick concrete wall and delivers its end\nreaction to the wall through direct bearing (see figures/IID_2.png). Investigate the\nbearing in three parts:\n\nA. With the beam bearing over the full wall thickness (bearing length lb = h = 10 in.),\n   determine whether a steel bearing plate is required, checking web local yielding\n   and web local crippling of the beam web, the bearing strength of the concrete, and\n   the flexural adequacy of the bare beam flange acting as a cantilever.\n\nB. If a bearing plate is used with lb = 10 in. (full wall thickness), size the plate\n   (width B and thickness t).\n\nC. If the bearing length is reduced to lb = 6½ in. with the plate centered on the\n   wall thickness (so the concrete area A₂ is larger than the loaded area A₁), size\n   the plate.\n\n## Given\n- Beam: W18×50, ASTM A992/A992M, Fy = 50 ksi, Fu = 65 ksi.\n  d = 18.0 in., tw = 0.355 in., bf = 7.50 in., tf = 0.570 in., kdes = 0.972 in.,\n  k1 = 13⁄16 in.\n- Bearing plate: ASTM A572/A572M Grade 50, Fy = 50 ksi, Fu = 65 ksi.\n- Concrete wall: f′c = 3 ksi, thickness h = 10 in.\n- End reactions: RD = 15 kips, RL = 45 kips.\n- Code basis: AISC 360-22 (load combinations per ASCE/SEI 7).\n\n## Find\nA. Whether a bearing plate is required at lb = 10 in. (web local yielding, web local\n   crippling, concrete bearing, and required beam-flange thickness).\nB. The bearing plate (B × t) for lb = 10 in.\nC. The bearing plate (B × t) for lb = 6½ in. centered on the wall.\nReport results in both LRFD and ASD.",
 "has_figure": true,
 "stem": "II_D_2",
 "breadcrumb": "EXAMPLE II.D-2 · AISC 360-22 II.D (connection) · §J10.2 §J10.3 §J8 · Beam Bearing on a Concrete Wall (Bearing-Plate Design)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.D-2 · AISC 360-22 II.D (connection) · §J10.2 §J10.3 §J8 · Beam Bearing on a Concrete Wall (Bearing-Plate Design)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (Eq. J10-3), §J10.3 (Eqs. J10-5a/b), §J8 (concrete bearing, Pp = 0.85f′cA1√(A2/A1) ≤ 1.7f′cA1; φc = 0.65, Ωc = 2.31); plate flexure per the Manual Part 14 cantilever model. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 15 kips, L = 45 kips → **LRFD Ru = 90.0 kips; ASD Ra = 60.0 kips**. W18x50: tw = 0.355 in., tf = 0.570 in., bf = 7.50 in., kdes = 0.972 in., k1 = 13/16 in. Wall: f′c = 3 ksi, h = 10 in.

### Part A — Beam Bearing Directly on the Wall (lb = 10 in.)

- **Web local yielding (Eq. J10-3):** Rn = 50(0.355)(2.5 × 0.972 + 10) = 221 kips → 221/147 ≥ 90/60 ✓
- **Web local crippling (Eq. J10-5b, lb/d = 0.56):** Rn = 153 kips → φ = 115/76.7 ✓
- **Concrete bearing (§J8, A2 = A1):** Pp = 0.85(3)(7.50 × 10) = 191 kips → φcPp = 124/82.8 ✓
- **Beam flange as a cantilever (n = bf/2 − k1 = 2.94 in.):** bearing pressure fp = 90/75 = 1.20 ksi → Mu = fpn²/2 = 5.18 kip-in./in. → required t = √(4Mu/0.9Fy) = **0.68 in. > tf = 0.570 in. ✗**

**The flange is overstressed in bending — a bearing plate IS required** (all other limit states pass).

### Part B — Bearing Plate with lb = 10 in.

Concrete: A1,req = 90/[0.65(0.85)(3)] = 54.3 in.² → with lb = 10, B ≥ 5.4 in.; **use B = 8 in.** (≥ bf).
fp = 90/(8 × 10) = 1.13 ksi; plate cantilever n = B/2 − k1 = 3.19 in. → Mu = 5.72 kip-in./in.
t ≥ √(4Mu/0.9Fy) = 0.71 in. (ASD identical: 0.71 in.) → **use PL3/4 × 8 × 0′-10 (A572 Gr. 50).**

### Part C — Bearing Plate with lb = 6 1/2 in., Centered on the Wall

Confinement credit: √(A2/A1) = 10/6.5 = 1.54 (geometrically similar) → φcPp = 0.65(0.85)(3)(1.54)A1 → A1,req = 35.3 in.² → B ≥ 5.4 in.; **use B = 8 in.**
fp = 90/(8 × 6.5) = 1.73 ksi → Mu = 1.73(3.19)²/2 = 8.79 kip-in./in. → t ≥ √(4 × 8.79/45) = 0.88 in. → **use PL1 × 8 × 0′-6 1/2.**
Re-check web crippling at lb = 6.5 in. (Eq. J10-5b): φRn = 92.9 ≥ 90 ✓ (ASD 62.0 ≥ 60 ✓ — at 97%, the governing beam check for Part C).

### Conclusion

Bearing directly on the wall fails only the **flange-bending** check, so a plate is required: **PL3/4 × 8 × 10 for full-thickness bearing (Part B)**, or **PL1 × 8 × 6 1/2 when the bearing is shortened and centered (Part C)** — the confinement factor √(A2/A1) offsets the smaller contact area, but the thicker plate is needed for the higher pressure, and web crippling of the W18x50 becomes the near-governing member check at the 6 1/2-in. bearing.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.D-2 (from figures/IID_2.png)

Beam bearing: a **W18×50** rests on a **10-in.-thick concrete wall** (h = 10 in.)
and delivers its end reaction through a bearing plate.

- **End view (across the wall thickness):** plate width **B**, made up of
  **n + k + k + n** (the central 2k is under the web; each n is the cantilever
  overhang of the plate/flange beyond k). Plate thickness **t**. The "k" dimension
  is the beam's flange-to-web fillet distance.
- **Side view (along the beam):** bearing length **l_b** (= h = 10 in. in Parts A/B;
  6½ in. in Part C). Web local-yielding/crippling dispersion length shown as
  **l_b + 2.5k**.
- Bearing-plate flexure treated as a cantilever of length n from the critical
  section; concrete bearing uses loaded area A₁ = B·l_b on wall area A₂.
