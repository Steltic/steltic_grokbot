<!-- chunk_id: Radau_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Radau.html",
 "title": "4.13.4. Radau",
 "category": "general",
 "command": "Radau",
 "doc_section": "src",
 "rel_path": "src/Radau.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 645,
 "word_count": 68,
 "has_code": true,
 "has_table": false
} -->

## 4.13.4. Radau

**beamIntegration(*'Radau'*, *tag*, *secTag*, *N*)**

**beamIntegration(*'Radau'*, *tag*, *N*, **secTags*)**

Gauss–Radau integration: uncommon in force-based elements because only **one** end holds an integration point; useful as building block for plastic-hinge schemes. Places `N` Gauss–Radau points with a point at node **I**. Order of accuracy: \(2N-2\).

**Prismatic / non-prismatic:** same pattern as [Lobatto](https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html#lobatto-beamintegration).

Example

```
import openseespy.opensees as ops

ops.beamIntegration('Radau', 2, 1, 6)
ops.beamIntegration('Radau', 3, 4, 1, 2, 2, 1)
```
