<!-- chunk_id: ElasticPPGap_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElasticPPGap.html",
 "title": "4.14.3.3. Elastic-Perfectly Plastic Gap Material",
 "category": "material",
 "command": "ElasticPPGap",
 "doc_section": "src",
 "rel_path": "src/ElasticPPGap.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1211,
 "word_count": 126,
 "has_code": false,
 "has_table": true
} -->

## 4.14.3.3. Elastic-Perfectly Plastic Gap Material

**uniaxialMaterial(*'ElasticPPGap'*, *matTag*, *E*, *Fy*, *gap*, *eta=0.0*, *damage='noDamage'*)**

This command is used to construct an elastic perfectly-plastic gap uniaxial material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | tangent |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | stress or force at which material reaches plastic state |
| `gap` ([float](https://docs.python.org/3/library/functions.html#float)) | initial gap (strain or deformation) |
| `eta` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening ratio (=Eh/E), which can be negative |
| `damage` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | an optional string to specify whether to accumulate damage or not in the material. With the default string, `'noDamage'` the gap material will re-center on load reversal. If the string `'damage'` is provided this recentering will not occur and gap will grow. |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Elastic-Perfectly_Plastic_Gap_Material)
