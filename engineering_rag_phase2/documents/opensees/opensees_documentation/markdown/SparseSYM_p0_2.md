<!-- chunk_id: SparseSYM_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/SparseSYM.html",
 "title": "3.2.3.7. SparseSYM Solver",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "SparseSYM",
 "doc_section": "user/manual/analysis/system",
 "rel_path": "user/manual/analysis/system/SparseSYM.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 988,
 "word_count": 140,
 "has_code": true,
 "has_table": false
} -->

## 3.2.3.7. SparseSYM Solver

This command is used to construct a sparse symmetric system of equations which uses a row-oriented solution method in the solution phase. The following command is used to construct such a system:

**system SparseSYM**

Note

Versions of OpenSees up to and including 2.2.0 used SparseSPD instead of SparseSYM as the option to create this system. The code is more general than the SPD moniker implies, working for negative definite as well as positive definite. For backward compatibility this old option continues to work.

Example

The following example shows how to construct a SparseSYM system:

1. **Tcl Code**

```
system SparseSYM
```

1. **Python Code**

```
system('SparseSYM')
```

Code developed by: [J. Peng](https://www.linkedin.com/in/james-peng-a6194b13/)

**REFERENCES**

Kincho H. Law and David R. McKay, “A Parallel Row-Oriented Sparse Solution Method for Finite Element Structural Analysis,” International Journal for Numerical Methods in Engineering, 36:2895-2919, 1993.
