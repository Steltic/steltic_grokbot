<!-- chunk_id: SecantNewton_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/SecantNewton.html",
 "title": "3.2.5.6. Secant Newton Algorithm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "SecantNewton",
 "doc_section": "user/manual/analysis/algorithm",
 "rel_path": "user/manual/analysis/algorithm/SecantNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 921,
 "word_count": 146,
 "has_code": false,
 "has_table": true
} -->

## 3.2.5.6. Secant Newton Algorithm

**algorithm SecantNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim>**

| Argument | Type | Description |
| --- | --- | --- |
| $tangIter | *string* | tangent to iterate on, options are current, initial, noTangent. default is current. |
| $tangIncr | *string* | tangent to increment on, options are current, initial, noTangent. default is current |
| $maxDim | *float* | max number of iterations until the tangent is reformed and acceleration restarts (default = 3) of iterations within a time step until a new tangent is formed |

This command is used to construct a SecantNewton algorithm object which uses the two-term update to accelerate the convergence of the modified newton method.

Note

- The default “cut-out” values recommended by Crisfield (R1=3.5, R2=0.3) are used.

Note

> References:

- Crisfield, M.A. “Non-linear Finite Element Analysis of Solids and Structures”, Vol. 1, Wiley, 1991.
