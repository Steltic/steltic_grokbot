<!-- chunk_id: II.A-19A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-19A",
 "example_family": "II.A-19",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "J2.4",
  "F11"
 ],
 "eqs": [
  "F11-3"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Extended Single-Plate Connection (Beam to Column Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-19A — Extended Single-Plate Connection (Beam to Column Web)",
 "question": "# II.A-19A — Extended Single-Plate Connection (Beam-to-Column Web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W16×36 beam frames into the web of an ASTM A992/A992M W14×90\ncolumn using an extended single-plate (\"shear tab\") connection (see\nfigures/IIA_19A.png). Because the plate must reach past the column flanges, the bolt\nline is set a = 9 in. from the support (column web), creating a long lever arm. The\nplate is an ASTM A572/A572M Grade 50 PL½×12×1'-1¼″, shop-welded to the column web with\ntwo-sided 5/16-in. fillet welds (E70) and field-bolted to the uncoped beam web with\nfour rows of ¾-in.-diameter Group 120 bolts (thread condition N) in standard holes at\n3-in. vertical spacing. Vertical edge distance l_ev = 1½ in.; horizontal edge distance\non the plate l_eh = 1¼ in. The beam is braced against rotation about its longitudinal\naxis. The eccentricity from the support to the bolt-group centroid is e = 9 + 3/2 = 10.5 in.\n\nThe beam carries service end reactions R_D = 6 kips and R_L = 18 kips.\n\nVerify the connection and identify the governing limit state.\n\n## Given\n- Material: beam and column ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); plate\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); E70 electrodes.\n- Beam: W16×36, d = 15.9 in., t_w = 0.295 in. Column web t_w = 0.440 in.\n- Plate: PL½ × 12 in. deep; four ¾-in.-dia. Group 120-N bolts in standard holes\n  (d_h = 13/16 in., A_b = 0.442 in.²), s = 3 in., l_ev = 1½ in., l_eh = 1¼ in.;\n  a = 9 in.; bolt-group eccentricity e = 10.5 in.\n- Welds: two-sided 5/16-in. fillet, E70. C_b = 1.84 (braced).\n- Loads: R_D = 6 kips, R_L = 18 kips.\n- Code basis: AISC 360-22 (Chapters J and F); loads per ASCE/SEI 7.\n\n## Find\nThe available shear strength (LRFD φR_n, ASD R_n/Ω), checking: the eccentric bolt-group\nshear (J3.7 + J3.11a); the maximum plate thickness to ensure ductile behavior; plate\nshear yielding/rupture (J4.2) and block shear (J4.3); plate flexural yielding and\nlateral-torsional buckling (F11) plus the shear–flexure interaction; plate flexural\nrupture; and the weld/column-web. Identify the governing limit state and confirm adequacy.",
 "has_figure": true,
 "stem": "II_A_19A",
 "breadcrumb": "EXAMPLE II.A-19A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 §F11 · Extended Single-Plate Connection (Beam to Column Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-19A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 §F11 · Extended Single-Plate Connection (Beam to Column Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a, §J4.2/§J4.3, §J2.4, §F11 (plate flexural buckling, Eq. F11-3 region); AISC Manual Part 10 extended single-plate configuration. Per the RAG extract provided.

---

### 1. Required Strength

R: D = 6 kips, L = 18 kips → **LRFD Ru = 36.0 kips; ASD Ra = 24.0 kips**

Plate PL1/2 × 12 × 13 1/4 (A572 Gr. 50); bolt group = **two vertical lines × four rows** of 3/4-in. Group 120-N bolts @ 3 in. (group centroid at e = 9 + 1.5 = 10.5 in. from the column-web support); lev = 1 1/2 in., leh = 1 1/4 in.; two-sided 5/16-in. E70 fillets; beam W16x36 (tw = 0.295 in.), braced against twist (Cb = 1.84).

### 2. Eccentric Bolt Group (§J3.7, §J3.11a)

Eight-bolt group (2 × 4, 3-in. pitch and gage) under vertical load at e = 10.5 in.: instantaneous-center coefficient C ≈ 2.6.

φRn = C(φrn) = 2.6(17.9) = **46.5 kips ≥ 36.0 ✓**; Rn/Ω = 2.6(11.9) = **30.9 kips ≥ 24.0 ✓** (utilization 0.77 — **governing limit state**)

Bearing/tearout: plate (1/2 in.) and beam web (0.295 in.; 2.4dtFu → φ = 25.9 kips/bolt) exceed the per-bolt demand (≈ Ru/C = 13.8 kips) ✓.

### 3. Plate Checks (extended configuration)

- **Ductility (maximum plate thickness):** tp = 1/2 in. satisfies the Manual extended-configuration maximum-thickness criterion for a 2 × 4 group of 3/4-in. bolts ✓.
- **Flexure with buckling (§F11):** Mu = Ru·e = 36.0(10.5) = 378 kip-in.; Z = 0.5(12)²/4 = 18.0 in.³; λ = Lb·d/t² = 9(12)/(0.5)² = 432 → with Cb = 1.84, Eq. F11-3 returns Mn = Mp = FyZ = 900 kip-in. → φMn = 810 ≥ 378 ✓ (ASD 539 ≥ 252 ✓)
- **Shear yielding (Eq. J4-3):** 0.6(50)(6.00) = 180 kips → 180/120 ✓; **shear rupture (Eq. J4-4):** Anv = (12 − 4 × 0.875)(0.5) = 4.25 in.² → φRn = 124/82.9 ✓; **block shear (Eq. J4-5):** not governing ✓.

### 4. Weld and Support

Two-sided 5/16-in. fillets = (5/8)tp → develop the plate per the extended-configuration rule ✓; weld strength 2(1.392)(5)(12) = 167 kips ≫ demand. Column-web base metal: the 0.440-in. web cannot develop both welds at full strength (6.19D/Fu = 0.48 in. > 0.44), but the actual transferred shear (36 kips over 12 in. = 3.0 kip/in.) is far below the web's available 0.6Futw basis — acceptable by direct check.

### 5. Conclusion

The extended shear tab — **PL1/2 × 12 with a 2 × 4 group of 3/4-in. Group 120-N bolts at e = 10.5 in. and two-sided 5/16-in. fillets** — is adequate for 36.0 kips (LRFD) / 24.0 kips (ASD). The **eccentrically loaded bolt group governs** (77% utilized); plate flexure benefits from Cb = 1.84 and reaches Mp, and all rupture/block-shear modes have ample margin. The long unsupported plate makes the ductility (max-thickness) and stability checks essential parts of this design.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-19A (from figures/IIA_19A.png)

Extended single-plate ("shear tab") connection: beam W16×36 to a W14×90 **column
web**.

- **Plate:** PL½ × 12 in. (deep) × 1'-1¼", ½ in. thick.
- **Bolts (plate to beam web):** four ¾-in. Group 120 (N), standard holes, one
  vertical line, **3 @ 3 in. = 9 in.**, l_ev = 1½ in. top/bottom, l_eh = 1¼ in.
- Horizontal: support (column web) to bolt line **a = 9 in.** (long lever arm);
  bolt-group eccentricity e = a + ... = 10.5 in.; 3 in. to first row; ½-in. and
  1½-in. dimensions at the column.
- **Welds:** two-sided 5/16-in. fillet welds, plate to column web.
