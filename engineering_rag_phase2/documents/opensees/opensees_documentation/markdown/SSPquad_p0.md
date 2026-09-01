<!-- chunk_id: SSPquad_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/SSPquad.html",
 "title": "3.1.10.16. SSPquad Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "SSPquad",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/SSPquad.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 6337,
 "word_count": 964,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.16. SSPquad Element

This command is used to construct a SSPquad element object. The SSPquad element is a four-node quadrilateral element using physically stabilized single-point integration (SSP –> Stabilized Single Point). The stabilization incorporates an assumed strain field in which the volumetric dilation and the shear strain associated with the the hourglass modes are zero, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements. The formulation for this element is identical to the solid phase portion of the SSPquadUP element as described by [McGannEtAl2012].

**element SSPquad $eleTag $iNode $jNode $kNode $lNode $matTag $type $thick <$b1 $b2>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag unique integer tag identifying element object |  |  |
| $iNode $jNode $kNode $lNode | 4 *integer* | the four nodes defining the element input in counterclockwise order (-ndm 2 -ndf 2) |
| $thick | *float* | thickness of the element in out-of-plane direction |
| $type | *float* | string to relay material behavior to the element (either “PlaneStrain” or “PlaneStress”) |
| $matTag | *integer* | unique integer tag associated with previously-defined nDMaterial object |
| $b1 $b2 | *float* | constant body forces in global x- and y-directions respectively (optional: default = 0.0) |

Fig. 3.1.10.17 SSPquad Element Node Numbering

Note

Valid queries to the SSPquad element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., ‘stress’, ‘strain’). Material response is recorded at the single integration point located in the center of the element.

The SSPquad element was designed with intentions of duplicating the functionality of the Quad Element. If an example is found where the SSPquad element cannot do something that works for the Quad Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.

Elemental recorders for stress and strain when using the SSPquad element (note the difference from the Quad Element)

Example

SSPquad element definition with element tag 1, nodes 1, 2, 3, and 4, material tag 1, plane strain conditions, unit thickness, horizontal body force of zero, and vertical body force of -10.0

1. **Tcl Code**

```
element SSPquad 1  1 2 3 4  1 "PlaneStrain" 1.0 0.0 -10.0
recorder Element -eleRange 1 $numElem -time -file stress.out  stress
recorder Element -eleRange 1 $numElem -time -file strain.out  strain
```

1. **Tcl Code**

```
element('SSPquad', 1, 1, 2,  3,  4,   1,  'PlaneStrain',  1.0,  0.0,  -10.0)
```

Code Developed by: [Chris McGann](https://www.canterbury.ac.nz/engineering/contact-us/people/chris-mcgann.html), [Pedro Arduino](https://www.ce.washington.edu/facultyfinder/pedro-arduino), [Peter Mackenzie-Helnwein](https://www.ce.washington.edu/facultyfinder/peter-mackenzie-helnwein) at University of Washington.

**McGannEtAl2012**

> McGann, C. R., Arduino, P., and Mackenzie-Helnwein, P. (2012). “Stabilized single-point 4-node quadrilateral element for dynamic analysis of fluid saturated porous media.” Acta Geotechnica, 7(4), 297-311.

Another Tcl Example

The input file shown below creates a cantilever beam subject to a parabolic shear stress distribution at the free end. The beam is modeled with only one element over the height to test the coarse-mesh accuracy of the designated quadrilateral element. Anti-symmetry conditions hold, only the top half of the beam is modeled.

Try running this with the SSPquad element and the Quad Element. Compare the results to each other and to the beam solution to see shear locking in action. Volumetric locking in the Quad Element can be observed by increasing Poisson’s ratio to 0.49.

```
#########################################################
#                #
# Coarse-mesh cantilever beam analysis.  The beam is    #
# modeled with only 4 elements and uses anti-symmetry.  #
##
# ---> Basic units used are kN and meters#
##
#########################################################

wipe

model BasicBuilder -ndm 2 -ndf 2

# beam dimensions
set L 24.0
set D 3.0

# define number and size of elements
set nElemX 4
set nElemY 1
set nElemT [expr $nElemX*$nElemY]
set sElemX [expr $L/$nElemX]
set sElemY [expr $D/$nElemY]

set nNodeX [expr $nElemX + 1]
set nNodeY [expr $nElemY + 1]
set nNodeT [expr $nNodeX*$nNodeY]

# create the nodes
set nid   1
set count 0.0
for {set j 1} {$j <= $nNodeY} {incr j 1} {
    for {set i 1} {$i <= $nNodeX} {incr i 1} {
	node $nid [expr 0.0 + $count*$sElemX] [expr ($j-1)*$sElemY]
	set nid   [expr $nid + 1]
	set count [expr $count + 1]
    }
    set count 0.0
}

# boundary conditions
fix 1   1 1
fix [expr $nElemY*$nNodeX+1]   1 0
for {set k 2} {$k <= $nNodeX} {incr k 1} {
    fix $k 1 0
}

# define material
set matID 1
set E     20000
set nu    0.25
nDMaterial ElasticIsotropic $matID $E $nu

# create elements
set thick 1.0
set b1 0.0
set b2 0.0
set count 1
for {set j 1} {$j <= $nNodeY} {incr j 1} {
    for {set i 1} {$i <= $nNodeX} {incr i 1} {
	if {($i < $nNodeX) && ($j < $nNodeY)} {
	    set nI [expr $i+($j-1)*$nNodeX]
	    set nJ [expr $i+($j-1)*$nNodeX+1]
	    set nK [expr $i+$j*$nNodeX+1]
	    set nL [expr $i+$j*$nNodeX]
	    element SSPquad $count  $nI $nJ $nK $nL $matID "PlaneStrain" $thick $b1 $b2

	    set count [expr $count+1]
	}
    }
}

# create recorders
set step 0.1

recorder Node -time -file results/d1p1m1.out -dT $step -nodeRange 1 $nNodeT -dof 1 2 disp
recorder Element -eleRange 1 $nElemT -time -file results/s1p1m1.out  -dT $step  stress
recorder Element -eleRange 1 $nElemT -time -file results/e1p1m1.out  -dT $step  strain

# create loading
set P -300.0;

pattern Plain 3 {Series -time {0 10 15} -values {0 1 1} -factor 1} {
    load $nNodeT   0.0 [expr 0.1875*$P]
    load $nNodeX   0.0 [expr 0.3125*$P]

    load [expr $nNodeX+1]   0.0 [expr -0.1875*$P]
}

# create analysis

integrator LoadControl 0.1
numberer RCM
system SparseGeneral
constraints Transformation
test NormDispIncr 1e-5 40 1
algorithm Newton
analysis Static

analyze 105

wipe
```
