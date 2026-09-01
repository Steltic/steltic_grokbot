<!-- chunk_id: periodicNewton_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/periodicNewton.html",
 "title": "5.5.8. PeriodicNewton Algorithm",
 "category": "analysis",
 "command": "periodicNewton",
 "doc_section": "src",
 "rel_path": "src/periodicNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 647,
 "word_count": 61,
 "has_code": false,
 "has_table": true
} -->

## 5.5.8. PeriodicNewton Algorithm

**algorithm(*'PeriodicNewton'*, *iterate='current'*, *increment='current'*, *maxDim=3*)**

Create a PeriodicNewton algorithm using periodic accelerator.

| `iterate` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to iterate on, `'current'`, `'initial'`, `'noTangent'` (optional) |
| --- | --- |
| `increment` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to increment on, `'current'`, `'initial'`, `'noTangent'` (optional) |
| `maxDim` ([int](https://docs.python.org/3/library/functions.html#int)) | Max number of iterations until the tangent is reformed and the acceleration restarts. (optional) |
