<!-- chunk_id: loadControl_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/loadControl.html",
 "title": "5.6.1.1. LoadControl",
 "category": "general",
 "command": "loadControl",
 "doc_section": "src",
 "rel_path": "src/loadControl.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1227,
 "word_count": 164,
 "has_code": false,
 "has_table": true
} -->

## 5.6.1.1. LoadControl

**integrator(*'LoadControl'*, *incr*, *numIter=1*, *minIncr=incr*, *maxIncr=incr*)**

Create a OpenSees LoadControl integrator object.

| `incr` ([float](https://docs.python.org/3/library/functions.html#float)) | Load factor increment \(\lambda\). |
| --- | --- |
| `numIter` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of iterations the user would like to occur in the solution algorithm. (optional) |
| `minIncr` ([float](https://docs.python.org/3/library/functions.html#float)) | Min stepsize the user will allow \(\lambda_{min}\). (optional) |
| `maxIncr` ([float](https://docs.python.org/3/library/functions.html#float)) | Max stepsize the user will allow \(\lambda_{max}\). (optional) |

1. The change in applied loads that this causes depends on the active load pattern (those load pattern not set constant) and the loads in the load pattern. If the only active load acting on the Domain are in load pattern with a Linear time series with a factor of 1.0, this integrator is the same as the classical load control method.
2. The optional arguments are supplied to speed up the step size in cases where convergence is too fast and slow down the step size in cases where convergence is too slow.
