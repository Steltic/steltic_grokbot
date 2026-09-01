<!-- chunk_id: trigTs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/trigTs.html",
 "title": "4.7.3. Trigonometric TimeSeries",
 "category": "time_series",
 "command": "trigTs",
 "doc_section": "src",
 "rel_path": "src/trigTs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1386,
 "word_count": 130,
 "has_code": false,
 "has_table": true
} -->

## 4.7.3. Trigonometric TimeSeries

**timeSeries(*'Trig'*, *tag*, *tStart*, *tEnd*, *period*, *'-factor'*, *factor=1.0*, *'-shift'*, *shift=0.0*, *'-zeroShift'*, *zeroShift=0.0*)**

This command is used to construct a TimeSeries object in which the load factor is some trigonemtric function of the time in the domain

\[ \begin{align}\begin{aligned}\begin{split}\lambda = f(t) =
\begin{cases}
    cFactor * sin(\frac{2.0\pi(t-tStart)}{period}+\phi), &  tStart<=t<=tEnd\\
    0.0, & otherwise
\end{cases}\end{split}\\\phi = shift - \frac{period}{2.0\pi} * \arcsin(\frac{zeroShift}{cFactor})\end{aligned}\end{align} \]

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among TimeSeries objects. |
| --- | --- |
| `tStart` ([float](https://docs.python.org/3/library/functions.html#float)) | Starting time of non-zero load factor. |
| `tEnd` ([float](https://docs.python.org/3/library/functions.html#float)) | Ending time of non-zero load factor. |
| `period` ([float](https://docs.python.org/3/library/functions.html#float)) | Characteristic period of sine wave. |
| `shift` ([float](https://docs.python.org/3/library/functions.html#float)) | Phase shift in radians. (optional) |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | Load factor. (optional) |
| `zeroShift` ([float](https://docs.python.org/3/library/functions.html#float)) | Zero shift. (optional) |
