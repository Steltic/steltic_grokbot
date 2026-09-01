<!-- chunk_id: K.4_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.4",
 "example_family": "K.4",
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
 "title": "Unstiffened Seated Connection to an HSS Column Face",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.4 — Unstiffened Seated Connection to an HSS Column Face",
 "question": "# K.4 — Unstiffened Seated Connection to an HSS Column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA beam is supported on an unstiffened seat angle welded to the face of a square HSS\ncolumn. The seat angle's outstanding leg provides bearing for the beam bottom flange; a\nlight top angle is added for stability only. Verify the seated connection (seat angle,\nits weld to the HSS, and the bearing length required by the beam web) for the given\nreaction.\n\nThe supported beam is an ASTM A992/A992M W21×62. The column is an ASTM A500/A500M\nGrade C HSS12×12×1/2. The seat and top angles are ASTM A572/A572M Grade 50. Use 70-ksi\n(E70XX) electrodes. The seat is an L8×4×5/8 (8-in. long) welded to the HSS with 5/16-in.\nfillet welds along its vertical legs; a 1/4-in. underrun tolerance is included when\nchecking the bearing-length-to-depth ratio. Verify for the following service vertical\nshear (beam end reaction):\n\n  Dead load   P_D = 9 kips\n  Live load   P_L = 27 kips\n\n## Given\n- Materials: beam ASTM A992 (F_y = 50 ksi, F_u = 65 ksi); column ASTM A500 Grade C\n  (F_y = 50 ksi, F_u = 62 ksi); angles ASTM A572 Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n  Electrodes E70XX.\n- Beam W21×62: t_w = 0.400 in., t_f = 0.615 in., d = 21.0 in., k_des = 1.12 in.\n- Column HSS12×12×1/2: design wall t = 0.465 in., B = 12.0 in.\n- Seat angle L8×4×5/8 (length 8 in.), 5/16-in. fillet welds; top angle L4×4×1/4 for stability.\n- Loads: P_D = 9 kips, P_L = 27 kips.\n- Code basis: AISC 360-22 (Chapter J: J10 web limit states, J2.4 welds, J4 angle); ASCE/SEI 7.\n\n## Find\nDetermine the minimum required bearing length l_b (controlled by web local yielding and web\nlocal crippling of the beam, but not less than k_des); verify the outstanding seat-angle leg\nstrength and the seat-angle weld strength against the demand; confirm the HSS wall is thick\nenough to develop the 5/16-in. weld; and specify the top angle. Compare available to required\nstrength (LRFD and ASD).",
 "has_figure": false,
 "stem": "K_4",
 "breadcrumb": "EXAMPLE K.4 · AISC 360-22 Ch.K (HSS connection) · §J10.2 §J10.3 §J2.4 §J4.2 · Unstiffened Seated Connection to an HSS Column Face",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.4 · AISC 360-22 Ch.K (HSS connection) · §J10.2 §J10.3 §J2.4 §J4.2 · Unstiffened Seated Connection to an HSS Column Face

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J10.2 (Eq. J10-3), §J10.3 (Eq. J10-5a), §J2.4 (seat welds), §J4.2; HSS-wall development (3.09D/Fu); Manual Part 10 seated-connection model. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 9 kips, L = 27 kips → **LRFD Ru = 54.0 kips; ASD Ra = 36.0 kips**

Seat: L8x4x5/8 × 8 in. (A572 Gr. 50), 4-in. OSL, welded to the HSS12x12x1/2 face (t = 0.465 in., Fu = 62 ksi) with two vertical 5/16-in. E70 fillets × 8 in.; beam W21x62 (tw = 0.400 in., tf = 0.615 in., kdes = 1.12 in., d = 21.0 in.); 1/2-in. setback + 1/4-in. underrun.

### 2. Beam-Web Bearing Length

- Web local yielding (Eq. J10-3): lb,req = 54.0/[50(0.400)] − 2.5(1.12) = 2.70 − 2.80 < 0 → contact governs ✓
- Web local crippling (Eq. J10-5a at small lb, lb/d ≤ 0.2 even with underrun): φRn ≈ 71.7 kips ≥ 54.0 ✓ (ASD 47.8 ≥ 36.0 ✓)

Use lb = 3/4 in. minimum ≤ 3.25 in. available on the OSL ✓.

### 3. Seat Angle and Welds

OSL flexure: critical-section eccentricity = 0.50 + 0.38 − (0.625 + 0.375) < 0 → not critical; leg shear 150 kips ✓.

Welds (two 5/16-in. × 8 in. verticals; reaction at e = 0.875 in., conservatively up to 2.25 in.):
fv = 54.0/16 = 3.38 kip/in.; fb(e = 2.25) = 6(27.0)(2.25)/64 = 5.70 kip/in. → resultant ≈ **6.6 kip/in. ≤ 6.96 ✓** (LRFD; ASD 4.4 ≤ 4.64 ✓)

**HSS wall:** 3.09D/Fu = 3.09(5)/62 = **0.25 in. ≤ 0.465 in. ✓** — the 1/2-in. wall develops the seat welds, and face plastification under the seat moment is non-critical for this wall thickness.

### 4. Conclusion

The welded L8x4x5/8 seat on the HSS12x12x1/2 face is **adequate** for 54.0 kips (LRFD) / 36.0 kips (ASD): the W21x62 web needs only nominal bearing, the seat welds work at ≈95% under the conservative outer-bearing eccentricity (74% at the Manual eccentricity), and the heavy HSS wall develops the welds without face-plastification concerns. The L4x4x1/4 top angle completes the detail for stability.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
