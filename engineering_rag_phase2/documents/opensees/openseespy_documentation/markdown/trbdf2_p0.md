<!-- chunk_id: trbdf2_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/trbdf2.html",
 "title": "5.6.2.5. TRBDF2",
 "category": "general",
 "command": "trbdf2",
 "doc_section": "src",
 "rel_path": "src/trbdf2.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 642,
 "word_count": 78,
 "has_code": false,
 "has_table": false
} -->

## 5.6.2.5. TRBDF2

**integrator(*'TRBDF2'*)**

> Create a TRBDF2 integrator. The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. It does this in an attempt to conserve energy and momentum, something Newmark does not always do.

As opposed to dividing the time-step in 2 as outlined in the [Bathe2007](http://www.sciencedirect.com/science/article/pii/S0045794906003099), we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the [Bathe2007](http://www.sciencedirect.com/science/article/pii/S0045794906003099).
