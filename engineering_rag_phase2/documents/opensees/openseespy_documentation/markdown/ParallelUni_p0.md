<!-- chunk_id: ParallelUni_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ParallelUni.html",
 "title": "4.14.3.6. Parallel Material",
 "category": "material",
 "command": "ParallelUni",
 "doc_section": "src",
 "rel_path": "src/ParallelUni.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 945,
 "word_count": 88,
 "has_code": false,
 "has_table": true
} -->

## 4.14.3.6. Parallel Material

**uniaxialMaterial(*'Parallel'*, *matTag*, **MatTags*, *'-factors'*, **factorArgs*)**

This command is used to construct a parallel material object made up of an arbitrary number of previously-constructed UniaxialMaterial objects.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `MatTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | identification tags of materials making up the material model |
| `factorArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | factors to create a linear combination of the specified materials. Factors can be negative to subtract one material from an other. (optional, default = 1.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Parallel_Material)
