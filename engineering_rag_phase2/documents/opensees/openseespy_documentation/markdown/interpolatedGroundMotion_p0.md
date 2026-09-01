<!-- chunk_id: interpolatedGroundMotion_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/interpolatedGroundMotion.html",
 "title": "4.8.3.2. Interpolated Ground Motion",
 "category": "general",
 "command": "interpolatedGroundMotion",
 "doc_section": "src",
 "rel_path": "src/interpolatedGroundMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 789,
 "word_count": 78,
 "has_code": false,
 "has_table": true
} -->

## 4.8.3.2. Interpolated Ground Motion

**groundMotion(*gmTag*, *'Interpolated'*, **gmTags*, *'-fact'*, *facts*)**

This command is used to construct an interpolated GroundMotion object, where the motion is determined by combining several previously defined ground motions in the load pattern.

| `gmTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among ground motions in load pattern |
| --- | --- |
| `gmTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | the tags of existing ground motions in pattern to be used for interpolation |
| `facts` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | the interpolation factors. (optional) |
