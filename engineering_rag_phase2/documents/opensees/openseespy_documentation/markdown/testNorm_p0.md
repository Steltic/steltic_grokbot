<!-- chunk_id: testNorm_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/testNorm.html",
 "title": "6.40. testNorm command",
 "category": "general",
 "command": "testNorm",
 "doc_section": "src",
 "rel_path": "src/testNorm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 250,
 "word_count": 42,
 "has_code": false,
 "has_table": false
} -->

## 6.40. testNorm command

**testNorm()**

Returns the norms from the convergence test for the last analysis step.

Note

The size of norms will be equal to the max number of iterations specified. The first `testIter` of these will be non-zero, the remaining ones will be zero.
