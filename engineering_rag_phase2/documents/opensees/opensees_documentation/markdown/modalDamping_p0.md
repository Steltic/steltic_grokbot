<!-- chunk_id: modalDamping_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/modalDamping.html",
 "title": "3.1.13.2. Modal Damping Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "modalDamping",
 "doc_section": "user/manual/model/damping",
 "rel_path": "user/manual/model/damping/modalDamping.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 436,
 "word_count": 64,
 "has_code": true,
 "has_table": true
} -->

## 3.1.13.2. Modal Damping Command

**modalDamping $factor**

| Argument | Type | Description |
| --- | --- | --- |
| $factor | *float* | damping factor. |

Example:

1. **Tcl Code**

```
set N 2 ;# Number of modes for modal damping
eigen $N

modalDamping 0.05 0.02 ;# 5% in mode 1, 2% in mode 2
```

Further reading about Modal Damping can be seen in [[ChopraMcKenna2015]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping.html#chopramckenna2015)
