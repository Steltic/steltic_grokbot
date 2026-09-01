<!-- chunk_id: newtonLineSearch_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/newtonLineSearch.html",
 "title": "5.5.3. Newton with Line Search",
 "category": "general",
 "command": "newtonLineSearch",
 "doc_section": "src",
 "rel_path": "src/newtonLineSearch.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1303,
 "word_count": 117,
 "has_code": false,
 "has_table": true
} -->

## 5.5.3. Newton with Line Search

**algorithm(*'NewtonLineSearch'*, *Bisection=False*, *Secant=False*, *RegulaFalsi=False*, *InitialInterpolated=False*, *tol=0.8*, *maxIter=10*, *minEta=0.1*, *maxEta=10.0*)**

Create a NewtonLineSearch algorithm. Introduces line search to the Newton algorithm to solve the nonlinear residual equation.

| `Bisection` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to use Bisection line search. (optional) |
| --- | --- |
| `Secant` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to use Secant line search. (optional) |
| `RegulaFalsi` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to use RegulaFalsi line search. (optional) |
| `InitialInterpolated` ([bool](https://docs.python.org/3/library/functions.html#bool)) | Flag to use InitialInterpolated line search.(optional) |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for search. (optional) |
| `maxIter` ([float](https://docs.python.org/3/library/functions.html#float)) | Max num of iterations to try. (optional) |
| `minEta` ([float](https://docs.python.org/3/library/functions.html#float)) | Min \(\eta\) value. (optional) |
| `maxEta` ([float](https://docs.python.org/3/library/functions.html#float)) | Max \(\eta\) value. (optional) |
