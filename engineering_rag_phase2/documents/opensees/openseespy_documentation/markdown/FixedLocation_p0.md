<!-- chunk_id: FixedLocation_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/FixedLocation.html",
 "title": "4.13.8. FixedLocation",
 "category": "general",
 "command": "FixedLocation",
 "doc_section": "src",
 "rel_path": "src/FixedLocation.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1516,
 "word_count": 155,
 "has_code": false,
 "has_table": true
} -->

## 4.13.8. FixedLocation

**beamIntegration(*'FixedLocation'*, *tag*, *N*, **secTags*, **locs*)**

Create a FixedLocation beamIntegration object.
This option allows user-specified locations of the integration points. The associated integration
weights are computed by the method of undetermined coefficients (Vandermonde
system)

\[\sum^N_{i=1}x_i^{j-1}w_i = \int_0^1x^{j-1}dx = \frac{1}{j},\qquad (j=1,...,N)\]

Note that [NewtonCotes](https://openseespydoc.readthedocs.io/en/latest/src/NewtonCotes.html#newtoncotes-beamintegration) integration is recovered when the integration point locations are equally spaced.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the beam integration |
| --- | --- |
| `N` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points along the element. |
| `secTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list previous-defined section objects. |
| `locs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | Locations of integration points along the element. |

Places `N` integration points along the element, whose locations are defined in `locs`.
on the natural domain [0, 1]. The force-deformation response at each integration
point is defined by the `secs`. Both the `locs` and `secs`
should be of length `N`. The order of accuracy for Fixed Location integration is N-1.
