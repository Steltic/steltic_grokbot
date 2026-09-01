<!-- chunk_id: fix_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/fix.html",
 "title": "3.1.4.1. fix Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "fix",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/fix.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 892,
 "word_count": 162,
 "has_code": true,
 "has_table": true
} -->

## 3.1.4.1. fix Command

This command is used to construct a number of single-point homogeneous boundary constraints.

**fix $nodeTag (ndf $constrValues)**

| Argument | Type | Description |
| --- | --- | --- |
| $nodeTag | *integer* | unique tag identifying the node to be constrained |
| $constrValues | *list integer* | ndf constraint values (0 or 1) corresponding to the ndf degrees-of-freedom. 0 unconstrained (or free) 1 constrained (or fixed) |

Example:

The following examples demonstrate the commands in a script to add homogeneous boundary conditions

to nodes **1** and **2** for a model with **ndf** of 6. Node **1** is specified to be totally fixed, node **2** is only constrained in the second and fifth degree-of-freedom.

> 1. **Tcl Code**
>
> ```
> fix 1 1 1 1 1 1 1
> fix 2 0 1 0 0 1 0
> ```
>
> 1. **Python Code**
>
> ```
> fix(1,1,1,1,1,1,1)
> fix(2,0,1,0,0,1,0)
> ```

Code developed by: **fmk**
