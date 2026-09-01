<!-- chunk_id: nodeEnRecorder_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nodeEnRecorder.html",
 "title": "6.31.2. node envelope recorder command",
 "category": "output",
 "command": "nodeEnRecorder",
 "doc_section": "src",
 "rel_path": "src/nodeEnRecorder.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3038,
 "word_count": 347,
 "has_code": false,
 "has_table": true
} -->

## 6.31.2. node envelope recorder command

**recorder(*'EnvelopeNode'*, *'-file'*, *filename*, *'-xml'*, *filename*, *'-precision'*, *nSD=6*, *'-timeSeries'*, *tsTag*, *'-time'*, *'-dT'*, *deltaT=0.0*, *'-closeOnWrite'*, *'-node'*, **nodeTags=[]*, *'-nodeRange'*, *startNode*, *endNode*, *'-region'*, *regionTag*, *'-dof'*, **dofs=[]*, *respType*)**

The EnvelopeNode recorder type records the min, max and absolute max of a number of nodal response quantaties.

| `filename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | name of file to which output is sent. file output is either in xml format (`'-xml'` option), or textual (`'-file'` option) which must pre-exist. |
| --- | --- |
| `nSD` ([int](https://docs.python.org/3/library/functions.html#int)) | number of significant digits (optional) |
| `'-time'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | using this option places domain time in first entry of each data line, default is to have time ommitted, (optional) |
| `'-closeOnWrite'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | using this option will instruct the recorder to invoke a close on the data handler after every timestep. If this is a file it will close the file on every step and then re-open it for the next step. Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) |
| `deltaT` ([float](https://docs.python.org/3/library/functions.html#float)) | time interval for recording. will record when next step is `deltaT` greater than last recorder step. (optional, default: records at every time step) |
| `tsTag` ([int](https://docs.python.org/3/library/functions.html#int)) | the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional) |
| `nodeTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | list of tags of nodes whose response is being recorded (optional) |
| `startNode` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for start node whose response is being recorded (optional) |
| `endNode` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for end node whose response is being recorded (optional) |
| `regionTag` ([int](https://docs.python.org/3/library/functions.html#int)) | a region tag; to specify all nodes in the previously defined region. (optional) |
| `dofs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | the specified dof at the nodes whose response is requested. |
| `resType` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([str](https://docs.python.org/3/library/stdtypes.html#str))) | a string indicating response required. Response types are given in table below `'disp'` displacement `'vel'` velocity `'accel'` acceleration `'incrDisp'` incremental displacement `'reaction'` nodal reaction `'eigen i'` eigenvector for mode i |
