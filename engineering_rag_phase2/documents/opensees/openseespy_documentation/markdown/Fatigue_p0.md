<!-- chunk_id: Fatigue_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Fatigue.html",
 "title": "4.14.5.12. Fatigue Material",
 "category": "material",
 "command": "Fatigue",
 "doc_section": "src",
 "rel_path": "src/Fatigue.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1278,
 "word_count": 133,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.12. Fatigue Material

**uniaxialMaterial(*'Fatigue'*, *matTag*, *otherTag*, *'-E0'*, *E0=0.191*, *'-m'*, *m=-0.458*, *'-min'*, *min=-1e16*, *'-max'*, *max=1e16*)**

The fatigue material uses a modified rainflow cycle counting algorithm to accumulate damage in a material using Miner’s Rule. Element stress/strain relationships become zero when fatigue life is exhausted.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `otherTag` ([float](https://docs.python.org/3/library/functions.html#float)) | Unique material object integer tag for the material that is being wrapped |
| `E0` ([float](https://docs.python.org/3/library/functions.html#float)) | Value of strain at which one cycle will cause failure (default 0.191) |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | Slope of Coffin-Manson curve in log-log space (default -0.458) |
| `min` ([float](https://docs.python.org/3/library/functions.html#float)) | Global minimum value for strain or deformation (default -1e16) |
| `max` ([float](https://docs.python.org/3/library/functions.html#float)) | Global maximum value for strain or deformation (default 1e16) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Fatigue_Material)
