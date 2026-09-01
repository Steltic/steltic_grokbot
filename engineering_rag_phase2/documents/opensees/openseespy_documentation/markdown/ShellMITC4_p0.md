<!-- chunk_id: ShellMITC4_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ShellMITC4.html",
 "title": "4.2.7.2. Shell Element",
 "category": "element",
 "command": "ShellMITC4",
 "doc_section": "src",
 "rel_path": "src/ShellMITC4.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1246,
 "word_count": 143,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.2. Shell Element

This command is used to construct a ShellMITC4 element object, which uses a bilinear isoparametric formulation in combination with a modified shear interpolation to improve thin-plate bending performance.

**element(*'ShellMITC4'*, *eleTag*, **eleNodes*, *secTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes in counter-clockwise order |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined SectionForceDeformation object. Currently must be either a `'PlateFiberSection'`, or `'ElasticMembranePlateSection'` |

Note

1. The valid queries to a Quad element when creating an ElementRecorder object are ‘forces’, ‘stresses,’ and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.
2. It is a 3D element with 6 dofs and CAN NOT be used in 2D domain.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Shell_Element)
