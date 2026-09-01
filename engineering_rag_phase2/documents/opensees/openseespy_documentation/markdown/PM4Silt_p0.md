<!-- chunk_id: PM4Silt_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PM4Silt.html",
 "title": "4.15.1.13. PM4Silt",
 "category": "general",
 "command": "PM4Silt",
 "doc_section": "src",
 "rel_path": "src/PM4Silt.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5772,
 "word_count": 616,
 "has_code": true,
 "has_table": true
} -->

## 4.15.1.13. PM4Silt

**nDMaterial(*'PM4Silt'*, *matTag*, *S_u*, *Su_Rat*, *G_o*, *h_po*, *Den <Su_factor*, *Patm*, *nu*, *nG*, *h0*, *eInit*, *lambda*, *phicv*, *nb_wet*, *nb_dry*, *nd*, *Ado*, *ru_max*, *zmax*, *cz*, *ce*, *Cgd*, *ckaf*, *m_m*, *CG_consol>*)**

Code Developed by: **Long Chen** and [pedro](https://www.ce.washington.edu/facultyfinder/pedro-arduino) at U.Washington.

[Boulanger-Ziotopoulou2018]

This command is used to construct a 2-dimensional PM4Silt material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `S_u` ([float](https://docs.python.org/3/library/functions.html#float)) | Undrained shear strength |
| `Su_Rat` ([float](https://docs.python.org/3/library/functions.html#float)) | Undrained shear strength ratio. |
| `G_o` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear modulus constant |
| `h_po` ([float](https://docs.python.org/3/library/functions.html#float)) | Contraction rate parameter |
| `Den` ([float](https://docs.python.org/3/library/functions.html#float)) | Mass density of the material |
| `Su_factor` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Undrained shear strength reduction factor |
| `P_atm` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Atmospheric pressure |
| `nu` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Poisson’s ratio. Default value is 0.3. |
| `nG` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Shear modulus exponent. Default value is 0.75. |
| `h0` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Variable that adjusts the ratio of plastic modulus to elastic modulus. Default value is 0.5. |
| `eInit` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Initial void ratios. Default value is 0.90. |
| `lambda` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: The slope of critical state line in e-ln(p) space. Default value is 0.060. |
| `phicv` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Critical state effective friction angle. Default value is 32 degrees. |
| `nb_wet` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Bounding surface parameter for loose of critical state conditions \(1.0 \geq nb_wet \geq 0.01\). Default value is 0.8. in cyclic loading |
| `nb_dry` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Bounding surface parameter for dense of critical state conditions \(nb_dry \geq 0\). Default value is 0.5. |
| `nd` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Dilatancy surface parameter \(nd \geq 0\). Default value is 0.3. |
| `Ado` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Dilatancy parameter. Default value is 0.8. with accumulation of fabric |
| `ru_max` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Maximum pore pressure ratio based on p’. |
| `z_max` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Fabric-dilatancy tensor parameter |
| `cz` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Fabric-dilatancy tensor parameter. Default value is 100.0. |
| `ce` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Variable that adjusts the rate of strain accumulation in cyclic loading |
| `cgd` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Variable that adjusts degradation of elastic modulus with accumulation of fabric. Default value is 3.0. in stress ratio space) |
| `ckaf` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Variable that controls the effect that sustained static shear stresses have on plastic modulus. Default value is 4.0. |
| `m_m` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Yield surface constant (radius of yield surface in stress ratio space). Default value is 0.01. |
| `CG_consol` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional: Reduction factor of elastic modulus for reconsolidation. \(CG_consol \geq 1\). Default value is 2.0. |

Note

The material formulation for the PM4Silt object is PlaneStrain

If both S_u and Su_Rat values are specified the value of S_u is used.

Valid Element Recorder queries are **stress**, **strain**, **alpha** (or backstressratio) for \(\mathbf{\alpha}\), **fabric** for \(\mathbf{z}\), and **alpha_in** (or alphain) for \(\mathbf{\alpha_{in}}\)

Elastic or response could be enforced by

```
updateMaterialStage('-material', matTag, '-stage', 0)
```

Elastoplastic by

```
updateMaterialStage('-material', matTag, '-stage', 1)
```

The program will use the default value of a secondary parameter if a negative input is assigned to that parameter, e.g. Ado = -1. However, FirstCall is mandatory when switching from elastic to elastoplastic if negative inputs are assigned to stress-dependent secondary parameters, e.g. Ado and zmax. FirstCall can be set as,

```
setParameter('-value', 0, '-ele', elementTag, 'FirstCall', matTag)
```

Post-shake reconsolidation can be activated by

```
setParameter('-value', 1, '-ele', elementTag, 'Postshake', matTag)

The user should check that the results are not sensitive to time step size.
```

Refer to [PM4Sand](https://openseespydoc.readthedocs.io/en/latest/src/PM4Sand.html) for examples.

[Boulanger-Ziotopoulou2018]

R.W.Boulanger, K.Ziotopoulou. “PM4Silt(Version 1): A Silt Plasticity Model for Earthquake Engineering Applications”. Report No. UCD/CGM-18/01 2018
