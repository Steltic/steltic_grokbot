<!-- chunk_id: setNodeTemperature_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/setNodeTemperature.html",
 "title": "7.20. setNodeTemperature command",
 "category": "general",
 "command": "setNodeTemperature",
 "doc_section": "src",
 "rel_path": "src/setNodeTemperature.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 735,
 "word_count": 56,
 "has_code": false,
 "has_table": true
} -->

## 7.20. setNodeTemperature command

**setNodeTemperature(*nodeTag*, *value*)**

set the nodal temperature for [Elastic Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/pipe.html) and [Curved Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/curvedPipe.html) elements.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `value` ([float](https://docs.python.org/3/library/functions.html#float)) | the temperature value for the node. The nodal temperature will affect the thermal expansion for both [Elastic Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/pipe.html) and [Curved Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/curvedPipe.html) elements. |
