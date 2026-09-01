<!-- chunk_id: ElasticTubularJoint_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElasticTubularJoint.html",
 "title": "4.2.4.2. ElasticTubularJoint Element",
 "category": "element",
 "command": "ElasticTubularJoint",
 "doc_section": "src",
 "rel_path": "src/ElasticTubularJoint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1440,
 "word_count": 131,
 "has_code": false,
 "has_table": true
} -->

## 4.2.4.2. ElasticTubularJoint Element

This command is used to construct an ElasticTubularJoint element object, which models joint flexibility of tubular joints in two dimensional analysis of any structure having tubular joints.

**element(*'ElasticTubularJoint'*, *eleTag*, **eleNodes*, *Brace_Diameter*, *Brace_Angle*, *E*, *Chord_Diameter*, *Chord_Thickness*, *Chord_Angle*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `Brace_Diameter` ([float](https://docs.python.org/3/library/functions.html#float)) | outer diameter of brace |
| `Brace_Angle` ([float](https://docs.python.org/3/library/functions.html#float)) | angle between brace and chord axis 0 < Brace_Angle < 90 |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | Young’s Modulus |
| `Chord_Diameter` ([float](https://docs.python.org/3/library/functions.html#float)) | outer diameter of chord |
| `Chord_Thickness` ([float](https://docs.python.org/3/library/functions.html#float)) | thickness of chord |
| `Chord_Angle` ([float](https://docs.python.org/3/library/functions.html#float)) | angle between chord axis and global x-axis 0 < Chord_Angle < 180 |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ElasticTubularJoint_Element)
