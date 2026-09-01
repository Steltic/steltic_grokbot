<!-- chunk_id: materialCommands_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/materialCommands.html",
 "title": "Material Commands",
 "category": "command_manual",
 "manual_group": "",
 "command": "materialCommands",
 "doc_section": "user/manual",
 "rel_path": "user/manual/materialCommands.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1108,
 "word_count": 105,
 "has_code": false,
 "has_table": false
} -->

## Material Commands

Like many finite element applications, all nonlinear elements have associated with them a material. It is the material in conjunction with the element geometry that provides the force-displacement response of the element. In OpenSees materials are divided into three general types:

1. **uniaxial materials** which define a uniaxial (1 dimensional) stress-strain relationship.
2. **nDimensional materials** which define multi-dimensional (plane stress, plane strain, or 3d) stress-strain relationships.
3. **sections** which define coupled moment-curvature and axial-deformation relationships for beam column elements.

OpenSees Materials

- [3.1.5. uniaxialMaterial Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterial.html)
- [3.1.6. nDMaterial Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterial.html)

For simple investigation of material/section behavior, try the built-in material testing commands.

- [Material Testing Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/matTestCommands.html)
