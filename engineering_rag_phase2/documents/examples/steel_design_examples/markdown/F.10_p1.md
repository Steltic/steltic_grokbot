<!-- chunk_id: F.10_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.10",
 "example_family": "F.10",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F9",
  "F9.1",
  "F9.3"
 ],
 "eqs": [
  "F9-1",
  "F9-2",
  "F9-3",
  "F9-14"
 ],
 "tables": [],
 "title": "WT-Shape (Tee) Flexural Member",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.10 — WT-Shape (Tee) Flexural Member",
 "question": "# F.10 — WT-shape (tee) flexural member  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nUsing the AISC Specification directly, select a WT beam with a 5-in. nominal depth for a\nsimply supported, single-span beam carrying a uniformly distributed load. The beam is\n**continuously braced**, has no deflection limit, and is oriented so that the **toe of the\nstem is in tension** (flange in compression). Determine an adequate WT, identify the\ngoverning flexural limit state, and report φ_b M_n (LRFD) and M_n/Ω_b (ASD).\n\n## Given\n- Material: ASTM A992/A992M (Fy = 50 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, L = 6 ft, continuously braced; stem toe in tension.\n- Loads (service, uniformly distributed): dead wD = 0.08 kip/ft, live wL = 0.24 kip/ft.\n- Member / section: to be selected (5-in. nominal WT).\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nSelect an adequate WT5 and report the governing limit state with φ_b M_n (LRFD) and\nM_n/Ω_b (ASD).",
 "has_figure": false,
 "stem": "F_10",
 "breadcrumb": "EXAMPLE F.10 · AISC 360-22 Ch.F (beam flexure) · §F9 §F9.1 §F9.3 · WT-Shape (Tee) Flexural Member",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.10 · AISC 360-22 Ch.F (beam flexure) · §F9 §F9.1 §F9.3 · WT-Shape (Tee) Flexural Member

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F9 (Tees Loaded in the Plane of Symmetry): Eqs. F9-1, F9-2, F9-3, F9-14. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 6 ft, uniform load; wD = 0.08 kip/ft, wL = 0.24 kip/ft:

- **LRFD:** wu = 1.2(0.08) + 1.6(0.24) = 0.480 kip/ft → Mu = 0.480(6)²/8 = **2.16 kip-ft** (25.9 kip-in.)
- **ASD:** wa = 0.32 kip/ft → Ma = 0.32(6)²/8 = **1.44 kip-ft** (17.3 kip-in.)

### 2. Trial Section — WT5x6 (A992, lightest WT5)

Sx = 1.22 in.³ (to stem tip); Zx = 2.20 in.³; bf = 3.96 in.; tf = 0.210 in.; Ix = 4.35 in.⁴; ȳ = 1.36 in.

Configuration: **continuously braced, flange in compression / stem toe in tension** → lateral-torsional buckling does not apply; check yielding (F9.1) and flange local buckling (F9.3).

### 3. Yielding — §F9.1

For tee stems in tension (Eq. F9-2):

> Mn = Mp = FyZx ≤ 1.6My, with My = FySx (Eq. F9-3)

FyZx = 50(2.20) = 110 kip-in.; 1.6My = 1.6(50)(1.22) = 97.6 kip-in. ← cap governs

**Mn = 97.6 kip-in. = 8.13 kip-ft**

### 4. Flange Local Buckling — §F9.3

λ = bf/2tf = 3.96/[2(0.210)] = 9.43; λpf = 0.38√(E/Fy) = 9.15; λrf = 1.0√(E/Fy) = 24.1 → noncompact flange → Eq. F9-14:

Sxc (to compression flange) = Ix/ȳ = 4.35/1.36 = 3.20 in.³; 0.7FySxc = 112 kip-in. ≥ Mp = 110 kip-in., so Eq. F9-14 returns ≈ Mp and is capped at 1.6My = 97.6 kip-in. → **FLB does not govern below the yield cap.**

### 5. Available Flexural Strength

Governing limit state: **yielding (1.6My cap of Eq. F9-2)**, Mn = 97.6 kip-in.

- **LRFD:** φbMn = 0.90(97.6) = 87.8 kip-in. = **7.32 kip-ft** ≥ 2.16 kip-ft ✓
- **ASD:** Mn/Ωb = 97.6/1.67 = 58.4 kip-in. = **4.87 kip-ft** ≥ 1.44 kip-ft ✓

### 6. Conclusion

**Select WT5x6 (A992).** With continuous bracing and the stem toe in tension, the governing limit state is **tensile-stem yielding limited by the 1.6My cap** of Eq. F9-2 (Mn = 97.6 kip-in.); LTB is excluded by bracing and flange local buckling does not control. Available strengths of 7.32 kip-ft (LRFD) and 4.87 kip-ft (ASD) far exceed the required 2.16 / 1.44 kip-ft, so the lightest 5-in. WT is adequate.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
