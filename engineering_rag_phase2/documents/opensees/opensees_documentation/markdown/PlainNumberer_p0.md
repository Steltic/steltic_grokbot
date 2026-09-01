<!-- chunk_id: PlainNumberer_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/numberer/PlainNumberer.html",
 "title": "3.2.2.1. Plain Numberer",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "PlainNumberer",
 "doc_section": "user/manual/analysis/numberer",
 "rel_path": "user/manual/analysis/numberer/PlainNumberer.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 946,
 "word_count": 154,
 "has_code": true,
 "has_table": false
} -->

## 3.2.2.1. Plain Numberer

This command is used to construct a Plain degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. A Plain numberer just takes whatever order the domain gives it nodes and numbers them, this ordering is both dependent on node numbering and size of the model. The command to construct a Plain numberer is a follows:

**numberer Plain**

Note

For very small problems and for the sparse matrix solvers which provide their own numbering scheme, order is not really important so plain numberer is just fine. For large models and analysis using solver types other than the sparse solvers, the order will have a major impact on performance of the solver and the plain handler is a poor choice.

Example

The following example shows how to construct a plain numberer

1. **Tcl Code**

```
numberer Plain
```

1. **Python Code**

```
numberer('Plain')
```

Code Developed by: **fmk**
