<!-- chunk_id: Newton_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/Newton.html",
 "title": "OpenSees Documentation Page",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "Newton",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/Newton.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2796,
 "word_count": 425,
 "has_code": true,
 "has_table": true
} -->

## OpenSees Documentation Page

This command is used to construct a NewtonRaphson algorithm object which is uses the Newton-Raphson algorithm to solve the nonlinear residual equation. The Newton-Raphson method is the most widely used and most robust method for solving nonlinear algebraic equations. The command is of the following form:

**algorithm Newton <-initial> <-initialThenCurrent>**

| Argument | Type | Description |
| --- | --- | --- |
| -initial | *string* | optional flag to indicate to use initial stiffness |
| -initialThenCurrent | *string* | optional flag to indicate to use initial stiffness on first step and then current on subsequent steps |

The Newton method used in finite element analysis is identical to that taught in basic calculus courses. It is just extended for the n unknown degrees-of-freedom. The method as taught in basic calculus, is a root-finding algorithm that uses the first few terms of the Taylor series of a function \(f(x)\,\!\) in the vicinity of a suspected root \(x_n\,\!\) to find the root \(x_{n+1}\,\!\). Newton’s method is sometimes also known as Newton’s iteration, although in this work the latter term is reserved to the application of Newton’s method for computing square roots.

The Taylor series of \(r(x)\,\!\) about the point \(x=x_n+\Delta x\,\!\) is given by

\(f(x_n+\Delta x) = f(x_n)+r^{'}(x_n)\Delta x + 1/2r^{}(x_n) \Delta x^2+....\,\!\)
Keeping terms only to first order,

\(f(x_n+\Delta x) \approx f(x_n)+r^'(x_n)\Delta x = f(x_n)+ \frac{df(x_n)}{dx}\Delta x\)
and since at the root we wish to find \(x_n + \Delta x\), the function equates to 0, i.e. \(f(x_n+\Delta x) = 0\), we can solve for an approximate \(\Delta x\)

:math:` Delta x approx -frac{f(x_n)}{f^’(x_n)} = - frac{df(x_n)}{dx}^{-1}f(x_n)`
The Newmark method is thus an iterative method in which, starting at a good initial guess \(x_0\,\!\) we keep iterating until our convergence criteria is met with the following:

:math:` Delta x = - frac{df(x_n)}{dx}^{-1}f(x_n),!`
:math:` x_{n+1} = x_n + Delta x,!`

The method is generalized to n unknowns by replacing the above scalar equations with matrix ones.

\(R(U_n+\Delta x) = R(U_n)+\frac{\partial R(U_n)}{\partial U} \Delta U + O(\Delta U ^2) \,\!\)
The matrix \(\frac{\partial R(U_n)}{\partial U}\,\!\) is called the system Jacobian matrix and will be denoted K:

\[`K = \frac{\partial R(U_n)}{\partial U}\,\!\]

resulting in our iterative procedure where starting from a good initial guess we iterate until our convergence criteria is met with the following:

\[\Delta U = - K^{-1}R(U_n),\!\]

\[U_{n+1} = U_n + \Delta U\,\!\]

Example:

The following examples demonstrate the command to create a Linear solution algorithm.

1. **Tcl Code**

```
algorithm Newton
```

1. **Python Code**

```
algorithm('Newton')
```

Code Developed by: **fmk**
