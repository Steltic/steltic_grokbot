<!-- chunk_id: plainPattern_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/plainPattern.html",
 "title": "4.8.1. Plain Pattern",
 "category": "pattern",
 "command": "plainPattern",
 "doc_section": "src",
 "rel_path": "src/plainPattern.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1503,
 "word_count": 150,
 "has_code": false,
 "has_table": true
} -->

## 4.8.1. Plain Pattern

**pattern(*'Plain'*, *patternTag*, *tsTag*, *'-fact'*, *fact*)**

This commnand allows the user to construct a LoadPattern object. Each plain load pattern is associated with a TimeSeries object and can contain multiple NodalLoads, ElementalLoads and SP_Constraint objects. The command to generate LoadPattern object contains in { } the commands to generate all the loads and the single-point constraints in the pattern. To construct a load pattern and populate it, the following command is used:

| `patternTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among load patterns. |
| --- | --- |
| `tsTag` ([int](https://docs.python.org/3/library/functions.html#int)) | the tag of the time series to be used in the load pattern |
| `fact` ([float](https://docs.python.org/3/library/functions.html#float)) | constant factor. (optional) |

Note

the commands below to generate all the loads and sp constraints will be
included in last called pattern command.

- [4.8.1.1. load command](https://openseespydoc.readthedocs.io/en/latest/src/load.html)

  - [`load()`](https://openseespydoc.readthedocs.io/en/latest/src/load.html#load)
- [4.8.1.2. eleLoad command](https://openseespydoc.readthedocs.io/en/latest/src/eleload.html)

  - [`eleLoad()`](https://openseespydoc.readthedocs.io/en/latest/src/eleload.html#eleLoad)
- [4.8.1.3. sp command](https://openseespydoc.readthedocs.io/en/latest/src/sp.html)

  - [`sp()`](https://openseespydoc.readthedocs.io/en/latest/src/sp.html#sp)
