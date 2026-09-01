<!-- chunk_id: wipeAnalysis_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/wipeAnalysis.html",
 "title": "3.4.10. wipeAnalysis Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "wipeAnalysis",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/wipeAnalysis.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1147,
 "word_count": 146,
 "has_code": true,
 "has_table": false
} -->

## 3.4.10. wipeAnalysis Command

The wipeAnalysis command is used to remove all the analysis objects.

**wipeAnalsyis()**

This command is needed for example when the user wishes to switch from a static analysis to a transient analysis, e.g. when switching from the initial gravity load analysis to an analysis of the subsequent response due to earthquake loading.

Warning

- The time in the domain is not reset as in the [wipe Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/wipe.html#wipe).
- The state of the model does not change, i.e. the loads remain active and will change with subsequent analyze commands unless a [loadConst Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/loadConst.html#loadconst) is issued.
- There is NO space between the wipe and Analysis. Putting a space results in domain and recorder objects also being remove, e.g. a [wipe Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/wipe.html#wipe).

Example:

The following demonstrates the use of the wipe command.

1. **Tcl Code**

```
wipeAnalysis
```

1. **Python Code**

```
wipeAnalysis()
```

Code Developed by: **fmk**
