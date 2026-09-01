<!-- chunk_id: Corotational_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/geomTransf/Corotational.html",
 "title": "3.1.8.3. Corotational Transformation",
 "category": "command_manual",
 "manual_group": "model",
 "command": "Corotational",
 "doc_section": "user/manual/model/geomTransf",
 "rel_path": "user/manual/model/geomTransf/Corotational.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1866,
 "word_count": 274,
 "has_code": false,
 "has_table": true
} -->

## 3.1.8.3. Corotational Transformation

This command is used to construct the Corotational Coordinate Transformation (CorotCrdTransf) object, which performs an exact geometric transformation of beam stiffness and resisting force from the basic system to the global coordinate system.

- For a two-dimensional problem:

**geomTransf Corotational $transfTag <-jntOffset $dXi $dYi $dXj $dYj>**

- For a three-dimensional problem:

**geomTransf Corotational $transfTag $vecxzX $vecxzY $vecxzZ <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>**

| Argument | Type | Description |
| --- | --- | --- |
| $transfTag | *integer* | integer tag identifying transformation |
| $vecxzX $vecxzY $vecxzZ | *float* | X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis. These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system. These items need to be specified for the three-dimensional problem. |
| $dXi $dYi $dZi | *float* | joint offset values – offsets specified with respect to the global coordinate system for element-end node i (optional, the number of arguments depends on the dimensions of the current model). |
| $dXj $dYj $dZj | *float* | joint offset values – offsets specified with respect to the global coordinate system for element-end node j (optional, the number of arguments depends on the dimensions of the current model). |

Note

The element coordinate system and joint offset values are specified as in the [Linear Transformation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/geomTransf/Linear.html#lineartr).

Code Developed by: Remo Magalhaes de Souza

Images Developed by: [Silvia Mazzoni](https://www.silviasbrainery.com/)
