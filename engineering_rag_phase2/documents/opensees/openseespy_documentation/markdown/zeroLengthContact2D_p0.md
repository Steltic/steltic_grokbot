<!-- chunk_id: zeroLengthContact2D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthContact2D.html",
 "title": "4.2.1.6. zeroLengthContact Element",
 "category": "element",
 "command": "zeroLengthContact2D",
 "doc_section": "src",
 "rel_path": "src/zeroLengthContact2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2285,
 "word_count": 234,
 "has_code": false,
 "has_table": true
} -->

## 4.2.1.6. zeroLengthContact Element

**element(*'zeroLengthContact2D'*, *eleTag*, **eleNodes*, *Kn*, *Kt*, *mu*, *'-normal'*, *Nx*, *Ny*)**

This command is used to construct a zeroLengthContact2D element, which is Node-to-node frictional contact element used in two dimensional analysis and three dimensional analysis:

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of a constrained and a retained nodes |
| `Kn` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in normal direction |
| `Kt` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in tangential direction |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | friction coefficient |

**element(*'zeroLengthContact3D'*, *eleTag*, **eleNodes*, *Kn*, *Kt*, *mu*, *c*, *dir*)**

This command is used to construct a zeroLengthContact3D element, which is Node-to-node frictional contact element used in two dimensional analysis and three dimensional analysis:

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of a constrained and a retained nodes |
| `Kn` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in normal direction |
| `Kt` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in tangential direction |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | friction coefficient |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | cohesion (not available in 2D) |
| `dir` ([int](https://docs.python.org/3/library/functions.html#int)) | Direction flag of the contact plane (3D), it can be: 1 Out normal of the master plane pointing to +X direction 2 Out normal of the master plane pointing to +Y direction 3 Out normal of the master plane pointing to +Z direction |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContact_Element)
