<!-- chunk_id: Newmark_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/Newmark.html",
 "title": "3.2.6.3. Newmark Method",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "Newmark",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/Newmark.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4388,
 "word_count": 629,
 "has_code": true,
 "has_table": true
} -->

## 3.2.6.3. Newmark Method

This command is used to construct a Newmark integrator object.

**integrator Newmark $gamma $beta**

| Argument | Type | Description |
| --- | --- | --- |
| $gamma | *float* | \(\gamma\) factor |
| $beta | *float* | \(\beta\) factor |

Note

1. If the accelerations are chosen as the unknowns and \(\beta\) is chosen as 0, the formulation results in the fast but conditionally stable explicit Central Difference method. Otherwise the method is implicit and requires an iterative solution process.
2. Two common sets of choices are:

  Average Acceleration Method (\(\gamma=\frac{1}{2}, \beta = \frac{1}{4}\))

  Linear Acceleration Method (\(\gamma=\frac{1}{2}, \beta = \frac{1}{6}\))
3. \(\gamma > \frac{1}{2}\) results in numerical damping proportional to \(\gamma - \frac{1}{2}\)
4. The method is second order accurate if and only if \(\gamma = \frac{1}{2}\)
5. The method is conditionally stable for \(\beta >= \frac{\gamma}{2} >= \frac{1}{4}\)

#### 3.2.6.3.1. Theory

The Newmark method is a one step implicit method for solving the transient problem, represented by the residual for the momentum equation:

\[R_{t + \Delta t} = F_{t+\Delta t}^{ext} - M \ddot U_{t + \Delta t} - C \dot U_{t + \Delta t} + F(U_{t + \Delta t})^{int}\]

Using the Taylor series approximation of \(U_{t+\Delta t}\) and \(\dot U_{t+\Delta t}\):

\[ \begin{align}\begin{aligned}U_{t+\Delta t} = U_t + \Delta t \dot U_t + \frac{\Delta t^2}{2} \ddot U_t + \frac{\Delta t^3}{6} \dddot U_t + \cdots\\\dot U_{t+\Delta t} = \dot U_t + \Delta t \ddot U_t + \frac{\Delta t^2}{2} \dddot U_t + \cdots\end{aligned}\end{align} \]

Newton truncated these using the following:

\[ \begin{align}\begin{aligned}U_{t+\Delta t} = u_t + \Delta t \dot U_t + \frac{\Delta t^2}{2} \ddot U + \beta {\Delta t^3} \dddot U\\\dot U_{t + \Delta t} = \dot U_t + \Delta t \ddot U_t + \gamma \Delta t^2 \dddot U\end{aligned}\end{align} \]

in which he assumed linear acceleration within a time step, i.e.,

\[\dddot U = \frac{{\ddot U_{t+\Delta t}} - \ddot U_t}{\Delta t}\]

which results in the following expressions:

\[ \begin{align}\begin{aligned}U_{t+\Delta t} = U_t + \Delta t \dot U_t + [(0.5 - \beta) \Delta t^2] \ddot U_t + [\beta \Delta t^2] \ddot U_{t+\Delta t}\\\dot U_{t+\Delta t} = \dot U_t + [(1-\gamma)\Delta t] \ddot U_t + [\gamma \Delta t ] \ddot U_{t+\Delta t}\end{aligned}\end{align} \]

The variables \(\beta\) and \(\gamma\) are numerical parameters that control both the stability of the method and the amount of numerical damping introduced into the system by the method. For \(\gamma=\frac{1}{2}\) there is no numerical damping; for \(\gamma>=\frac{1}{2}\) numerical damping is introduced. Two well known and commonly used cases are:

> 1. Average Acceleration Method (\(\gamma=\frac{1}{2}, \beta = \frac{1}{4}\))
> 2. Constant Acceleration Method (\(\gamma=\frac{1}{2}, \beta = \frac{1}{6}\))

The linearization of the Newmark equations gives:

\[ \begin{align}\begin{aligned}dU_{t+\Delta t}^{i+1} = \beta \Delta t^2 d \ddot U_{t+\Delta t}^{i+1}\\d \dot U_{t+\Delta t}^{i+1} = \gamma \Delta t \ddot U_{t+\Delta t}^{i+1}\end{aligned}\end{align} \]

which gives the update formula when displacement increment is used as unknown in the linearized system as:

\[ \begin{align}\begin{aligned}U_{t+\Delta t}^{i+1} = U_{t+\Delta t}^i + dU_{t+\Delta t}^{i+1}\\\dot U_{t+\Delta t}^{i+1} = \dot U_{t+\Delta t}^i + \frac{\gamma}{\beta \Delta t}dU_{t+\Delta t}^{i+1}\\\ddot U_{t+\Delta t}^{i+1} = \ddot U_{t+\Delta t}^i + \frac{1}{\beta \Delta t^2}dU_{t+\Delta t}^{i+1}\end{aligned}\end{align} \]

The linearization of the momentum equation using the displacements as the unknowns leads to the following linear equation:

\[K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = R_{t+\Delta t}^i\]

where,

\[K_{t+\Delta t}^{*i} = K_t + \frac{\gamma}{\beta \Delta t} C_t + \frac{1}{\beta \Delta t^2} M\]

and,

\[R_{t+\Delta t}^i = F_{t + \Delta t}^{ext} - F(U_{t + \Delta t}^{i-1})^{int} - C \dot U_{t+\Delta t}^{i-1} - M \ddot U_{t+ \Delta t}^{i-1}\]

Example

The following example shows how to construct a Newmark Integrator.

1. **Tcl Code**

```
integrator Newmark 0.5 0.25
```

1. **Python Code**

```
integrator('Newmark', 0.5, 0.25)
```

**Newmark1959**

> Newmark, N.M. “A Method of Computation for Structural Dynamics” ASCE Journal of Engineering Mechanics Division, Vol 85. No EM3, 1959.

Code Developed by: **fmk**
