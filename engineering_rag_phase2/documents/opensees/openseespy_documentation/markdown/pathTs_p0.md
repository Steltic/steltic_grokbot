<!-- chunk_id: pathTs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pathTs.html",
 "title": "4.7.7. Path TimeSeries",
 "category": "time_series",
 "command": "pathTs",
 "doc_section": "src",
 "rel_path": "src/pathTs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2858,
 "word_count": 333,
 "has_code": false,
 "has_table": true
} -->

## 4.7.7. Path TimeSeries

**timeSeries(*'Path'*, *tag*, *'-dt'*, *dt=0.0*, *'-values'*, **values*, *'-time'*, **time*, *'-filePath'*, *filePath=''*, *'-fileTime'*, *fileTime=''*, *'-factor'*, *factor=1.0*, *'-startTime'*, *startTime=0.0*, *'-useLast'*, *'-prependZero'*)**

The relationship between load
factor and time is input by the user as a series of discrete points in
the 2d space (load factor, time). The input points can come from a
file or from a list in the script. When the time specified does not match
any of the input points, linear interpolation is used between points.
There are many ways to specify the load path, for example,
the load factors set with `values` or `filePath`,
and the time set with `dt`, `time`, or `fileTime`.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among TimeSeries objects. |
| --- | --- |
| `dt` ([float](https://docs.python.org/3/library/functions.html#float)) | Time interval between specified points. (optional) |
| `values` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | Load factor values in a ([list](https://docs.python.org/3/library/stdtypes.html#list)). (optional) |
| `time` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | Time values in a ([list](https://docs.python.org/3/library/stdtypes.html#list)). (optional) |
| `filePath` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | File containing the load factors values. (optional) |
| `fileTime` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | File containing the time values for corresponding load factors. (optional) |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | A factor to multiply load factors by. (optional) |
| `startTime` ([float](https://docs.python.org/3/library/functions.html#float)) | Provide a start time for provided load factors. (optional) |
| `'-useLast'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Use last value after the end of the series. (optional) |
| `'-prependZero'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Prepend a zero value to the series of load factors. (optional) |

- Linear interpolation between points.
- If the specified time is beyond last point (AND WATCH FOR NUMERICAL ROUNDOFF), 0.0 is returned. Specify `'-useLast'` to use the last data point instead of 0.0.
- The transient integration methods in OpenSees assume zero initial conditions. So it is important that any timeSeries that is being used in a transient analysis` starts from zero (first data point in the timeSeries = 0.0). To guarantee that this is the case the optional parameter `'-prependZero'` can be specified to prepend a zero value to the provided TimeSeries.
