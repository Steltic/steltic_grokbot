<!-- chunk_id: ShellNL_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ShellNL.html",
 "title": "4.2.7.7. ShellNL",
 "category": "general",
 "command": "ShellNL",
 "doc_section": "src",
 "rel_path": "src/ShellNL.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 808,
 "word_count": 73,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.7. ShellNL

**element(*'ShellNL'*, *eleTag*, **eleNodes*, *secTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of nine element nodes, input is the typical, firstly four corner nodes counter-clockwise, then mid-side nodes counter-clockwise and finally the central node |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined SectionForceDeformation object. currently can be a `'PlateFiberSection'`, a `'ElasticMembranePlateSection'` and a `'LayeredShell'` section |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ShellNL)
