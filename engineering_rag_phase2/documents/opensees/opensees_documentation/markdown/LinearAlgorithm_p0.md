<!-- chunk_id: LinearAlgorithm_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/LinearAlgorithm.html",
 "title": "3.2.5.1. Linear Algorithm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "LinearAlgorithm",
 "doc_section": "user/manual/analysis/algorithm",
 "rel_path": "user/manual/analysis/algorithm/LinearAlgorithm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1197,
 "word_count": 184,
 "has_code": true,
 "has_table": true
} -->

## 3.2.5.1. Linear Algorithm

This command is used to construct a Linear algorithm object which takes one iteration to solve the system of equations.

**algorithm Linear <-initial> <-factorOnce>**

| Argument | Type | Description |
| --- | --- | --- |
| -initial | *string* | optional flag to indicate to use initial stiffness |
| -factorOnce | *string* | optional flag to indicate to only set up and factor matrix once |

Note

As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the -factorOnce option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.

The Linear algorithm REQUIRES NO [test Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test.html#test) and will complain if one is provided. This means that convergence is not checked.

Certain transient explicit integration schemes require a Linear algorithm.

Example:

The following examples demonstrate the command to create a Linear solution algorithm.

1. **Tcl Code**

```
algorithm Linear
```

1. **Python Code**

```
algorithm('Linear')
```

Code Developed by: **fmk**
