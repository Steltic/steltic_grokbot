<!-- chunk_id: ExpressNewton_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/ExpressNewton.html",
 "title": "3.2.5.9. ExpressNewton Algorithm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "ExpressNewton",
 "doc_section": "user/manual/analysis/algorithm",
 "rel_path": "user/manual/analysis/algorithm/ExpressNewton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2588,
 "word_count": 358,
 "has_code": false,
 "has_table": true
} -->

## 3.2.5.9. ExpressNewton Algorithm

This command is used to construct an ExpressNewton algorithm object for nonlinear structural dynamics. It accepts the solution after a constant number of Newton-Raphson iterations using a constant system Jacobian matrix. It is advised to be combined with transient integrators only. The command is of the following form:

**algorithm ExpressNewton $iter $kMultiplier <-initialTangent> <-currentTangent> <-factorOnce>**

| Argument | Type | Description |
| --- | --- | --- |
| $iter | *integer* | constant number of iterations. Default to 2 |
| $kMultiplier | *float* | multiplier to system stiffness in evaluation of the system Jacobian matrix to support unconditional stability for hardening system. Default to 1.0. Dicussed in Reference [1] |
| -initialTangent | *string* | optional flag to indicate to use initial stiffness in evaluation of the system Jacobian matrix |
| -currentTangent | *string* | optional and default flag to indicate to use current stiffness in evaluation of the system Jacobian matrix |
| -factorOnce | *string* | optional flag to indicate to factorize the system Jacobian matrix only once. It is suggested to specify this flag to maximize the solution efficiency (Reference [1]). If this flag is not specified factorization will be performed on every iteraction. |

The strategy of the ExpressNewton algorithm is to adopt a typical transient integrator and accept the solution after a constant number of iterations using a constant system Jacobian matrix. The algorithm inherits the advantages of the host transient integrators, such as the unconditional stability, the order of accuracy, and the numerical dissipation that helps suppress the spurious high-frequency oscillation. Using a constant Jacobian matrix is vital to minimizing the computational expense associated with matrix operations. The algorithm helps achieve an exponential efficiency improvement in a response history analysis with any transient integrator.

Warning

There is no check on the convergence of the model in this algorithm. It iterates a constant number of iterations and then proceeds to the next time step.

Code Developed by: Yuli Huang

**References**

**1**

> Xu J, Huang Y, Qu Z. 2020. [An efficient and unconditionally stable numerical algorithm for nonlinear structural dynamics](https://www.researchgate.net/publication/342098037_An_efficient_and_unconditionally_stable_numerical_algorithm_for_nonlinear_structural_dynamics). International Journal for Numerical Methods in Engineering, 121(20):4614-29. [https://doi.org/10.1002/nme.6456](https://doi.org/10.1002/nme.6456)
