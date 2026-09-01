<!-- chunk_id: corotational_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/corotational.html",
 "title": "4.18.3. Corotational Transformation",
 "category": "general",
 "command": "corotational",
 "doc_section": "src",
 "rel_path": "src/corotational.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1800,
 "word_count": 214,
 "has_code": false,
 "has_table": true
} -->

## 4.18.3. Corotational Transformation

**geomTransf(*'Corotational'*, *transfTag*, *'-jntOffset'*, **dI*, **dJ*)**

**geomTransf(*'Corotational'*, *transfTag*, **vecxz*)**

This command is used to construct the Corotational Coordinate Transformation (CorotCrdTransf) object. Corotational transformation can be used in large displacement-small strain problems.

| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying transformation |
| --- | --- |
| `vecxz` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis. These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system. These items need to be specified for the three-dimensional problem. |
| `dI` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | joint offset values – offsets specified with respect to the global coordinate system for element-end node i (the number of arguments depends on the dimensions of the current model). |
| `dJ` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | joint offset values – offsets specified with respect to the global coordinate system for element-end node j (the number of arguments depends on the dimensions of the current model). |

Note

Currently the transformation does not deal with element loads and will ignore any that are applied to the element.
