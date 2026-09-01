<!-- chunk_id: rcsection2d_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/rcsection2d.html",
 "title": "4.16.6. RC Section",
 "category": "section",
 "command": "rcsection2d",
 "doc_section": "src",
 "rel_path": "src/rcsection2d.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2194,
 "word_count": 237,
 "has_code": false,
 "has_table": true
} -->

## 4.16.6. RC Section

**section(*'RCSection2d'*, *secTag*, *coreMatTag*, *coverMatTag*, *steelMatTag*, *d*, *b*, *cover_depth*, *Atop*, *Abot*, *Aside*, *Nfcore*, *Nfcover*, *Nfs*)**

This command allows the user to construct an RCSection2d object, which is an encapsulated fiber representation of a rectangular reinforced concrete section with core and confined regions of concrete and single top and bottom layers of reinforcement appropriate for plane frame analysis.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `coreMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to each fiber in the core region |
| `coverMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to each fiber in the cover region |
| `steelMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to each reinforcing bar |
| `d` ([float](https://docs.python.org/3/library/functions.html#float)) | section depth |
| `b` ([float](https://docs.python.org/3/library/functions.html#float)) | section width |
| `cover_depth` ([float](https://docs.python.org/3/library/functions.html#float)) | cover depth (assumed uniform around perimeter) |
| `Atop` ([float](https://docs.python.org/3/library/functions.html#float)) | area of reinforcing bars in top layer |
| `Abot` ([float](https://docs.python.org/3/library/functions.html#float)) | area of reinforcing bars in bottom layer |
| `Aside` ([float](https://docs.python.org/3/library/functions.html#float)) | area of reinforcing bars on intermediate layers |
| `Nfcore` ([float](https://docs.python.org/3/library/functions.html#float)) | number of fibers through the core depth |
| `Nfcover` ([float](https://docs.python.org/3/library/functions.html#float)) | number of fibers through the cover depth |
| `Nfs` ([float](https://docs.python.org/3/library/functions.html#float)) | number of bars on the top and bottom rows of reinforcement (Nfs-2 bars will be placed on the side rows) |

Note

For more general reinforced concrete section definitions, use the Fiber Section command.
