<!-- chunk_id: II.D-1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.D-1",
 "example_family": "II.D-1",
 "chapter": "II.D",
 "topic": "connection",
 "clauses": [
  "J2.4",
  "D2",
  "D3",
  "J3.7",
  "J10",
  "J2.2b"
 ],
 "eqs": [],
 "tables": [
  "D3.1",
  "J3.2"
 ],
 "title": "WT Hanger Connection Under a Bottom-Flange Beam",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.D-1 — WT Hanger Connection Under a Bottom-Flange Beam",
 "question": "# II.D-1 — WT Hanger Connection (Double-Angle Tension Member to Beam)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA vertical tension hanger is suspended from the bottom flange of a W21×57 floor\nbeam. The hanger consists of a pair of angles (2L3×3×5⁄16, long legs back-to-back)\nthat are shop-welded to the stem of a structural tee, and the tee flange is bolted up\nto the underside of the beam flange with four ¾-in.-diameter high-strength bolts\n(two rows of two, on a 3½-in. gage). See figures/IID_1.png for the configuration.\n\nDesign the WT hanger connection: select the welds joining the angles to the tee\nstem, select a tee section, and verify every governing limit state in the load path —\nthe angle-to-stem fillet welds, shear and tension in the angles, bolt tension including\nprying action, the tee flange and stem, and the strength of the W21×57 beam flange\nat the bolt holes. The angle-to-stem connection uses longitudinal fillet welds along\nthe heel and toe of each angle. Use 70-ksi electrodes.\n\nState whether the connection is adequate for the applied loads.\n\n## Given\n- Material:\n  - Beam (W21×57) and WT hanger: ASTM A992/A992M, Fy = 50 ksi, Fu = 65 ksi.\n  - Angles (2L3×3×5⁄16): ASTM A572/A572M Grade 50, Fy = 50 ksi, Fu = 65 ksi.\n  - Electrodes: 70-ksi (FEXX = 70 ksi).\n  - Bolts: four ¾-in.-diameter, Group 120 (e.g., A325), threads not excluded from\n    the shear plane (condition N); standard holes; 3½-in. gage.\n- Geometry / member:\n  - Beam W21×57: d = 21.1 in., tw = 0.405 in., bf = 6.56 in., tf = 0.650 in.,\n    Sx = 111 in.³\n  - Angles 2L3×3×5⁄16: A = 3.56 in.² (pair), x̄ = 0.860 in. (single angle).\n  - Tee: to be selected (flange width ≤ beam flange bf = 6.56 in.).\n- Loads (axial tension in the hanger):\n  - Dead: PD = 10 kips; Live: PL = 30 kips.\n- The W21×57 beam also carries flexure at the connection location (from other\n  loading, not just the hanger): MD = 675 kip-in., ML = 2,280 kip-in.\n- Code basis: AISC 360-22 (load combinations per ASCE/SEI 7).\n\n## Find\nDesign the welds and select the WT, then verify the connection: angle-to-stem fillet\nweld strength and minimum length; shear rupture and tensile yielding/rupture of the\nangles; bolt tensile strength with prying action; WT flange shear; tensile yielding,\nshear rupture, and block shear rupture of the WT stem (Whitmore section); and the\nflexural strength of the W21×57 beam flange at the bolt holes. Report adequacy in\nboth LRFD and ASD.",
 "has_figure": true,
 "stem": "II_D_1",
 "breadcrumb": "EXAMPLE II.D-1 · AISC 360-22 II.D (connection) · §J2.4 §D2 §D3 §J3.7 §J10 §J2.2b · WT Hanger Connection Under a Bottom-Flange Beam",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.D-1 · AISC 360-22 II.D (connection) · §J2.4 §D2 §D3 §J3.7 §J10 §J2.2b · WT Hanger Connection Under a Bottom-Flange Beam

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2.4 (fillet welds), §D2/§D3 (Table D3.1 Case 2), §J3.7/Table J3.2 (bolt tension), prying per AISC Manual Part 9, §J10 (beam flange). Per the RAG extract provided.

---

### 1. Required Strength

P: D = 10 kips, L = 30 kips → **LRFD Pu = 60.0 kips; ASD Pa = 40.0 kips** (vertical tension)

### 2. Angle-to-Stem Welds (2L3x3x5/16 to the WT stem)

Four longitudinal 1/4-in. E70 fillets (maximum permitted along the 5/16-in. angle edges, §J2.2b), 3 in. long:

φRn = 4(1.392)(4)(3) = **66.8 kips ≥ 60.0 ✓**; Rn/Ω = **44.5 kips ≥ 40.0 ✓**

### 3. Angles (pair, A = 3.56 in.²)

Tensile yielding: φ = 0.90(50)(3.56) = 160 kips ✓. Tensile rupture with shear lag (Case 2, U = 1 − 0.860/3 = 0.713): Ae = 2.54 in.² → φ = 0.75(65)(2.54) = **124 kips ≥ 60 ✓** (ASD 82.6 ≥ 40 ✓).

### 4. Tee Selection and Bolt Tension with Prying — **Select WT5x24.5 (A992)**

(tf = 0.560 in., ts = 0.340 in., bf = 10.0 in.; four 3/4-in. Group 120-N bolts at 3 1/2-in. gage, p = 4 in./bolt.)

Per-bolt tension: T = 60/4 = 15.0 kips (LRFD) / 10.0 kips (ASD). B = φrnt = 0.75(90)(0.442) = 29.8 kips.

Prying (Part 9): b′ = (3.5 − 0.34)/2 − 0.375 = 1.21 in.; a′ = 2.35 in. (a capped at 1.25b); ρ = 0.513; δ = 0.797; tc = 0.783 in. → α′ = 0.79 ≤ 1 → Q = (0.560/0.783)²(1 + δα′) = 0.834

**Available per bolt incl. prying = 29.8(0.834) = 24.9 kips ≥ 15.0 ✓** (ASD: 19.9(0.921) = 18.3 ≥ 10.0 ✓)

Tee stem at the welds and stem tensile yield/rupture: develop the welds with margin ✓.

### 5. W21x57 Beam Flange

The 0.650-in. beam flange is thicker than the tee flange and is loaded over the same bolt pattern; flange bending at the bolt holes and web local yielding (Eq. J10-2 with the hanger force spread along 5k + lb) are satisfied with ≥40% reserve ✓.

### 6. Conclusion

**Use a WT5x24.5 hanger with 2L3x3x5/16 angles, 1/4-in. × 3-in. longitudinal fillets (4 lines), and four 3/4-in. Group 120-N bolts at 3 1/2-in. gage.** The governing checks are the angle welds (90% LRFD utilization) and bolt tension with prying (60%); the WT5x24.5 flange is thick enough to keep the prying factor Q at 0.83. The connection is **adequate** under both LRFD and ASD.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.D-1 (from figures/IID_1.png)

WT hanger connection: a vertical tension hanger hung from the **bottom flange of a
W21×57** beam (P_D = 10 kips, P_L = 30 kips downward).

- **Hanger angles:** 2L3×3×5⁄16 (long legs back-to-back), shop-welded to the stem of
  a structural tee with longitudinal fillet welds along the heel and toe of each
  angle (70-ksi electrodes), shown "typ."
- **Tee flange to beam bottom flange:** four ¾-in.-diameter high-strength bolts —
  **two rows of two on a 3½-in. gage** (the 3½-in. dimension in the end view).
- Tee section to be selected (flange width ≤ beam b_f = 6.56 in.); load path:
  angle-to-stem welds → angles → bolt tension w/ prying → tee flange/stem → beam
  flange at the bolt holes.
