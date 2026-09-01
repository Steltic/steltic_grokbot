<!-- chunk_id: fixedNumIter_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/fixedNumIter.html",
 "title": "5.4.8. FixedNumIter",
 "category": "general",
 "command": "fixedNumIter",
 "doc_section": "src",
 "rel_path": "src/fixedNumIter.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1010,
 "word_count": 138,
 "has_code": false,
 "has_table": true
} -->

## 5.4.8. FixedNumIter

**test(*'FixedNumIter'*, *iter*, *pFlag=0*, *nType=2*)**

Create a FixedNumIter test, that performs a fixed number of iterations without testing for convergence.

| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance criteria used to check for convergence. |
| --- | --- |
| `iter` ([int](https://docs.python.org/3/library/functions.html#int)) | Max number of iterations to check |
| `pFlag` ([int](https://docs.python.org/3/library/functions.html#int)) | Print flag (optional): 0 print nothing. 1 print information on norms each time `test()` is invoked. 2 print information on norms and number of iterations at end of successful test. 4 at each step it will print the norms and also the \(\Delta U\) and \(R(U)\) vectors. 5 if it fails to converge at end of `numIter` it will print an error message **but return a successfull test**. |
| `nType` ([int](https://docs.python.org/3/library/functions.html#int)) | Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional) |
