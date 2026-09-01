<!-- chunk_id: setElementRayleighDampingFactors_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/setElementRayleighDampingFactors.html",
 "title": "7.19. setElementRayleighDampingFactors command",
 "category": "element",
 "command": "setElementRayleighDampingFactors",
 "doc_section": "src",
 "rel_path": "src/setElementRayleighDampingFactors.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 844,
 "word_count": 73,
 "has_code": false,
 "has_table": true
} -->

## 7.19. setElementRayleighDampingFactors command

**setElementRayleighDampingFactors(*eleTag*, *alphaM*, *betaK*, *betaK0*, *betaKc*)**

Set the [`rayleigh()`](https://openseespydoc.readthedocs.io/en/latest/src/reyleigh.html#rayleigh) damping for an element.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag |
| --- | --- |
| `alphaM` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements or nodes mass matrix |
| `betaK` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements current stiffness matrix. |
| `betaK0` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements initial stiffness matrix. |
| `betaKc` ([float](https://docs.python.org/3/library/functions.html#float)) | factor applied to elements committed stiffness matrix. |
