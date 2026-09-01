<!-- chunk_id: StressDensityModel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/StressDensityModel.html",
 "title": "4.15.1.14. StressDensityModel",
 "category": "model",
 "command": "StressDensityModel",
 "doc_section": "src",
 "rel_path": "src/StressDensityModel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3645,
 "word_count": 374,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.14. StressDensityModel

**nDMaterial(*'stressDensity'*, *matTag*, *mDen*, *eNot*, *A*, *n*, *nu*, *a1*, *b1*, *a2*, *b2*, *a3*, *b3*, *fd*, *muNot*, *muCyc*, *sc*, *M*, *patm*, **ssls*, *hsl*, *p1*)**

This command is used to construct a multi-dimensional stress density material object for modeling sand behaviour following the work of Cubrinovski and Ishihara (1998a,b).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `mDen` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density |
| `eNot` ([float](https://docs.python.org/3/library/functions.html#float)) | initial void ratio |
| `A` ([float](https://docs.python.org/3/library/functions.html#float)) | constant for elastic shear modulus |
| `n` ([float](https://docs.python.org/3/library/functions.html#float)) | pressure dependency exponent for elastic shear modulus |
| `nu` ([float](https://docs.python.org/3/library/functions.html#float)) | Poisson’s ratio |
| `a1` ([float](https://docs.python.org/3/library/functions.html#float)) | peak stress ratio coefficient (\(etaMax = a1 + b1*Is\)) |
| `b1` ([float](https://docs.python.org/3/library/functions.html#float)) | peak stress ratio coefficient (\(etaMax = a1 + b1*Is\)) |
| `a2` ([float](https://docs.python.org/3/library/functions.html#float)) | max shear modulus coefficient (\(Gn_max = a2 + b2*Is\)) |
| `b2` ([float](https://docs.python.org/3/library/functions.html#float)) | max shear modulus coefficient (\(Gn_max = a2 + b2*Is\)) |
| `a3` ([float](https://docs.python.org/3/library/functions.html#float)) | min shear modulus coefficient (\(Gn_min = a3 + b3*Is\)) |
| `b3` ([float](https://docs.python.org/3/library/functions.html#float)) | min shear modulus coefficient (\(Gn_min = a3 + b3*Is\)) |
| `fd` ([float](https://docs.python.org/3/library/functions.html#float)) | degradation constant |
| `muNot` ([float](https://docs.python.org/3/library/functions.html#float)) | dilatancy coefficient (monotonic loading) |
| `muCyc` ([float](https://docs.python.org/3/library/functions.html#float)) | dilatancy coefficient (cyclic loading) |
| `sc` ([float](https://docs.python.org/3/library/functions.html#float)) | dilatancy strain |
| `M` ([float](https://docs.python.org/3/library/functions.html#float)) | critical state stress ratio |
| `patm` ([float](https://docs.python.org/3/library/functions.html#float)) | atmospheric pressure (in appropriate units) |
| `ssls` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | void ratio of quasi steady state (QSS-line) at pressures [pmin, 10kPa, 30kPa, 50kPa, 100kPa, 200kPa, 400kPa] (default = [0.877, 0.877, 0.873, 0.870, 0.860, 0.850, 0.833]) |
| `hsl` ([float](https://docs.python.org/3/library/functions.html#float)) | void ratio of upper reference state (UR-line) for all pressures (default = 0.895) |
| `p1` ([float](https://docs.python.org/3/library/functions.html#float)) | pressure corresponding to ssl1 (default = 1.0 kPa) |

The material formulations for the StressDensityModel object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`

References

Cubrinovski, M. and Ishihara K. (1998a) ‘Modelling of sand behaviour based on state concept,’ Soils and Foundations, 38(3), 115-127.

Cubrinovski, M. and Ishihara K. (1998b) ‘State concept and modified elastoplasticity for sand modelling,’ Soils and Foundations, 38(4), 213-225.

Das, S. (2014) Three Dimensional Formulation for the Stress-Strain-Dilatancy Elasto-Plastic Constitutive Model for Sand Under Cyclic Behaviour, Master’s Thesis, University of Canterbury.
