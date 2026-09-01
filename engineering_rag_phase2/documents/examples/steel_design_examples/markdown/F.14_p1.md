<!-- chunk_id: F.14_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "F.14",
 "example_family": "F.14",
 "chapter": "F",
 "topic": "beam flexure",
 "clauses": [
  "F4",
  "F13.2",
  "G2.1",
  "G1",
  "F5"
 ],
 "eqs": [
  "F4-1",
  "F4-2",
  "F4-5",
  "F4-12",
  "G2-1",
  "G2-4",
  "F1-1"
 ],
 "tables": [
  "B4.1b"
 ],
 "title": "Welded Plate-Girder Flexural Member (Noncompact Web)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE F.14 — Welded Plate-Girder Flexural Member (Noncompact Web)",
 "question": "# F.14 — Welded plate-girder flexural member (noncompact web)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nVerify a doubly symmetric welded built-up I-shaped plate girder for flexure and shear. The\ngirder is simply supported, carries a concentrated dead and live load at midspan plus its own\nuniformly distributed self-weight, and is laterally braced at the quarter points and ends. The\ncross section has a **noncompact web** and compact flanges. Confirm that the available\nflexural strength (LRFD and ASD) exceeds the required moment, that the available shear\nstrength exceeds the required shear, and that the live-plus-dead deflection is within the\n1-in. limit.\n\n## Given\n- Material: ASTM A572/A572M Grade 50 (Fy = 50 ksi, Fu = 65 ksi, E = 29,000 ksi).\n- Cross section (built-up I): flanges 14 in. × 2 in.; web 62 in. × 1/2 in.; overall depth\n  d = 66 in.; h = 62 in., h_o = 64 in. Derived section properties: I_x = 67,300 in.⁴,\n  S_xc = S_xt = 2,040 in.³, Z_x = 2,270 in.³, J = 77.3 in.⁴.\n- Geometry / span: simply supported, L = 50 ft, laterally braced at the ends and quarter\n  points (unbraced length L_b = 12.5 ft). Transverse stiffener spacing gives a/h = 4.83.\n- Loads: concentrated at midspan P_D = 240 kips, P_L = 160 kips; self-weight w = 0.296 kip/ft.\n- Serviceability: total deflection limited to 1.00 in.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nThe required moment and shear; the governing flexural limit state with φ_b M_n and M_n/Ω_b;\nthe available shear strength φ_v V_n and V_n/Ω_v; and the deflection check.",
 "has_figure": false,
 "stem": "F_14",
 "breadcrumb": "EXAMPLE F.14 · AISC 360-22 Ch.F (beam flexure) · §F4 §F13.2 §G2.1 §G1 §F5 · Welded Plate-Girder Flexural Member (Noncompact Web)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE F.14 · AISC 360-22 Ch.F (beam flexure) · §F4 §F13.2 §G2.1 §G1 §F5 · Welded Plate-Girder Flexural Member (Noncompact Web)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22: §F4 (Eqs. F4-1, F4-2, F4-5 through F4-12), Table B4.1b (Cases 11, 15), §F13.2, §G2.1 (Eqs. G2-1, G2-4), Eq. F1-1 (Cb). φb = 0.90/Ωb = 1.67; φv = 0.90/Ωv = 1.67 (§G1). Per the RAG extract provided.

---

### 1. Required Strengths

L = 50 ft simple span; PD = 240 kips, PL = 160 kips at midspan; self-weight w = 0.296 kip/ft; Lb = 12.5 ft.

- **LRFD:** Pu = 1.2(240) + 1.6(160) = 544 kips; wu = 0.355 kip/ft
  Mu = 544(50)/4 + 0.355(50)²/8 = 6,800 + 111 = **6,910 kip-ft**; Vu = 272 + 8.9 = **281 kips**
- **ASD:** Pa = 400 kips; wa = 0.296 kip/ft
  Ma = 5,000 + 92.5 = **5,090 kip-ft**; Va = 200 + 7.4 = **207 kips**

### 2. Classification (Table B4.1b)

Flanges (Case 11): b/2tf = 7.00/2.00 = 3.50 ≤ λpf = 0.38√(E/Fy) = 9.15 → **compact**.
Web (Case 15): h/tw = 62/0.50 = 124; λpw = 3.76√(E/Fy) = 90.6; λrw = 5.70√(E/Fy) = 137 → 90.6 < 124 < 137 → **noncompact web → §F4 applies** (not §F5). Proportioning: aw = 1.11 ≤ 10 ✓ (§F13.2).

### 3. Flexure — §F4

**Web plastification factor (Eq. F4-9b, Iyc/Iy = 0.5 > 0.23):**
Mp = FyZx = 50(2,270) = 113,500 kip-in. ≤ 1.6FySx ✓; Myc = FySxc = 50(2,040) = 102,000 kip-in.
Rpc = 1.113 − (0.113)[(124 − 90.6)/(137 − 90.6)] = **1.03**

**LTB parameters:** aw = hctw/(bfctfc) = 62(0.5)/[14(2)] = 1.11 (Eq. F4-12); rt = 14/√[12(1 + 1.11/6)] = **3.71 in.** (Eq. F4-11)
Lp = 1.1rt√(E/Fy) = 98.4 in. = 8.20 ft (Eq. F4-7); FL = 0.7Fy = 35 ksi (Eq. F4-6a, Sxt = Sxc)
J/(Sxcho) = 77.3/[2,040(64)] = 5.92 × 10⁻⁴ → Lr = 1.95rt(E/FL)√[…] = 369 in. = **30.8 ft** (Eq. F4-8)

Lp = 8.20 ft < Lb = 12.5 ft ≤ Lr → **Eq. F4-2**, with Cb = 1.25 for the critical (inner) segment per Eq. F1-1:

Mn = Cb[RpcMyc − (RpcMyc − FLSxc)((Lb − Lp)/(Lr − Lp))] ≤ RpcMyc
= 1.25[105,300 − (105,300 − 71,400)(0.191)] = 1.25(98,800) = 123,200 → **capped at RpcMyc = 105,300 kip-in.**

Compression-flange local buckling: N/A (compact); tension-flange yielding: N/A (Sxt = Sxc).

**Governing limit state: compression flange yielding (Eq. F4-1), Mn = 105,300 kip-in. = 8,770 kip-ft**

- **LRFD:** φbMn = 0.90(8,770) = **7,890 kip-ft** ≥ 6,910 kip-ft ✓ (0.88)
- **ASD:** Mn/Ωb = 8,770/1.67 = **5,250 kip-ft** ≥ 5,090 kip-ft ✓ (0.97)

### 4. Shear — §G2.1(b)

Aw = dtw = 66(0.50) = 33.0 in.²; a/h = 4.83 > 3.0 → kv = 5.34.
1.10√(kvE/Fy) = 61.2 < h/tw = 124 → Cv1 = 61.2/124 = 0.494 (Eq. G2-4)

Vn = 0.6FyAwCv1 = 0.6(50)(33.0)(0.494) = **489 kips** (Eq. G2-1)

- **LRFD:** φvVn = 0.90(489) = **440 kips** ≥ 281 kips ✓
- **ASD:** Vn/Ωv = 489/1.67 = **293 kips** ≥ 207 kips ✓

### 5. Deflection (service D + L, limit 1.00 in.)

Δ = PL³/(48EIx) + 5wL⁴/(384EIx) = 400(600)³/[48(29,000)(67,300)] + 5(0.0247)(600)⁴/[384(29,000)(67,300)]
Δ = 0.92 + 0.02 = **0.94 in. ≤ 1.00 in. ✓**

### 6. Conclusion

The welded 14×2 flange / 62×1/2 web plate girder is **adequate in flexure, shear, and deflection**. With the noncompact web, §F4 governs: the Cb-amplified LTB strength exceeds the cap, so **compression flange yielding (Eq. F4-1, Mn = RpcMyc with Rpc = 1.03)** is the controlling flexural limit state. ASD flexure is the tightest check at 97% utilization; the stiffened web (a/h = 4.83, kv = 5.34) provides ample shear capacity.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
