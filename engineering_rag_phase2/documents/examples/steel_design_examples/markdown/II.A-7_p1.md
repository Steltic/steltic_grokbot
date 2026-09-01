<!-- chunk_id: II.A-7_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "II.A-7",
 "example_family": "II.A-7",
 "chapter": "II.A",
 "topic": "simple / shear connection",
 "clauses": [
  "F11",
  "F11.2"
 ],
 "eqs": [
  "F11-1",
  "F11-3"
 ],
 "tables": [],
 "title": "Beam End Coped at Both Flanges",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE II.A-7 — Beam End Coped at Both Flanges",
 "question": "# II.A-7 — Beam End Coped at the Top and Bottom Flanges  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992 W16x40 beam is coped at both flanges: a 3-1/2-in.-deep by 9-1/2-in.-wide cope\nat the top flange and a 2-in.-deep by 9-1/2-in.-wide cope at the bottom flange, with a\n1/2-in. setback from the face of the support (moment arm e = 10.0 in.). Determine the\navailable strength of the coped beam end, considering flexural yielding and lateral-torsional\nbuckling of the remaining rectangular web section. See figures/IIA_7.png.\n\n## Given\n- Beam: ASTM A992 W16x40 (d = 16.0 in., t_w = 0.305 in., b_f = 7.00 in., t_f = 0.505 in.),\n  F_y = 50 ksi, F_u = 65 ksi.\n- Top cope: d_ct = 3-1/2 in., c_t = 9-1/2 in.; bottom cope: d_cb = 2 in., c_b = 9-1/2 in.\n- Remaining web depth h_c = d - d_ct - d_cb = 10.5 in.; setback 1/2 in.; e = 10.0 in.\n- Code basis: AISC 360-22 Section F11 (flexure of the rectangular coped web), with the\n  coped-section C_b from AISC Manual Eq. 9-21 and R_n = M_n/e from Manual Eq. 9-9.\n\n## Find\nThe available flexural strength of the coped section, expressed as an available end reaction\nphi_b R_n (LRFD) and R_n/Omega_b (ASD), governed by lateral-torsional buckling of the\nrectangular web per AISC 360 Section F11.2(b), capped at the plastic moment M_p.",
 "has_figure": true,
 "stem": "II_A_7",
 "breadcrumb": "EXAMPLE II.A-7 · AISC 360-22 II.A (simple / shear connection) · §F11 §F11.2 · Beam End Coped at Both Flanges",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE II.A-7 · AISC 360-22 II.A (simple / shear connection) · §F11 §F11.2 · Beam End Coped at Both Flanges

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22 §F11 (rectangular bars: Eqs. F11-1, F11-3) applied to the remaining rectangular web, with the coped-end Cb of AISC Manual Eq. 9-21 and the end-reaction conversion Rn = Mn/e (Manual Eq. 9-9). Per the RAG extract provided.

---

### 1. Coped-Section Geometry

W16x40 (A992): top cope 3 1/2 × 9 1/2 in.; bottom cope 2 × 9 1/2 in. → remaining rectangular web hc = 16.0 − 3.5 − 2.0 = **10.5 in. × tw = 0.305 in.**; e = 9.5 + 0.5 = **10.0 in.**; Lb = c = 9.5 in.

Section properties of the web rectangle:
Snet = twhc²/6 = 0.305(10.5)²/6 = **5.60 in.³**; Znet = twhc²/4 = **8.41 in.³**
My = FySnet = 280 kip-in.; Mp = FyZnet = **420 kip-in.** (≤ 1.6My = 448 ✓, Eq. F11-1)

### 2. Lateral-Torsional Buckling of the Web Rectangle — §F11.2

λ = Lbhc/tw² = 9.5(10.5)/(0.305)² = **1,070**
Limits: 0.08E/Fy = 46.4; 1.9E/Fy = 1,100 → 46.4 < 1,070 ≤ 1,100 → **inelastic LTB, Eq. F11-3:**

Mn = Cb[1.52 − 0.274(Lbhc/tw²)(Fy/E)]My = Cb[1.52 − 0.274(1,070)(0.001724)]My = Cb(1.01)My

With the coped-end moment-gradient factor Cb ≈ 1.84 (Manual Eq. 9-21 for the reaction-loaded coped segment):

Mn = 1.84(1.01)(280) = 522 kip-in. → **capped at Mp = 420 kip-in.** (Eq. F11-3 limit)

### 3. Available End Reaction (Rn = Mn/e)

- **LRFD:** φbRn = 0.90(420)/10.0 = **37.8 kips**
- **ASD:** Rn/(Ωbe) = (420/1.67)/10.0 = **25.2 kips**

(Web shear through hc: φRn = 0.6(50)(3.20) = 96.1 kips — not governing.)

### 4. Conclusion

With both flanges coped, the W16x40 end reduces to a 10.5 × 0.305 in. rectangular web whose strength is governed by **§F11 flexure: the LTB expression with Cb = 1.84 exceeds the plastic moment, so Mn = Mp = 420 kip-in.**, giving an available end reaction of **37.8 kips (LRFD) / 25.2 kips (ASD)**. The double cope is far more punishing than a single top cope (compare Example II.A-6); reactions above these values require cope reinforcement (doublers or extension plates) or a revised framing detail.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*

### Figure
# Figure-derived geometry — II.A-7 (from figures/IIA_7.png)

Beam W16×40 coped at **both flanges**, with a simple shear connection at the end.

- **Top cope:** depth **d_ct = 3½ in.**, length **c_t = 9½ in.**
- **Bottom cope:** depth **d_cb = 2 in.**, length **c_b = 9½ in.**
- ½-in. setback from the face of support (moment arm e = 10.0 in.).
- Remaining rectangular web depth between copes h_o = d − d_ct − d_cb =
  16.0 − 3½ − 2 = 10.5 in.
