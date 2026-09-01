<!-- chunk_id: 20NodeBrick_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/20NodeBrick.html",
 "title": "4.2.9.3. Twenty Node Brick Element",
 "category": "element",
 "command": "20NodeBrick",
 "doc_section": "src",
 "rel_path": "src/20NodeBrick.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1531,
 "word_count": 174,
 "has_code": false,
 "has_table": true
} -->

## 4.2.9.3. Twenty Node Brick Element

The element is used to construct a twenty-node three dimensional element object

**element(*'20NodeBrick'*, *eleTag*, **eleNodes*, *matTag*, *bf1*, *bf2*, *bf3*, *massDen*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of twenty element nodes, input order is shown in notes below |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with previsouly-defined NDMaterial object |
| `bf1` `bf2` `bf3` ([float](https://docs.python.org/3/library/functions.html#float)) | body force in the direction of global coordinates x, y and z |
| `massDen` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density (mass/volume) |

Note

The valid queries to a 20NodeBrick element when creating an ElementRecorder object are ‘force,’ ‘stiffness,’ stress’, ‘gausspoint’ or ‘plastic’. The output is given as follows:

1. ‘stress’

  the six stress components from each Gauss points are output by the order: sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_xz,sigma_yz
2. ‘gausspoint’

  the coordinates of all Gauss points are printed out
3. ‘plastic’

  the equivalent deviatoric plastic strain from each Gauss point is output in the same order as the coordinates are printed

See also

[Notes](http://opensees.berkeley.edu/OpenSees/manuals/usermanual/734.htm)
