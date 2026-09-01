<!-- chunk_id: ConcentratedCurvature_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ConcentratedCurvature.html",
 "title": "ConcentratedCurvature",
 "category": "general",
 "command": "ConcentratedCurvature",
 "doc_section": "src",
 "rel_path": "src/ConcentratedCurvature.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1735,
 "word_count": 254,
 "has_code": false,
 "has_table": true
} -->

## ConcentratedCurvature

This command creates a Concentrated-Plasticity beamIntegration object. This integration places one integration point at each element end, representing the plastic hinge and three elastic-curvature integration points along the elastic segment.

**beamIntegration ConcentratedCurvature $integrationTag $secTagI $LpI $secTagJ $LpJ $secTagE**

**beamIntegration(*'ConcentratedCurvature'*, *integrationTag*, *secTagI*, *LpI*, *secTagJ*, *LpJ*, *secTagE*)**

| Argument | Type | Description |
| --- | --- | --- | --- | --- |
| $integrationTag | \|integer\| | Integer tag identifying beamIntegration |
| $secTagI | \|integer\| | Tag of previously-defined section object for plastic hinge at node-I end of the element. (see note 1 below) |
| $LpI | \|float\| | Node-I plastic-hinge length. |
| $secTagJ | \|integer\| | Tag of previously-defined section object for plastic hinge at node-J end of the element. (see note 1 below) |
| $LpJ | \|float\| | Node-J plastic-hinge length. |
| $secTagE | \|integer\| | Tag of previously-defined Elastic section object elastic behavior along element length. (see note 2 below) |

Note 1: The plastic-hinge behavior at the element ends represents plastic-hinge deformations assumed to be constant over the plastic-hinge length (LpNodeI and LpNodeJ) but located at the element ends. Bending must be defined in terms of bending moment vs curvature,
Axial must be defined in terms of axial force vs axial strain, etc. All deformations must be represented by the section. YES YOU MAY USE A FIBER SECTION!!!

Note 2: Use an elastic section which defines elastic moment-curvature, force-strain deformations

Code Developed (2023) by: |Silvia Mazzoni (Silvia's Brainery) & Michael Scott (Oregon State University)|
