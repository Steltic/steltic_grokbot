<!-- chunk_id: PlaneStrain_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PlaneStrain.html",
 "title": "4.15.1.6. PlaneStrain",
 "category": "general",
 "command": "PlaneStrain",
 "doc_section": "src",
 "rel_path": "src/PlaneStrain.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 605,
 "word_count": 69,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.6. PlaneStrain

**nDMaterial(*'PlaneStrain'*, *matTag*, *mat3DTag*)**

This command is used to construct a plane-stress material wrapper which converts any three-dimensional material into a plane strain material by imposing plain strain conditions on the three-dimensional material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `mat3DTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag of previously defined 3d ndMaterial material |

The material formulations for the PlaneStrain object are:

- `'PlaneStrain'`
