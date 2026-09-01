<!-- chunk_id: pfemTest_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pfemTest.html",
 "title": "8.5. PFEM test",
 "category": "general",
 "command": "pfemTest",
 "doc_section": "src",
 "rel_path": "src/pfemTest.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1733,
 "word_count": 198,
 "has_code": false,
 "has_table": true
} -->

## 8.5. PFEM test

**test(*'PFEM'*, *tolv*, *tolp*, *tolrv*, *tolrp*, *tolrelv*, *tolrelp*, *iter*, *maxincr*, *pFlag=0*, *nType=2*)**

Create a PFEM test, which check both increments and residual for
velocities and pressures.

| `tolv` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for velocity increments |
| --- | --- |
| `tolp` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for pressure increments |
| `tolrv` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for velocity residual |
| `tolrp` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for pressure residual |
| `tolrv` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for relative velocity increments |
| `tolrp` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for relative pressure increments |
| `iter` ([int](https://docs.python.org/3/library/functions.html#int)) | Max number of iterations to check |
| `maxincr` ([int](https://docs.python.org/3/library/functions.html#int)) | Max times for error increasing |
| `pFlag` ([int](https://docs.python.org/3/library/functions.html#int)) | Print flag (optional): 0 print nothing. 1 print information on norms each time `test()` is invoked. 2 print information on norms and number of iterations at end of successful test. 4 at each step it will print the norms and also the \(\Delta U\) and \(R(U)\) vectors. 5 if it fails to converge at end of `numIter` it will print an error message **but return a successfull test**. |
| `nType` ([int](https://docs.python.org/3/library/functions.html#int)) | Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional) |
