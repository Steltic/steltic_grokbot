<!-- chunk_id: newton_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/newton.html",
 "title": "5.5.2. Newton Algorithm",
 "category": "analysis",
 "command": "newton",
 "doc_section": "src",
 "rel_path": "src/newton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 726,
 "word_count": 78,
 "has_code": false,
 "has_table": true
} -->

## 5.5.2. Newton Algorithm

**algorithm(*'Newton'*, *secant=False*, *initial=False*, *initialThenCurrent=False*)**

Create a Newton-Raphson algorithm. The Newton-Raphson method is the most widely used and most robust method for solving nonlinear algebraic equations.

| `secant` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use secant stiffness. (optional) |
| --- | --- |
| `initial` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use initial stiffness.(optional) |
| `initialThenCurrent` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use initial stiffness on first step, then use current stiffness for subsequent steps. (optional) |
