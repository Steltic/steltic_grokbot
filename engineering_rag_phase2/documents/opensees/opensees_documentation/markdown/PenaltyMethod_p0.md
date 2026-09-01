<!-- chunk_id: PenaltyMethod_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraint/PenaltyMethod.html",
 "title": "3.2.1.2. Penalty Method",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "PenaltyMethod",
 "doc_section": "user/manual/analysis/constraint",
 "rel_path": "user/manual/analysis/constraint/PenaltyMethod.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 931,
 "word_count": 145,
 "has_code": true,
 "has_table": true
} -->

## 3.2.1.2. Penalty Method

This command is used to construct a PenaltyMethod constraint handler, which enforces the constraints by using the penalty method. The following is the command to construct such a constraint handler:

**constraints Penalty $alphaS $alphaM**

| Argument | Type | Description |
| --- | --- | --- |
| $alphaS | *float* | \(\alpha_S\) factor on singe points. |
| $alphaM | *float* | \(\alpha_M\) factor on multi-points. |

Warning

The degree to which the constraints are enforced is dependent on the penalty values chosen. Problems can arise if these values are too small (constraint not enforced strongly enough) or too large (problems associated with conditioning of the system of equations).

Example

The following example shows how to construct a Penalty Method constraint handler

1. **Tcl Code**

```
numberer Penalty 1.0e10 1.0e10
```

1. **Python Code**

```
numberer('Penalty', 1.0e10, 1.0e10)
```

Code Developed by: **fmk**
