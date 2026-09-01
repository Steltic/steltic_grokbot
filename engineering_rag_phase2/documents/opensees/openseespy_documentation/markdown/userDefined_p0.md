<!-- chunk_id: userDefined_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/userDefined.html",
 "title": "4.13.7. UserDefined",
 "category": "general",
 "command": "userDefined",
 "doc_section": "src",
 "rel_path": "src/userDefined.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1560,
 "word_count": 176,
 "has_code": true,
 "has_table": true
} -->

## 4.13.7. UserDefined

**beamIntegration(*'UserDefined'*, *tag*, *N*, **secTags*, **locs*, **wts*)**

Create a UserDefined beamIntegration object.
This option allows user-specified locations and weights of the integration points.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the beam integration |
| --- | --- |
| `N` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points along the element. |
| `secTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list previous-defined section objects. |
| `locs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | Locations of integration points along the element. |
| `wts` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | weights of integration points. |

```
locs = [0.1, 0.3, 0.5, 0.7, 0.9]
wts = [0.2, 0.15, 0.3, 0.15, 0.2]
secs = [1, 2, 2, 2, 1]
beamIntegration('UserDefined',1,len(secs),*secs,*locs,*wts)
```

Places `N` integration points along the element, which are defined in `locs`
on the natural domain [0, 1]. The weight of each integration point is
defined in the `wts` also on the [0, 1] domain.
The force-deformation response at each integration point
is defined by the `secs`. The `locs`, `wts`, and `secs`
should be of length `N`. In general, there is no accuracy for this approach
to numerical integration.
