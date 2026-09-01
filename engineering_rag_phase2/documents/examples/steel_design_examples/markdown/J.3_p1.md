<!-- chunk_id: J.3_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.3",
 "example_family": "J.3",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J3.7",
  "J3.8"
 ],
 "eqs": [
  "J3-2"
 ],
 "tables": [
  "J3.2"
 ],
 "title": "Bolt Under Combined Tension and Shear (Bearing-Type)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.3 — Bolt Under Combined Tension and Shear (Bearing-Type)",
 "question": "# J.3 — Combined Tension and Shear in a Bearing-Type Connection  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA single 3/4-in.-diameter high-strength bolt (Group 120, e.g., ASTM F3125 Grade A325)\nin a bearing-type connection is subjected simultaneously to tension and shear. The\nthreads are NOT excluded from the shear plane (thread condition N). The applied\nservice loads on the bolt are: an axial tension of 3.5 kips dead load plus 12 kips\nlive load, and a shear of 1.33 kips dead load plus 4 kips live load.\n\nDetermine whether the bolt is adequate for the combined tension and shear, checking\nthe available shear stress and the available tensile strength modified for the\npresence of shear, for both LRFD and ASD.\n\n## Given\n- Fastener: 3/4-in.-dia. Group 120 high-strength bolt, threads not excluded (N);\n  nominal unthreaded body area Ab = 0.442 in².\n- Loads (per bolt): tension TD = 3.5 kips, TL = 12 kips; shear VD = 1.33 kips,\n  VL = 4 kips.\n- Connection type: bearing-type.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nWhether the bolt has adequate available tensile strength under the combined tension\nand shear (LRFD and ASD).",
 "has_figure": false,
 "stem": "J_3",
 "breadcrumb": "EXAMPLE J.3 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.7 §J3.8 · Bolt Under Combined Tension and Shear (Bearing-Type)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.3 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.7 §J3.8 · Bolt Under Combined Tension and Shear (Bearing-Type)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J3.7/Table J3.2 (Fnt = 90 ksi, Fnv = 54 ksi for Group 120-N) and §J3.8 (Eq. J3-2: F′nt = 1.3Fnt − (Fnt/φFnv)frv ≤ Fnt; φ = 0.75, Ω = 2.00). Per the RAG extract provided.

---

### 1. Required Strengths (per bolt; Ab = 0.442 in.²)

- **LRFD:** Tu = 1.2(3.5) + 1.6(12) = **23.4 kips**; Vu = 1.2(1.33) + 1.6(4) = **8.00 kips** → frv = 8.00/0.442 = 18.1 ksi
- **ASD:** Ta = **15.5 kips**; Va = **5.33 kips** → frv = 12.1 ksi

### 2. Shear Check and Interaction Trigger

φFnv = 0.75(54) = 40.5 ksi ≥ frv = 18.1 ✓ (ASD: Fnv/Ω = 27.0 ≥ 12.1 ✓)

frv/(φFnv) = 18.1/40.5 = **0.45 > 0.30** → the combined-stress reduction of §J3.8 must be applied (User Note threshold exceeded).

### 3. Modified Tensile Stress — Eq. J3-2

- **LRFD:** F′nt = 1.3(90) − (90/40.5)(18.1) = 117 − 40.2 = **76.8 ksi** ≤ 90 ✓
- **ASD:** F′nt = 1.3(90) − (2.00 × 90/54)(12.1) = 117 − 40.2 = **76.8 ksi** ≤ 90 ✓

### 4. Available Tensile Strength

- **LRFD:** φRn = 0.75(76.8)(0.442) = **25.5 kips ≥ 23.4 ✓** (utilization 0.92)
- **ASD:** Rn/Ω = 76.8(0.442)/2.00 = **17.0 kips ≥ 15.5 ✓** (utilization 0.91)

### 5. Conclusion

The single 3/4-in. Group 120-N bolt is **adequate for the simultaneous 23.4-kip tension and 8.0-kip shear (LRFD)** and 15.5/5.33 kips (ASD). The shear stress at 45% of the available value reduces the usable tensile stress from 90 to 76.8 ksi (a 15% penalty), leaving ~8–9% margin. Without the §J3.8 interaction the bolt would appear to have 28% margin — the combined check is essential at this shear level.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
