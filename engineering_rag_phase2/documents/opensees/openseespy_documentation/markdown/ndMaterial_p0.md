<!-- chunk_id: ndMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ndMaterial.html",
 "title": "4.15. nDMaterial commands",
 "category": "nd_material",
 "command": "ndMaterial",
 "doc_section": "src",
 "rel_path": "src/ndMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3966,
 "word_count": 193,
 "has_code": true,
 "has_table": true
} -->

## 4.15. nDMaterial commands

**nDMaterial(*matType*, *matTag*, **matArgs*)**

This command is used to construct an NDMaterial object which represents the stress-strain relationship at the gauss-point of a continuum element.

| `matType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | material type |
| --- | --- |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag. |
| `matArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of material arguments, must be preceded with `*`. |

For example,

```
matType = 'ElasticIsotropic'
matTag = 1
matArgs = [E, v]
nDMaterial(matType, matTag, *matArgs)
```

#### 4.15.1. Standard Models

The following contain information about available `matType`:

1. [ElasticIsotropic](https://openseespydoc.readthedocs.io/en/latest/src/elasticIsotropic.html)
2. [ElasticOrthotropic](https://openseespydoc.readthedocs.io/en/latest/src/elasticOrthotropic.html)
3. [J2Plasticity](https://openseespydoc.readthedocs.io/en/latest/src/J2Plasticity.html)
4. [DruckerPrager](https://openseespydoc.readthedocs.io/en/latest/src/DrunkerPrager.html)
5. [PlaneStress](https://openseespydoc.readthedocs.io/en/latest/src/PlaneStress.html)
6. [PlaneStrain](https://openseespydoc.readthedocs.io/en/latest/src/PlaneStrain.html)
7. [MultiaxialCyclicPlasticity](https://openseespydoc.readthedocs.io/en/latest/src/MultiAxialCyclicPlasticity.html)
8. [BoundingCamClay](https://openseespydoc.readthedocs.io/en/latest/src/BoundingCamClay.html)
9. [PlateFiber](https://openseespydoc.readthedocs.io/en/latest/src/PlateFiber.html)
10. [FSAM](https://openseespydoc.readthedocs.io/en/latest/src/FSAM.html)
11. [ManzariDafalias](https://openseespydoc.readthedocs.io/en/latest/src/ManzariDafalias.html)
12. [PM4Sand](https://openseespydoc.readthedocs.io/en/latest/src/PM4Sand.html)
13. [PM4Silt](https://openseespydoc.readthedocs.io/en/latest/src/PM4Silt.html)
14. [StressDensityModel](https://openseespydoc.readthedocs.io/en/latest/src/StressDensityModel.html)
15. [AcousticMedium](https://openseespydoc.readthedocs.io/en/latest/src/AcousticMedium.html)

#### 4.15.2. Tsinghua Sand Models

1. [CycLiqCP](https://openseespydoc.readthedocs.io/en/latest/src/CycLiqCP.html)
2. [CycLiqCPSP](https://openseespydoc.readthedocs.io/en/latest/src/CycLiqCPSP.html)

#### 4.15.3. Materials for Modeling Concrete Walls

1. [PlateFromPlaneStress](https://openseespydoc.readthedocs.io/en/latest/src/PlateFromPlaneStress.html)
2. [PlateRebar](https://openseespydoc.readthedocs.io/en/latest/src/PlateRebar.html)
3. [PlasticDamageConcretePlaneStress](https://openseespydoc.readthedocs.io/en/latest/src/PlasticDamageConcretePlaneStress.html)

#### 4.15.4. Contact Materials for 2D and 3D

1. [ContactMaterial2D](https://openseespydoc.readthedocs.io/en/latest/src/ContactMaterial2D.html)
2. [ContactMaterial3D](https://openseespydoc.readthedocs.io/en/latest/src/ContactMaterial3D.html)

#### 4.15.5. Wrapper material for Initial State Analysis

1. [InitialStateAnalysisWrapper](https://openseespydoc.readthedocs.io/en/latest/src/InitialStateAnalysisWrapper.html)
2. [Initial Stress Material](https://openseespydoc.readthedocs.io/en/latest/src/InitStressNDMaterial.html)
3. [Initial Strain Material](https://openseespydoc.readthedocs.io/en/latest/src/InitStrainNDMaterial.html)

#### 4.15.6. UC San Diego soil models

1. [PressureIndependMultiYield](https://openseespydoc.readthedocs.io/en/latest/src/PressureIndependMultiYield.html)
2. [PressureDependMultiYield](https://openseespydoc.readthedocs.io/en/latest/src/PressureDependMultiYield.html)
3. [PressureDependMultiYield02](https://openseespydoc.readthedocs.io/en/latest/src/PressureDependMultiYield02.html)
4. [PressureDependMultiYield03](https://openseespydoc.readthedocs.io/en/latest/src/PressureDependMultiYield03.html)

#### 4.15.7. UC San Diego Saturated Undrained soil

1. [FluidSolidPorousMaterial](https://openseespydoc.readthedocs.io/en/latest/src/FluidSolidPorousMaterial.html)
