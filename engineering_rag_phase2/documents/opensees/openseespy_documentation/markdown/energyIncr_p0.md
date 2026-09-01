<!-- chunk_id: energyIncr_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/energyIncr.html",
 "title": "5.4.3. energyIncr",
 "category": "general",
 "command": "energyIncr",
 "doc_section": "src",
 "rel_path": "src/energyIncr.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1424,
 "word_count": 206,
 "has_code": false,
 "has_table": true
} -->

## 5.4.3. energyIncr

**test(*'EnergyIncr'*, *tol*, *iter*, *pFlag=0*, *nType=2*)**

Create a EnergyIncr test, which uses the dot product of the solution vector and norm of the right hand side of the matrix equation to determine if convergence has been reached.

| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance criteria used to check for convergence. |
| --- | --- |
| `iter` ([int](https://docs.python.org/3/library/functions.html#int)) | Max number of iterations to check |
| `pFlag` ([int](https://docs.python.org/3/library/functions.html#int)) | Print flag (optional): 0 print nothing. 1 print information on norms each time `test()` is invoked. 2 print information on norms and number of iterations at end of successful test. 4 at each step it will print the norms and also the \(\Delta U\) and \(R(U)\) vectors. 5 if it fails to converge at end of `numIter` it will print an error message **but return a successfull test**. |
| `nType` ([int](https://docs.python.org/3/library/functions.html#int)) | Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional) |

- When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).
- When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.
