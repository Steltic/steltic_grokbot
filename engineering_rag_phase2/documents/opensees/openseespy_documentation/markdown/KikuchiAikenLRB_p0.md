<!-- chunk_id: KikuchiAikenLRB_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/KikuchiAikenLRB.html",
 "title": "4.14.5.34. KikuchiAikenLRB Material",
 "category": "material",
 "command": "KikuchiAikenLRB",
 "doc_section": "src",
 "rel_path": "src/KikuchiAikenLRB.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2473,
 "word_count": 280,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.34. KikuchiAikenLRB Material

**uniaxialMaterial(*'KikuchiAikenLRB'*, *matTag*, *type*, *ar*, *hr*, *gr*, *ap*, *tp*, *alph*, *beta*, *<'-T'*, *temp>*, *<'-coKQ'*, *rk*, *rq>*, *<'-coMSS'*, *rs*, *rf>*)**

This command is used to construct a uniaxial KikuchiAikenLRB material object. This material model produces nonlinear hysteretic curves of lead-rubber bearings.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `type` ([int](https://docs.python.org/3/library/functions.html#int)) | rubber type (see note 1) |
| `ar` ([float](https://docs.python.org/3/library/functions.html#float)) | area of rubber [unit: m^2] |
| `hr` ([float](https://docs.python.org/3/library/functions.html#float)) | total thickness of rubber [unit: m] |
| `gr` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus of rubber [unit: N/m^2] |
| `ap` ([float](https://docs.python.org/3/library/functions.html#float)) | area of lead plug [unit: m^2] |
| `tp` ([float](https://docs.python.org/3/library/functions.html#float)) | yield stress of lead plug [unit: N/m^2] |
| `alph` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus of lead plug [unit: N/m^2] |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | ratio of initial stiffness to yielding stiffness |
| `temp` ([float](https://docs.python.org/3/library/functions.html#float)) | temperature [unit: °C] |
| `rk` `rq` ([float](https://docs.python.org/3/library/functions.html#float)) | reduction rate for yielding stiffness ( `rk`) and force at zero displacement ( `rq`) |
| `rs` `rf` ([float](https://docs.python.org/3/library/functions.html#float)) | reduction rate for stiffness ( `rs`) and force ( `rf`) (see note 3) |

Note

1. Following rubber types for    `type` are available:

  - `1` lead-rubber bearing, up to 400% shear strain [Kikuchi et al., 2010 & 2012]
2. This material uses SI unit in calculation formula. Input arguments must be converted into [m], [m^2], [N/m^2].
3. `rs` and    `rf` are available if this material is applied to multipleShearSpring (MSS) element. Recommended values are    `rs` = \(\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)^2}\) and    `rf` = \(\frac{1}{\sum_{i=0}{n-1}\sin(\pi*i/n)}\), where n is the number of springs in the MSS. For example, when n=8,    `rs` = 0.2500 and `rf` = 0.1989.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/KikuchiAikenLRB_Material)
