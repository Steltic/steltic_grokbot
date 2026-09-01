<!-- chunk_id: uniformExcitation_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/uniformExcitation.html",
 "title": "4.8.2. UniformExcitation Pattern",
 "category": "pattern",
 "command": "uniformExcitation",
 "doc_section": "src",
 "rel_path": "src/uniformExcitation.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1790,
 "word_count": 213,
 "has_code": false,
 "has_table": true
} -->

## 4.8.2. UniformExcitation Pattern

**pattern(*'UniformExcitation'*, *patternTag*, *dir*, *'-disp'*, *dispSeriesTag*, *'-vel'*, *velSeriesTag*, *'-accel'*, *accelSeriesTag*, *'-vel0'*, *vel0*, *'-fact'*, *fact*)**

The UniformExcitation pattern allows the user to apply a uniform excitation to a model acting in a certain direction. The command is as follows:

| `patternTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among load patterns |
| --- | --- |
| `dir` ([int](https://docs.python.org/3/library/functions.html#int)) | direction in which ground motion acts corresponds to translation along the global X axis corresponds to translation along the global Y axis corresponds to translation along the global Z axis corresponds to rotation about the global X axis corresponds to rotation about the global Y axis corresponds to rotation about the global Z axis |
| `dispSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the TimeSeries series defining the displacement history. (optional) |
| `velSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the TimeSeries series defining the velocity history. (optional) |
| `accelSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the TimeSeries series defining the acceleration history. (optional) |
| `vel0` ([float](https://docs.python.org/3/library/functions.html#float)) | the initial velocity (optional, default=0.0) |
| `fact` ([float](https://docs.python.org/3/library/functions.html#float)) | constant factor (optional, default=1.0) |

Note

1. The responses obtained from the nodes for this type of excitation are RELATIVE values, and not the absolute values obtained from a multi-support case.
2. must set one of the disp, vel or accel time series
