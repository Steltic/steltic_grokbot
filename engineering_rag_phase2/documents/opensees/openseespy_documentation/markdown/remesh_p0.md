<!-- chunk_id: remesh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/remesh.html",
 "title": "8.2. remesh command",
 "category": "general",
 "command": "remesh",
 "doc_section": "src",
 "rel_path": "src/remesh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 960,
 "word_count": 168,
 "has_code": false,
 "has_table": true
} -->

## 8.2. remesh command

**remesh(*alpha=-1.0*)**

- \(\alpha \ge 0\) for updating moving mesh.
- \(\alpha < 0\) for updating background mesh.

If there are nodes shared by different mesh in the domain,
the principles to decide what element should be used for
a triangle:

1. If all 3 nodes share the same mesh, use that mesh for the triangle.
2. If all 3 nodes share more than one mesh, use the mesh with `eleArgs` defined
  and lowest `id`.
3. If all 3 nodes are in different mesh, use the mesh with lowest `id`.
4. If the selected mesh `id` >= 0, skip the triangle.
5. If the selected mesh has no `eleArgs`, skip the triangle.

| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameter for the \(\alpha\) method to construct a mesh from the node cloud of moving meshes. (optional) \(\alpha = 0\) : no elements are created large \(\alpha\) : all elements in the convex hull are created \(1.0 < \alpha < 2.0\) : usually gives a good shape |
| --- | --- |
