<!-- chunk_id: explicitDifference_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/explicitDifference.html",
 "title": "5.6.2.6. Explicit Difference",
 "category": "general",
 "command": "explicitDifference",
 "doc_section": "src",
 "rel_path": "src/explicitDifference.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 561,
 "word_count": 80,
 "has_code": false,
 "has_table": false
} -->

## 5.6.2.6. Explicit Difference

**integrator(*'ExplicitDifference'*)**

Create a ExplicitDifference integrator.

1. When using Rayleigh damping, the damping ratio of high vibration modes is overrated, and the critical time step size will be much smaller. Hence Modal damping is more suitable for this method.
2. There should be no zero element on the diagonal of the mass matrix when using this method.
3. Diagonal solver should be used when lumped mass matrix is used because the equations are uncoupled.
4. For stability, \(\Delta t \leq \left(\sqrt{\zeta^2+1}-\zeta\right)\frac{2}{\omega}\)
