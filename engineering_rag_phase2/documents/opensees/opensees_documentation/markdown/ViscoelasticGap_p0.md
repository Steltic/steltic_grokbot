<!-- chunk_id: ViscoelasticGap_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/ViscoelasticGap.html",
 "title": "3.1.5.30. Viscoelastic Gap Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "ViscoelasticGap",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/ViscoelasticGap.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 971,
 "word_count": 166,
 "has_code": false,
 "has_table": true
} -->

## 3.1.5.30. Viscoelastic Gap Material

This command is used to construct the uniaxial Jankowski Impact Material

**uniaxialMaterial ViscoelasticGap $matTag $K $c $gap**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material. |
| $K | *float* | stiffness. |
| $C | *float* | damping coefficient. |
| $gap | *float* | initial gap |

This material is implemented as a compression-only gap material, so $gap should be input as a negative value. Due to the viscous component of this material, a small tensile force is present at the end of an impact event.
.. Description::
This material model follows the constitutive law

> \[f_c(t) = k(\delta(t)-g) + c \dot{\delta} (t)\]

where t is time, \(f_c (t)\)  is the contact force, \(k\) is the stiffness ($K), \(\delta(t)\) is the indentation, g is the initial gap ($gap), c is the damping coefficient ($C) and \(\dot{\delta}(t)\) is the indentation velocity.

Code Developed by: Patrick J. Hughes, UC San Diego
