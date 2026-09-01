<!-- chunk_id: CoulombDamper_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/CoulombDamper.html",
 "title": "3.1.5.27. CoulombDamper Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "CoulombDamper",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/CoulombDamper.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 891,
 "word_count": 145,
 "has_code": false,
 "has_table": true
} -->

## 3.1.5.27. CoulombDamper Material

This command is used to construct the uniaxial CoulombDamper material producing elastic stiffness and friction force.

**uniaxialMaterial CoulombDamper $matTag $Tangent $FrictionFoce -tol $tol -numFlipped $numFlipped -reduceFc -dampOutTangent $dampOutTangent**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material. |
| $Tangent | *float* | the tangent stiffness for strain. |
| $FrictionFoce | *float* | the friction force opposite to strain rate. |
| $tol | *float* | the tolerance to check if strain rate is small. |
| $numFlipped | *integer* | the number of times that the strain rate is flipped before adjusting friction force. |
| -reduceFc | *string* | reducing friction force if strain rate is flipped several times. |
| $dampOutTangent | *float* | giving a constant damping tangent if strain rate is flipped several times. |
