<!-- chunk_id: III-1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "III-1",
 "example_family": "III-1",
 "chapter": "III",
 "topic": "complete building design",
 "clauses": [
  "C2.2b",
  "12.8",
  "E"
 ],
 "eqs": [
  "A-8-6",
  "E3-1",
  "E3-2",
  "E3-4"
 ],
 "tables": [],
 "title": "Lateral Analysis of a Four-Story Building",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE III-1 — Lateral Analysis of a Four-Story Building",
 "question": "# III-1 — Lateral analysis of a four-story building (E-W moment frames + N-S braced frames)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA four-story steel office building measures **210 ft in the E-W direction**\n(7 bays @ 30.0 ft) and **120 ft in the N-S direction** (4 bays @ 30.0 ft). Story\nheights are 13.5 ft at the lower three stories and 14.5 ft at the roof, for a total\nheight *h_n* = 55.0 ft above grade. All steel is ASTM A992 (*F_y* = 50 ksi,\n*E* = 29,000 ksi).\n\nThe lateral force-resisting system is:\n- **E-W:** two perimeter **moment frames** on grid lines A and F. Each is a 7-bay\n  @ 30 ft rigid frame with **W14×90 columns and W24×55 beams**, fixed bases, and\n  fully restrained (continuous) beam-to-column joints. The interior gravity framing\n  carries no lateral load and \"leans\" on these two frames.\n- **N-S:** two **concentrically braced frames** on grid lines 1 and 8, in the C-D\n  bay (30 ft wide), configured as **chevron (inverted-V) bracing** over all four\n  stories (columns W14×90, beams W24×55; braces to be designed; pinned bases and\n  pinned brace ends).\n\nSeismic design parameters (already established for the site and building):\n*S_DS* = 0.129, *S_D1* = 0.096, response modification *R* = 3 (system not\nspecifically detailed for seismic), importance factor *I_e* = 1.0, approximate\nperiod *T_a* = 0.404 s, and total seismic weight *W* = 8,280 kips (≈ equal per\nfloor).\n\nUsing the **equivalent lateral force (ELF) procedure of ASCE/SEI 7-22** for the\nseismic load and the **direct analysis method of AISC 360-22 Chapter C** for the\nlateral analysis, determine, for LRFD:\n1. the seismic response coefficient *C_s*, the ELF base shear *V*, and the share\n   carried by one perimeter frame;\n2. the first-story drift of the E-W moment frame **including second-order (P-Δ)\n   effects** under the direct analysis method, the corresponding story stability\n   amplifier *B_2*, and confirmation that the interstory drifts satisfy the ASCE 7\n   drift limit;\n3. a **brace size** for the N-S chevron frame adequate for the design story shear,\n   with the controlling compression check per AISC 360 Chapter E.\n\n## Given\n- Geometry: 210 ft (7@30) E-W × 120 ft (4@30) N-S; stories 13.5/13.5/13.5/14.5 ft;\n  *h_n* = 55 ft.\n- Material: ASTM A992, *F_y* = 50 ksi, *E* = 29,000 ksi.\n- E-W frames (×2): W14×90 columns, W24×55 beams, fixed bases, FR joints.\n- N-S frames (×2): chevron CBF in the 30-ft C-D bay; W14×90 cols / W24×55 beams;\n  braces TBD; pinned.\n- Seismic: *S_DS* = 0.129, *S_D1* = 0.096, *R* = 3, *I_e* = 1.0, *T_a* = 0.404 s,\n  *W* = 8,280 kips.\n- Code basis: ASCE/SEI 7-22 (loads, ELF) + AISC 360-22 (stability and member strength).\n\n## Find\nThe ELF base shear and per-frame share; the E-W first-story second-order drift and\n*B_2* by the direct analysis method; and an N-S chevron brace design with its\nChapter E compression check. Results for LRFD.",
 "has_figure": false,
 "stem": "III_1",
 "breadcrumb": "EXAMPLE III-1 · AISC 360-22 III (complete building design) · §C2.2b §12.8 §E · Lateral Analysis of a Four-Story Building",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE III-1 · AISC 360-22 III (complete building design) · §C2.2b §12.8 §E · Lateral Analysis of a Four-Story Building

## Engineering Design Report

**Code basis:** ASCE/SEI 7-22 §12.8 (ELF procedure); ANSI/AISC 360-22 Chapter C (direct analysis method: 0.8τb stiffness, P-Δ via B2 per App. 8 Eqs. A-8-6/7/8) and Chapter E (Eqs. E3-1, E3-2, E3-4). LRFD. Per the RAG extract provided.

---

### 1. ELF Base Shear and Frame Share

Cs = SDS/(R/Ie) = 0.129/(3/1.0) = **0.0430** (upper limit SD1/[T(R/Ie)] = 0.096/[0.404(3)] = 0.0792 — not governing; minimum 0.01 — not governing)

**V = CsW = 0.0430(8,280) = 356 kips** (each direction)

Vertical distribution (k = 1.0 for T < 0.5 s; equal floor weights 2,070 kips at h = 13.5/27/40.5/55 ft):
F = 35.3 / 70.7 / 106 / 144 kips (floors 2–4, roof). Two identical frames per direction → **one perimeter frame carries V/2 = 178 kips** (first-story shear), i.e., 17.7/35.3/53.0/72.0 kips at the four levels.

### 2. E-W Moment Frame: First-Story Drift and B2 (Direct Analysis Method)

Frame: 7 bays @ 30 ft; 8 W14x90 columns (Ix = 999 in.⁴), W24x55 girders (Ix = 1,350 in.⁴), fixed bases; h = 13.5 ft = 162 in. Analysis stiffness = 0.8EI (τb = 1.0; column axial ratios low).

Story lateral stiffness (D-value method, fixed-base first story, reduced stiffness): interior columns ≈ 34.9 kip/in., exterior ≈ 27.8 kip/in. → ΣK ≈ **265 kip/in. per frame**

First-order drift at 0.8EI: ΔH = 178/265 = **0.67 in.** → HL/ΔH = 178(162)/0.67 = 43,000 kips

Leaning-column effects: Pstory (per frame) = 8,280/2 = 4,140 kips; Pmf ≈ 1,040 kips → RM = 1 − 0.15(0.25) = 0.96 (Eq. A-8-8); Pe,story = 0.96(43,000) = **41,300 kips** (Eq. A-8-7)

**B2 = 1/(1 − 4,140/41,300) = 1.11** (Eq. A-8-6) → second-order first-story drift (analysis basis) = 1.11(0.67) = **0.75 in.**

**ASCE 7 drift check (nominal stiffness):** elastic drift δe = 0.8(0.67)(1.09) = 0.58 in.; design drift = Cdδe/Ie = 3(0.58) = **1.75 in.** ≤ Δa = 0.020hsx = 0.020(162) = **3.24 in. ✓** (upper stories, with lower shears, comply by inspection). B2 = 1.11 ≤ 1.7 also confirms notional loads need apply only to gravity-only combinations (§C2.2b(d)).

### 3. N-S Chevron Brace Design (first story)

Geometry: half-bay 15 ft, rise 13.5 ft → brace length Lc = √(15² + 13.5²) = 20.2 ft = 242 in.; horizontal cosine = 15/20.2 = 0.743.

Per braced frame: story shear = 178 kips, shared by the tension/compression brace pair:
**Brace axial force Pu = (178/2)/0.743 = 120 kips (compression governs)**

**Try HSS6x6x5/16 (A500 Gr. C):** Ag = 6.43 in.²; r = 2.31 in.; b/t = 17.2 ≤ λr = 1.40√(E/Fy) = 33.7 → nonslender ✓

Lc/r = 242/2.31 = 105 ≤ 200 ✓; Fe = π²E/(105)² = 26.1 ksi (Eq. E3-4); Fy/Fe = 1.92 ≤ 2.25 → Fn = (0.658^1.92)(50) = 22.4 ksi (Eq. E3-2)

Pn = 22.4(6.43) = 144 kips → **φcPn = 0.90(144) = 130 kips ≥ 120 kips ✓ (utilization 0.93)**

(HSS6x6x1/4 gives φcPn = 108 kips < 120 — inadequate; the 5/16 wall is the lightest square HSS6 that works.)

### 4. Summary

| Item | Result |
|---|---|
| Cs; V | 0.0430; 356 kips |
| Per-frame first-story shear | 178 kips |
| E-W first-story drift (2nd order, DAM basis) | 0.75 in.; B2 = 1.11 |
| ASCE 7 drift check | 1.75 in. ≤ 3.24 in. ✓ |
| N-S brace (per first-story chevron leg) | **HSS6x6x5/16**, φcPn = 130 kips ≥ 120 kips |

### 5. Conclusion

The ELF base shear of 356 kips splits equally between the two frames in each direction. The E-W moment frame satisfies the ASCE 7 story-drift limit with a modest P-Δ amplification (B2 = 1.11 ≤ 1.7, validating the direct analysis assumptions, with leaning-column gravity included). For the N-S chevron braced frame, an **HSS6x6x5/16** brace satisfies the Chapter E compression check (inelastic flexural buckling at Lc/r = 105) at 93% utilization. Upper-story braces may be re-optimized for the smaller story shears; connection design and the chevron beam unbalanced-force check follow separately.

---
*Design performed in accordance with ANSI/AISC 360-22 and ASCE/SEI 7-22 using the specification extracts (RAG) provided for this problem.*
