<!-- chunk_id: PM4Sand_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PM4Sand.html",
 "title": "3.1.6.7. PM4Sand Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "PM4Sand",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/PM4Sand.html",
 "part_index": 0,
 "part_count": 2,
 "char_count": 9563,
 "word_count": 1497,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.7. PM4Sand Material [part 1/2]

Code Developed by: **Long Chen** and [Pedro Arduino](https://www.ce.washington.edu/facultyfinder/pedro-arduino) at U.Washington.

This command is used to construct a 2-dimensional PM4Sand material ([Boulanger-Ziotopoulou2017]).

> nDmaterial PM4Sand $matTag $Dr $G0 $hpo $Den <$patm $h0 $emax $emin $nb $nd $Ado $zmax $cz $ce $phic $nu $cgd $cdr $ckaf $Q $R $m $Fsed_min $p_sedo>

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | tag identifying material |
| $Dr | *float* | Relative density (fraction) |
| $G0 | *float* | Shear modulus constant |
| $hpo | *float* | Contraction rate parameter |
| $Den | *float* | Mass density of the material |
| $P_atm | *float* | optional: Atmospheric pressure |
| $h0 | *float* | optional: Variable that adjusts the ratio of plastic modulus to elastic modulus |
| $emax and $emin | *float* | optional: Maximum and minimum void ratios |
| $nb | *float* | optional: Bounding surface parameter $nb ≥ 0 |
| $nd | *float* | optional: Dilatancy surface parameter $nd ≥ 0 |
| $Ado | *float* | optional: Dilatancy parameter will be computed at the time of initialization if input value is negative |
| $z_max | *float* | optional: Fabric-dilatancy tensor parameter |
| $cz | *float* | optional: Fabric-dilatancy tensor parameter |
| $ce | *float* | optional: Variable that adjusts the rate of strain accumulation in cyclic loading |
| $phic | *float* | optional: Critical state effective friction angle |
| $nu | *float* | optional: Poisson’s ratio |
| $cgd | *float* | optional: Variable that adjusts degradation of elastic modulus with accumulation of fabric |
| $cdr | *float* | optional: Variable that controls the rotated dilatancy surface |
| $ckaf | *float* | optional: Variable that controls the effect that sustained static shear stresses have on plastic modulus |
| $Q | *float* | optional: Critical state line parameter |
| $R | *float* | optional: Critical state line parameter |
| $m | *float* | optional: Yield surface constant (radius of yield surface in stress ratio space) |
| $Fsed_min | *float* | optional: Variable that controls the minimum value the reduction factor of the elastic moduli can get during reconsolidation |
| $p_sedo | *float* | optional: Mean effective stress up to which reconsolidation strains are enhanced |

Note

The only material formulation for the PM4Sand object is “PlaneStrain”, as a consequence limited to plain strain continuum elements.

Valid Element Recorder queries are **stress**, **strain**, **alpha** (or backstressratio) for \(\mathbf{\alpha}\), **fabric** for \(\mathbf{z}\), and **alpha_in** (or alphain) for \(\mathbf{\alpha_{in}}\)

Elastic or response could be enforced by

```
updateMaterialStage -material $matTag -stage 0
```

Elastoplastic by

```
updateMaterialStage -material $matTag -stage 1
```

The program will use the default value of a secondary parameter if a negative input is assigned to that parameter, e.g. Ado = -1. However, FirstCall is mandatory when switching from elastic to elastoplastic if negative inputs are assigned to stress-dependent secondary parameters, e.g. Ado and zmax. FirstCall can be set as,

```
setParameter -value 0 -ele $elementTag FirstCall $matTag
```

Post-shake reconsolidation can be activated by

```
setParameter -value 1 -ele $elementTag Postshake $matTag

The user should check that the results are not sensitive to time step size.
```

**Boulanger-Ziotopoulou2017**

> R.W.Boulanger, K.Ziotopoulou. “PM4Sand(Version 3.1): A Sand Plasticity Model for Earthquake Engineering Applications”. Report No. UCD/CGM-17/01 2017

Example 1

2D undrained monotonic direct simple shear test using one element

```
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #
# 2D Undrained Direct Simple Shear Test Using One Element #
# University of Washington, Department of Civil and Environmental Eng   #
# Geotechnical Eng Group, L. Chen, P. Arduino - Jan 2018               #
# Basic Units are m, kN and s unless otherwise specified#
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #

wipe

# ------------------------ #
# Test Specific parameters #
# ------------------------ #
# Initial Vertical Stress
set sigvo -101.3
set K0 0.5
# set Poisson's ratio to match user specified K0
set nu [expr $K0 / (1+$K0)]
# Deviatoric strain (Cyclic)
set devDisp 0.10
# Permeablity
set perm 1.0e-9
# Initial void ratio
# relative density
set Dr 0.35
# max and min void ratio
set emax 0.8
set emin 0.5
set eInit [expr $emax - ($emax - $emin)*$Dr ]
# other primary parameters
set G0 476.0
set hpo 0.53
set rho 1.42

# Rayleigh damping parameter
set damp   0.02
set omega1 0.2
set omega2 20.0
set a1 [expr 2.0*$damp/($omega1+$omega2)]
set a0 [expr $a1*$omega1*$omega2]

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHCreate ModelHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

# Create a 2D model with 3 Degrees of Freedom
model BasicBuilder -ndm 2 -ndf 3

# Create nodes
node 10.00.0
node 21.00.0
node 3 1.01.0
node 40.01.0

# Create Fixities
fix 1 1 1 1
fix 2 1 1 1
fix 30 0 1
fix 4 0 0 1

equalDOF 3 4 1 2

# Create material
#          PM4Sand  tag    Dr   G0   hpo   den  Patm  h0     emax   emin  nb   nd  Ado   zmax    cz    ce     phicv  nu
nDMaterial PM4Sand   1    $Dr  $G0  $hpo  $rho 101.3 -1.00   $emax  $emin 0.5  0.1  -1.0  -1.0  250.0  -1.00  33.0  $nu

# Create element
element SSPquadUP   1     1 2 3 4    1  1.0   2.2e6 1.0 $perm $perm $eInit  1.0e-5

# Create recorders
recorder Node  -nodeRange 1 4  -time -file Cycdisp.out  -dof 1 2 disp
recorder Node  -nodeRange 1 4  -time -file Cycpress.out -dof 3 vel
recorder Element -ele 1 -time -file Cycstress.out stress
recorder Element -ele 1 -time -file Cycstrain.out strain

# Create analysis
constraints Transformation
test        NormDispIncr 1.0e-5 35 1
algorithm   Newton
numberer    RCM
system      SparseGeneral
integrator  Newmark [expr 5.0 / 6.0] [expr  4.0 / 9.0]
rayleigh    $a0 $a1 0.0 0.0
analysis    Transient

# Apply consolidation pressure
set pNode [expr $sigvo / 2.0]
pattern Plain 1 {Series -time {0 100 1e10} -values {0 1 1} -factor 1} {
    load 3  0.0  $pNode 0.0
    load 4  0.0  $pNode 0.0
}
updateMaterialStage -material 1 -stage 0

analyze 100 1
set vDisp [nodeDisp 3 2]
set ts1 "{Series -time {100 80000 1.0e10} -values {1.0 1.0 1.0} -factor 1}"
eval "pattern Plain 2 $ts1 {
sp 3 2 $vDisp
sp 4 2 $vDisp
}"

# Close drainage valves
for {set x 1} {$x< 5} {incr x} {
   remove sp $x 3
}

analyze 25 1
puts "Removed drainage fixities."

updateMaterialStage -material 1 -stage 1
setParameter -value 0 -ele 1 FirstCall 1
analyze 25 1

puts "finished update fixties"

set ts2 "{Series -time {150 5150 1.0e10} -values {0.0 1.0 1.0} -factor 1}"

eval "pattern Plain 3 $ts2 {
sp 3 1 $devDisp
}"
# update Poisson's ratio for analysis
setParameter -value 0.3 -ele 1 poissonRatio 1
analyze 5000 1

wipe
```

Example 2

2D undrained cyclic direct simple shear test using one element (Displacement Controlled)

```
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #
# 2D Undrained Cyclic Direct Simple Shear Test Using One Element        #
# University of Washington, Department of Civil and Environmental Eng   #
# Geotechnical Eng Group, L. Chen, P. Arduino - Feb 2018                #
# Basic Units are m, kN and s unless otherwise specified#
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #

wipe

# ------------------------ #
# Test Specific parameters #
# ------------------------ #
# Initial Vertical Stress
set sigvo -101.3
# cyclic stress ratio
set CSR 0.16
# max number of cycles
set maxCycles 20
# strain increment
set strainIncr 5.0e-6
# K0
set K0 0.5
# set Poisson's ratio to match user specified K0 for applying initial confinement
set nu [expr $K0 / (1+$K0)]
# Cutoff shear strain
set devDisp 0.03
# Permeablity
set perm 1.0e-9
# ---------primary parameters-------------
set Dr 0.35
set G0 476.0
set hpo 0.53
set rho 1.42
# ---------secondary parameters-------------
set Patm 101.3
# all initial stress dependant parameters have negative default values
# and will be calculated during initialization
set h0 -1.0
set emax 0.8
set emin 0.5
set eInit [expr $emax - ($emax - $emin)*$Dr ]
set nb 0.5
set nd 0.1
set Ado -1.0
set zmax -1.0
set cz 250.0
set ce -1.0
set phicv 33.0
set Cgd 2.0
set Cdr -1.0
set ckaf -1.0
set Q 10.0
set R 1.5
set m_m 0.01
set Fsed_min -1.0
set p_sedo -1.0
# ---------------------------------------------
# Rayleigh damping parameter
set damp   0.02
set omega1 0.2
set omega2 20.0
set a1 [expr 2.0*$damp/($omega1+$omega2)]
set a0 [expr $a1*$omega1*$omega2]

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHCreate ModelHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

# Create a 2D model with 3 Degrees of Freedom
model BasicBuilder -ndm 2 -ndf 3

# Create nodes
node 10.00.0
node 21.00.0
node 3 1.01.0
node 40.01.0

# Create Fixities
fix 1 1 1 1
fix 2 1 1 1
fix 30 0 1
fix 4 0 0 1

equalDOF 3 4 1 2

# Create material
#          PM4Sand  tag    Dr   G0   hpo   den  Patm  h0   emax   emin  nb  nd  Ado   zmax    cz    ce     phicv  nu
nDMaterial PM4Sand   1    $Dr  $G0  $hpo  $rho $Patm $h0  $emax $emin  $nb  $nd $Ado  $zmax  $cz   $ce  $phicv  $nu $Cgd $Cdr $ckaf $Q $R $m_m $Fsed_min $p_sedo

# Create element
element SSPquadUP   1     1 2 3 4    1  1.0   2.2e6 1.0 $perm $perm $eInit  1.0e-5
