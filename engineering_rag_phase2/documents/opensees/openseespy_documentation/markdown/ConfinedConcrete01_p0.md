<!-- chunk_id: ConfinedConcrete01_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ConfinedConcrete01.html",
 "title": "4.14.2.8. ConfinedConcrete01",
 "category": "general",
 "command": "ConfinedConcrete01",
 "doc_section": "src",
 "rel_path": "src/ConfinedConcrete01.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5573,
 "word_count": 622,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.8. ConfinedConcrete01

**uniaxialMaterial(*'ConfinedConcrete01'*, *matTag*, *secType*, *fpc*, *Ec*, *epscu_type*, *epscu_val*, *nu*, *L1*, *L2*, *L3*, *phis*, *S*, *fyh*, *Es0*, *haRatio*, *mu*, *phiLon*, *'-internal'*, **internalArgs*, *'-wrap'*, **wrapArgs*, *'-gravel'*, *'-silica'*, *'-tol'*, *tol*, *'-maxNumIter'*, *maxNumIter*, *'-epscuLimit'*, *epscuLimit*, *'-stRatio'*, *stRatio*)**

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `secType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | tag for the transverse reinforcement configuration. see image below. `'S1'` square section with S1 type of transverse reinforcement with or without external FRP wrapping `'S2'` square section with S2 type of transverse reinforcement with or without external FRP wrapping `'S3'` square section with S3 type of transverse reinforcement with or without external FRP wrapping `'S4a'` square section with S4a type of transverse reinforcement with or without external FRP wrapping `'S4b'` square section with S4b type of transverse reinforcement with or without external FRP wrapping `'S5'` square section with S5 type of transverse reinforcement with or without external FRP wrapping `'C'` circular section with or without external FRP wrapping `'R'` rectangular section with or without external FRP wrapping. |
| `fpc` ([float](https://docs.python.org/3/library/functions.html#float)) | unconfined cylindrical strength of concrete specimen. |
| `Ec` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic modulus of unconfined concrete. |
| `epscu_type` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Method to define confined concrete ultimate strain - `-epscu` then value is confined concrete ultimate strain, - `-gamma` then value is the ratio of the strength corresponding to ultimate strain to the peak strength of the confined concrete stress-strain curve. If `gamma` cannot be achieved in the range [0, epscuLimit] then epscuLimit (optional, default: 0.05) will be assumed as ultimate strain. |
| `epscu_val` ([float](https://docs.python.org/3/library/functions.html#float)) | Value for the definition of the concrete ultimate strain |
| `nu` ([str](https://docs.python.org/3/library/stdtypes.html#str)) or ([list](https://docs.python.org/3/library/stdtypes.html#list)) | Definition for Poisson’s Ratio. - `['-nu', <value of Poisson's ratio>]` - `'-varub'` Poisson’s ratio is defined as a function of axial strain by means of the expression proposed by Braga et al. (2006) with the upper bound equal to 0.5 -`'-varnoub'` Poisson’s ratio is defined as a function of axial strain by means of the expression proposed by Braga et al. (2006) without any upper bound. |
| `L1` ([float](https://docs.python.org/3/library/functions.html#float)) | length/diameter of square/circular core section measured respect to the hoop center line. |
| `L2` ([float](https://docs.python.org/3/library/functions.html#float)) | additional dimensions when multiple hoops are being used. |
| `L3` ([float](https://docs.python.org/3/library/functions.html#float)) | additional dimensions when multiple hoops are being used. |
| `phis` ([float](https://docs.python.org/3/library/functions.html#float)) | hoop diameter. If section arrangement has multiple hoops it refers to the external hoop. |
| `S` ([float](https://docs.python.org/3/library/functions.html#float)) | hoop spacing. |
| `fyh` ([float](https://docs.python.org/3/library/functions.html#float)) | yielding strength of the hoop steel. |
| `Es0` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic modulus of the hoop steel. |
| `haRatio` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening ratio of the hoop steel. |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | ductility factor of the hoop steel. |
| `phiLon` ([float](https://docs.python.org/3/library/functions.html#float)) | diameter of longitudinal bars. |
| `internalArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `internalArgs= [phisi, Si, fyhi, Es0i, haRatioi, mui]` optional parameters for defining the internal transverse reinforcement. If they are not specified they will be assumed equal to the external ones (for `S2`, `S3`, `S4a`, `S4b` and `S5` typed). |
| `wrapArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `wrapArgs=[cover, Am, Sw, ful, Es0w]` optional parameters required when section is strengthened with FRP wraps. `cover` cover thickness measured from the outer line of hoop. `Am` total area of FRP wraps (number of layers x wrap thickness x wrap width). `Sw` spacing of FRP wraps (if continuous wraps are used the spacing is equal to the wrap width). `ful` ultimate strength of FRP wraps. `Es0w` elastic modulus of FRP wraps. |
| `'-gravel'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Unknown |
| `'-silica'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Unknown |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | Unknown |
| `maxNumIter` ([int](https://docs.python.org/3/library/functions.html#int)) | Unknown |
| `epscuLimit` ([float](https://docs.python.org/3/library/functions.html#float)) | Unknown |
| `stRatio` | Unknown |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ConfinedConcrete01_Material)
