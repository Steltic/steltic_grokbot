<!-- chunk_id: KrylovNewton_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/KrylovNewton.html",
 "title": "3.2.5.5. Krylov-Newton Algorithm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "KrylovNewton",
 "doc_section": "user/manual/analysis/algorithm",
 "rel_path": "user/manual/analysis/algorithm/KrylovNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 942,
 "word_count": 148,
 "has_code": false,
 "has_table": true
} -->

## 3.2.5.5. Krylov-Newton Algorithm

**algorithm KrylovNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim>**

| Argument | Type | Description |
| --- | --- | --- |
| $tangIter | *string* | tangent to iterate on, options are current, initial, noTangent. default is current. |
| $tangIncr | *string* | tangent to increment on, options are current, initial, noTangent. default is current |
| $maxDim | *float* | max number of iterations until the tangent is reformed and acceleration restarts (default = 3) of iterations within a time step until a new tangent is formed |

This command is used to construct a KrylovNewton algorithm object which uses a modified Newton method with Krylov subspace acceleration to advance to the next time step.

Note

References:
* Scott, M.H. and G.L. Fenves. “A Krylov Subspace Accelerated Newton Algorithm: Application to Dynamic Progressive Collapse Simulation of Frames.” Journal of Structural Engineering, 136(5), May 2010. DOI
