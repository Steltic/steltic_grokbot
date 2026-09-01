<!-- chunk_id: constraints_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/constraints.html",
 "title": "5.1. constraints commands",
 "category": "constraint",
 "command": "constraints",
 "doc_section": "src",
 "rel_path": "src/constraints.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1005,
 "word_count": 79,
 "has_code": false,
 "has_table": true
} -->

## 5.1. constraints commands

**constraints(*constraintType*, **constraintArgs*)**

This command is used to construct the ConstraintHandler object. The ConstraintHandler object determines how the constraint equations are enforced in the analysis. Constraint equations enforce a specified value for a DOF, or a relationship between DOFs.

| `constraintType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | constraints type |
| --- | --- |
| `constraintArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of constraints arguments |

The following contain information about available `constraintType`:

1. [Plain Constraints](https://openseespydoc.readthedocs.io/en/latest/src/PlainConstraint.html)
2. [Lagrange Multipliers](https://openseespydoc.readthedocs.io/en/latest/src/LagrangeMultipliers.html)
3. [Penalty Method](https://openseespydoc.readthedocs.io/en/latest/src/PenaltyMethod.html)
4. [Transformation Method](https://openseespydoc.readthedocs.io/en/latest/src/TransformationMethod.html)
