<!-- chunk_id: SFI_MVLEM_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SFI_MVLEM.html",
 "title": "4.2.3.10. SFI MVLEM - Cyclic Shear-Flexure Interaction Model for RC Walls",
 "category": "model",
 "command": "SFI_MVLEM",
 "doc_section": "src",
 "rel_path": "src/SFI_MVLEM.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3609,
 "word_count": 383,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.10. SFI MVLEM - Cyclic Shear-Flexure Interaction Model for RC Walls

Developed and implemented by:

Kristijan Kolozvari (CSU Fullerton)

Kutay Orakcal (Bogazici University)

Leonardo Massone (University of Chile, Santiago)

John Wallace (UCLA)

The SFI_MVLEM command is used to construct a Shear-Flexure Interaction Multiple-Vertical-Line-Element Model (SFI-MVLEM, Kolozvari et al., 2018, 2015a, b, c; Kolozvari 2013), which captures interaction between axial/flexural and shear behavior of RC structural walls and columns under cyclic loading. The SFI_MVLEM element (Figure 1) incorporates 2-D RC panel behavior described by the Fixed-Strut-Angle-Model (nDMaterial FSAM; Ulugtekin, 2010; Orakcal et al., 2012), into a 2-D macroscopic fiber-based model (MVLEM). The interaction between axial and shear behavior is captured at each RC panel (macro-fiber) level, which further incorporates interaction between shear and flexural behavior at the SFI_MVLEM element level.

**element(*'SFI_MVLEM'*, *eleTag*, **eleNodes*, *m*, *c*, *'-thick'*, **thick*, *'-width'*, **widths*, *'-mat'*, **mat_tags*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `m` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of element macro-fibers |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | Location of center of rotation with from the iNode, `c` = 0.4 (recommended) |
| `Thicknesses` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of m macro-fiber thicknesses |
| `Widths` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of m macro-fiber widths |
| `Material_tags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of m macro-fiber nDMaterial1 tags |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/SFI_MVLEM_-_Cyclic_Shear-Flexure_Interaction_Model_for_RC_Walls)

> Kolozvari K., Orakcal K., and Wallace J. W. (2015a). “New opensees models for simulating nonlinear flexural and coupled shear-flexural behavior of RC walls and columns”, Computers and Structures, Volume 196, February 2018, Pages 246-262, [doi](https://doi.org/10.1016/j.compstruc.2017.10.010)
>
> Kolozvari K., Orakcal K., and Wallace J. W. (2015a). ”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls. I: Theory”, ASCE Journal of Structural Engineering, 141(5), 04014135 [doi](https://ascelibrary.org/doi/10.1061/%28ASCE%29ST.1943-541X.0001059)
>
> Kolozvari K., Tran T., Orakcal K., and Wallace, J.W. (2015c). ”Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls. II: Experimental Validation”, ASCE Journal of Structural Engineering, 141(5), 04014136 [doi](https://ascelibrary.org/doi/10.1061/%28ASCE%29ST.1943-541X.0001083)
>
> Kolozvari K., Orakcal K., and Wallace J. W. (2015c). “Shear-Flexure Interaction Modeling of reinforced Concrete Structural Walls and Columns under Reversed Cyclic Loading”, Pacific Earthquake Engineering Research Center, University of California, Berkeley, PEER Report No. 2015/12
>
> Kolozvari K. (2013). “Analytical Modeling of Cyclic Shear-Flexure Interaction in Reinforced Concrete Structural Walls”, PhD Dissertation, University of California, Los Angeles.
