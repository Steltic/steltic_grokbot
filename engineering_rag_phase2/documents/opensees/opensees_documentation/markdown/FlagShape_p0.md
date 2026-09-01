<!-- chunk_id: FlagShape_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/FlagShape.html",
 "title": "FlagShape Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "FlagShape",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/FlagShape.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1017,
 "word_count": 166,
 "has_code": false,
 "has_table": true
} -->

## FlagShape Material

This command is used to construct the uniaxial FlagShape material

**uniaxialMaterial FlagShape $matTag $E $fy $Eh <$beta>**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material. |
| $E | *float* | initial stiffness. |
| $fy | *float* | yield force. |
| $Eh | *float* | plastic stiffness. |
| $beta | *float* | parameter controlling flag behavior (optional with default value of: 0.0). |

Note

The value of $beta should range from 0 to 1. Bilinear elastic response is obtained with beta=0 while beta=1 gives bilinear hysteretic response. Values between 0 and 1 will give flag-shape response.

Response of FlagShape material for E=100, fy=100, and Eh=10 showing variation in beta parameter:

Code Developed by: Chin-Long Lee (Univ. of Canterbury) and Lei Zhang

**Lee2020**

> Lee CL (2020) Sparse proportional viscous damping model for structures with large number of degrees of freedom. Journal of Sound and Vibration; 478.  DOI: 10.1016/j.jsv.2020.115312.
