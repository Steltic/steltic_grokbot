<!-- chunk_id: lagrangeMultipliers_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraint/lagrangeMultipliers.html",
 "title": "3.2.1.4. Lagrange Multipliers",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "lagrangeMultipliers",
 "doc_section": "user/manual/analysis/constraint",
 "rel_path": "user/manual/analysis/constraint/lagrangeMultipliers.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1025,
 "word_count": 160,
 "has_code": true,
 "has_table": true
} -->

## 3.2.1.4. Lagrange Multipliers

This command is used to construct a LagrangeMultiplier constraint handler, which enforces the constraints by introducing Lagrange multipliers to the system of equation. The following is the command to construct a plain constraint handler:

**constraints Lagrange <$alphaS $alphaM >**

| Argument | Type | Description |
| --- | --- | --- |
| $alphaS | *float* | \(\alpha_S\) factor on singe points. optional: default = 1.0 |
| $alphaM | *float* | \(\alpha_M\) factor on multi-points. optional: default = 1.0 |

Warning

The Lagrange multiplier method introduces new unknowns to the system of equations. The diagonal part of the system corresponding to these new unknowns is 0.0. This ensure that the system **IS NOT** symmetric positive definite and so do not use a positive definite solver.

Example

The following example shows how to construct a Lagrange constraint handler

1. **Tcl Code**

```
numberer Lagrange
```

1. **Python Code**

```
numberer('Lagrange')
```

Code Developed by: **fmk**

Code Developed by: **fmk**
