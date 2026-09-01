<!-- chunk_id: zeroLengthImpact3D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthImpact3D.html",
 "title": "4.2.1.9. zeroLengthImpact3D",
 "category": "general",
 "command": "zeroLengthImpact3D",
 "doc_section": "src",
 "rel_path": "src/zeroLengthImpact3D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2827,
 "word_count": 346,
 "has_code": false,
 "has_table": true
} -->

## 4.2.1.9. zeroLengthImpact3D

**element(*'zeroLengthImpact3D'*, *eleTag*, **eleNodes*, *direction*, *initGap*, *frictionRatio*, *Kt*, *Kn*, *Kn2*, *Delta_y*, *cohesion*)**

This command constructs a node-to-node zero-length contact element in 3D space to simulate the impact/pounding and friction phenomena.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of a constrained and a retained nodes |
| `direction` ([int](https://docs.python.org/3/library/functions.html#int)) | `1` if out-normal vector of master plane points to +X direction `2` if out-normal vector of master plane points to +Y direction `3` if out-normal vector of master plane points to +Z direction |
| `initGap` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial gap between master plane and slave plane |
| `frictionRatio` ([float](https://docs.python.org/3/library/functions.html#float)) | Friction ratio in two tangential directions (parallel to master and slave planes) |
| `Kt` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in two tangential directions |
| `Kn` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in normal direction (normal to master and slave planes) |
| `Kn2` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in normal direction after yielding based on Hertz impact model |
| `Delta_y` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield deformation based on Hertz impact model |
| `cohesion` ([float](https://docs.python.org/3/library/functions.html#float)) | Cohesion, if no cohesion, it is zero |

Note

1. This element has been developed on top of the “zeroLengthContact3D”. All the notes available in “zeroLengthContact3D” wiki page would apply to this element as well. It includes the definition of master and slave nodes, the number of degrees of freedom in the domain, etc.
2. Regarding the number of degrees of freedom (DOF), the end nodes of this element should be defined in 3DOF domain. For getting information on how to use 3DOF and 6DOF domain together, please refer to OpenSees documentation and forums or see the zip file provided in the EXAMPLES section below.
3. This element adds the capabilities of “ImpactMaterial” to “zeroLengthContact3D.”
4. For simulating a surface-to-surface contact, the element can be defined for connecting the nodes on slave surface to the nodes on master surface.
5. The element was found to be fast-converging and eliminating the need for extra elements and nodes in the modeling process.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ZeroLengthImpact3D)
