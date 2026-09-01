<!-- chunk_id: element_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/element.html",
 "title": "3.1.10. Element Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "element",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/element.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 6049,
 "word_count": 350,
 "has_code": false,
 "has_table": true
} -->

## 3.1.10. Element Command

This command is used to construct an element and add it to the Domain.

**element $eleType $tag (num $nodes) $arg1 ...**

| Argument | Type | Description |
| --- | --- | --- |
| $eleType | *string* | element type |
| $eleTag | *integer* | unique element tag. |
| $nodes | *list integer* | a list of element nodes with number dependent on ele type |
| $eleArgs | *list* | a list of element arguments with number dependent on ele type |

Note

The type of element created and the additional arguments required depends on the **$eleType** provided.

The valid queries to any element when creating an ElementRecorder are documented in the NOTES section for each element.

The following subsections contain information about **$eleType** and the number of nodes and args required for each of the available element types:

1. Zero-Length Elements

- [3.1.10.1. ZeroLength Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/zeroLength.html)
- [3.1.10.2. ZeroLength Section Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/zeroLengthSection.html)
- [3.1.10.3. ZeroLengthND Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/zeroLengthND.html)
- [3.1.10.4. ZeroLengthContactASDimplex Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/zeroLengthContactASDimplex.html)

1. Trusss Elements

1. Beam Column Elements

- [3.1.10.5. Elastic Beam Column Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/elasticBeamColumn.html)
- [3.1.10.6. Modified Elastic Beam Column Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ModElasticBeam.html)
- [3.1.10.7. Gradient Inelastic (GI) Beam-Column Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/gradientInelasticBeamColumn.html)
- [3.1.10.8. MVLEM_3D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/MVLEM_3D.html)
- [3.1.10.9. SFI-MVLEM-3D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/SFI_MVLEM_3D.html)
- [3.1.10.10. E-SFI-MVLEM-3D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/E_SFI_MVLEM_3D.html)
- [3.1.10.11. Displacement-Based Beam Element (Asymmetric Sections)](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/dispBeamColumnAsym.html)
- [3.1.10.12. Mixed Beam Element (Asymmetric Sections)](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/mixedBeamColumnAsym.html)
- [3.1.10.13. E-SFI Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/E_SFI.html)

1. Quadrilateral & Shell Elements

- [3.1.10.14. ASDShellQ4 Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ASDShellQ4.html)
- [3.1.10.15. Quadrilateral Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/Quad.html)
- [3.1.10.16. SSPquad Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/SSPquad.html)
- [3.1.10.17. MEFI Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/MEFI.html)

1. Triangles

- [3.1.10.18. ASDShellT3 Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ASDShellT3.html)

1. Bricks

- [3.1.10.19. stdBrick Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/stdBrick.html)
- [3.1.10.20. bbarBrick Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/bbarBrick.html)
- [3.1.10.21. SSPbrick Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/SSPbrick.html)

1. Tetrahedrons

- [3.1.10.22. FourNodeTetrahedron Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FourNodeTetrahedron.html)
- [3.1.10.23. TenNodeTetrahedron Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/TenNodeTetrahedron.html)

1. Joint Elements

- [3.1.10.24. BeamColumnJoint Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/BeamColumnJoint.html)
- [3.1.10.25. ElasticTubularJoint Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ElasticTubularJoint.html)
- [3.1.10.26. Joint2D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/Joint2D.html)
- [3.1.10.27. Inno3DPnPJoint Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/Inno3DPnPJoint.html)
- [3.1.10.28. LehighJoint2D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/LehighJoint2D.html)

1. Link Elements

1. Bearing Elements

- [3.1.10.29. TripleFrictionPendulumX Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/TripleFrictionPendulumX.html)

1. U-P Elements (saturated soil)

1. Contact

1. Cable

1. Absorbing Elements

- [3.1.10.30. PML Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/PML.html)

1. Misc.

- [3.1.10.31. ASDEmbeddedNode Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ASDEmbeddedNodeElement.html)
- [3.1.10.32. ASDAbsorbingBoundary Element (2D and 3D)](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ASDAbsorbingBoundary.html)
- [3.1.10.33. RockingBC Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/RockingBC.html)
- [3.1.10.34. FSIFluidBoundaryElement2D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIFluidBoundaryElement2D.html)
- [3.1.10.35. FSIFluidElement2D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIFluidElement2D.html)
- [3.1.10.36. FSIInterfaceElement2D Element](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html)
