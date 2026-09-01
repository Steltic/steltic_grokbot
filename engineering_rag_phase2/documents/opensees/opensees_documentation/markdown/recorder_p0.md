<!-- chunk_id: recorder_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/recorder.html",
 "title": "3.3.1. recorder Command",
 "category": "command_manual",
 "manual_group": "output",
 "command": "recorder",
 "doc_section": "user/manual/output",
 "rel_path": "user/manual/output/recorder.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1470,
 "word_count": 147,
 "has_code": false,
 "has_table": false
} -->

## 3.3.1. recorder Command

This command is used to generate a recorder object which is to monitor what is happening during the analysis and generate output for the user. The output may go to the screen, files, databases, or to remote processes through the TCP/IP options.

**recorder $recorderType $arg1 $arg2 ...**

The type of recorder created and the additional arguments required depends on the $recorderType provided in the command.

1. Recorders to record Node Information

- [3.3.1.1. Node Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/NodeRecorder.html)
- [3.3.1.2. Envelope Node Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/EnvelopeNodeRecorder.html)

2. Recorders to record Element Information

- [3.3.1.3. Element Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/ElementRecorder.html)

4. Recorders for whole-model output

- [3.3.1.4. PVD Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/PVDRecorder.html)
- [3.3.1.5. MPCO Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/MPCORecorder.html)
- [3.3.1.6. GMSH Recorder](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/GmshRecorder.html)

Note

The function returns a value:

**>0** an integer tag that can be used as a handle on the recorder for the remove a recorder in the remove.

**-1** recorder command failed if integer -1 returned.

Code Developed by: **fmk**
