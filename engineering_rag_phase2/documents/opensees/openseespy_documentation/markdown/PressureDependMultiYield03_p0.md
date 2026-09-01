<!-- chunk_id: PressureDependMultiYield03_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PressureDependMultiYield03.html",
 "title": "4.15.6.4. PressureDependMultiYield03",
 "category": "general",
 "command": "PressureDependMultiYield03",
 "doc_section": "src",
 "rel_path": "src/PressureDependMultiYield03.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 960,
 "word_count": 96,
 "has_code": false,
 "has_table": false
} -->

## 4.15.6.4. PressureDependMultiYield03

**nDMaterial(*'PressureDependMultiYield03'*, *matTag*, *nd*, *rho*, *refShearModul*, *refBulkModul*, *frictionAng*, *peakShearStra*, *refPress*, *pressDependCoe*, *PTAng*, *ca*, *cb*, *cc*, *cd*, *ce*, *da*, *db*, *dc*, *noYieldSurf=20.0*, **yieldSurf=[]*, *liquefac1=1*, *liquefac2=0.*, *pa=101*, *s0=1.73*)**

The reference for PressureDependMultiYield03 material: Khosravifar, A., Elgamal, A., Lu, J., and Li, J. [2018]. “A 3D model for earthquake-induced liquefaction triggering and post-liquefaction response.” Soil Dynamics and Earthquake Engineering, 110, 43-52)

PressureDependMultiYield03 is modified from PressureDependMultiYield02 material to comply with the established guidelines on the dependence of liquefaction triggering to the number of loading cycles, effective overburden stress (Kσ), and static shear stress (Kα).

The explanations of parameters

See [notes](http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02_Material)
