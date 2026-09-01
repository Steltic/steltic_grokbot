<!-- chunk_id: record_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/record.html",
 "title": "6.30. record command",
 "category": "general",
 "command": "record",
 "doc_section": "src",
 "rel_path": "src/record.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 484,
 "word_count": 87,
 "has_code": false,
 "has_table": false
} -->

## 6.30. record command

**record()**

This command is used to cause all the recorders to do a record on the current state of the model.

Note

A record is issued after every successfull static or transient analysis step. Sometimes the user may need the record to be issued on more occasions than this,
for example if the user is just looking to record the eigenvectors after an eigen command or for example the user wishes to include the state of the model
at time 0.0 before any analysis has been completed.
