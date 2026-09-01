<!-- chunk_id: F.11C_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.11C",
 "example_family": "F.11",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F10",
  "H2"
 ],
 "eqs": [
  "F10-1",
  "F10-2",
  "F10-4",
  "F10-6",
  "H2-1"
 ],
 "tables": [],
 "title": "Single-Angle Beam with Vertical and Horizontal Loading (H2 Interaction)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.11C — Single-Angle Beam with Vertical and Horizontal Loading (H2 Interaction)",
 "question": "# F.11C — Single-angle beam with vertical and horizontal loading (H2 interaction)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nUsing the AISC Specification directly, verify an equal-leg single angle acting as a beam\nunder combined **vertical** (gravity) and **horizontal** (wind) uniformly distributed loads.\nThe angle is simply supported, braced at the end points only, with **no lateral-torsional\nrestraint** along the span and no deflection limit. Because the moment resultant has\ncomponents about both principal axes, the member must be checked with the combined-stress\ninteraction of AISC 360-22 Section H2. Resolve the geometric-axis moments into principal-axis\nmoments, compute the available flexural strengths about each principal axis, and evaluate the\nH2-1 interaction at the three critical cross-section points (heel and the two leg tips).\n\n## Given\n- Material: ASTM A572/A572M Grade 50 (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, L = 6 ft, braced at the ends only, no LTB restraint.\n- Loads (service, uniformly distributed): vertical dead wD = 0.05 kip/ft, vertical live\n  wL = 0.15 kip/ft; horizontal wind w_wind = 0.12 kip/ft.\n- Load combinations: LRFD comb. 4a (ASCE/SEI 7 §2.3.1); ASD comb. 6a (§2.4.1).\n- Trial member: L4×4×1/4 (equal leg). Geometric: A_g = 1.93 in.², S_x = S_y = 1.03 in.³,\n  I_x = I_y = 3.00 in.⁴, I_z = 1.19 in.⁴, r_z = 0.783 in. Principal-axis properties\n  (AISC Shapes Database): S_zB = 0.778 in.³, S_zC = 0.856 in.³, S_wC = 1.76 in.³;\n  for an equal-leg angle the principal axes are at α = 45° and β_w = 0.\n- Code basis: AISC 360-22.\n\n## Find\nThe principal-axis required moments, the available flexural strengths about the w- and z-axes,\nand the H2-1 combined-stress ratios at the three critical points; confirm the member is adequate.",
 "has_figure": false,
 "stem": "F_11C",
 "breadcrumb": "EXAMPLE F.11C · AISC 360-22 Ch.F (beam flexure) · §F10 §H2 · Single-Angle Beam with Vertical and Horizontal Loading (H2 Interaction)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.11C · AISC 360-22 Ch.F (beam flexure) · §F10 §H2 · Single-Angle Beam with Vertical and Horizontal Loading (H2 Interaction)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F10 (Eqs. F10-1, F10-2, F10-4, F10-6; principal-axis design required when the moment resultant has components about both principal axes — §F10 directs to §H2), §H2 (Eq. H2-1). φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Moments

L = Lb = 6 ft, braced at ends only. Vertical: wD = 0.05, wL = 0.15 kip/ft; horizontal wind = 0.12 kip/ft.

- **LRFD (comb. 4a, 1.2D + 1.0W + 1.0L):** vertical wu = 0.21 kip/ft → Mx = 0.945 kip-ft = 11.3 kip-in.; horizontal wu = 0.12 → My = 0.54 kip-ft = 6.48 kip-in.
- **ASD (comb. 6a, D + 0.75L + 0.75(0.6W)):** vertical wa = 0.163 kip/ft → Mx = 8.78 kip-in.; horizontal wa = 0.054 → My = 2.92 kip-in.

**Principal-axis moments (equal-leg angle, α = 45°):** Mw = (Mx + My)/√2; Mz = (Mx − My)/√2 (worst-sense wind direction):

- **LRFD:** Mw = **12.6 kip-in.**; Mz = **3.44 kip-in.**
- **ASD:** Mw = **8.27 kip-in.**; Mz = **4.14 kip-in.**

### 2. Available Flexural Strength, Major Principal Axis (w) — §F10

L4x4x1/4: Ag = 1.93 in.², rz = 0.783 in., t = 0.25 in., βw = 0 (equal legs), Cb = 1.14; SwC = 1.76 in.³ (toes); My,w = 50(1.76) = 88.0 kip-in.

**LTB (Eq. F10-4 with βw = 0):** Mcr = 9EAgrztCb/(8Lb) = 9(29,000)(1.93)(0.783)(0.25)(1.14)/[8(72)] = **195 kip-in.**
My/Mcr = 88.0/195 = 0.451 ≤ 1 → Mn = (1.92 − 1.17√0.451)(88.0) = **99.8 kip-in.** (Eq. F10-2; ≤ 1.5My = 132) ← governs
**LLB (Eq. F10-6, noncompact, b/t = 16):** Mn = 50(1.76)(1.287) = 113 kip-in.

**Mnw = 99.8 kip-in.** → φbMnw = 89.8 kip-in.; Mnw/Ωb = 59.8 kip-in.

### 3. Available Flexural Strength, Minor Principal Axis (z) — §F10

Only yielding and LLB apply (User Note). SzB = 0.778 in.³ (heel), SzC = 0.856 in.³ (toes); My,z = 50(0.778) = 38.9 kip-in.

- Yielding (Eq. F10-1): Mn = 1.5My = 58.4 kip-in.
- LLB, toes in compression (Eq. F10-6): Mn = 50(0.856)(1.287) = **55.1 kip-in.** ← governs for toe-compression sense

**Mnz = 55.1 kip-in.** → φbMnz = 49.6 kip-in.; Mnz/Ωb = 33.0 kip-in. (heel-compression sense: 58.4 → 52.5 / 35.0)

### 4. H2 Interaction at the Critical Points — Eq. H2-1

Because stresses at each point scale with M/S, the stress ratios reduce to moment ratios:

**LRFD:**
- Point C (toe; Mw compression + Mz, worst additive): 12.6/89.8 + 3.44/49.6 = 0.140 + 0.069 = **0.21 ≤ 1.0 ✓**
- Point B (heel; Mw stress ≈ 0, Mz compression): 3.44/52.5 = **0.07 ≤ 1.0 ✓**
- Point A (other toe; Mw tension − Mz): |−0.140 + 0.069| = **0.07 ≤ 1.0 ✓**

**ASD:**
- Point C: 8.27/59.8 + 4.14/33.0 = 0.138 + 0.126 = **0.26 ≤ 1.0 ✓**
- Points A, B: ≤ 0.13 ✓

### 5. Conclusion

The L4x4x1/4 (A572 Gr. 50) under combined gravity and wind loading satisfies the §H2 combined-stress interaction at all three critical points, with a maximum ratio of **0.21 (LRFD) / 0.26 (ASD)** at the toe under additive major- and minor-axis compression. The governing flexural limit states are LTB about the w-axis (Eq. F10-2/F10-4, βw = 0) and leg local buckling about the z-axis (Eq. F10-6). **The member is adequate** with substantial reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
