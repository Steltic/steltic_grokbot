<!-- chunk_id: MultiLinear_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MultiLinear.html",
 "title": "4.14.5.20. MultiLinear",
 "category": "general",
 "command": "MultiLinear",
 "doc_section": "src",
 "rel_path": "src/MultiLinear.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 568,
 "word_count": 52,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.20. MultiLinear

**uniaxialMaterial(*'MultiLinear'*, *matTag*, **pts*)**

This command is used to construct a uniaxial multilinear material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `pts` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of strain and stress points `pts = [strain1, stress1, strain2, stress2, ..., ]` |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/MultiLinear_Material)
