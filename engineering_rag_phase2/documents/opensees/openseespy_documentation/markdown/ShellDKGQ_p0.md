<!-- chunk_id: ShellDKGQ_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ShellDKGQ.html",
 "title": "4.2.7.3. ShellDKGQ",
 "category": "general",
 "command": "ShellDKGQ",
 "doc_section": "src",
 "rel_path": "src/ShellDKGQ.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 861,
 "word_count": 82,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.3. ShellDKGQ

This command is used to construct a ShellDKGQ element object, which is a quadrilateral shell element based on the theory of generalized conforming element.

**element(*'ShellDKGQ'*, *eleTag*, **eleNodes*, *secTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes in counter-clockwise order |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined SectionForceDeformation object. Currently can be a `'PlateFiberSection'`, a `'ElasticMembranePlateSection'` and a `'LayeredShell'` section |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ShellDKGQ)
