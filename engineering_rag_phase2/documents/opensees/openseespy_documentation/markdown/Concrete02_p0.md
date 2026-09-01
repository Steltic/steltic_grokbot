<!-- chunk_id: Concrete02_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Concrete02.html",
 "title": "4.14.2.2. Concrete02",
 "category": "general",
 "command": "Concrete02",
 "doc_section": "src",
 "rel_path": "src/Concrete02.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1641,
 "word_count": 166,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.2. Concrete02

**uniaxialMaterial(*'Concrete02'*, *matTag*, *fpc*, *epsc0*, *fpcu*, *epsU*, *lambda*, *ft*, *Ets*)**

This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fpc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete compressive strength at 28 days (compression is negative) |
| `epsc0` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at maximum strength |
| `fpcu` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete crushing strength |
| `epsU` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at crushing strength |
| `lambda` ([float](https://docs.python.org/3/library/functions.html#float)) | ratio between unloading slope at $epscu and initial slope |
| `ft` ([float](https://docs.python.org/3/library/functions.html#float)) | tensile strength |
| `Ets` ([float](https://docs.python.org/3/library/functions.html#float)) | tension softening stiffness (absolute value) (slope of the linear tension softening branch) |

Note

1. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
2. The initial slope for this model is (2*fpc/epsc0)

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Concrete02_Material_--_Linear_Tension_Softening)
