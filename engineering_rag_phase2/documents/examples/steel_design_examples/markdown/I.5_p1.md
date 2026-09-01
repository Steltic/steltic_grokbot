<!-- chunk_id: I.5_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.5",
 "example_family": "I.5",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I2.2",
  "I6"
 ],
 "eqs": [],
 "tables": [],
 "title": "Filled Composite Member in Axial Tension (Uplift)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.5 — Filled Composite Member in Axial Tension (Uplift)",
 "question": "# I.5 — Filled (concrete-filled HSS) composite member in axial tension  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA concrete-filled rectangular HSS member must resist a net uplift (tension)\ncaused by wind acting against a sustained gravity compression. The steel\nsection is an ASTM A500/A500M Grade C HSS10×6×3/8 (Fy = 50 ksi), completely\nfilled with normal-weight concrete (wc = 145 lb/ft³, f′c = 5 ksi) and contains\nno longitudinal reinforcement (Asr = 0). The entire applied load is delivered\ndirectly to the steel section.\n\nThe member carries an axial dead load D = 32 kips in compression and a wind\nload W = 100 kips in tension. Using AISC 360 Chapter I, determine the governing\nrequired tensile strength from the uplift load combinations and check whether\nthe available tensile strength of the filled composite member is adequate\n(LRFD φtPn and ASD Pn/Ωt).\n\n## Given\n- Material: ASTM A500/A500M Gr. C, Fy = 50 ksi; normal-weight concrete\n  wc = 145 lb/ft³, f′c = 5 ksi; no reinforcement, Asr = 0.\n- Section: HSS10×6×3/8 — As = 10.4 in.².\n- Loads: axial D = 32 kips (compression), W = 100 kips (tension); entire load\n  applied to the steel section. Take compression negative, tension positive.\n- Code basis: AISC 360-22 (uplift load combinations per ASCE/SEI 7).\n\n## Find\nThe governing required tensile strength (LRFD and ASD) and the available\ntensile strength φtPn / (Pn/Ωt) of the filled composite member, and whether\nthe member is adequate.",
 "has_figure": false,
 "stem": "I_5",
 "breadcrumb": "EXAMPLE I.5 · AISC 360-22 Ch.I (composite member) · §I2.2 §I6 · Filled Composite Member in Axial Tension (Uplift)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.5 · AISC 360-22 Ch.I (composite member) · §I2.2 §I6 · Filled Composite Member in Axial Tension (Uplift)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §I2.2 (tension of filled members: concrete neglected; Pn = FyAs + FyrAsr with Asr = 0; φt = 0.90, Ωt = 1.67). Per the RAG extract provided.

---

### 1. Required Tensile Strength (uplift combinations)

D = 32 kips (C); W = 100 kips (T):

- **LRFD (0.9D + 1.0W):** Tu = 100 − 0.9(32) = **71.2 kips**
- **ASD (0.6D + 0.6W):** Ta = 0.6(100) − 0.6(32) = **40.8 kips**

### 2. Available Tensile Strength

HSS10x6x3/8 (A500 Gr. C): As = 10.4 in.²; no longitudinal reinforcement → only the steel section resists tension:

Pn = FyAs = 50(10.4) = **520 kips**

- **LRFD:** φtPn = 0.90(520) = **468 kips ≥ 71.2 ✓** (utilization 0.15)
- **ASD:** Pn/Ωt = 520/1.67 = **311 kips ≥ 40.8 ✓** (utilization 0.13)

### 3. Conclusion

Under net wind uplift the filled HSS resists tension through its steel shell alone, providing **468 kips (LRFD) / 311 kips (ASD)** against required strengths of 71.2 / 40.8 kips — adequate by a wide margin. Because the entire load is applied to the steel section and the concrete is not engaged in tension, **no §I6 longitudinal shear transfer is required for this load case** (contrast with the encased member of Example I.10, where the reinforcement participates).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
