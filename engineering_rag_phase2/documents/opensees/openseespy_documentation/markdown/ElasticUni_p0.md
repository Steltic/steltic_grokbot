<!-- chunk_id: ElasticUni_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElasticUni.html",
 "title": "4.14.3.1. Elastic Uniaxial Material",
 "category": "uniaxial_material",
 "command": "ElasticUni",
 "doc_section": "src",
 "rel_path": "src/ElasticUni.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 682,
 "word_count": 58,
 "has_code": false,
 "has_table": true
} -->

## 4.14.3.1. Elastic Uniaxial Material

**uniaxialMaterial(*'Elastic'*, *matTag*, *E*, *eta=0.0*, *Eneg=E*)**

This command is used to construct an elastic uniaxial material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | tangent |
| `eta` ([float](https://docs.python.org/3/library/functions.html#float)) | damping tangent (optional, default=0.0) |
| `Eneg` ([float](https://docs.python.org/3/library/functions.html#float)) | tangent in compression (optional, default=E) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Elastic_Uniaxial_Material)
