<!-- chunk_id: J.4B_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.4B",
 "example_family": "J.4",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J3.9"
 ],
 "eqs": [
  "J3-4"
 ],
 "tables": [],
 "title": "Slip-Critical Connection with Long-Slotted Holes Parallel to the Load",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.4B — Slip-Critical Connection with Long-Slotted Holes Parallel to the Load",
 "question": "# J.4B — Slip-Critical Connection with Long-Slotted Holes  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA bolted lap-type tension connection is to be designed as slip-critical. The\nconnection plates contain long-slotted holes oriented in the direction of the applied\nload, and no fillers are present. The bolts are 3/4-in.-diameter Group 120\nhigh-strength bolts (e.g., ASTM F3125 Grade A325) in a connection with two slip\nplanes (double shear). The faying surfaces are uncoated clean mill scale (Class A,\nμ = 0.30), and washers are provided per the RCSC Specification.\n\nThe connection transfers a service dead load of 17 kips and a service live load of\n51 kips. Determine the number of bolts required to prevent slip (slip resistance\nonly), for both LRFD and ASD. (This is the same connection and loading as the\nshort-slotted case, but with long-slotted holes parallel to the load.)\n\n## Given\n- Fastener: 3/4-in.-dia. Group 120 bolts; two slip planes (ns = 2); minimum\n  pretension Tb = 28 kips (Table J3.1).\n- Faying surface: Class A, μ = 0.30; Du = 1.13; no fillers (hf = 1.0).\n- Holes: long-slotted, in the direction of the load.\n- Loads: PD = 17 kips, PL = 51 kips.\n- Code basis: AISC 360-22 (loads per ASCE/SEI 7).\n\n## Find\nThe number of bolts required for the limit state of slip (LRFD and ASD).",
 "has_figure": false,
 "stem": "J_4B",
 "breadcrumb": "EXAMPLE J.4B · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.9 · Slip-Critical Connection with Long-Slotted Holes Parallel to the Load",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.4B · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J3.9 · Slip-Critical Connection with Long-Slotted Holes Parallel to the Load

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J3.9: Rn = μDuhfTbns (Eq. J3-4); for long-slotted holes, **φ = 0.70, Ω = 2.14**. Per the RAG extract provided.

---

### 1. Required Strength

Same connection and loads as Example J.4A: **Pu = 102 kips; Pa = 68.0 kips**

### 2. Slip Resistance per Bolt

Rn = 0.30(1.13)(1.0)(28)(2) = 18.98 kips/bolt (unchanged — slip resistance itself does not depend on hole type):

- **LRFD (φ = 0.70):** φrn = 0.70(18.98) = **13.3 kips**
- **ASD (Ω = 2.14):** rn/Ω = 18.98/2.14 = **8.87 kips**

### 3. Required Number of Bolts

- **LRFD:** n = 102/13.3 = 7.7 → **8 bolts**
- **ASD:** n = 68.0/8.87 = 7.7 → **8 bolts**

### 4. Conclusion

With long-slotted holes parallel to the load, the reduced reliability factors (φ = 0.70/Ω = 2.14 — reflecting the severe consequence of slip into a long slot) raise the requirement from six bolts (Example J.4A) to **eight 3/4-in. Group 120 slip-critical bolts**, a 33% premium for the slot orientation. Washer/plate-washer requirements for long slots per the RCSC Specification apply, and bearing-type limit states are again confirmed separately.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
