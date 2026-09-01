<!-- chunk_id: LagrangeMultipliers_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/LagrangeMultipliers.html",
 "title": "5.1.2. Lagrange Multipliers",
 "category": "general",
 "command": "LagrangeMultipliers",
 "doc_section": "src",
 "rel_path": "src/LagrangeMultipliers.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 778,
 "word_count": 97,
 "has_code": false,
 "has_table": true
} -->

## 5.1.2. Lagrange Multipliers

**constraints(*'Lagrange'*, *alphaS=1.0*, *alphaM=1.0*)**

This command is used to construct a LagrangeMultiplier constraint handler, which enforces the constraints by introducing Lagrange multiplies to the system of equation. The following is the command to construct a plain constraint handler:

| `alphaS` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_S\) factor on single points. |
| --- | --- |
| `alphaM` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_M\) factor on multi-points. |

Note

The Lagrange multiplier method introduces new unknowns to the system of equations. The diagonal part of the system corresponding to these new unknowns is 0.0. This ensure that the system IS NOT symmetric positive definite.
