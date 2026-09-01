<!-- chunk_id: ParallelDisplacementControl_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ParallelDisplacementControl.html",
 "title": "5.6.1.3. Parallel DisplacementControl",
 "category": "general",
 "command": "ParallelDisplacementControl",
 "doc_section": "src",
 "rel_path": "src/ParallelDisplacementControl.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1351,
 "word_count": 156,
 "has_code": false,
 "has_table": true
} -->

## 5.6.1.3. Parallel DisplacementControl

**integrator(*'ParallelDisplacementControl'*, *nodeTag*, *dof*, *incr*, *numIter=1*, *dUmin=incr*, *dUmax=incr*)**

Create a Parallel version of DisplacementControl integrator.  In an analysis step with Displacement Control we seek to determine the time step that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of node whose response controls solution |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | Degree of freedom at the node, 1 through ndf. |
| `incr` ([float](https://docs.python.org/3/library/functions.html#float)) | First displacement increment \(\Delta U_{dof}\). |
| `numIter` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of iterations the user would like to occur in the solution algorithm. (optional) |
| `minIncr` ([float](https://docs.python.org/3/library/functions.html#float)) | Min stepsize the user will allow \(\Delta U_{min}\). (optional) |
| `maxIncr` ([float](https://docs.python.org/3/library/functions.html#float)) | Max stepsize the user will allow \(\Delta U_{max}\). (optional) |

Use this command only for parallel model.

Warning

Don’t use this command if model is not parallel, for example,
parametric study.
