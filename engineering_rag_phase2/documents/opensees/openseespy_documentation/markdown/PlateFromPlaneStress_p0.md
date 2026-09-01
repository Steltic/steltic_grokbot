<!-- chunk_id: PlateFromPlaneStress_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PlateFromPlaneStress.html",
 "title": "4.15.3.1. PlateFromPlaneStress",
 "category": "general",
 "command": "PlateFromPlaneStress",
 "doc_section": "src",
 "rel_path": "src/PlateFromPlaneStress.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 668,
 "word_count": 68,
 "has_code": false,
 "has_table": true
} -->

## 4.15.3.1. PlateFromPlaneStress

**nDMaterial(*'PlateFromPlaneStress'*, *matTag*, *pre_def_matTag*, *OutofPlaneModulus*)**

This command is used to create the multi-dimensional concrete material model that is based on the damage mechanism and smeared crack model.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | new integer tag identifying material deriving from pre-defined PlaneStress material |
| --- | --- |
| `pre_def_matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying PlaneStress material |
| `OutofPlaneModulus` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus for out of plane stresses |
