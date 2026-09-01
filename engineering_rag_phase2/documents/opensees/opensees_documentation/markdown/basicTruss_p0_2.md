<!-- chunk_id: basicTruss_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/examples/basicTruss/basicTruss.html",
 "title": "Basic Truss Example",
 "category": "examples",
 "manual_group": "",
 "command": "basicTruss",
 "doc_section": "user/examples/basicTruss",
 "rel_path": "user/examples/basicTruss/basicTruss.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 666,
 "word_count": 112,
 "has_code": false,
 "has_table": false
} -->

## Basic Truss Example

This example is of a linear-elastic three bar truss, as shown in the figure, subject to static loads. The model has four nodes, labelled **1** through **4**, and three elements, labelled **1** through **3**. Nodes **1**, **2** ,and **3** are fixed and a loads of **100kip** and **-50kip** are imposed at node **4**. The elements all have a youngs modulus of **300ksi**, elements **2** and **3** have an area of **5in^2** and element **1** an area of **10in^***.

Because the model is planar and is comprised of truss elements, the spatial dimension of the mesh (`ndm`) will be specified as **2** and the nodes will only be specified to have **2** degrees-of-freedom.
