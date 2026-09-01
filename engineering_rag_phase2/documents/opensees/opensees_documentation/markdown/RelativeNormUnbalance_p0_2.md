<!-- chunk_id: RelativeNormUnbalance_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/RelativeNormUnbalance.html",
 "title": "3.2.4.4. Relative Norm Unbalance",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "RelativeNormUnbalance",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/RelativeNormUnbalance.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2291,
 "word_count": 380,
 "has_code": true,
 "has_table": true
} -->

## 3.2.4.4. Relative Norm Unbalance

This command is used to construct a convergence test which uses the norms of the right hand side of the matrix equation, i.e. \(b\) vector in \(Ax=b\), to determine if convergence has been reached. It uses the ratio of the current norm to the first norm, i.e. :math:`frac{sqrt({b_i}^T{b_i})}{sqrt({b_1}^T{b_1})}. What the right-hand-side of the matrix equation is depends on integrator and constraint handler chosen. Usually, though not always, it is equal to the unbalanced forces in the system. The command to create a RelativeNormUnbalance test is the following:

**test RelativeNormUnbalance $tol $iter <$pFlag> <$nType>**

| Argument | Type | Description |
| --- | --- | --- |
| $tol | *float* | the tolerance criteria used to check for convergence |
| $iter | *integer* | the max number of iterations to check before returning failure condition |
| $pFlag | *integer* | print flag (optional: default is 0) valid options: 0 print nothing 1 print information on norms each time test() is invoked 2 print information on norms and number of iterations at end of successful test 4 at each step it will print the norms and also the <math>Delta U</math> and <math>R(U)</math> vectors. 5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCCESSFUL test. |
| $nType | *integer* | type of norm (optional: default is 2 (0 = max-norm 1 = 1-norm 2 = 2-norm …)) |

Note

The convergence test compares the current norm of the unbalance with the norm of the first step to determine if convergence has been achieved. As a consequence it will always take at least two steps to achieve convergence.

If numerically the solution has a very small unbalance at the first step, this may mean that the test may never indicate success even though the solution had indeed converged to a solution. This is because machine precision and numerical round-off limit how small the unbalance can become.

Example:

The following examples demonstrate the command to create a RelativeNormUnbalance test which allows 10 iterations till failure with a 2-norm in the \(b\) vector, i.e. \(\sqrt(b^T b)\) of **1.0e-2**.

1. **Tcl Code**

```
test RelativeNormUnbalance 1.0e-2  10 2
```

1. **Python Code**

```
test('RelativeNormUnbalance', 1.0e-2, 10, 2)
```

Code Developed by: **fmk**
