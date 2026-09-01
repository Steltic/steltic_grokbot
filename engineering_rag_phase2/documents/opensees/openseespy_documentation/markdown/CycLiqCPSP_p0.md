<!-- chunk_id: CycLiqCPSP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/CycLiqCPSP.html",
 "title": "4.15.2.2. CycLiqCPSP",
 "category": "general",
 "command": "CycLiqCPSP",
 "doc_section": "src",
 "rel_path": "src/CycLiqCPSP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3798,
 "word_count": 427,
 "has_code": false,
 "has_table": true
} -->

## 4.15.2.2. CycLiqCPSP

**nDMaterial(*'CycLiqCPSP'*, *matTag*, *G0*, *kappa*, *h*, *M*, *dre1*, *dre2*, *rdr*, *alpha*, *dir*, *lambdac*, *ksi*, *e0*, *np*, *nd*, *ein*, *rho*)**

This command is used to construct a multi-dimensional material object that that follows the constitutive behavior of a cyclic elastoplasticity model for large post- liquefaction deformation.

CycLiqCPSP material is a constitutive model for sand with special considerations for cyclic behaviour and accumulation of large post-liquefaction shear deformation, and is implemented using a cutting plane algorithm. The model: (1) achieves the simulation of post-liquefaction shear deformation based on its physics, allowing the unified description of pre- and post-liquefaction behavior of sand; (2) directly links the cyclic mobility of sand with reversible and irreversible dilatancy, enabling the unified description of monotonic and cyclic loading; (3) introduces critical state soil mechanics concepts to achieve unified modelling of sand under different states.

The critical, maximum stress ratio and reversible dilatancy surfaces follow a rounded triangle in the pi plane similar to the Matsuoka-Nakai criterion.

When this material is employed in regular solid elements (e.g., FourNodeQuad, Brick), it simulates drained soil response. When solid-fluid coupled elements (u-p elements and SSP u-p elements) are used, the model is able to simulate undrained and partially drained behavior of soil.

> | `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
> | --- | --- |
> | `G0` ([float](https://docs.python.org/3/library/functions.html#float)) | A constant related to elastic shear modulus |
> | `kappa` ([float](https://docs.python.org/3/library/functions.html#float)) | bulk modulus |
> | `h` ([float](https://docs.python.org/3/library/functions.html#float)) | Model parameter for plastic modulus |
> | `M` ([float](https://docs.python.org/3/library/functions.html#float)) | Critical state stress ratio |
> | `dre1` ([float](https://docs.python.org/3/library/functions.html#float)) | Coefficient for reversible dilatancy generation |
> | `dre2` ([float](https://docs.python.org/3/library/functions.html#float)) | Coefficient for reversible dilatancy release |
> | `rdr` ([float](https://docs.python.org/3/library/functions.html#float)) | Reference shear strain length |
> | `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameter controlling the decrease rate of irreversible dilatancy |
> | `dir` ([float](https://docs.python.org/3/library/functions.html#float)) | Coefficient for irreversible dilatancy potential |
> | `lambdac` ([float](https://docs.python.org/3/library/functions.html#float)) | Critical state constant |
> | `ksi` ([float](https://docs.python.org/3/library/functions.html#float)) | Critical state constant |
> | `e0` ([float](https://docs.python.org/3/library/functions.html#float)) | Void ratio at pc=0 |
> | `np` ([float](https://docs.python.org/3/library/functions.html#float)) | Material constant for peak mobilized stress ratio |
> | `nd` ([float](https://docs.python.org/3/library/functions.html#float)) | Material constant for reversible dilatancy generation stress ratio |
> | `ein` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial void ratio |
> | `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | Saturated mass density |

The material formulations for the CycLiqCP object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`

See also [here](http://opensees.berkeley.edu/wiki/index.php/CycLiqCPSP_Material)

REFERENCES: Wang R., Zhang J.M., Wang G., 2014. A unified plasticity model for large post-liquefaction shear deformation of sand. Computers and Geotechnics. 59, 54-66.
