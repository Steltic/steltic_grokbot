<!-- chunk_id: SAniSandMS_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/SAniSandMS.html",
 "title": "3.1.6.13. SANISAND-MS Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "SAniSandMS",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/SAniSandMS.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 12977,
 "word_count": 1884,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.13. SANISAND-MS Material

**Code Developed by**: [Haoyuan Liu](https://www.linkedin.com/in/haoyuan-liu-059500171/?originalSubdomain=nl) (Norwegian Geotechnical Institute (NGI), formerly TUDelft), [José A. Abell](http://www.joseabell.com) (UANDES, Chile), [Andrea Diambra](https://research-information.bris.ac.uk/en/persons/andrea-diambra) (University of Bristol), and [Federico Pisanò](https://www.tudelft.nl/citg/over-faculteit/afdelingen/geoscience-engineering/sections/geo-engineering/staff/academic-staff/dr-f-federico-pisano) (TU Delft).

This command is used to construct a multi-dimensional SANISAND-MS (`SAniSandMS`) material, which is an extension of the Manzari-Dafalias (SAniSand) model with cyclic ratcheting control using the memory-surface (MS) concept. This allows capturing the ratcheting effects in sands that occur in high-cyclic loading in the presence of a static stress field or in the case of assymetric loading.

TCL command:

nDMaterial SAniSandMS  $matTag $G0 $nu $e_init $Mc $c $lambda_c $e0 $ksi $P_atm $m $h0 $ch $nb $A0 $nd $zeta $mu0 $beta $Den $fabric_flag $flow_flag $intScheme $TanType $JacoType $TolF $TolR

Please report bugs as an issue on the main OpenSees repositoy and tag `@jaabell`

Where,

| Argument | Type | Description |
| --- | --- | --- | --- |
| $matTag | *integer* | unique tag identifying material |
| $G0 | *float* | dimensionless shear modulus constant |
| $nu | *float* | Poisson ratio |
| $e_init | *float* | initial void ratio |
| $Mc | *float* | critical state stress ratio |
| $c | *float* | ratio of critical state stress ratio in extension and compression |
| $lambda_c | *float* | critical state line constant |
| $e0 | *float* | reference critical void ratio at p = 0 |
| $ksi | *float* | critical state line constant |
| $P_atm | *float* | atmospheric pressure |
| $m | *float* | yield locus opening parameter (radius of yield surface in stress ratio space) |
| $h0 | *float* | hardening parameter |
| $ch | *float* | hardening parameter |
| $nb | *float* | bounding surface void ratio dependence parameter $nb ≥ 0 |
| $A0 | *float* | intrinsic dilatancy parameter |
| $nd | *float* | dilatancy surface parameter $nd ≥ 0 |
| $zeta | *float* | memory surface shrinkage parameter |
| $mu0 | *float* | ratcheting parameter |
| $beta | *float* | dilatancy memory parameter |
| $Den | *float* | mass density of the material |
| $fabric_flag | *integer* | (deprecated) |
| $flow_flag | *integer* | (deprecated) |
| $intScheme | *integer* | constitutive integration method (3: Runge-Kutta 4th order with error control (the only one currently implemented)) |
| $TanType | *integer* | type of tangent stiffness to report (0: elastic stiffness \| 1: continuum elastoplastic stiffness ) |
| $JacoType | *integer* | placeholder (not used in explicit methods) |
| $TolF | *float* | tolerance for yield surface intersection calculation (stress units) |
| $TolE | *float* | (adimensional) relative error for explicit integrator |

The current implementation on SANISAND-MS uses fourth-order Runge-Kutta with error control for constitutive integration. The strain coming from a finite-element containing SANISAND-MS is applied incrementally by subdividing automatically to keep the constitutive integration error below the parameter `$TolE`. The integration error \(e\) is defined as:

\[\begin{split}e = \max\left\lbrace e_{\sigma},\, e_{\alpha} \right\rbrace \\
e_{\sigma} = \dfrac{\Vert \sigma^5 - \sigma^4 \Vert}{\Vert \sigma^4 \Vert} \\
e_{\alpha} = \dfrac{\Vert \alpha^5 - \alpha^4 \Vert}{\Vert \alpha^4 \Vert}\end{split}\]

And \(\sigma^p\) is the stress prediction using a \(p\)-th order integration formula, and likewise for the backstress \(\alpha^p\). Thus, in the code a 5-th order formula to approximate and bound the integration error, while integration advances using the fourth-order equation (RK45).

The above equations differ from those in the main reference by Liu et al. (2019) in that the use of the yield back-stress ratio \(\alpha\) is resumed here, as in Dafalias and Manzari (2004), to avoid certain numerical inconveniences.

Citation information

If you use SANISAND-MS in your published research work, please cite the main reference ([SANISAND-MS]) and also inform `jaabell` (*at* miuandes *dot* cl), to update the list of published articles and works that use the code.

Naming convention

In text documents we use the spelling SANISAND-MS, but the OpenSees implementation uses `SAniSandMS` to accomodate coding conventions in OpenSees.

Available formulations

The material formulations for the SAniSandMS object are “ThreeDimensional” and “PlaneStrain”

Recorder queries

Valid Element recorder queries are:

- `stress` returns stress tensor
- ``strain``returns strain tensor
- `alpha`  for \(\mathbf{\alpha}\), the back-stress ratio tensor for the yield surface
- `alphaM`  for \(\mathbf{\alpha^M}\), the back-stress ratio tensor for the memory surface
- `alpha_in` for \(\mathbf{\alpha_{in}}\)
- `MM` size of memory surface
- `estrain` elastic strain tensor

```
recorder Element -eleRange 1 $numElem -time -file stress.out  stress

#. Elastic or Elastoplastic response could be enforced by
   Elastic:   updateMaterialStage -material $matTag -stage 0
   Elastoplastic:   updateMaterialStage -material $matTag -stage 1
```

Example

This example, provides an asymetric drained triaxial test of the constitutive model to show the effect of ratcheting. First the sample is compressed isotropically to 200KPa, then a cyclic deviator stress is applied.

```
set test_type "drained_triaxial_cyc" ;# Used in recorders.tcl

wipe

# Create a 3D model with 4 Degrees of Freedom
model BasicBuilder -ndm 3 -ndf 3

# Confinement Stress
set pConf -200.0

# Increment of q added at constant p0 (will be the average during cyclic loading)
set delta_qav -75.0;

# Amplitude of cyclic deviatoric stress
set delta_qcyc -60.0;

set G0        110.  ; # [Adimensional]
set nu        0.05  ; # [Adimensional]
set e_init    0.72  ; # [Adimensional]
set Mc        1.27  ; # [Adimensional]
set c         0.712 ; # [Adimensional]
set lambda_c  0.049 ; # [Adimensional]
set e0        0.845 ; # [Adimensional]
set ksi       0.27  ; # [Adimensional]
set P_atm     101.3 ; # [kPa]
set m         0.01  ; # [Adimensional]
set h0        5.95  ; # [Adimensional]
set ch        1.01  ; # [Adimensional]
set nb        2.0   ; # [Adimensional]
set A0        1.06  ; # [Adimensional]
set nd        1.17  ; # [Adimensional]
set z_max     4     ; # For SAniSand [Adimensional]
set cz        0     ; # For SAniSand [Adimensional]
set mu0       260.  ; # For SAniSand [Adimensional]
set zeta      0.0005; # For SAniSand [Adimensional]
set beta      1     ; # For SAniSand [Adimensional]
set w1        0.5   ;
set w2        2     ;
set Den       1.584 ; # [Mg/m^3]
set intScheme 3     ; # Corresponds to Modified-Euler integration scheme
set TanType   1     ; # 0: elastic stiffness, 1: continuum elastoplastic stiffness
set JacoType  1     ; # Not used in explicit methods
set TolF      1.0e-6; # Tolerances, not used in explicit
set TolR      1.0e-6; # Tolerances, not used in explicit

#Reference atmospheric pressure
set P_ref $P_atm

# Create material
nDMaterial SAniSandMS  1 $G0 $nu $e_init $Mc $c $lambda_c $e0 $ksi $P_atm $m $h0 $ch $nb $A0 $nd $zeta $mu0 $beta $Den  $intScheme $TanType $JacoType $TolF $TolR
set type "RK"

# Create nodes
node 1  1.0 0.0 0.0
node 2  1.0 1.0 0.0
node 3  0.0 1.0 0.0
node 4  0.0 0.0 0.0
node 5  1.0 0.0 1.0
node 6  1.0 1.0 1.0
node 7  0.0 1.0 1.0
node 8  0.0 0.0 1.0

# Create Fixities
fix 1   0 1 1
fix 2   0 0 1
fix 3   1 0 1
fix 4   1 1 1
fix 5   0 1 0
fix 6   0 0 0
fix 7   1 0 0
fix 8   1 1 0



# Create element
#       SSPbrickUP  tag    i j k l m n p q  matTag  fBulk  fDen    k1    k2   k3   void   alpha    <b1 b2 b3>
element SSPbrick   1     1 2 3 4 5 6 7 8    1

recorder Element -file ${type}_${test_type}_stress.out -ele 1  -time stress
recorder Element -file ${type}_${test_type}_strain.out -ele 1 -time strain

# Create analysis
constraints Transformation
test        NormDispIncr 1.0e-4 20 0
algorithm   Newton
numberer    RCM
system      BandGeneral
integrator  LoadControl 0.0001
analysis    Static


# Apply confinement pressure
set pNode [expr $pConf / 4.0]
pattern Plain 1 {Series -time {0 1 100} -values {0 1 1} -factor 1} {
    load 1  $pNode  0.0    0.0
    load 2  $pNode  $pNode 0.0
    load 3  0.0     $pNode 0.0
    load 4  0.0     0.0    0.0
    load 5  $pNode  0.0    $pNode
    load 6  $pNode  $pNode $pNode
    load 7  0.0     $pNode $pNode
    load 8  0.0     0.0    $pNode
}
analyze 10000


loadConst

puts "Starting monotonic analysis"

# Apply confinement pressure
set delta_sigma_a [expr $delta_qav*2./3.]
set delta_sigma_r [expr -$delta_sigma_a/2]
set pNode2 [expr $delta_sigma_r / 4.0 ]
set pNode1 [expr $delta_sigma_a / 4.0]
pattern Plain 3 {Series -time {1 2 100} -values {0 1 1} -factor 1} {
    load 1  $pNode2  0.0     0.0
    load 2  $pNode2  $pNode2 0.0
    load 3  0.0      $pNode2 0.0
    load 4  0.0      0.0     0.0
    load 5  $pNode2  0.0     $pNode1
    load 6  $pNode2  $pNode2 $pNode1
    load 7  0.0      $pNode2 $pNode1
    load 8  0.0      0.0     $pNode1
}

integrator LoadControl 0.0001
analyze 10000


loadConst

puts "Starting cyclic analysis"

set Ncyc 1000
set NcycActuallyDo 1000
set dT      [expr 0.001]
set tmax    [expr $NcycActuallyDo]
set numStep [expr int(2.0*$tmax / $dT)]


set qlist [list 0]
set timelist [list 2]

for {set i 1} {$i <= $Ncyc} {incr i} {
   lappend qlist [expr $delta_qcyc/4.0] [expr -$delta_qcyc/4.0]
   lappend timelist [expr 2*$i + 1] [expr 2*$i + 2]
}

set tsq "{Series      -time {$timelist} -values {$qlist} }" ;#-factor 1}"
puts $tsq

# return

eval "pattern Plain 4 $tsq { load 5  0 0 1.0;  }"
eval "pattern Plain 5 $tsq { load 6  0 0 1.0;  }"
eval "pattern Plain 6 $tsq { load 7  0 0 1.0;  }"
eval "pattern Plain 7 $tsq { load 8  0 0 1.0;  }"

# Analyze and use substepping if needed
set remStep $numStep
set success 0
integrator  LoadControl $dT
proc subStepAnalyze {dT subStep} {
    if {$subStep > 10} {
        return -10
    }
    for {set i 1} {$i < 3} {incr i} {
        puts "Try dT = $dT"
        # set success [analyze 1 $dT]
        integrator  LoadControl $dT
        set success [analyze 1]
        if {$success != 0} {
            set success [subStepAnalyze [expr $dT/2.0] [expr $subStep+1]]
            if {$success == -10} {
                puts "Did not converge."
                return success
            }
        } else {
            if {$i==1} {
                puts "Substep $subStep : Left side converged with dT = $dT"
            } else {
                puts "Substep $subStep : Right side converged with dT = $dT"
            }
        }
    }
    return success
}

puts "Finished static Start analysis"
set startT [clock seconds]

set startTime  [getTime]
while {$success != -10} {
    set subStep 0
    integrator  LoadControl $dT
    set success [analyze $remStep  $dT]
    if {$success == 0} {
        puts "Analysis Finished"
        break
    } else {
        set curTime  [getTime]
        puts "Analysis failed at $curTime . Try substepping."
        set success  [subStepAnalyze [expr $dT/2.0] [incr subStep]]
        set curStep  [expr int(($curTime-$startTime)/$dT + 1)]
        set remStep  [expr int($numStep-$curStep)]
        puts "Current step: $curStep , Remaining steps: $remStep"
    }
}
set endT [clock seconds]
puts "loading analysis execution time: [expr $endT-$startT] seconds."

wipe
```

The script produces an output that can be visualized as follows.

**Main references**

**SANISAND-MS**

> Liu, H. Y., Abell, J. A., Diambra, A., & Pisanò, F. (2019). [Modelling the cyclic ratcheting of sands through](https://www.researchgate.net/publication/328211282_Modelling_the_cyclic_ratcheting_of_sands_through_memory-enhanced_bounding_surface_plasticity). Géotechnique, 69(9), 783-800.

**PhDThesis**

> Liu, H.Y.  (2020). [Constitutive modelling of cyclic sand behaviour for offshore foundations](https://repository.tudelft.nl/islandora/object/uuid%3A6e3ae33c-e95d-474f-8d6b-d8c0f8aa4788?collection=research) (Doctoral dissertation, Delft University of Technology).

**List of works using SANISAND-MS**

**1**

> Liu, H. Y., & Pisano, F. (2019). [Prediction of oedometer terminal densities through a memory-enhanced cyclic model for sand](https://www.icevirtuallibrary.com/doi/pdf/10.1680/jgele.18.00187). Géotechnique Letters, 9(2), 81-88.

**2**

> Liu, H. Y., Kementzetzidis, E., Abell, J. A., & Pisanò, F. (2021). [From cyclic sand ratcheting to tilt accumulation of offshore monopiles: 3D FE modelling using SANISAND-MS](https://www.icevirtuallibrary.com/doi/pdf/10.1680/jgeot.20.P.029). Géotechnique, 1-16.

**3**

> Liu, H.Y., & Kaynia, A. M. (2021). [Characteristics of cyclic undrained model SANISAND-MSu and their effects on response of monopiles for offshore wind structures](https://www.icevirtuallibrary.com/doi/pdf/10.1680/jgeot.21.00068). Géotechnique, 1-39.
