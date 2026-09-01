<!-- chunk_id: K.2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.2",
 "example_family": "K.2",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J2.4",
  "J4.2",
  "K"
 ],
 "eqs": [],
 "tables": [
  "J2.5"
 ],
 "title": "Narrow-Tee Shear Connection to an HSS Column Face",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.2 — Narrow-Tee Shear Connection to an HSS Column Face",
 "question": "# K.2 — Welded/Bolted Narrow-Tee Connection to an HSS Column  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simple beam-to-column shear connection uses a structural tee bolted to the beam web\nand fillet-welded to the flat face of a square HSS column. This is the narrow-tee\nvariant of the wide-tee detail: the tee flange has been stripped down to b_f = 5 in. so\nthat two fillet welds fit entirely on the flat width of the HSS face (no flare-bevel\ngroove weld is needed). The supported beam stays centered on the column centerline, so\nthe tee stem is slightly offset from the column centerline.\n\nThe supported beam is an ASTM A992/A992M W16×50. The column is an ASTM A500/A500M\nGrade C HSS8×8×1/4. The tee is an ASTM A992/A992M WT5×24.5 with its flange stripped to\n5 in. The tee stem is bolted to the beam web with four 3/4-in. Group 120 bolts (N) in\nstandard holes at s = 3 in.; the tee is l = 11.5 in. long. The bolt-group, tee-stem,\nand beam-web-bearing checks are identical to the wide-tee detail and are taken as\nsatisfied here; the new question is whether the fillet weld on the HSS flat is adequate\nand whether the stripped flange fits. Use 70-ksi (E70XX) electrodes and a flexible\n(simple) support assumption.\n\nVerify the welded connection for the following service vertical shear:\n\n  Dead load   P_D = 6.2 kips\n  Live load   P_L = 18.5 kips\n\n## Given\n- Materials: beam and tee ASTM A992 (F_y = 50 ksi, F_u = 65 ksi); column ASTM A500\n  Grade C (F_y = 50 ksi, F_u = 62 ksi). Electrodes E70XX.\n- Beam W16×50: t_w = 0.380 in., d = 16.3 in., t_f = 0.630 in.\n- Tee WT5×24.5 (flange stripped): stem t_sw = 0.340 in., d = 4.99 in., t_f = 0.560 in.,\n  stripped b_f = 5.00 in., k_1 = 13/16 in.\n- Column HSS8×8×1/4: t = 0.233 in., B = 8.00 in.\n- Tee length l = 11.5 in.; bolt-line offset (stem) ≈ 0.360 in. from column centerline.\n- Loads: P_D = 6.2 kips, P_L = 18.5 kips.\n- Code basis: AISC 360-22 (Chapter J); ASCE/SEI 7 load combinations.\n\n## Find\nCheck that the 5-in. stripped flange fits within the flat HSS face (allowing weld shelf\nand corner radius), determine the minimum and trial fillet-weld size (including the weld\nductility limit), verify the available fillet-weld shear strength against the demand, and\nconfirm the HSS wall is thick enough to develop the weld. State the governing weld\nstrength (LRFD and ASD).",
 "has_figure": false,
 "stem": "K_2",
 "breadcrumb": "EXAMPLE K.2 · AISC 360-22 Ch.K (HSS connection) · §J2.4 §J4.2 §K · Narrow-Tee Shear Connection to an HSS Column Face",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.2 · AISC 360-22 Ch.K (HSS connection) · §J2.4 §J4.2 §K · Narrow-Tee Shear Connection to an HSS Column Face

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J2.4/Table J2.5 (fillet welds on the HSS flat), §J4.2 (HSS-wall base metal, 3.09D/Fu criterion), Chapter K face checks. Bolt-group, tee-stem, and beam-web checks identical to Example K.1 (taken as satisfied). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6.2 kips, L = 18.5 kips → **LRFD Ru = 37.0 kips; ASD Ra = 24.7 kips**

WT5x24.5 with the flange stripped to bf = 5.00 in. so two vertical fillet welds land entirely on the flat of the HSS8x8x1/4 face (t = 0.233 in., flat width ≈ 8 − 3t ≈ 7.3 in. ≥ 5.0 ✓).

### 2. Weld Design (two vertical fillets, l = 11 1/2 in.)

Demand per weld line (flexible-support model, R at the bolt-line eccentricity): fv = 37.0/(2 × 11.5) = 1.61 kip/in.; flexural component from the small weld-line eccentricity ≈ 2.6 kip/in. → resultant ≈ **3.1 kip/in.**

**Use 3/16-in. fillets (D = 3):** available 1.392(3) = **4.18 kip/in. ≥ 3.1 ✓** (LRFD); 2.78 ≥ 2.1 ✓ (ASD). Minimum size for the 0.233-in. wall = 1/8 in. ✓.

### 3. HSS Wall Adequacy

Each weld is one-sided on the wall at its location: required wall ≥ 3.09D/Fu = 3.09(3)/62 = **0.15 in. ≤ 0.233 in. ✓** — the wall develops the weld. (Had 1/4-in. welds both been required at one point, 6.19D/Fu = 0.40 in. would exceed the wall — the reason the weld is kept at 3/16 in. and the flange stripped to keep welds on the flat but apart.) Face plastification under the small end moment of the flexible connection is non-critical for the 1/4-in. wall at this load level ✓.

### 4. Conclusion

The narrow-tee detail is **adequate** for 37.0 kips (LRFD) / 24.7 kips (ASD): 3/16-in. fillets on the HSS flat carry the reaction at ~74% utilization with the 0.233-in. wall able to develop them. The trade-off versus the wide-tee (Example K.1) is that the welds now bear on the flexible face rather than the corners, so weld size is capped by the wall-development criterion — satisfied here.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
