<!-- chunk_id: ProfileSPD_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ProfileSPD.html",
 "title": "5.3.3. ProfileSPD SOE",
 "category": "general",
 "command": "ProfileSPD",
 "doc_section": "src",
 "rel_path": "src/ProfileSPD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 404,
 "word_count": 65,
 "has_code": false,
 "has_table": false
} -->

## 5.3.3. ProfileSPD SOE

**system(*'ProfileSPD'*)**

This command is used to construct a profileSPDSOE linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems. The matrix is stored as shown below in a 1 dimensional array with only those values below the first non-zero row in any column being stored. This is sometimes also referred to as a skyline storage scheme.
