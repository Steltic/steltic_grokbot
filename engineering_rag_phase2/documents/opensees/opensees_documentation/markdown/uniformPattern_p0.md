<!-- chunk_id: uniformPattern_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniformPattern.html",
 "title": "Uniform Excitation Pattern",
 "category": "command_manual",
 "manual_group": "model",
 "command": "uniformPattern",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/uniformPattern.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1378,
 "word_count": 222,
 "has_code": true,
 "has_table": true
} -->

## Uniform Excitation Pattern

This command allows the user to construct a LoadPattern object. Each plain load pattern is associated with a TimeSeries object and can contain multiple NodalLoads, ElementalLoads and SP_Constraint objects.

**pattern Plain $patternTag $tsTag <-fact $cFactor> {load commands}**

| Argument | Type | Description |
| --- | --- | --- |
| $patternTag | *integer* | unique tag among load patterns |
| $tsTag | *integer* | the tag of the time series to be used in the load pattern |
| $cFactor | *float* | constant factor (optional: default=1.0) |

Warning

Tcl and Python differ here. In the Tcl interpreter the commands to create loads and constraints come in the squirrelly brackets after the command. In python, any load or constraints defined after a pattern are added to that pattern. This is as shown in following example.

Example:

The following example demonstrates how to create a **Linear** time series, and associate it with a **Plain** load pattern which contains **nodal loads** to be applied to nodes **3** and **4** of reference magnitude **(0,-50)** and **(50.0, -100)** respectively.

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
