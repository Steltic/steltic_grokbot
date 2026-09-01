<!-- chunk_id: uniaxialMaterial_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterial.html",
 "title": "3.1.5. uniaxialMaterial Command",
 "category": "command_manual",
 "manual_group": "material",
 "command": "uniaxialMaterial",
 "doc_section": "user/manual/material",
 "rel_path": "user/manual/material/uniaxialMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 6204,
 "word_count": 287,
 "has_code": false,
 "has_table": true
} -->

## 3.1.5. uniaxialMaterial Command

This command is used to construct a uniaxial material, which provides a uniaxial stress-strain (or force-deformation) relationships.
.

**uniaxialMaterial $matType $matTag $matArgs**

| Argument | Type | Description |
| --- | --- | --- |
| $matType | *string* | material type |
| $matTag | *integer* | unique material tag. |
| $matArgs | *list* | a list of material arguments with number dependent on material type |

The following subsections contain information about **$matType**

1. Steel & Reinforcing-Steel Materials

  - [3.1.5.1. Steel01 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Steel01.html)
  - [3.1.5.2. Steel02 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Steel02.html)
  - [3.1.5.3. Steel4 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Steel4.html)
  - [3.1.5.4. Reinforcing Steel Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/ReinforcingSteel.html)
  - [3.1.5.5. DoddRestrepo Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/DoddRestrepo.html)
  - [3.1.5.6. Ramberg Osgood Steel Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/RambergOsgoodSteel.html)
  - [3.1.5.7. SteelMPF Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/SteelMPF.html)
  - [3.1.5.8. UVCUniaxial Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/UVCuniaxial.html)
  - [3.1.5.9. SteelFractureDI Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/SteelFractureDI.html)
  - [3.1.5.10. DuctileFracture Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/DuctileFracture.html)
2. Concrete Materials

  - [3.1.5.11. Concrete01 Material – Zero Tensile Strength](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Concrete01.html)
  - [3.1.5.12. Concrete02 Material – Linear Tension Softening](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Concrete02.html)
  - [3.1.5.13. Concrete04 Material – Popovics Concrete Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Concrete04.html)
  - [3.1.5.14. ASDConcrete1D Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/ASDConcrete1D.html)
  - [3.1.5.15. GMG_CyclicReinforcedConcrete Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/GMG_CyclicReinforcedConcrete.html)

1. Some Standard Uniaxial Materials

1. Generic Multilinear Hysteretic Materials

  - [3.1.5.16. Hysteretic Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Hysteretic.html)
  - [3.1.5.17. HystereticSM Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/HystereticSM.html)
  - [3.1.5.18. IMKBilin Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/IMKBilin.html)
  - [3.1.5.19. IMKPeakOriented Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/IMKPeakOriented.html)
  - [3.1.5.20. IMKPinching Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/IMKPinching.html)
  - [3.1.5.21. SLModel Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/SLModel.html)

1. Wrapper Uniaxial Materials

1. Other Uniaxial Materials

  - [3.1.5.22. BoucWenInfill Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/BoucWenInfill.html)
  - [3.1.5.23. HystereticPoly Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/HystereticPoly.html)
  - [3.1.5.24. HystereticAsym Material (Smooth asymmetric hysteresis)](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/HystereticAsym.html)
  - [3.1.5.25. HystereticSmooth Material (Smooth hysteretic material)](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/HystereticSmooth.html)
  - [3.1.5.26. DowelType Timber Joint Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/DowelType.html)
  - [3.1.5.27. CoulombDamper Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/CoulombDamper.html)
  - [3.1.5.28. Hertz Damp Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/HertzDamp.html)
  - [3.1.5.29. Jankowski Impact Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/JankowskiImpact.html)
  - [3.1.5.30. Viscoelastic Gap Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/ViscoelasticGap.html)
  - [3.1.5.31. Ratchet Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Ratchet.html)

1. PyTzQz uniaxial materials for p-y, t-z and q-z elements

- [3.1.5.32. PySimple1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/PySimple1.html)
- [3.1.5.33. TzSimple1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/TzSimple1.html)
- [3.1.5.34. QzSimple1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/QzSimple1.html)
- [3.1.5.35. PyLiq1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/PyLiq1.html)
- [3.1.5.36. TzLiq1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/TzLiq1.html)
- [3.1.5.37. QzLiq1 Material](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/QzLiq1.html)
