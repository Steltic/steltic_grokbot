<!-- chunk_id: HingeRadau_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeRadau.html",
 "title": "3.1.9.15. HingeRadau",
 "category": "command_manual",
 "manual_group": "model",
 "command": "HingeRadau",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/HingeRadau.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 646,
 "word_count": 71,
 "has_code": false,
 "has_table": false
} -->

## 3.1.9.15. HingeRadau

**beamIntegration(*'HingeRadau'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

> Create a HingeRadau beamIntegration object.
> Modified two-point Gauss-Radau integration over each hinge region places an integration point at
> the element ends and at 8/3 the hinge length inside the element. This approach represents
> linear curvature distributions exactly and the characteristic length for softening plastic hinges is equal to the assumed palstic hinge length.
>
> Arguments and examples see [HingeMidpoint](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/HingeMidpoint.html#hingemidpoint-beamintegration).
