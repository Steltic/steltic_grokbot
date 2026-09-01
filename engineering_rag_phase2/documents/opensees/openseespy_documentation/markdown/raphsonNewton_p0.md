<!-- chunk_id: raphsonNewton_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/raphsonNewton.html",
 "title": "5.5.7. RaphsonNewton Algorithm",
 "category": "analysis",
 "command": "raphsonNewton",
 "doc_section": "src",
 "rel_path": "src/raphsonNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 463,
 "word_count": 42,
 "has_code": false,
 "has_table": true
} -->

## 5.5.7. RaphsonNewton Algorithm

**algorithm(*'RaphsonNewton'*, *iterate='current'*, *increment='current'*)**

Create a RaphsonNewton algorithm which uses Raphson accelerator.

| `iterate` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to iterate on, `'current'`, `'initial'`, `'noTangent'` (optional) |
| --- | --- |
| `increment` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to increment on, `'current'`, `'initial'`, `'noTangent'` (optional) |
