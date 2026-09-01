<!-- chunk_id: LayeredShell_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/LayeredShell.html",
 "title": "4.16.15. LayeredShell",
 "category": "general",
 "command": "LayeredShell",
 "doc_section": "src",
 "rel_path": "src/LayeredShell.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 606,
 "word_count": 63,
 "has_code": false,
 "has_table": true
} -->

## 4.16.15. LayeredShell

**section(*'LayeredShell'*, *sectionTag*, *nLayers*, **mats*)**

This command will create the section of the multi-layer shell element, including the multi-dimensional concrete, reinforcement material and the corresponding thickness.

| `sectionTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among sections |
| --- | --- |
| `nLayers` ([int](https://docs.python.org/3/library/functions.html#int)) | total numbers of layers |
| `mats` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of material tags and thickness, `[[mat1,thk1], ..., [mat2,thk2]]` |
