<!-- chunk_id: rccircularsection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/rccircularsection.html",
 "title": "4.16.7. RCCircular Section",
 "category": "section",
 "command": "rccircularsection",
 "doc_section": "src",
 "rel_path": "src/rccircularsection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2127,
 "word_count": 221,
 "has_code": false,
 "has_table": true
} -->

## 4.16.7. RCCircular Section

**section(*'RCCircularSection'*, *secTag*, *coreMatTag*, *coverMatTag*, *steelMatTag*, *d*, *cover_depth*, *Ab*, *NringsCore*, *NringsCover*, *Nwedges*, *Nsteel*, *'-GJ'*, *GJ <or '-torsion'*, *matTag>*)**

This command allows the user to construct an RCCircularSection object, which is an encapsulated fiber representation of a circular reinforced concrete section with core and confined regions of concrete.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `coreMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to each fiber in the core region |
| `coverMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to each fiber in the cover region |
| `steelMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to each reinforcing bar |
| `d` ([float](https://docs.python.org/3/library/functions.html#float)) | section radius |
| `cover_depth` ([float](https://docs.python.org/3/library/functions.html#float)) | cover depth (assumed uniform around perimeter) |
| `Ab` ([float](https://docs.python.org/3/library/functions.html#float)) | area of each reinforcing bar |
| `NringsCore` ([int](https://docs.python.org/3/library/functions.html#int)) | number of fiber rings in the core |
| `NringsCover` ([int](https://docs.python.org/3/library/functions.html#int)) | number of fiber rings in the cover |
| `Nwedges` ([int](https://docs.python.org/3/library/functions.html#int)) | number of fiber wedges for the section |
| `Nsteel` ([int](https://docs.python.org/3/library/functions.html#int)) | number of reinforcing bars |
| `GJ` ([float](https://docs.python.org/3/library/functions.html#float)) | secton torsional stiffness |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to section torsion response |

Note

One of the -GJ or the -torsion inputs is required

For more general reinforced concrete section definitions, use the Fiber Section command.
