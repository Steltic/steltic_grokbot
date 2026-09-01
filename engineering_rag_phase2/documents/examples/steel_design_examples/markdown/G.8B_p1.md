<!-- chunk_id: G.8B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.8B",
 "example_family": "G.8",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G1",
  "G2.1",
  "G2.2",
  "G2.3",
  "G2.4"
 ],
 "eqs": [
  "G2-1",
  "G2-4",
  "G2-5",
  "G2-7",
  "G2-11"
 ],
 "tables": [],
 "title": "Built-Up Girder: Verification of 42-in. / 90-in. Stiffened Panels",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.8B — Built-Up Girder: Verification of 42-in. / 90-in. Stiffened Panels",
 "question": "# G.8B -- Built-up Girder with Transverse Stiffeners (verify spacing from the Specification)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nTake the same ASTM A572/A572M Grade 50 welded built-up girder (36 in. deep overall;\nPL 1-1/2 x 16 flanges; 5/16-in. web; clear web depth h = 33.0 in.; 56-ft simply\nsupported span; uniform service load 1.25 kip/ft dead + 3.75 kip/ft live; compression\nflange continuously braced). Transverse stiffeners are placed at 42 in. in the end\npanel and 90 in. in the second panel. Verify, by directly applying AISC 360 Chapter G\n(not Manual tables), that these panels have adequate shear strength for LRFD and ASD.\nTreat the end panel WITHOUT tension field action (conservative) and the second panel\nWITH tension field action.\n\n## Given\n- Material: ASTM A572/A572M Grade 50, Fy = 50 ksi.\n- Web: tw = 5/16 in., h = 33.0 in., Aw = 11.3 in.^2; flanges PL 1-1/2 x 16.\n- Required strength (from the uniform load): Vu = 210 kips, Va = 140 kips at the\n  support; Vu = 184 kips, Va = 123 kips at the start of the second panel (42 in.).\n- Stiffener spacing: end panel a = 42 in.; second panel a = 90 in.\n- Code basis: AISC 360-22 Sections G1, G2.1, G2.2.\n\n## Find\nThe available shear strength of the end panel and of the second panel, and adequacy.",
 "has_figure": false,
 "stem": "G_8B",
 "breadcrumb": "EXAMPLE G.8B · AISC 360-22 Ch.G (beam shear) · §G1 §G2.1 §G2.2 §G2.3 §G2.4 · Built-Up Girder: Verification of 42-in. / 90-in. Stiffened Panels",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.8B · AISC 360-22 Ch.G (beam shear) · §G1 §G2.1 §G2.2 §G2.3 §G2.4 · Built-Up Girder: Verification of 42-in. / 90-in. Stiffened Panels

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §§G1, G2.1 (Eqs. G2-1, G2-4, G2-5), G2.2 (Eqs. G2-7, G2-11). φv = 0.90, Ωv = 1.67. Per the RAG extract provided.

---

### 1. Data and Demands

Web: h = 33.0 in.; tw = 0.3125 in.; h/tw = 106; Aw = 11.3 in.²; flanges PL 1-1/2 × 16 (Afc = Aft = 24.0 in.²).

Demands: at support Vu = 210 kips / Va = 140 kips; at start of second panel (x = 42 in.) Vu = 184 kips / Va = 123 kips.

### 2. End Panel — a = 42 in., No Tension Field Action (§G2.1(b))

a/h = 42/33 = 1.27 → kv = 5 + 5/(1.27)² = **8.09** (Eq. G2-5)

1.10√(kvE/Fy) = 1.10√(8.09 × 580) = 75.3 < h/tw = 106 → Cv1 = 75.3/106 = **0.713** (Eq. G2-4)

Vn = 0.6FyAwCv1 = 0.6(50)(11.3)(0.713) = **241 kips** (Eq. G2-1)

- **LRFD:** φvVn = 0.90(241) = **217 kips** ≥ 210 kips ✓ (utilization 0.97)
- **ASD:** Vn/Ωv = 241/1.67 = **144 kips** ≥ 140 kips ✓ (utilization 0.97)

### 3. Second Panel — a = 90 in., With Tension Field Action (§G2.2)

a/h = 90/33 = 2.73 ≤ 3 ✓ → kv = 5 + 5/(2.73)² = **5.67**

h/tw = 106 > 1.37√(kvE/Fy) = 78.6 → Cv2 = 1.51kvE/[(h/tw)²Fy] = 1.51(5.67)(29,000)/[(106)²(50)] = **0.445** (Eq. G2-11)

Eligibility for Eq. G2-7: 2Aw/(Afc + Aft) = 2(11.3)/48.0 = 0.47 ≤ 2.5 ✓; h/bfc = h/bft = 33/16 = 2.06 ≤ 6.0 ✓

Vn = 0.6FyAw[Cv2 + (1 − Cv2)/(1.15√(1 + (a/h)²))] = 338[0.445 + 0.555/(1.15 × 2.90)] = 338(0.611) = **206 kips** (Eq. G2-7)

- **LRFD:** φvVn = 0.90(206) = **186 kips** ≥ 184 kips ✓ (utilization 0.99)
- **ASD:** Vn/Ωv = 206/1.67 = **124 kips** ≥ 123 kips ✓ (utilization 0.99)

### 4. Conclusion

Both panels are **adequate**: the 42-in. end panel develops 217 kips (LRFD) / 144 kips (ASD) from the elevated buckling coefficient alone (conservatively no tension field action, per §G2.3 philosophy), and the 90-in. second panel reaches 186 kips / 124 kips by mobilizing tension field action per Eq. G2-7 — without TFA the second panel would provide only 0.9(0.6 × 50 × 11.3 × Cv1) ≈ 167 kips and would fail the 184-kip demand. Utilizations are 97–99%, so the stated stiffener locations should be treated as minimum requirements, with stiffener sizing per §G2.4.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
