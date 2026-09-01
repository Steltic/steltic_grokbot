<!-- chunk_id: K.7_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.7",
 "example_family": "K.7",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J2.4"
 ],
 "eqs": [],
 "tables": [],
 "title": "Through-Plate Shear Connection to a Thin-Walled HSS Column",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.7 — Through-Plate Shear Connection to a Thin-Walled HSS Column",
 "question": "# K.7 — Through-plate connection to a thin-walled rectangular HSS column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA wide-flange beam frames into the narrow (4-in.) wall of a thin-walled rectangular\nHSS column. Because the connected HSS wall is a slender element, a single shear plate\nis not permitted; instead a through-plate is used—a plate that passes completely\nthrough two slots in the HSS and is welded to both walls, with the beam bolted to the\nprojecting leg. Verify the through-plate connection: treat the bolted-to-beam portion\nas a single plate (bolt shear transfer, plate/weld) and check shear yielding and\nshear rupture of the two HSS walls that the plate welds engage.\n\nThe beam is an ASTM A992 W18×35. The column is an ASTM A500 Grade C HSS6×4×1/8, with\nthe plate connected to one of the 6-in. faces (a deliberately thin wall, to illustrate\nthe through-plate). The plate is ASTM A572 Grade 50, welded with 70-ksi (E70XX)\nelectrodes. The trial detail is a 1/4-in. through-plate with three rows of 3/4-in.\nGroup 120 bolts (thread condition N) at 3-in. spacing (plate length l = 8-1/2 in.),\n3/16-in. fillet welds to each HSS wall, the bolt line at a = 3 in. from the nearer\nweld line, and a 1-1/4-in. vertical edge distance.\n\n## Given\n- Material: beam ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); column ASTM A500 Gr. C\n  (Fy = 50 ksi, Fu = 62 ksi); plate ASTM A572 Gr. 50 (Fy = 50 ksi, Fu = 65 ksi).\n- Beam W18×35: d = 17.7 in., tw = 0.300 in., T = 15-1/2 in.\n- Column HSS6×4×1/8: B = 4.00 in., H = 6.00 in., design wall t = 0.116 in.,\n  h/t = 48.7, b/t = 31.5.\n- Service vertical end reactions: dead PD = 3.3 kips, live PL = 9.9 kips.\n- Connection: 1/4-in. through-plate, l = 8-1/2 in.; three 3/4-in. Group 120 (N)\n  bolts at 3-in. spacing; lev = 1-1/4 in.; 3/16-in. E70XX fillet welds to both HSS\n  walls; a = 3 in. (bolt line to nearer weld line).\n- Code basis: AISC 360 (+ ASCE/SEI 7 for the load combinations).\n\n## Find\nThe required end reaction (LRFD and ASD); confirmation that the HSS wall is slender\n(so a through-plate, not a single plate, is required); the available plate/weld\nstrength and bolt-group shear-transfer strength of the single-plate-like portion;\nthe required weld size; and the available shear yielding (§J4.2 Eq. J4-3) and shear\nrupture (§J4.2 Eq. J4-4) strengths of the two engaged HSS walls. Report the governing\navailable strengths and whether the connection is adequate.",
 "has_figure": false,
 "stem": "K_7",
 "breadcrumb": "EXAMPLE K.7 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J2.4 · Through-Plate Shear Connection to a Thin-Walled HSS Column",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.7 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J2.4 · Through-Plate Shear Connection to a Thin-Walled HSS Column

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: wall-slenderness screen (slender wall → through-plate required), §J3.7/§J3.11a, §J4.2 (HSS wall shear yielding/rupture at the slots), §J2.4. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 3.3 kips, L = 9.9 kips → **LRFD Ru = 19.8 kips; ASD Ra = 13.2 kips**

HSS6x4x1/8 (t = 0.116 in.): connected 6-in. wall slenderness = 6/0.116 ≈ 52 > 1.40√(E/Fy) = 33.7 → **slender; a single plate is not permitted — a through-plate is used** (1/4-in. plate through slots, 3/16-in. fillets to both walls; three 3/4-in. Group 120-N bolts @ 3 in., a = 3 in., l = 8 1/2 in.).

### 2. Bolted Side (treated as a single-plate connection)

Bolt group (3 bolts, e = 3 in., C ≈ 2.2): φRn = **39.4 kips ≥ 19.8 ✓**; Rn/Ω = 26.2 ≥ 13.2 ✓
Plate: shear yielding 0.6(50)(2.13) = 63.8 kips ✓; rupture φ = 43.0 ✓; block shear ✓; bearing on the 1/4-in. plate and beam web ✓.

### 3. Welds and HSS Walls

Welds: 3/16-in. fillets both faces at **both** walls (4 lines × 8.5 in.): φRn = 4(1.392)(3)(8.5) = 142 kips ≫ 19.8 ✓. The through-plate delivers the reaction (and the e = 3 in. moment couple) to the two walls rather than bending the slender face.

Wall shear at the slots (§J4.2), both walls engaged, two planes each:
Shear yielding: Rn = 0.6(50)[4 × 8.5 × 0.116] = **118 kips** → 118/78.9 ✓
Shear rupture: Rn = 0.6(62)(3.94) = 147 → φ110 ✓

### 4. Conclusion

The through-plate detail is **adequate** for 19.8 kips (LRFD) / 13.2 kips (ASD) with the bolt group at ~50% and every wall limit state far below capacity. The example's point: with a 1/8-in. slender HSS wall, the through-plate bypasses face plastification/punching entirely by reacting the connection on both walls — at the cost of slotting the column. Bolts/plate remain identical to a conventional shear tab.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
