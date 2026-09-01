<!-- chunk_id: UserHinge_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/UserHinge.html",
 "title": "4.13.11. UserHinge",
 "category": "general",
 "command": "UserHinge",
 "doc_section": "src",
 "rel_path": "src/UserHinge.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2114,
 "word_count": 212,
 "has_code": true,
 "has_table": true
} -->

## 4.13.11. UserHinge

**beamIntegration(*'UserHinge'*, *tag*, *secETag*, *npL*, **secsLTags*, **locsL*, **wtsL*, *npR*, **secsRTags*, **locsR*, **wtsR*)**

Create a UserHinge beamIntegration object.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the beam integration |
| --- | --- |
| `secE` ([int](https://docs.python.org/3/library/functions.html#int)) | A previous-defined section tags for element interior |
| `npI` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points along the hinge at end I |
| `secsI` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list of previous-defined section tags for hinge at end I |
| `locsI` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | A list of locations of integration points for hinge at end I |
| `wtsI` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | A list of weights of integration points for hinge at end I |
| `npJ` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points along the hinge at end J |
| `secsJ` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list of previous-defined section tags for hinge at end J |
| `locsJ` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | A list of locations of integration points for hinge at end J |
| `wtsJ` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | A list of weights of integration points for hinge at end J |

```
tag = 1
secE = 5

npI = 2
secsI = [1,2]
locsI = [0.1,0.2]
wtsI = [0.1,0.05]

npJ = 2
secsJ = [3,4]
locsJ = [0.8,0.9]
wtsJ = [0.05,0.1]

beamIntegration('UserHinge',tag,secE,npI,*secsI,*locsI,*wtsI,npJ,*secsJ,*locsJ,*wtsJ)
```
