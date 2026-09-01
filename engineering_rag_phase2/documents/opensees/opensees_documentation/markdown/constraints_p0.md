<!-- chunk_id: constraints_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraints.html",
 "title": "3.2.1. constraints Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "constraints",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/constraints.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1399,
 "word_count": 147,
 "has_code": false,
 "has_table": true
} -->

## 3.2.1. constraints Command

This command is used to construct the ConstraintHandler object. The ConstraintHandler object determines how the constraint equations are enforced in the analysis. Constraint equations define a specified value for a DOF, or a relationship between DOFs.

**constraints constraintType? arg1? ...**

| Argument | Type | Description |
| --- | --- | --- |
| $constraintType | *string* | the constraints type |
| $args | *list* | a list of arguments for that type |

The following contain information about numbererType? and the args required for each of the available dof numberer types:

The type of ConstraintHandler created and the additional arguments required depends on the constraintType? provided in the command.

The following contain information about numbererType? and the args required for each of the available constraint handler types:

- [3.2.1.1. Plain Constraint Handler](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraint/PlainConstraints.html)
- [3.2.1.2. Penalty Method](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraint/PenaltyMethod.html)
- [3.2.1.3. Transformation Method](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraint/TransformationMethod.html)
- [3.2.1.4. Lagrange Multipliers](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraint/lagrangeMultipliers.html)
