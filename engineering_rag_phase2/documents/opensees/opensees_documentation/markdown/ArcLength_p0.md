<!-- chunk_id: ArcLength_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/ArcLength.html",
 "title": "3.2.6.4. Arc-Length Control",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "ArcLength",
 "doc_section": "user/manual/analysis/integrator",
 "rel_path": "user/manual/analysis/integrator/ArcLength.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 384,
 "word_count": 71,
 "has_code": false,
 "has_table": true
} -->

## 3.2.6.4. Arc-Length Control

**integrator ArcLength $s $alpha**

| Argument | Type | Description |
| --- | --- | --- |
| $s | *float* | the arcLength |
| $alpha | *float* | a scaling factor on the reference loads. |

This command is used to construct an ArcLength integrator object. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied.
