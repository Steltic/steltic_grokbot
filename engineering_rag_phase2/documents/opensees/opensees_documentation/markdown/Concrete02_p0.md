<!-- chunk_id: Concrete02_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Concrete02.html",
 "title": "3.1.5.12. Concrete02 Material – Linear Tension Softening",
 "category": "command_manual",
 "manual_group": "material",
 "command": "Concrete02",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/Concrete02.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1359,
 "word_count": 215,
 "has_code": false,
 "has_table": true
} -->

## 3.1.5.12. Concrete02 Material – Linear Tension Softening

This command is used to construct a uniaxial concrete material as described in [Yassin1994]
.. function:: uniaxialMaterial Concrete02 $matTag $fpc $epsc0 $fpcu $epsU $lambda $ft $Ets

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material. |
| $fpc | *float* | concrete compressive strength at 28 days (compression is negative)* . |
| $epsc0 | *float* | concrete strain at maximum strength* . |
| $fpcu | *float* | concrete crushing strength*. |
| $epsU | *float* | concrete strain at crushing strength*. |
| $lambda | *float* | ratio between unloading slope at $epscu and initial slope. |
| $ft | *float* | tensile strength. |
| $ets | *float* | tension softening stiffness (absolute value) (slope of the linear tension softening branch) |

Note

- Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
- The initial slope for this model is (2*$fpc/$epsc0)

Typical Hysteretic Stress-Strain Relation for material

Comparison with Concrete01

Code Developed by: Filip Filippou, UC Berkeley
Images Developed by Silvia Mazzoni

**Yassin1994**

> Mohd Hisham Mohd Yassin, “Nonlinear Analysis of Prestressed Concrete Structures under Monotonic and Cycling Loads”, PhD dissertation, University of California, Berkeley, 1994.
