<!-- chunk_id: bfgs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/bfgs.html",
 "title": "5.5.9. BFGS Algorithm",
 "category": "analysis",
 "command": "bfgs",
 "doc_section": "src",
 "rel_path": "src/bfgs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 954,
 "word_count": 120,
 "has_code": false,
 "has_table": true
} -->

## 5.5.9. BFGS Algorithm

**algorithm(*'BFGS'*, *secant=False*, *initial=False*, *count=10*)**

Create a BFGS algorithm.  The BFGS method is one of the most effective matrix-update or quasi Newton methods for iteration on a nonlinear system of equations. The method computes new search directions at each iteration step based on the initial jacobian, and subsequent trial solutions. The unlike regular Newton does not require the tangent matrix be reformulated and refactored at every iteration, however unlike ModifiedNewton it does not rely on the tangent matrix from a previous iteration.

| `secant` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use secant stiffness. (optional) |
| --- | --- |
| `initial` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use initial stiffness.(optional) |
| `count` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of iterations. (optional) |
