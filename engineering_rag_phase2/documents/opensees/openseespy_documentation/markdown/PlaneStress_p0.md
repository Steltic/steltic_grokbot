<!-- chunk_id: PlaneStress_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PlaneStress.html",
 "title": "4.15.1.5. PlaneStress",
 "category": "general",
 "command": "PlaneStress",
 "doc_section": "src",
 "rel_path": "src/PlaneStress.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 552,
 "word_count": 63,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.5. PlaneStress

**nDMaterial(*'PlaneStress'*, *matTag*, *mat3DTag*)**

This command is used to construct a plane-stress material wrapper which converts any three-dimensional material into a plane stress material via static condensation.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `mat3DTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of perviously defined 3d ndMaterial material |

The material formulations for the PlaneStress object are:

- `'Plane Stress'`
