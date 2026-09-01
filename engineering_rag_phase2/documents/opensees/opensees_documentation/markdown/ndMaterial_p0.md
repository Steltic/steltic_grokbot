<!-- chunk_id: ndMaterial_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterial.html",
 "title": "3.1.6. nDMaterial Command",
 "category": "command_manual",
 "manual_group": "material",
 "command": "ndMaterial",
 "doc_section": "user/manual/material",
 "rel_path": "user/manual/material/ndMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 7448,
 "word_count": 404,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6. nDMaterial Command

This command is used to construct an NDMaterial object which represents the stress-strain relationship at the gauss-point of a continuum element.

**nDMaterial $matType $matTag $matArgs**

| Argument | Type | Description |
| --- | --- | --- |
| $matType | *string* | material type |
| $matTag | *integer* | unique material tag. |
| $matArgs | *list* | a list of material arguments with number dependent on material type |

Note

The valid queries to any uniaxial material when creating an ElementRecorder are ‘strain’, and ‘stress’. Some materials have additional queries to which they will respond. These are documented in the NOTES section for those materials.

The following contain information about matType? and the args required for each of the available material types:

- [3.1.6.1. Elastic Isotropic Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ElasticIsotropic.html)
- [3.1.6.2. Elastic Orthotropic Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ElasticOrthotropic.html)
- [3.1.6.3. J2 Plasticity Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/J2Plasticity.html)
- [3.1.6.4. Drucker Prager Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/DruckerPrager.html)
- [3.1.6.5. Manzari Dafalias Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ManzariDafalias.html)
- [3.1.6.6. Bounding Cam Clay](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/BoundingCamClay.html)
- [3.1.6.7. PM4Sand Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PM4Sand.html)
- [3.1.6.8. PM4Silt Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PM4Silt.html)
- [3.1.6.9. Pressure Independent Multi Yield](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PressureIndependentMultiYield.html)
- [3.1.6.10. Pressure Dependent Multi Yield](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PressureDependentMultiYield.html)
- [3.1.6.11. Pressure Dependent Multi Yield 02](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PressureDependentMultiYield02.html)
- [3.1.6.12. J2CyclicBoundingSurface Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/J2CyclicBoundingSurface.html)
- [3.1.6.13. SANISAND-MS Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/SAniSandMS.html)
- [3.1.6.14. Orthotropic Material Wrapper](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/Orthotropic.html)

  - [3.1.6.14.1. Usage Notes](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/Orthotropic.html#usage-notes)
- [3.1.6.15. Series3D Material Wrapper](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/Series3D.html)

  - [3.1.6.15.1. Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/Series3D.html#theory)
  - [3.1.6.15.2. Usage Notes](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/Series3D.html#usage-notes)
- [3.1.6.16. Parallel3D Material Wrapper](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/Parallel3D.html)

  - [3.1.6.16.1. Usage Notes](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/Parallel3D.html#usage-notes)
- [3.1.6.17. InitStrain Material Wrapper](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/InitStrain.html)

  - [3.1.6.17.1. Usage Notes](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/InitStrain.html#usage-notes)
- [3.1.6.18. ASDConcrete3D Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDConcrete3D.html)

  - [3.1.6.18.1. Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDConcrete3D.html#theory)
  - [3.1.6.18.2. Usage Notes](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDConcrete3D.html#usage-notes)
  - [3.1.6.18.3. References](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDConcrete3D.html#references)
- [3.1.6.19. ASDPlasticMaterial](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html)

  - [3.1.6.19.1. Yield Functions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html)
  - [3.1.6.19.2. Plastic Flow Directions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html)
  - [3.1.6.19.3. Elasticity Types](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html)
  - [3.1.6.19.4. Hardening Functions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/HardeningFunctions.html)
  - [3.1.6.19.5. ASDPlasticMaterial Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#asdplasticmaterial-theory)
  - [3.1.6.19.6. Integration Options](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#id4)
  - [3.1.6.19.7. Other Features](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#other-features)
  - [3.1.6.19.8. Implementation details](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#implementation-details)
  - [3.1.6.19.9. Example](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#example)
- [3.1.6.20. OrthotropicRAConcrete Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/OrthotropicRAConcrete.html)
- [3.1.6.21. SmearedSteelDoubleLayer Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/SmearedSteelDoubleLayer.html)

Concrete Damage Model
Plane Stress Material
Plane Strain Material
Multi Axial Cyclic Plasticity
Plate Fiber Material
Plane Stress Concrete Materials
FSAM - 2D RC Panel Constitutive Behavior
Tsinghua Sand Models
CycLiqCP Material (Cyclic ElasticPlasticity)
CycLiqCPSP Material
Manzari Dafalias Material
Stress Density Material
Materials for Modeling Concrete Walls
PlaneStressUserMaterial
PlateFromPlaneStress
PlateRebar
LayeredShell
Contact Materials for 2D and 3D
ContactMaterial2D
ContactMaterial3D
Wrapper material for Initial State Analysis
InitialStateAnalysisWrapper
UC San Diego soil models (Linear/Nonlinear, dry/drained/undrained soil response under general 2D/3D static/cyclic loading conditions (please visit UCSD for examples)
PressureIndependMultiYield Material
PressureDependMultiYield Material
PressureDependMultiYield02 Material
PressureDependMultiYield03 Material
UC San Diego Saturated Undrained soil
FluidSolidPorousMaterial
Misc.
AcousticMedium
Steel & Reinforcing-Steel Materials
UVCmultiaxial (Updated Voce-Chaboche)
UVCplanestress (Updated Voce-Chaboche)
