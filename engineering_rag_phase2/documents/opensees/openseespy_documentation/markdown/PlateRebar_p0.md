<!-- chunk_id: PlateRebar_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PlateRebar.html",
 "title": "4.15.3.2. PlateRebar",
 "category": "general",
 "command": "PlateRebar",
 "doc_section": "src",
 "rel_path": "src/PlateRebar.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 597,
 "word_count": 59,
 "has_code": false,
 "has_table": true
} -->

## 4.15.3.2. PlateRebar

**nDMaterial(*'PlateRebar'*, *matTag*, *pre_def_matTag*, *sita*)**

This command is used to create the multi-dimensional reinforcement material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | new integer tag identifying material deriving from pre-defined uniaxial material |
| --- | --- |
| `pre_def_matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying uniaxial material |
| `sita` ([float](https://docs.python.org/3/library/functions.html#float)) | define the angle of reinforcement layer, 90 (longitudinal), 0 (tranverse) |
