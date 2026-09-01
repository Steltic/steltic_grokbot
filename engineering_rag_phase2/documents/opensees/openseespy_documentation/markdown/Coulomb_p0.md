<!-- chunk_id: Coulomb_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Coulomb.html",
 "title": "4.17.1. Coulomb",
 "category": "general",
 "command": "Coulomb",
 "doc_section": "src",
 "rel_path": "src/Coulomb.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 469,
 "word_count": 50,
 "has_code": false,
 "has_table": true
} -->

## 4.17.1. Coulomb

**frictionModel(*'Coulomb'*, *frnTag*, *mu*)**

This command is used to construct a [Coulomb friction](http://en.wikipedia.org/wiki/Friction) model object. Coulomb’s Law of Friction states that kinetic friction is independent of the sliding velocity.

| `frnTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique friction model tag |
| --- | --- |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficient of friction |
