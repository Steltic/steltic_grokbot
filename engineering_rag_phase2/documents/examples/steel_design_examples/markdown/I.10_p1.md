<!-- chunk_id: I.10_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "I.10",
 "example_family": "I.10",
 "chapter": "I",
 "topic": "composite member",
 "clauses": [
  "I2.1b",
  "I6",
  "I6.4"
 ],
 "eqs": [],
 "tables": [],
 "title": "Encased Composite Member in Axial Tension (Uplift)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE I.10 — Encased Composite Member in Axial Tension (Uplift)",
 "question": "# I.10 — Encased composite member in axial tension  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA concrete-encased composite member must resist net uplift from wind acting\nagainst sustained gravity compression. The steel section is an ASTM A992/A992M\nW10×45 (Fy = 50 ksi) encased in a 24 in. × 24 in. normal-weight reinforced-\nconcrete section (wc = 145 lb/ft³, f′c = 5 ksi) with eight No. 8 longitudinal\nbars (total Asr = 6.32 in.², ASTM A615/A615M, Fyr = 60 ksi). The entire applied\nload is delivered to the encased steel section. (Material and detailing limits\nare as established for this encased section; see the encased-compression\ncompanion problem.)\n\nThe member carries an axial dead load D = 260 kips in compression and a wind\nload W = 980 kips in tension. Using AISC 360 Chapter I, determine the governing\nrequired tensile strength from the uplift load combinations, check the available\ntensile strength (LRFD φtPn and ASD Pn/Ωt), and — because both the steel shape\nand the reinforcement are needed — determine the longitudinal-shear force that\nmust be transferred when the external tension is applied to the steel section.\n\n## Given\n- Material: steel ASTM A992/A992M, Fy = 50 ksi; bars ASTM A615, Fyr = 60 ksi;\n  normal-weight concrete, f′c = 5 ksi (concrete neglected in tension).\n- Section: W10×45 encased in 24 in. × 24 in. concrete; As = 13.3 in.²,\n  Asr = 6.32 in.² (eight No. 8 bars).\n- Loads: axial D = 260 kips (compression), W = 980 kips (tension); entire load\n  applied to the encased steel section. Take compression negative, tension positive.\n- Code basis: AISC 360-22 (uplift load combinations per ASCE/SEI 7).\n\n## Find\nThe governing required tensile strength (LRFD and ASD), the available tensile\nstrength φtPn / (Pn/Ωt) of the encased composite member and whether it is\nadequate, and the longitudinal-shear force V′r to be transferred to the\nreinforcement.",
 "has_figure": false,
 "stem": "I_10",
 "breadcrumb": "EXAMPLE I.10 · AISC 360-22 Ch.I (composite member) · §I2.1b §I6 §I6.4 · Encased Composite Member in Axial Tension (Uplift)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE I.10 · AISC 360-22 Ch.I (composite member) · §I2.1b §I6 §I6.4 · Encased Composite Member in Axial Tension (Uplift)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter I: §I2.1b (encased member tension, Pn = FyAs + FyrAsr; φt = 0.90, Ωt = 1.67) and §I6 (load transfer where the external force is applied to the steel section). Per the RAG extract provided.

---

### 1. Required Tensile Strength (uplift combinations)

D = 260 kips (C); W = 980 kips (T):

- **LRFD (0.9D + 1.0W):** Tu = 980 − 0.9(260) = **746 kips**
- **ASD (0.6D + 0.6W):** Ta = 0.6(980) − 0.6(260) = **432 kips**

### 2. Available Tensile Strength

W10x45: As = 13.3 in.²; reinforcement: Asr = 6.32 in.² (Fyr = 60 ksi). Concrete is neglected in tension:

Pn = FyAs + FyrAsr = 50(13.3) + 60(6.32) = 665 + 379 = **1,040 kips**

- **LRFD:** φtPn = 0.90(1,040) = **940 kips ≥ 746 ✓** (utilization 0.79)
- **ASD:** Pn/Ωt = 1,040/1.67 = **625 kips ≥ 432 ✓** (utilization 0.69)

### 3. Longitudinal Shear Transfer — §I6

The entire external tension enters through the steel shape, but the reinforcement supplies 379/1,040 = 36% of the resistance; that share must be transferred out of the steel into the encasement (and thence to the bars) by the load-transfer mechanism:

- **LRFD:** V′r = Tu(FyrAsr/Pn) = 746(0.363) = **271 kips**
- **ASD:** V′r = 432(0.363) = **157 kips**

This force shall be developed by steel headed stud anchors (or direct bond where permitted) within the §I6.4 load-introduction length (2× the minimum transverse dimension above and below the transfer region), with the transverse-tie detailing of the companion encased-column design maintained through the region.

### 4. Conclusion

The encased W10x45 with eight No. 8 bars is **adequate for the 746-kip (LRFD) / 432-kip (ASD) net uplift**, with both steel and reinforcement required to act. Accordingly, the connection region must transfer **271 kips (LRFD) / 157 kips (ASD)** of longitudinal shear from the steel core to the reinforced encasement per §I6 — the governing detailing requirement of this design.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
