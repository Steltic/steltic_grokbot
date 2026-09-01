<!-- chunk_id: II.A-22_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-22",
 "example_family": "II.A-22",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Bolted Triangular Bracket Plate",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-22 — Bolted Triangular Bracket Plate",
 "question": "# II.A-22 — Bolted bracket plate design  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA triangular bracket plate is bolted to the flange of a column and supports a\nvertical service load applied at the outer tip of the bracket. Determine whether\nthe single bracket plate shown in figures/IIA_22.png is adequate. The plate is\nASTM A572/A572M Grade 50 (Fy = 50 ksi, Fu = 65 ksi) and is ⅜ in. thick. The\ncolumn is assumed to have sufficient strength for the connection.\n\nGeometry (per the figure): the plate is bolted to the column through a single\nvertical line of six ¾-in.-diameter Group 120 bolts (thread condition N, standard\nholes) spaced 3 in. on center (5 spaces = 15 in.), with 2½-in. end distances and a\n5½-in. gage. The horizontal leg of the bracket measures a = 20 in. and the\nsloped (free) edge drops b = 15¼ in., giving a triangular plate. The applied load\nacts vertically at a horizontal distance e = 9¼ in. from Section A-A (the vertical\nsection through the bolt line at the column face). Section B-B is the critical\nsection taken along the sloped free edge of the triangle.\n\n## Given\n- Material: bracket plate ASTM A572/A572M Grade 50, Fy = 50 ksi, Fu = 65 ksi.\n- Plate: ⅜-in. thick triangular bracket; a = 20 in. (vertical edge at column),\n  b = 15¼ in. (drop of sloped edge), load eccentricity e = 9¼ in.\n- Fasteners: six ¾-in.-dia. Group 120 bolts, thread condition N, standard holes\n  (dh = ¹³⁄₁₆ in.), one vertical row, s = 3 in., 5½-in. gage, 2½-in. end distance.\n- Loads (service, per bracket plate): dead PD = 6 kips, live PL = 18 kips.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7); bracket-plate\n  procedure per AISC Manual Part 15.\n\n## Find\nVerify the bracket plate is adequate: check the bolt group (shear / bearing /\ntearout with eccentricity), flexural yielding and flexural rupture of the plate on\nSection A-A, shear strength of the plate on Section A-A, and the\nshear / normal-force / flexure interaction on the sloped Section B-B.",
 "has_figure": true,
 "stem": "II_A_22",
 "breadcrumb": "EXAMPLE II.A-22 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 · Bolted Triangular Bracket Plate",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-22 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 · Bolted Triangular Bracket Plate

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2; bracket-plate procedure per AISC Manual Part 15 (free-edge buckling parameter λ and Fcr). Per the RAG extract provided.

---

### 1. Required Strength

P: D = 6 kips, L = 18 kips → **LRFD Pu = 36.0 kips; ASD Pa = 24.0 kips**, vertical at e = 9 1/4 in. from Section A-A (bolt line).

PL3/8 triangular bracket (A572 Gr. 50): a = 20 in. vertical edge, b = 15 1/4 in. drop; six 3/4-in. Group 120-N bolts @ 3 in. (one line, 2 1/2-in. end distances).

### 2. Eccentric Bolt Group (§J3.7)

Six bolts @ 3 in., ex = 9.25 in. → instantaneous-center coefficient C ≈ 2.8:

φRn = 2.8(17.9) = **50.1 kips ≥ 36.0 ✓**; Rn/Ω = 2.8(11.9) = **33.3 kips ≥ 24.0 ✓** (utilization 0.72 — **governing**)

Bearing/tearout on the 3/8-in. plate (2 1/2-in. end distance): φ ≥ 22 kips/bolt — not governing relative to per-bolt demand (≈12.9 kips).

### 3. Section A-A (vertical section at the bolt line)

V = 36.0 kips; M = 36.0(9.25) = 333 kip-in. Plate d = 20 in., t = 3/8 in.:

- Flexural yielding: φMn = 0.9(50)(0.375 × 20²/4) = 1,690 kip-in. ≥ 333 ✓ (net-section flexural rupture with six 7/8-in. holes likewise non-critical)
- Shear yielding (Eq. J4-3): 0.6(50)(7.50) = 225 kips ≥ 36 ✓; shear rupture (Eq. J4-4): φRn = 162 kips ✓

### 4. Section B-B (sloped free edge) — Manual Part 15

Buckling parameter: λ = (b/t)√Fy / [5√(475 + 1,120(b/a)²)] = 40.7(7.07)/[5√(475 + 651)] = **1.71 > 1.41**
→ Fcr = 1.30Fy/λ² = 1.30(50)/2.94 = **22.1 ksi**; φFcr = 19.9 ksi (LRFD), Fcr/Ω = 13.2 ksi (ASD)

Maximum combined (direct + flexural) compressive stress on the 25.2-in. inclined section, resolving the tip load onto B-B:
f ≈ 3.8 (direct) + 6.9 (flexural) = **≈10.8 ksi ≤ 19.9 ksi ✓** (ASD: ≈7.2 ≤ 13.2 ✓)

### 5. Conclusion

The 3/8-in. triangular bracket plate is **adequate**: the eccentrically loaded six-bolt group governs at ~72% utilization, the bolt-line section carries the 333 kip-in. moment with order-of-magnitude margin, and the slender sloped free edge (λ = 1.71, elastic-buckling regime) still works at about half its available stress. The column-side strength is adequate per the problem statement.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-22 (from figures/IIA_22.png)

Bolted triangular bracket plate (⅜ in. thick, ASTM A572 Gr. 50) bolted to a column
flange; vertical service load at the bracket tip (P_D = 6 kips, P_L = 18 kips).

- **Bolts:** single vertical line of **six ¾-in. Group 120 (N)** bolts, standard
  holes, **5 @ 3 in. = 15 in.**, with **2½-in. end distances** top and bottom;
  5½-in. gage and 2¼-in. dimension shown at the column face; plate top width 1'-0"
  with 2¾-in. offset.
- **Bracket geometry:** vertical edge at the column **a = 20 in.** (= 1'-8"); the
  sloped free edge drops **b = 15¼ in.**; load eccentricity **e = 9¼ in.** from
  Section A-A (the vertical section through the bolt line / column face).
- **Section A-A** = critical vertical section at the column; **Section B-B** =
  critical section along the sloped free edge (resists Vᵣ, Nᵣ, Mᵣ at angle θ).
