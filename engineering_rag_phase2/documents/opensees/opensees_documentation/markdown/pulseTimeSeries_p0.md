<!-- chunk_id: pulseTimeSeries_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/pulseTimeSeries.html",
 "title": "3.1.11.7. Pulse TimeSeries",
 "category": "command_manual",
 "manual_group": "model",
 "command": "pulseTimeSeries",
 "doc_section": "user/manual/model/timeseries",
 "rel_path": "user/manual/model/timeseries/pulseTimeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1226,
 "word_count": 216,
 "has_code": true,
 "has_table": true
} -->

## 3.1.11.7. Pulse TimeSeries

This command is used to construct a TimeSeries object in which the load factor is some pulse function of the time in the domain.

Fig. 3.1.11.6 Pulse Time Series

**timeSeries Pulse $tag $tStart $tFinish $period <-width $pulseWidth> <-shift $shift> <-factor $cFactor>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among TimeSeries objects |
| $tStart | *float* | starting time of non-zero load factor |
| $tEnd | *float* | ending time of non-zero load factor |
| $period | *float* | characteristic period of pulse |
| $pulseWidth | *float* | pulse width as a fraction of the period (optional: default = 0.5) |
| $shift | *float* | phase shift in seconds (optional: default = 0.0) |
| $cFactor | *float* | the load amplification factor (optional: default = 1.0) |

Example:

The following code demonstrates how user would create a trigonemtric time series with a tag of **1**, has a start time of **0.0**, an end time of **10.0**, a period of **1.0**, and a max load factor of **2.0**.

1. **Tcl Code**

```
timeSeries Pulse 1 0.0 10.0 1.0 -factor 2.0
```

1. **Python Code**

```
timSeries('Pulse',  1, 0.0, 10.0, 1.0, '-factor', 2.0)
```

Code Developed by: **Andreas Schellenberg**
