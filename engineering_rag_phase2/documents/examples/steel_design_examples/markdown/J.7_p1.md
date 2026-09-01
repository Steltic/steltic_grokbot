<!-- chunk_id: J.7_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.7",
 "example_family": "J.7",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J10.2",
  "J10.3",
  "J10.4"
 ],
 "eqs": [
  "J10-2",
  "J10-4"
 ],
 "tables": [],
 "title": "Girder Web Under an Interior Concentrated Force",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.7 — Girder Web Under an Interior Concentrated Force",
 "question": "# J.7 — Concentrated Forces for a Beam Bearing on a Girder  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA W24×55 girder spans 20 ft and is simply supported. A W18×50 beam frames onto the\ntop of the girder and delivers a downward concentrated reaction at a point 8 ft from\nthe girder's left support (i.e., a = 8 ft, b = 12 ft along the 20-ft span). The beam\nis bolted to the top flange of the girder, so the girder's compression (top) flange\nis restrained against rotation at the load point. The concentrated force is applied\nfar enough from the girder ends (greater than the full girder depth d) that interior\nlimit-state equations apply. The bearing length delivered to the girder web is taken\nas the beam flange width, lb = bf(beam) = 7.50 in. Both members are ASTM A992/A992M.\n\nThe concentrated reaction is 15 kips dead load plus 30 kips live load. Determine the\navailable strength of the W24×55 girder for the applicable concentrated-force limit\nstates (web local yielding, web local crippling, web sidesway buckling) and state\nwhether transverse stiffeners are required, for both LRFD and ASD.\n\n## Given\n- Girder: W24×55, A992 (Fy = 50 ksi); d = 23.6 in., tw = 0.395 in., tf = 0.505 in.,\n  bf = 7.01 in., kdes = 1.01 in., h/tw = 54.6, Sx = 114 in³.\n- Beam: W18×50, A992; bf = 7.50 in. (= bearing length lb), tf = 0.570 in.\n- Geometry: girder span L = 20 ft, simple; concentrated load at a = 8 ft, b = 12 ft;\n  compression flange restrained against rotation (beam bolted to top flange).\n- Loads: RD = 15 kips, RL = 30 kips.\n- Code basis: AISC 360-22 §J10; loads per ASCE/SEI 7.\n\n## Find\nAvailable strength of the girder web for the governing concentrated-force limit states\nand whether stiffeners are required.",
 "has_figure": false,
 "stem": "J_7",
 "breadcrumb": "EXAMPLE J.7 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J10.2 §J10.3 §J10.4 · Girder Web Under an Interior Concentrated Force",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.7 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J10.2 §J10.3 §J10.4 · Girder Web Under an Interior Concentrated Force

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J10.2 (web local yielding, Eq. J10-2 — interior), §J10.3 (web local crippling, Eq. J10-4 — interior), §J10.4 (web sidesway buckling applicability). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 15 kips, L = 30 kips → **LRFD Ru = 66.0 kips; ASD Ra = 60.0 kips**

W24x55 girder (tw = 0.395 in., tf = 0.505 in., kdes = 1.11 in., d = 23.6 in., h/tw = 54.6, bf = 7.01 in.); interior load (a = 8 ft > d from the end); bearing length lb = 7.50 in.; top (compression) flange restrained against rotation by the bolted W18x50.

### 2. Web Local Yielding — Eq. J10-2 (φ = 1.00, Ω = 1.50)

Rn = Fywtw(5kdes + lb) = 50(0.395)(5.55 + 7.50) = **258 kips**

- LRFD: **258 ≥ 66.0 ✓**; ASD: 172 ≥ 60.0 ✓

### 3. Web Local Crippling — Eq. J10-4 (φ = 0.75, Ω = 2.00)

Rn = 0.80tw²[1 + 3(lb/d)(tw/tf)^1.5]√(EFywtf/tw)
= 0.80(0.395)²[1 + 3(0.318)(0.692)]√(29,000 × 50 × 0.505/0.395) = 0.125(1.66)(1,360) = **282 kips**

- LRFD: φRn = **212 ≥ 66.0 ✓**; ASD: 141 ≥ 60.0 ✓

### 4. Web Sidesway Buckling — §J10.4

With the compression flange restrained against rotation, Eq. J10-6 applies only when (h/tw)/(Lb/bf) ≤ 2.3. Taking Lb = 96 in. (the 8-ft segment): (54.6)/(96/7.01) = 54.6/13.7 = **3.99 > 2.3 → the limit state does not apply.**

### 5. Conclusion

The W24x55 girder web carries the 66-kip (LRFD) / 60-kip (ASD) interior concentrated reaction with large margins — web local yielding 26% utilized, web local crippling 31% (LRFD) — and web sidesway buckling is excluded by the restrained, relatively stocky configuration. **No transverse stiffeners or doubler plates are required** at the load point.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
