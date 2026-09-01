<!-- chunk_id: modelCommands_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/modelCommands.html",
 "title": "3.1. Model Commands",
 "category": "command_manual",
 "manual_group": "",
 "command": "modelCommands",
 "doc_section": "user/manual",
 "rel_path": "user/manual/modelCommands.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2336,
 "word_count": 169,
 "has_code": false,
 "has_table": false
} -->

## 3.1. Model Commands

These are the commands added to the interpreter to create the finite element model. A finite element model consists of **Nodes**, **Elements**, **Constraints**, and **Loads**. In OpenSees the Constraints are divided into two types: single-point constraints (**SP_Constraints)** for specifying the boundary condition for a specific degree-of-freedom at a node and multiple-point constraints (**MP_Constraints**) for specifying the relationship between the responses between the degrees-of-freedom at two separate nodes. The loads in OpenSees are assigned to **LoadPatterns**. Also associated with load patterns are **TimeSeries** objects ans sometime **SP_Constraints** when the user wants to specify time-varying **SP_Constraints**.

Fig. 3.1.1 OpenSees Model

In OpenSees there are commands to add each of these types of objects to a domain:

- [3.1.1. model Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/model.html)
- [3.1.2. node Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/node.html)
- [3.1.3. SP_Constraint Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/spConstraints.html)
- [3.1.4. MP_Constraint Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/mpConstraints.html)
- [3.1.5. uniaxialMaterial Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterial.html)
- [3.1.6. nDMaterial Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterial.html)
- [3.1.7. section Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/section.html)
- [3.1.8. Geometric Transformation Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/geomTransf.html)
- [3.1.9. Beam integration Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegration.html)
- [3.1.10. Element Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/element.html)
- [3.1.11. Time Series Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeSeries.html)
- [3.1.12. Pattern Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern.html)
- [3.1.13. Damping Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping.html)
