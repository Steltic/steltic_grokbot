<!-- chunk_id: eleResponse_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/eleResponse.html",
 "title": "6.7. eleResponse command",
 "category": "general",
 "command": "eleResponse",
 "doc_section": "src",
 "rel_path": "src/eleResponse.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 465,
 "word_count": 60,
 "has_code": false,
 "has_table": true
} -->

## 6.7. eleResponse command

**eleResponse(*eleTag*, **args*)**

This command is used to obtain the same element quantities as those obtained from the element recorder at a particular time step.

| `eletag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag. |
| --- | --- |
| `args` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | same arguments as those specified in element recorder. These arguments are specific to the type of element being used. |
