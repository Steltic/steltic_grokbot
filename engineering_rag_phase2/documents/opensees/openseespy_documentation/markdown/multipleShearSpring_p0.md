<!-- chunk_id: multipleShearSpring_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/multipleShearSpring.html",
 "title": "4.2.6.7. MultipleShearSpring Element",
 "category": "element",
 "command": "multipleShearSpring",
 "doc_section": "src",
 "rel_path": "src/multipleShearSpring.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2030,
 "word_count": 223,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.7. MultipleShearSpring Element

This command is used to construct a multipleShearSpring (MSS) element object, which is defined by two nodes. This element consists of a series of identical shear springs arranged radially to represent the isotropic behavior in the local y-z plane.

**element(*'multipleShearSpring'*, *eleTag*, **eleNodes*, *nSpring*, *'-mat'*, *matTag*, *<'-lim'*, *lim>*, *<'-orient'*, *<x1*, *x2*, *x3>*, *yp1*, *yp2*, *yp3>*, *<'-mass'*, *mass>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `nSpring` ([int](https://docs.python.org/3/library/functions.html#int)) | number of springs |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial object |
| `lim` ([float](https://docs.python.org/3/library/functions.html#float)) | minimum deformation to calculate equivalent coefficient (see note 1) |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local x-axis |
| `yp1` `yp2` `yp3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining vector yp which lies in the local x-y plane for the element |
| `mass` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass |

Note

If `dsp` is positive and the shear deformation of MSS exceeds    `dsp`, this element calculates equivalent coefficient to adjust force and stiffness of MSS. The adjusted MSS force and stiffness reproduce the behavior of the previously defined uniaxial material under monotonic loading in every direction. If    `dsp` is zero, the element does not calculate the equivalent coefficient.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/MultipleShearSpring_Element)
