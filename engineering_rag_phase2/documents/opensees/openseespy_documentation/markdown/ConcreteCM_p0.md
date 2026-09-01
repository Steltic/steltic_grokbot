<!-- chunk_id: ConcreteCM_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ConcreteCM.html",
 "title": "4.14.2.12. ConcreteCM",
 "category": "general",
 "command": "ConcreteCM",
 "doc_section": "src",
 "rel_path": "src/ConcreteCM.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2400,
 "word_count": 236,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.12. ConcreteCM

**uniaxialMaterial(*'ConcreteCM'*, *matTag*, *fpcc*, *epcc*, *Ec*, *rc*, *xcrn*, *ft*, *et*, *rt*, *xcrp*, *mon*, *'-GapClose'*, *GapClose=0*)**

This command is used to construct a uniaxialMaterial ConcreteCM (Kolozvari et al., 2015), which is a uniaxial hysteretic constitutive model for concrete developed by Chang and Mander (1994).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fpcc` ([float](https://docs.python.org/3/library/functions.html#float)) | Compressive strength (\(f'_c\)) |
| `epcc` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain at compressive strength (\(\epsilon'_c\)) |
| `Ec` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial tangent modulus (\(E_c\)) |
| `rc` ([float](https://docs.python.org/3/library/functions.html#float)) | Shape parameter in Tsai’s equation defined for compression (\(r_c\)) |
| `xcrn` ([float](https://docs.python.org/3/library/functions.html#float)) | Non-dimensional critical strain on compression envelope (\(\epsilon^{-}_{cr}\), where the envelope curve starts following a straight line) |
| `ft` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile strength (\(f_t\)) |
| `et` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain at tensile strength (\(\epsilon_t\)) |
| `rt` ([float](https://docs.python.org/3/library/functions.html#float)) | Shape parameter in Tsai’s equation defined for tension (\(r_t\)) |
| `xcrp` ([float](https://docs.python.org/3/library/functions.html#float)) | Non-dimensional critical strain on tension envelope (\(\epsilon^{+}_{cr}\), where the envelope curve starts following a straight line - large value [e.g., 10000] recommended when tension stiffening is considered) |
| `mon` | optional, monotonic stress-strain relationship only: mon=1 (invoked in FSAM only), mon=0 (no impact since monotonic) |
| `'-GapClose'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | optional, denote next parameter is `GapClose` |
| `GapClose` ([float](https://docs.python.org/3/library/functions.html#float)) | optional, GapClose = 0, less gradual gap closure (default); GapClose = 1, more gradual gap closure |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ConcreteCM_-_Complete_Concrete_Model_by_Chang_and_Mander_(1994))
