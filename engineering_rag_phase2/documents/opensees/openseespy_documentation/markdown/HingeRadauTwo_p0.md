<!-- chunk_id: HingeRadauTwo_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/HingeRadauTwo.html",
 "title": "4.13.14. HingeRadauTwo",
 "category": "general",
 "command": "HingeRadauTwo",
 "doc_section": "src",
 "rel_path": "src/HingeRadauTwo.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 650,
 "word_count": 72,
 "has_code": false,
 "has_table": false
} -->

## 4.13.14. HingeRadauTwo

**beamIntegration(*'HingeRadauTwo'*, *tag*, *secI*, *lpI*, *secJ*, *lpJ*, *secE*)**

Create a HingeRadauTwo beamIntegration object.
Two-point Gauss-Radau integration over each hinge region places an integration
point at the element ends and at 2/3 the hinge length inside the element. This approach
represents linear curvature distributions exactly; however, the characteristic length for softening
plastic hinges is not equal to the assumed plastic hinge length (equals 1/4 of the plastic hinge length).

Arguments and examples see [HingeMidpoint](https://openseespydoc.readthedocs.io/en/latest/src/HingeMidpoint.html#hingemidpoint-beamintegration).
