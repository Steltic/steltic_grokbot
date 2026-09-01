<!-- chunk_id: PlateFiber_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PlateFiber.html",
 "title": "4.15.1.9. PlateFiber",
 "category": "general",
 "command": "PlateFiber",
 "doc_section": "src",
 "rel_path": "src/PlateFiber.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 524,
 "word_count": 56,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.9. PlateFiber

**nDMaterial(*'PlateFiber'*, *matTag*, *threeDTag*)**

This command is used to construct a plate-fiber material wrapper which converts any three-dimensional material into a plate fiber material (by static condensation) appropriate for shell analysis.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `threeDTag` ([float](https://docs.python.org/3/library/functions.html#float)) | material tag for a previously-defined three-dimensional material |
