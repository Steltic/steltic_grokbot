<!-- chunk_id: PFEMElementBubble_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementBubble.html",
 "title": "4.2.15.1. PFEMElementBubble",
 "category": "element",
 "command": "PFEMElementBubble",
 "doc_section": "src",
 "rel_path": "src/PFEMElementBubble.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1389,
 "word_count": 137,
 "has_code": false,
 "has_table": true
} -->

## 4.2.15.1. PFEMElementBubble

**element(*'PFEMElementBubble'*, *eleTag*, **eleNodes*, *rho*, *mu*, *b1*, *b2*, *<b3>*, *<thickness*, *kappa>*)**

Create a PFEM Bubble element, which is a fluid element for FSI analysis.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the element |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list of three or four element nodes, four are required for 3D |
| `nd4` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of node 4 (required for 3D) |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | fluid density |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | fluid viscosity |
| `b1` ([float](https://docs.python.org/3/library/functions.html#float)) | body body acceleration in x direction |
| `b2` ([float](https://docs.python.org/3/library/functions.html#float)) | body body acceleration in y direction |
| `b3` ([float](https://docs.python.org/3/library/functions.html#float)) | body body acceleration in z direction (required for 3D) |
| `thickness` ([float](https://docs.python.org/3/library/functions.html#float)) | element thickness (required for 2D) |
| `kappa` ([float](https://docs.python.org/3/library/functions.html#float)) | fluid bulk modulus (optional) |
