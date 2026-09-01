<!-- chunk_id: I.2_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.2",
 "example_family": "I.2",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I3.1c",
  "I3.2a",
  "I8.2a",
  "F2"
 ],
 "eqs": [],
 "tables": [],
 "title": "Composite Floor Girder with Third-Point Loads",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.2 — Composite Floor Girder with Third-Point Loads",
 "question": "# I.2 — Composite Girder Design (W-shape, formed deck, partial composite)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA typical interior girder in a composite floor system spans **L = 30 ft** between\ncolumn supports and is part of a framing grid spaced **45 ft** on center (girder to\ngirder). Filler beams frame into the girder at the **third points** (10 ft on center),\ndelivering equal concentrated loads; the girder also carries its own self-weight as a\nuniform load. The girder is **not shored** during construction.\n\nThe floor consists of **normal-weight concrete** (unit weight 145 lb/ft³, specified\ncompressive strength f′c = 4 ksi) on **3-in. formed steel deck**, with **4½ in. of\nconcrete above the top of the deck** (total slab depth Y_con = 7.5 in.). The deck ribs\nrun **parallel** to the girder; average rib width w_r = 6 in. Connection is by\n**¾-in.-diameter steel headed stud anchors** (ASTM A29, F_u = 65 ksi) welded directly\nto the girder flange.\n\nSelect an appropriate **ASTM A992 (F_y = 50 ksi)** rolled W-shape girder and determine\nthe required number of stud anchors, using **LRFD**. Design the girder for the\npre-composite (construction) condition and for the final composite condition, and\nsize the studs for the required horizontal shear. (Also note the ASD result.)\n\n## Given\n- Material: girder ASTM A992, F_y = 50 ksi, E = 29,000 ksi; studs ASTM A29, F_u = 65 ksi.\n- Geometry / span: simple span L = 30 ft; girder spacing 45 ft; filler beams at third\n  points (concentrated loads at 10 ft and 20 ft); slab Y_con = 7.5 in. (4½ in. of NW\n  concrete over 3-in. deck), f′c = 4 ksi, w_c = 145 lb/ft³; deck parallel to girder, w_r = 6 in.\n- Loads (service):\n  - Pre-composite dead: slab 75 lb/ft², girder self-weight (~80 lb/ft trial), filler\n    beams 50 lb/ft (from the supported-beam design).\n  - Pre-composite live (construction): 25 lb/ft².\n  - Composite (post-cure) dead: 10 lb/ft² (MEP/ceiling/finishes).\n  - Composite live: 100 lb/ft² (non-reducible, assembly occupancy).\n  - Tributary width to the girder for the filler-beam point loads = 45 ft (beam span).\n- Member / section: select a rolled W-shape (design problem).\n- Code basis: AISC 360-22 Chapter I (composite members); ASCE/SEI 7 load combinations.\n\n## Find\n1. A rolled W-shape adequate for the pre-composite (construction) flexural demand,\n   with a camber recommendation.\n2. The effective slab width and the available composite flexural strength\n   (plastic stress distribution), confirming the required composite percentage.\n3. The stud-anchor shear strength Q_n, and the number of ¾-in. studs required.",
 "has_figure": false,
 "stem": "I_2",
 "breadcrumb": "EXAMPLE I.2 · AISC 360-22 Ch.I (composite member) · §I3.1c §I3.2a §I8.2a §F2 · Composite Floor Girder with Third-Point Loads",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.2 · AISC 360-22 Ch.I (composite member) · §I3.1c §I3.2a §I8.2a §F2 · Composite Floor Girder with Third-Point Loads

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter I: §I3.1c/§I3.2a (composite flexure), §I8.2a (studs welded directly to the flange, deck parallel), §F2 (pre-composite LTB with Lb = 10 ft). LRFD primary; ASD noted. Per the RAG extract provided.

---

### 1. Loads (filler beams at third points; 45-ft tributary each side)

Per third point: PD = (90 psf)(10)(45)/1,000 = 40.5 kips; PL = (100 psf)(10)(45)/1,000 = 45.0 kips
Pre-composite: PD,pre = 33.8 kips (slab + deck + beams); PCL = 22.5 kips (25 psf construction)

- **Pre-composite:** Pu = 1.2(33.8) + 1.6(22.5) = 76.5 kips → Mu,pre = 76.5(10) + Mself ≈ **776 kip-ft**
- **Composite:** Pu = 1.2(40.5) + 1.6(45.0) = 121 kips → **Mu ≈ 1,220 kip-ft** (ASD: Pa = 85.5 → Ma ≈ 864 kip-ft)

### 2. Pre-Composite (Unshored) Selection — governs the shape

The parallel deck does not brace the girder; Lb = 10 ft between filler beams, center segment Cb ≈ 1.0:

- W24x76: φMn(Lb = 10 ft) ≈ 677 kip-ft < 776 ✗; W24x84: ≈ 764 kip-ft < 776 ✗
- **W24x94 (Zx = 254 in.³, Sx = 222 in.³, Lp = 7.5 ft, Lr = 21.7 ft): φMn = 886 kip-ft ≥ 776 ✓** (ASD 590 ≥ 561 ✓)

**Select W24x94 (A992)** — the unshored construction stage, not the composite stage, sizes this girder. (Alternatives: shore the girder, or add temporary bracing and use a W24x84.)

### 3. Composite Condition

beff = min(2 × 30/8, 45) = 7.5 ft = 90 in. Full-composite force = min[AsFy = 27.7(50) = 1,390; 0.85(4)(90)(4.5) = 1,380] ≈ 1,380 kips.

With **ΣQn ≈ 700 kips (≈50% composite)**: a = 2.3 in.; φbMn ≈ **1,490 kip-ft ≥ 1,220 ✓** (ASD ≈ 991 ≥ 864 ✓)

### 4. Stud Anchors (3/4-in., welded directly to the flange; deck parallel, wr/hr = 2 ≥ 1.5 → Rg = 1.0, Rp = 0.75)

Qn = min[0.5(0.442)√(4 × 3,490) = 26.1; 0.75(0.442)(65) = 21.5] = **21.5 kips/stud**

Studs are required between each support and the adjacent third point (the shear spans): n = 700/21.5 = 32.6 → **34 studs each end region (68 total)**, placed in pairs at ≈7-in. spacing to respect the 4d minimum longitudinal spacing; nominal studs only in the center third.

### 5. Conclusion

**Use a W24x94 (A992) girder with 68 — 3/4-in. studs (34 per end shear span, ΣQn ≈ 700 kips ≈ 50% composite).** The design is controlled by the **unshored pre-composite condition** (Lb = 10 ft LTB, 88% utilized); the composite section then carries the 1,220 kip-ft factored moment at only ~82%. ASD checks pass concurrently. Camber on the order of 1 in. offsets the wet-concrete deflection.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
