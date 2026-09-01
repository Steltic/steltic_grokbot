<!-- chunk_id: eleResponse_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/eleResponse.html",
 "title": "3.4.5. eleResponse Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "eleResponse",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/eleResponse.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1217,
 "word_count": 167,
 "has_code": true,
 "has_table": true
} -->

## 3.4.5. eleResponse Command

This command is used to obtain state information from the element. The quantities that can be obtained from the element are the same as that whcih can be obtained using the [Element Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/ElementRecorder.html#elementrecorder).

**eleResponse $eleTag $arg1 $arg2 ....**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | *integer* | integer tag identifying element |
| $args | *list* | list of the arguments |

Note

1. The values obtained are for the current state of the element.
2. The arguments are specific to the type of element being used and are the same as those that are used in [Element Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/ElementRecorder.html#elementrecorder).

Example:

Then following code can be used to obtain the current state related to the **forces** and the **material stress** in element **1**, a Truss element.

1. **Tcl Code**

```
set eleForces [eleResponse 1 forces]
set eleMatStress [eleResponse 1 material stress]
```

1. **Python Code**

```
eleForces = eleResponse(1,'forces')
eleMatStress = eleResponse(1, 'material','stress')
```

Code developed by: **fmk**
