<!-- chunk_id: J.5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.5",
 "example_family": "J.5",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J3.9",
  "J3.10",
  "J3.8"
 ],
 "eqs": [
  "J3-4",
  "J3-5a",
  "J3-5b"
 ],
 "tables": [],
 "title": "Slip-Critical Bolt Group Under Combined Tension and Shear",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.5 — Slip-Critical Bolt Group Under Combined Tension and Shear",
 "question": "# J.5 — Combined Tension and Shear in a Slip-Critical Connection  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA slip-critical bracket connection uses a group of eight (8) 3/4-in.-diameter Group\n120 high-strength bolts (e.g., ASTM F3125 Grade A325). The connection is loaded by an\ninclined service force whose components are oriented in a 3-4-5 geometry, so that\n4/5 of the resultant acts as direct tension on the bolt group and 3/5 acts as shear.\nThe resultant service force is 15 kips dead load plus 45 kips live load. The faying\nsurfaces are uncoated clean mill scale (Class A, μ = 0.30) with standard holes and a\nsingle slip plane (ns = 1); no fillers are present. Washers are provided per the RCSC\nSpecification. Assume the connected beams and plates are adequate; check only the\nbolt slip resistance (as reduced by the applied tension).\n\nDetermine whether the eight-bolt group has adequate slip resistance under the combined\ntension and shear, for both LRFD and ASD.\n\n## Given\n- Fastener group: 8 × 3/4-in.-dia. Group 120 bolts; standard holes; ns = 1;\n  Tb = 28 kips (Table J3.1); Fnt = 90 ksi; Ab = 0.442 in².\n- Faying surface: Class A, μ = 0.30; Du = 1.13; hf = 1.0.\n- Load: resultant PD = 15 kips, PL = 45 kips, applied so that tension = (4/5)P and\n  shear = (3/5)P on the group.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nWhether the bolt group's available slip resistance (reduced for the applied tension)\nequals or exceeds the required shear (LRFD and ASD); confirm bolt tensile strength.",
 "has_figure": false,
 "stem": "J_5",
 "breadcrumb": "EXAMPLE J.5 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.9 §J3.10 §J3.8 · Slip-Critical Bolt Group Under Combined Tension and Shear",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.5 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.9 §J3.10 §J3.8 · Slip-Critical Bolt Group Under Combined Tension and Shear

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J3.9 (Eq. J3-4) with the applied-tension reduction factor ksc of §J3.10 (Eq. J3-5a LRFD / J3-5b ASD). Standard holes → φ = 1.00, Ω = 1.50. Per the RAG extract provided.

---

### 1. Required Strengths (3-4-5 load split)

Resultant: D = 15 kips, L = 45 kips → **LRFD R = 90.0 kips → Tu = 0.8(90) = 72.0 kips; Vu = 0.6(90) = 54.0 kips**
**ASD R = 60.0 kips → Ta = 48.0 kips; Va = 36.0 kips**

### 2. Slip Resistance Without Applied Tension

Per bolt: Rn = μDuhfTbns = 0.30(1.13)(1.0)(28)(1) = **9.49 kips**; group of 8:

- LRFD: φRn = 8(9.49) = **75.9 kips**; ASD: Rn/Ω = 75.9/1.5 = **50.6 kips**

### 3. Reduction for Applied Tension — Eqs. J3-5a/b

DuTbnb = 1.13(28)(8) = 253 kips

- **LRFD:** ksc = 1 − Tu/(DuTbnb) = 1 − 72.0/253 = **0.715**
- **ASD:** ksc = 1 − 1.5Ta/(DuTbnb) = 1 − 1.5(48.0)/253 = **0.715**

### 4. Reduced Slip Resistance vs. Shear Demand

- **LRFD:** φRn·ksc = 75.9(0.715) = **54.3 kips ≥ Vu = 54.0 ✓** (99.4% utilized)
- **ASD:** (Rn/Ω)·ksc = 50.6(0.715) = **36.2 kips ≥ Va = 36.0 ✓** (99.4%)

Bolt tension itself: 72.0/8 = 9.0 kips ≤ φFntAb = 29.8 kips ✓ (and the §J3.8 bearing-type interaction is satisfied by inspection).

### 5. Conclusion

The eight-bolt slip-critical group **just satisfies** the combined check: the 72-kip tension strips away 28.5% of the clamping force (ksc = 0.715), leaving 54.3 kips of slip resistance against the 54.0-kip shear — **0.6% margin in both LRFD and ASD**. The design is acceptable as posed, but any load increase, surface degradation below Class A, or relaxation losses would cause slip; a ninth bolt or Class B surfaces would be prudent in practice.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
