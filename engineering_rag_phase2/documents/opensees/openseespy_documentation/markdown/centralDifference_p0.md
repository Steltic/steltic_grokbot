<!-- chunk_id: centralDifference_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/centralDifference.html",
 "title": "5.6.2.1. Central Difference",
 "category": "general",
 "command": "centralDifference",
 "doc_section": "src",
 "rel_path": "src/centralDifference.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 429,
 "word_count": 67,
 "has_code": false,
 "has_table": false
} -->

## 5.6.2.1. Central Difference

**integrator(*'CentralDifference'*)**

Create a centralDifference integrator.

1. The calculation of \(U_t + \Delta t\), is based on using the equilibrium equation at time t. For this reason the method is called an explicit integration method.
2. If there is no rayleigh damping and the C matrix is 0, for a diagonal mass matrix a diagonal solver may and should be used.
3. For stability, \(\frac{\Delta t}{T_n} < \frac{1}{\pi}\)
