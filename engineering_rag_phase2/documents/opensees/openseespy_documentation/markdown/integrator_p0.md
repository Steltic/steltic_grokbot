<!-- chunk_id: integrator_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/integrator.html",
 "title": "5.6. integrator commands",
 "category": "analysis",
 "command": "integrator",
 "doc_section": "src",
 "rel_path": "src/integrator.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1971,
 "word_count": 140,
 "has_code": false,
 "has_table": true
} -->

## 5.6. integrator commands

**integrator(*intType*, **intArgs*)**

This command is used to construct the Integrator object. The Integrator object determines the meaning of the terms in the system of equation object Ax=B.

The Integrator object is used for the following:

- determine the predictive step for time t+dt
- specify the tangent matrix and residual vector at any iteration
- determine the corrective step based on the displacement increment dU

| `intType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | integrator type |
| --- | --- |
| `intArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of integrator arguments |

The following contain information about available `intType`:

#### 5.6.1. Static integrator objects

1. [LoadControl](https://openseespydoc.readthedocs.io/en/latest/src/loadControl.html)
2. [DisplacementControl](https://openseespydoc.readthedocs.io/en/latest/src/displacementControl.html)
3. [Parallel DisplacementControl](https://openseespydoc.readthedocs.io/en/latest/src/ParallelDisplacementControl.html)
4. [Minimum Unbalanced Displacement Norm](https://openseespydoc.readthedocs.io/en/latest/src/minUnbalDispNorm.html)
5. [Arc-Length Control](https://openseespydoc.readthedocs.io/en/latest/src/arcLength.html)

#### 5.6.2. Transient integrator objects

1. [Central Difference](https://openseespydoc.readthedocs.io/en/latest/src/centralDifference.html)
2. [Newmark Method](https://openseespydoc.readthedocs.io/en/latest/src/newmark.html)
3. [Hilber-Hughes-Taylor Method](https://openseespydoc.readthedocs.io/en/latest/src/hht.html)
4. [Generalized Alpha Method](https://openseespydoc.readthedocs.io/en/latest/src/generalizedAlpha.html)
5. [TRBDF2](https://openseespydoc.readthedocs.io/en/latest/src/trbdf2.html)
6. [Explicit Difference](https://openseespydoc.readthedocs.io/en/latest/src/explicitDifference.html)
7. [PFEM integrator](https://openseespydoc.readthedocs.io/en/latest/src/pfemIntegrator.html#pfem-integrator)
