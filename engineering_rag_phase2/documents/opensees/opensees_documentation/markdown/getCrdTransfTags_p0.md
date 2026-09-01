<!-- chunk_id: getCrdTransfTags_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/getCrdTransfTags.html",
 "title": "3.4.6. getCrdTransfTags Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "getCrdTransfTags",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/getCrdTransfTags.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1569,
 "word_count": 166,
 "has_code": true,
 "has_table": false
} -->

## 3.4.6. getCrdTransfTags Command

This command returns a list of all defined coordinate transformation object tags

**getCrdTransfTags()**

Example:

The following example is used to set the variable **currentTime** to current state of **time** in the **Domain**

1. **Tcl Code** (note use of **set** and **[ ]**)

This example creates a set of **geomTransf** objects and the asks for a list of all the created objects using the
command **getCrdTransfTags** and assigning the list to the variable called **allCrdTransfTags**, then prints them.

```
model BasicBuilder -ndm 3 -ndf 6

geomTransf Linear 1        0                -1               0                -jntOffset 100              0                0                -0               -0               -0
geomTransf Linear 2        0                -1               0                -jntOffset 0                0                0                -0               -0               -0
geomTransf Linear 3        0                -1               0                -jntOffset 0                0                0                -0               -0               -0
geomTransf Linear 4        0                -1               0                -jntOffset 0                0                0                -0               -0               -0
geomTransf Linear 5        0                -1               0                -jntOffset 0                0                0                -0               -0               -0

set allCrdTransfTags [getCrdTransfTags]

puts $allCrdTransfTags
```

1. **Python Code**

```
# missing
```

Code developed by: **fmk**
