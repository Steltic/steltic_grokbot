<!-- chunk_id: updateMaterialStage_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/updateMaterialStage.html",
 "title": "7.25. updateMaterialStage",
 "category": "material",
 "command": "updateMaterialStage",
 "doc_section": "src",
 "rel_path": "src/updateMaterialStage.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 636,
 "word_count": 69,
 "has_code": false,
 "has_table": true
} -->

## 7.25. updateMaterialStage

**updateMaterialStage(*'-material'*, *matTag*, *'-stage'*, *value*, *'-parameter'*, *paramTag*)**

This function is used in geotechnical modeling to maintain elastic nDMaterial response during the application of gravity loads. The material is then updated to allow for plastic strains during additional static loads or earthquakes.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of nDMaterial |
| --- | --- |
| `value` ([int](https://docs.python.org/3/library/functions.html#int)) | stage value |
| `paramTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of parameter (optional) |
