<!-- chunk_id: MinMax_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MinMax.html",
 "title": "4.14.5.17. MinMax Material",
 "category": "material",
 "command": "MinMax",
 "doc_section": "src",
 "rel_path": "src/MinMax.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1030,
 "word_count": 115,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.17. MinMax Material

**uniaxialMaterial(*'MinMax'*, *matTag*, *otherTag*, *'-min'*, *minStrain=1e-16*, *'-max'*, *maxStrain=1e16*)**

This command is used to construct a MinMax material object. This stress-strain behaviour for this material is provided by another material. If however the strain ever falls below or above certain threshold values, the other material is assumed to have failed. From that point on, values of 0.0 are returned for the tangent and stress.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `otherTag` ([float](https://docs.python.org/3/library/functions.html#float)) | tag of the other material |
| `minStrain` ([float](https://docs.python.org/3/library/functions.html#float)) | minimum value of strain. optional default = -1.0e16. |
| `maxStrain` ([float](https://docs.python.org/3/library/functions.html#float)) | max value of strain. optional default = 1.0e16. |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/MinMax_Material)
