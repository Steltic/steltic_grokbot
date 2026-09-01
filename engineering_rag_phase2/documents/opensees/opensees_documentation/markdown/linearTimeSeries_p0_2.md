<!-- chunk_id: linearTimeSeries_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/linearTimeSeries.html",
 "title": "3.1.11.2. Linear TimeSeries",
 "category": "command_manual",
 "manual_group": "model",
 "command": "linearTimeSeries",
 "doc_section": "user/manual/model/timeseries",
 "rel_path": "user/manual/model/timeseries/linearTimeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 831,
 "word_count": 136,
 "has_code": true,
 "has_table": true
} -->

## 3.1.11.2. Linear TimeSeries

This command is used to construct a TimeSeries object in which the load factor applied is linearly proportional to the time in the domain, i.e. \(\lambda = f(t) = cFactor*t\).

Fig. 3.1.11.2 Linear Time Series

**timeSeries Linear $tag <-factor $cFactor>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among TimeSeries objects |
| $cFactor | *float* | the linear factor (optional: default=1.0) |

Example:

The following code demonstrates how user would create two linear time series, the first with tag **1** has a **1.0** factor, the second **2** has a constant load factor of **20.0**.

1. **Tcl Code**

```
timeSeries Linear 1
timeSeries Linear 2 -factor 20.0
```

1. **Python Code**

```
timSeries('Linear',  1)
timSeries('Linear',  2, '-factor', 20.0)
```

Code Developed by: **fmk**
