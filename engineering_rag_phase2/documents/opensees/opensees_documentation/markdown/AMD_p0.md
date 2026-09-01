<!-- chunk_id: AMD_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/AMD.html",
 "title": "3.2.2.3. Alternative Min Degree Numberer",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "AMD",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/AMD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1086,
 "word_count": 171,
 "has_code": true,
 "has_table": false
} -->

## 3.2.2.3. Alternative Min Degree Numberer

This command is used to construct an AMD degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. An AMD numberer uses the approximate minimum degree scheme to order the matrix equations. The command to construct an AMD numberer is a follows:

**numberer AMD**

Example

The following example shows how to construct an alternative min-degree numberer.

1. **Tcl Code**

```
numberer AMD
```

1. **Python Code**

```
numberer('AMD')
```

Code developed by: **fmk**

**REFERENCES**

> Algorithm 837: AMD, An approximate minimum degree ordering algorithm, P. Amestoy, T. A. Davis, and I. S. Duff, ACM Transactions on Mathematical Software, vol 30, no. 3, Sept. 2004, pp. 381-388.
>
> An approximate minimum degree ordering algorithm, P. Amestoy, T. A. Davis, and I. S. Duff, SIAM Journal on Matrix Analysis and Applications, vol 17, no. 4, pp. 886-905, Dec. 1996.
>
> Direct Methods for Sparse Linear Systems, T. A. Davis, SIAM, Philadelphia, Sept. 2006. Part of the SIAM Book Series on the Fundamentals of Algorithms.
