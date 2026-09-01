<!-- chunk_id: ConcreteD_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ConcreteD.html",
 "title": "4.14.2.9. ConcreteD",
 "category": "general",
 "command": "ConcreteD",
 "doc_section": "src",
 "rel_path": "src/ConcreteD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1648,
 "word_count": 154,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.9. ConcreteD

**uniaxialMaterial(*'ConcreteD'*, *matTag*, *fc*, *epsc*, *ft*, *epst*, *Ec*, *alphac*, *alphat*, *cesp=0.25*, *etap=1.15*)**

This command is used to construct a concrete material based on the Chinese design code.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete compressive strength |
| `epsc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at corresponding to compressive strength |
| `ft` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete tensile strength |
| `epst` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at corresponding to tensile strength |
| `Ec` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete initial Elastic modulus |
| `alphac` ([float](https://docs.python.org/3/library/functions.html#float)) | compressive descending parameter |
| `alphat` ([float](https://docs.python.org/3/library/functions.html#float)) | tensile descending parameter |
| `cesp` ([float](https://docs.python.org/3/library/functions.html#float)) | plastic parameter, recommended values: 0.2~0.3 |
| `etap` ([float](https://docs.python.org/3/library/functions.html#float)) | plastic parameter, recommended values: 1.0~1.3 |

Note

1. Concrete compressive strength and the corresponding strain should be input as negative values.
2. The value `fc/epsc` and `ft/epst` should be smaller than `Ec`.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ConcreteD)
