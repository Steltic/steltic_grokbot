<!-- chunk_id: rectangularTimeSeries_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/rectangularTimeSeries.html",
 "title": "3.1.11.6. Rectangular Time Series",
 "category": "command_manual",
 "manual_group": "model",
 "command": "rectangularTimeSeries",
 "doc_section": "user/manual/model/timeseries",
 "rel_path": "user/manual/model/timeseries/rectangularTimeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1166,
 "word_count": 184,
 "has_code": true,
 "has_table": true
} -->

## 3.1.11.6. Rectangular Time Series

This command is used to construct a TimeSeries object in which the load factor is constant for a specified period and 0 otherwise, i.e. \(\lambda = f(t) = \begin{cases} \text{cFactor}, &\text{tStart} <= t <= \text{tFinish}\\
\text{0.0}, &\text{otherwise}\\
\end{cases}\)

**timeSeries Rectangular $tag $tStart $tEnd <-factor $cFactor>**

Fig. 3.1.11.5 Rectangular Time Series

**timeSeries Rectangular $tag $tStart $tFinish $period <-shift $shift> <-factor $cFactor>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among TimeSeries objects. |
| $tStart | *float* | starting time of non-zero load factor |
| $tFinish | *float* | ending time of non-zero load factor |
| $cFactor | *float* | the load factor applied (optional: default=1.0) |

Example:

The following code demonstrates how user would create a trigonometric time series with a tag of **1**, has a start time of **0.0**, an end time of **10.0**, and a max load factor of **2.0**.

1. **Tcl Code**

```
timeSeries Rectangular 1 0.0 10.0 -factor 2.0
```

1. **Python Code**

```
timSeries('Rectangular',  1, 0.0, 10.0, '-factor', 2.0)
```

Code Developed by: **fmk**
