<!-- chunk_id: Mumps_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/Mumps.html",
 "title": "3.2.3.8. Mumps Solver",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "Mumps",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/Mumps.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 508,
 "word_count": 73,
 "has_code": true,
 "has_table": false
} -->

## 3.2.3.8. Mumps Solver

This command is used to construct a sparse system of equations which uses the [Mumps](http://mumps-solver.org/)  solver. The following command is used to construct such a system:

**system Mumps**

Warning

It is presently limited to the parallel **OpenSeesSP** and **OpenSeesMP** applications.

Example

The following example shows how to construct a sparse system solved using the Mumps solver.

1. **Tcl Code**

```
system Mumps
```

1. **Python Code**

```
system('Mumps')
```

Code developed by: **fmk**
