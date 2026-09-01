<!-- chunk_id: bgpvdRecorder_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/bgpvdRecorder.html",
 "title": "6.31.6. background recorder command",
 "category": "output",
 "command": "bgpvdRecorder",
 "doc_section": "src",
 "rel_path": "src/bgpvdRecorder.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1037,
 "word_count": 105,
 "has_code": false,
 "has_table": true
} -->

## 6.31.6. background recorder command

**recorder(*'BgPVD'*, *filename*, *'-precision'*, *precision=10*, *'-dT'*, *dT=0.0*, **res*)**

Create a PVD recorder for background mesh. This recorder is same as the
PVD recorder, but will be automatically called in background mesh and
is able to record wave height and velocity.

| `filename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the name for `filename.pvd` and `filename/` directory, which must pre-exist. |
| --- | --- |
| `precision` ([int](https://docs.python.org/3/library/functions.html#int)) | the precision of data. (optional) |
| `dT` ([float](https://docs.python.org/3/library/functions.html#float)) | the time interval for recording. (optional) |
| `res` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([str](https://docs.python.org/3/library/stdtypes.html#str))) | a list of ([str](https://docs.python.org/3/library/stdtypes.html#str)) of responses to be recorded, (optional) `'disp'` `'vel'` `'accel'` `'incrDisp'` `'reaction'` `'pressure'` `'unbalancedLoad'` `'mass'` `'eigen'` |
