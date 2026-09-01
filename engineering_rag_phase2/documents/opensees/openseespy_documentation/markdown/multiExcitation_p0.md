<!-- chunk_id: multiExcitation_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/multiExcitation.html",
 "title": "4.8.3. Multi-Support Excitation Pattern",
 "category": "pattern",
 "command": "multiExcitation",
 "doc_section": "src",
 "rel_path": "src/multiExcitation.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1261,
 "word_count": 113,
 "has_code": false,
 "has_table": true
} -->

## 4.8.3. Multi-Support Excitation Pattern

**pattern(*'MultipleSupport'*, *patternTag*)**

The Multi-Support pattern allows similar or different prescribed ground motions to be input at various supports in the structure. In OpenSees, the prescribed motion is applied using single-point constraints, the single-point constraints taking their constraint value from user created ground motions.

| `patternTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying pattern |
| --- | --- |

Note

1. The results for the responses at the nodes are the ABSOLUTE values, and not relative values as in the case of a UniformExciatation.
2. The non-homogeneous single point constraints require an appropriate choice of constraint handler.

- [4.8.3.1. Plain Ground Motion](https://openseespydoc.readthedocs.io/en/latest/src/groundMotion.html)

  - [`groundMotion()`](https://openseespydoc.readthedocs.io/en/latest/src/groundMotion.html#groundMotion)
- [4.8.3.2. Interpolated Ground Motion](https://openseespydoc.readthedocs.io/en/latest/src/interpolatedGroundMotion.html)
- [4.8.3.3. Imposed Motion](https://openseespydoc.readthedocs.io/en/latest/src/imposedMotion.html)

  - [`imposedMotion()`](https://openseespydoc.readthedocs.io/en/latest/src/imposedMotion.html#imposedMotion)
