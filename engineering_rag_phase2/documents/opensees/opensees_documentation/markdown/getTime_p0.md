<!-- chunk_id: getTime_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/getTime.html",
 "title": "3.4.1. getTime Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "getTime",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/getTime.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 362,
 "word_count": 56,
 "has_code": true,
 "has_table": false
} -->

## 3.4.1. getTime Command

This command returns the current time in the **Domain**.

**getTime()**

Example:

The following example is used to set the variable **currentTime** to current state of **time** in the **Domain**

1. **Tcl Code** (note use of **set** and **[ ]**)

```
set currentTime [getTime]
```

1. **Python Code**

```
currentTime = getTime()
```

Code developed by: **fmk**
