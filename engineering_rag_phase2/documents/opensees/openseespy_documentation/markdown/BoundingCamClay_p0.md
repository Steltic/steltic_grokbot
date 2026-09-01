<!-- chunk_id: BoundingCamClay_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BoundingCamClay.html",
 "title": "4.15.1.8. BoundingCamClay",
 "category": "general",
 "command": "BoundingCamClay",
 "doc_section": "src",
 "rel_path": "src/BoundingCamClay.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1765,
 "word_count": 172,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.8. BoundingCamClay

**nDMaterial(*'BoundingCamClay'*, *matTag*, *massDensity*, *C*, *bulkMod*, *OCR*, *mu_o*, *alpha*, *lambda*, *h*, *m*)**

This command is used to construct a multi-dimensional bounding surface Cam Clay material object after Borja et al. (2001).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `massDensity` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density |
| `C` ([float](https://docs.python.org/3/library/functions.html#float)) | ellipsoidal axis ratio (defines shape of ellipsoidal loading/bounding surfaces) |
| `bulkMod` ([float](https://docs.python.org/3/library/functions.html#float)) | initial bulk modulus |
| `OCR` ([float](https://docs.python.org/3/library/functions.html#float)) | overconsolidation ratio |
| `mu_o` ([float](https://docs.python.org/3/library/functions.html#float)) | initial shear modulus |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | pressure-dependency parameter for modulii (greater than or equal to zero) |
| `lambda` ([float](https://docs.python.org/3/library/functions.html#float)) | soil compressibility index for virgin loading |
| `h` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening parameter for plastic response inside of bounding surface (if h = 0, no hardening) |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening parameter (exponent) for plastic response inside of bounding surface (if m = 0, only linear hardening) |

The material formulations for the BoundingCamClay object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`

See also for [information](http://opensees.berkeley.edu/wiki/index.php/Bounding_Cam_Clay)
