<!-- chunk_id: G.2A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "G.2A",
 "example_family": "G.2",
 "chapter": "G",
 "topic": "beam shear",
 "clauses": [
  "G2.1",
  "G1"
 ],
 "eqs": [
  "G2-1",
  "G2-3"
 ],
 "tables": [],
 "title": "C15x33.9 Shear Strength (Manual Table Basis)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE G.2A — C15x33.9 Shear Strength (Manual Table Basis)",
 "question": "# G.2A -- Channel in Major-Axis Shear (Manual-table approach)  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nAn ASTM A992/A992M C15x33.9 channel carries end shears of 25 kips from service dead\nload and 75 kips from service live load, bent about its major axis. Using the AISC\n*Manual* available-shear tables (which apply AISC 360 Chapter G), verify the channel\nhas adequate major-axis shear strength for LRFD and ASD.\n\n## Given\n- Material: ASTM A992/A992M, Fy = 50 ksi.\n- Member: C15x33.9 (d = 15.0 in., tw = 0.400 in.).\n- Loads (service end shear): D = 25 kips, L = 75 kips.\n- Code basis: AISC 360-22 Chapter G; loads per ASCE/SEI 7 Ch. 2.\n\n## Find\nphi_v*Vn, Vn/Omega_v, and adequacy.",
 "has_figure": false,
 "stem": "G_2A",
 "breadcrumb": "EXAMPLE G.2A · AISC 360-22 Ch.G (beam shear) · §G2.1 §G1 · C15x33.9 Shear Strength (Manual Table Basis)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE G.2A · AISC 360-22 Ch.G (beam shear) · §G2.1 §G1 · C15x33.9 Shear Strength (Manual Table Basis)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §G2.1(b) (Eqs. G2-1, G2-3) with §G1 factors (φv = 0.90, Ωv = 1.67). Per the RAG extract provided.

---

### 1. Required Shear Strength

End shears: D = 25 kips, L = 75 kips:

- **LRFD:** Vu = 1.2(25) + 1.6(75) = **150 kips**
- **ASD:** Va = 25 + 75 = **100 kips**

### 2. Available Shear Strength — C15x33.9 (A992)

Aw = d·tw = 15.0(0.400) = 6.00 in.²

Channels do not qualify for the §G2.1(a) rolled-I provision, so §G2.1(b) applies with φv = 0.90, Ωv = 1.67 (§G1). Without transverse stiffeners, kv = 5.34; the web slenderness is well below 1.10√(kvE/Fy) = 61.2 → **Cv1 = 1.0** (Eq. G2-3).

Vn = 0.6FyAwCv1 = 0.6(50)(6.00)(1.0) = **180 kips** (Eq. G2-1)

- **LRFD:** φvVn = 0.90(180) = **162 kips** ≥ 150 kips ✓ (utilization 0.93)
- **ASD:** Vn/Ωv = 180/1.67 = **108 kips** ≥ 100 kips ✓ (utilization 0.93)

These equal the Manual tabulated values, which apply the same Chapter G provisions.

### 3. Conclusion

The C15x33.9 channel is **adequate in shear**: web yielding governs (Cv1 = 1.0), with φvVn = 162 kips (LRFD) and Vn/Ωv = 108 kips (ASD) versus required 150 / 100 kips. Note the channel uses the standard φv = 0.90/Ωv = 1.67 rather than the enhanced rolled-I factors.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
