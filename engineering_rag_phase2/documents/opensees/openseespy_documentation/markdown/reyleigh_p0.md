<!-- chunk_id: reyleigh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/reyleigh.html",
 "title": "4.11. rayleigh command",
 "category": "general",
 "command": "reyleigh",
 "doc_section": "src",
 "rel_path": "src/reyleigh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 964,
 "word_count": 114,
 "has_code": false,
 "has_table": true
} -->

## 4.11. rayleigh command

**rayleigh(*alphaM*, *betaK*, *betaKinit*, *betaKcomm*)**

This command is used to assign damping to all previously-defined elements and nodes. When using rayleigh damping in OpenSees, the damping matrix for an element or node, D is specified as a combination of stiffness and mass-proportional damping matrices:

\[D = \alpha_M * M + \beta_K * K_{curr} + \beta_{Kinit} * K_{init} + \beta_{Kcomm} * K_{commit}\]

| `alphaM` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements or nodes mass matrix |
| --- | --- |
| `betaK` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements current stiffness matrix. |
| `betaKinit` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements initial stiffness matrix. |
| `betaKcomm` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements committed stiffness matrix. |
