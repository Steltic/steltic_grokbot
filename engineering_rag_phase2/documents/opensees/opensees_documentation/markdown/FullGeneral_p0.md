<!-- chunk_id: FullGeneral_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/FullGeneral.html",
 "title": "3.2.3.6. FullGeneral System",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "FullGeneral",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/FullGeneral.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 989,
 "word_count": 167,
 "has_code": true,
 "has_table": false
} -->

## 3.2.3.6. FullGeneral System

This command is used to construct a Full General linear system of equation object. As the name implies, the class utilizes NO space saving techniques to cut down on the amount of memory used. If the matrix is of size, nxn, then storage for an nxn array is sought from memory when the program runs. When a solution is required, the Lapack routines DGESV and DGETRS are used. The following command is used to construct such a system:

**system FullGeneral**

Warning

1. This type of system should almost never be used in production! This is because it requires a lot more memory than every other solver and takes more time in the actual solving operation than any other solver.
2. It is required if the user is interested in looking at the global system matrix, using the **printA** command

Example

The following example shows how to construct a FullGeneral system

1. **Tcl Code**

```
system FullGeneral
```

1. **Python Code**

```
system('FullGeneral')
```

Code Developed by: **fmk**
