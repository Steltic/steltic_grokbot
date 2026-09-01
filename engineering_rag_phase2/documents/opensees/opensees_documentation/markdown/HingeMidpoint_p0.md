<!-- chunk_id: HingeMidpoint_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeMidpoint.html",
 "title": "3.1.9.14. HingeMidpoint",
 "category": "command_manual",
 "manual_group": "model",
 "command": "HingeMidpoint",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/HingeMidpoint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1219,
 "word_count": 210,
 "has_code": true,
 "has_table": true
} -->

## 3.1.9.14. HingeMidpoint

**beamIntegration(*'HingeMidpoint'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

> Create a HingeMidpoint beamIntegration object.
> Midpoint integration over each hinge region is the most accurate one-point integration rule;
> however, it does not place integration points at the element ends and there is a small integration
> error for linear curvature distributions along the element.
>
> | `tag` \|int\| | tag of the beam integration. |
> | --- | --- | --- | --- |
> | `secI` \|int\| | A previous-defined section object for hinge at I. |
> | `lpI` *float* | The plastic hinge length at I. |
> | `secJ` \|int\| | A previous-defined section object for hinge at J. |
> | `lpJ` *float* | The plastic hinge length at J. |
> | `secE` \|int\| | A previous-defined section object for the element interior. |
>
> The plastic hinge length at end I (J) is equal to `lpI` (`lpJ`) and the associated force deformation response is defined by the `secI` (`secJ`). The force deformation
> response of the element interior is defined by the `secE`.
> Typically, the interior section is linear-elastic, but this is not necessary.
>
> ```
> lpI = 0.1
> lpJ = 0.2
> beamIntegration('HingeMidpoint',tag,secI,lpI,secJ,lpJ,secE)
> ```
