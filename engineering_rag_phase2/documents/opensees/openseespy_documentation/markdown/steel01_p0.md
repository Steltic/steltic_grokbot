<!-- chunk_id: steel01_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/steel01.html",
 "title": "4.14.1.1. Steel01",
 "category": "general",
 "command": "steel01",
 "doc_section": "src",
 "rel_path": "src/steel01.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1629,
 "word_count": 174,
 "has_code": false,
 "has_table": true
} -->

## 4.14.1.1. Steel01

**uniaxialMaterial(*'Steel01'*, *matTag*, *Fy*, *E0*, *b*, *a1*, *a2*, *a3*, *a4*)**

This command is used to construct a uniaxial bilinear steel material object with kinematic hardening and optional isotropic hardening described by a non-linear evolution equation (REF: Fedeas).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield strength |
| `E0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic tangent |
| `b` ([float](https://docs.python.org/3/library/functions.html#float)) | strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent) |
| `a1` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of compression yield envelope as proportion of yield strength after a plastic strain of \(a_2*(F_y/E_0)\) (optional) |
| `a2` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under `a1`). (optional). |
| `a3` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of tension yield envelope as proportion of yield strength after a plastic strain of \(a_4*(F_y/E_0)\). (optional) |
| `a4` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under `a3`). (optional) |

Note

If strain-hardening ratio is zero and you do not expect softening of your system use BandSPD solver.
