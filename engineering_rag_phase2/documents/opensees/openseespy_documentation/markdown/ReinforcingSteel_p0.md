<!-- chunk_id: ReinforcingSteel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ReinforcingSteel.html",
 "title": "4.14.1.4. ReinforcingSteel",
 "category": "general",
 "command": "ReinforcingSteel",
 "doc_section": "src",
 "rel_path": "src/ReinforcingSteel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3822,
 "word_count": 366,
 "has_code": false,
 "has_table": true
} -->

## 4.14.1.4. ReinforcingSteel

**uniaxialMaterial(*'ReinforcingSteel'*, *matTag*, *fy*, *fu*, *Es*, *Esh*, *eps_sh*, *eps_ult*, *'-GABuck'*, *lsr*, *beta*, *r*, *gamma*, *'-DMBuck'*, *lsr*, *alpha=1.0*, *'-CMFatigue'*, *Cf*, *alpha*, *Cd*, *'-IsoHard'*, *a1=4.3*, *limit=1.0*, *'-MPCurveParams'*, *R1=0.333*, *R2=18.0*, *R3=4.0*)**

This command is used to construct a ReinforcingSteel uniaxial material object. This object is intended to be used in a reinforced concrete fiber section as the steel reinforcing material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fy` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield stress in tension |
| `fu` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate stress in tension |
| `Es` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial elastic tangent |
| `Esh` ([float](https://docs.python.org/3/library/functions.html#float)) | Tangent at initial strain hardening |
| `eps_sh` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain corresponding to initial strain hardening |
| `eps_ult` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain at peak stress |
| `'-GABuck'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Buckling Model Based on Gomes and Appleton (1997) |
| `lsr` ([float](https://docs.python.org/3/library/functions.html#float)) | Slenderness Ratio |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | Amplification factor for the buckled stress strain curve. |
| `r` ([float](https://docs.python.org/3/library/functions.html#float)) | Buckling reduction factor r can be a real number between [0.0 and 1.0] r=1.0 full reduction (no buckling) r=0.0 no reduction 0.0<r<1.0 linear interpolation between buckled and unbuckled curves |
| `gamma` ([float](https://docs.python.org/3/library/functions.html#float)) | Buckling constant |
| `'-DMBuck'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Buckling model based on Dhakal and Maekawa (2002) |
| `lsr` ([float](https://docs.python.org/3/library/functions.html#float)) | Slenderness Ratio |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | Adjustment Constant usually between 0.75 and 1.0 Default: alpha=1.0, this parameter is optional. |
| `'-CMFatigue'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Coffin-Manson Fatigue and Strength Reduction |
| `Cf` ([float](https://docs.python.org/3/library/functions.html#float)) | Coffin-Manson constant C |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | Coffin-Manson constant a |
| `Cd` ([float](https://docs.python.org/3/library/functions.html#float)) | Cyclic strength reduction constant |
| `'-IsoHard'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Isotropic Hardening / Diminishing Yield Plateau |
| `a1` ([float](https://docs.python.org/3/library/functions.html#float)) | Hardening constant (default = 4.3) |
| `limit` ([float](https://docs.python.org/3/library/functions.html#float)) | Limit for the reduction of the yield plateau. % of original plateau length to remain (0.01 < limit < 1.0 ) Limit =1.0, then no reduction takes place (default =0.01) |
| `'-MPCurveParams'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Menegotto and Pinto Curve Parameters |
| `R1` ([float](https://docs.python.org/3/library/functions.html#float)) | (default = 0.333) |
| `R2` ([float](https://docs.python.org/3/library/functions.html#float)) | (default = 18) |
| `R3` ([float](https://docs.python.org/3/library/functions.html#float)) | (default = 4) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Reinforcing_Steel_Material)
