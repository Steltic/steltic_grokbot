<!-- chunk_id: LowOrder_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/LowOrder.html",
 "title": "4.13.9. LowOrder",
 "category": "general",
 "command": "LowOrder",
 "doc_section": "src",
 "rel_path": "src/LowOrder.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2868,
 "word_count": 282,
 "has_code": true,
 "has_table": true
} -->

## 4.13.9. LowOrder

**beamIntegration(*'LowOrder'*, *tag*, *N*, **secTags*, **locs*, **wts*)**

Create a LowOrder beamIntegration object.
This option is a generalization of the [FixedLocation](https://openseespydoc.readthedocs.io/en/latest/src/FixedLocation.html#fixedlocation-beamintegration) and [UserDefined](https://openseespydoc.readthedocs.io/en/latest/src/userDefined.html#userdefined-beamintegration) integration approaches and is useful for moving load analysis ([Kidarsa, Scott and Higgins 2008](https://doi.org/10.1016/j.finel.2007.11.013)). The locations of the integration points are user defined,
while a selected number of weights are specified and the remaining weights are
computed by the method of undetermined coefficients.

\[\sum_{i=1}^{N_f}x_{fi}^{j-1}w_{fi}=\frac{1}{j}-\sum_{i=1}^{N_c}x_{ci}^{j-1}w_{ci}\]

Note that [FixedLocation](https://openseespydoc.readthedocs.io/en/latest/src/FixedLocation.html#fixedlocation-beamintegration) integration is recovered when `Nc` is zero.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the beam integration |
| --- | --- |
| `N` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points along the element. |
| `secTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list previous-defined section objects. |
| `locs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | Locations of integration points along the element. |
| `wts` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | weights of integration points. |

```
locs = [0.0, 0.2, 0.5, 0.8, 1.0]
wts = [0.2, 0.2]
secs = [1, 2, 2, 2, 1]
beamIntegration('LowOrder',1,len(secs),*secs,*locs,*wts)
```

Places `N` integration points along the element, which are defined in `locs`.
on the natural domain [0, 1]. The force-deformation response at each integration point is
defined by the `secs`. Both the `locs` and `secs`
should be of length `N`. The `wts` at user-selected integration
points are specified on [0, 1],
which can be of length `Nc` equals `0` up to `N`. These specified weights
are assigned to the first `Nc` entries in the `locs` and `secs`, respectively. The
order of accuracy for Low Order integration is N-Nc-1.

Note

`Nc` is determined from the length of the `wts` list. Accordingly,
[FixedLocation](https://openseespydoc.readthedocs.io/en/latest/src/FixedLocation.html#fixedlocation-beamintegration)
integration is recovered when `wts` is an empty list and
[UserDefined](https://openseespydoc.readthedocs.io/en/latest/src/userDefined.html#userdefined-beamintegration) integration is
recovered when the `wts` and `locs` lists are of equal length.
