<!-- chunk_id: AxialSp_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/AxialSp.html",
 "title": "4.14.5.35. AxialSp Material",
 "category": "material",
 "command": "AxialSp",
 "doc_section": "src",
 "rel_path": "src/AxialSp.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1212,
 "word_count": 142,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.35. AxialSp Material

**uniaxialMaterial(*'AxialSp'*, *matTag*, *sce*, *fty*, *fcy*, *<bte*, *bty*, *bcy*, *fcr>*)**

This command is used to construct a uniaxial AxialSp material object. This material model produces axial stress-strain curve of elastomeric bearings.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `sce` ([float](https://docs.python.org/3/library/functions.html#float)) | compressive modulus |
| `fty` `fcy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield stress under tension ( `fty`) and compression ( `fcy`) (see note 1) |
| `bte` `bty` `bcy` ([float](https://docs.python.org/3/library/functions.html#float)) | reduction rate for tensile elastic range ( `bte`), tensile yielding ( `bty`) and compressive yielding ( `bcy`) (see note 1) |
| `fcr` ([float](https://docs.python.org/3/library/functions.html#float)) | target point stress (see note 1) |

Note

1. Input parameters are required to satisfy followings.

  `fcy` < 0.0 <    `fty`

  0.0 <=    `bty` <    `bte` <= 1.0

  0.0 <=    `bcy` <= 1.0

  `fcy` <=    `fcr` <= 0.0

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/AxialSp_Material)
