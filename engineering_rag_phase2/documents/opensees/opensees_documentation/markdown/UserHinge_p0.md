<!-- chunk_id: UserHinge_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/UserHinge.html",
 "title": "3.1.9.13. UserHinge",
 "category": "command_manual",
 "manual_group": "model",
 "command": "UserHinge",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/UserHinge.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1259,
 "word_count": 240,
 "has_code": true,
 "has_table": true
} -->

## 3.1.9.13. UserHinge

**beamIntegration(*'UserHinge'*, *tag*, *secETag*, *npL*, **secsLTags*, **locsL*, **wtsL*, *npR*, **secsRTags*, **locsR*, **wtsR*)**

> Create a UserHinge beamIntegration object.
>
> | `tag` \|int\| | tag of the beam integration |
> | --- | --- | --- | --- |
> | `secE` \|int\| | A previous-defined section tags for element interior |
> | `npI` \|int\| | number of integration points along the hinge at end I |
> | `secsI` \|listi\| | A list of previous-defined section tags for hinge at end I |
> | `locsI` \|listf\| | A list of locations of integration points for hinge at end I |
> | `wtsI` \|listf\| | A list of weights of integration points for hinge at end I |
> | `npJ` \|int\| | number of integration points along the hinge at end J |
> | `secsJ` \|listi\| | A list of previous-defined section tags for hinge at end J |
> | `locsJ` \|listf\| | A list of locations of integration points for hinge at end J |
> | `wtsJ` \|listf\| | A list of weights of integration points for hinge at end J |
>
> ```
> tag = 1
> secE = 5
>
> npI = 2
> secsI = [1,2]
> locsI = [0.1,0.2]
> wtsI = [0.1,0.05]
>
> npJ = 2
> secsJ = [3,4]
> locsJ = [0.8,0.9]
> wtsJ = [0.05,0.1]
>
> beamIntegration('UserHinge',tag,secE,npI,*secsI,*locsI,*wtsI,npJ,*secsJ,*locsJ,*wtsJ)
> ```
