<!-- chunk_id: modifiedNewton_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/modifiedNewton.html",
 "title": "5.5.4. Modified Newton Algorithm",
 "category": "analysis",
 "command": "modifiedNewton",
 "doc_section": "src",
 "rel_path": "src/modifiedNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 507,
 "word_count": 59,
 "has_code": false,
 "has_table": true
} -->

## 5.5.4. Modified Newton Algorithm

**algorithm(*'ModifiedNewton'*, *secant=False*, *initial=False*)**

Create a ModifiedNewton algorithm. The difference to Newton is that the tangent at the initial guess is used in the iterations, instead of the current tangent.

| `secant` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use secant stiffness. (optional) |
| --- | --- |
| `initial` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to indicate to use initial stiffness.(optional) |
