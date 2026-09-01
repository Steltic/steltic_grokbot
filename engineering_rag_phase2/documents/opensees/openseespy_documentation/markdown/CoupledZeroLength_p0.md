<!-- chunk_id: CoupledZeroLength_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/CoupledZeroLength.html",
 "title": "4.2.1.4. CoupledZeroLength Element",
 "category": "element",
 "command": "CoupledZeroLength",
 "doc_section": "src",
 "rel_path": "src/CoupledZeroLength.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 915,
 "word_count": 80,
 "has_code": false,
 "has_table": true
} -->

## 4.2.1.4. CoupledZeroLength Element

**element(*'CoupledZeroLength'*, *eleTag*, **eleNodes*, *dirn1*, *dirn2*, *matTag*, *<rFlag=1>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `matTag` ([float](https://docs.python.org/3/library/functions.html#float)) | tags associated with previously-defined UniaxialMaterial |
| `dirn1` `dirn2` ([int](https://docs.python.org/3/library/functions.html#int)) | the two directions, 1 through ndof. |
| `rFlag` ([float](https://docs.python.org/3/library/functions.html#float)) | optional, default = 0 `rFlag` = 0 NO RAYLEIGH DAMPING (default) `rFlag` = 1 include rayleigh damping |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/CoupledZeroLength_Element)
