<!-- chunk_id: imposedMotion_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/imposedMotion.html",
 "title": "3.1.7.3.2. Imposed Motion Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "imposedMotion",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/imposedMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1404,
 "word_count": 198,
 "has_code": true,
 "has_table": false
} -->

## 3.1.7.3.2. Imposed Motion Command

This command is used to construct an ImposedMotionSP constraint which is used to enforce the response of a dof at a node in the model. The response enforced at the node at any give time is obtained from the GroundMotion object associated with the constraint.

**imposedMotion $nodeTag $dirn $gMotionTag**

> $nodeTag, *integer*, tag of node on which constraint is to be placed
> $dof, *integer*, dof of enforced response. Valid range is from 1 through ndf at node.
> $gMotionTag, *integer*,   pre-defined GroundMotion object tag

Example:

The following example shows how to construct a **Multi-Suppert Excitation** pattern with a tag of **1* that will constrain the nodes **1**, **4**, and **7** to move in the **1** dof direcection with the ground Motion supplied by the **groundMotion** with tag **101**, whose displacement is given by **timeSeries** with a tag of 3.

1. **Tcl Code**

```
timeSeries Path 3 -filePath elCentroDisp.dat -dt 0.02
pattern MultipleSupport  1  {
     groundMotion 101 Series -disp 3

     imposedSupportMotion 1 1 101
     imposedSupportMotion 4 1 101
     imposedSupportMotion 7 1 101
}
```

1. **Python Code**

```
timeSeries('Path', 3, '-dt', 0.02, '-filePath', 'elCentroDisp.dat')
pattern('MultiSupport', 1)
groundMotion(101, 'Series', '-disp', 3)
imposedSupportMotion(1,1,101)
imposedSupportMotion(4,1,101)
imposedSupportMotion(7,1,101)
```

Code Developed by: **fmk**
