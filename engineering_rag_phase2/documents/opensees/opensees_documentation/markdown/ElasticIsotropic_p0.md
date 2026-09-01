<!-- chunk_id: ElasticIsotropic_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ElasticIsotropic.html",
 "title": "3.1.6.1. Elastic Isotropic Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "ElasticIsotropic",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/ElasticIsotropic.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 540,
 "word_count": 84,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.1. Elastic Isotropic Material

This command is used to construct an ElasticIsotropic material object.

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | unique tag identifying material |
| $E | *float* | elastic Modulus |
| $v | *float* | Poisson’s ratio |
| $rho | *float* | mass density. optional default = 0.0. |

Note

The material formulations for the ElasticIsotropic object are “ThreeDimensional,” “PlaneStrain,” “Plane Stress,” “AxiSymmetric,” and “PlateFiber.”

Code Developed by: [Michael H. Scott](https://cce.oregonstate.edu/scott)
