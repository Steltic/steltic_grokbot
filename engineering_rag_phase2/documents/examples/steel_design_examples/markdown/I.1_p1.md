<!-- chunk_id: I.1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.1",
 "example_family": "I.1",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I3.2a",
  "I3.2d",
  "I8.2a",
  "I3.1c",
  "F2"
 ],
 "eqs": [],
 "tables": [],
 "title": "Composite Interior Floor Beam",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.1 — Composite Interior Floor Beam",
 "question": "# I.1 — Composite Beam Design (W-shape, formed steel deck)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect and check an interior composite floor beam for a typical bay of an office\nbuilding. The beam is simply supported, spans 45 ft, and is spaced 10 ft on center\n(tributary width = 10 ft). A 7½-in.-thick floor consists of 4½ in. of normal-weight\nconcrete on a 3-in.-deep formed steel deck; the deck ribs run perpendicular to the\nbeam. The concrete is normal weight (145 lb/ft³) with f′c = 4 ksi. The steel beam is\nASTM A992 (Fy = 50 ksi) and is **unshored** during construction.\n\nLoads (service, in psf of floor area unless noted):\n- Pre-composite (steel acts alone): slab + deck dead load 75 psf, beam self-weight\n  ≈ 5 psf, construction live load 25 psf.\n- Composite (after the slab cures): superimposed dead load 10 psf (partitions/MEP/\n  finishes) and a non-reducible live load of 100 psf.\n\nConnect the slab to the beam with ¾-in.-diameter steel headed stud anchors\n(Fu = 65 ksi), installed one or two per deck rib, welded through the deck.\n\nDetermine (a) a suitable rolled W-shape, (b) the degree of composite action and the\nrequired total number of stud anchors, (c) the available flexural strength of the\ncomposite section, and (d) verify pre-composite strength and live-load deflection.\n\n## Given\n- Material: steel ASTM A992, Fy = 50 ksi, Fu = 65 ksi; concrete f′c = 4 ksi,\n  normal weight wc = 145 lb/ft³; studs Fu = 65 ksi, ¾-in. dia. (Asa = 0.442 in²).\n- Geometry / span: simple span L = 45 ft; beam spacing 10 ft; slab 7½ in. total\n  (4½ in. solid above a 3-in. deck), ribs perpendicular to beam; unshored.\n- Loads: pre-composite wD from 75 + 5 = 80 psf, construction wL = 25 psf;\n  composite superimposed wD = 10 psf, wL = 100 psf (non-reducible).\n- Member: select a rolled W-shape (design).\n- Code basis: AISC 360-22 (Chapter I composite + Chapter F construction stage),\n  loads per ASCE 7 LRFD/ASD combinations.\n\n## Find\nSelect the W-shape; determine ΣQn (degree of composite action), the PNA location,\nthe required number of ¾-in. studs, the design and allowable composite flexural\nstrength (φbMn and Mn/Ωb) compared with the required moments, and check the bare\nsteel beam for construction loads and the composite live-load deflection.",
 "has_figure": false,
 "stem": "I_1",
 "breadcrumb": "EXAMPLE I.1 · AISC 360-22 Ch.I (composite member) · §I3.2a §I3.2d §I8.2a §I3.1c §F2 · Composite Interior Floor Beam",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.1 · AISC 360-22 Ch.I (composite member) · §I3.2a §I3.2d §I8.2a §I3.1c §F2 · Composite Interior Floor Beam

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter I: §I3.2a (positive flexure, plastic stress distribution; φb = 0.90/Ωb = 1.67), §I3.2d/§I8.2a (stud strength Qn = 0.5Asa√(f′cEc) ≤ RgRpAsaFu), §I3.1c (effective width), §F2 (pre-composite). Per the RAG extract provided.

---

### 1. Loads and Required Strengths (trib. width 10 ft, L = 45 ft, unshored)

**Pre-composite:** w = (75 + 5)(10) = 0.80 kip/ft D; 0.25 kip/ft construction L →
wu = 1.36 kip/ft → **Mu,pre = 344 kip-ft** (ASD 1.05 kip/ft → 266 kip-ft)

**Composite:** w = 0.90 kip/ft D + 1.00 kip/ft L → wu = 2.68 kip/ft → **Mu = 678 kip-ft**; wa = 1.90 → **Ma = 481 kip-ft**

### 2. (a) Beam Selection — **W21x50 (A992)** (As = 14.7 in.², Ix = 984 in.⁴, Zx = 110 in.³)

### 3. (b) Composite Action and Studs

Effective width (§I3.1c): beff = min(2 × 45/8, 10) = 10 ft = 120 in.
Full-composite force: min[AsFy = 735 kips; 0.85f′cbefftc = 0.85(4)(120)(4.5) = 1,840 kips] = 735 kips.

**Partial composite with ΣQn = 386 kips (≈53%)** suffices for strength (below).

Stud strength (3/4-in., NW 4-ksi concrete, deck ⊥, one weak-position stud per rib: Rg = 1.0, Rp = 0.6):
Qn = min[0.5(0.442)√(4 × 3,490) = 26.1; 0.6(0.442)(65) = 17.2] = **17.2 kips/stud**

n = ΣQn/Qn per half-span = 386/17.2 = 22.5 → **23 per half-span; 46 studs total** (one per rib @ 12 in. fits the 45-ft span ✓).

### 4. (c) Composite Flexural Strength

a = ΣQn/(0.85f′cbeff) = 386/408 = 0.95 in.; PNA in the steel flange; plastic stress distribution gives

**φbMn = 769 kip-ft ≥ Mu = 678 kip-ft ✓ (LRFD, 88%)**; Mn/Ωb = 512 kip-ft ≥ 481 kip-ft ✓ (ASD, 94%)

### 5. (d) Pre-Composite Strength and Deflections

- Bare W21x50 (top flange braced by the deck, ribs ⊥): φMn = φFyZx = **413 kip-ft ≥ 344 ✓** (ASD 274 ≥ 266 ✓)
- Pre-composite (wet-concrete) deflection: Δ = 5wL⁴/(384EIx) = **2.6 in.** → **camber ≈ 2 in.** (or accept with finish allowance)
- Live-load deflection on the lower-bound composite inertia (ILB ≈ 2,500 in.⁴, Manual Table 3-20 basis): Δ_LL ≈ **1.3 in. ≈ L/420 ≤ L/360 ✓**

### 6. Conclusion

**Use a W21x50 (A992) with 46 — 3/4-in. headed studs (one per rib, ΣQn = 386 kips ≈ 53% composite) and ≈2 in. of camber.** The composite section provides φbMn = 769 kip-ft against 678 kip-ft (LRFD), the bare beam carries the unshored construction condition, and live-load deflection satisfies L/360. ASD checks pass concurrently (94% flexure).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
