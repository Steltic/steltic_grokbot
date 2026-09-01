<!-- chunk_id: newmark_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/newmark.html",
 "title": "5.6.2.2. Newmark Method",
 "category": "general",
 "command": "newmark",
 "doc_section": "src",
 "rel_path": "src/newmark.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1242,
 "word_count": 154,
 "has_code": false,
 "has_table": true
} -->

## 5.6.2.2. Newmark Method

**integrator(*'Newmark'*, *gamma*, *beta*, *'-form'*, *form*)**

Create a Newmark integrator.

| `gamma` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\gamma\) factor. |
| --- | --- |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\beta\) factor. |
| `form` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Flag to indicate which variable to be used as primary variable (optional) `'D'` – displacement (default) `'V'` – velocity `'A'` – acceleration |

1. If the accelerations are chosen as the unknowns and \(\beta\) is chosen as 0, the formulation results in the fast but conditionally stable explicit Central Difference method. Otherwise the method is implicit and requires an iterative solution process.
2. Two common sets of choices are

  1. Average Acceleration Method (\(\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{4}\))
  2. Linear Acceleration Method (\(\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{6}\))
3. \(\gamma > \tfrac{1}{2}\) results in numerical damping proportional to \(\gamma - \tfrac{1}{2}\)
4. The method is second order accurate if and only if \(\gamma=\tfrac{1}{2}\)
5. The method is unconditionally stable for  \(\beta >= \frac{\gamma}{2} >= \tfrac{1}{4}\)
