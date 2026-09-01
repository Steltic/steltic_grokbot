<!-- chunk_id: E.10_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "E.10",
 "example_family": "E.10",
 "chapter": "E",
 "topic": "HSS / rectangular-pipe compression",
 "clauses": [
  "E2",
  "E3",
  "E7",
  "E1",
  "E7.1"
 ],
 "eqs": [
  "E3-2",
  "E3-4",
  "E7-1",
  "E7-2",
  "E7-3",
  "E7-5"
 ],
 "tables": [
  "E7.1",
  "B4.1a"
 ],
 "title": "Rectangular HSS Compression Member with Slender Walls",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE E.10 — Rectangular HSS Compression Member with Slender Walls",
 "question": "# E.10 — Rectangular HSS compression member with slender walls (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn HSS12×8×3⁄16 rectangular hollow structural section is used as an axial compression\nmember with an effective length of L_c = 24 ft about both axes (base and top both\npinned). The steel is ASTM A500/A500M Grade C (F_y = 50 ksi). All four walls are\nslender in uniform compression, so the effective-area provisions of §E7 apply.\nUsing AISC 360-22 by hand calculation, determine the available compressive strength\n(LRFD and ASD).\n\n## Given\n- Material: ASTM A500/A500M Grade C (rectangular HSS), F_y = 50 ksi, E = 29,000 ksi.\n- Member: HSS12×8×3⁄16, with A_g = 6.76 in.², design wall t = 0.174 in.,\n  r_x = 4.56 in., r_y = 3.35 in., b/t = 43.0 (narrow wall), h/t = 66.0 (wide wall).\n- Geometry: effective length L_c = 24.0 ft about both axes (pinned-pinned, K = 1.0).\n- Loads: determine available strength (no specific demand specified).\n- Code basis: AISC 360-22.\n\n## Find\nThe nominal stress F_n, the effective area A_e (with any wall local-buckling\nreduction), and the available compressive strength φ_cP_n and P_n/Ω_c.",
 "has_figure": false,
 "stem": "E_10",
 "breadcrumb": "EXAMPLE E.10 · AISC 360-22 Ch.E (HSS / rectangular-pipe compression) · §E2 §E3 §E7 §E1 §E7.1 · Rectangular HSS Compression Member with Slender Walls",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE E.10 · AISC 360-22 Ch.E (HSS / rectangular-pipe compression) · §E2 §E3 §E7 §E1 §E7.1 · Rectangular HSS Compression Member with Slender Walls

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, Chapter E: §E2 (effective length), §E3 (Eqs. E3-2/E3-4), §E7 (Eqs. E7-1, E7-2, E7-3, E7-5; Table E7.1), Table B4.1a Case 6. φc = 0.90, Ωc = 1.67 (§E1). Per the RAG extract provided.

---

### 1. Design Data

| Item | Value |
|---|---|
| Section | HSS12x8x3/16, A500/A500M Gr. C (Fy = 50 ksi, E = 29,000 ksi) |
| Properties | Ag = 6.76 in.²; t = 0.174 in.; rx = 4.56 in.; ry = 3.35 in.; b/t = 43.0; h/t = 66.0 |
| Effective length | Lc = 24.0 ft = 288 in., both axes (K = 1.0) |

### 2. Slenderness Classification — Table B4.1a, Case 6

λr = 1.40√(E/Fy) = 1.40√(29,000/50) = 33.7

b/t = 43.0 > 33.7 and h/t = 66.0 > 33.7 → **all walls slender** under uniform compression → §E7 applies (Pn = FnAe, Eq. E7-1), with Fn from §E3.

### 3. Nominal Stress Fn — §E3

Governing slenderness (y-axis): Lc/ry = 288/3.35 = 86.0 (≤ 200, §E2 User Note ✓)

Fe = π²E/(Lc/r)² = π²(29,000)/(86.0)² = **38.7 ksi** (Eq. E3-4)

4.71√(E/Fy) = 113 > 86.0 → inelastic buckling (Eq. E3-2):

Fn = (0.658^(Fy/Fe))Fy = (0.658^(50/38.7))(50) = (0.658^1.291)(50) = **29.1 ksi**

### 4. Effective Area Ae — §E7.1

Effective-width check (Eqs. E7-2/E7-3): walls are fully effective when λ ≤ λr√(Fy/Fn):

λr√(Fy/Fn) = 33.7√(50/29.1) = **44.2**

**Narrow walls (b/t = 43.0 ≤ 44.2):** fully effective, be = b (Eq. E7-2).

**Wide walls (h/t = 66.0 > 44.2):** reduced per Eq. E7-3 with Table E7.1(b) (walls of rectangular HSS): c1 = 0.20, c2 = 1.38.

Fel = (c2 λr/λ)²Fy = [1.38(33.7)/66.0]²(50) = (0.705)²(50) = **24.9 ksi** (Eq. E7-5)

√(Fel/Fn) = √(24.9/29.1) = 0.924

he = h[1 − c1√(Fel/Fn)]√(Fel/Fn) = h[1 − 0.20(0.924)](0.924) = **0.753h** (Eq. E7-3)

With h = (h/t)t = 66.0(0.174) = 11.48 in.: he = 8.65 in.; ineffective length per wide wall = 11.48 − 8.65 = 2.83 in.

Ae = Ag − 2(2.83)(0.174) = 6.76 − 0.99 = **5.77 in.²**

### 5. Available Compressive Strength — §E7, Eq. E7-1

Pn = Fn Ae = 29.1(5.77) = **168 kips**

- **LRFD:** φcPn = 0.90(168) = **151 kips**
- **ASD:** Pn/Ωc = 168/1.67 = **101 kips**

### 6. Summary and Conclusion

| Quantity | Value | Reference |
|---|---|---|
| Lc/r (governing) | 86.0 (y-axis) | §E2 |
| Fe | 38.7 ksi | Eq. E3-4 |
| Fn | 29.1 ksi | Eq. E3-2 |
| Ae | 5.77 in.² (wide walls reduced) | Eqs. E7-2/3/5, Table E7.1(b) |
| φcPn / Pn,Ωc | **151 kips / 101 kips** | Eq. E7-1 |

The HSS12x8x3/16 with Lc = 24 ft provides an available compressive strength of **151 kips (LRFD)** and **101 kips (ASD)**. Only the two 12-in. (wide) walls require an effective-width reduction at the governing stress level; the 8-in. walls remain fully effective (43.0 ≤ 44.2). The local-buckling reduction costs about 15% of the gross area capacity.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
