<!-- chunk_id: triangleTs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/triangleTs.html",
 "title": "4.7.4. Triangular TimeSeries",
 "category": "time_series",
 "command": "triangleTs",
 "doc_section": "src",
 "rel_path": "src/triangleTs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1543,
 "word_count": 143,
 "has_code": false,
 "has_table": true
} -->

## 4.7.4. Triangular TimeSeries

**timeSeries(*'Triangle'*, *tag*, *tStart*, *tEnd*, *period*, *'-factor'*, *factor=1.0*, *'-shift'*, *shift=0.0*, *'-zeroShift'*, *zeroShift=0.0*)**

This command is used to construct a TimeSeries object in which the load factor is some triangular function of the time in the domain.

\[\begin{split}\lambda = f(t) =
\begin{cases}
    slope*k*period+zeroShift, & k < 0.25\\
    cFactor-slope*(k-0.25)*period+zeroShift, & k < 0.75\\
    -cFactor+slope*(k-0.75)*period+zeroShift, & k < 1.0\\
    0.0, & otherwise
\end{cases}\end{split}\]

\[ \begin{align}\begin{aligned}slope = \frac{cFactor}{period/4}\\k = \frac{t+\phi-tStart}{period}-floor(\frac{t+\phi-tStart}{period})\\\phi = shift - \frac{zeroShift}{slope}\end{aligned}\end{align} \]

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among TimeSeries objects. |
| --- | --- |
| `tStart` ([float](https://docs.python.org/3/library/functions.html#float)) | Starting time of non-zero load factor. |
| `tEnd` ([float](https://docs.python.org/3/library/functions.html#float)) | Ending time of non-zero load factor. |
| `period` ([float](https://docs.python.org/3/library/functions.html#float)) | Characteristic period of sine wave. |
| `shift` ([float](https://docs.python.org/3/library/functions.html#float)) | Phase shift in radians. (optional) |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | Load factor. (optional) |
| `zeroShift` ([float](https://docs.python.org/3/library/functions.html#float)) | Zero shift. (optional) |
