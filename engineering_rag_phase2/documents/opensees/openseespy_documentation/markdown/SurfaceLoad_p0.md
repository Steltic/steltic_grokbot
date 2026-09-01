<!-- chunk_id: SurfaceLoad_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SurfaceLoad.html",
 "title": "4.2.16.1. SurfaceLoad Element",
 "category": "element",
 "command": "SurfaceLoad",
 "doc_section": "src",
 "rel_path": "src/SurfaceLoad.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1375,
 "word_count": 173,
 "has_code": false,
 "has_table": true
} -->

## 4.2.16.1. SurfaceLoad Element

This command is used to construct a SurfaceLoad element object.

**element(*'SurfaceLoad'*, *eleTag*, **eleNodes*, *p*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | the four nodes defining the element, input in counterclockwise order (-ndm 3 -ndf 3) |
| `p` ([float](https://docs.python.org/3/library/functions.html#float)) | applied pressure loading normal to the surface, outward is positive, inward is negative |

The SurfaceLoad element is a four-node element which can be used to apply surface pressure loading to 3D brick elements. The SurfaceLoad element applies energetically-conjugate forces corresponding to the input scalar pressure to the nodes associated with the element. As these nodes are shared with a 3D brick element, the appropriate nodal loads are therefore applied to the brick.

Note

1. There are no valid ElementalRecorder queries for the SurfaceLoad element. Its sole purpose is to apply nodal forces to the adjacent brick element.
2. The pressure loading from the SurfaceLoad element can be applied in a load pattern. See the analysis example below.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/SurfaceLoad_Element)
