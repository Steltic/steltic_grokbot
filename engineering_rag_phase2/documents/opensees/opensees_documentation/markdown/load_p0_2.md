<!-- chunk_id: load_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/load.html",
 "title": "load Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "load",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/load.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 952,
 "word_count": 160,
 "has_code": true,
 "has_table": true
} -->

## load Command

This command is used to construct a NodalLoad object.

**load $nodeTag (ndf $LoadValues)**

The nodal load is added to the LoadPattern being defined in the enclosing scope of the pattern command.

| Argument | Type | Description |
| --- | --- | --- |
| $nodeTag | *integer* | tag of node on which loads act |
| $LoadValues | *list float* | **ndf** load values that are to be applied to the node. |

Example:

The following example demonstrates how to create a **Linear** time series, and asociate it with a **Plain** load pattern which contains **nodal loads** to be applied to nodes **3** and **4** of reference magnitude **(0,-50)** and **(50.0, -100)** respectivily.

1. **Tcl Code**

```
timeSeries Linear 2
pattern Plain 1 2 {
        load  3   0.0  -50.0  0.0
        load  4   50.0  -100.0 0.0
}
```

1. **Python Code**

```
timeSeries("Linear", 2)
pattern("Plain", 1, 2)
load(3, 0.0, -50.0)
load(4, 50.0, -100.0)
```

Code Developed by: **fmk**
