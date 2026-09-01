<!-- chunk_id: InitStressMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/InitStressMaterial.html",
 "title": "4.14.5.22. Initial Stress Material",
 "category": "material",
 "command": "InitStressMaterial",
 "doc_section": "src",
 "rel_path": "src/InitStressMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 843,
 "word_count": 88,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.22. Initial Stress Material

**uniaxialMaterial(*'InitStressMaterial'*, *matTag*, *otherTag*, *initStress*)**

This command is used to construct an Initial Stress material object. The stress-strain behaviour for this material is defined by another material. Initial Stress Material enables definition of initial stress for the material under consideration. The strain that corresponds to the initial stress will be calculated from the other material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `otherTag` ([float](https://docs.python.org/3/library/functions.html#float)) | tag of the other material |
| `initStress` ([float](https://docs.python.org/3/library/functions.html#float)) | initial stress |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Initial_Stress_Material)
