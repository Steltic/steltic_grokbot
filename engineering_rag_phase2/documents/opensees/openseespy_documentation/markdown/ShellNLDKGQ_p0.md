<!-- chunk_id: ShellNLDKGQ_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ShellNLDKGQ.html",
 "title": "4.2.7.5. ShellNLDKGQ",
 "category": "general",
 "command": "ShellNLDKGQ",
 "doc_section": "src",
 "rel_path": "src/ShellNLDKGQ.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 924,
 "word_count": 89,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.5. ShellNLDKGQ

This command is used to construct a ShellNLDKGQ element object accounting for the geometric nonlinearity of large deformation using the updated Lagrangian formula, which is developed based on the ShellDKGQ element.

**element(*'ShellNLDKGQ'*, *eleTag*, **eleNodes*, *secTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes in counter-clockwise order |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined SectionForceDeformation object. currently can be a `'PlateFiberSection'`, a `'ElasticMembranePlateSection'` and a `'LayeredShell'` section |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ShellNLDKGQ)
