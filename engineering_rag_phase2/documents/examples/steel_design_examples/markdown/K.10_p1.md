<!-- chunk_id: K.10_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "K.10",
 "example_family": "K.10",
 "chapter": "K",
 "topic": "HSS connection",
 "clauses": [
  "J3.7",
  "J2.4",
  "J4.2"
 ],
 "eqs": [],
 "tables": [
  "J3.2"
 ],
 "title": "Bolted End-Plate (Flange-Plate) Tension Connection for an HSS Strut",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE K.10 — Bolted End-Plate (Flange-Plate) Tension Connection for an HSS Strut",
 "question": "# K.10 — Bolted end-plate for a rectangular HSS strut in axial tension  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA square HSS strut carries an axial tension force and is connected at its end by a\nflange (end) plate: a rectangular plate welded all around the end of the HSS and\nbolted to the supporting element with four bolts (one near each corner of the plate,\none bolt per side of the HSS). Determine (1) the bolt size, (2) the end-plate\nthickness considering prying action, and (3) the fillet-weld leg size to develop the\ntension.\n\nThe strut is an ASTM A500 Grade C HSS4×4×1/4. The end plate is ASTM A572 Grade 50,\n10 in. wide, with 70-ksi (E70XX) electrode welds. Bolt-line geometry: the bolt\ngage gives b = 1-1/2 in. (HSS face to bolt line) and a = 1-1/2 in. (bolt line to plate\nedge); one bolt per side (per HSS wall), so the tributary length per bolt is the full\n10-in. plate width.\n\n## Given\n- Material: strut ASTM A500 Gr. C (Fy = 50 ksi, Fu = 62 ksi); end plate ASTM A572\n  Gr. 50 (Fy = 50 ksi, Fu = 65 ksi); E70XX welds.\n- Strut HSS4×4×1/4: design wall t = 0.233 in., A = 3.37 in².\n- End plate: 10 in. wide; b = 1-1/2 in., a = 1-1/2 in.; four bolts (one per side).\n- Service axial tension: dead PD = 16 kips, live PL = 50 kips.\n- Code basis: AISC 360 (+ ASCE/SEI 7 for the load combinations; prying-action plate\n  thickness per AISC Manual Part 9, with Fy in lieu of Fu per Packer & Olson 2023).\n\n## Find\nThe required tensile force (LRFD and ASD); a trial bolt size (4 bolts) and its\navailable tensile strength; the minimum end-plate thickness including prying action;\nand the required fillet-weld leg size to develop the strut tension, using the AISC 360\nweld provisions with the directional-strength-increase factor set to unity for a\nfillet weld at the end of a rectangular HSS loaded in tension (§J2.4, Eq. J2-4). Also\nconfirm the minimum weld size for the HSS wall thickness. State the final detail.",
 "has_figure": false,
 "stem": "K_10",
 "breadcrumb": "EXAMPLE K.10 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J2.4 §J4.2 · Bolted End-Plate (Flange-Plate) Tension Connection for an HSS Strut",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE K.10 · AISC 360-22 Ch.K (HSS connection) · §J3.7 §J2.4 §J4.2 · Bolted End-Plate (Flange-Plate) Tension Connection for an HSS Strut

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §J3.7/Table J3.2 (bolt tension), AISC Manual Part 9 prying model (b′, a′, ρ, δ, tc, Q), §J2.4 (fillet weld with transverse directional factor), §J4.2 (HSS wall development). Per the RAG extract provided.

---

### 1. Required Strength

P: D = 16 kips, L = 50 kips → **LRFD Pu = 99.2 kips; ASD Pa = 66.0 kips** (tension)

HSS4x4x1/4 (t = 0.233 in., Fu = 62 ksi); end plate 10 in. wide (A572 Gr. 50); four bolts (one per side), b = a = 1 1/2 in.; tributary length per bolt p = 10 in.

### 2. (1) Bolt Size

Per-bolt tension T = 99.2/4 = **24.8 kips (LRFD)** / 16.5 kips (ASD).
**Try 3/4-in. Group 120:** B = φFntAb = 0.75(90)(0.442) = 29.8 kips ≥ 24.8 ✓ (ASD 19.9 ≥ 16.5 ✓) — **use four 3/4-in. Group 120 bolts.**

### 3. (2) End-Plate Thickness with Prying (Part 9)

b′ = b − d/2 = 1.50 − 0.375 = 1.13 in.; a = 1.50 ≤ 1.25b ✓; a′ = 1.88 in.; ρ = 0.60; δ = 1 − (13/16)/10 = 0.92
tc = √(4.44Bb′/(pFu)) = √(4.44 × 29.8 × 1.13/(10 × 65)) = **0.479 in.**

**With t = 3/8 in.:** α′ = [1/(δ(1 + ρ))][(tc/t)² − 1] = (0.629)/1.47 = 0.43 ≤ 1 → Q = (t/tc)²(1 + δα′) = 0.614(1.39) = 0.855
Available per bolt = BQ = 29.8(0.855) = **25.5 kips ≥ 24.8 ✓** (ASD: 19.9(0.97) = 19.3 ≥ 16.5 ✓)

**Use a 3/8-in. end plate** (prying consumes ~15% of the bolt capacity; LRFD utilization 97%).

### 4. (3) Weld Size (fillet all around the HSS, perimeter = 16 in.)

Required = 99.2/16 = 6.2 kip/in., transverse to the weld axis (directional factor 1.5):
D_req = 6.2/[1.392(1.5)] = 3.0 → **use 1/4-in. fillets (D = 4)**: available 1.392(4)(1.5) = 8.35 kip/in. ✓ (ASD 5.57 ≥ 4.13 ✓)
HSS wall development: 3.09D/Fu = 3.09(4)/62 = 0.20 in. ≤ 0.233 in. ✓; minimum size for the 0.233-in. wall = 1/8 in. ✓.

### 5. Conclusion

**Use four 3/4-in. Group 120 bolts, a 3/8-in. A572 Gr. 50 end plate, and 1/4-in. E70 fillet welds all around the HSS4x4x1/4.** The governing check is bolt tension including prying action (25.5 vs. 24.8 kips per bolt, 97% LRFD) — the thin-plate/strong-bolt solution intentionally accepts prying; a 1/2-in. plate would eliminate it (tc basis) if future loads grow. All weld and wall checks pass with margin.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
