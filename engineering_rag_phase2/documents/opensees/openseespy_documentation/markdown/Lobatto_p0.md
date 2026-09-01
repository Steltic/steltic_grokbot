<!-- chunk_id: Lobatto_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html",
 "title": "4.13.1. Lobatto",
 "category": "general",
 "command": "Lobatto",
 "doc_section": "src",
 "rel_path": "src/Lobatto.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2075,
 "word_count": 186,
 "has_code": true,
 "has_table": true
} -->

## 4.13.1. Lobatto

**beamIntegration(*'Lobatto'*, *tag*, *secTag*, *N*)**

**beamIntegration(*'Lobatto'*, *tag*, *N*, **secTags*)**

Create a Gauss–Lobatto `beamIntegration` object. Gauss–Lobatto is common for [forceBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/ForceBeamColumn.html) ([Neuenhofer and Filippou 1997](https://doi.org/10.1061/(ASCE)0733-9445(1997)123:7(958))) because it places an integration point at each end of the element, where bending is largest if there are no interior element loads.

**Prismatic** — one section for all points: `(tag, secTag, N)`.

**Non-prismatic** — one section tag per point, in order from node *I* to *J*: `(tag, N, secTag1, secTag2, …, secTagN)`.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique beam integration tag |
| --- | --- |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | (prismatic) one defined section for all points |
| `N` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points |
| `secTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | (non-prismatic) `N` section tags |

Note

The non-prismatic form assigns different sections along the length (e.g. tapering reinforcement) without relying on hinge-only schemes. The same two forms exist for [Legendre](https://openseespydoc.readthedocs.io/en/latest/src/Legendre.html), [Radau](https://openseespydoc.readthedocs.io/en/latest/src/Radau.html), [NewtonCotes](https://openseespydoc.readthedocs.io/en/latest/src/NewtonCotes.html), [Trapezoidal](https://openseespydoc.readthedocs.io/en/latest/src/Trapezoidal.html), and [CompositeSimpson](https://openseespydoc.readthedocs.io/en/latest/src/CompositeSimpson.html).

Example

Prismatic: 6 points, section tag 1. Non-prismatic: 3 sections `[1, 2, 1]` at 3 Lobatto points.

```
import openseespy.opensees as ops

ops.beamIntegration('Lobatto', 2, 1, 6)
sec_tag_list = [1, 2, 1]
ops.beamIntegration('Lobatto', 3, len(sec_tag_list), *sec_tag_list)
```
