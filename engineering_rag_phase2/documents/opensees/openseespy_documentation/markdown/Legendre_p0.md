<!-- chunk_id: Legendre_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Legendre.html",
 "title": "4.13.2. Legendre",
 "category": "general",
 "command": "Legendre",
 "doc_section": "src",
 "rel_path": "src/Legendre.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 692,
 "word_count": 66,
 "has_code": true,
 "has_table": false
} -->

## 4.13.2. Legendre

**beamIntegration(*'Legendre'*, *tag*, *secTag*, *N*)**

**beamIntegration(*'Legendre'*, *tag*, *N*, **secTags*)**

Gauss–Legendre integration: more accurate than Lobatto but **no** points at the element ends by default, so less common in force-based elements. Order of accuracy: \(2N-1\).

**Prismatic:** `beamIntegration('Legendre', tag, secTag, N)`.

**Non-prismatic:** `beamIntegration('Legendre', tag, N, secTag1, …, secTagN)`.

Arguments: see [Lobatto](https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html#lobatto-beamintegration).

Example

```
import openseespy.opensees as ops

ops.beamIntegration('Legendre', 2, 1, 6)
ops.beamIntegration('Legendre', 3, 4, 1, 2, 2, 1)
```
