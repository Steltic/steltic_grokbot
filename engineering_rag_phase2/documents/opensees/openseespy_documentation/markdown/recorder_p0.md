<!-- chunk_id: recorder_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/recorder.html",
 "title": "6.31. recorder command",
 "category": "output",
 "command": "recorder",
 "doc_section": "src",
 "rel_path": "src/recorder.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1369,
 "word_count": 116,
 "has_code": false,
 "has_table": true
} -->

## 6.31. recorder command

**recorder(*recorderType*, **recorderArgs*)**

This command is used to generate a recorder object which is to monitor what is happening during the analysis and generate output for the user.

Return:

- >0 an integer tag that can be used as a handle on the recorder for the remove recorder commmand.
- -1 recorder command failed if integer -1 returned.

| `recorderType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | recorder type |
| --- | --- |
| `recorderArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of recorder arguments |

The following contain information about available `recorderType`:

1. [node recorder command](https://openseespydoc.readthedocs.io/en/latest/src/nodeRecorder.html)
2. [node envelope recorder command](https://openseespydoc.readthedocs.io/en/latest/src/nodeEnRecorder.html)
3. [element recorder command](https://openseespydoc.readthedocs.io/en/latest/src/elementRecorder.html)
4. [element envelope recorder command](https://openseespydoc.readthedocs.io/en/latest/src/elementEnRecorder.html)
5. [pvd recorder command](https://openseespydoc.readthedocs.io/en/latest/src/pvdRecorder.html)
6. [background recorder command](https://openseespydoc.readthedocs.io/en/latest/src/bgpvdRecorder.html)
7. [Collapse Recorder command](https://openseespydoc.readthedocs.io/en/latest/src/CollapseRecorder.html)
