<!-- chunk_id: ParallelRCMNumberer_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ParallelRCMNumberer.html",
 "title": "5.2.5. Parallel RCM Numberer",
 "category": "analysis",
 "command": "ParallelRCMNumberer",
 "doc_section": "src",
 "rel_path": "src/ParallelRCMNumberer.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 511,
 "word_count": 78,
 "has_code": false,
 "has_table": false
} -->

## 5.2.5. Parallel RCM Numberer

**numberer(*'ParallelRCM'*)**

This command is used to construct a parallel version
of RCM degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. A Plain numberer just takes whatever order the domain gives it nodes and numbers them, this ordering is both dependent on node numbering and size of the model.

Use this command only for parallel model.

Warning

Don’t use this command if model is not parallel, for example,
parametric study.
