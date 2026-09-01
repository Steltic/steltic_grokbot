<!-- chunk_id: RCM_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/numberer/RCM.html",
 "title": "3.2.2.2. Reverse Cuthill McKee Numberer",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "RCM",
 "doc_section": "user/manual/analysis/numberer",
 "rel_path": "user/manual/analysis/numberer/RCM.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1141,
 "word_count": 182,
 "has_code": true,
 "has_table": false
} -->

## 3.2.2.2. Reverse Cuthill McKee Numberer

This command is used to construct an RCM degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. An RCM numberer uses the reverse Cuthill-McKee scheme to order the matrix equations. The command to construct an RCM numberer is a follows:

**numberer RCM**

Note

For very small problems and for the sparse matrix solvers which provide their own numbering scheme, order is not really important so plain numberer is just fine. For large models and analysis using solver types other than the sparse solvers, the order will have a major impact on performance of the solver and the plain handler is a poor choice.

Example

The following example shows how to construct a reverse Cuthill-McKee numberer.

1. **Tcl Code**

```
numberer RCM
```

1. **Python Code**

```
numberer('RCM')
```

**REFERNCES**

> 1. Cuthill and J. McKee. Reducing the bandwidth of sparse symmetric matrices In Proc. 24th Nat. Conf. ACM, pages 157–172, 1969.
>
> 1. 1. George and J. W-H. Liu, Computer Solution of Large Sparse Positive Definite Systems, Prentice-Hall, 1981

Code Developed by: **fmk**
