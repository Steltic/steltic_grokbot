<!-- chunk_id: E.14B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.14B",
 "example_family": "E.14",
 "chapter": "E",
 "topic": "column / axial compression",
 "clauses": [
  "E5",
  "E3",
  "E7",
  "F10",
  "H2",
  "App8"
 ],
 "eqs": [
  "E3-2",
  "E3-4",
  "E7-1",
  "E7-3",
  "E7-5",
  "F10-1",
  "F10-2",
  "F10-4",
  "F10-6",
  "H2-1",
  "A-8-3",
  "A-8-5"
 ],
 "tables": [],
 "title": "Eccentrically Loaded Single-Angle Compression Member (Long Leg Attached)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.14B — Eccentrically Loaded Single-Angle Compression Member (Long Leg Attached)",
 "question": "# E.14B — Eccentrically loaded single-angle compression member (long leg attached)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA single-angle strut is built from an **L8×4×1/2** of **ASTM A572/A572M Grade 50** steel\n(Fy = 50 ksi). The member has an **effective length of 5 ft (Lc = 60 in.) about every axis**\nand carries no transverse load, so the moment varies uniformly along the length\n(Cb = 1.0, Cm = 1.0). The **long (8-in.) leg is the attached/connected leg.**\n\nThe axial compressive force, Pr, is applied **eccentrically**: the line of action lies on the\nattached (long) leg at a distance of **0.75t (= 0.375 in.) from the outer face of that leg**, at the\nmid-width of the leg, as shown in Figure E.14B-1 (figures/E_14B.png). Because the angle is\nunsymmetric, this load point is offset from the centroid in both principal directions, producing\nbending about **both principal axes (w-w and z-z)** in addition to axial compression.\n\nUse the AISC 360-22 Specification to determine the **maximum eccentric axial force the member\ncan support** (the available strength), accounting for member compressive strength, the flexural\nstrengths about both principal axes at the three cross-section corner points (A = heel of the\nshort leg toe region, B = heel, C = toe of the long leg), the second-order (P-δ) amplification of\nthe eccentric moments, and the combined-stress interaction. Report both the LRFD design strength\nand the ASD allowable strength.\n\n## Given\n- Material: ASTM A572/A572M Grade 50; Fy = 50 ksi; E = 29,000 ksi.\n- Member / section: single angle L8×4×1/2 (long leg = 8 in. attached; short leg = 4 in.; t = 1/2 in.).\n- Section properties (AISC Shapes Database v16.0): Ag = 5.80 in.²; x̄ = 0.854 in.; ȳ = 2.84 in.;\n  Ix = 38.6 in.⁴; Iy = 6.75 in.⁴; Iz = 4.32 in.⁴; Iw = 41.0 in.⁴; rz = 0.863 in.; tan α = 0.266 (α = 14.9°);\n  principal-axis section moduli SwA = 12.4, SwB = 16.3, SwC = 7.98, SzA = 1.82, SzB = 2.77, SzC = 5.81 in.³;\n  βw = 5.48 in. (use −5.48 in. when the long leg is in compression).\n- Effective length: Lc = KL = 5.00 ft = 60.0 in. (all axes).\n- Loading: eccentric axial compression Pr applied at 0.75t on the long leg (mid-width); no transverse load\n  (uniform moment, Cb = 1.0, Cm = 1.0).\n- Code basis: AISC 360-22.\n\n## Find\nThe available eccentric axial compressive strength of the member (LRFD φPn and ASD Pn/Ω),\ngoverned by the AISC 360-22 Section H2 combined-stress interaction evaluated at corner points A, B, and C.",
 "has_figure": true,
 "stem": "E_14B",
 "breadcrumb": "EXAMPLE E.14B · AISC 360-22 Ch.E (column / axial compression) · §E5 §E3 §E7 §F10 §H2 §App8 · Eccentrically Loaded Single-Angle Compression Member (Long Leg Attached)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.14B · AISC 360-22 Ch.E (column / axial compression) · §E5 §E3 §E7 §F10 §H2 §App8 · Eccentrically Loaded Single-Angle Compression Member (Long Leg Attached)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §E5 (conditions not met → Chapter H evaluation required), §E3/§E7 (axial capacity, Eqs. E3-2/E3-4, E7-1/E7-3/E7-5), §F10 (Eqs. F10-1, F10-2, F10-4, F10-6), §H2 (Eq. H2-1), Appendix 8 (Eqs. A-8-3, A-8-5). φc = φb = 0.90; Ωc = Ωb ≈ 1.67/1.67. Per the RAG extract provided.

---

### 1. Setup

L8x4x1/2, A572 Gr. 50; Ag = 5.80 in.²; Lc = 60 in. all axes; Cb = Cm = 1.0. The load is applied on the long (attached) leg at mid-width (4.00 in. from the heel) and 0.375 in. from its outer face. Because the load is eccentric, the §E5 effective-slenderness treatment does not apply; per §E5 and §F10 the member is evaluated for combined stress using **§H2** at corner points A (short-leg toe), B (heel), C (long-leg toe).

**Eccentricities.** Geometric offsets from the centroid (x̄ = 0.854, ȳ = 2.84): Δx = 0.375 − 0.854 = −0.479 in.; Δy = 4.00 − 2.84 = +1.16 in. Transforming to principal axes (α = 14.9°, major axis w tilted from the geometric x-axis):

ew = Δx cos α + Δy sin α = **−0.165 in.**; ez = −Δx sin α + Δy cos α = **+1.245 in.**

→ Mw = 1.245P (major axis), Mz = 0.165P (minor axis), both proportional to P (Mnt-type; B1 applies).

**Point coordinates (principal, from given S values, Iw = 41.0, Iz = 4.32):** A (w = +2.37, z = −3.31); B (w = −1.56, z = −2.52); C (w = +0.74, z = +5.14).

**First-order stresses per unit P (compression +):** σ = P[1/A + ez·z/Iw + ew·w/Iz]

| Point | axial | from Mw | from Mz | net |
|---|---|---|---|---|
| A | +0.172P | −0.101P (T) | −0.091P (T) | −0.019P |
| B | +0.172P | −0.077P (T) | +0.059P (C) | +0.155P |
| C | +0.172P | +0.156P (C) | −0.028P (T) | **+0.300P (governs)** |

### 2. Axial Term — Chapter E

Long leg b/t = 16 > λr = 0.45√(E/Fy) = 10.8 → slender (§E7); FTB exempt since b/t = 16 ≤ 0.71√(E/Fy) = 17.1 (§E5). Governing flexural buckling about z: Lc/rz = 60/0.863 = 69.5.

Fe = π²E/(69.5)² = 59.2 ksi (Eq. E3-4); Fy/Fe = 0.844 ≤ 2.25 → Fn = 0.658^0.844(50) = **35.1 ksi** (Eq. E3-2)

§E7 long leg: λr√(Fy/Fn) = 12.9 < 16 → Fel = (1.49 × 10.8/16)²(50) = 51.0 ksi (Eq. E7-5); be = 8[1 − 0.22√(51.0/35.1)]√(51.0/35.1) = 7.08 in. (Eq. E7-3, Table E7.1(c)); Ae = 5.80 − (8 − 7.08)(0.5) = 5.34 in.²

Pn = FnAe = 35.1(5.34) = **188 kips** (Eq. E7-1) → Fca = φcPn/Ag = 29.1 ksi (LRFD); 19.4 ksi (ASD)

### 3. Flexural Capacities — §F10

**Major axis (w), long-leg toe C in compression (βw = −5.48 in.):**
Mcr = [9EAgrztCb/(8Lb)]·[√(1 + (4.4βwrz/(Lbt))²) + 4.4βwrz/(Lbt)] (Eq. F10-4)
= 1,361 × [√(1 + 0.481) − 0.694] = 1,361(0.523) = **712 kip-in.**
My = FySwC = 50(7.98) = 399 kip-in.; My/Mcr = 0.560 ≤ 1.0 → Mn = (1.92 − 1.17√0.560)(399) = **417 kip-in.** (Eq. F10-2; ≤ 1.5My = 599)
Leg local buckling (noncompact, λp = 13.0 < 16 < λr = 21.9): Mn = FySc[2.43 − 1.72(b/t)√(Fy/E)] = 50(7.98)(1.287) = 514 kip-in. (Eq. F10-6)
**Mnw = 417 kip-in. (LTB governs).** φMnw = 375 kip-in.; Mnw/Ω = 250 kip-in.

**Minor axis (z):** Mz compresses the heel (B); the leg toes are in tension → leg local buckling does not apply; yielding governs (Eq. F10-1): Mnz = 1.5My = 1.5(50)(1.82) = **137 kip-in.** φMnz = 123 kip-in.; Mnz/Ω = 81.7 kip-in.

Available flexural stresses at each point: Fcb = φMn/S (LRFD) or (Mn/Ω)/S (ASD), e.g. at C: Fcbw = 375/7.98 = 47.0 ksi, Fcbz = 123/5.81 = 21.1 ksi (LRFD).

### 4. Second-Order Amplification — Appendix 8

B1 = Cm/(1 − αPr/Pe1) ≥ 1 (Eq. A-8-3), Pe1 = π²EI/Lc² (Eq. A-8-5), in each plane of bending:
Pe1w = π²(29,000)(41.0)/(60)² = 3,260 kips; Pe1z = π²(29,000)(4.32)/(60)² = 343 kips.

### 5. Interaction — §H2, Eq. H2-1 (signs per stress sense; tension terms subtract)

|fra/Fca + frbw/Fcbw + frbz/Fcbz| ≤ 1.0, with frbw, frbz amplified by B1w, B1z.

**Point C governs** (axial + Mw compression, small Mz tension relief). Solving for the maximum P:

- **LRFD (α = 1.0):** at P = 140 kips → B1w = 1.04, B1z = 1.69:
  0.829 + 0.486 − 0.317 = 0.998 ≈ 1.0 → **Pu,max ≈ 140 kips** (< φcPn = 169 kips ✓)
- **ASD (α = 1.6):** at P = 95 kips → B1w = 1.05, B1z = 1.79:
  0.846 + 0.497 − 0.343 = 1.00 → **Pa,max ≈ 95 kips** (< Pn/Ωc = 112 kips ✓)

Points A and B are verified non-critical (B: 0.66 at Pu = 140; A is in net tension with ratio ≪ 1).

### 6. Conclusion

| Result | LRFD | ASD |
|---|---|---|
| Maximum eccentric axial force | **≈ 140 kips** | **≈ 95 kips** |
| Governing check | §H2 Eq. H2-1 at point C (long-leg toe) | same |
| Governing flexural limit state | LTB about w-axis, Eq. F10-2 (βw = −5.48) | same |

The eccentric load (ew = −0.165 in., ez = +1.245 in. in principal axes) makes the long-leg toe (point C) critical under combined axial compression and major-axis bending, with P-δ amplification per Appendix 8 (the minor-axis amplifier B1z ≈ 1.7 is significant because Pe1z is small). The §H2 stress interaction limits the member to about **140 kips (LRFD) / 95 kips (ASD)** — roughly 83% of its concentric compressive capacity.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — E.14B (from figures/E_14B.png)

Single angle L8×4×½, shown in 3-D with the load point on the attached long leg.

- Long (attached) leg width **b = 8.00 in.**; short leg **d = 4.00 in.**;
  thickness **t = ½ in.**
- The eccentric axial load **Pᵣ** is applied on the long leg at **mid-width
  (b/2 = 4.00 in.)** and **0.75t = 0.375 in.** from the outer face of that leg.
- Cross-section corner points: **A** = toe of the short leg, **B** = heel
  (where the two legs meet), **C** = toe of the long leg.
- Principal axes shown: **w** (major, running along the long leg direction) and
  **z** (minor, transverse). The load offset produces bending about both w and z.
