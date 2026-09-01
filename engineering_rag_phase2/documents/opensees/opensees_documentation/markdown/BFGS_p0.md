<!-- chunk_id: BFGS_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/BFGS.html",
 "title": "3.2.5.7. BFGS Algorithm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "BFGS",
 "doc_section": "user/manual/analysis/algorithm",
 "rel_path": "user/manual/analysis/algorithm/BFGS.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 365,
 "word_count": 66,
 "has_code": false,
 "has_table": true
} -->

## 3.2.5.7. BFGS Algorithm

**algorithm BFGS <$count>**

| Argument | Type | Description |
| --- | --- | --- |
| $count | *integer* | number of iterations within a time step until a new tangent is formed |

This command is used to construct a BFGS algorithm object for symmetric systems which performs successive rank-two updates of the tangent at the first iteration of the current time step.
