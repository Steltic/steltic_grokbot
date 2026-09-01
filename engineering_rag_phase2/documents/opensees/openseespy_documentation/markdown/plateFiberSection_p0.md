<!-- chunk_id: plateFiberSection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/plateFiberSection.html",
 "title": "4.16.12. Plate Fiber Section",
 "category": "section",
 "command": "plateFiberSection",
 "doc_section": "src",
 "rel_path": "src/plateFiberSection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 593,
 "word_count": 68,
 "has_code": false,
 "has_table": true
} -->

## 4.16.12. Plate Fiber Section

**section(*'PlateFiber'*, *secTag*, *matTag*, *h*)**

This command allows the user to construct a MembranePlateFiberSection object, which is a section that numerically integrates through the plate thickness with “fibers” and is appropriate for plate and shell analysis.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | nDMaterial tag to be assigned to each fiber |
| `h` ([float](https://docs.python.org/3/library/functions.html#float)) | plate thickness |
