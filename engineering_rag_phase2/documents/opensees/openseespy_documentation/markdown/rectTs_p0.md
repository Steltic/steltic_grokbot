<!-- chunk_id: rectTs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/rectTs.html",
 "title": "4.7.5. Rectangular TimeSeries",
 "category": "time_series",
 "command": "rectTs",
 "doc_section": "src",
 "rel_path": "src/rectTs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 814,
 "word_count": 87,
 "has_code": false,
 "has_table": true
} -->

## 4.7.5. Rectangular TimeSeries

**timeSeries(*'Rectangular'*, *tag*, *tStart*, *tEnd*, *'-factor'*, *factor=1.0*)**

This command is used to construct a TimeSeries object in which the load factor is constant for a specified period and 0 otherwise, i.e.

\[\begin{split}\lambda = f(t) =
\begin{cases}
    cFactor, &  tStart<=t<=tEnd\\
    0.0, & otherwise
\end{cases}\end{split}\]

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among TimeSeries objects. |
| --- | --- |
| `tStart` ([float](https://docs.python.org/3/library/functions.html#float)) | Starting time of non-zero load factor. |
| `tEnd` ([float](https://docs.python.org/3/library/functions.html#float)) | Ending time of non-zero load factor. |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | Load factor. (optional) |
