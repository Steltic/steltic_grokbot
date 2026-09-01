<!-- chunk_id: II.A-11C_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-11C",
 "example_family": "II.A-11",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "B3.9",
  "J3.7",
  "J2.4",
  "J4.1"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Shear End-Plate Connection: Structural Integrity Check (§B3.9)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-11C — Shear End-Plate Connection: Structural Integrity Check (§B3.9)",
 "question": "# II.A-11C — Shear End-Plate Connection, Structural Integrity Check  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA shear end-plate connection joins an ASTM A992/A992M W18×50 beam (t_w = 0.355 in.) to\na support, and the beam also braces a column. The connection must be checked for the\nstructural-integrity provisions of AISC 360-22 Section B3.9 (these checks apply only\nwhen structural integrity is required by the applicable building code). The end plate\nis ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi), 8½ in. wide × 14½ in. long ×\n½ in. thick, with a bolt gage g = 5½ in. It carries five rows of ⅞-in.-diameter Group\n120 bolts (two per row, ten total) in standard holes (d_h = 15/16 in.) at a 3-in.\nvertical pitch, with 1¼-in. end distances. The plate is welded to the beam web with a\npair of 3/16-in. fillet welds (one each side, E70, D = 3). A_b = 0.601 in² for a ⅞-in.\nbolt; F_nt = 90 ksi for Group 120. The configuration is shown in figures/IIA_11C.png.\n\nFrom the parent connection design (a shear end-plate carrying combined shear and axial\nload), the required vertical shear strength is V_u = 75 kips (LRFD) and V_a = 50 kips\n(ASD).\n\n## Given\n- Material: beam ASTM A992/A992M (F_y = 50, F_u = 65); end plate ASTM A572/A572M Grade 50\n  (F_y = 50, F_u = 65); E70 electrodes (F_EXX = 70).\n- Beam: W18×50, t_w = 0.355 in.\n- End plate: 8½ in. wide × 14½ in. long × ½ in. thick; gage = 5½ in.\n- Fasteners: ⅞-in.-dia. Group 120 (F_nt = 90 ksi, A_b = 0.601 in², d_h = 15/16 in.);\n  5 rows × 2 = 10 bolts at s = 3 in.; end distances 1¼ in.\n- Welds: 3/16-in. fillet (D = 3), E70, one each side of the beam web.\n- Required vertical shear (from parent connection): V_u = 75 kips, V_a = 50 kips.\n- Code basis: AISC 360-22 (Section B3.9 structural integrity).\n\n## Find\n(1) The minimum nominal axial tensile strength required of the end connection per\nB3.9(b). (2) The available nominal tensile strength of the connection, taken as the\nleast of: bolt tension (J3.7), end-plate bending with prying action, weld tension\n(J2.4), and beam-web tension rupture at the weld (J4.1); and whether it satisfies B3.9(b).\n(3) Per B3.9(c), the maximum column axial force this connection can brace.",
 "has_figure": true,
 "stem": "II_A_11C",
 "breadcrumb": "EXAMPLE II.A-11C · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J2.4 §J4.1 · Shear End-Plate Connection: Structural Integrity Check (§B3.9)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-11C · AISC 360-22 II.A (simple / shear connection) · §B3.9 §J3.7 §J2.4 §J4.1 · Shear End-Plate Connection: Structural Integrity Check (§B3.9)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §B3.9 (structural integrity — nominal strengths, no resistance/safety factors), with nominal tensile strengths from §J3.7/Table J3.2 (bolts), AISC Manual Part 9 (plate bending with prying), §J2.4 (welds, transverse), §J4.1 (web). Per the RAG extract provided.

---

### 1. Minimum Required Nominal Tensile Strength — §B3.9(b)

From the parent design, Vu = 75 kips (LRFD) / Va = 50 kips (ASD). §B3.9(b) requires a nominal tensile strength not less than two-thirds of the required LRFD shear, or the full ASD shear:

Tn,min = max[(2/3)(75), 50] = **50 kips**

### 2. Available Nominal Tensile Strength (least of four limit states; nominal values)

**(a) Bolt tension (§J3.7):** Rn = nFntAb = 10(90)(0.601) = **541 kips**

**(b) End-plate bending with prying (Manual Part 9, nominal basis):**
b′ = (5.5 − 0.355)/2 − 0.875/2 = 2.14 in.; p = 3 in.; δ = 1 − (15/16)/3 = 0.688; per-bolt nominal B = 54.1 kips
tc = √(4.44Bb′/(pFu)) = √(4.44 × 54.1 × 2.14/(3 × 65)) = 1.62 in.
Q = (t/tc)²(1 + δ) = (0.50/1.62)²(1.688) = 0.160
Tn = nBQ = 10(54.1)(0.160) = **86.8 kips** ← **governs**

**(c) Weld tension (§J2.4, transverse, directional factor 1.5):**
Rn = 1.5(0.6 × 70)(2 × 0.707 × 0.1875 × 14.5) = 63(3.84) = **242 kips**

**(d) Beam-web tension at the weld (§J4.1(b), no holes):**
Rn = Fu(l·tw) = 65(14.5 × 0.355) = **335 kips**

**Available Tn = 86.8 kips ≥ 50 kips ✓ — §B3.9(b) is satisfied** (utilization 0.58), governed by plate bending with prying.

### 3. Column-Bracing Capacity — §B3.9(c)

§B3.9(c) requires end connections of members that brace columns to have a nominal tensile strength ≥ 1% of two-thirds of the required column axial strength (LRFD) or 1% of the required column axial strength (ASD). Inverting with Tn = 86.8 kips:

- **LRFD:** Pu,max = Tn/[0.01(2/3)] = 86.8(150) = **≈13,000 kips**
- **ASD:** Pa,max = Tn/0.01 = **≈8,680 kips**

Any practical column braced by this beam falls far below these limits.

### 4. Conclusion

The shear end-plate connection satisfies the §B3.9 structural-integrity provisions: its nominal tensile capacity of **86.8 kips** (limited by end-plate flexure with prying action) exceeds the 50-kip minimum of §B3.9(b), and per §B3.9(c) it can serve as a bracing connection for columns with required axial strengths up to roughly 13,000 kips (LRFD) / 8,700 kips (ASD). No modification to the parent connection design is needed for integrity.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-11C (from figures/IIA_11C.png)

Same shear end-plate as II.A-11B (structural-integrity check): **PL½ × 8½ in. ×
1'-2½" (14½ in.)** on a W18×50 web.

- **Bolts:** ⅞-in. Group 120 (N), standard holes; two vertical lines, **5 rows**,
  l_ev = 1¼ in., 4 @ 3 in. = 1'-0" (12 in.); **gage = 5½ in.**; 3 in. to first row.
- **Welds:** 3/16-in. fillet each side of the beam web.
- ½-in. dimension at plate edge. Loads: shear **V** with axial **N**.
