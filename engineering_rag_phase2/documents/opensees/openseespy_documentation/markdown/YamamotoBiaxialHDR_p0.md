<!-- chunk_id: YamamotoBiaxialHDR_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/YamamotoBiaxialHDR.html",
 "title": "4.2.6.9. YamamotoBiaxialHDR Element",
 "category": "element",
 "command": "YamamotoBiaxialHDR",
 "doc_section": "src",
 "rel_path": "src/YamamotoBiaxialHDR.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1943,
 "word_count": 191,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.9. YamamotoBiaxialHDR Element

This command is used to construct a YamamotoBiaxialHDR element object, which is defined by two nodes. This element can be used to represent the isotropic behavior of high-damping rubber bearing in the local y-z plane.

**element(*'YamamotoBiaxialHDR'*, *eleTag*, **eleNodes*, *Tp*, *DDo*, *DDi*, *Hr*, *<'-coRS`*, *cr*, *cs>*, *<'-orient`*, **vecx*, **vecyp>*, *<'-mass`*, *m>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `Tp` ([int](https://docs.python.org/3/library/functions.html#int)) | compound type = 1 : X0.6R manufactured by Bridgestone corporation. |
| `DDo` ([float](https://docs.python.org/3/library/functions.html#float)) | outer diameter [m] |
| `DDi` ([float](https://docs.python.org/3/library/functions.html#float)) | bore diameter [m] |
| `Hr` ([float](https://docs.python.org/3/library/functions.html#float)) | total thickness of rubber layer [m] Optional Data |
| `cr` `cs` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficients for shear stress components of tau_r and tau_s |
| `vecx` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of vector components in global coordinates defining local x-axis (optional) |
| `vecyp` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass [kg] |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/YamamotoBiaxialHDR_Element)
