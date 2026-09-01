<!-- chunk_id: krylovNewton_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/krylovNewton.html",
 "title": "5.5.5. Krylov-Newton Algorithm",
 "category": "analysis",
 "command": "krylovNewton",
 "doc_section": "src",
 "rel_path": "src/krylovNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 709,
 "word_count": 71,
 "has_code": false,
 "has_table": true
} -->

## 5.5.5. Krylov-Newton Algorithm

**algorithm(*'KrylovNewton'*, *iterate='current'*, *increment='current'*, *maxDim=3*)**

Create a KrylovNewton algorithm which uses a Krylov subspace accelerator to accelerate the convergence of the ModifiedNewton.

| `iterate` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to iterate on, `'current'`, `'initial'`, `'noTangent'` (optional) |
| --- | --- |
| `increment` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Tangent to increment on, `'current'`, `'initial'`, `'noTangent'` (optional) |
| `maxDim` ([int](https://docs.python.org/3/library/functions.html#int)) | Max number of iterations until the tangent is reformed and the acceleration restarts. (optional) |
