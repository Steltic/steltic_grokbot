<!-- chunk_id: ModifiedNewton_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/ModifiedNewton.html",
 "title": "3.2.5.4. Modified Newton Algorithm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "ModifiedNewton",
 "doc_section": "user/manual/analysis/algorithm",
 "rel_path": "user/manual/analysis/algorithm/ModifiedNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 343,
 "word_count": 54,
 "has_code": false,
 "has_table": true
} -->

## 3.2.5.4. Modified Newton Algorithm

**algorithm ModifiedNewton <-initial>**

| Argument | Type | Description |
| --- | --- | --- |
| -initial | *string* | optional flag to indicate to use initial stiffness iterations |

This command is used to construct a ModifiedNewton algorithm object, which uses the modified newton-raphson algorithm to solve the nonlinear residual equation.
