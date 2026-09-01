<!-- chunk_id: NormUnbalance_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/NormUnbalance.html",
 "title": "3.2.4.1. Norm Unbalance",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "NormUnbalance",
 "doc_section": "user/manual/analysis/test",
 "rel_path": "user/manual/analysis/test/NormUnbalance.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1897,
 "word_count": 324,
 "has_code": true,
 "has_table": true
} -->

## 3.2.4.1. Norm Unbalance

This command is used to construct a convergence test which uses the norm of the right hand side of the matrix equation, i.e. \(b\) vector in \(Ax=b\), to determine if convergence has been reached. What the right-hand-side of the matrix equation is depends on integrator and constraint handler chosen. Usually, though not always, it is equal to the unbalanced forces in the system. The command to create a NormUnbalance test is the following:

**test NormUnbalance $tol $iter <$pFlag> <$nType>**

| Argument | Type | Description |
| --- | --- | --- |
| $tol | *float* | the tolerance criteria used to check for convergence |
| $iter | *integer* | the max number of iterations to check before returning failure condition |
| $pFlag | *integer* | print flag (optional: default is 0) valid options: 0 print nothing 1 print information on norms each time test() is invoked 2 print information on norms and number of iterations at end of successful test 4 at each step it will print the norms and also the <math>Delta U</math> and <math>R(U)</math> vectors. 5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCCESSFUL test. |
| $nType | *integer* | type of norm (optional: default is 2 (0 = max-norm 1 = 1-norm 2 = 2-norm …)) |

Note

When using a penalty constraint handler, large forces (those necessary to enforce the constraint) are included in the \(b\) vector. Even for very small changes in the displacement, if user has selected overly large penalty factor, large forces can appear in the \(b\) vector.

Example:

The following examples demonstrate the command to create a NormUnbalance test which allows 10 iterations till failure with a 2-norm in the \(b\) vector, i.e. \(\sqrt(b^T b)\) of **1.0e-2**.

1. **Tcl Code**

```
test NormUnbalance 1.0e-2  10 2
```

1. **Python Code**

```
test('NormUnbalance', 1.0e-2, 10, 2)
```

Code Developed by: **fmk**
