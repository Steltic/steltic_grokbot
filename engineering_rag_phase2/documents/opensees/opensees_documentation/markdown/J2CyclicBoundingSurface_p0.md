<!-- chunk_id: J2CyclicBoundingSurface_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/J2CyclicBoundingSurface.html",
 "title": "3.1.6.12. J2CyclicBoundingSurface Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "J2CyclicBoundingSurface",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/J2CyclicBoundingSurface.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4145,
 "word_count": 632,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.12. J2CyclicBoundingSurface Material

Code Developed by: **Alborz Ghofrani** and [Pedro Arduino](https://www.ce.washington.edu/facultyfinder/pedro-arduino) at U.Washington.

This command is used to construct a J2CyclicBoundingSurface material ([Borja-Amies1994]).

> J2CyclicBoundingSurface $matTag $G $K $Su $Den $h $m $h0 $chi $beta

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | tag identifying material |
| $G | *float* | Shear modulus |
| $K | *float* | Bulk modulus |
| $su | *float* | Undrained shear strength |
| $Den | *float* | Mass density of the material |
| $h | *float* | Hardening parameter |
| $m | *float* | Hardening exponent |
| $h0 | *float* | Initial hardening parameter |
| $chi | *float* | Initial damping (viscous). chi = 2*dr_o/omega (dr_o = damping ratio at zero strain, omega = angular frequency) |
| $beta | *float* | Integration variable (0 = explicit, 1 = implicit, 0.5 = midpoint rule) |

Note

The material formulations for the J2CyclicBoundingSurface object are “ThreeDimensional” and “PlaneStrain”.

Valid Element Recorder queries are **stress**, **strain**

Elastic response could be enforced by

```
updateMaterialStage -material $matTag -stage 0
```

Elastoplastic by

```
updateMaterialStage -material $matTag -stage 1
```

**Borja-Amies1994**

> Borja R., Amies A., “Multiaxial Cyclic Plasticity Model for Clays”. Journal of Geotech. Engrg., 1994, 120(6):1051-1070

Example 1

This example, provides an conventional triaxial compression test using one 8-node SSPBrick element and J2CyclicBoundingSurface material model.

```
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #
# 3D Conventional Triaxial Compression Test Using One Element              #
# University of Washington, Department of Civil and Environmental Eng      #
# Computational Geotechnics Eng Group, A. Ghofrani, P. Arduino - Dec 2013  #
# Basic units are m, Ton(metric), s		     			   #
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #

set strains {0.05}

for {set ii 0} {$ii < [llength $strains]} {incr ii} {
	# debug material model
	wipe

	# #################################
	# build model: -ndm 3  -ndf 3
	# #################################
	model BasicBuilder -ndm 3 -ndf 3

	# create the materials
	node 1  0.00000000 0.00000000 0.00000000
	node 2  0.00000000 1.00000000 0.00000000
	node 3  1.00000000 1.00000000 0.00000000
	node 4  1.00000000 0.00000000 0.00000000
	node 5  0.00000000 0.00000000 1.00000000
	node 6  0.00000000 1.00000000 1.00000000
	node 7  1.00000000 1.00000000 1.00000000
	node 8  1.00000000 0.00000000 1.00000000

	# create the materials

	set E 20000.0
	set nu 0.499
	set G [expr $E / 2.0 / (1 + $nu)]
	set K [expr $E / 3.0 / (1 - 2.0 * $nu)]

	set R [expr 100.0]
	set su [expr sqrt(3.0 / 8.0) * $R]
	# nDMaterial ElasticIsotropic 1 100000 0.3
	# nDMaterial J2CyclicBoundingSurface  tag? G? K? su? rho? h? m? h0? chi? beta? in kpa
	nDMaterial J2CyclicBoundingSurface 1 $G $K $su 1.7 $G 1.0 0.2 0.0 0.5

	# create the elements
	element SSPbrick    1    1 4 3 2 5 8 7 6   1

	# create the fixities
	fix     1      1   1   1
	fix     2      1   0   1
	fix     3      0   0   1
	fix     4      0   1   1
	fix     5      1   1   0
	fix     6      1   0   0
	fix     7      0   0   0
	fix     8      0   1   0

	# recorders
	recorder Node     -file "displacement.out"  -nodeRange 1 8 -dof 1 2 3 disp
	recorder Node     -file "velocity.out"      -nodeRange 1 8 -dof 1 2 3 vel
	recorder Node     -file "reactions.out"     -nodeRange 1 8 -dof 1 2 3 reaction
	recorder Element  -file "stress.out"     -ele 1  stress
	recorder Element  -file "strain.out"     -ele 1  strain

	# load pattern
	pattern Plain 1 {Series -time {0.0 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0} -values {0.0 1.0 0.0 -1.0 0.0 1.0 0.0 -1.0 0.0} -factor -1.0} {
		sp 5 3 [lindex $strains $ii]
		sp 6 3 [lindex $strains $ii]
		sp 7 3 [lindex $strains $ii]
		sp 8 3 [lindex $strains $ii]
	}

	# analysis
	constraints Transformation
	test        NormDispIncr 1e-9 50 1
	algorithm   Newton
	numberer    Plain
	system      SparseSPD
	integrator  LoadControl 0.004
	analysis    Static

	analyze    2000

	wipe
```
