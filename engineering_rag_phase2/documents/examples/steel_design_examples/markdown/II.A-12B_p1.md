<!-- chunk_id: II.A-12B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-12B",
 "example_family": "II.A-12",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "B3.9",
  "J3.7",
  "J3.11"
 ],
 "eqs": [
  "J3-6b",
  "J3-6d"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Seated Connection: Structural Integrity Check (§B3.9)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-12B — Seated Connection: Structural Integrity Check (§B3.9)",
 "question": "# II.A-12B — All-Bolted Unstiffened Seated Connection — Structural Integrity Check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nThe all-bolted unstiffened seated connection of Example II.A-12A — an ASTM A992/A992M\nW16×50 beam seated on an 8-in.-long L6×4×⅝ ASTM A572/A572M Grade 50 seat angle bolted\nto a column web with ¾-in.-diameter Group 120 (thread condition N) bolts in standard\nholes — must be checked for the **structural-integrity** provisions of AISC 360-22\nSection B3.9 (required where the applicable building code triggers structural-integrity\ndesign). The connection geometry is shown in figures/IIA_12B.png.\n\nThe seat angle has a 4-in. outstanding leg, the bolt gage on the support leg is 5½ in.,\nthe bolt end distances on the angle are 1¼ in., and there are two bolt rows at an 8-in.\nangle length (average pitch p = 4 in.). The required vertical shear from Example\nII.A-12A is V_u = 54.8 kips (LRFD) / V_a = 36.5 kips (ASD).\n\nTreat the connection both as a beam end connection [B3.9(b)] and as the end connection\nof a member bracing a column [B3.9(c)]. Determine the controlling nominal axial tensile\nstrength T_n and confirm it satisfies the required integrity tie force, and find the\nlargest column axial force this connection can brace.\n\n## Given\n- Material: beam ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); seat angle ASTM A572/A572M\n  Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n- Beam: W16×50 — b_f = 7.07 in., t_f = 0.630 in.\n- Seat angle: L6×4×⅝, 8 in. long, 4-in. OSL, 5½-in. gage, 1¼-in. end distances,\n  two ¾-in.-dia. Group 120 (N) bolts on the outstanding leg and two on the support leg;\n  standard holes d_h = 13/16 in. (Table J3.3); A_b = 0.442 in.²\n- Required shear (from II.A-12A): V_u = 54.8 kips, V_a = 36.5 kips.\n- Code basis: AISC 360-22 §B3.9 (integrity checks evaluated independently of other\n  strength requirements; inelastic deformation of the connection permitted).\n\n## Find\nThe required integrity tie force per B3.9(b); the nominal tensile strength T_n as the\nleast of bolt shear, bolt tension, bolt bearing/tearout (with inelastic deformation\npermitted), angle prying, and beam-flange block shear; confirmation that T_n exceeds the\nrequired tie force; and the maximum column axial strength the connection can brace per\nB3.9(c).",
 "has_figure": true,
 "stem": "II_A_12B",
 "breadcrumb": "EXAMPLE II.A-12B · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 · Seated Connection: Structural Integrity Check (§B3.9)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-12B · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J3.11 · Seated Connection: Structural Integrity Check (§B3.9)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §B3.9 (structural integrity — nominal strengths, inelastic deformation of the connection permitted), with §J3.7/Table J3.2 (bolt shear and tension) and §J3.11 (bearing/tearout with deformation NOT a design consideration, Eqs. J3-6b/J3-6d). Per the RAG extract provided.

---

### 1. Required Integrity Tie Force — §B3.9(b)

From Example II.A-12A: Vu = 54.8 kips / Va = 36.5 kips. Required nominal tensile strength:

Tn,min = max[(2/3)Vu, Va] = max[(2/3)(54.8), 36.5] = **36.5 kips**

### 2. Nominal Tensile Strength of the Tie Path (least of the following)

The tie force acts along the beam axis: through the two outstanding-leg (OSL) bolts in shear, the seat angle, and the two support-leg bolts in tension.

**(a) Bolt shear, OSL bolts (§J3.7):** Rn = 2FnvAb = 2(54)(0.442) = **47.7 kips** ← **governs**

**(b) Bolt tension, support-leg bolts (§J3.7):** Rn = 2FntAb = 2(90)(0.442) = **79.6 kips**

**(c) Bearing/tearout on the 5/8-in. angle (deformation not a consideration, per §B3.9):**
Bearing: 3.0dtFu = 3.0(0.75)(0.625)(65) = 91.4 kips/bolt (Eq. J3-6b)
Tearout (1 1/4-in. end distance): lc = 1.25 − (13/16)/2 = 0.844 in. → 1.5lctFu = 51.4 kips/bolt (Eq. J3-6d)
Group: 2(51.4) = **103 kips**

(Angle-leg flexure under the tie force acts in double curvature between the heel and the clamped bolt line; its nominal mechanism strength, ≈2FyZ/b′ ≈ 39 kips with Z = 0.781 in.³, also exceeds the requirement and inelastic deformation is permitted for integrity checks.)

**Controlling nominal tensile strength: Tn = 47.7 kips ≥ 36.5 kips ✓ — §B3.9(b) satisfied** (utilization 0.77).

### 3. Column-Bracing Capacity — §B3.9(c)

The connection may serve as the end connection of a member bracing a column provided Tn ≥ 1% of (2/3)Pu (LRFD) or 1% of Pa (ASD):

- **LRFD:** Pu,max = 47.7/[0.01(2/3)] = **≈7,160 kips**
- **ASD:** Pa,max = 47.7/0.01 = **≈4,770 kips**

### 4. Conclusion

Evaluated independently of the gravity design and with the relaxed deformation criteria of §B3.9, the all-bolted seated connection provides a nominal tie capacity of **47.7 kips, governed by shear of the two outstanding-leg bolts**, comfortably above the 36.5-kip integrity requirement. The connection can also brace columns with required axial strengths up to roughly 7,200 kips (LRFD) — far beyond any column it would realistically support. No modifications are required for structural integrity.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-12B (from figures/IIA_12B.png)

Same all-bolted unstiffened seated connection as II.A-12A (structural-integrity
check): beam W16×50 on a seat bolted to a W14×90 **column web**.

- **Seat angle:** L6×4×⅝ × 0'-8" (8 in. long), 4-in. OSL; ¾-in. Group 120 (N),
  standard holes.
- **Bolts to column web ("Type B", 2 rows):** 4 bolts, **gage = 5½ in.**, overall
  seat width 8 in.; vertical 2 in. then 3 in.; 2½-in. dimension from column face;
  end distances 1¼ in.
- **Top angle:** L4×4×¼ loose angle, (2) ¾-in. bolts each leg; ⅛–¼-in. clearance.
- ½-in. nominal setback.
