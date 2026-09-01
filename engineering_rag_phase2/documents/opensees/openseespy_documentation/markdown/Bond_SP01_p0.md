<!-- chunk_id: Bond_SP01_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Bond_SP01.html",
 "title": "4.14.5.11. Bond SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars",
 "category": "model",
 "command": "Bond_SP01",
 "doc_section": "src",
 "rel_path": "src/Bond_SP01.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1955,
 "word_count": 230,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.11. Bond SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars

**uniaxialMaterial(*'Bond_SP01'*, *matTag*, *Fy*, *Sy*, *Fu*, *Su*, *b*, *R*)**

This command is used to construct a uniaxial material object for capturing strain penetration effects at the column-to-footing, column-to-bridge bent caps, and wall-to-footing intersections. In these cases, the bond slip associated with strain penetration typically occurs along a portion of the anchorage length. This model can also be applied to the beam end regions, where the strain penetration may include slippage of the bar along the entire anchorage length, but the model parameters should be chosen appropriately.

This model is for fully anchored steel reinforcement bars that experience bond slip along a portion of the anchorage length due to strain penetration effects, which are usually the case for column and wall longitudinal bars anchored into footings or bridge joints

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield strength of the reinforcement steel |
| `Sy` ([float](https://docs.python.org/3/library/functions.html#float)) | Rebar slip at member interface under yield stress. (see NOTES below) |
| `Fu` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate strength of the reinforcement steel |
| `Su` ([float](https://docs.python.org/3/library/functions.html#float)) | Rebar slip at the loaded end at the bar fracture strength |
| `b` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial hardening ratio in the monotonic slip vs. bar stress response (0.3~0.5) |
| `R` ([float](https://docs.python.org/3/library/functions.html#float)) | Pinching factor for the cyclic slip vs. bar response (0.5~1.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Bond_SP01_-_-_Strain_Penetration_Model_for_Fully_Anchored_Steel_Reinforcing_Bars)
