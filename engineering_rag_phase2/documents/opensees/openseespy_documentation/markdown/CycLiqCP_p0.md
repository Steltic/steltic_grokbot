<!-- chunk_id: CycLiqCP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/CycLiqCP.html",
 "title": "4.15.2.1. CycLiqCP",
 "category": "general",
 "command": "CycLiqCP",
 "doc_section": "src",
 "rel_path": "src/CycLiqCP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3260,
 "word_count": 376,
 "has_code": false,
 "has_table": true
} -->

## 4.15.2.1. CycLiqCP

**nDMaterial(*'CycLiqCP'*, *matTag*, *G0*, *kappa*, *h*, *Mfc*, *dre1*, *Mdc*, *dre2*, *rdr*, *alpha*, *dir*, *ein*, *rho*)**

This command is used to construct a multi-dimensional material object that that follows the constitutive behavior of a cyclic elastoplasticity model for large post- liquefaction deformation.

CycLiqCP material is a cyclic elastoplasticity model for large post-liquefaction deformation, and is implemented using a cutting plane algorithm. The model is capable of reproducing small to large deformation in the pre- to post-liquefaction regime. The elastic moduli of the model are pressure dependent. The plasticity in the model is developed within the framework of bounding surface plasticity, with special consideration to the formulation of reversible and irreversible dilatancy.

The model does not take into consideration of the state of sand, and requires different parameters for sand under different densities and confining pressures. The surfaces (i.e. failure and maximum pre-stress) are considered as circles in the pi plane.

The model has been validated against VELACS centrifuge model tests and has used on numerous simulations of liquefaction related problems.

When this material is employed in regular solid elements (e.g., FourNodeQuad, Brick), it simulates drained soil response. When solid-fluid coupled elements (u-p elements and SSP u-p elements) are used, the model is able to simulate undrained and partially drained behavior of soil.

> | `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
> | --- | --- |
> | `G0` ([float](https://docs.python.org/3/library/functions.html#float)) | A constant related to elastic shear modulus |
> | `kappa` ([float](https://docs.python.org/3/library/functions.html#float)) | bulk modulus |
> | `h` ([float](https://docs.python.org/3/library/functions.html#float)) | Model parameter for plastic modulus |
> | `Mfc` ([float](https://docs.python.org/3/library/functions.html#float)) | Stress ratio at failure in triaxial compression |
> | `dre1` ([float](https://docs.python.org/3/library/functions.html#float)) | Coefficient for reversible dilatancy generation |
> | `Mdc` ([float](https://docs.python.org/3/library/functions.html#float)) | Stress ratio at which the reversible dilatancy sign changes |
> | `dre2` ([float](https://docs.python.org/3/library/functions.html#float)) | Coefficient for reversible dilatancy release |
> | `rdr` ([float](https://docs.python.org/3/library/functions.html#float)) | Reference shear strain length |
> | `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameter controlling the decrease rate of irreversible dilatancy |
> | `dir` ([float](https://docs.python.org/3/library/functions.html#float)) | Coefficient for irreversible dilatancy potential |
> | `ein` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial void ratio |
> | `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | Saturated mass density |

The material formulations for the CycLiqCP object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`

See also [here](http://opensees.berkeley.edu/wiki/index.php/CycLiqCP_Material_(Cyclic_ElasticPlasticity))
