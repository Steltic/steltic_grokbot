<!-- chunk_id: ImpactMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ImpactMaterial.html",
 "title": "4.14.5.14. Impact Material",
 "category": "material",
 "command": "ImpactMaterial",
 "doc_section": "src",
 "rel_path": "src/ImpactMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 723,
 "word_count": 61,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.14. Impact Material

**uniaxialMaterial(*'ImpactMaterial'*, *matTag*, *K1*, *K2*, *sigy*, *gap*)**

This command is used to construct an impact material object

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `K1` ([float](https://docs.python.org/3/library/functions.html#float)) | initial stiffness |
| `K2` ([float](https://docs.python.org/3/library/functions.html#float)) | secondary stiffness |
| `sigy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield displacement |
| `gap` ([float](https://docs.python.org/3/library/functions.html#float)) | initial gap |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Impact_Material)
