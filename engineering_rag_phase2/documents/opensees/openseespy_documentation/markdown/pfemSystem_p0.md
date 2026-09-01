<!-- chunk_id: pfemSystem_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pfemSystem.html",
 "title": "8.4. PFEM SOE",
 "category": "analysis",
 "command": "pfemSystem",
 "doc_section": "src",
 "rel_path": "src/pfemSystem.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 304,
 "word_count": 43,
 "has_code": false,
 "has_table": true
} -->

## 8.4. PFEM SOE

**system(*'PFEM'*, *'-compressible'*, *'-mumps'*)**

Create a incompressible PFEM system of equations using the Umfpack solver

| `-compressible` | Solve using a quasi-incompressible formulation. (optional) |
| --- | --- |
| `-mumps` | Solve using the MUMPS solver. (optional, not supported on Windows) |
