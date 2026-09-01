<!-- chunk_id: AxialSpHD_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/AxialSpHD.html",
 "title": "4.14.5.36. AxialSpHD Material",
 "category": "material",
 "command": "AxialSpHD",
 "doc_section": "src",
 "rel_path": "src/AxialSpHD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1437,
 "word_count": 163,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.36. AxialSpHD Material

**uniaxialMaterial(*'AxialSpHD'*, *matTag*, *sce*, *fty*, *fcy*, *<bte*, *bty*, *bth*, *bcy*, *fcr*, *ath>*)**

This command is used to construct a uniaxial AxialSpHD material object. This material model produces axial stress-strain curve of elastomeric bearings including hardening behavior.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `sce` ([float](https://docs.python.org/3/library/functions.html#float)) | compressive modulus |
| `fty` `fcy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield stress under tension (`fty`) and compression (`fcy`) (see note 1) |
| `bte` `bty` `bth` `bcy` ([float](https://docs.python.org/3/library/functions.html#float)) | reduction rate for tensile elastic range (`bte`), tensile yielding (`bty`), tensile hardening ( `bth`) and compressive yielding (`bcy`) (see note 1) |
| `fcr` ([float](https://docs.python.org/3/library/functions.html#float)) | target point stress (see note 1) |
| `ath` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening strain ratio to yield strain |

Note

1. Input parameters are required to satisfy followings.

  `fcy` < 0.0 <    `fty`

  0.0 <=    `bty` <    `bth` <    `bte` <= 1.0

  0.0 <=    `bcy` <= 1.0

  `fcy` <=    `fcr` <= 0.0

  1.0 <=    `ath`

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/AxialSpHD_Material)
