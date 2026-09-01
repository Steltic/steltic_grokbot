<!-- chunk_id: Viscous_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Viscous.html",
 "title": "4.14.5.30. Viscous Material",
 "category": "material",
 "command": "Viscous",
 "doc_section": "src",
 "rel_path": "src/Viscous.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 795,
 "word_count": 87,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.30. Viscous Material

**uniaxialMaterial(*'Viscous'*, *matTag*, *C*, *alpha*)**

This command is used to construct a uniaxial viscous material object. stress =C(strain-rate)^alpha

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `C` ([float](https://docs.python.org/3/library/functions.html#float)) | damping coeficient |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | power factor (=1 means linear damping) |

Note

1. This material can only be assigned to truss and zeroLength elements.
2. This material can not be combined in parallel/series with other materials. When defined in parallel with other materials it is ignored.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Viscous_Material)
