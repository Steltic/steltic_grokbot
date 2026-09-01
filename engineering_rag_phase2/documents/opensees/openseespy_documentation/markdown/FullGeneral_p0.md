<!-- chunk_id: FullGeneral_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/FullGeneral.html",
 "title": "5.3.6. FullGeneral SOE",
 "category": "general",
 "command": "FullGeneral",
 "doc_section": "src",
 "rel_path": "src/FullGeneral.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 683,
 "word_count": 120,
 "has_code": false,
 "has_table": false
} -->

## 5.3.6. FullGeneral SOE

**system(*'FullGeneral'*)**

This command is used to construct a Full General linear system of equation object. As the name implies, the class utilizes NO space saving techniques to cut down on the amount of memory used. If the matrix is of size, nxn, then storage for an nxn array is sought from memory when the program runs. When a solution is required, the Lapack routines DGESV and DGETRS are used.

Note

This type of system should almost never be used! This is because it requires a lot more memory than every other solver and takes more time in the actal solving operation than any other solver. It is required if the user is interested in looking at the global system matrix.
