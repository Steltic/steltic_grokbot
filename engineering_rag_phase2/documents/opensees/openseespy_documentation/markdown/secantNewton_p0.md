<!-- chunk_id: secantNewton_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/secantNewton.html",
 "title": "5.5.6. SecantNewton Algorithm",
 "category": "analysis",
 "command": "secantNewton",
 "doc_section": "src",
 "rel_path": "src/secantNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 781,
 "word_count": 81,
 "has_code": false,
 "has_table": true
} -->

## 5.5.6. SecantNewton Algorithm

**algorithm(*'SecantNewton'*, *iterate='current'*, *increment='current'*, *maxDim=3*)**

Create a SecantNewton algorithm which uses the two-term update to accelerate the convergence of the ModifiedNewton.

The default “cut-out” values recommended by Crisfield (R1=3.5, R2=0.3) are used.

| `iterate` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to iterate on, `'current'`, `'initial'`, `'noTangent'` (optional) |
| --- | --- |
| `increment` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to increment on, `'current'`, `'initial'`, `'noTangent'` (optional) |
| `maxDim` ([int](https://docs.python.org/3/library/functions.html#int)) | Max number of iterations until the tangent is reformed and the acceleration restarts. (optional) |
