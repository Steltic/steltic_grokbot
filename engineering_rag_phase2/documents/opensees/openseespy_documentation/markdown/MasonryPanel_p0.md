<!-- chunk_id: MasonryPanel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MasonryPanel.html",
 "title": "4.2.16.6. MasonPan12 - 12 node Masonry panel element",
 "category": "element",
 "command": "MasonryPanel",
 "doc_section": "src",
 "rel_path": "src/MasonryPanel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1678,
 "word_count": 224,
 "has_code": false,
 "has_table": true
} -->

## 4.2.16.6. MasonPan12 - 12 node Masonry panel element

Developed and implemented by:

Gonzalo Torrisi <mailto:gonzalo.torrisi@ingenieria.uncuyo.edu.ar> (UNCuyo, Mendoza, Arrgentina)

The MasonPan12 command is used to construct a 12 node masonry panel element (Torrisi, 2012), which has 6 struts (3 in each direction) and it is able to capture the non linear behaviour of a masonry panel element diagonally loaded where
the principal crack is diagonal. The six struts allow the element to carry axial forces after the central strut are totally degraded due to cracking. Also, the six struts can interact with the sourronding frame to introduce shear forces and bending moments to the extreme zone of the columns and beams near the joint.

**element(*'MasonPan12'*, *eleTag*, **eleNodes*, *mat_1*, *mat_2*, *thick*, *w_tot*, *w_1*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- | --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of twelve element nodes in anti clockwise direction startin from the left down corner |
| `mat_1` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for uniaxial material for central strut behaviour |
| `mat_2` ([int](https://docs.python.org/3/library/functions.html#int)) | tag for uniaxial material for lateral struts behaviour |
| `Thick` ([float](https://docs.python.org/3/library/functions.html#float)) | out of plane thickness of the panel |
| `w_tot` \|float \| | ratio of the total strut width to diagonal length of the panel |
| `w1` \|float \| | ratio of central strut width to total strut widht |
