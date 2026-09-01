<!-- chunk_id: CentralDifference_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/CentralDifference.html",
 "title": "3.2.6.5. Central Difference",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "CentralDifference",
 "doc_section": "user/manual/analysis/integrator",
 "rel_path": "user/manual/analysis/integrator/CentralDifference.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1112,
 "word_count": 189,
 "has_code": false,
 "has_table": false
} -->

## 3.2.6.5. Central Difference

**integrator CentralDifference**

Note

- The calculation of \(U_{t+\Delta t}\), as shown below, is based on using the equilibrium equation at time t. For this reason the method is called an explicit integration method.
- If there is no rayleigh damping and the C matrix is 0, for a diagonal mass matrix a diagonal solver may and should be used.
- For stability, \(\frac{\Delta t}{T_n} < \frac{1}{\pi}\)

#### 3.2.6.5.1. THEORY:

The Central difference approximations for velocity and acceleration:

> :math:` v_n = frac{d_{n+1} - d_{n-1}}{2 Delta t}`
>
> :math:` a_n = frac{d_{n+1} - 2 d_n + d_{n-1}}{Delta t^2}`

In the Central Difference method we determine the displacement solution at time \(t+\delta t\) by considering the the eqilibrium equation for the finite element system in motion at time t:

> \(M \ddot U_t + C \dot U_t + K U_t = R_t\)

which when using the above two expressions of becomes:

> :math:` left ( frac{1}{Delta t^2} M + frac{1}{2 Delta t} C right ) U_{t+Delta t} = R_t - left (K - frac{2}{Delta t^2}M right )U_t - left (frac{1}{Delta t^2}M - frac{1}{2 Delta t} C right) U_{t-Delta t} `
