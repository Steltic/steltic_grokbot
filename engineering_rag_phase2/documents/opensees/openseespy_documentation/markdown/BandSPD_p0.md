<!-- chunk_id: BandSPD_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BandSPD.html",
 "title": "5.3.2. BandSPD SOE",
 "category": "general",
 "command": "BandSPD",
 "doc_section": "src",
 "rel_path": "src/BandSPD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 423,
 "word_count": 69,
 "has_code": false,
 "has_table": false
} -->

## 5.3.2. BandSPD SOE

**system(*'BandSPD'*)**

This command is used to construct a BandSPDSOE linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems which have a banded profile. The matrix is stored as shown below in a 1 dimensional array of size equal to the (bandwidth/2) times the number of unknowns. When a solution is required, the Lapack routines DPBSV and DPBTRS are used.
