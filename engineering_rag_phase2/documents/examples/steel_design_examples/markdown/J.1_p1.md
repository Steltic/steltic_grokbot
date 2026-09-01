<!-- chunk_id: J.1_p1 | collection: steel_design_examples -->
<!-- meta: {
 "example_id": "J.1",
 "example_family": "J.1",
 "chapter": "J",
 "topic": "bolt / weld / connecting element",
 "clauses": [
  "J2.2b",
  "J2.4",
  "J4.2"
 ],
 "eqs": [],
 "tables": [
  "J2.5"
 ],
 "title": "Longitudinal Fillet-Welded Lap Splice (End-Loaded Welds)",
 "source": "AISC_manual_egs",
 "section": "EXAMPLE J.1 — Longitudinal Fillet-Welded Lap Splice (End-Loaded Welds)",
 "question": "# J.1 — Fillet Weld in Longitudinal Shear  (question)\n\n*Original problem statement, written by us. Not copied from the textbook.*\n\n## Question\nA tension splice transfers an axial load through a pair of longitudinal fillet\nwelds. A 1/4-in.-thick × 18-in.-wide plate is lapped onto a 3/4-in.-thick plate and\njoined to it by two longitudinal fillet welds, one along each long edge of the lap.\nEach weld is 3/16 in. (leg size) and 27 in. long, and the welds are loaded parallel\nto their longitudinal axis (end-loaded, θ = 0°). Both plates are ASTM A572/A572M\nGrade 50 steel and have already been sized for the member forces. The welds are\nmade with 70-ksi (E70XX) electrodes.\n\nThe connection carries a concentric axial service dead load of 33 kips and a service\nlive load of 100 kips. Confirm whether the indicated weld size and length are\nadequate to transfer the load (weld-metal shear rupture and base-metal strength),\nconsidering the end-loaded length effect.\n\n## Given\n- Material: plates ASTM A572/A572M Grade 50 (Fy = 50 ksi, Fu = 65 ksi); E70XX\n  electrodes (FEXX = 70 ksi).\n- Geometry: 1/4-in. × 18-in. lap plate fillet welded to a 3/4-in. plate; two\n  longitudinal fillet welds, each 3/16-in. leg × 27 in. long; load parallel to welds.\n- Loads: PD = 33 kips, PL = 100 kips (concentric axial).\n- Member / section: welds connect the two plates; plates already adequate.\n- Code basis: AISC 360-22 (loads combined per ASCE/SEI 7).\n\n## Find\nWhether the 3/16-in. × 27-in. two-sided longitudinal fillet weld is adequate\n(governing of weld-metal shear rupture and base-metal rupture), in both LRFD and ASD.",
 "has_figure": false,
 "stem": "J_1",
 "breadcrumb": "EXAMPLE J.1 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J2.2b §J2.4 §J4.2 · Longitudinal Fillet-Welded Lap Splice (End-Loaded Welds)",
 "part": 1,
 "nparts": 1
} -->

EXAMPLE J.1 · AISC 360-22 Ch.J (bolt / weld / connecting element) · §J2.2b §J2.4 §J4.2 · Longitudinal Fillet-Welded Lap Splice (End-Loaded Welds)

## Engineering Design Report

**Code basis:** ANSI/AISC 360-22, §J2.2b (end-loaded fillet weld length-reduction factor β = 1.2 − 0.002(l/w) for l/w > 100), §J2.4/Table J2.5 (Fnw = 0.60FEXX, φ = 0.75/Ω = 2.00), §J4.2 (base metal). Per the RAG extract provided.

---

### 1. Required Strength

P: D = 33 kips, L = 100 kips → **LRFD Pu = 200 kips; ASD Pa = 133 kips**

Two 3/16-in. E70 longitudinal fillets, 27 in. each, loaded parallel to their axes (θ = 0°, no directional increase).

### 2. End-Loaded Length Effect — §J2.2b

l/w = 27/0.1875 = **144 > 100** → β = 1.2 − 0.002(144) = **0.912** → effective length = 0.912(27) = 24.6 in. per weld.

### 3. Weld Strength

φRn = 2(1.392)(3)(24.6) = **206 kips ≥ 200 ✓** (LRFD, 97% utilized)
Rn/Ω = 2(0.928)(3)(24.6) = **137 kips ≥ 133 ✓** (ASD, 97%)

### 4. Base Metal — §J4.2

Shear rupture of the 1/4-in. lap plate along the two weld lines: φRn = 0.75(0.6)(65)(0.25)(2 × 27) = **395 kips** ✓; the 3/4-in. plate and member gross/net sections are pre-sized ✓. Minimum weld size for the 1/4-in. plate = 1/8 in. ≤ 3/16 ✓; maximum at its edge = 3/16 in. = provided ✓.

### 5. Conclusion

The two 3/16-in. × 27-in. longitudinal fillets are **adequate — just** (97% utilization in both LRFD and ASD) once the §J2.2b end-loaded reduction (β = 0.912) is applied. The example's lesson: for long end-loaded welds, the 14% effective-length penalty at l/w = 144 must not be overlooked, or the splice would be unconservatively rated. No increase is needed, but no reduction in length or size is possible.

---
*Design performed in accordance with ANSI/AISC 360-22 using the specification extracts (RAG) provided for this problem.*
