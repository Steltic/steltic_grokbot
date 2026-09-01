<!-- chunk_id: steel01thermal_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/steel01thermal.html",
 "title": "4.14.1.8. Steel01Thermal",
 "category": "general",
 "command": "steel01thermal",
 "doc_section": "src",
 "rel_path": "src/steel01thermal.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1387,
 "word_count": 137,
 "has_code": false,
 "has_table": true
} -->

## 4.14.1.8. Steel01Thermal

**uniaxialMaterial(*'Steel01Thermal'*, *matTag*, *Fy*, *E0*, *b*, *a1*, *a2*, *a3*, *a4*)**

This command is the thermal version for `'Steel01'`.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield strength |
| `E0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic tangent |
| `b` ([float](https://docs.python.org/3/library/functions.html#float)) | strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent) |
| `a1` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of compression yield envelope as proportion of yield strength after a plastic strain of \(a_2*(F_y/E_0)\) (optional) |
| `a2` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under `a1`). (optional). |
| `a3` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of tension yield envelope as proportion of yield strength after a plastic strain of \(a_4*(F_y/E_0)\). (optional) |
| `a4` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under `a3`). (optional) |
