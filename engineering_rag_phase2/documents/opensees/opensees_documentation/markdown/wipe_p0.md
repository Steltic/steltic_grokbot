<!-- chunk_id: wipe_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/wipe.html",
 "title": "3.4.9. wipe Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "wipe",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/wipe.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 735,
 "word_count": 121,
 "has_code": true,
 "has_table": false
} -->

## 3.4.9. wipe Command

This command is used to clear the domain objects, the recorders, and any analysis objects. It resets the time in the **Domain** to **0.0**.a

**wipe()**

This command is used to start over without having to exit and restart the interpreter. This is useful for example if you want to subject the model to multiple ground motions or subject different models to the same ground motion! It causes all elements, nodes, constraints, loads to be removed from the domain. In addition it deletes all recorders, analysis objects and all material objects created by the model builder.

Example:

The following demonstrates the use of the wipe command.

1. **Tcl Code**

```
wipe
```

1. **Python Code**

```
wipe()
```

Code Developed by: **fmk**
