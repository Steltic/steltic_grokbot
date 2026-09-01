<!-- chunk_id: SeriesUni_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SeriesUni.html",
 "title": "4.14.3.7. Series Material",
 "category": "material",
 "command": "SeriesUni",
 "doc_section": "src",
 "rel_path": "src/SeriesUni.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 605,
 "word_count": 55,
 "has_code": false,
 "has_table": true
} -->

## 4.14.3.7. Series Material

**uniaxialMaterial(*'Series'*, *matTag*, **matTags*)**

This command is used to construct a series material object made up of an arbitrary number of previously-constructed UniaxialMaterial objects.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `matTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | identification tags of materials making up the material model |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Series_Material)
