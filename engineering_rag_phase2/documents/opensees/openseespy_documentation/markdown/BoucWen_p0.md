<!-- chunk_id: BoucWen_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BoucWen.html",
 "title": "4.14.5.31. BoucWen Material",
 "category": "material",
 "command": "BoucWen",
 "doc_section": "src",
 "rel_path": "src/BoucWen.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1564,
 "word_count": 170,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.31. BoucWen Material

**uniaxialMaterial(*'BoucWen'*, *matTag*, *alpha*, *ko*, *n*, *gamma*, *beta*, *Ao*, *deltaA*, *deltaNu*, *deltaEta*)**

This command is used to construct a uniaxial Bouc-Wen smooth hysteretic material object. This material model is an extension of the original Bouc-Wen model that includes stiffness and strength degradation (Baber and Noori (1985)).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | ratio of post-yield stiffness to the initial elastic stiffenss (0< alpha <1) |
| `ko` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic stiffness |
| `n` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter that controls transition from linear to nonlinear range (as n increases the transition becomes sharper; n is usually grater or equal to 1) |
| `gamma` `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | parameters that control shape of hysteresis loop; depending on the values of gamma and beta softening, hardening or quasi-linearity can be simulated (look at the NOTES) |
| `Ao` `deltaA` ([float](https://docs.python.org/3/library/functions.html#float)) | parameters that control tangent stiffness |
| `deltaNu` `deltaEta` ([float](https://docs.python.org/3/library/functions.html#float)) | parameters that control material degradation |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/BoucWen_Material)
