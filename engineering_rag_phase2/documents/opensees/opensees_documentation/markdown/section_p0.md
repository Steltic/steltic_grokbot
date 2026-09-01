<!-- chunk_id: section_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/section.html",
 "title": "3.1.7. section Command",
 "category": "command_manual",
 "manual_group": "",
 "command": "section",
 "doc_section": "user/manual",
 "rel_path": "user/manual/section.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1496,
 "word_count": 162,
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

- [3.1.7.1. ElasticSection](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/section/ElasticSection.html)
- [3.1.7.2. ReinforcedConcreteLayeredMembraneSection](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/section/ReinforcedConcreteLayeredMembraneSection.html)
- [3.1.7.3. LayeredMembraneSection](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/section/LayeredMembraneSection.html)
- [3.1.7.4. ASDCoupledHinge3D](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/section/ASDCoupledHinge3D.html)
