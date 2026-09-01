<!-- chunk_id: Broyden_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/Broyden.html",
 "title": "3.2.5.8. Broyden Algorithm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "Broyden",
 "doc_section": "user/manual/analysis/algorithm",
 "rel_path": "user/manual/analysis/algorithm/Broyden.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 381,
 "word_count": 67,
 "has_code": false,
 "has_table": true
} -->

## 3.2.5.8. Broyden Algorithm

**algorithm Broyden <$count>**

| Argument | Type | Description |
| --- | --- | --- |
| $count | *integer* | number of iterations within a time step until a new tangent is formed |

This command is used to construct a Broyden algorithm object for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.
