<!-- chunk_id: fixZ_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/sp_constraint/fixZ.html",
 "title": "3.1.3.4. fixY Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "fixZ",
 "doc_section": "user/manual/model/sp_constraint",
 "rel_path": "user/manual/model/sp_constraint/fixZ.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 822,
 "word_count": 141,
 "has_code": true,
 "has_table": true
} -->

## 3.1.3.4. fixY Command

This command is used to construct multiple homogeneous single-point boundary constraints for all nodes whose z-coordinate lies within a specified distance from a specified coordinate.

| Argument | Type | Description |
| --- | --- | --- |
| $zCoordinate | *float* | z-coordinate of nodes to be constrained |
| $constrValues | *list integer* | ndf constraint values (0 or 1) corresponding to the ndf degrees-of-freedom. 0 unconstrained (or free) 1 constrained (or fixed) |
| $tol | *float* | user-defined tolerance (optional: default = 1e-10) |

Example:

The following example demonstrate the command to fix the first 3 degrees-of-freedom at all nodes in the model at z location **30.0**.

1. **Tcl Code**

```
fixZ 30.0 1 1 1 0 0 0
```

1. **Python Code**

```
fixZ(30.0, 1, 1, 1, 0, 0, 0)
```

Code Developed by: **fmk**
