<!-- chunk_id: beamIntegration_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegration.html",
 "title": "3.1.9. Beam integration Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "beamIntegration",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/beamIntegration.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3116,
 "word_count": 193,
 "has_code": false,
 "has_table": true
} -->

## 3.1.9. Beam integration Command

This command is used to construct an element and add it to the Domain.

**beamIntegration $integtaionType $tag $arg1 ...**

| Argument | Type | Description |
| --- | --- | --- |
| $integrationType | *string* | integration type |
| $tag | *integer* | unique beam integration tag. |
| $args | *list* | a list of arguments with number dependent on integration type |

Following are beamIntegration types available in the OpenSees:

1. Integration Methods for Distributed Plasticity. Distributed plasticity methods permit yielding at any integration point along the element length.

1. Zero-Length Elements

- [3.1.9.1. Lobatto](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/Lobatto.html)
- [3.1.9.2. Legendre](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/Legendre.html)
- [3.1.9.3. NewtonCotes](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/NewtonCotes.html)
- [3.1.9.4. Radau](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/Radau.html)
- [3.1.9.5. Trapezoidal](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/Trapezoidal.html)
- [3.1.9.6. CompositeSimpson](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/CompositeSimpson.html)
- [3.1.9.7. UserDefined](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/userDefined.html)
- [3.1.9.8. FixedLocation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/FixedLocation.html)
- [3.1.9.9. LowOrder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/LowOrder.html)
- [3.1.9.10. MidDistance](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/MidDistance.html)

1. Plastic Hinge Integration Methods. Plastic hinge integration methods confine material yielding to regions of the element of specified length while the remainder of the element is linear elastic. A summary of plastic hinge integration methods is found in (Scott and Fenves 2006).

- [3.1.9.11. ConcentratedPlasticity beamIntegration](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/ConcentratedPlasticity.html)
- [3.1.9.12. ConcentratedCurvature beamIntegration](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/ConcentratedCurvature.html)
- [3.1.9.13. UserHinge](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/UserHinge.html)
- [3.1.9.14. HingeMidpoint](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeMidpoint.html)
- [3.1.9.15. HingeRadau](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeRadau.html)
- [3.1.9.16. HingeRadauTwo](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeRadauTwo.html)
- [3.1.9.17. HingeEndpoint](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeEndpoint.html)
