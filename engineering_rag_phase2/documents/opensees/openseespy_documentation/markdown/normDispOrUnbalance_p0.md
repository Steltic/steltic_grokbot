<!-- chunk_id: normDispOrUnbalance_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/normDispOrUnbalance.html",
 "title": "5.4.10. NormDispOrUnbalance",
 "category": "general",
 "command": "normDispOrUnbalance",
 "doc_section": "src",
 "rel_path": "src/normDispOrUnbalance.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1293,
 "word_count": 159,
 "has_code": false,
 "has_table": true
} -->

## 5.4.10. NormDispOrUnbalance

**test(*'NormDispOrUnbalance'*, *tolIncr*, *tolR*, *iter*, *pFlag=0*, *nType=2*, *maxincr=-1*)**

Create a NormDispOrUnbalance test, which check if both
`'NormUnbalance'` and `'normDispIncr'` are converged.

| `tolIncr` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for left hand solution increments |
| --- | --- |
| `tolIncr` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for right hand residual |
| `iter` ([int](https://docs.python.org/3/library/functions.html#int)) | Max number of iterations to check |
| `pFlag` ([int](https://docs.python.org/3/library/functions.html#int)) | Print flag (optional): 0 print nothing. 1 print information on norms each time `test()` is invoked. 2 print information on norms and number of iterations at end of successful test. 4 at each step it will print the norms and also the \(\Delta U\) and \(R(U)\) vectors. 5 if it fails to converge at end of `numIter` it will print an error message **but return a successfull test**. |
| `nType` ([int](https://docs.python.org/3/library/functions.html#int)) | Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional) |
| `maxincr` ([int](https://docs.python.org/3/library/functions.html#int)) | Maximum times of error increasing. (optional) |
