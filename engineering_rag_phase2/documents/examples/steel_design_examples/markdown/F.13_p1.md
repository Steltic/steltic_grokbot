<!-- chunk_id: F.13_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.13",
 "example_family": "F.13",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F11",
  "F11.2"
 ],
 "eqs": [
  "F11-2"
 ],
 "tables": [],
 "title": "Round Bar in Bending",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.13 — Round Bar in Bending",
 "question": "# F.13 — Round bar in bending  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nUsing the AISC Specification directly, select a solid round bar for a simply supported,\nsingle-span beam carrying a concentrated dead and live load at midspan. The beam is braced\nat the end points only; conservatively take C_b = 1.0. The bar diameter is limited to 2 in.,\nand the self-weight of the bar is negligible. Determine an adequate bar diameter and report\nφ_b M_n (LRFD) and M_n/Ω_b (ASD).\n\n## Given\n- Material: ASTM A572/A572M Grade 50 (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, L = 2.5 ft, braced at the ends only; C_b = 1.0.\n- Loads (service, concentrated at midspan): dead P_D = 0.10 kip, live P_L = 0.25 kip.\n- Constraint: diameter ≤ 2 in.; bar self-weight negligible.\n- Member / section: to be selected (solid round bar).\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nSelect an adequate round-bar diameter and report the governing limit state with φ_b M_n\n(LRFD) and M_n/Ω_b (ASD).",
 "has_figure": false,
 "stem": "F_13",
 "breadcrumb": "EXAMPLE F.13 · AISC 360-22 Ch.F (beam flexure) · §F11 §F11.2 · Round Bar in Bending",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.13 · AISC 360-22 Ch.F (beam flexure) · §F11 §F11.2 · Round Bar in Bending

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F11 (Rectangular Bars and Rounds): Eq. F11-2; per §F11.2, lateral-torsional buckling does not apply to rounds. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 2.5 ft = 30 in.; midspan point load; self-weight negligible:

- **LRFD:** Pu = 1.2(0.10) + 1.6(0.25) = 0.520 kips → Mu = PuL/4 = 0.520(30)/4 = **3.90 kip-in.** (0.325 kip-ft)
- **ASD:** Pa = 0.35 kips → Ma = 0.35(30)/4 = **2.63 kip-in.** (0.219 kip-ft)

### 2. Trial Member — 1-in.-Diameter Round Bar (A572 Gr. 50; ≤ 2 in. limit ✓)

Z = d³/6 = 0.167 in.³; Sx = πd³/32 = 0.0982 in.³

### 3. Limit States — §F11

**Lateral-torsional buckling:** does not apply to rounds (§F11.2(a)) — bracing at ends only is therefore not a penalty.

**Yielding — Eq. F11-2 (rounds):**

> Mn = Mp = FyZ ≤ 1.6FySx

FyZ = 50(0.167) = 8.33 kip-in.; 1.6FySx = 1.6(50)(0.0982) = **7.85 kip-in.** ← cap governs (round shape factor 1.70 > 1.6)

**Mn = 7.85 kip-in.**

### 4. Available Flexural Strength

- **LRFD:** φbMn = 0.90(7.85) = **7.07 kip-in. (0.589 kip-ft)** ≥ 3.90 kip-in. ✓ (utilization 0.55)
- **ASD:** Mn/Ωb = 7.85/1.67 = **4.70 kip-in. (0.392 kip-ft)** ≥ 2.63 kip-in. ✓ (utilization 0.56)

### 5. Conclusion

**Select a 1-in.-diameter round bar (A572 Gr. 50).** The governing limit state is **yielding capped at 1.6FySx** (Eq. F11-2) — because the shape factor of a round (1.70) exceeds 1.6, the cap controls rather than the full plastic moment, a serviceability-motivated limit noted in the §F11 provisions. LTB does not apply to rounds, so the ends-only bracing has no effect. The bar carries the required moments with ~45% reserve; a 7/8-in. bar would also check numerically, but the 1-in. bar is selected as the practical standard size.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
