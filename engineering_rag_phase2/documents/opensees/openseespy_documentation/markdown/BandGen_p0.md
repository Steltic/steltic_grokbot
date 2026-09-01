<!-- chunk_id: BandGen_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BandGen.html",
 "title": "5.3.1. BandGeneral SOE",
 "category": "general",
 "command": "BandGen",
 "doc_section": "src",
 "rel_path": "src/BandGen.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 394,
 "word_count": 65,
 "has_code": false,
 "has_table": false
} -->

## 5.3.1. BandGeneral SOE

**system(*'BandGen'*)**

This command is used to construct a BandGeneralSOE linear system of equation object. As the name implies, this class is used for matrix systems which have a banded profile. The matrix is stored as shown below in a 1dimensional array of size equal to the bandwidth times the number of unknowns. When a solution is required, the Lapack routines DGBSV and SGBTRS are used.
