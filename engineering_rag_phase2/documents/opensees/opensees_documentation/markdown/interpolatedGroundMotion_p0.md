<!-- chunk_id: interpolatedGroundMotion_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/interpolatedGroundMotion.html",
 "title": "Interpolated Ground Motion",
 "category": "command_manual",
 "manual_group": "model",
 "command": "interpolatedGroundMotion",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/interpolatedGroundMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 577,
 "word_count": 99,
 "has_code": false,
 "has_table": true
} -->

## Interpolated Ground Motion

This command is used to construct an interpolated GroundMotion object, where the motion is determined by combining several previously defined ground motions in the load pattern. The command is as follows:

**`groundMotion $tag Interpolated $gmTag1 $gmTag2 ... -fact $fact1 $fact2 ...`**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among ground motions in load pattern |
| $gmTags | *list integer* | the tags of existing ground motions in pattern to be used for interpolation. |
| $factors | *list float* | the interpolation factors. |
