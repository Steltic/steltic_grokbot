<!-- chunk_id: K.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.6",
 "example_family": "K.6",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "J2.4"
 ],
 "eqs": [],
 "tables": [],
 "title": "Single-Plate (Shear Tab) Connection to an HSS Column Face",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.6 — Single-Plate (Shear Tab) Connection to an HSS Column Face",
 "question": "# K.6 — Single-plate (shear-tab) connection to a rectangular HSS column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA wide-flange beam frames into the face of a square HSS column through a single\nshear plate (shear tab) that is shop-welded to the HSS face and field-bolted to the\nbeam web. Verify the trial single-plate connection: confirm that the HSS wall is\nnot a slender element (so that a single plate is permitted), check punching shear of\nthe HSS face from the eccentric beam reaction, and check the plate/weld and the\nbolt-group shear-transfer strength.\n\nThe beam is an ASTM A992 W18×35. The column is an ASTM A500 Grade C HSS6×6×3/8.\nThe plate is ASTM A572 Grade 50, welded with 70-ksi (E70XX) electrodes. The trial\ndetail is a PL5/16 in. × 4-1/2 in. × 8-1/2 in. with three rows of 3/4-in.-diameter\nGroup 120 bolts (thread condition N) at 3-in. vertical spacing, a 1-1/4-in. vertical\nedge distance, 1/4-in. fillet welds, and the bolt line at e = 3 in. from the HSS face.\n\n## Given\n- Material: beam ASTM A992 (Fy = 50 ksi, Fu = 65 ksi); column ASTM A500 Gr. C\n  (Fy = 50 ksi, Fu = 62 ksi); plate ASTM A572 Gr. 50 (Fy = 50 ksi, Fu = 65 ksi).\n- Beam W18×35: d = 17.7 in., tw = 0.300 in., T = 15-1/2 in.\n- Column HSS6×6×3/8: B = H = 6.00 in., design wall t = 0.349 in., b/t = 14.2.\n- Service vertical end reactions: dead PD = 6.5 kips, live PL = 19.5 kips.\n- Connection: PL5/16 × 4-1/2 × 8-1/2; three 3/4-in. Group 120 bolts (N) at 3-in.\n  spacing; lev = 1-1/4 in.; 1/4-in. E70XX fillet welds; eccentricity e = 3 in.\n- Code basis: AISC 360 (+ ASCE/SEI 7 for the load combinations).\n\n## Find\nThe required end reaction (LRFD and ASD); confirmation that the HSS wall is\nnonslender; the available punching-shear strength of the HSS face under the\neccentric reaction; the available plate/weld strength; and the available\nshear-transfer strength of the bolt group (bolt shear and bolt-hole bearing/tearout\nin the plate and beam web, reduced by eccentricity). Report the governing available\nstrength and whether the connection is adequate.",
 "has_figure": false,
 "stem": "K_6",
 "breadcrumb": "EXAMPLE K.6 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Single-Plate (Shear Tab) Connection to an HSS Column Face",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.6 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Single-Plate (Shear Tab) Connection to an HSS Column Face

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: HSS wall slenderness screen (single plates permitted on nonslender walls), face punching criterion (Fy,p·tp ≤ Fu,HSS·t), §J3.7/§J3.11a, §J4.2/§J4.3, §J2.4. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6.5 kips, L = 19.5 kips → **LRFD Ru = 39.0 kips; ASD Ra = 26.0 kips**

PL5/16 × 4 1/2 × 8 1/2 (A572 Gr. 50); three 3/4-in. Group 120-N bolts @ 3 in. (lev = 1 1/4 in.); e = 3 in.; 1/4-in. fillets to the HSS6x6x3/8 face (t = 0.349 in., Fu = 62 ksi); beam W18x35.

### 2. HSS Wall Checks

**Slenderness:** B/t = 6/0.349 = 17.2 ≤ 1.40√(E/Fy) = 33.7 → **wall nonslender; single plate permitted** ✓

**Punching (plate yields before the wall tears):** Fy,p·tp = 50(0.3125) = 15.6 kip/in. ≤ Fu,HSS·t = 62(0.349) = 21.6 kip/in. ✓

**Weld development:** demand per weld = 39.0/(2 × 8.5) = 2.3 kip/in. ≪ the wall's interface shear capacity (≈10 kip/in. per face) ✓.

### 3. Bolt Group (3 bolts, e = 3.0 in.)

C ≈ 2.2 → φRn = 2.2(17.9) = **39.4 kips ≥ 39.0 ✓** (LRFD, 99% — **governing**); Rn/Ω = 26.2 ≥ 26.0 ✓ (ASD, 99%)
Bearing on the 5/16 plate and 0.300-in. beam web — not controlling per bolt.

### 4. Plate and Welds

Shear yielding 0.6(50)(2.66) = 79.7 kips ✓; shear rupture φ = 53.7 ✓; block shear ✓; flexure at e trivial ✓.
Welds: 2(1.392)(4)(8.5) = 94.7 kips (LRFD) ≥ 39.0 ✓; 1/4 in. ≥ (5/8)tp = 0.195 → develops the plate ✓.

### 5. Conclusion

The trial shear tab on the HSS6x6x3/8 is **adequate** for 39.0 kips (LRFD) / 26.0 kips (ASD): the nonslender 3/8 wall permits the single-plate detail and passes the punching criterion, and the design is governed by the **eccentric three-bolt group at ≈99% utilization** — add a fourth row if loads may grow. (Compare Example K.7, where a slender wall forces a through-plate.)

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
