<!-- chunk_id: ConcentratedPlasticity_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/ConcentratedPlasticity.html",
 "title": "3.1.9.11. ConcentratedPlasticity beamIntegration",
 "category": "command_manual",
 "manual_group": "model",
 "command": "ConcentratedPlasticity",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/ConcentratedPlasticity.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1537,
 "word_count": 226,
 "has_code": false,
 "has_table": true
} -->

## 3.1.9.11. ConcentratedPlasticity beamIntegration

This command creates a Concentrated-Plasticity beamIntegration object. This integration places one plastic-rotation integration point at each element end and three elastic-curvature integration points along the length.

**beamIntegration ConcentratedPlasticity $integrationTag $secTagI $secTagJ $secTagE**

| Argument | Type | Description |
| --- | --- | --- |
| $integrationTag | *integer* | Integer tag identifying beamIntegration |
| $secTagI | *integer* | Tag of previously-defined section object for plastic “deformations” of the plastic hinge at node-I end of the element. (see note 1 below) |
| $secTagJ | *integer* | Tag of previously-defined section object for plastic “deformations” of the plastic hinge at node-J end of the element. (see note 1 below) |
| $secTagE | *integer* | Tag of previously-defined Elastic section object elastic behavior along element length. (see note 2 below) |

Note 1: The plastic-deformations behavior at the element ends represents finite plastic deformations. E.g. Bending must be defined in terms of bending moment vs plastic rotation, Axial must be defined in terms of axial force vs plastic axial deformations, etc. Because this integration defines flexibilities, you do not need to add rigid behavior for elastic deformation components, as they are already taken care of by the elastic segment.

Note 2: Use an elastic section which defines elastic moment-curvature, force-strain deformations

Code Developed by: |Silvia Mazzoni (Silvia's Brainery) & Michael Scott (Oregon State University)|
