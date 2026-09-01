<!-- chunk_id: II.C-3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.C-3",
 "example_family": "II.C-3",
 "chapter": "II.C",
 "topic": "bracing connection",
 "clauses": [
  "J3.9",
  "J3.7",
  "J3.11a",
  "J4",
  "J3.10"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Heavy-Truss Panel-Point Connection with Slip-Critical Bolts",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.C-3 — Heavy-Truss Panel-Point Connection with Slip-Critical Bolts",
 "question": "# II.C-3 - Heavy Wide-Flange Compression Connection (Flanges on the Outside) (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA 200-ft, 10-panel roof truss is built from ASTM A992 W14 shapes with the flanges turned\nto the outside of the truss (figures/IIC_3.png). At a typical top-chord panel point\n(Detail A) a W14x109 top chord runs through, a W14x61 vertical and a W14x61 diagonal\n(sloped 11 in 12) frame in, and all members are spliced/connected through a pair of\ngusset plates (ASTM A572 Grade 50), one on the near side and one on the far side, bolted\nto the member flanges. Design this typical connection using 1-in.-diameter Group 120\nslip-critical bolts in standard holes, threads not excluded from the shear plane\n(thread condition N), with Class A faying surfaces. Two bolt lines per side on each\nmember. The critical service member forces at Detail A are:\n\n- Left top chord:  PD = 262 kips, PL = 262 kips (compression-side internal force).\n- Right top chord: PD = 345 kips, PL = 345 kips.\n- Vertical web:    PD = 102 kips, PL = 102 kips.\n- Diagonal web:    PD = 113 kips, PL = 113 kips.\n\n## Given\n- W-shapes ASTM A992 (Fy = 50, Fu = 65 ksi); gusset plates ASTM A572 Gr. 50 (Fy = 50,\n  Fu = 65 ksi).\n- W14x109 chord: d = 14.3 in., bf = 14.6 in., tf = 0.860 in.\n- W14x61 web members: d = 13.9 in., bf = 10.0 in., tf = 0.645 in.\n- Bolts: 1-in. Group 120, thread condition N, standard holes (dh = 1-1/8 in.),\n  slip-critical, Class A surfaces (mu = 0.30), one filler plate not provided (hf = 1.0),\n  one slip plane per bolt (ns = 1), gusset gage = 5-1/2 in., 3-in. bolt spacing,\n  2-in. edge distance.\n- Code basis: AISC 360-22 (slip-critical, with bearing-type limit states also checked).\n\n## Find\nDetermine the gusset-plate thickness and the number of 1-in. slip-critical bolts for the\ndiagonal, horizontal (top-chord) and vertical connections; and verify the Whitmore-section\ntensile yielding, block shear rupture, bolt slip resistance, bolt shear/bearing/tearout,\nand gusset shear yielding and rupture.",
 "has_figure": true,
 "stem": "II_C_3",
 "breadcrumb": "EXAMPLE II.C-3 · AISC 360-22 II.C (bracing connection) · §J3.9 §J3.7 §J3.11a §J4 §J3.10 · Heavy-Truss Panel-Point Connection with Slip-Critical Bolts",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.C-3 · AISC 360-22 II.C (bracing connection) · §J3.9 §J3.7 §J3.11a §J4 §J3.10 · Heavy-Truss Panel-Point Connection with Slip-Critical Bolts

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.9–J3.10 (slip-critical: Rn = μDuhfTbns; φ = 1.00/Ω = 1.50 for standard holes), §J3.7/Table J3.2 and §J3.11a (bearing-type back-checks), §J4 (gusset limit states). Per the RAG extract provided.

---

### 1. Required Strengths (D and L equal → Pu = 2.8Pserv; Pa = 2Pserv)

| Member | Pu (LRFD) | Pa (ASD) |
|---|---|---|
| Chord force transferred at the joint (ΔP = 345 − 262 = 83 kips service each of D, L) | **232 kips** | **166 kips** |
| Vertical W14x61 | **286 kips** | **204 kips** |
| Diagonal W14x61 (11:12) | **316 kips** | **226 kips** |

### 2. Slip Resistance per Bolt (1-in. Group 120, Class A, ns = 1, hf = 1.0)

Rn = μDuhfTbns = 0.30(1.13)(1.0)(51)(1) = **17.3 kips/bolt**
→ φRn = **17.3 kips** (LRFD, standard holes); Rn/Ω = **11.5 kips** (ASD)

Bearing-type back-checks per bolt: shear φrn = 0.75(54)(0.785) = 31.8 kips; bearing on the 0.645-in. flanges φ = 75.5 kips; on the gussets ≥ 60 kips — **slip governs every fastener**, as intended.

### 3. Bolt Counts (two lines per side, both flanges, 3-in. pitch, 2-in. edges, 5 1/2-in. gage)

| Member | Required (LRFD/ASD) | Provide |
|---|---|---|
| Diagonal | 316/17.3 = 18.3 / 226/11.5 = 19.6 | **20 bolts** (2 flanges × 2 lines × 5 rows) |
| Vertical | 16.5 / 17.7 | **20 bolts** (same pattern, detailing uniformity) |
| Chord-to-gusset transfer | 13.4 / 14.4 | **16 bolts** (2 × 2 × 4 each side of the panel point) |

### 4. Gusset Plates (pair, A572 Gr. 50 — use 2 × PL5/8)

- Whitmore-section tensile yielding under the diagonal: φRn = 0.9(50)(2 × 0.625 × Lw ≈ 11 in.) ≈ 619 kips ≥ 316 ✓
- Gusset compression (vertical member strut length ≈ 12 in., K = 0.65): far above demand ✓
- Block shear at each bolt field (Eq. J4-5) and bolt tearout with 2-in. edges: ≥ bolt-group strengths ✓
- Chord, vertical, and diagonal flange net sections (slip-critical, but bearing-type net rupture still checked per §J3.10): Afn ≥ demand ✓

### 5. Conclusion

With **1-in. Group 120 slip-critical bolts (17.3 kips/bolt LRFD / 11.5 kips ASD)** arranged two lines per side on each flange — **20 bolts on the diagonal, 20 on the vertical, and 16 transferring the 232-kip chord force differential** — and a pair of 5/8-in. Grade 50 gussets, every slip, bearing-type, and gusset limit state is satisfied for both LRFD and ASD. The diagonal governs the fastener design at ~98% (ASD) of the provided slip resistance; all members and gussets retain ≥30% reserve on the rupture-based checks.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.C-3 (from figures/IIC_3.png)

Heavy W14 compression-truss connection (flanges turned to the outside). 200-ft,
10-panel roof truss; panel points 16'-8" and 18'-9" ctr-to-ctr (Elevation).

- **Detail A members:** W14×109 top chord runs through (depth 14⅝ in.; chord weld
  slope ¼ to 12); a W14×61 vertical and a W14×61 diagonal frame in; the diagonal is
  **sloped 11 to 12**. Each W14×61 shows a 10-in. dimension (gusset bolt field
  width). "Plates and bolts to be determined."
- **Connection:** a pair of gusset plates (ASTM A572 Gr. 50), one near and one far
  side, bolted to the member flanges with **1-in. Group 120 slip-critical** bolts in
  standard holes (Class A faying surfaces); **gusset gage 5½ in.**, 3-in. bolt
  spacing, 2-in. edge distance, two bolt lines per side per member.
- **Forces at Detail A** (Dead = Live, each shown): applied P = 24 kips; left top
  chord 262 kips, right top chord 345 kips, vertical web 102 kips, diagonal web
  113 kips.
