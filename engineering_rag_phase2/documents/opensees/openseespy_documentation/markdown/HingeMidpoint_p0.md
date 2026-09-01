<!-- chunk_id: HingeMidpoint_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/HingeMidpoint.html",
 "title": "4.13.12. HingeMidpoint",
 "category": "general",
 "command": "HingeMidpoint",
 "doc_section": "src",
 "rel_path": "src/HingeMidpoint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1498,
 "word_count": 184,
 "has_code": true,
 "has_table": true
} -->

## 4.13.12. HingeMidpoint

**beamIntegration(*'HingeMidpoint'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

Create a HingeMidpoint beamIntegration object.
Midpoint integration over each hinge region is the most accurate one-point integration rule;
however, it does not place integration points at the element ends and there is a small integration
error for linear curvature distributions along the element.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the beam integration. |
| --- | --- |
| `secI` ([int](https://docs.python.org/3/library/functions.html#int)) | A previous-defined section object for hinge at I. |
| `lpI` ([float](https://docs.python.org/3/library/functions.html#float)) | The plastic hinge length at I. |
| `secJ` ([int](https://docs.python.org/3/library/functions.html#int)) | A previous-defined section object for hinge at J. |
| `lpJ` ([float](https://docs.python.org/3/library/functions.html#float)) | The plastic hinge length at J. |
| `secE` ([int](https://docs.python.org/3/library/functions.html#int)) | A previous-defined section object for the element interior. |

The plastic hinge length at end I (J) is equal to `lpI` (`lpJ`) and the associated force deformation response is defined by the `secI` (`secJ`). The force deformation
response of the element interior is defined by the `secE`.
Typically, the interior section is linear-elastic, but this is not necessary.

```
lpI = 0.1
lpJ = 0.2
beamIntegration('HingeMidpoint',tag,secI,lpI,secJ,lpJ,secE)
```
