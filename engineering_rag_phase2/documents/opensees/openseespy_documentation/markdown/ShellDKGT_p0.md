<!-- chunk_id: ShellDKGT_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ShellDKGT.html",
 "title": "4.2.7.4. ShellDKGT",
 "category": "general",
 "command": "ShellDKGT",
 "doc_section": "src",
 "rel_path": "src/ShellDKGT.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 872,
 "word_count": 84,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.4. ShellDKGT

This command is used to construct a ShellDKGT element object, which is a triangular shell element based on the theory of generalized conforming element.

**element(*'ShellDKGT'*, *eleTag*, **eleNodes*, *secTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of three element nodes in clockwise or counter-clockwise order |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined SectionForceDeformation object. currently can be a `'PlateFiberSection'`, a `'ElasticMembranePlateSection'` and a `'LayeredShell'` section |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ShellDKGT)
