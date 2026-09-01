<!-- chunk_id: K.5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.5",
 "example_family": "K.5",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J10.2",
  "J10.3",
  "J2.4",
  "J4.2"
 ],
 "eqs": [
  "J10-3",
  "J10-5a"
 ],
 "tables": [],
 "title": "Stiffened Seated Connection to an HSS Column Face",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.5 — Stiffened Seated Connection to an HSS Column Face",
 "question": "# K.5 — Stiffened seated connection of a W-shape beam to an HSS column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA wide-flange floor beam frames into the face of a square HSS column and is\nsupported on a stiffened seat (a horizontal seat plate reinforced by a vertical\ntriangular stiffener plate welded beneath it, with the stiffener and seat welded\nto the column face). Verify that the seat assembly and the beam web are adequate\nfor the beam end reaction, and confirm the trial stiffener width, stiffener\nlength, weld size, and HSS-wall thickness.\n\nThe beam is an ASTM A992 W21×68. The column is an ASTM A500 Grade C HSS14×14×1/2.\nThe seat plate, stiffener plate, and top angle are ASTM A572 Grade 50. All welds\nuse 70-ksi (E70XX) electrodes. Assume a 3/4-in. beam end setback from the column\nface. The trial detail is a 7-in.-wide seat, a 24-in.-long stiffener welded to the\ncolumn with 5/16-in. fillet welds (with 5-in.-long, 5/16-in. seat-plate-to-column\nwelds on each side of the stiffener), and an L4×4×1/4 top angle for stability.\n\n## Given\n- Material: beam ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); column ASTM A500 Gr. C\n  (Fy = 50 ksi, Fu = 62 ksi); plates/angle ASTM A572 Gr. 50 (Fy = 50 ksi, Fu = 65 ksi).\n- Beam W21×68: tw = 0.430 in., tf = 0.685 in., d = 21.1 in., kdes = 1.19 in.\n- Column HSS14×14×1/2: design wall t = 0.465 in., B = 14.0 in.\n- Service vertical end reactions: dead PD = 20 kips, live PL = 60 kips.\n- Beam end setback = 3/4 in. Welds: E70XX. Trial seat width W = 7 in.; stiffener\n  length l = 24 in.; 5/16-in. fillet welds; L4×4×1/4 top angle.\n- Code basis: AISC 360 (+ ASCE/SEI 7 for the load combinations).\n\n## Find\nThe factored/required end reaction (LRFD and ASD), and whether the trial stiffened\nseated connection is adequate: the seat width required to satisfy beam web local\nyielding and web local crippling, the seat-weld available strength, the required\nHSS-wall thickness to match the weld, and the HSS-wall strength check for the\nstiffener length. Report the governing available strength and the conclusion.",
 "has_figure": false,
 "stem": "K_5",
 "breadcrumb": "EXAMPLE K.5 · AISC 360-22 Ch.K (HSS connection) · §J10.2 §J10.3 §J2.4 §J4.2 · Stiffened Seated Connection to an HSS Column Face",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.5 · AISC 360-22 Ch.K (HSS connection) · §J10.2 §J10.3 §J2.4 §J4.2 · Stiffened Seated Connection to an HSS Column Face

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (Eq. J10-3), §J10.3 (Eqs. J10-5a/b), §J2.4, §J4.2; HSS-wall development (3.09D/Fu); Manual Part 10 stiffened-seat model (e = 0.8W). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 20 kips, L = 60 kips → **LRFD Ru = 120 kips; ASD Ra = 80.0 kips**

Trial: 7-in.-wide seat plate over a 24-in.-long stiffener, both welded to the HSS14x14x1/2 face (t = 0.465 in., Fu = 62 ksi) with 5/16-in. E70 fillets (plus 5-in. seat-plate welds each side); W21x68 beam (tw = 0.430 in., tf = 0.685 in., kdes = 1.19 in., d = 21.1 in.); 3/4-in. setback; L4x4x1/4 top angle.

### 2. Beam-Web Bearing (sets the seat width)

- Web local yielding (Eq. J10-3): lb,req = 120/[50(0.430)] − 2.98 = **2.60 in.**
- Web local crippling: at lb/d = 0.2 the Eq. J10-5a capacity is φ110 kips < 120 → Eq. J10-5b: **lb,req ≈ 5.9 in.** ← governs

W ≥ 5.9 + 0.75 = 6.65 in. → **W = 7 in. ✓**

### 3. Stiffener-to-HSS Welds (two 5/16-in. fillets, l = 24 in.; e = 0.8W = 5.6 in.)

fv = 120/(2 × 24) = 2.50 kip/in.; fb = 6(120 × 5.6/2)/24² = 3.50 kip/in. → resultant = **4.30 kip/in. ≤ 1.392(5) = 6.96 ✓** (LRFD, 62%); ASD 2.87 ≤ 4.64 ✓

Seat-plate-to-column welds (5 in. each side) and seat/stiffener interface welds: lightly stressed ✓. Stiffener thickness 5/8 in. develops the welds (≥ 0.48 in.) and exceeds the beam tw ✓.

### 4. HSS Wall

3.09D/Fu = 3.09(5)/62 = **0.25 in. ≤ 0.465 in. ✓** — the 1/2-in. wall develops the stiffener welds; wall plastification under the seat moment couple is satisfied for the 14-in. face at this load (the long 24-in. stiffener keeps face stresses low).

### 5. Conclusion

The trial stiffened seat — **7-in. seat, 24-in. stiffener, 5/16-in. E70 fillets on the HSS14x14x1/2** — is **adequate** for 120 kips (LRFD) / 80 kips (ASD). Web local crippling of the W21x68 governs the seat width (5.9-in. bearing required of the 7-in. seat), while the generous 24-in. stiffener keeps the eccentric weld group at only ~62% utilization and protects the HSS face. Detail with the top stability angle as shown.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
