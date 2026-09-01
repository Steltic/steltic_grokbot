<!-- chunk_id: H.5C_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.5C",
 "example_family": "H.5",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "H3.2",
  "H3.1",
  "G4",
  "F7"
 ],
 "eqs": [
  "H3-6"
 ],
 "tables": [],
 "title": "HSS6x4x1/4 Under Combined Torsion, Shear, and Flexure",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.5C — HSS6x4x1/4 Under Combined Torsion, Shear, and Flexure",
 "question": "# H.5C - Rectangular HSS combined torsion, shear, and flexure (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A500/A500M Grade C HSS6x4x1/4 beam spans 8 ft, is simply supported and torsionally fixed at the\nends, and bends about its strong axis. A uniformly distributed load is applied at a 6-in. eccentricity from\nthe shear center, producing both transverse load and a distributed torque. Service loads are wD = 0.46 kip/ft\n(dead) and wL = 1.38 kip/ft (live), each at e = 6 in. Verify the member for combined torsion, shear, and flexure\nusing AISC 360-22 Section H3.2 (Eq. H3-6). The available torsional strength of this HSS is Tc = 273 kip-in (LRFD)\nand 181 kip-in (ASD) (rectangular-HSS torsion per Section H3.1, Fcr = 0.6Fy = 30 ksi, C = 10.1 in^3).\n\n## Given\n- Material: ASTM A500/A500M Grade C, Fy = 50 ksi.\n- Member: HSS6x4x1/4; t = 0.233 in.; Ag = 4.30 in^2; b/t = 14.2; h/t = 22.8; ry = 1.61 in; Zx = 8.53 in^3; J = 23.6 in^4.\n- Geometry: span L = 8 ft, simply supported, torsionally fixed ends; Lb = 8 ft; load eccentricity e = 6 in.\n- Loads (ASCE/SEI 7): wD = 0.46 kip/ft, wL = 1.38 kip/ft.\n- Available torsional strength (from rectangular-HSS torsion, Section H3.1): Tc = 273 (LRFD) / 181 (ASD) kip-in.\n- Code basis: AISC 360-22.\n\n## Find\nThe required shear and torsion, the available shear (G4) and flexural (F7) strengths, and the Eq. H3-6\ninteraction at the critical locations (LRFD and ASD).",
 "has_figure": false,
 "stem": "H_5C",
 "breadcrumb": "EXAMPLE H.5C · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.2 §H3.1 §G4 §F7 · HSS6x4x1/4 Under Combined Torsion, Shear, and Flexure",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.5C · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.2 §H3.1 §G4 §F7 · HSS6x4x1/4 Under Combined Torsion, Shear, and Flexure

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §H3.2 (Eq. H3-6) with available strengths from §H3.1 (torsion, per Example H.5A), §G4 (shear), §F7 (flexure). Per the RAG extract provided.

---

### 1. Required Strengths

Span L = 8 ft, simply supported, torsionally fixed ends; uniform load at e = 6 in. from the shear center.

- **LRFD:** wu = 1.2(0.46) + 1.6(1.38) = 2.76 kip/ft
  Vu = 2.76(8)/2 = **11.0 kips**; Mu = 2.76(8)²/8 = **22.1 kip-ft**; distributed torque = 2.76(6/12) = 1.38 kip-ft/ft → end torsion Tu = 1.38(8)/2 = 5.52 kip-ft = **66.2 kip-in.**
- **ASD:** wa = 1.84 kip/ft → Va = **7.36 kips**; Ma = **14.7 kip-ft**; Ta = **44.2 kip-in.**

Torsion varies linearly (max at supports, zero at midspan); shear likewise; moment peaks at midspan.

### 2. Available Strengths

**Torsion (§H3.1, Example H.5A):** Tc = **273 kip-in. (LRFD) / 181 kip-in. (ASD)**
Check threshold: Tr = 66.2 > 0.2Tc = 54.6 (LRFD) → full Eq. H3-6 interaction required.

**Shear (§G4):** h = 6.00 − 3(0.233) = 5.30 in.; Aw = 2(5.30)(0.233) = 2.47 in.²; h/t = 22.8 ≤ 59.2 → Cv2 = 1.0
Vn = 0.6(50)(2.47) = 74.1 kips → **Vc = 66.7 kips (LRFD) / 44.4 kips (ASD)**

**Flexure (§F7):** b/t = 14.2 ≤ λp = 27.0 and h/t = 22.8 ≤ λpw = 58.3 → compact; LTB non-critical (closed shape, Lb = 8 ft)
Mn = Mp = FyZx = 50(8.53) = 427 kip-in. = 35.5 kip-ft → **Mc = 32.0 kip-ft (LRFD) / 21.3 kip-ft (ASD)**

### 3. Interaction — Eq. H3-6

(Pr/Pc + Mrx/Mcx) + (Vr/Vc + Tr/Tc)² ≤ 1.0 (Pr = 0)

**At the supports (V and T maxima, M = 0):**
- LRFD: (0) + (11.0/66.7 + 66.2/273)² = (0.166 + 0.242)² = (0.408)² = **0.17 ≤ 1.0 ✓**
- ASD: (7.36/44.4 + 44.2/181)² = (0.410)² = **0.17 ≤ 1.0 ✓**

**At midspan (M maximum, V = T = 0):**
- LRFD: 22.1/32.0 = **0.69 ≤ 1.0 ✓**; ASD: 14.7/21.3 = **0.69 ≤ 1.0 ✓**

Intermediate locations were scanned (f(x) = M/Mc + (V/Vc + T/Tc)²) and are bounded by the midspan value.

### 4. Conclusion

The HSS6x4x1/4 **satisfies Eq. H3-6 at every cross section**, with the governing ratio 0.69 at midspan (flexure-dominated) and only 0.17 at the supports (shear + torsion). The torsionally stiff closed section carries the 6-in. load eccentricity efficiently; the member is adequate under both LRFD and ASD with ~30% reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
