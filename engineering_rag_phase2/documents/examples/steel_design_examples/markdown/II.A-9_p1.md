<!-- chunk_id: II.A-9_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-9",
 "example_family": "II.A-9",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "J3.7",
  "J3.11a"
 ],
 "eqs": [
  "J3-6a"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Offset Double-Angle Connections with a Shared Bolt Column",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-9 — Offset Double-Angle Connections with a Shared Bolt Column",
 "question": "# II.A-9 — Offset All-Bolted Double-Angle Connections (Beams-to-Girder Web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nTwo ASTM A992/A992M W16×45 floor beams frame into opposite faces of the web of an\nASTM A992/A992M W18×50 girder, back to back, each through a bolted double-angle\n(2L5×3½×¼, short legs back-to-back) shear connection. The two beam center lines are\noffset 6 in. along the girder, so the two connections overlap and share one common\nvertical row (column) of bolts that passes through the girder web. Each angle leg at\nthe girder has three bolt rows (vertical pitch 3 in.) in two vertical columns, using\n¾-in.-diameter Group 120 (e.g., A325) bolts, thread condition N (threads not excluded\nfrom the shear plane), in standard holes. The girder web thickness is t_w = 0.355 in.;\nthe W16×45 beam web is t_w = 0.345 in. The geometry is shown in figures/IIA_9.png.\n\nEach beam delivers a service dead-load reaction R_D = 10 kips and a service live-load\nreaction R_L = 30 kips to the girder. Because the offset (6 in.) is essentially equal\nto the bolt gage on the support, the eccentricity of the shared row is negligible and\nthe bolts may be treated as concentrically loaded.\n\nThe strength of the angles themselves (shear yielding, shear rupture, block shear) is\nthe same as in the companion 2L5×3½×¼ connection and is not re-checked here; the issue\ncreated by the offset is that the **shared middle column of bolts carries a share of\nthe reaction from BOTH beams simultaneously**. Verify that this most heavily loaded\nbolt is adequate.\n\n## Given\n- Material: beams and girder ASTM A992/A992M (F_y = 50 ksi, F_u = 65 ksi); angles\n  ASTM A572/A572M Grade 50 (F_y = 50 ksi, F_u = 65 ksi).\n- Members: beams W16×45 (t_w = 0.345 in.); girder W18×50 (t_w = 0.355 in.).\n- Connection: 2L5×3½×¼ SLBB, three rows at 3-in. pitch, two columns of bolts.\n- Fasteners: ¾-in.-dia. Group 120, thread condition N, standard holes\n  (d_h = 13/16 in.); A_b = 0.442 in.²\n- Loads (each beam, service): R_D = 10 kips, R_L = 30 kips.\n- Offset between the two beam connections: 6 in. (≈ support gage, so treated as\n  concentric).\n- Code basis: AISC 360-22 (load combinations from ASCE/SEI 7).\n\n## Find\nThe available shear strength of the most heavily loaded (shared, middle-column) bolt\nat the girder web — limit states of bolt shear (J3.7) and bearing/tearout on the\ngirder web (J3.11) — and confirm it exceeds the required per-bolt force produced by\nboth beam reactions acting together.",
 "has_figure": true,
 "stem": "II_A_9",
 "breadcrumb": "EXAMPLE II.A-9 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a · Offset Double-Angle Connections with a Shared Bolt Column",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-9 · AISC 360-22 II.A (simple / shear connection) · §J3.7 §J3.11a · Offset Double-Angle Connections with a Shared Bolt Column

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2 (bolt shear), §J3.11a (bearing, Eq. J3-6a). The 6-in. offset ≈ support gage → shared-column eccentricity negligible (concentric treatment per the problem statement). Per the RAG extract provided.

---

### 1. Required Strengths

Each W16x45 beam: R: D = 10 kips, L = 30 kips → **LRFD Ru = 60.0 kips; ASD Ra = 40.0 kips per beam**

Each connection: 2L5x3-1/2x1/4 with six 3/4-in. Group 120-N bolts (3 rows × 2 columns) through the W18x50 girder web (tw = 0.355 in.); the two connections overlap so the **middle column of three bolts is shared** — those bolts receive load from both beams simultaneously, one connection on each shear plane.

### 2. Shared-Bolt Demands

Per connection, per bolt: 60.0/6 = **10.0 kips (LRFD)** / 6.67 kips (ASD).

A shared bolt is in double shear with one beam's angles bearing on each side:
- Shear per plane: 10.0 kips (LRFD) / 6.67 kips (ASD)
- Bearing on the girder web: the planes are **additive**: 10.0 + 10.0 = 20.0 kips (LRFD) / 13.3 kips (ASD)

### 3. Available Strengths

**Bolt shear (per plane):** φrn = 0.75(54)(0.442) = **17.9 kips ≥ 10.0 ✓** (ASD 11.9 ≥ 6.67 ✓)
(Total double-shear capacity 35.8 kips ≥ 20.0 combined ✓)

**Bearing on the girder web (Eq. J3-6a, deformation considered):**
φrn = 0.75(2.4)(0.75)(0.355)(65) = **31.1 kips ≥ 20.0 ✓** (ASD 20.7 ≥ 13.3 ✓)
Tearout: interior spacing lc = 3 − 13/16 = 2.19 in. → 1.2lctFu = 60.6 kips ≫ — not critical.

**Bearing on the angles (each side, t = 1/4 in.):** φrn = 21.9 kips ≥ 10.0 per plane ✓.

### 4. Conclusion

The most heavily loaded (shared) bolts are **adequate**: each shear plane works at 56% of the bolt's single-plane strength, and the critical combined check — **bearing on the 0.355-in. girder web under the sum of both beams' per-bolt forces (20.0 vs. 31.1 kips LRFD)** — is at 64% utilization. The offset detail is therefore acceptable without enlarging the shared bolts, provided the angle limit states (verified in the companion example) remain unchanged. Where offsets differ from the gage, the shared-column eccentricity must be re-examined.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-9 (from figures/IIA_9.png)

Two W16×45 beams frame into opposite faces of a W18×50 girder web, back to back,
their centerlines **offset D = 6 in.** along the girder. Each delivers
R_D = 10 kips, R_L = 30 kips. Connection angles 2L5×3½×¼ SLBB; ¾-in. Group 120 (N)
bolts, SSL holes in the angles and STD holes in the beam web.

- **Section E-E (each beam):** top-flange cope length **c = 4½ in.** (depth d_c),
  l_ev = 1¼ in., **2 @ 3 in. = 6 in.** (three rows), ½-in. setback.
- **Each girder-attached angle leg has the bolts in two vertical columns**; because
  the two beams are offset by 6 in., the two connections **overlap and share one
  common middle vertical column of bolts** through the girder web (see the plan and
  Section F-F, with vertical spacing 4 in. typ. and offset D = 6 in.).
- The shared middle column of bolts carries load from **both** beams; that most
  heavily loaded bolt is the one verified.
