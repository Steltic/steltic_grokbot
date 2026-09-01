<!-- chunk_id: PlainConstraints_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/PlainConstraints.html",
 "title": "3.2.1.1. Plain Constraint Handler",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "PlainConstraints",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/PlainConstraints.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 907,
 "word_count": 129,
 "has_code": true,
 "has_table": false
} -->

## 3.2.1.1. Plain Constraint Handler

This command is used to construct a Plain constraint handler. A plain constraint handler can only enforce homogeneous single point constraints (fix command) and multi-point constraints constructed where the constraint matrix is equal to the identity (equalDOF command). The following is the command to construct a plain constraint handler:

**constraints Plain**

This constraint handler can only enforce homogeneous single point constraints (fix command) and multi-pont constraints where the constraint matrix is equal to the identity (equalDOF command).

It does not follow constraints, by that we mean the constrained node in a MP_Constraint cannot be a retained node in another MP_Constraint.

Example

The following example shows how to construct a reverse Cuthill-McKee numberer.

1. **Tcl Code**

```
constraints Plain
```

1. **Python Code**

```
constraints('Plain')
```

Code Developed by: **fmk**
