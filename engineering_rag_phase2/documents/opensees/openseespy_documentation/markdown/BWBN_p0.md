<!-- chunk_id: BWBN_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BWBN.html",
 "title": "4.14.5.32. BWBN Material",
 "category": "material",
 "command": "BWBN",
 "doc_section": "src",
 "rel_path": "src/BWBN.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1787,
 "word_count": 191,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.32. BWBN Material

**uniaxialMaterial(*'BWBN'*, *matTag*, *alpha*, *ko*, *n*, *gamma*, *beta*, *Ao*, *q*, *zetas*, *p*, *Shi*, *deltaShi*, *lambda*, *tol*, *maxIter*)**

This command is used to construct a uniaxial Bouc-Wen pinching hysteretic material object. This material model is an extension of the original Bouc-Wen model that includes pinching (Baber and Noori (1986) and Foliente (1995)).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | ratio of post-yield stiffness to the initial elastic stiffenss (0< alpha <1) |
| `ko` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic stiffness |
| `n` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter that controls transition from linear to nonlinear range (as n increases the transition becomes sharper; n is usually grater or equal to 1) |
| `gamma` `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | parameters that control shape of hysteresis loop; depending on the values of gamma and beta softening, hardening or quasi-linearity can be simulated (look at the BoucWen Material) |
| `Ao` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter that controls tangent stiffness |
| `q` `zetas` `p` `Shi` `deltaShi` `lambda` ([float](https://docs.python.org/3/library/functions.html#float)) | parameters that control pinching |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | tolerance |
| `maxIter` ([float](https://docs.python.org/3/library/functions.html#float)) | maximum iterations |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/BWBN_Material)
