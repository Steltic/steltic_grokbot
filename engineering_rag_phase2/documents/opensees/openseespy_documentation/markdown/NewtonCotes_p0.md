<!-- chunk_id: NewtonCotes_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/NewtonCotes.html",
 "title": "4.13.3. NewtonCotes",
 "category": "general",
 "command": "NewtonCotes",
 "doc_section": "src",
 "rel_path": "src/NewtonCotes.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 501,
 "word_count": 51,
 "has_code": true,
 "has_table": false
} -->

## 4.13.3. NewtonCotes

**beamIntegration(*'NewtonCotes'*, *tag*, *secTag*, *N*)**

**beamIntegration(*'NewtonCotes'*, *tag*, *N*, **secTags*)**

Newton–Cotes integration: points uniformly spaced along the element, **including** both ends. Order of accuracy: \(N-1\).

**Prismatic:** `('NewtonCotes', tag, secTag, N)`.

**Non-prismatic:** `('NewtonCotes', tag, N, *secTags)`.

Example

```
import openseespy.opensees as ops

ops.beamIntegration('NewtonCotes', 2, 1, 6)
ops.beamIntegration('NewtonCotes', 3, 4, 1, 2, 2, 1)
```
