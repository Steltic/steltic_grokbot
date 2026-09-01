<!-- chunk_id: ExplicitDifference_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/ExplicitDifference.html",
 "title": "3.2.6.10. Explicit Difference",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "ExplicitDifference",
 "doc_section": "user/manual/analysis/integrator",
 "rel_path": "user/manual/analysis/integrator/ExplicitDifference.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 632,
 "word_count": 96,
 "has_code": true,
 "has_table": false
} -->

## 3.2.6.10. Explicit Difference

**integrator Explicitdifference**

Note

- When using Rayleigh damping, the damping ratio of high vibration modes is overrated, and the critical time step size will be much smaller. Hence Modal damping is more suitable for this method.
- There should be no zero element on the diagonal of the mass matrix when using this method.
- Diagonal solver should be used when lumped mass matrix is used because the equations are uncoupled.
- For stability \(\delta t \leq (\sqrt{\xi^2 +1} - \xi) \frac{2}{\omega}\)

Example

1. **Tcl Code**

```
integrator Explicitdifference
```

1. **Python Code**

```
integrator('ExplicitDifference')
```
