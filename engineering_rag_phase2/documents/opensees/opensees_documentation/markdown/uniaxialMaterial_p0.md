<!-- chunk_id: uniaxialMaterial_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterial.html",
 "title": "uniaxialMaterial Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "uniaxialMaterial",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/uniaxialMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3021,
 "word_count": 210,
 "has_code": false,
 "has_table": true
} -->

## uniaxialMaterial Command

This command is used to construct a uniaxial material, which provides a uniaxial stress-strain (or force-deformation) relationships.
.

**`uniaxialMaterial $matType $matTag $matArgs`**

| Argument | Type | Description |
| --- | --- | --- |
| $matType | *string* | material type |
| $matTag | *integer* | unique material tag. |
| $matArgs | *list* | a list of material arguments with number dependent on material type |

The following subsections contain information about **$matType**

1. Steel & Reinforcing-Steel Materials

- [3.4.1.1. Steel01 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterials/Steel01.html)
- [Steel02 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterials/Steel02.html)

#. Concrete Materials
uniaxialMaterials/Concrete01
uniaxialMaterials/Concrete02
uniaxialMaterials/Concrete04
uniaxialMaterials/Concrete06
uniaxialMaterials/Concrete07
uniaxialMaterials/Concrete01
uniaxialMaterials/ConfinedConcrete01
uniaxialMaterials/ConcreteD
uniaxialMaterials/FRPConfinedConcrete
uniaxialMaterials/ConcreteCM

#. Some Standard Uniaxial Materials
uniaxialMaterials/Elastic
uniaxialMaterials/ElasticPP
uniaxialMaterials/ElasticPP_Gap
uniaxialMaterials/ElasticNoTension
uniaxialMaterials/ElasticBilin
uniaxialMaterials/ElasticMultiLinear
uniaxialMaterials/MultiLinear
uniaxialMaterials/Parallel
uniaxialMaterials/Series
uniaxialMaterials/InitialStrain
uniaxialMaterials/InitialStress
uniaxialMaterials/MinMax

#. Other Uniaxial Materials
uniaxialMaterials/CastFuse
uniaxialMaterials/ViscousDamper
uniaxialMaterials/BilinearOilDamper
uniaxialMaterials/Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear Hysteretic Response (Bilin Material)
uniaxialMaterials/Modified Ibarra-Medina-Krawinkler Deterioration Model with Peak-Oriented Hysteretic Response (ModIMKPeakOriented Material)
uniaxialMaterials/Modified Ibarra-Medina-Krawinkler Deterioration Model with Pinched Hysteretic Response (ModIMKPinching Material)
uniaxialMaterials/SAWS
uniaxialMaterials/BARSLIP
uniaxialMaterials/Bond_SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
uniaxialMaterials/Fatigue
uniaxialMaterials/Hardening
uniaxialMaterials/Impact
uniaxialMaterials/Hyperbolic Gap
uniaxialMaterials/LimitState
uniaxialMaterials/PathIndependent
uniaxialMaterials/Pinching4
uniaxialMaterials/Engineered Cementitious Composites
uniaxialMaterials/SelfCentering
uniaxialMaterials/Viscous
uniaxialMaterials/BoucWen
uniaxialMaterials/BWBN (Pinching Hysteretic Bouc-Wen)

1. PyTzQz uniaxial materials for p-y, t-z and q-z elements

- [3.4.1.3. PySimple1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterials/PySimple1.html)
- [3.4.1.4. TzSimple1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterials/TzSimple1.html)
- [3.4.1.5. QzSimple1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterials/QzSimple1.html)
