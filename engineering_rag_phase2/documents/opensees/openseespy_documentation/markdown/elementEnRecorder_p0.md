<!-- chunk_id: elementEnRecorder_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elementEnRecorder.html",
 "title": "6.31.4. element envelope recorder command",
 "category": "element",
 "command": "elementEnRecorder",
 "doc_section": "src",
 "rel_path": "src/elementEnRecorder.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3142,
 "word_count": 384,
 "has_code": false,
 "has_table": true
} -->

## 6.31.4. element envelope recorder command

**recorder(*'EnvelopeElement'*, *'-file'*, *filename*, *'-xml'*, *filename*, *'-binary'*, *filename*, *'-precision'*, *nSD=6*, *'-timeSeries'*, *tsTag*, *'-time'*, *'-dT'*, *deltaT=0.0*, *'-closeOnWrite'*, *'-ele'*, **eleTags=[]*, *'-eleRange'*, *startEle*, *endEle*, *'-region'*, *regionTag*, **args*)**

The Envelope Element recorder type records the response of a number of elements at every converged step. The response recorded is element-dependent and also depends on the arguments which are passed to the setResponse() element method. When the object is terminated, through the use of a wipe, exit, or remove the object will output the min, max and absolute max values on 3 seperate lines of the output file for each quantity.

| `filename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | name of file to which output is sent. file output is either in xml format (`'-xml'` option), textual (`'-file'` option) or binary (`'-binary'` option) which must pre-exist. |
| --- | --- |
| `nSD` ([int](https://docs.python.org/3/library/functions.html#int)) | number of significant digits (optional) |
| `'-time'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | using this option places domain time in first entry of each data line, default is to have time ommitted, (optional) |
| `'-closeOnWrite'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | using this option will instruct the recorder to invoke a close on the data handler after every timestep. If this is a file it will close the file on every step and then re-open it for the next step. Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) |
| `deltaT` ([float](https://docs.python.org/3/library/functions.html#float)) | time interval for recording. will record when next step is `deltaT` greater than last recorder step. (optional, default: records at every time step) |
| `tsTag` ([int](https://docs.python.org/3/library/functions.html#int)) | the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional) |
| `eleTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | list of tags of elements whose response is being recorded (optional) |
| `startEle` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for start node whose response is being recorded (optional) |
| `endEle` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for end node whose response is being recorded (optional) |
| `regionTag` ([int](https://docs.python.org/3/library/functions.html#int)) | a region tag; to specify all nodes in the previously defined region. (optional) |
| `args` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | arguments which are passed to the setResponse() element method |

Note

The setResponse() element method is dependent on the element type, and is described with the [`element()`](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthContact.html#id0) Command.
