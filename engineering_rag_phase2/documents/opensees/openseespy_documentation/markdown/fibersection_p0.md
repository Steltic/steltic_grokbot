<!-- chunk_id: fibersection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/fibersection.html",
 "title": "4.16.2. Fiber Section",
 "category": "section",
 "command": "fibersection",
 "doc_section": "src",
 "rel_path": "src/fibersection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1642,
 "word_count": 196,
 "has_code": false,
 "has_table": true
} -->

## 4.16.2. Fiber Section

**section(*'Fiber'*, *secTag*, *'-GJ'*, *GJ*)**

This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are `[P, Mz]`,
for 3D are `[P,Mz,My,T]`.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `GJ` ([float](https://docs.python.org/3/library/functions.html#float)) | linear-elastic torsional stiffness assigned to the section |

**section(*'Fiber'*, *secTag*, *'-torsion'*, *torsionMatTag*)**

This command allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are `[P, Mz]`,
for 3D are `[P,Mz,My,T]`.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `torsionMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxialMaterial tag assigned to the section for torsional response (can be nonlinear) |

Note

1. The commands below should be called after the section command to generate all the fibers in the section.
2. The patch and layer commands can be used to generate multiple fibers in a single command.

Commands to generate all fibers:

1. [Fiber Command](https://openseespydoc.readthedocs.io/en/latest/src/fiber.html)
2. [Patch Command](https://openseespydoc.readthedocs.io/en/latest/src/patch.html)
3. [Layer Command](https://openseespydoc.readthedocs.io/en/latest/src/layer.html)
