<!-- chunk_id: geomTransf_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/geomTransf.html",
 "title": "3.1.8. Geometric Transformation Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "geomTransf",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/geomTransf.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1029,
 "word_count": 98,
 "has_code": false,
 "has_table": false
} -->

## 3.1.8. Geometric Transformation Command

The geometric-transformation command is used to construct a coordinate-transformation (CrdTransf) object, which transforms beam element stiffness and resisting force from the basic system to the global-coordinate system. The command has at least one argument, the transformation type. Each type is outlined below.

**geomTransf transfType? arg1? ...**

The type of transformation created and the additional arguments required depends on the transfType? provided in the command.

The following contain information about transfType? and the args required for each of the available geometric transformation types:

- [3.1.8.1. Linear Transformation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/geomTransf/Linear.html)
- [3.1.8.2. PDelta Transformation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/geomTransf/PDelta.html)
- [3.1.8.3. Corotational Transformation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/geomTransf/Corotational.html)

Code Developed by: **fmk**
