<!-- chunk_id: fiberThermalsection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/fiberThermalsection.html",
 "title": "4.16.3. Fiber Thermal Section",
 "category": "section",
 "command": "fiberThermalsection",
 "doc_section": "src",
 "rel_path": "src/fiberThermalsection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 661,
 "word_count": 73,
 "has_code": false,
 "has_table": false
} -->

## 4.16.3. Fiber Thermal Section

**section(*'FiberThermal'*, *secTag*, *'-GJ'*, *GJ=0.0*)**

This command create a FiberSectionThermal object.
The dofs for 2D section are `[P, Mz]`,
for 3D are `[P,Mz,My]`.

Note

1. The commands below should be called after the section command to generate all the fibers in the section.
2. The patch and layer commands can be used to generate multiple fibers in a single command.

Commands to generate all fibers:

1. [Fiber Command](https://openseespydoc.readthedocs.io/en/latest/src/fiber.html)
2. [Patch Command](https://openseespydoc.readthedocs.io/en/latest/src/patch.html)
3. [Layer Command](https://openseespydoc.readthedocs.io/en/latest/src/layer.html)
