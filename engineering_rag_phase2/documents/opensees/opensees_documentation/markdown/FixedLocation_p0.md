<!-- chunk_id: FixedLocation_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/FixedLocation.html",
 "title": "3.1.9.8. FixedLocation",
 "category": "command_manual",
 "manual_group": "model",
 "command": "FixedLocation",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/FixedLocation.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1253,
 "word_count": 176,
 "has_code": false,
 "has_table": true
} -->

## 3.1.9.8. FixedLocation

**beamIntegration(*'FixedLocation'*, *tag*, *N*, **secTags*, **locs*)**

> Create a FixedLocation beamIntegration object.
> This option allows user-specified locations of the integration points. The associated integration
> weights are computed by the method of undetermined coefficients (Vandermonde
> system)
>
> \[\sum^N_{i=1}x_i^{j-1}w_i = \int_0^1x^{j-1}dx = \frac{1}{j},\qquad (j=1,...,N)\]
>
> Note that [NewtonCotes](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/NewtonCotes.html#newtoncotes-beamintegration) integration is recovered when the integration point locations are equally spaced.
>
> | `tag` \|int\| | tag of the beam integration |
> | --- | --- | --- | --- |
> | `N` \|int\| | number of integration points along the element. |
> | `secTags` \|listi\| | A list previous-defined section objects. |
> | `locs` \|listf\| | Locations of integration points along the element. |
>
> Places `N` integration points along the element, whose locations are defined in `locs`.
> on the natural domain [0, 1]. The force-deformation response at each integration
> point is defined by the `secs`. Both the `locs` and `secs`
> should be of length `N`. The order of accuracy for Fixed Location integration is N-1.
