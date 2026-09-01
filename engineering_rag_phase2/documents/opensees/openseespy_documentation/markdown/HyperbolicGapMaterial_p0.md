<!-- chunk_id: HyperbolicGapMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/HyperbolicGapMaterial.html",
 "title": "4.14.5.15. Hyperbolic Gap Material",
 "category": "material",
 "command": "HyperbolicGapMaterial",
 "doc_section": "src",
 "rel_path": "src/HyperbolicGapMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1198,
 "word_count": 126,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.15. Hyperbolic Gap Material

**uniaxialMaterial(*'HyperbolicGapMaterial'*, *matTag*, *Kmax*, *Kur*, *Rf*, *Fult*, *gap*)**

This command is used to construct a hyperbolic gap material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Kmax` ([float](https://docs.python.org/3/library/functions.html#float)) | initial stiffness |
| `Kur` ([float](https://docs.python.org/3/library/functions.html#float)) | unloading/reloading stiffness |
| `Rf` ([float](https://docs.python.org/3/library/functions.html#float)) | failure ratio |
| `Fult` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate (maximum) passive resistance |
| `gap` ([float](https://docs.python.org/3/library/functions.html#float)) | initial gap |

Note

1. This material is implemented as a compression-only gap material. `Fult` and `gap` should be input as negative values.
2. Recomended Values:

  - `Kmax`        = 20300 kN/m of abutment width
  - `Kcur`        = `Kmax`
  - `Rf`  = 0.7
  - `Fult`        = -326 kN per meter of abutment width
  - `gap` = -2.54 cm

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Hyperbolic_Gap_Material)
