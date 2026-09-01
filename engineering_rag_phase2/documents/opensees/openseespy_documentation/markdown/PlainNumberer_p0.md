<!-- chunk_id: PlainNumberer_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PlainNumberer.html",
 "title": "5.2.1. Plain Numberer",
 "category": "analysis",
 "command": "PlainNumberer",
 "doc_section": "src",
 "rel_path": "src/PlainNumberer.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 707,
 "word_count": 115,
 "has_code": false,
 "has_table": false
} -->

## 5.2.1. Plain Numberer

**numberer(*'Plain'*)**

This command is used to construct a Plain degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. A Plain numberer just takes whatever order the domain gives it nodes and numbers them, this ordering is both dependent on node numbering and size of the model.

Note

For very small problems and for the sparse matrix solvers which provide their own numbering scheme, order is not really important so plain numberer is just fine. For large models and analysis using solver types other than the sparse solvers, the order will have a major impact on performance of the solver and the plain handler is a poor choice.
