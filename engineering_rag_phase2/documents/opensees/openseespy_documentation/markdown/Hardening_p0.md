<!-- chunk_id: Hardening_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Hardening.html",
 "title": "4.14.5.1. Hardening Material",
 "category": "material",
 "command": "Hardening",
 "doc_section": "src",
 "rel_path": "src/Hardening.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1030,
 "word_count": 91,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.1. Hardening Material

**uniaxialMaterial(*'Hardening'*, *matTag*, *E*, *sigmaY*, *H_iso*, *H_kin*, *eta=0.0*)**

This command is used to construct a uniaxial material object with combined linear kinematic and isotropic hardening. The model includes optional visco-plasticity using a Perzyna formulation.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | tangent stiffness |
| `sigmaY` ([float](https://docs.python.org/3/library/functions.html#float)) | yield stress or force |
| `H_iso` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening Modulus |
| `H_kin` ([float](https://docs.python.org/3/library/functions.html#float)) | kinematic hardening Modulus |
| `eta` ([float](https://docs.python.org/3/library/functions.html#float)) | visco-plastic coefficient (optional, default=0.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Hardening_Material)
