<!-- chunk_id: element_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/element.html",
 "title": "4.2. element commands",
 "category": "element",
 "command": "element",
 "doc_section": "src",
 "rel_path": "src/element.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 9463,
 "word_count": 460,
 "has_code": true,
 "has_table": true
} -->

## 4.2. element commands

**element(*eleType*, *eleTag*, **eleNodes*, **eleArgs*)**

Create a OpenSees element.

| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | element type |
| --- | --- |
| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag. |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of element nodes, must be preceded with `*`. |
| `eleArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of element arguments, must be preceded with `*`. |

For example,

```
eleType = 'truss'
eleTag = 1
eleNodes = [iNode, jNode]
eleArgs = [A, matTag]
element(eleType, eleTag, *eleNodes, *eleArgs)
```

The following contain information about available `eleType`:

#### 4.2.1. Zero-Length Element

1. [zeroLength Element](https://openseespydoc.readthedocs.io/en/latest/src/ZeroLength.html)
2. [zeroLengthND Element](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthND.html)
3. [zeroLengthSection Element](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthSection.html)
4. [CoupledZeroLength Element](https://openseespydoc.readthedocs.io/en/latest/src/CoupledZeroLength.html)
5. [zeroLengthContact elements](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthContact.html)
6. [zeroLengthContact Element](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthContact2D.html)
7. [zeroLengthContactNTS2D](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthContactNTS2D.html)
8. [zeroLengthInterface2D](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthInterface2D.html)
9. [zeroLengthImpact3D](https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthImpact3D.html)

#### 4.2.2. Truss Elements

1. [Truss Element](https://openseespydoc.readthedocs.io/en/latest/src/trussEle.html)
2. [Corotational Truss Element](https://openseespydoc.readthedocs.io/en/latest/src/corotTruss.html)

#### 4.2.3. Beam-Column Elements

1. [Elastic Beam Column Element](https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html)
2. [Elastic Beam Column Element with Stiffness Modifiers](https://openseespydoc.readthedocs.io/en/latest/src/ModElasticBeam2d.html)
3. [Elastic Timoshenko Beam Column Element](https://openseespydoc.readthedocs.io/en/latest/src/ElasticTimoshenkoBeam.html)
4. [Beam With Hinges Element](https://openseespydoc.readthedocs.io/en/latest/src/beamWithHinges.html)
5. [dispBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/dispBeamColumn.html)
6. [forceBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/ForceBeamColumn.html)
7. [nonlinearBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/nonlinearBeamColumn.html)
8. [Flexure-Shear Interaction Displacement-Based Beam-Column Element](https://openseespydoc.readthedocs.io/en/latest/src/dispBeamColumnInt.html)
9. [MVLEM - Multiple-Vertical-Line-Element-Model for RC Walls](https://openseespydoc.readthedocs.io/en/latest/src/MVLEM.html)
10. [SFI MVLEM - Cyclic Shear-Flexure Interaction Model for RC Walls](https://openseespydoc.readthedocs.io/en/latest/src/SFI_MVLEM.html)
11. [Elastic Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/pipe.html)
12. [Curved Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/curvedPipe.html)

#### 4.2.4. Joint Elements

1. [BeamColumnJoint Element](https://openseespydoc.readthedocs.io/en/latest/src/beamColumnJoint.html)
2. [ElasticTubularJoint Element](https://openseespydoc.readthedocs.io/en/latest/src/ElasticTubularJoint.html)
3. [Joint2D Element](https://openseespydoc.readthedocs.io/en/latest/src/Joint2D.html)

#### 4.2.5. Link Elements

1. [Two Node Link Element](https://openseespydoc.readthedocs.io/en/latest/src/twoNodeLink.html)

#### 4.2.6. Bearing Elements

1. [Elastomeric Bearing (Plasticity) Element](https://openseespydoc.readthedocs.io/en/latest/src/elastomericBearingPlasticity.html)
2. [Elastomeric Bearing (Bouc-Wen) Element](https://openseespydoc.readthedocs.io/en/latest/src/elastomericBearingBoucWen.html)
3. [Flat Slider Bearing Element](https://openseespydoc.readthedocs.io/en/latest/src/flatSliderBearing.html)
4. [Single Friction Pendulum Bearing Element](https://openseespydoc.readthedocs.io/en/latest/src/singleFPBearing.html)
5. [Triple Friction Pendulum Bearing Element](https://openseespydoc.readthedocs.io/en/latest/src/TFP.html)
6. [Triple Friction Pendulum Element](https://openseespydoc.readthedocs.io/en/latest/src/TripleFrictionPendulum.html)
7. [MultipleShearSpring Element](https://openseespydoc.readthedocs.io/en/latest/src/multipleShearSpring.html)
8. [KikuchiBearing Element](https://openseespydoc.readthedocs.io/en/latest/src/KikuchiBearing.html)
9. [YamamotoBiaxialHDR Element](https://openseespydoc.readthedocs.io/en/latest/src/YamamotoBiaxialHDR.html)
10. [ElastomericX](https://openseespydoc.readthedocs.io/en/latest/src/ElastomericX.html)
11. [LeadRubberX](https://openseespydoc.readthedocs.io/en/latest/src/LeadRubberX.html)
12. [HDR](https://openseespydoc.readthedocs.io/en/latest/src/HDR.html)
13. [RJ-Watson EQS Bearing Element](https://openseespydoc.readthedocs.io/en/latest/src/RJWatsonEqsBearing.html)
14. [FPBearingPTV](https://openseespydoc.readthedocs.io/en/latest/src/FPBearingPTV.html)

#### 4.2.7. Quadrilateral Elements

1. [Quad Element](https://openseespydoc.readthedocs.io/en/latest/src/quad.html)
2. [Shell Element](https://openseespydoc.readthedocs.io/en/latest/src/ShellMITC4.html)
3. [ShellDKGQ](https://openseespydoc.readthedocs.io/en/latest/src/ShellDKGQ.html)
4. [ShellDKGT](https://openseespydoc.readthedocs.io/en/latest/src/ShellDKGT.html)
5. [ShellNLDKGQ](https://openseespydoc.readthedocs.io/en/latest/src/ShellNLDKGQ.html)
6. [ShellNLDKGT](https://openseespydoc.readthedocs.io/en/latest/src/ShellNLDKGT.html)
7. [ShellNL](https://openseespydoc.readthedocs.io/en/latest/src/ShellNL.html)
8. [Bbar Plane Strain Quadrilateral Element](https://openseespydoc.readthedocs.io/en/latest/src/bbarQuad.html)
9. [Enhanced Strain Quadrilateral Element](https://openseespydoc.readthedocs.io/en/latest/src/enhancedQuad.html)
10. [SSPquad Element](https://openseespydoc.readthedocs.io/en/latest/src/SSPquad.html)
11. [MVLEM_3D - 3-D MVLEM Element for Flexure-Dominated RC Walls](https://openseespydoc.readthedocs.io/en/latest/src/MVLEM_3D.html)
12. [SFI_MVLEM_3D - 3-D Shear-Flexure-Interaction Element for RC Walls](https://openseespydoc.readthedocs.io/en/latest/src/SFI_MVLEM_3D.html)

#### 4.2.8. Triangular Elements

1. [Tri31 Element](https://openseespydoc.readthedocs.io/en/latest/src/tri31.html)

#### 4.2.9. Brick Elements

1. [Standard Brick Element](https://openseespydoc.readthedocs.io/en/latest/src/stdBrick.html)
2. [Bbar Brick Element](https://openseespydoc.readthedocs.io/en/latest/src/bbarBrick.html)
3. [Twenty Node Brick Element](https://openseespydoc.readthedocs.io/en/latest/src/20NodeBrick.html)
4. [SSPbrick Element](https://openseespydoc.readthedocs.io/en/latest/src/SSPbrick.html)

#### 4.2.10. Tetrahedron Elements

1. [FourNodeTetrahedron](https://openseespydoc.readthedocs.io/en/latest/src/FourNodeTetrahedron.html)

#### 4.2.11. UC San Diego u-p element (saturated soil)

1. [Four Node Quad u-p Element](https://openseespydoc.readthedocs.io/en/latest/src/quadUP.html)
2. [Brick u-p Element](https://openseespydoc.readthedocs.io/en/latest/src/brickUP.html)
3. [BbarQuad u-p Element](https://openseespydoc.readthedocs.io/en/latest/src/bbarQuadUP.html)
4. [BbarBrick u-p Element](https://openseespydoc.readthedocs.io/en/latest/src/bbarBrickUP.html)
5. [Nine Four Node Quad u-p Element](https://openseespydoc.readthedocs.io/en/latest/src/NineFourNodeQuadUP.html)
6. [Twenty Eight Node Brick u-p Element](https://openseespydoc.readthedocs.io/en/latest/src/TwentyEightNodeBrickUP.html)

#### 4.2.12. Other u-p elements

1. [SSPquadUP Element](https://openseespydoc.readthedocs.io/en/latest/src/SSPquadUP.html)
2. [SSPbrickUP Element](https://openseespydoc.readthedocs.io/en/latest/src/SSPbrickUP.html)

#### 4.2.13. Contact Elements

1. [SimpleContact2D](https://openseespydoc.readthedocs.io/en/latest/src/SimpleContact2D.html)
2. [SimpleContact3D](https://openseespydoc.readthedocs.io/en/latest/src/SimpleContact3D.html)
3. [BeamContact2D](https://openseespydoc.readthedocs.io/en/latest/src/BeamContact2D.html)
4. [BeamContact3D](https://openseespydoc.readthedocs.io/en/latest/src/BeamContact3D.html)
5. [BeamEndContact3D](https://openseespydoc.readthedocs.io/en/latest/src/BeamEndContact3D.html)

#### 4.2.14. Cable Elements

1. [CatenaryCableElement](https://openseespydoc.readthedocs.io/en/latest/src/CatenaryCable.html)

#### 4.2.15. PFEM Elements

1. [PFEMElementBubble](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementBubble.html)
2. [PFEMElementCompressible](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementCompressible.html)

#### 4.2.16. Misc.

1. [SurfaceLoad Element](https://openseespydoc.readthedocs.io/en/latest/src/SurfaceLoad.html)
2. [VS3D4](https://openseespydoc.readthedocs.io/en/latest/src/VS3D4.html)
3. [AC3D8](https://openseespydoc.readthedocs.io/en/latest/src/AC3D8.html)
4. [ASI3D8](https://openseespydoc.readthedocs.io/en/latest/src/ASI3D8.html)
5. [AV3D4](https://openseespydoc.readthedocs.io/en/latest/src/AV3D4.html)
6. [MasonPan12 - 12 node Masonry panel element](https://openseespydoc.readthedocs.io/en/latest/src/MasonryPanel.html)
