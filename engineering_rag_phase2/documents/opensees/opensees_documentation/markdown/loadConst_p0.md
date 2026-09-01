<!-- chunk_id: loadConst_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/loadConst.html",
 "title": "3.4.8. loadConst Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "loadConst",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/loadConst.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 817,
 "word_count": 143,
 "has_code": true,
 "has_table": true
} -->

## 3.4.8. loadConst Command

This command is used to set the loads constant in the domain and to also set the time in the domain. When setting the loads constant, the procedure will invoke setLoadConst() on all LoadPattern objects which exist in the domain at the time the command is called.

**loadConst <-time $pseudoTime>**

| Argument | Type | Description |
| --- | --- | --- |
| $pseudoTime | *float* | Time domain is to be set to (optional) |

Note

Load Patterns added afer this command is invoked are not set to constant.

Example:

The following examples demonstrate the command to set the loads constant and to also rest the time to 0.0, which is the most common use of the command.

1. **Tcl Code**

```
loadConst -time 0.0
```

1. **Python Code**

```
loadConst('-time',0.0)
```

Code Developed by: **fmk**

Code Developed by: **fmk**
