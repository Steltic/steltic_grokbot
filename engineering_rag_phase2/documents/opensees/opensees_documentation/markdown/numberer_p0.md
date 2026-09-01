<!-- chunk_id: numberer_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/numberer.html",
 "title": "3.2.2. numberer Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "numberer",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/numberer.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 996,
 "word_count": 112,
 "has_code": false,
 "has_table": true
} -->

## 3.2.2. numberer Command

This command is used to construct the **DOF_Numberer** object. The **DOF_Numberer** object determines the mapping between equation numbers in the system of equations and the degrees-of-freedom at the nodes, basically how degrees-of-freedom are numbered.

**numberer numbererType? arg1? ...**

| Argument | Type | Description |
| --- | --- | --- |
| $numbererType | *string* | the numberer type |
| $args | *list* | a list of arguments for that type |

The following contain information about numbererType? and the args required for each of the available dof numberer types:

- [3.2.2.1. Plain Numberer](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/numberer/PlainNumberer.html)
- [3.2.2.2. Reverse Cuthill McKee Numberer](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/numberer/RCM.html)
- [3.2.2.3. Alternative Min Degree Numberer](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/numberer/AMD.html)

Code developed by: **fmk**
