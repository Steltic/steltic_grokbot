<!-- chunk_id: rayleigh_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/rayleigh.html",
 "title": "3.1.13.1. Rayleigh Damping Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "rayleigh",
 "doc_section": "user/manual/model/damping",
 "rel_path": "user/manual/model/damping/rayleigh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1132,
 "word_count": 161,
 "has_code": false,
 "has_table": true
} -->

## 3.1.13.1. Rayleigh Damping Command

**rayleigh $alphaM $betaK $betaKInit $betaKcomm**

| Argument | Type | Description |
| --- | --- | --- |
| $alphaM | *float* | factor applied to elements or nodes mass matrix |
| $betaK | *float* | factor applied to elements current stiffness matrix. |
| $betaKInit | *float* | factor applied to elements initial stiffness matrix |
| $betaKcomm | *float* | factor applied to elements committed stiffness matrix |

This command is used to assign damping to all previously-defined elements and nodes. When using rayleigh damping in OpenSees, the damping matrix for an element or node, D is specified as a combination of stiffness and mass-proportional damping matrices:

\(D = \alpha_m M + \beta_k K_{current} + \beta_{k_{init}} K_{init} + \beta_{K_{comm}} K_{last commit}\)

Note

- The command overwrites any existing damping coeeficients at the Elements and Nodes.
- The usage of Rayleigh damping may provide incorrect result when used with Non-Linear Time History Analysis using Concentrated Plasticity Model. [[ChopraMcKenna2015]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping.html#chopramckenna2015)
