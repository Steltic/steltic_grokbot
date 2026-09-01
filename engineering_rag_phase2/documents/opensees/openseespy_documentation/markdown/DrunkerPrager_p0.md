<!-- chunk_id: DrunkerPrager_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/DrunkerPrager.html",
 "title": "4.15.1.4. DruckerPrager",
 "category": "general",
 "command": "DrunkerPrager",
 "doc_section": "src",
 "rel_path": "src/DrunkerPrager.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2223,
 "word_count": 207,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.4. DruckerPrager

**nDMaterial(*'DruckerPrager'*, *matTag*, *K*, *G*, *sigmaY*, *rho*, *rhoBar*, *Kinf*, *Ko*, *delta1*, *delta2*, *H*, *theta*, *density*, *atmPressure=101e3*)**

This command is used to construct an multi dimensional material object that has a Drucker-Prager yield criterium.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `K` ([float](https://docs.python.org/3/library/functions.html#float)) | bulk modulus |
| `G` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus |
| `sigmaY` ([float](https://docs.python.org/3/library/functions.html#float)) | yield stress |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | frictional strength parameter |
| `rhoBar` ([float](https://docs.python.org/3/library/functions.html#float)) | controls evolution of plastic volume change, \(0\le rhoBar \le rho\). |
| `Kinf` ([float](https://docs.python.org/3/library/functions.html#float)) | nonlinear isotropic strain hardening parameter, \(Kinf \ge 0\). |
| `Ko` ([float](https://docs.python.org/3/library/functions.html#float)) | nonlinear isotropic strain hardening parameter, \(Ko \ge 0\). |
| `delta1` ([float](https://docs.python.org/3/library/functions.html#float)) | nonlinear isotropic strain hardening parameter, \(delta1\ge 0\). |
| `delta2` ([float](https://docs.python.org/3/library/functions.html#float)) | tension softening parameter, \(delta2\ge 0\). |
| `H` ([float](https://docs.python.org/3/library/functions.html#float)) | linear hardening parameter, \(H \ge 0\). |
| `theta` ([float](https://docs.python.org/3/library/functions.html#float)) | controls relative proportions of isotropic and kinematic hardening, \(0 \le theta \le 1\). |
| `density` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density of the material |
| `atmPressure` ([float](https://docs.python.org/3/library/functions.html#float)) | optional atmospheric pressure for update of elastic bulk and shear moduli |

The material formulations for the DrukerPrager object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`

See [theory](http://opensees.berkeley.edu/wiki/index.php/Drucker_Prager).
