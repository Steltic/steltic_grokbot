<!-- chunk_id: logFile_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/logFile.html",
 "title": "6.42. logFile command",
 "category": "general",
 "command": "logFile",
 "doc_section": "src",
 "rel_path": "src/logFile.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 532,
 "word_count": 66,
 "has_code": false,
 "has_table": true
} -->

## 6.42. logFile command

**logFile(*filename*, *'-append'*, *'-noEcho'*)**

Log all messages and errors in a file. By default,
all messages and errors print to terminal or Jupyter Notebook depending on
how Python was run.

| `filename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | name of the log file |
| --- | --- |
| `'-append'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | append to the file |
| `'-noEcho'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | do not print to terminal or Jupyter Notebook |
