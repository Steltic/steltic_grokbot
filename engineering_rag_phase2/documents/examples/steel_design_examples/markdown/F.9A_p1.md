<!-- chunk_id: F.9A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.9A",
 "example_family": "F.9",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F8",
  "F8.1"
 ],
 "eqs": [
  "F8-1"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "Pipe Flexural Member, 8-in. Nominal (Selection)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.9A — Pipe Flexural Member, 8-in. Nominal (Selection)",
 "question": "# F.9A — Pipe (round HSS) beam selection  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nSelect a Pipe shape with an 8-in. nominal diameter for a simply supported, single-span\nbeam carrying a uniformly distributed load. The beam is braced at the end points only and\nthere is no deflection limit. Determine an adequate Pipe section and confirm its available\nflexural strength (LRFD and ASD).\n\n## Given\n- Material: ASTM A53/A53M Grade B (Fy = 35 ksi, E = 29,000 ksi).\n- Geometry / span: simply supported, L = 16 ft, braced at the ends only.\n- Loads (service, uniformly distributed): dead wD = 0.32 kip/ft, live wL = 0.96 kip/ft.\n- Serviceability: no deflection limit.\n- Member / section: to be selected (8-in. nominal Pipe).\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nSelect an adequate 8-in. nominal Pipe and report the governing limit state with φ_b M_n\n(LRFD) and M_n/Ω_b (ASD).",
 "has_figure": false,
 "stem": "F_9A",
 "breadcrumb": "EXAMPLE F.9A · AISC 360-22 Ch.F (beam flexure) · §F8 §F8.1 · Pipe Flexural Member, 8-in. Nominal (Selection)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.9A · AISC 360-22 Ch.F (beam flexure) · §F8 §F8.1 · Pipe Flexural Member, 8-in. Nominal (Selection)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §F8 (Round HSS): Eq. F8-1 (yielding; compact wall); Table B4.1b Case 20. LTB is not a limit state for round shapes. φb = 0.90, Ωb = 1.67. Per the RAG extract provided.

---

### 1. Required Strength

Simple span L = 16 ft, braced at ends only (no penalty — round section); wD = 0.32 kip/ft, wL = 0.96 kip/ft:

- **LRFD:** wu = 1.2(0.32) + 1.6(0.96) = 1.92 kip/ft → Mu = 1.92(16)²/8 = **61.4 kip-ft**
- **ASD:** wa = 1.28 kip/ft → Ma = **41.0 kip-ft**

### 2. Selection — Pipe 8 x-Strong (A53 Gr. B, Fy = 35 ksi)

Z = 31.0 in.³; D/t = 18.5. (The standard-weight Pipe 8 Std, Z = 22.2 in.³, gives φbMn = 58.3 kip-ft < 61.4 — inadequate, so the extra-strong wall is required.)

### 3. Wall Classification — Table B4.1b, Case 20

λp = 0.07E/Fy = 0.07(29,000)/35 = **58.0**

D/t = 18.5 ≤ 58.0 → **compact**; no local-buckling reduction; §F8.1 yielding governs.

### 4. Flexural Strength — Eq. F8-1

Mn = Mp = FyZ = 35(31.0) = 1,090 kip-in. = **90.4 kip-ft**

- **LRFD:** φbMn = 0.90(90.4) = **81.4 kip-ft** ≥ 61.4 kip-ft ✓ (utilization 0.75)
- **ASD:** Mn/Ωb = 90.4/1.67 = **54.1 kip-ft** ≥ 41.0 kip-ft ✓ (utilization 0.76)

### 5. Conclusion

**Select Pipe 8 x-Strong (A53 Gr. B).** The compact round section reaches its plastic moment (Eq. F8-1, governing limit state: **yielding**); lateral-torsional buckling does not apply to round members, so ends-only bracing is irrelevant. Available strengths of 81.4 kip-ft (LRFD) and 54.1 kip-ft (ASD) exceed the required 61.4 / 41.0 kip-ft with ~25% reserve.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
