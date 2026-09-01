<!-- chunk_id: rigidLink_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/rigidLink.html",
 "title": "3.1.5.3. Rigid Link",
 "category": "command_manual",
 "manual_group": "model",
 "command": "rigidLink",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/rigidLink.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2808,
 "word_count": 457,
 "has_code": true,
 "has_table": true
} -->

## 3.1.5.3. Rigid Link

This command is used to construct a single MP_Constraint object.

**rigidLink $type $retainedNodeTag $constrainedNodeTag**

| Argument | Type | Description |
| --- | --- | --- |
| $type | *string* | string-based argument for rigid-link type: **bar** only the translational degree-of-freedom will be constrained to be exactly the same as those at the master node **beam** both the translational and rotational degrees of freedom are constrained. |
| $retainedNodeTag | *integer* | integer tag identifying the retained node |
| $constrainedNodeTag | *integer* | integer tag identifying the constrained node |

Note

1. By retained node, we mean the node who’s degrees-of-freedom are retained in the system of equations. The constrained nodes degrees-of-freedom need not appear in the system (depending on the constraint handler).
2. For 2d and 3d problems with a **beam** type link, the constraint matrix (that matrix relating the responses at constrained node, \(U_c\), to responses at retained node, \(U_r\), i.e. \(U_c = C_{cr} U_r\), is constructed assuming small rotations. For 3d problems this results in the following constraint matrix:

  (3.1.5.5)\[\begin{split}\begin{bmatrix}
          1 & 0 & 0 & 0 & \Delta Z & -\Delta Y \\
          0 & 1 & 0 & -\Delta Z & 0 & \Delta X \\
          0 & 0 & 1 & \Delta Y & -\Delta X & 0 \\
          0 & 0 & 0 & 1 & 0 & 0 \\
          0 & 0 & 0 & 0 & 1 & 0 \\
          0 & 0 & 0 & 0 & 0 & 1
  \end{bmatrix}\end{split}\]

  For 2d problems, the constraint matrix is the following:

  (3.1.5.5)\[\begin{split}\begin{bmatrix}
          1 & 0 & -\Delta Y \\
          0 & 1 & \Delta X \\
          0 & 0 & 1
  \end{bmatrix}\end{split}\]

  where \(\Delta X\) is x coordinate of constrained node minus the x coordinate of the retained node. \(\Delta Y\) and \(\Delta Z\) being similarily defined for y and z coordinates of the nodes.
3. For 2d and 3d problems with a **rod** type link the constraint matrix, that which matrix relates the responses at translational degrees-of-freedom at the constrained node to corresponding responses at retained node, is the identity matrix. For 3d problems this results in the following constraint matrix:

(3.1.5.5)\[\begin{split}\begin{bmatrix}
        1 & 0 & 0  \\
        0 & 1 & 0  \\
        0 & 0 & 1
\end{bmatrix}\end{split}\]

For 2d problems, the constraint matrix is the following:

> (3.1.5.5)\[\begin{split}\begin{bmatrix}
>         1 & 0 \\
>         0 & 1 \\
> \end{bmatrix}\end{split}\]

1. The rod constraint can also be generated using the equalDOF command.

Example:

The following command will constrain node **3** to move rigidly following rules for small rotations to displacements and rotations at node **2** is

1. **Tcl Code**

```
rigidLink beam 2 3
```

1. **Python Code**

```
rigidLink('beam',2,3)
```
