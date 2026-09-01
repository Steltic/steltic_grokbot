<!-- chunk_id: linearAlgo_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/linearAlgo.html",
 "title": "5.5.1. Linear Algorithm",
 "category": "analysis",
 "command": "linearAlgo",
 "doc_section": "src",
 "rel_path": "src/linearAlgo.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 892,
 "word_count": 120,
 "has_code": false,
 "has_table": true
} -->

## 5.5.1. Linear Algorithm

**algorithm(*'Linear'*, *secant=False*, *initial=False*, *factorOnce=False*)**

Create a Linear algorithm which takes one iteration to solve the system of equations.

| `secant` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use secant stiffness. (optional) |
| --- | --- |
| `initial` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use initial stiffness. (optional) |
| `factorOnce` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to only set up and factor matrix once. (optional) |

Note

As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the -factorOnce option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.
