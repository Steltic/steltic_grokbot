<!-- chunk_id: ConcentratedCurvature_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/ConcentratedCurvature.html",
 "title": "3.1.9.12. ConcentratedCurvature beamIntegration",
 "category": "command_manual",
 "manual_group": "model",
 "command": "ConcentratedCurvature",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/ConcentratedCurvature.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1591,
 "word_count": 242,
 "has_code": false,
 "has_table": true
} -->

## 3.1.9.12. ConcentratedCurvature beamIntegration

This command creates a Concentrated-Plasticity beamIntegration object. This integration places one integration point at each element end, representing the plastic hinge and three elastic-curvature integration points along the elastic segment.

**beamIntegration ConcentratedCurvature $integrationTag $secTagI $LpI $secTagJ $LpJ $secTagE**

| Argument | Type | Description |
| --- | --- | --- |
| $integrationTag | *integer* | Integer tag identifying beamIntegration |
| $secTagI | *integer* | Tag of previously-defined section object for plastic hinge at node-I end of the element. (see note 1 below) |
| $LpI | *float* | Node-I plastic-hinge length. |
| $secTagJ | *integer* | Tag of previously-defined section object for plastic hinge at node-J end of the element. (see note 1 below) |
| $LpJ | *float* | Node-J plastic-hinge length. |
| $secTagE | *integer* | Tag of previously-defined Elastic section object elastic behavior along element length. (see note 2 below) |

Note 1: The plastic-hinge behavior at the element ends represents plastic-hinge deformations assumed to be constant over the plastic-hinge length (LpNodeI and LpNodeJ) but located at the element ends. Bending must be defined in terms of bending moment vs curvature,
Axial must be defined in terms of axial force vs axial strain, etc. All deformations must be represented by the section. YES YOU MAY USE A FIBER SECTION!!!

Note 2: Use an elastic section which defines elastic moment-curvature, force-strain deformations

Code Developed by: |Silvia Mazzoni (Silvia's Brainery) & Michael Scott (Oregon State University)|
