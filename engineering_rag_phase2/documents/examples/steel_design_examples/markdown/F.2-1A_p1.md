<!-- chunk_id: F.2-1A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.2-1A",
 "example_family": "F.2-1",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F2",
  "F1"
 ],
 "eqs": [
  "F2-1"
 ],
 "tables": [],
 "title": "Channel Flexural Member Design, Continuously Braced",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.2-1A — Channel Flexural Member Design, Continuously Braced",
 "question": "# F.2-1A — Compact channel flexural member, continuously braced (design)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported roof edge beam spans 25 ft. It carries a uniform service dead load\nof 0.23 kip/ft and a uniform service live load of 0.69 kip/ft (the dead load already\nincludes an allowance for the beam self-weight). The compression flange is continuously\nbraced against lateral-torsional buckling by the roof construction along the full length.\n\nSelect the lightest American Standard channel (C-shape) of ASTM A992/A992M steel\n(Fy = 50 ksi) that satisfies the AISC 360 flexural strength requirement in both LRFD and\nASD, and verify that the live-load deflection at midspan does not exceed L/360.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi, E = 29,000 ksi.\n- Geometry / span: simply supported, L = 25 ft; compression flange continuously braced (Lb = 0).\n- Loads (service, uniform): wD = 0.23 kip/ft, wL = 0.69 kip/ft.\n- Member / section: to be selected (a channel, C-shape).\n- Serviceability: live-load deflection limited to L/360.\n- Code basis: AISC 360-22 (Chapter F); ASCE/SEI 7 load combinations.\n\n## Find\nSelect a channel that provides adequate available flexural strength (LRFD and ASD) and\nsatisfies the L/360 live-load deflection limit.",
 "has_figure": false,
 "stem": "F_2_1A",
 "breadcrumb": "EXAMPLE F.2-1A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · Channel Flexural Member Design, Continuously Braced",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.2-1A · AISC 360-22 Ch.F (beam flexure) · §F2 §F1 · Channel Flexural Member Design, Continuously Braced

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F2 (Eq. F2-1; channels bent about their major axis; LTB precluded by continuous bracing). φb = 0.90, Ωb = 1.67 (§F1). Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 25 ft; wD = 0.23 kip/ft, wL = 0.69 kip/ft:

- **LRFD:** wu = 1.2(0.23) + 1.6(0.69) = 1.38 kip/ft → Mu = 1.38(25)²/8 = **108 kip-ft**
- **ASD:** wa = 0.92 kip/ft → Ma = 0.92(25)²/8 = **71.9 kip-ft**

### 2. Serviceability Requirement

Δ_LL ≤ L/360 = 25(12)/360 = 0.833 in. → I_req = 5wL L⁴/(384EΔ) = 5(0.69/12)(300)⁴/[384(29,000)(0.833)] = **251 in.⁴**

### 3. Selection — C15x33.9 (A992)

Zx = 50.8 in.³; Ix = 315 in.⁴. Compact channel; §F2 applies; continuous bracing → yielding governs.

### 4. Flexural Strength — Eq. F2-1

Mn = Mp = FyZx = 50(50.8) = 2,540 kip-in. = **212 kip-ft**

- **LRFD:** φbMn = 0.90(212) = **190 kip-ft** ≥ 108 kip-ft ✓ (utilization 0.57)
- **ASD:** Mn/Ωb = 212/1.67 = **127 kip-ft** ≥ 71.9 kip-ft ✓ (utilization 0.57)

### 5. Deflection Check

Ix = 315 in.⁴ ≥ 251 in.⁴ → Δ_LL = 0.833(251/315) = **0.66 in. ≤ 0.833 in. ✓**

(The next lighter channel family, C12x30 with Ix = 162 in.⁴, fails the deflection requirement.)

### 6. Conclusion

**Select C15x33.9 (ASTM A992).** With the compression flange continuously braced, the channel reaches its full plastic moment (Eq. F2-1): φbMn = 190 kip-ft (LRFD) and Mn/Ωb = 127 kip-ft (ASD), well above the required 108 / 71.9 kip-ft. The live-load deflection criterion (I ≥ 251 in.⁴), not strength, dictates the C15 depth.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
