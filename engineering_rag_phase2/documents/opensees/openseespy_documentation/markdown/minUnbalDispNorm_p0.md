<!-- chunk_id: minUnbalDispNorm_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/minUnbalDispNorm.html",
 "title": "5.6.1.4. Minimum Unbalanced Displacement Norm",
 "category": "general",
 "command": "minUnbalDispNorm",
 "doc_section": "src",
 "rel_path": "src/minUnbalDispNorm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 738,
 "word_count": 70,
 "has_code": false,
 "has_table": true
} -->

## 5.6.1.4. Minimum Unbalanced Displacement Norm

**integrator(*'MinUnbalDispNorm'*, *dlambda1*, *Jd=1*, *minLambda=dlambda1*, *maxLambda=dlambda1*, *det=False*)**

Create a MinUnbalDispNorm integrator.

| `dlambda1` ([float](https://docs.python.org/3/library/functions.html#float)) | First load increment (pseudo-time step) at the first iteration in the next invocation of the analysis command. |
| --- | --- |
| `Jd` ([int](https://docs.python.org/3/library/functions.html#int)) | Factor relating first load increment at subsequent time steps. (optional) |
| `minLambda` ([float](https://docs.python.org/3/library/functions.html#float)) | Min load increment. (optional) |
| `maxLambda` ([float](https://docs.python.org/3/library/functions.html#float)) | Max load increment. (optional) |
