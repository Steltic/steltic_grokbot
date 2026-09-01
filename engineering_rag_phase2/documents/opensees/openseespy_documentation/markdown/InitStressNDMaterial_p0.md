<!-- chunk_id: InitStressNDMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/InitStressNDMaterial.html",
 "title": "4.15.5.2. Initial Stress Material",
 "category": "material",
 "command": "InitStressNDMaterial",
 "doc_section": "src",
 "rel_path": "src/InitStressNDMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 973,
 "word_count": 102,
 "has_code": false,
 "has_table": true
} -->

## 4.15.5.2. Initial Stress Material

**nDMaterial(*'InitStressNDMaterial'*, *matTag*, *otherTag*, *initStress*, *nDim*)**

This command is used to construct an Initial Stress material object.
The stress-strain behaviour for this material is defined by another material.
Initial Stress Material enables definition of initial stress for the material under consideration.
The strain that corresponds to the initial stress will be calculated from the other material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `otherTag` ([float](https://docs.python.org/3/library/functions.html#float)) | tag of the other material |
| `initStress` ([float](https://docs.python.org/3/library/functions.html#float)) | initial stress |
| `nDim` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of dimensions (e.g. if plane strain nDim=2) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Initial_Stress_Material)
