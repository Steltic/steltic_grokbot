<!-- chunk_id: MPAccTimeSeries_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/MPAccTimeSeries.html",
 "title": "MPAcc TimeSeries",
 "category": "command_manual",
 "manual_group": "model",
 "command": "MPAccTimeSeries",
 "doc_section": "user/manual/model/timeseries",
 "rel_path": "user/manual/model/timeseries/MPAccTimeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1450,
 "word_count": 243,
 "has_code": true,
 "has_table": true
} -->

## MPAcc TimeSeries

This command is used to represent near-field strong ground motion and can simulate the entire set of available near-fault displacement, velocity, and (in many cases) acceleration time histories, as well as the corresponding deformation, velocity, and acceleration response spectra.

MPAcc Time Series

**timeSeries MPAcc $tag $tStart $tEnd $period <-gammaMP $gammaMP> <-nuMP $nuMP> <-AFactor $AFactor>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among TimeSeries objects |
| $tStart | *float* | starting time of non-zero load factor |
| $tEnd | *float* | ending time of non-zero load factor |
| $period | *float* | characteristic period of M&P pulse |
| $gammaMP | *float* | γ factor in M&P pulse model (optional: default = 1.0) |
| $nuMP | *float* | v in degree in M&P pulse model (optional: default = 90.0) |
| $AFactor | *float* | the M&P velocity amplification factor (optional: default = 1.0) |

Example:

The following code demonstrates how user would create a MPAcc time series with a tag of **1**, has a start time of **0.0**, an end time of **10.0**, a period of **5.0**, a gamma of **1.0**,a nuMP of **90**, and the M&P velocity amplification factor of **2.0**.

1. **Tcl Code**

```
timeSeries MPAcc 1 0.0 10.0 5.0 -gammaMP 1.0 -nuMP 90 -AFactor 2.0
```

1. **Python Code**

```
timSeries('MPAcc',  1, 0.0, 10.0, 5.0,'-gammaMP',1.0,'-nuMP',90, '-AFactor', 2.0)
```

Code Developed by: |TangSEU|
