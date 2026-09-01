<!-- chunk_id: wfsection2d_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/wfsection2d.html",
 "title": "4.16.5. Wide Flange Section",
 "category": "section",
 "command": "wfsection2d",
 "doc_section": "src",
 "rel_path": "src/wfsection2d.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1176,
 "word_count": 128,
 "has_code": false,
 "has_table": true
} -->

## 4.16.5. Wide Flange Section

**section(*'WFSection2d'*, *secTag*, *matTag*, *d*, *tw*, *bf*, *tf*, *Nfw*, *Nff*)**

This command allows the user to construct a WFSection2d object, which is an encapsulated fiber representation of a wide flange steel section appropriate for plane frame analysis.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxialMaterial assigned to each fiber |
| `d` ([float](https://docs.python.org/3/library/functions.html#float)) | section depth |
| `tw` ([float](https://docs.python.org/3/library/functions.html#float)) | web thickness |
| `bf` ([float](https://docs.python.org/3/library/functions.html#float)) | flange width |
| `tf` ([float](https://docs.python.org/3/library/functions.html#float)) | flange thickness |
| `Nfw` ([float](https://docs.python.org/3/library/functions.html#float)) | number of fibers in the web |
| `Nff` ([float](https://docs.python.org/3/library/functions.html#float)) | number of fibers in each flange |

Note

The section dimensions `d`, `tw`, `bf`, and `tf` can be found in the AISC steel manual.
