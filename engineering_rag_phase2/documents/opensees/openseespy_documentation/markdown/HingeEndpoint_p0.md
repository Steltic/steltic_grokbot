<!-- chunk_id: HingeEndpoint_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/HingeEndpoint.html",
 "title": "4.13.15. HingeEndpoint",
 "category": "general",
 "command": "HingeEndpoint",
 "doc_section": "src",
 "rel_path": "src/HingeEndpoint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1190,
 "word_count": 121,
 "has_code": false,
 "has_table": true
} -->

## 4.13.15. HingeEndpoint

**beamIntegration(*'HingeEndpoint'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

Create a HingeEndpoint beamIntegration object.
Endpoint integration over each hinge region moves the integration points to the element ends;
however, there is a large integration error for linear curvature distributions along the element.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the beam integration. |
| --- | --- |
| `secI` ([int](https://docs.python.org/3/library/functions.html#int)) | A previous-defined section object for hinge at I. |
| `lpI` ([float](https://docs.python.org/3/library/functions.html#float)) | The plastic hinge length at I. |
| `secJ` ([int](https://docs.python.org/3/library/functions.html#int)) | A previous-defined section object for hinge at J. |
| `lpJ` ([float](https://docs.python.org/3/library/functions.html#float)) | The plastic hinge length at J. |
| `secE` ([int](https://docs.python.org/3/library/functions.html#int)) | A previous-defined section object for the element interior. |

Arguments and examples see [HingeMidpoint](https://openseespydoc.readthedocs.io/en/latest/src/HingeMidpoint.html#hingemidpoint-beamintegration).
