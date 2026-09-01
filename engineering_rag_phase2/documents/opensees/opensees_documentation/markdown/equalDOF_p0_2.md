<!-- chunk_id: equalDOF_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/mp_constraint/equalDOF.html",
 "title": "3.1.4.1. EqualDOF Constraints",
 "category": "command_manual",
 "manual_group": "model",
 "command": "equalDOF",
 "doc_section": "user/manual/model/mp_constraint",
 "rel_path": "user/manual/model/mp_constraint/equalDOF.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 907,
 "word_count": 144,
 "has_code": true,
 "has_table": false
} -->

## 3.1.4.1. EqualDOF Constraints

This command is used to construct a multi-point constraint between nodes where the degrees-of-freedom at the constrained node move exactly the same as the degrees-of-freedom at the other node, the retained node.

**equalDOF $rNodeTag $cNodeTag $dof1 $dof2 ..**

Note

retained (primary) node

constrained (secondary) node

valid range of $dof is 1 through **ndf** of the **constrained** node

if no dofs are specified, *all* dofs of the constrained node are used

Example:

The following command will impose the displacenents at dof’s **1, 3, and 5** at node **2** to be the same as those of node **33*.

1. **Tcl Code**

```
equalDOF 2 33 1 3 5;
```

1. **Python Code**

```
equalDOF(2,33,1,3,5);
```

Reference:

Cook, R.D., Malkus, D.S., Plesha, M. E., and Witt, R. J., “Concepts and Applications of Finite Element Analysis,” 4th edition, John Wiley and Sons publishers, 2002.

Code developed by: **fmk**
