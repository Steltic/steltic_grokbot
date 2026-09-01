<!-- chunk_id: printA_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/printA.html",
 "title": "6.26. printA command",
 "category": "general",
 "command": "printA",
 "doc_section": "src",
 "rel_path": "src/printA.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 692,
 "word_count": 101,
 "has_code": false,
 "has_table": true
} -->

## 6.26. printA command

**printA(*'-file'*, *filename*, *'-ret'*)**

print the contents of a FullGeneral system that the integrator creates to the screen or a file if the `'-file'` option is used. If using a static integrator, the resulting matrix is the stiffness matrix. If a transient integrator, it will be some combination of mass and stiffness matrices. The printA command can only be issued after an analyze command.

| `filename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | name of file to which output is sent, by default, print to the screen. (optional) |
| --- | --- |
| `'-ret'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | return the A matrix as a list. (optional) |
