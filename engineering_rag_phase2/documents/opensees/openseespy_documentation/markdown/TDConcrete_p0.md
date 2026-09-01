<!-- chunk_id: TDConcrete_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/TDConcrete.html",
 "title": "4.14.2.13. TDConcrete",
 "category": "general",
 "command": "TDConcrete",
 "doc_section": "src",
 "rel_path": "src/TDConcrete.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3187,
 "word_count": 357,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.13. TDConcrete

**uniaxialMaterial(*'TDConcrete'*, *matTag*, *fc*, *fct*, *Ec*, *beta*, *tD*, *epsshu*, *psish*, *Tcr*, *phiu*, *psicr1*, *psicr2*, *tcast*)**

This command is used to construct a uniaxial time-dependent concrete material object with linear behavior in compression, nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to ACI 209R-92.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete compressive strength (compression is negative) |
| `fct` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete tensile strength (tension is positive) |
| `Ec` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete modulus of elasticity |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | tension softening parameter (tension softening exponent) |
| `tD` ([float](https://docs.python.org/3/library/functions.html#float)) | analysis time at initiation of drying (in days) |
| `epsshu` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate shrinkage strain as per ACI 209R-92 (shrinkage is negative) |
| `psish` ([float](https://docs.python.org/3/library/functions.html#float)) | fitting parameter of the shrinkage time evolution function as per ACI 209R-92 |
| `Tcr` ([float](https://docs.python.org/3/library/functions.html#float)) | creep model age (in days) |
| `phiu` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate creep coefficient as per ACI 209R-92 |
| `psicr1` ([float](https://docs.python.org/3/library/functions.html#float)) | fitting parameter of the creep time evolution function as per ACI 209R-92 |
| `psicr2` ([float](https://docs.python.org/3/library/functions.html#float)) | fitting parameter of the creep time evolution function as per ACI 209R-92 |
| `tcast` ([float](https://docs.python.org/3/library/functions.html#float)) | analysis time corresponding to concrete casting (in days; minimum value 2.0) |

Note

1. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
2. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).

See also

Detailed descriptions of the model and its implementation can be found in the following:
(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153
(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp
A manual describing the use of the model and sample files can be found at:
[https://data.mendeley.com/datasets/z4gxnhchky/5](https://data.mendeley.com/datasets/z4gxnhchky/5)
