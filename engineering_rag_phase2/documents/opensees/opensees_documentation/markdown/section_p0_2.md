<!-- chunk_id: section_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/section.html",
 "title": "3.1.7. section Command",
 "category": "command_manual",
 "manual_group": "material",
 "command": "section",
 "doc_section": "user/manual/material",
 "rel_path": "user/manual/material/section.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1077,
 "word_count": 153,
 "has_code": false,
 "has_table": true
} -->

## 3.1.7. section Command

This command is used to construct a SectionForceDeformation object, hereto referred to as Section, which represents force-deformation (or resultant stress-strain) relationships at beam-column and plate sample points.

**section secType? secTag? arg1? ...**

| Argument | Type | Description |
| --- | --- | --- |
| $secType | *string* | section type |
| $secTag | *integer* | unique section tag. |
| $secArgs | *list* | a list of material arguments with number dependent on section type |

The type of section created and the additional arguments required depends on the secType? provided in the command.

Note

The valid queries to any section when creating an ElementRecorder are ‘force’, and ‘deformation’. Some sections have additional queries to which they will respond. These are documented in the NOTES section for those sections.

The following contain information about secType? and the args required for each of the available section types:

- [3.1.7.1. ElasticSection](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/section/ElasticSection.html)
