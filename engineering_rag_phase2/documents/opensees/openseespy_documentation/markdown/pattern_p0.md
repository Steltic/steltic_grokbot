<!-- chunk_id: pattern_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pattern.html",
 "title": "4.8. pattern commands",
 "category": "pattern",
 "command": "pattern",
 "doc_section": "src",
 "rel_path": "src/pattern.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1048,
 "word_count": 93,
 "has_code": false,
 "has_table": true
} -->

## 4.8. pattern commands

**pattern(*patternType*, *patternTag*, **patternArgs*)**

The pattern command is used to construct a LoadPattern and add it to the Domain. Each LoadPattern in OpenSees has a TimeSeries associated with it. In addition it may contain ElementLoads, NodalLoads and SinglePointConstraints. Some of these SinglePoint constraints may be associated with GroundMotions.

| `patternType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | pattern type. |
| --- | --- |
| `patternTag` ([int](https://docs.python.org/3/library/functions.html#int)) | pattern tag. |
| `patternArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of pattern arguments |

The following contain information about available `patternType`:

1. [Plain Pattern](https://openseespydoc.readthedocs.io/en/latest/src/plainPattern.html)
2. [UniformExcitation Pattern](https://openseespydoc.readthedocs.io/en/latest/src/uniformExcitation.html)
3. [Multi-Support Excitation Pattern](https://openseespydoc.readthedocs.io/en/latest/src/multiExcitation.html)
