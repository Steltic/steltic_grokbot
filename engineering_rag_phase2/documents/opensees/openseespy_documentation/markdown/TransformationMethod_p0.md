<!-- chunk_id: TransformationMethod_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/TransformationMethod.html",
 "title": "5.1.4. Transformation Method",
 "category": "general",
 "command": "TransformationMethod",
 "doc_section": "src",
 "rel_path": "src/TransformationMethod.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 958,
 "word_count": 148,
 "has_code": false,
 "has_table": false
} -->

## 5.1.4. Transformation Method

**constraints(*'Transformation'*)**

This command is used to construct a transformation constraint handler, which enforces the constraints using the transformation method. The following is the command to construct a transformation constraint handler

Note

- The single-point constraints when using the transformation method are done directly. The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.
- Great care must be taken when multiple constraints are being enforced as the transformation method does not follow constraints:

  1. If a node is fixed, constrain it with the fix command and not equalDOF or other type of constraint.
  2. If multiple nodes are constrained, make sure that the retained node is not constrained in any other constraint.

And remember if a node is constrained to multiple nodes in your model it probably means you have messed up.
