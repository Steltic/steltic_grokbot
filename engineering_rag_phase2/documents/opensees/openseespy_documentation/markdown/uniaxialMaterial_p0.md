<!-- chunk_id: uniaxialMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/uniaxialMaterial.html",
 "title": "4.14. uniaxialMaterial commands",
 "category": "uniaxial_material",
 "command": "uniaxialMaterial",
 "doc_section": "src",
 "rel_path": "src/uniaxialMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 8856,
 "word_count": 396,
 "has_code": true,
 "has_table": true
} -->

## 4.14. uniaxialMaterial commands

**uniaxialMaterial(*matType*, *matTag*, **matArgs*)**

This command is used to construct a UniaxialMaterial object which represents uniaxial stress-strain (or force-deformation) relationships.

| `matType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | material type |
| --- | --- |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag. |
| `matArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of material arguments, must be preceded with `*`. |

For example,

```
matType = 'Steel01'
matTag = 1
matArgs = [Fy, E0, b]
uniaxialMaterial(matType, matTag, *matArgs)
```

The following contain information about available `matType`:

#### 4.14.1. Steel & Reinforcing-Steel Materials

1. [Steel01](https://openseespydoc.readthedocs.io/en/latest/src/steel01.html)
2. [Steel02](https://openseespydoc.readthedocs.io/en/latest/src/steel02.html)
3. [Steel4](https://openseespydoc.readthedocs.io/en/latest/src/steel4.html)
4. [ReinforcingSteel](https://openseespydoc.readthedocs.io/en/latest/src/ReinforcingSteel.html)
5. [Dodd_Restrepo](https://openseespydoc.readthedocs.io/en/latest/src/Dodd_Restrepo.html)
6. [RambergOsgoodSteel](https://openseespydoc.readthedocs.io/en/latest/src/RambergOsgoodSteel.html)
7. [SteelMPF](https://openseespydoc.readthedocs.io/en/latest/src/SteelMPF.html)
8. [Steel01Thermal](https://openseespydoc.readthedocs.io/en/latest/src/steel01thermal.html)

#### 4.14.2. Concrete Materials

1. [Concrete01](https://openseespydoc.readthedocs.io/en/latest/src/Concrete01.html)
2. [Concrete02](https://openseespydoc.readthedocs.io/en/latest/src/Concrete02.html)
3. [Concrete02IS material](https://openseespydoc.readthedocs.io/en/latest/src/Concrete02IS.html)
4. [Concrete04](https://openseespydoc.readthedocs.io/en/latest/src/Concrete04.html)
5. [Concrete06](https://openseespydoc.readthedocs.io/en/latest/src/Concrete06.html)
6. [Concrete07](https://openseespydoc.readthedocs.io/en/latest/src/Concrete07.html)
7. [Concrete01WithSITC](https://openseespydoc.readthedocs.io/en/latest/src/Concrete01WithSITC.html)
8. [ConfinedConcrete01](https://openseespydoc.readthedocs.io/en/latest/src/ConfinedConcrete01.html)
9. [ConcreteD](https://openseespydoc.readthedocs.io/en/latest/src/ConcreteD.html)
10. [FRPConfinedConcrete](https://openseespydoc.readthedocs.io/en/latest/src/FRPConfinedConcrete.html)
11. [FRPConfinedConcrete02](https://openseespydoc.readthedocs.io/en/latest/src/FRPConfinedConcrete02.html)
12. [ConcreteCM](https://openseespydoc.readthedocs.io/en/latest/src/ConcreteCM.html)
13. [TDConcrete](https://openseespydoc.readthedocs.io/en/latest/src/TDConcrete.html)
14. [TDConcreteEXP](https://openseespydoc.readthedocs.io/en/latest/src/TDConcreteEXP.html)
15. [TDConcreteMC10](https://openseespydoc.readthedocs.io/en/latest/src/TDConcreteMC10.html)
16. [TDConcreteMC10NL](https://openseespydoc.readthedocs.io/en/latest/src/TDConcreteMC10NL.html)

#### 4.14.3. Standard Uniaxial Materials

1. [Elastic Uniaxial Material](https://openseespydoc.readthedocs.io/en/latest/src/ElasticUni.html)
2. [Elastic-Perfectly Plastic Material](https://openseespydoc.readthedocs.io/en/latest/src/ElasticPP.html)
3. [Elastic-Perfectly Plastic Gap Material](https://openseespydoc.readthedocs.io/en/latest/src/ElasticPPGap.html)
4. [Elastic-No Tension Material](https://openseespydoc.readthedocs.io/en/latest/src/ENT.html)
5. [Hysteretic](https://openseespydoc.readthedocs.io/en/latest/src/Hysteretic.html)
6. HystereticSM
7. [Parallel Material](https://openseespydoc.readthedocs.io/en/latest/src/ParallelUni.html)
8. [Series Material](https://openseespydoc.readthedocs.io/en/latest/src/SeriesUni.html)

#### 4.14.4. PyTzQz uniaxial materials for p-y, t-z and q-z elements for modeling soil-structure interaction through the piles in a structural foundation

1. [PySimple1 Material](https://openseespydoc.readthedocs.io/en/latest/src/PySimple1.html)
2. [TzSimple1 Material](https://openseespydoc.readthedocs.io/en/latest/src/TzSimple1.html)
3. [QzSimple1 Material](https://openseespydoc.readthedocs.io/en/latest/src/QzSimple1.html)
4. [PyLiq1 Material](https://openseespydoc.readthedocs.io/en/latest/src/PyLiq1.html)
5. [TzLiq1 Material](https://openseespydoc.readthedocs.io/en/latest/src/TzLiq1.html)
6. [QzLiq1 Material](https://openseespydoc.readthedocs.io/en/latest/src/QzLiq1.html)

#### 4.14.5. Other Uniaxial Materials

1. [Hardening Material](https://openseespydoc.readthedocs.io/en/latest/src/Hardening.html)
2. [CastFuse Material](https://openseespydoc.readthedocs.io/en/latest/src/Cast.html)
3. [Damper material wrapper](https://openseespydoc.readthedocs.io/en/latest/src/Damper.html)
4. [ViscousDamper Material](https://openseespydoc.readthedocs.io/en/latest/src/ViscousDamper.html)
5. [BilinearOilDamper Material](https://openseespydoc.readthedocs.io/en/latest/src/BilinearOilDamper.html)
6. [Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear Hysteretic Response (Bilin Material)](https://openseespydoc.readthedocs.io/en/latest/src/Bilin.html)
7. [Modified Ibarra-Medina-Krawinkler Deterioration Model with Peak-Oriented Hysteretic Response (ModIMKPeakOriented Material)](https://openseespydoc.readthedocs.io/en/latest/src/ModIMKPeakOriented.html)
8. [Modified Ibarra-Medina-Krawinkler Deterioration Model with Pinched Hysteretic Response (ModIMKPinching Material)](https://openseespydoc.readthedocs.io/en/latest/src/ModIMKPinching.html)
9. [SAWS Material](https://openseespydoc.readthedocs.io/en/latest/src/SAWS.html)
10. [BarSlip Material](https://openseespydoc.readthedocs.io/en/latest/src/BarSlip.html)
11. [Bond SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars](https://openseespydoc.readthedocs.io/en/latest/src/Bond_SP01.html)
12. [Fatigue Material](https://openseespydoc.readthedocs.io/en/latest/src/Fatigue.html)
13. [Multiplier material wrapper](https://openseespydoc.readthedocs.io/en/latest/src/MultiplierUni.html)
14. [Impact Material](https://openseespydoc.readthedocs.io/en/latest/src/ImpactMaterial.html)
15. [Hyperbolic Gap Material](https://openseespydoc.readthedocs.io/en/latest/src/HyperbolicGapMaterial.html)
16. [Limit State Material](https://openseespydoc.readthedocs.io/en/latest/src/LimitState.html)
17. [MinMax Material](https://openseespydoc.readthedocs.io/en/latest/src/MinMax.html)
18. [ElasticBilin Material](https://openseespydoc.readthedocs.io/en/latest/src/ElasticBilin.html)
19. [ElasticMultiLinear Material](https://openseespydoc.readthedocs.io/en/latest/src/ElasticMultiLinear.html)
20. [MultiLinear](https://openseespydoc.readthedocs.io/en/latest/src/MultiLinear.html)
21. [Initial Strain Material](https://openseespydoc.readthedocs.io/en/latest/src/InitStrainMaterial.html)
22. [Initial Stress Material](https://openseespydoc.readthedocs.io/en/latest/src/InitStressMaterial.html)
23. [Penalty material wrapper](https://openseespydoc.readthedocs.io/en/latest/src/PenaltyUni.html)
24. [PathIndependent Material](https://openseespydoc.readthedocs.io/en/latest/src/PathIndependent.html)
25. [SimpleFracture material wrapper](https://openseespydoc.readthedocs.io/en/latest/src/SimpleFracture.html)
26. [TensionOnly material wrapper](https://openseespydoc.readthedocs.io/en/latest/src/TensionOnly.html)
27. [Pinching4 Material](https://openseespydoc.readthedocs.io/en/latest/src/Pinching4.html)
28. [Engineered Cementitious Composites Material](https://openseespydoc.readthedocs.io/en/latest/src/ECC01.html)
29. [SelfCentering Material](https://openseespydoc.readthedocs.io/en/latest/src/SelfCentering.html)
30. [Viscous Material](https://openseespydoc.readthedocs.io/en/latest/src/Viscous.html)
31. [BoucWen Material](https://openseespydoc.readthedocs.io/en/latest/src/BoucWen.html)
32. [BWBN Material](https://openseespydoc.readthedocs.io/en/latest/src/BWBN.html)
33. [KikuchiAikenHDR Material](https://openseespydoc.readthedocs.io/en/latest/src/KikuchiAikenHDR.html)
34. [KikuchiAikenLRB Material](https://openseespydoc.readthedocs.io/en/latest/src/KikuchiAikenLRB.html)
35. [AxialSp Material](https://openseespydoc.readthedocs.io/en/latest/src/AxialSp.html)
36. [AxialSpHD Material](https://openseespydoc.readthedocs.io/en/latest/src/AxialSpHD.html)
37. [Pinching Limit State Material](https://openseespydoc.readthedocs.io/en/latest/src/PinchingLimitStateMaterial.html)
38. [CFSWSWP Wood-Sheathed Cold-Formed Steel Shear Wall Panel](https://openseespydoc.readthedocs.io/en/latest/src/CFSWSWP.html)
39. [CFSSSWP Steel-Sheathed Cold-formed Steel Shear Wall Panel](https://openseespydoc.readthedocs.io/en/latest/src/CFSSSWP.html)
40. [Backbone Material](https://openseespydoc.readthedocs.io/en/latest/src/Backbone.html)
41. [Masonry](https://openseespydoc.readthedocs.io/en/latest/src/Masonry.html)
42. [Pipe Material](https://openseespydoc.readthedocs.io/en/latest/src/pipeMaterial.html)
