<!-- chunk_id: G.8A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.8A",
 "example_family": "G.8",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G1",
  "G2.1",
  "G2.4",
  "G2.2"
 ],
 "eqs": [
  "G2-1",
  "G2-4",
  "G2-5",
  "G2-7",
  "G2-11"
 ],
 "tables": [],
 "title": "Built-Up Girder: Web Shear and Transverse Stiffener Layout",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.8A — Built-Up Girder: Web Shear and Transverse Stiffener Layout",
 "question": "# G.8A -- Built-up Girder with Transverse Stiffeners (determine required spacing)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA welded built-up I-shaped plate girder spans 56 ft, simply supported, and carries a\nuniform service load of 1.25 kip/ft dead load plus 3.75 kip/ft live load over the\nfull span. The girder is ASTM A572/A572M Grade 50. Its cross section is 36 in. deep\noverall with two PL 1-1/2 in. x 16 in. flanges and a 5/16-in.-thick web; the clear\nweb depth between flanges is h = 33.0 in. The compression flange is continuously\nbraced. The web was intentionally made thin to illustrate transverse-stiffener design.\n\nDetermine, using AISC 360 Chapter G: (a) whether the unstiffened web has sufficient\nshear strength at the support; and (b) if not, a workable transverse-stiffener layout\n(end panel and subsequent panels) such that the available shear strength meets or\nexceeds the demand along the girder. Report results for both LRFD and ASD. The end\npanel is treated conservatively WITHOUT tension field action; interior panels may use\ntension field action (Section G2.2), with the panel aspect ratio a/h not exceeding 3.\n\n## Given\n- Material: ASTM A572/A572M Grade 50, Fy = 50 ksi.\n- Built-up girder: d = 36.0 in.; flanges PL 1-1/2 x 16 (bfc = bft = 16.0 in.,\n  tf = 1.5 in.); web tw = 5/16 in.; clear web depth h = 33.0 in.\n- Span: 56 ft, simply supported, uniform load; compression flange continuously braced.\n- Loads (service uniform): wD = 1.25 kip/ft, wL = 3.75 kip/ft.\n- Code basis: AISC 360-22 Sections G1, G2.1, G2.2, G2.3, G2.4; loads per ASCE/SEI 7 Ch. 2.\n\n## Find\nThe unstiffened-web available shear strength, whether stiffeners are required, and a\nrequired transverse-stiffener spacing layout that satisfies the shear demand.",
 "has_figure": false,
 "stem": "G_8A",
 "breadcrumb": "EXAMPLE G.8A · AISC 360-22 Ch.G (beam shear) · §G1 §G2.1 §G2.4 §G2.2 · Built-Up Girder: Web Shear and Transverse Stiffener Layout",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.8A · AISC 360-22 Ch.G (beam shear) · §G1 §G2.1 §G2.4 §G2.2 · Built-Up Girder: Web Shear and Transverse Stiffener Layout

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §§G1, G2.1 (Eqs. G2-1, G2-4, G2-5), G2.2 (Eqs. G2-7, G2-11), G2.4 (stiffener requirements). φv = 0.90, Ωv = 1.67. Per the RAG extract provided.

---

### 1. Required Shear

wu = 1.2(1.25) + 1.6(3.75) = 7.50 kip/ft; wa = 5.00 kip/ft; L = 56 ft:

- **At support:** Vu = 7.50(56)/2 = **210 kips**; Va = **140 kips**
- Demand decreases linearly: Vu(x) = 210 − 7.50x; Va(x) = 140 − 5.00x (x in ft)

### 2. (a) Unstiffened Web — §G2.1(b), kv = 5.34

Web: h/tw = 33.0/0.3125 = 106; Aw = d·tw = 36.0(0.3125) = 11.3 in.²

1.10√(5.34E/Fy) = 61.2 < 106 → Cv1 = 61.2/106 = 0.580 (Eq. G2-4)

Vn = 0.6(50)(11.3)(0.580) = **196 kips** → φvVn = **176 kips** < 210 ✗; Vn/Ωv = **117 kips** < 140 ✗

**The unstiffened web is inadequate at the supports — transverse stiffeners are required** (§G2.4(a) screen also fails: available < required).

### 3. (b) Stiffener Layout

**End panel — a = 42 in. (a/h = 1.27), without tension field action (§G2.1(b)):**
kv = 5 + 5/(1.27)² = 8.09 (Eq. G2-5); 1.10√(kvE/Fy) = 75.3 < 106 → Cv1 = 75.3/106 = 0.713
Vn = 0.6(50)(11.3)(0.713) = **241 kips** → φvVn = **217 kips ≥ 210 ✓**; Vn/Ωv = **144 kips ≥ 140 ✓**

**Second panel — a = 90 in. (a/h = 2.73 ≤ 3), with tension field action (§G2.2):**
Demand at x = 3.5 ft: Vu = 184 kips; Va = 123 kips.
kv = 5 + 5/(2.73)² = 5.67; 1.37√(kvE/Fy) = 78.6 < 106 → Cv2 = 1.51kvE/[(h/tw)²Fy] = 0.445 (Eq. G2-11)
TFA eligibility: 2Aw/(Afc + Aft) = 22.5/48 = 0.47 ≤ 2.5 ✓; h/bf = 33/16 = 2.06 ≤ 6.0 ✓ → Eq. G2-7:
Vn = 0.6(50)(11.3)[0.445 + (1 − 0.445)/(1.15√(1 + 2.73²))] = 338(0.611) = **206 kips**
→ φvVn = **186 kips ≥ 184 ✓**; Vn/Ωv = **124 kips ≥ 123 ✓**

**Beyond x = 11 ft (42 + 90 = 132 in.):** demand Vu = 210 − 7.50(11) = 128 kips < 176 kips (unstiffened capacity) ✓; Va = 85 kips < 117 kips ✓ → **no further stiffeners needed**.

### 4. Recommended Layout (each end, symmetric)

| Panel | a (in.) | Basis | φvVn / Vn,Ωv (kips) | Demand (kips) |
|---|---|---|---|---|
| End panel | 42 | G2.1, kv = 8.09 (no TFA) | 217 / 144 | 210 / 140 ✓ |
| Second panel | 90 | G2.2, TFA (Eq. G2-7) | 186 / 124 | 184 / 123 ✓ |
| Remainder | — | G2.1 unstiffened | 176 / 117 | ≤128 / ≤85 ✓ |

Stiffeners shall be proportioned per §G2.4 (Eqs. G2-16 through G2-19) and detailed per §G2.4(b)/(c).

### 5. Conclusion

The intentionally thin 5/16-in. web cannot carry the 210-kip (LRFD) support shear unstiffened. A pair of transverse stiffeners at **42 in. and 132 in. from each end** restores compliance: the end panel works conservatively without tension field action (kv enhancement alone), the second panel relies on tension field action per §G2.2, and the remainder of the span is adequate unstiffened. All checks satisfy both LRFD and ASD.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
