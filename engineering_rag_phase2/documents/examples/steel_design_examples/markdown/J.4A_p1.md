<!-- chunk_id: J.4A_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.4A",
 "example_family": "J.4",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J3.9",
  "J3.10"
 ],
 "eqs": [
  "J3-4"
 ],
 "tables": [],
 "title": "Slip-Critical Connection with Short-Slotted Holes",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.4A — Slip-Critical Connection with Short-Slotted Holes",
 "question": "# J.4A — Slip-Critical Connection with Short-Slotted Holes  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA bolted lap-type tension connection is to be designed as slip-critical. The\nconnection plates contain short-slotted holes oriented transverse (perpendicular) to\nthe direction of the applied load, and no fillers are present. The bolts are\n3/4-in.-diameter Group 120 high-strength bolts (e.g., ASTM F3125 Grade A325) in a\nconnection with two slip planes (double shear). The faying surfaces are uncoated\nclean mill scale (Class A, μ = 0.30), and washers are provided per the RCSC\nSpecification.\n\nThe connection transfers a service dead load of 17 kips and a service live load of\n51 kips. Determine the number of bolts required to prevent slip (slip resistance\nonly), for both LRFD and ASD.\n\n## Given\n- Fastener: 3/4-in.-dia. Group 120 bolts; two slip planes (ns = 2); minimum\n  pretension Tb = 28 kips (Table J3.1).\n- Faying surface: Class A, μ = 0.30; Du = 1.13; no fillers (hf = 1.0).\n- Holes: short-slotted, transverse to the load.\n- Loads: PD = 17 kips, PL = 51 kips.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nThe number of bolts required for the limit state of slip (LRFD and ASD).",
 "has_figure": false,
 "stem": "J_4A",
 "breadcrumb": "EXAMPLE J.4A · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.9 §J3.10 · Slip-Critical Connection with Short-Slotted Holes",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.4A · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.9 §J3.10 · Slip-Critical Connection with Short-Slotted Holes

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J3.9: Rn = μDuhfTbns (Eq. J3-4); for short-slotted holes perpendicular to the load, φ = 1.00, Ω = 1.50. Per the RAG extract provided.

---

### 1. Required Strength

P: D = 17 kips, L = 51 kips → **LRFD Pu = 102 kips; ASD Pa = 68.0 kips**

### 2. Slip Resistance per Bolt

3/4-in. Group 120, Tb = 28 kips (Table J3.1); Class A (μ = 0.30); Du = 1.13; hf = 1.0 (no fillers); ns = 2:

Rn = 0.30(1.13)(1.0)(28)(2) = **18.98 kips/bolt**

- **LRFD (φ = 1.00):** φrn = **19.0 kips**
- **ASD (Ω = 1.50):** rn/Ω = **12.7 kips**

### 3. Required Number of Bolts

- **LRFD:** n = 102/19.0 = 5.4 → **6 bolts**
- **ASD:** n = 68.0/12.7 = 5.4 → **6 bolts**

### 4. Conclusion

**Six 3/4-in. Group 120 slip-critical bolts** (double shear, Class A surfaces, short-slotted holes transverse to the load) prevent slip under the 102-kip (LRFD) / 68-kip (ASD) tension. Because the slots are perpendicular to the load, no φ/Ω penalty applies relative to standard holes. Bearing-type strength limit states must also be confirmed in the final design per §J3.10 (readily satisfied here, since φrn,shear = 35.8 kips/bolt ≫ slip values).

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
