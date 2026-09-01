<!-- chunk_id: UmfPack_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/UmfPack.html",
 "title": "5.3.5. UmfPack SOE",
 "category": "general",
 "command": "UmfPack",
 "doc_section": "src",
 "rel_path": "src/UmfPack.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 394,
 "word_count": 44,
 "has_code": false,
 "has_table": false
} -->

## 5.3.5. UmfPack SOE

**system(*'UmfPack'*)**

This command is used to construct a sparse system of equations which uses the [UmfPack](http://faculty.cse.tamu.edu/davis/suitesparse.html) solver.

**system(*'UmfPack'*, *'-useLongIndices'*)**

Pass `'-useLongIndices'` to use 64-bit indices in UMFPACK instead of the default 32-bit indices.

If symbolic or numeric factorization returns **-1**, try adding this option.
