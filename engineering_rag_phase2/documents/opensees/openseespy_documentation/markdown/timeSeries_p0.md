<!-- chunk_id: timeSeries_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/timeSeries.html",
 "title": "4.7. timeSeries commands",
 "category": "time_series",
 "command": "timeSeries",
 "doc_section": "src",
 "rel_path": "src/timeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1329,
 "word_count": 107,
 "has_code": false,
 "has_table": true
} -->

## 4.7. timeSeries commands

**timeSeries(*tsType*, *tsTag*, **tsArgs*)**

This command is used to construct a TimeSeries object which represents the relationship between the time in the domain, \(t\), and the load factor applied to the loads, \(\lambda\), in the load pattern with which the TimeSeries object is associated, i.e. \(\lambda = F(t)\).

| `tsType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | time series type. |
| --- | --- |
| `tsTag` ([int](https://docs.python.org/3/library/functions.html#int)) | time series tag. |
| `tsArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of time series arguments |

The following contain information about available `tsType`:

1. [Constant TimeSeries](https://openseespydoc.readthedocs.io/en/latest/src/constantTs.html)
2. [Linear TimeSeries](https://openseespydoc.readthedocs.io/en/latest/src/linearTs.html)
3. [Trigonometric TimeSeries](https://openseespydoc.readthedocs.io/en/latest/src/trigTs.html)
4. [Triangular TimeSeries](https://openseespydoc.readthedocs.io/en/latest/src/triangleTs.html)
5. [Rectangular TimeSeries](https://openseespydoc.readthedocs.io/en/latest/src/rectTs.html)
6. [Pulse TimeSeries](https://openseespydoc.readthedocs.io/en/latest/src/pulseTs.html)
7. [Path TimeSeries](https://openseespydoc.readthedocs.io/en/latest/src/pathTs.html)
