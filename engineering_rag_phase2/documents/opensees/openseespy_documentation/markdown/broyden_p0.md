<!-- chunk_id: broyden_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/broyden.html",
 "title": "5.5.10. Broyden Algorithm",
 "category": "analysis",
 "command": "broyden",
 "doc_section": "src",
 "rel_path": "src/broyden.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 627,
 "word_count": 68,
 "has_code": false,
 "has_table": true
} -->

## 5.5.10. Broyden Algorithm

**algorithm(*'Broyden'*, *secant=False*, *initial=False*, *count=10*)**

Create a Broyden algorithm for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.

| `secant` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use secant stiffness. (optional) |
| --- | --- |
| `initial` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use initial stiffness.(optional) |
| `count` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of iterations. (optional) |
