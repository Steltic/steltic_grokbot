<!-- chunk_id: NormEnergyIncr_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/NormEnergyIncr.html",
 "title": "3.2.4.3. Energy Increment",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "NormEnergyIncr",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/NormEnergyIncr.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1803,
 "word_count": 299,
 "has_code": true,
 "has_table": true
} -->

## 3.2.4.3. Energy Increment

This command is used to construct a convergence test which uses the energy increment, \(0.5 (x^T b)\), where the two vector come from the matrix equation \(Ax=b\), to determine if convergence has been reached. What the right-hand-side of the matrix equation is depends on integrator and constraint handler chosen. Usually, though not always, \(x\) is equal to the incremental displacement and \(b\) the unbalanced force. The command to create a NormEnergyIncr test is the following:

**test EnergyIncr $tol $iter <$pFlag>**

| Argument | Type | Description |
| --- | --- | --- |
| $tol | *float* | the tolerance criteria used to check for convergence |
| $iter | *integer* | the max number of iterations to check before returning failure condition |
| $pFlag | *integer* | print flag (optional: default is 0) valid options: 0 print nothing 1 print information on norms each time test() is invoked 2 print information on norms and number of iterations at end of successful test 4 at each step it will print the norms and also the <math>Delta U</math> and <math>R(U)</math> vectors. 5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCCESSFUL test. |

Note

When using a penalty constraint handler, large forces (those necessary to enforce the constraint) are included in the \(x\) vector. Even for very small changes in the displacement, if user has selected overly large penalty factor, large forces can appear in the \(x\) vector.

Example:

The following examples demonstrate the command to create a NormEnergyIncr test which allows 10 iterations till failure with an energy increment \(0.5 (x^T b)\) of **1.0e-2**.

1. **Tcl Code**

```
test EnergyIncr 1.0e-2  10 2
```

1. **Python Code**

```
test('EnergyIncr', 1.0e-2, 10, 2)
```

Code Developed by: **fmk**
