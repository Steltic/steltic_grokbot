<!-- chunk_id: ElasticOrthotropic_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ElasticOrthotropic.html",
 "title": "3.1.6.2. Elastic Orthotropic Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "ElasticOrthotropic",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/ElasticOrthotropic.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 762,
 "word_count": 120,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.2. Elastic Orthotropic Material

This command is used to construct an ElasticOrthotropic material object.

**nDMaterial ElasticOrthotropic $matTag $Ex $Ey $Ez $vxy $vyz $vzx $Gxy $Gyz $Gzx <$rho>**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | unique tag identifying material |
| $Ex $Ey $Ez | 3 *float* | elastic moduli in three mutually perpendicular directions |
| $vxy $vyz $vzx | 3 *float* | Poisson’s ratios |
| $Gxy $Gyz $Gzx | 3 *float* | shear moduli |
| $rho | *float* | mass density. optional default = 0.0 |

Note

The material formulations for the ElasticOrthotropic object are “ThreeDimensional”, “PlaneStrain”, “Plane Stress”, “AxiSymmetric”, “BeamFiber”, and “PlateFiber”.

Code Developed by: [Michael H. Scott](https://cce.oregonstate.edu/scott)
