<!-- chunk_id: PlainConstraint_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PlainConstraint.html",
 "title": "5.1.1. Plain Constraints",
 "category": "constraint",
 "command": "PlainConstraint",
 "doc_section": "src",
 "rel_path": "src/PlainConstraint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 580,
 "word_count": 79,
 "has_code": false,
 "has_table": false
} -->

## 5.1.1. Plain Constraints

**constraints(*'Plain'*)**

This command is used to construct a Plain constraint handler. A plain constraint handler can only enforce homogeneous single point constraints (fix command) and multi-point constraints constructed where the constraint matrix is equal to the identity (equalDOF command). The following is the command to construct a plain constraint handler:

Note

As mentioned, this constraint handler can only enforce homogeneous single point constraints (fix command) and multi-pont constraints where the constraint matrix is equal to the identity (equalDOF command).
