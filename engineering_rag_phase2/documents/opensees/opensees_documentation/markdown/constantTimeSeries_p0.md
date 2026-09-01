<!-- chunk_id: constantTimeSeries_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/constantTimeSeries.html",
 "title": "3.1.6.1. Constant TimeSeries",
 "category": "command_manual",
 "manual_group": "model",
 "command": "constantTimeSeries",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/constantTimeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 853,
 "word_count": 139,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.1. Constant TimeSeries

This command is used to construct a TimeSeries object in which the load factor applied remains constant and is independent of the time in the domain, i.e. \(\lambda = f(t) = C\).

Fig. 3.1.6.1 Constant Time Series

**timeSeries Constant $tag <-factor $cFactor>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among TimeSeries objects. |
| $cFactor | *float* | the load factor applied (optional: default=1.0) |

Example:

The following code demonstrates how user would create two constant time series, the first with tag **1** has a **1.0** factor, the second **2** has a constant load factr of **10.0**.

1. **Tcl Code**

```
timeSeries Constant 1
timeSeries Constant 2 -factor 10.0
```

1. **Python Code**

```
timSeries('Constant',  1)
timSeries('Constant',  2, '-factor', 10.0)
```

Code Developed by: **fmk**
