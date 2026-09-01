<!-- chunk_id: fiber_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/fiber.html",
 "title": "4.16.2.1. Fiber Command",
 "category": "general",
 "command": "fiber",
 "doc_section": "src",
 "rel_path": "src/fiber.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 779,
 "word_count": 93,
 "has_code": false,
 "has_table": true
} -->

## 4.16.2.1. Fiber Command

**fiber(*yloc*, *zloc*, *A*, *matTag*)**

This command allows the user to construct a single fiber and add it to the enclosing FiberSection or NDFiberSection.

| `yloc` ([float](https://docs.python.org/3/library/functions.html#float)) | y coordinate of the fiber in the section (local coordinate system) |
| --- | --- |
| `zloc` ([float](https://docs.python.org/3/library/functions.html#float)) | z coordinate of the fiber in the section (local coordinate system) |
| `A` ([float](https://docs.python.org/3/library/functions.html#float)) | cross-sectional area of fiber |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection). |
