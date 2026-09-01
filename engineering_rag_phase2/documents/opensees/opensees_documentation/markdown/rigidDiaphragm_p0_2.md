<!-- chunk_id: rigidDiaphragm_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/rigidDiaphragm.html",
 "title": "3.1.5.2. Rigid Diaphragm",
 "category": "command_manual",
 "manual_group": "model",
 "command": "rigidDiaphragm",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/rigidDiaphragm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1908,
 "word_count": 300,
 "has_code": true,
 "has_table": true
} -->

## 3.1.5.2. Rigid Diaphragm

This command is used to construct a number of Multi-Point Constraint (MP_Constraint) objects. These objects will constraint certain degrees-of-freedom at the listed constrained nodes to move as if in a rigid plane with the retained node.

**rigidDiaphragm $perpDirn $retainedNodeTag $constrainedNodeTag1 $constrainedNodeTag2 ...**

| Argument | Type | Description |
| --- | --- | --- |
| $perpDirn | *integer* | direction perpendicular to the rigid plane (i.e. direction 3 (Z) corresponds to the 1-2 (X-Y) plane) – for 2D models direction of rigid motion (1 (X) or 2 (Y)) |
| $retainedNodeTag | *integer* | integer tag identifying the primary (retained) node |
| $constrainedNodeTag1 $constrainedNodeTag2 … | *list integer* | integer tags identifying the secondary (constrained) nodes |

Note

1. The constraint object is constructed assuming small rotations in 3D.
2. The rigidDiaphragm command works for problems in three dimensions with six-degrees-of-freedom at the nodes (ndf=6) and in two dimensions with ndf=3.

Example:

The following command will constrain nodes **4,5,6** to move as if in the same 1-2 plane as node *22*. The constraint matrix added for each of the constrained nodes, which defines the motion of degrees-of-freedom (**x**, **y**, **rZ**) or (**1**, **2**, and **6**) at node **4,5,6** relative to those same degrees-of-freedom at the retained node **22** is as follows:

> (3.1.5.1)\[\begin{split}\begin{bmatrix}
>         1 & 0 & -\Delta Y \\
>         0 & 1 & \Delta X \\
>         0 & 0 & 1
> \end{bmatrix}\end{split}\]
>
> where \(\Delta X\) is **x** (or **1**) coordinate of constrained node minus the **x** coordinate of the retained node and \(\Delta Y\) is **y** (or **2**) coordinate of constrained node minus the y coordinate of the retained node and \(\Delta Y\)

1. **Tcl Code**

```
rigidDiaphragm 3 22 4 5 6
```

1. **Python Code**

```
rigidDiaphragm(3,22,4,5,6)
```
