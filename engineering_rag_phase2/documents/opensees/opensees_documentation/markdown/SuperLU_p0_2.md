<!-- chunk_id: SuperLU_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/SuperLU.html",
 "title": "3.2.3.4. SuperLU System",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "SuperLU",
 "doc_section": "user/manual/analysis/system",
 "rel_path": "user/manual/analysis/system/SuperLU.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1017,
 "word_count": 158,
 "has_code": true,
 "has_table": false
} -->

## 3.2.3.4. SuperLU System

This command is used to construct a SparseGEN linear system of equation object. As the name implies, this class is used for sparse matrix systems. The solution of the sparse matrix is carried out using .. [SuperLU](https://portal.nersc.gov/project/sparse/superlu/). To following command is used to construct such a system:

**system SuperLU**

Note

1. When using the SuperLU system, the software will renumber the equations to ensure a fast solve. As a consequence it is a waste of time specifying anything but a Plain numberer.
2. The original and still working command was `system SparseGEN`

Example

The following example shows how to construct a SuperLU system

1. **Tcl Code**

```
system SuperLU
```

1. **Python Code**

```
system('SuperLU')
```

Code developed by: **fmk**

**REFERENCES**

> James W. Demmel and Stanley C. Eisenstat and John R. Gilbert and Xiaoye S. Li and Joseph W. H. Liu, “A supernodal approach to sparse partial pivoting”, SIAM J. Matrix Analysis and Applications, 20(3), 720-755, 1999.
