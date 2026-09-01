<!-- chunk_id: KikuchiBearing_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/KikuchiBearing.html",
 "title": "4.2.6.8. KikuchiBearing Element",
 "category": "element",
 "command": "KikuchiBearing",
 "doc_section": "src",
 "rel_path": "src/KikuchiBearing.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3413,
 "word_count": 342,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.8. KikuchiBearing Element

This command is used to construct a KikuchiBearing element object, which is defined by two nodes. This element consists of multiple shear spring model (MSS) and multiple normal spring model (MNS).

**element(*'KikuchiBearing'*, *eleTag*, **eleNodes*, *'-shape'*, *shape*, *'-size'*, *size*, *totalRubber*, *<'-totalHeight'*, *totalHeight>*, *'-nMSS'*, *nMSS*, *'-matMSS'*, *matMSSTag*, *<'-limDisp'*, *limDisp>*, *'-nMNS'*, *nMNS*, *'-matMNS'*, *matMNSTag*, *<'-lambda'*, *lambda>*, *<'-orient'*, *<x1*, *x2*, *x3>*, *yp1*, *yp2*, *yp3>*, *<'-mass'*, *m>*, *<'-noPDInput'>*, *<'-noTilt'>*, *<'-adjustPDOutput'*, *ci*, *cj>*, *<'-doBalance'*, *limFo*, *limFi*, *nIter>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `shape` ([float](https://docs.python.org/3/library/functions.html#float)) | following shapes are available: round, square |
| `size` ([float](https://docs.python.org/3/library/functions.html#float)) | diameter (round shape), length of edge (square shape) |
| `totalRubber` ([float](https://docs.python.org/3/library/functions.html#float)) | total rubber thickness |
| `totalHeight` ([float](https://docs.python.org/3/library/functions.html#float)) | total height of the bearing (defaulut: distance between iNode and jNode) |
| `nMSS` ([int](https://docs.python.org/3/library/functions.html#int)) | number of springs in MSS = nMSS |
| `matMSSTag` ([int](https://docs.python.org/3/library/functions.html#int)) | matTag for MSS |
| `limDisp` ([float](https://docs.python.org/3/library/functions.html#float)) | minimum deformation to calculate equivalent coefficient of MSS (see note 1) |
| `nMNS` ([int](https://docs.python.org/3/library/functions.html#int)) | number of springs in MNS = nMNS*nMNS (for round and square shape) |
| `matMNSTag` ([int](https://docs.python.org/3/library/functions.html#int)) | matTag for MNS |
| `lambda` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter to calculate compression modulus distribution on MNS (see note 2) |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local x-axis |
| `yp1` `yp2` `yp3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining vector yp which lies in the local x-y plane for the element |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass |
| `'-noPDInput'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | not consider P-Delta moment |
| `'-noTilt'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | not consider tilt of rigid link |
| `ci` `cj` ([float](https://docs.python.org/3/library/functions.html#float)) | P-Delta moment adjustment for reaction force (default: `ci` =0.5, `cj` =0.5) |
| `limFo` `limFi` `nIter` ([float](https://docs.python.org/3/library/functions.html#float)) | tolerance of external unbalanced force ( `limFo`), tolorance of internal unbalanced force ( `limFi`), number of iterations to get rid of internal unbalanced force ( `nIter`) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/KikuchiBearing_Element)
