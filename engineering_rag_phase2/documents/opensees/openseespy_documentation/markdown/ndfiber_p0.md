<!-- chunk_id: ndfiber_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ndfiber.html",
 "title": "4.16.4. NDFiber Section",
 "category": "section",
 "command": "ndfiber",
 "doc_section": "src",
 "rel_path": "src/ndfiber.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1444,
 "word_count": 195,
 "has_code": false,
 "has_table": true
} -->

## 4.16.4. NDFiber Section

**section(*'NDFiber'*, *secTag*)**

This command allows the user to construct an NDFiberSection object. Each NDFiberSection object is composed of NDFibers, with each fiber containing an NDMaterial, an area, and a location (y,z). The NDFiberSection works for 2D and 3D frame elements and it queries the NDMaterial of each fiber for its axial and shear stresses. In 2D, stress components 11 and 12 are obtained from each fiber in order to provide stress resultants for axial force, bending moment, and shear `[P, Mz, Vy]`. Stress components 11, 12, and 13 lead to all six stress resultants in 3D `[P, Mz, Vy, My, Vz, T]`.

The NDFiberSection works with any NDMaterial via wrapper classes that perform static condensation of the stress vector down to the 11, 12, and 13 components, or via specific NDMaterial subclasses that implement the appropriate fiber stress conditions.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |

Note

1. The commands below should be called after the section command to generate all the fibers in the section.
2. The patch and layer commands can be used to generate multiple fibers in a single command.

1. [`fiber()`](https://openseespydoc.readthedocs.io/en/latest/src/fiber.html#fiber)
2. [`patch()`](https://openseespydoc.readthedocs.io/en/latest/src/patch.html#patch)
3. [`layer()`](https://openseespydoc.readthedocs.io/en/latest/src/layer.html#layer)
