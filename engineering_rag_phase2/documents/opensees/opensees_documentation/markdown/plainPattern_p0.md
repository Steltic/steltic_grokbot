<!-- chunk_id: plainPattern_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/plainPattern.html",
 "title": "3.1.7.1. Plain Pattern",
 "category": "command_manual",
 "manual_group": "model",
 "command": "plainPattern",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/plainPattern.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2167,
 "word_count": 296,
 "has_code": true,
 "has_table": true
} -->

## 3.1.7.1. Plain Pattern

This command allows the user to construct a LoadPattern object. Each plain load pattern is associated with a TimeSeries object and can contain multiple NodalLoads, ElementalLoads and SP_Constraint objects.

**pattern Plain $patternTag $tsTag <-fact $cFactor> {load commands}**

| Argument | Type | Description |
| --- | --- | --- |
| $patternTag | *integer* | unique tag among load patterns |
| $tsTag | *integer* | the tag of the time series to be used in the load pattern |
| $cFactor | *float* | constant factor (optional: default=1.0) |

- [3.1.7.1.1. load Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/load.html)
- [3.1.7.1.2. eleLoad Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/eleLoad.html)
- [3.1.7.1.3. sp Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/sp.html)

Note

The loads (element, nodal, constraints) in a Plain Load pattern are **reference** loads. The actual load applied to a node or element is the product of the **$cFactor**, the reference load, and a **load factor**. The **load factor**, which is obtained from the associated [Time Series Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeSeries.html#timeseries) is a function of the **time** in the domain and the time series object.

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
