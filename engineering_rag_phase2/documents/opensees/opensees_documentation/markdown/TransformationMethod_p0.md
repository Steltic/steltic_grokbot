<!-- chunk_id: TransformationMethod_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/TransformationMethod.html",
 "title": "3.2.1.3. Transformation Method",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "TransformationMethod",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/TransformationMethod.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1052,
 "word_count": 159,
 "has_code": true,
 "has_table": false
} -->

## 3.2.1.3. Transformation Method

This command is used to construct a `PenaltyMethod` constraint handler, which enforces the constraints by using the penalty method. The following is the command to construct such a constraint handler:

**constraints Transformation**

Note

The single-point constraints when using the transformation method are done directly. The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.

**Great care must be taken when multiple constraints are being enforced as the transformation method does not follow constraints:**

> 1. If a node is fixed, constrain it with the fix command and not equalDOF or other type of constraint.
> 2. If multiple nodes are constrained, make sure that the retained node is not constrained in any other constraint.

Example

The following example shows how to construct a Lagrange constraint handler

1. **Tcl Code**

```
numberer Transformation
```

1. **Python Code**

```
numberer('Transformation')
```

Code Developed by: **fmk**
