<!-- chunk_id: trigTimeSeries_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/trigTimeSeries.html",
 "title": "3.1.6.3. Trig TimeSeries",
 "category": "command_manual",
 "manual_group": "model",
 "command": "trigTimeSeries",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/trigTimeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1313,
 "word_count": 214,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.3. Trig TimeSeries

This command is used to construct a TimeSeries object in which the load factor is some trigonometric function of the time in the domain \(\lambda = f(t) = \begin{cases}
\text{cFactor} * sin (\frac{2.0 \Pi (t-tStart)}{\text{period}} + \text{shift}), &\text{tStart} <= t <= \text{tFinish}\\
\text{0.0}, &\text{otherwise}\\
\end{cases}\)

Fig. 3.1.6.3 Trigonometric Time Series

**timeSeries Trig $tag $tStart $tEnd $period <-factor $cFactor> <-shift $shift>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among TimeSeries objects. |
| $tStart | *float* | starting time of non-zero load factor |
| $tFinish | *float* | ending time of non-zero load factor |
| $period | *float* | characteristic period of sine wave |
| $shift | *float* | phase shift in radians (optional: default=0.0) |
| $cFactor | *float* | the load factor amplification factor (optional: default=1.0) |

Example:

The following code demonstrates how user would create a trigonometric time series with a tag of **1**, has a start time of **0.0**, an end time of **10.0**, a period of **1.0**, and a max load factor of **2.0**.

1. **Tcl Code**

```
timeSeries Trig 1 0.0 10.0 1.0 -factor 2.0
```

1. **Python Code**

```
timSeries('Trig',  1, 0.0, 10.0, 1.0, '-factor', 2.0)
```

Code Developed by: **fmk**
