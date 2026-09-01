<!-- chunk_id: spConstraints_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/spConstraints.html",
 "title": "3.1.3. SP_Constraint Commands",
 "category": "command_manual",
 "manual_group": "model",
 "command": "spConstraints",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/spConstraints.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1170,
 "word_count": 90,
 "has_code": false,
 "has_table": false
} -->

## 3.1.3. SP_Constraint Commands

Single point constraints (SP_Constraints) are constraints that define the response of a single degree-of-freedom at a node. These constraints can be homogeneous **(=0.0)** or non-homogeneos. Non homogeneous SP_Constraints, which define the non-zero response of the degree-of-freedom, can be constant or time varying. In the OpenSees interpreters there are a number of commands to add a homogeneous SP_Constraint.

- [3.1.3.1. fix Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/sp_constraint/fix.html)
- [3.1.3.2. fixX Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/sp_constraint/fixX.html)
- [3.1.3.3. fixY Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/sp_constraint/fixY.html)
- [3.1.3.4. fixY Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/sp_constraint/fixZ.html)

Non-homogeneous constraints are added with wither sp_constraint/sp or imposedMotion commands inside the :ref:`plainPattern or [Multisupport Excitation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/multiSupportPattern.html#multisupportexcitation) commands.
