<!-- chunk_id: nodeCoord_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/nodeCoord.html",
 "title": "3.4.7. nodeCoord Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "nodeCoord",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/nodeCoord.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 736,
 "word_count": 122,
 "has_code": true,
 "has_table": true
} -->

## 3.4.7. nodeCoord Command

This command returns the current coordinate at a specified node.

**nodeCoord $nodeTag <$dim>**

| Argument | Type | Description |
| --- | --- | --- |
| $nodeTag | *integer* | tag identifying node whose velocities are sought |
| $dim | *integer* | optional: specific crd dimension at the node (1 through ndm) |

Note

If optional $ddim is not provided, an array containing all coordinate components is returned.

Example:

The following example is used to set the variable **crdNode** to the nodal coordinates for the node given by the variable **nodeTag**.

1. **Tcl Code** (note use of **set** and **[ ]**)

```
set crdNode [nodeCoord $nodeTag]
```

1. **Python Code**

```
crdNode = nodeCoord(nodeTag)
```

Code developed by: **fmk**
