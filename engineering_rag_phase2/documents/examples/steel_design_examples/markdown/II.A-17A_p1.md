<!-- chunk_id: II.A-17A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-17A",
 "example_family": "II.A-17",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a",
  "J4.2",
  "J4.3",
  "J2.4"
 ],
 "eqs": [
  "J3-6a",
  "J4-3",
  "J4-4",
  "J4-5"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Conventional Single-Plate (Shear Tab) Connection",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-17A — Conventional Single-Plate (Shear Tab) Connection",
 "question": "# II.A-17A — Single-Plate Connection (Conventional Beam-to-Column Flange)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W16×50 beam frames into the flange of an ASTM A992/A992M W14×90\ncolumn using a conventional single-plate (\"shear tab\") connection (see\nfigures/IIA_17A.png). The plate is an ASTM A572/A572M Grade 50 PL¼×4½×0'-11½″ that is\nshop-welded to the column flange with 3/16-in. fillet welds (both sides, E70 electrodes)\nand field-bolted to the uncoped beam web with four rows of ¾-in.-diameter Group 120\nbolts (thread condition N) in standard holes at 3-in. vertical spacing. The bolt line\nis a = 3 in. from the weld line (column face); vertical edge distance l_ev = 1¼ in.;\nhorizontal edge distance on the plate l_eh = 1½ in.\n\nThe beam carries service end reactions R_D = 8 kips and R_L = 25 kips.\n\nVerify the available shear strength of the connection and identify the governing limit\nstate.\n\n## Given\n- Material: beam and column ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); plate\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi); E70 weld electrodes.\n- Beam: W16×50, d = 16.3 in., t_w = 0.380 in. Column flange t_f = 0.710 in.\n- Plate: PL¼ × 4½ in. wide × 11½ in. long; four ¾-in.-dia. Group 120-N bolts in\n  standard holes (d_h = 13/16 in., A_b = 0.442 in.²), s = 3 in., l_ev = 1¼ in.,\n  l_eh = 1½ in.; eccentricity of bolt group from weld line e = a/2 = 1.50 in.\n- Welds: 3/16-in. fillet, both sides of plate, E70.\n- Loads: R_D = 8 kips, R_L = 25 kips.\n- Code basis: AISC 360-22 (Chapter J); loads per ASCE/SEI 7.\n\n## Find\nThe available shear strength (LRFD φR_n, ASD R_n/Ω), checking the bolt-group shear\ntransfer at the holes including connection eccentricity (J3.7 + J3.11a), shear\nyielding and shear rupture of the plate (J4.2), block shear rupture of the plate\n(J4.3), the dimensional/edge-distance limits, and the weld. State the governing limit\nstate and confirm adequacy.",
 "has_figure": true,
 "stem": "II_A_17A",
 "breadcrumb": "EXAMPLE II.A-17A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Conventional Single-Plate (Shear Tab) Connection",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-17A · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a §J4.2 §J4.3 §J2.4 · Conventional Single-Plate (Shear Tab) Connection

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2, §J3.11a (Eqs. J3-6a/c), §J4.2 (Eqs. J4-3/J4-4), §J4.3 (Eq. J4-5), §J2.4 (fillet welds); AISC Manual Part 10 conventional single-plate configuration (e = a/2). Per the RAG extract provided.

---

### 1. Required Strength

R: D = 8 kips, L = 25 kips → **LRFD Ru = 49.6 kips; ASD Ra = 33.0 kips**

Plate PL1/4 × 4 1/2 × 11 1/2 (A572 Gr. 50); four 3/4-in. Group 120-N bolts @ 3 in. (lev = 1 1/4 in., leh = 1 1/2 in.); a = 3 in. → bolt-group eccentricity e = a/2 = 1.50 in.; 3/16-in. E70 fillets both sides to the column flange. Effective hole = 7/8 in. Conventional-configuration limits (single bolt line, a ≤ 3 1/2 in., t = 1/4 in. ductility limit) are satisfied.

### 2. Bolt Group with Eccentricity (§J3.7, §J3.11a)

Eccentric group coefficient (4 bolts @ 3 in., e = 1.50 in.): C ≈ 3.43.

Bolt shear: φrn = 17.9 kips → **φRn = 3.43(17.9) = 61.4 kips**; ASD 3.43(11.9) = **40.8 kips**.
Bearing/tearout on the 1/4-in. plate (vertical): interior bolts governed by bolt shear (φ 21.9 > 17.9); bottom bolt tearout lc = 0.844 in. → φ = 12.3 kips. Vertical group: 12.3 + 3(17.9) = 66.0 kips (LRFD) / 44.0 (ASD) — not governing.

### 3. Plate Limit States

| Limit state | Rn | LRFD avail. | ASD avail. |
|---|---|---|---|
| Shear yielding (Eq. J4-3) | 0.6(50)(2.88) = 86.3 | 86.3 | 57.5 |
| **Shear rupture (Eq. J4-4)** | 0.6(65)(2.00) = 78.0 | **58.5** | **39.0** |
| Block shear (Eq. J4-5, Ubs = 1) | 87.3 (≤ 94.1) | 65.5 | 43.7 |
| Flexural yielding at e (Z = 8.27 in.³) | Mu = 74.4 ≤ φMn = 372 kip-in. | ✓ | ✓ |

### 4. Welds and Supports

3/16-in. fillets both sides ≥ (5/8)tp = 0.156 in. → develop the plate per the conventional-configuration rule ✓.
Weld strength: 2(1.392)(3)(11.5) = 96.0 kips (LRFD) / 64.1 kips (ASD) ≥ demands ✓. Column flange (0.710 in.) and beam web (0.380 in.) bearing — not governing.

### 5. Summary and Conclusion

| Element | LRFD (kips) | ASD (kips) |
|---|---|---|
| Bolt group (eccentric) | 61.4 | 40.8 |
| **Plate shear rupture — governs** | **58.5** | **39.0** |
| Block shear | 65.5 | 43.7 |
| Plate shear yielding | 86.3 | 57.5 |
| Welds | 96.0 | 64.1 |
| **Available / required** | **58.5 / 49.6 ✓** | **39.0 / 33.0 ✓** |

The conventional shear tab — **PL1/4 × 4 1/2 × 11 1/2 with four 3/4-in. Group 120-N bolts and 3/16-in. double fillets** — is adequate; the governing limit state is **shear rupture of the plate** at 85% utilization, with the eccentrically loaded bolt group close behind. All AISC 360-22 Chapter J checks and Manual conventional-configuration limits are satisfied.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-17A (from figures/IIA_17A.png)

Conventional single-plate ("shear tab") connection: beam W16×50 to a W14×90
column flange.

- **Plate:** PL¼ × 4½ in. wide × 0'-11½" (11½ in. long, ¼ in. thick).
- **Bolts (plate to beam web):** four ¾-in. Group 120 (N), standard holes, one
  vertical line, **3 @ 3 in. = 9 in.**, l_ev = 1¼ in. top/bottom.
- Horizontal: weld line (column face) to bolt line **a = 3 in.**; plate edge to
  bolt line l_eh = 1½ in.; ½-in. setback dimension. 3 in. from top of plate to
  first bolt.
- **Welds:** 3/16-in. fillet, both sides of the plate, to the column flange.
