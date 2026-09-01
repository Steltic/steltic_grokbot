<!-- chunk_id: HingeRadau_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/HingeRadau.html",
 "title": "4.13.13. HingeRadau",
 "category": "general",
 "command": "HingeRadau",
 "doc_section": "src",
 "rel_path": "src/HingeRadau.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 602,
 "word_count": 65,
 "has_code": false,
 "has_table": false
} -->

## 4.13.13. HingeRadau

**beamIntegration(*'HingeRadau'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

Create a HingeRadau beamIntegration object.
Modified two-point Gauss-Radau integration over each hinge region places an integration point at
the element ends and at 8/3 the hinge length inside the element. This approach represents
linear curvature distributions exactly and the characteristic length for softening plastic hinges is equal to the assumed palstic hinge length.

Arguments and examples see [HingeMidpoint](https://openseespydoc.readthedocs.io/en/latest/src/HingeMidpoint.html#hingemidpoint-beamintegration).
