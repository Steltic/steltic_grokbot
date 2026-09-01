<!-- chunk_id: H.6_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "H.6",
 "example_family": "H.6",
 "chapter": "H",
 "topic": "beam-column (combined axial + flexure)",
 "clauses": [
  "H3.3"
 ],
 "eqs": [
  "H3-7",
  "H3-8",
  "H3-9"
 ],
 "tables": [],
 "title": "W10x49 Under Combined Flexure and Torsion (Non-HSS)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE H.6 — W10x49 Under Combined Flexure and Torsion (Non-HSS)",
 "question": "# H.6 - W-shape torsional strength (open-section nonuniform torsion + Section H3.3) (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M W10x49 spans 15 ft (simply supported, flexurally pinned, warping unrestrained at both\nends). A concentrated load is applied at midspan at a 6-in. eccentricity from the shear center, resolved into\na transverse load through the shear center plus a concentrated torque. The concentrated load is 2.5 kips dead +\n7.5 kips live. Determine the maximum combined normal and shear stresses on the cross section, verify the section\nfor combined flexure and torsion using AISC 360-22 Section H3.3 (non-HSS torsion), and find the maximum service\nrotation. (Solve the nonuniform-torsion behavior by classical open-thin-walled torsion theory; the torsional\nsection properties are from the AISC Shapes Database.)\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi; E = 29,000 ksi; G = 11,200 ksi.\n- Member: W10x49 (tw = 0.340 in., tf = 0.560 in., Ix = 272 in^4, Sx = 54.6 in^3, Zx = 60.4 in^3,\n  J = 1.39 in^4, Cw = 2,070 in^6; warping statical/normalized properties Sw1 = 33.0 in^4, Wno = 23.6 in^2,\n  Qf = 12.8 in^3, Qw = 29.8 in^3).\n- Geometry: span L = 15 ft = 180 in.; pinned, warping-free ends; concentrated load + torque at midspan; e = 6 in.\n- Loads (ASCE/SEI 7): P = 2.5 k (D) + 7.5 k (L).\n- Code basis: AISC 360-22 Section H3.3 (limit states of yielding under normal stress, shear yielding under\n  shear stress, and buckling).\n\n## Find\nMaximum normal and shear stresses (LRFD and ASD), the adequacy check by Section H3.3, and the maximum rotation\nat service load.",
 "has_figure": false,
 "stem": "H_6",
 "breadcrumb": "EXAMPLE H.6 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.3 · W10x49 Under Combined Flexure and Torsion (Non-HSS)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE H.6 · AISC 360-22 Ch.H (beam-column (combined axial + flexure)) · §H3.3 · W10x49 Under Combined Flexure and Torsion (Non-HSS)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §H3.3 (non-HSS members under torsion and combined stress: Fn = Fy for normal-stress yielding (Eq. H3-7), Fn = 0.6Fy for shear yielding (Eq. H3-8), buckling per Eq. H3-9); torsional response by classical open-thin-walled (warping) torsion theory. φT = 0.90, ΩT = 1.67. Per the RAG extract provided.

---

### 1. Required Strengths

W10x49, L = 180 in., flexurally pinned, warping-free ends; midspan load P at e = 6 in. → midspan torque T = 6P.

- **LRFD:** Pu = 1.2(2.5) + 1.6(7.5) = 15.0 kips → Mu = PuL/4 = **675 kip-in.**; Vu = **7.50 kips**; Tu = **90.0 kip-in.**
- **ASD:** Pa = 10.0 kips → Ma = **450 kip-in.**; Va = **5.00 kips**; Ta = **60.0 kip-in.**

### 2. Torsional Solution (classical nonuniform torsion)

Torsional bending constant: a = √(ECw/GJ) = √[29,000(2,070)/(11,200 × 1.39)] = **62.1 in.**; L/(2a) = 1.45.

For a concentrated torque at midspan with rotation-fixed, warping-free ends (internal torque ±T/2):

- θ′max (at ends) = [T/(2GJ)][1 − 1/cosh(L/2a)] = (T/2GJ)(0.555)
- θ″max (at midspan) = [T/(2GJa)]tanh(L/2a) = (T/2GJ)(0.0144 in.⁻¹)
- θ‴max (at midspan) = T/(2GJa²)
- θmax (midspan) = [T/(2GJ)][L/2 − a·tanh(L/2a)]

### 3. Stresses (GJ = 15,570 kip-in.²)

**LRFD (T = 90 kip-in., B = T/2GJ = 2.89 × 10⁻³ rad/in.):**
- Warping normal (midspan): σw = EWnoθ″ = 29,000(23.6)(4.17 × 10⁻⁵) = **28.5 ksi**
- Bending normal (midspan): σb = Mu/Sx = 675/54.6 = **12.4 ksi**
- **Total normal: fn = 40.9 ksi**
- Pure-torsion shear (ends): τt = Gtθ′ → flange: 11,200(0.560)(1.60 × 10⁻³) = 10.1 ksi; web: 6.1 ksi
- Warping shear (midspan): τw = ESw1θ‴/tf = 29,000(33.0)(7.50 × 10⁻⁷)/0.560 = 1.3 ksi
- Flexural shear: VQw/(Ixtw) = 7.5(29.8)/[272(0.340)] = 2.4 ksi (web); VQf/(Ixtf) = 0.6 ksi (flange)
- **Max combined shear ≈ 10.1 + 0.6 = 10.7 ksi (flange at support)**

**ASD (T = 60 kip-in., ×2/3 on torsional stresses; M, V at service):** σw = 19.0 ksi; σb = 8.2 ksi → **fn = 27.3 ksi**; max shear ≈ **7.1 ksi**

### 4. §H3.3 Checks

| Limit state | LRFD: available vs required | ASD: available vs required |
|---|---|---|
| Normal-stress yielding (Eq. H3-7, Fn = Fy) | φTFn = 0.90(50) = 45.0 ≥ 40.9 ksi ✓ (0.91) | Fn/ΩT = 29.9 ≥ 27.3 ksi ✓ (0.91) |
| Shear yielding (Eq. H3-8, Fn = 0.6Fy) | 0.90(30) = 27.0 ≥ 10.7 ksi ✓ | 18.0 ≥ 7.1 ksi ✓ |
| Buckling (Eq. H3-9) | Not critical — compression-flange stress < LTB stress at Lb = 15 ft for W10x49 | same ✓ |

### 5. Maximum Service Rotation

T_serv = 10.0(6) = 60 kip-in.:
θmax = [60/(2 × 15,570)][90 − 62.1·tanh(1.45)] = (1.93 × 10⁻³)(90 − 55.6) = **0.066 rad ≈ 3.8°**

### 6. Conclusion

The W10x49 **satisfies §H3.3** under combined flexure and torsion: the governing check is normal-stress yielding at midspan, where the warping normal stress (28.5 ksi LRFD) dominates the bending stress (12.4 ksi), reaching 91% of the available 0.9Fy. Shear stresses are far below 0.6Fy limits. However, the **service rotation of ≈3.8° is substantial** — typical of open shapes in torsion — and the designer should confirm this is tolerable for attached construction or consider a closed (HSS) section or torsion-restraining details.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
