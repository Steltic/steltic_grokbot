<!-- chunk_id: TDConcreteMC10NL_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/TDConcreteMC10NL.html",
 "title": "4.14.2.16. TDConcreteMC10NL",
 "category": "general",
 "command": "TDConcreteMC10NL",
 "doc_section": "src",
 "rel_path": "src/TDConcreteMC10NL.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4360,
 "word_count": 500,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.16. TDConcreteMC10NL

**uniaxialMaterial(*'TDConcreteMC10NL'*, *matTag*, *fc*, *fcu*, *epscu*, *fct*, *Ec*, *Ecm*, *beta*, *tD*, *epsba*, *epsbb*, *epsda*, *epsdb*, *phiba*, *phibb*, *phida*, *phidb*, *tcast*, *cem*)**

This command is used to construct a uniaxial time-dependent concrete material object with non-linear behavior in compression (REF: Concrete02), nonlinear behavior in tension (REF: Tamai et al., 1988) and creep and shrinkage according to fib Model Code 2010.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete compressive strength (compression is negative) |
| `fcu` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete crushing strength (compression is negative) |
| `epscu` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at crushing strength (input as negative) |
| `fct` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete tensile strength (tension is positive) |
| `Ec` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete modulus of elasticity at loading age |
| `Ecm` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete modulus of elasticity at 28 days |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | tension softening parameter (tension softening exponent) |
| `tD` ([float](https://docs.python.org/3/library/functions.html#float)) | analysis time at initiation of drying (in days) |
| `epsba` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate basic shrinkage strain (input as negative) as per fib Model Code 2010 |
| `epsbb` ([float](https://docs.python.org/3/library/functions.html#float)) | fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010 |
| `epsda` ([float](https://docs.python.org/3/library/functions.html#float)) | product of ultimate drying shrinkage strain and relative humidity function as per fib Model Code 2010 |
| `epsdb` ([float](https://docs.python.org/3/library/functions.html#float)) | fitting parameter of the basic shrinkage time evolution function as per fib Model Code 2010 |
| `phiba` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter for the effect of compressive strength on basic creep as per fib Model Code 2010 |
| `phibb` ([float](https://docs.python.org/3/library/functions.html#float)) | fitting parameter of the basic creep time evolution function as per fib Model Code 2010 |
| `phida` ([float](https://docs.python.org/3/library/functions.html#float)) | product of the effect of compressive strength and relative humidity on drying creep as per fib Model Code 2010 |
| `phidb` ([float](https://docs.python.org/3/library/functions.html#float)) | fitting parameter of the drying creep time evolution function as per fib Model Code 2010 |
| `tcast` ([float](https://docs.python.org/3/library/functions.html#float)) | analysis time corresponding to concrete casting (in days; minimum value 2.0) |
| `cem` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficient dependent on the type of cement as per fib Model Code 2010 |

Note

1. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
2. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).

See also

Detailed descriptions of the model and its implementation can be found in the following:
(1) Knaack, A.M., Kurama, Y.C. 2018. Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural J. 115, 175-190. doi:10.14359/51701153
(2) Knaack, A.M., 2013. Sustainable concrete structures using recycled concrete aggregate: short-term and long-term behavior considering material variability. PhD Dissertation, Civil and Environmental Engineering and Earth Sciences, University of Notre Dame, Notre Dame, Indiana, USA, 680 pp
A manual describing the use of the model and sample files can be found at:
[https://data.mendeley.com/datasets/z4gxnhchky/5](https://data.mendeley.com/datasets/z4gxnhchky/5)
