<!-- chunk_id: ShellNLDKGT_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ShellNLDKGT.html",
 "title": "4.2.7.6. ShellNLDKGT",
 "category": "general",
 "command": "ShellNLDKGT",
 "doc_section": "src",
 "rel_path": "src/ShellNLDKGT.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 957,
 "word_count": 94,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.6. ShellNLDKGT

This command is used to construct a ShellNLDKGT element object accounting for the geometric nonlinearity of large deformation using the updated Lagrangian formula, which is developed based on the ShellDKGT element.

**element(*'ShellNLDKGT'*, *eleTag*, **eleNodes*, *secTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of three element nodes in clockwise or counter-clockwise order around the element |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined SectionForceDeformation object. currently can be a `'PlateFiberSection'`, a `'ElasticMembranePlateSection'` and a `'LayeredShell'` section |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ShellNLDKGT)
