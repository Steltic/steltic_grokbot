<!-- chunk_id: Concrete01_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Concrete01.html",
 "title": "4.14.2.1. Concrete01",
 "category": "general",
 "command": "Concrete01",
 "doc_section": "src",
 "rel_path": "src/Concrete01.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1212,
 "word_count": 125,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.1. Concrete01

**uniaxialMaterial(*'Concrete01'*, *matTag*, *fpc*, *epsc0*, *fpcu*, *epsU*)**

This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fpc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete compressive strength at 28 days (compression is negative) |
| `epsc0` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at maximum strength |
| `fpcu` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete crushing strength |
| `epsU` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at crushing strength |

Note

1. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
2. The initial slope for this model is (2*fpc/epsc0)

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Concrete01_Material_--_Zero_Tensile_Strength)
