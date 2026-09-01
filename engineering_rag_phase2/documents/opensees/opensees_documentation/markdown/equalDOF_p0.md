<!-- chunk_id: equalDOF_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/equalDOF.html",
 "title": "3.1.5.1. EqualDOF Constraints",
 "category": "command_manual",
 "manual_group": "model",
 "command": "equalDOF",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/equalDOF.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 874,
 "word_count": 141,
 "has_code": true,
 "has_table": false
} -->

## 3.1.5.1. EqualDOF Constraints

This command is used to construct a multi-point constraint between nodes where the degrees-of-freedom at the constrained node move exactly the same as the degrees-of-freedom at the other node, the retained node.

**equalDOF $rNodeTag $cNodeTag $dof1 $dof2 ..**

Note

retained node also known as the **master** node.

constarined node alsoe node as the **slave** node.

valid range of $dof is 1 through **ndf** of the **slave** node

Example:

The following command will impose the displacenents at dof’s **1, 3, and 5** at node **2** to be the same as those of node **33*.

1. **Tcl Code**

```
equalDOF 2 33 1 3 5;
```

1. **Tcl Code**

```
equalDOF(2,33,1,3,5);
```

Reference:

Cook, R.D., Malkus, D.S., Plesha, M. E., and Witt, R. J., “Concepts and Applications of Finite Element Analysis,” 4th edition, John Wiley and Sons publishers, 2002.

Code developed by: **fmk**
