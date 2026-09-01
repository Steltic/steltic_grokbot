<!-- chunk_id: Concrete06_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Concrete06.html",
 "title": "4.14.2.5. Concrete06",
 "category": "general",
 "command": "Concrete06",
 "doc_section": "src",
 "rel_path": "src/Concrete06.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1637,
 "word_count": 153,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.5. Concrete06

**uniaxialMaterial(*'Concrete06'*, *matTag*, *fc*, *e0*, *n*, *k*, *alpha1*, *fcr*, *ecr*, *b*, *alpha2*)**

This command is used to construct a uniaxial concrete material object with tensile strength, nonlinear tension stiffening and compressive behavior based on Thorenfeldt curve.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete compressive strength (compression is negative) |
| `e0` ([float](https://docs.python.org/3/library/functions.html#float)) | strain at compressive strength |
| `n` ([float](https://docs.python.org/3/library/functions.html#float)) | compressive shape factor |
| `k` ([float](https://docs.python.org/3/library/functions.html#float)) | post-peak compressive shape factor |
| `alpha1` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_1\) parameter for compressive plastic strain definition |
| `fcr` ([float](https://docs.python.org/3/library/functions.html#float)) | tensile strength |
| `ecr` ([float](https://docs.python.org/3/library/functions.html#float)) | tensile strain at peak stress (fcr) |
| `b` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent of the tension stiffening curve |
| `alpha2` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_2\) parameter for tensile plastic strain definition |

Note

1. Compressive concrete parameters should be input as negative values.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Concrete06_Material)
