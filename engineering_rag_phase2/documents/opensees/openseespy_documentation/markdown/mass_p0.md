<!-- chunk_id: mass_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/mass.html",
 "title": "4.9. mass command",
 "category": "general",
 "command": "mass",
 "doc_section": "src",
 "rel_path": "src/mass.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 470,
 "word_count": 53,
 "has_code": false,
 "has_table": true
} -->

## 4.9. mass command

**mass(*nodeTag*, **massValues*)**

This command is used to set the mass at a node, replacing any previously defined mass at the node.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying node whose mass is set |
| --- | --- |
| `massValues` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | ndf nodal mass values corresponding to each DOF |
