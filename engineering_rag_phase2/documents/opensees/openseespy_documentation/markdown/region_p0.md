<!-- chunk_id: region_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/region.html",
 "title": "4.10. region command",
 "category": "general",
 "command": "region",
 "doc_section": "src",
 "rel_path": "src/region.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2556,
 "word_count": 286,
 "has_code": false,
 "has_table": true
} -->

## 4.10. region command

**region(*regTag*, *'-ele'*, **eles*, *'-eleOnly'*, **eles*, *'-eleRange'*, *startEle*, *endEle*, *'-eleOnlyRange'*, *startEle*, *endEle*, *'-node'*, **nodes*, *'-nodeOnly'*, **nodes*, *'-nodeRange'*, *startNode*, *endNode*, *'-nodeOnlyRange'*, *startNode*, *endNode*, *'-rayleigh'*, *alphaM*, *betaK*, *betaKinit*, *betaKcomm*)**

The region command is used to label a group of nodes and elements. This command is also used to assign rayleigh damping parameters to the nodes and elements in this region. The region is specified by either elements or nodes, not both. If elements are defined, the region includes these elements and the all connected nodes, unless the -eleOnly option is used in which case only elements are included. If nodes are specified, the region includes these nodes and all elements of which all nodes are prescribed to be in the region, unless the -nodeOnly option is used in which case only the nodes are included.

| `regTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique integer tag |
| --- | --- |
| `eles` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | tags of selected elements in domain to be included in region (optional) |
| `nodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | tags of selected nodes in domain to be included in region (optional) |
| `startEle` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for start element (optional) |
| `endEle` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for end element (optional) |
| `startNode` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for start node (optional) |
| `endNode` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for end node (optional) |
| `alphaM` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements or nodes mass matrix (optional) |
| `betaK` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements current stiffness matrix (optional) |
| `betaKinit` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements initial stiffness matrix (optional) |
| `betaKcomm` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements committed stiffness matrix (optional) |

Note

The user cannot prescribe the region by BOTH elements and nodes.
