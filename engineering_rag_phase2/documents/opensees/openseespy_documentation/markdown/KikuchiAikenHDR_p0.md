<!-- chunk_id: KikuchiAikenHDR_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/KikuchiAikenHDR.html",
 "title": "4.14.5.33. KikuchiAikenHDR Material",
 "category": "material",
 "command": "KikuchiAikenHDR",
 "doc_section": "src",
 "rel_path": "src/KikuchiAikenHDR.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2277,
 "word_count": 278,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.33. KikuchiAikenHDR Material

**uniaxialMaterial(*'KikuchiAikenHDR'*, *matTag*, *tp*, *ar*, *hr*, *<'-coGHU'*, *cg*, *ch*, *cu>*, *<'-coMSS'*, *rs*, *rf>*)**

This command is used to construct a uniaxial KikuchiAikenHDR material object. This material model produces nonlinear hysteretic curves of high damping rubber bearings (HDRs).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `tp` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | rubber type (see note 1) |
| `ar` ([float](https://docs.python.org/3/library/functions.html#float)) | area of rubber [unit: m^2] (see note 2) |
| `hr` ([float](https://docs.python.org/3/library/functions.html#float)) | total thickness of rubber [unit: m] (see note 2) |
| `cg` `ch` `cu` ([float](https://docs.python.org/3/library/functions.html#float)) | correction coefficients for equivalent shear modulus (`cg`), equivalent viscous daming ratio (`ch`), ratio of shear force at zero displacement (`cu`). |
| `rs` `rf` ([float](https://docs.python.org/3/library/functions.html#float)) | reduction rate for stiffness (`rs`) and force (`rf`) (see note 3) |

Note

1. Following rubber types for    `tp` are available:

  - `'X0.6'` Bridgestone X0.6, standard compressive stress, up to 400% shear strain
  - `'X0.6-0MPa'` Bridgestone X0.6, zero compressive stress, up to 400% shear strain
  - `'X0.4'` Bridgestone X0.4, standard compressive stress, up to 400% shear strain
  - `'X0.4-0MPa'` Bridgestone X0.4, zero compressive stress, up to 400% shear strain
  - `'X0.3'` Bridgestone X0.3, standard compressive stress, up to 400% shear strain
  - `'X0.3-0MPa'` Bridgestone X0.3, zero compressive stress, up to 400% shear strain
2. This material uses SI unit in calculation formula.    `ar` and    `hr` must be converted into [m^2] and [m], respectively.
3. `rs` and    `rf` are　available if this material is applied to multipleShearSpring (MSS) element. Recommended values are    `rs` = \(\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)^2}\) and    `rf` = \(\frac{1}{\sum_{i=0}^{n-1}\sin(\pi*i/n)}\), where n is the number of springs in the MSS. For example, when n=8,    `rs` =0.2500,    `rf` =0.1989.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/KikuchiAikenHDR_Material)
