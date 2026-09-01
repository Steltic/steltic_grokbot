<!-- chunk_id: SAWS_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SAWS.html",
 "title": "4.14.5.9. SAWS Material",
 "category": "material",
 "command": "SAWS",
 "doc_section": "src",
 "rel_path": "src/SAWS.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2231,
 "word_count": 280,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.9. SAWS Material

**uniaxialMaterial(*'SAWS'*, *matTag*, *F0*, *FI*, *DU*, *S0*, *R1*, *R2*, *R3*, *R4*, *alpha*, *beta*)**

This file contains the class definition for SAWSMaterial. SAWSMaterial provides the implementation of a one-dimensional hysteretic model develeped as part of the CUREe Caltech wood frame project.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `F0` ([float](https://docs.python.org/3/library/functions.html#float)) | Intercept strength of the shear wall spring element for the asymtotic line to the envelope curve F0 > FI > 0 |
| `FI` ([float](https://docs.python.org/3/library/functions.html#float)) | Intercept strength of the spring element for the pinching branch of the hysteretic curve. (FI > 0). |
| `DU` ([float](https://docs.python.org/3/library/functions.html#float)) | Spring element displacement at ultimate load. (DU > 0). |
| `S0` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial stiffness of the shear wall spring element (S0 > 0). |
| `R1` ([float](https://docs.python.org/3/library/functions.html#float)) | Stiffness ratio of the asymptotic line to the spring element envelope curve. The slope of this line is R1 S0. (0 < R1 < 1.0). |
| `R2` ([float](https://docs.python.org/3/library/functions.html#float)) | Stiffness ratio of the descending branch of the spring element envelope curve. The slope of this line is R2 S0. ( R2 < 0). |
| `R3` ([float](https://docs.python.org/3/library/functions.html#float)) | Stiffness ratio of the unloading branch off the spring element envelope curve. The slope of this line is R3 S0. ( R3 1). |
| `R4` ([float](https://docs.python.org/3/library/functions.html#float)) | Stiffness ratio of the pinching branch for the spring element. The slope of this line is R4 S0. ( R4 > 0). |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | Stiffness degradation parameter for the shear wall spring element. (ALPHA > 0). |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | Stiffness degradation parameter for the spring element. (BETA > 0). |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/SAWS_Material)
