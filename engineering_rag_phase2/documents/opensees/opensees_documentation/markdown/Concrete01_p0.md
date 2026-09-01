<!-- chunk_id: Concrete01_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Concrete01.html",
 "title": "3.1.5.11. Concrete01 Material – Zero Tensile Strength",
 "category": "command_manual",
 "manual_group": "material",
 "command": "Concrete01",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/Concrete01.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 999,
 "word_count": 157,
 "has_code": false,
 "has_table": true
} -->

## 3.1.5.11. Concrete01 Material – Zero Tensile Strength

This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).

**uniaxialMaterial Concrete01 $matTag $fpc $epsc0 $fpcu $epsu**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material. |
| $fpc | *float* | concrete compressive strength at 28 days (compression is negative)* . |
| $epsc0 | *float* | concrete strain at maximum strength* . |
| $fpcu | *float* | concrete crushing strength*. |
| $epsU | *float* | concrete strain at crushing strength*. |

Note

- Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
- The initial slope for this model is (2*$fpc/$epsc0)

Typical Hysteretic Stress-Strain Relation for material

Code Developed by: Filip Filippou, UC Berkeley
Images Developed by Silvia Mazzoni
