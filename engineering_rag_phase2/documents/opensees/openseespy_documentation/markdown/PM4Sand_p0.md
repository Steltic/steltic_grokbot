<!-- chunk_id: PM4Sand_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PM4Sand.html",
 "title": "4.15.1.12. PM4Sand",
 "category": "general",
 "command": "PM4Sand",
 "doc_section": "src",
 "rel_path": "src/PM4Sand.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4030,
 "word_count": 387,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.12. PM4Sand

**nDMaterial(*'PM4Sand'*, *matTag*, *D_r*, *G_o*, *h_po*, *Den*, *P_atm*, *h_o*, *e_max*, *e_min*, *n_b*, *n_d*, *A_do*, *z_max*, *c_z*, *c_e*, *phi_cv*, *nu*, *g_degr*, *c_dr*, *c_kaf*, *Q_bolt*, *R_bolt*, *m_par*, *F_sed*, *p_sed*)**

This command is used to construct a 2-dimensional PM4Sand material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `D_r` ([float](https://docs.python.org/3/library/functions.html#float)) | Relative density, in fraction |
| `G_o` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear modulus constant |
| `h_po` ([float](https://docs.python.org/3/library/functions.html#float)) | Contraction rate parameter |
| `Den` ([float](https://docs.python.org/3/library/functions.html#float)) | Mass density of the material |
| `P_atm` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Atmospheric pressure |
| `h_o` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Variable that adjusts the ratio of plastic modulus to elastic modulus |
| `e_max` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Maximum and minimum void ratios |
| `e_min` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Maximum and minimum void ratios |
| `n_b` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Bounding surface parameter, \(n_b \ge 0\) |
| `n_d` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Dilatancy surface parameter \(n_d \ge 0\) |
| `A_do` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Dilatancy parameter, will be computed at the time of initialization if input value is negative |
| `z_max` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Fabric-dilatancy tensor parameter |
| `c_z` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Fabric-dilatancy tensor parameter |
| `c_e` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Variable that adjusts the rate of strain accumulation in cyclic loading |
| `phi_cv` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Critical state effective friction angle |
| `nu` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Poisson’s ratio |
| `g_degr` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Variable that adjusts degradation of elastic modulus with accumulation of fabric |
| `c_dr` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Variable that controls the rotated dilatancy surface |
| `c_kaf` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Variable that controls the effect that sustained static shear stresses have on plastic modulus |
| `Q_bolt` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Critical state line parameter |
| `R_bolt` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Critical state line parameter |
| `m_par` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Yield surface constant (radius of yield surface in stress ratio space) |
| `F_sed` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Variable that controls the minimum value the reduction factor of the elastic moduli can get during reconsolidation |
| `p_sed` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional, Mean effective stress up to which reconsolidation strains are enhanced |

The material formulations for the PM4Sand object are:

- `'PlaneStrain'`

See als [here](http://opensees.berkeley.edu/wiki/index.php/PM4Sand_Material)

References

R.W.Boulanger, K.Ziotopoulou. “PM4Sand(Version 3.1): A Sand Plasticity Model for Earthquake Engineering Applications”. Report No. UCD/CGM-17/01 2017
