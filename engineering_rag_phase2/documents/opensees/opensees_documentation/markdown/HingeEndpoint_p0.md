<!-- chunk_id: HingeEndpoint_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeEndpoint.html",
 "title": "3.1.9.17. HingeEndpoint",
 "category": "command_manual",
 "manual_group": "model",
 "command": "HingeEndpoint",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/HingeEndpoint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 927,
 "word_count": 138,
 "has_code": false,
 "has_table": true
} -->

## 3.1.9.17. HingeEndpoint

**beamIntegration(*'HingeEndpoint'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

> Create a HingeEndpoint beamIntegration object.
> Endpoint integration over each hinge region moves the integration points to the element ends;
> however, there is a large integration error for linear curvature distributions along the element.
>
> | `tag` \|int\| | tag of the beam integration. |
> | --- | --- | --- | --- |
> | `secI` \|int\| | A previous-defined section object for hinge at I. |
> | `lpI` *float* | The plastic hinge length at I. |
> | `secJ` \|int\| | A previous-defined section object for hinge at J. |
> | `lpJ` *float* | The plastic hinge length at J. |
> | `secE` \|int\| | A previous-defined section object for the element interior. |
>
> Arguments and examples see [HingeMidpoint](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeMidpoint.html#hingemidpoint-beamintegration).
