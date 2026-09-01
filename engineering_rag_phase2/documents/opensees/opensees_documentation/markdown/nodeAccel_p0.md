<!-- chunk_id: nodeAccel_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/nodeAccel.html",
 "title": "3.4.4. nodeAccel Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "nodeAccel",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/nodeAccel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 764,
 "word_count": 128,
 "has_code": true,
 "has_table": true
} -->

## 3.4.4. nodeAccel Command

This command returns the current acceleration at a specified node.

**nodeAccel $nodeTag <$dof>**

| Argument | Type | Description |
| --- | --- | --- |
| $nodeTag | *integer* | tag identifying node whose accelerations are sought |
| $dof | *integer* | optional: specific dof at the node (1 through ndf) |

Note

If optional $dof is not provided, an array containing all acceleration components for every dof at the node is returned.

Example:

The following example is used to set the array/list **accel1** equal to the nodal accelerations at the node given by the variable **nodeTag**.

1. **Tcl Code** (note use of **set** and **[ ]**)

```
set accel1 [nodeAccel $nodeTag]
```

1. **Python Code**

```
accel1 = nodeAccel(nodeTag)
```

Code developed by: **fmk**
