<!-- chunk_id: G.1A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.1A",
 "example_family": "G.1",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G2.1"
 ],
 "eqs": [
  "G2-1",
  "G2-2"
 ],
 "tables": [],
 "title": "W24x62 Shear Strength (Manual Table Basis)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.1A — W24x62 Shear Strength (Manual Table Basis)",
 "question": "# G.1A -- W-Shape in Major-Axis Shear (Manual-table approach)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA simply supported ASTM A992/A992M W24x62 beam frames into supports that deliver\nend reactions (shear) of 48 kips from service dead load and 145 kips from service\nlive load. Using the tabulated available-shear values of the AISC *Steel Construction\nManual* (which embody AISC 360 Chapter G), determine the available major-axis shear\nstrength of the W24x62 and verify it is adequate for both LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: W24x62 (d = 23.7 in., tw = 0.430 in.), bending/shear about the major axis.\n- Loads (service end shear): D = 48 kips, L = 145 kips.\n- Code basis: AISC 360-22 Chapter G; load combinations per ASCE/SEI 7 Chapter 2.\n\n## Find\nThe available shear strength (phi_v*Vn for LRFD and Vn/Omega_v for ASD) and whether\nthe W24x62 is adequate.",
 "has_figure": false,
 "stem": "G_1A",
 "breadcrumb": "EXAMPLE G.1A · AISC 360-22 Ch.G (beam shear) · §G2.1 · W24x62 Shear Strength (Manual Table Basis)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.1A · AISC 360-22 Ch.G (beam shear) · §G2.1 · W24x62 Shear Strength (Manual Table Basis)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G2.1(a) (Eqs. G2-1, G2-2) — the basis of the AISC Manual tabulated shear values. Per the RAG extract provided.

---

### 1. Required Shear Strength

End reactions: D = 48 kips, L = 145 kips:

- **LRFD:** Vu = 1.2(48) + 1.6(145) = **290 kips**
- **ASD:** Va = 48 + 145 = **193 kips**

### 2. Available Shear Strength — W24x62 (A992)

Web area: Aw = d·tw = 23.7(0.430) = 10.2 in.²

The W24x62 is a rolled I-shape with h/tw = 50.1 ≤ 2.24√(E/Fy) = 53.9 → per §G2.1(a): **φv = 1.00, Ωv = 1.50, Cv1 = 1.0** (Eq. G2-2).

Vn = 0.6FyAwCv1 = 0.6(50)(10.2)(1.0) = **306 kips** (Eq. G2-1)

- **LRFD:** φvVn = 1.00(306) = **306 kips** ≥ 290 kips ✓ (utilization 0.95)
- **ASD:** Vn/Ωv = 306/1.50 = **204 kips** ≥ 193 kips ✓ (utilization 0.95)

These match the AISC Manual tabulated available shear strengths, which embody exactly these Chapter G provisions.

### 3. Conclusion

The W24x62 provides φvVn = 306 kips (LRFD) and Vn/Ωv = 204 kips (ASD) by web shear yielding — **adequate** for the 290 / 193 kip end reactions at ~95% utilization.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
