<!-- chunk_id: MultiAxialCyclicPlasticity_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MultiAxialCyclicPlasticity.html",
 "title": "4.15.1.7. MultiaxialCyclicPlasticity",
 "category": "general",
 "command": "MultiAxialCyclicPlasticity",
 "doc_section": "src",
 "rel_path": "src/MultiAxialCyclicPlasticity.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1315,
 "word_count": 119,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.7. MultiaxialCyclicPlasticity

**nDMaterial(*'MultiaxialCyclicPlasticity'*, *matTag*, *rho*, *K*, *G*, *Su*, *Ho*, *h*, *m*, *beta*, *KCoeff*)**

This command is used to construct an multiaxial Cyclic Plasticity model for clays

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | density |
| `K` ([float](https://docs.python.org/3/library/functions.html#float)) | buck modulus |
| `G` ([float](https://docs.python.org/3/library/functions.html#float)) | maximum (small strain) shear modulus |
| `Su` ([float](https://docs.python.org/3/library/functions.html#float)) | undrained shear strength, size of bounding surface \(R=\sqrt{8/3}*Su\) |
| `Ho` ([float](https://docs.python.org/3/library/functions.html#float)) | linear kinematic hardening modulus of bounding surface |
| `h` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening parameter |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening parameter |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | integration parameter, usually beta=0.5 |
| `KCoeff` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficient of earth pressure, K0 |
