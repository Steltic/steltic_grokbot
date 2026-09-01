<!-- chunk_id: HingeRadauTwo_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeRadauTwo.html",
 "title": "3.1.9.16. HingeRadauTwo",
 "category": "command_manual",
 "manual_group": "model",
 "command": "HingeRadauTwo",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/HingeRadauTwo.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 696,
 "word_count": 79,
 "has_code": false,
 "has_table": false
} -->

## 3.1.9.16. HingeRadauTwo

**beamIntegration(*'HingeRadauTwo'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

> Create a HingeRadauTwo beamIntegration object.
> Two-point Gauss-Radau integration over each hinge region places an integration
> point at the element ends and at 2/3 the hinge length inside the element. This approach
> represents linear curvature distributions exactly; however, the characteristic length for softening
> plastic hinges is not equal to the assumed plastic hinge length (equals 1/4 of the plastic hinge length).
>
> Arguments and examples see [HingeMidpoint](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeMidpoint.html#hingemidpoint-beamintegration).
