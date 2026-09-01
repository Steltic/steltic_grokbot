<!-- chunk_id: bbarQuad_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/bbarQuad.html",
 "title": "Bbar Plane Strain Quad Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "bbarQuad",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/bbarQuad.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 922,
 "word_count": 125,
 "has_code": false,
 "has_table": false
} -->

## Bbar Plane Strain Quad Element

This command is used to construct a four-node quadrilateral element object, which uses a bilinear isoparametric formulation along with a mixed volume/pressure B-bar assumption. This element is for plane strain problems only.

**element bbarQuad $eleTag $iNode $jNode $kNode $lNode $thick $matTag**

$eleTag, *integer*,     unique element object tag
$iNode $jNode $kNode $lNode, *integer*,  four nodes defining element boundaries, input in counter-clockwise order around the element.
$thick, *float*, element thickness
$matTag, *integer*, tag of nDMaterial

Note

PlainStrain only.

The valid queries to a Quad element when creating an ElementRecorder object are ‘forces’, ‘stresses,’ and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

Code Developed by: **Edward Love, Sandia National Laboratories**
