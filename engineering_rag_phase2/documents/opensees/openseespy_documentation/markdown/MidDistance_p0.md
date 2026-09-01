<!-- chunk_id: MidDistance_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MidDistance.html",
 "title": "4.13.10. MidDistance",
 "category": "general",
 "command": "MidDistance",
 "doc_section": "src",
 "rel_path": "src/MidDistance.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1599,
 "word_count": 178,
 "has_code": true,
 "has_table": true
} -->

## 4.13.10. MidDistance

**beamIntegration(*'MidDistance'*, *tag*, *N*, **secTags*, **locs*)**

Create a MidDistance beamIntegration object.
This option allows user-specified locations of the integration points. The associated integration weights are determined from the midpoints between adjacent integration point locations.
\(w_i=(x_{i+1}-x_{i-1})/2\) for \(i=2...N-1\), \(w_1=(x_1+x_2)/2\), and \(w_N=1-(x_{N-1}+x_N)/2\).

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the beam integration |
| --- | --- |
| `N` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points along the element. |
| `secTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list previous-defined section objects. |
| `locs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | Locations of integration points along the element. |

```
locs = [0.0, 0.2, 0.5, 0.8, 1.0]
secs = [1,2,2,2,1]
beamIntegration('MidDistance',1,len(secs),*secs,*locs)
```

Places `N` integration points along the element, whose locations are defined
in `locs` on the natural domain [0, 1].
The force-deformation response at each integration
point is defined by the `secs`.
Both the `locs` and `secs` should be of length N.
This integration rule can only integrate constant
functions exactly since the sum of the integration weights is one.

For the `locs` shown above, the associated integration weights
will be `[0.15, 0.2, 0.3, 0.2, 0.15]`.
