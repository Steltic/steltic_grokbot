<!-- chunk_id: pulseTs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pulseTs.html",
 "title": "4.7.6. Pulse TimeSeries",
 "category": "time_series",
 "command": "pulseTs",
 "doc_section": "src",
 "rel_path": "src/pulseTs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1465,
 "word_count": 145,
 "has_code": false,
 "has_table": true
} -->

## 4.7.6. Pulse TimeSeries

**timeSeries(*'Pulse'*, *tag*, *tStart*, *tEnd*, *period*, *'-width'*, *width=0.5*, *'-shift'*, *shift=0.0*, *'-factor'*, *factor=1.0*, *'-zeroShift'*, *zeroShift=0.0*)**

This command is used to construct a TimeSeries object in which the load factor is some pulse function of the time in the domain.

\[\begin{split}\lambda = f(t) =
\begin{cases}
    cFactor+zeroShift, &  k < width\\
    zeroshift, & k < 1\\
    0.0, & otherwise
\end{cases}\end{split}\]

\[k = \frac{t+shift-tStart}{period}-floor(\frac{t+shift-tStart}{period})\]

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among TimeSeries objects. |
| --- | --- |
| `tStart` ([float](https://docs.python.org/3/library/functions.html#float)) | Starting time of non-zero load factor. |
| `tEnd` ([float](https://docs.python.org/3/library/functions.html#float)) | Ending time of non-zero load factor. |
| `period` ([float](https://docs.python.org/3/library/functions.html#float)) | Characteristic period of pulse. |
| `width` ([float](https://docs.python.org/3/library/functions.html#float)) | Pulse width as a fraction of the period. (optinal) |
| `shift` ([float](https://docs.python.org/3/library/functions.html#float)) | Phase shift in seconds. (optional) |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | Load factor. (optional) |
| `zeroShift` ([float](https://docs.python.org/3/library/functions.html#float)) | Zero shift. (optional) |
