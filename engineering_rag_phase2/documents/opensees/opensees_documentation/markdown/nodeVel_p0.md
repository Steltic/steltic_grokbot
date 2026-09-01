<!-- chunk_id: nodeVel_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/nodeVel.html",
 "title": "3.4.3. nodeVel Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "nodeVel",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/nodeVel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 769,
 "word_count": 132,
 "has_code": true,
 "has_table": true
} -->

## 3.4.3. nodeVel Command

This command returns the current velocity at a specified node.

**nodeVel $nodeTag <$dof>**

| Argument | Type | Description |
| --- | --- | --- |
| $nodeTag | *integer* | tag identifying node whose velocities are sought |
| $dof | *integer* | optional: specific dof at the node (1 through ndf) |

Note

If optional $dof is not provided, an array containing all velocity components for every dof at the node is returned.

Example:

The following example is used to set the variable **vel1** to the nodal velocity at node given by the variable **nodeTag** in the **1** degree-of-freedom direction.

1. **Tcl Code** (note use of **set** and **[ ]**)

```
set vel1 [nodeVel $nodeTag 1]
```

1. **Python Code**

```
vel1 = nodeVel(nodeTag,1)
```

Code developed by: **fmk**
