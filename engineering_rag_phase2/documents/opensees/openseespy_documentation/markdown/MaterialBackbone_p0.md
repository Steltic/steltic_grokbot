<!-- chunk_id: MaterialBackbone_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MaterialBackbone.html",
 "title": "4.14.5.40.1.6. MaterialBackbone",
 "category": "material",
 "command": "MaterialBackbone",
 "doc_section": "src",
 "rel_path": "src/MaterialBackbone.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 502,
 "word_count": 55,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.40.1.6. MaterialBackbone

**hystereticBackbone(*'Material'*, *backboneTag*, *matTag*, *'-compression'*)**

The backbone function treats a uniaxial material as a hysteretic backbone by removing path dependency, i.e. commitState is never called on the uniaxial material.

| `backboneTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the backbone function. |
| --- | --- |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for a predefined uniaxial material |
