<!-- chunk_id: II.A-6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-6",
 "example_family": "II.A-6",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J4.2"
 ],
 "eqs": [],
 "tables": [],
 "title": "Beam End Coped at the Top Flange",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-6 — Beam End Coped at the Top Flange",
 "question": "# II.A-6 — Beam End Coped at the Top Flange Only  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992 W21x62 beam has a rectangular cope at the top flange only: 8 in. deep by 9 in.\nlong, with a 1/2-in. setback (so the moment arm to the support is e = 9-1/2 in.). The shear\nconnection is welded to the beam web, and the beam is braced at the end of the uncoped section.\nSee figures/IIA_6.png.\n\nPart A: Determine the available strength of the coped beam end, considering flexural yielding,\nflexural local web buckling, shear yielding, and shear rupture.\n\nPart B: For end reactions R_D = 23 kips and R_L = 67 kips, select an alternate ASTM A992 W21\nshape that needs no cope reinforcement.\n\n## Given\n- Beam (Part A): ASTM A992 W21x62 (d = 21.0 in., t_w = 0.400 in., b_f = 8.24 in., t_f = 0.615 in.),\n  F_y = 50 ksi, F_u = 65 ksi. Cope: d_c = 8 in. (top flange), c = 9 in., setback 1/2 in., e = 9-1/2 in.\n- Loads (Part B): R_D = 23 kips, R_L = 67 kips.\n- Code basis: AISC 360-22 (web shear, Section J4.2) with the coped-section flexural local-web-\n  buckling check from AISC Manual Part 9 (Eq. 9-14 to 9-20; Manual Table 9-2 section properties).\n\n## Find\nPart A: the available strength of the coped W21x62 end (governed by the coped-section flexural\nlocal web buckling vs. web shear). Part B: confirm a heavier W21 (e.g., W21x73) provides\navailable strength >= the required reaction without reinforcement.",
 "has_figure": true,
 "stem": "II_A_6",
 "breadcrumb": "EXAMPLE II.A-6 · AISC 360-22 II.A (simple / shear connection) · §J4.2 · Beam End Coped at the Top Flange",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-6 · AISC 360-22 II.A (simple / shear connection) · §J4.2 · Beam End Coped at the Top Flange

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22 §J4.2 (web shear) with the coped-section flexural model of AISC Manual Part 9 (Fcr ≤ Fy on Snet; buckling coefficients f = 2c/d, k = 2.2(ho/c)^1.65). Per the RAG extract provided.

---

### Part A — Available Strength of the Coped W21x62

Cope: dc = 8 in., c = 9 in., setback 1/2 in. → e = 9.5 in.; remaining depth ho = 13.0 in.; tw = 0.400 in.

**Coped-section properties (tee):** Snet (to the top, reentrant fiber) ≈ **17.9 in.³**

**Flexural local web buckling:** f = 2c/d = 0.857; k = 2.2(13/9)^1.65 = 4.04 → Fcr = 26,210(tw/ho)²·f·k = 26,210(0.000947)(0.857)(4.04) = **86 ksi ≥ Fy → Fcr = 50 ksi** (buckling does not reduce the strength)

Mn = FySnet = 50(17.9) = 894 kip-in. → available end reaction from flexure:
- **LRFD:** φRn = 0.90(894)/9.5 = **84.6 kips** ← governs
- **ASD:** Rn/Ω = (894/1.67)/9.5 = **56.3 kips** ← governs

**Web shear (Eq. J4-3):** φRn = 1.00(0.6)(50)(13.0 × 0.400) = 156 kips; Rn/Ω = 104 kips — not governing. (Shear rupture at the net section likewise non-critical, no holes.)

**Available strength of the coped end: 84.6 kips (LRFD) / 56.3 kips (ASD), governed by flexure of the coped section.**

### Part B — Alternate W21 Without Cope Reinforcement

Required: **Ru = 1.2(23) + 1.6(67) = 135 kips; Ra = 90.0 kips** → required Snet ≥ Rue/(0.9Fy) = 135(9.5)/45 = **28.5 in.³** (LRFD; ASD gives a comparable 28.6 in.³).

- W21x62: Snet ≈ 17.9 in.³ → 84.6 kips — **inadequate without reinforcement** (doubler or longitudinal stiffening required).
- W21x73: Snet ≈ 21.0 in.³ → φRn ≈ 99.6 kips — an 18% improvement but **still short** of 135 kips for this 8 × 9 in. cope.
- **W21x93 (Snet ≈ 27.9 in.³, φRn ≈ 132 kips) is at the threshold; the first W21 fully clearing both LRFD and ASD demands without reinforcement is the W21x101/W21x111 class.**

The economical comparison is therefore between cope reinforcement on the W21x62 (the usual choice) and a substantially heavier section; if a shallower cope can be detailed (smaller dc or c), the lighter shapes recover quickly since capacity scales with Snet/e.

### Conclusion

The 8 × 9 in. top-flange cope reduces the W21x62 end capacity to **84.6 kips (LRFD) / 56.3 kips (ASD)**, flexure-governed (web buckling not critical, Fcr ≥ Fy). For the 135-kip factored reaction, upsizing within the W21 family requires Snet ≥ 28.5 in.³ — heavier than the suggested W21x73 — so cope reinforcement of the W21x62 per Manual Part 9 is recommended as the practical alternative.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-6 (from figures/IIA_6.png)

Beam W21×62 coped at the **top flange only**: cope length **c = 9 in.**, cope
depth **d_c = 8 in.** (½-in. setback → eccentricity e = 9½ in.). A simple shear
connection is at the coped end.

The figure shows three reinforcement options for the coped end:
- (a) **Simple shear connection** — bare cope (Part A evaluates this).
- (b) **Doubler plate** added at the cope, extending a length ≥ d_c past the cope.
- (c) **Longitudinal stiffeners** along the top and bottom of the cope, extending
  a length c (≥ d_c) past the cope.

Part B selects a heavier W21 that needs no reinforcement.
