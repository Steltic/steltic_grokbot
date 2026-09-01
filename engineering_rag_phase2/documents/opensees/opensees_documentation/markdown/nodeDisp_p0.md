<!-- chunk_id: nodeDisp_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/nodeDisp.html",
 "title": "3.4.2. nodeDisp Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "nodeDisp",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/nodeDisp.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 790,
 "word_count": 132,
 "has_code": true,
 "has_table": true
} -->

## 3.4.2. nodeDisp Command

This command returns the current displacement at a specified node.

**nodeDisp $nodeTag <$dof>**

| Argument | Type | Description |
| --- | --- | --- |
| $nodeTag | *integer* | tag identifying node whose displacements are sought |
| $dof | *integer* | optional: specific dof at the node (1 through ndf) |

Note

If optional $dof is not provided, an array containing all displacement components for every dof at the node is returned.

Example:

The following example is used to set the variable **disp1** to the nodal displacement at node given by the variable **nodeTag** in the **1** degree-of-freedom direction.

1. **Tcl Code** (note use of **set** and **[ ]**)

```
set disp1 [nodeDisp $nodeTag 1]
```

1. **Python Code**

```
disp1 = nodeDisp(nodeTag,1)
```

Code developed by: **fmk**
