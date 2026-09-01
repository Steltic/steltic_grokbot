<!-- chunk_id: UniformDamping_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/elementalDamping/UniformDamping.html",
 "title": "3.1.13.3.1. Uniform Damping",
 "category": "command_manual",
 "manual_group": "model",
 "command": "UniformDamping",
 "doc_section": "user/manual/model/damping/elementalDamping",
 "rel_path": "user/manual/model/damping/elementalDamping/UniformDamping.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4157,
 "word_count": 576,
 "has_code": true,
 "has_table": true
} -->

## 3.1.13.3.1. Uniform Damping

This command is used to construct a uniform damping model.

**damping Uniform $dampingTag $dampingRatio $freql $freq2 <-activateTime $Ta> <-deactivateTime $Td> <-fact $tsTagScaleFactorVsTime>**

| Argument | Type | Description |
| --- | --- | --- |
| $dampingTag | *integer* | integer tag identifying damping |
| $dampingRatio | *float* | target equivalent viscous damping ratio |
| $freql | *float* | lower bound of the frequency range (in units of T^−1) |
| $freq2 | *float* | upper bound of the frequency range (in units of T^−1) |
| $Ta | *float* | time when the damping is activated |
| $Td | *float* | time when the damping is deactivated |
| $tsTagScaleFactorVsTime | *integer* | time series tag identifying the scale factor of the damping versus time |

Fig. 3.1.13.1 Uniform Damping

Example

The following is used to construct a uniform damping with damping ratio of **0.05** in the frequency range of **1.0** ~ **100** Hz.

```
damping Uniform 1 0.05 1.0 100.0
```

The following is an example for an SDOF system.

```
wipe;

# Create a 2D model with 3 Degrees of Freedom
model BasicBuilder -ndm 2 -ndf 3;

# Create uniform damping
# Ref. [1] Huang Y, Sturt R, Willford M. 2019. A damping model for nonlinear dynamic analysis providing uniform damping over a frequency range. Computers and Structures 212:101–9. http://dx.doi.org/10.1016/j.compstruc.2018.10.016
# Ref. [2] Tian Y, Huang Y, Qu Z, Fei Y, Lu X. 2022. High-performance uniform damping model for response history analysis in OpenSees. Journal of Earthquake Engineering. 2022. http://dx.doi.org/10.1080/13632469.2022.2124557
damping Uniform 1 0.05 0.1 100

set Tol 1.0e-8;
set numStep 1000;
set PI [expr 4.0 * atan(1.0)]
set E 1.0
set A 1.0
set L 1.0
set I 0.08
set m 1
set v 20
set k [expr $E*$A/$L]
set d0 1.0
set wn [expr sqrt($k/$m)]

# Create nodes
node 11 0 0 -mass $m $m 0
node 12 $L 0 -mass $m  $m  0

# Create Fixities
fix 11 1 1 1
fix 12 0 1 1

# Create geometric transformation
geomTransf Linear 1

# Create element
element elasticBeamColumn 1 11 12 $A $E $I 1 -damp 1

set tag 1
set tStart 0
set tEnd 100
set period 1.0
set cFactor 1.0

# Create time series
timeSeries Trig $tag $tStart $tEnd $period -factor $cFactor

# Create node recorder
recorder Node -file disp1.txt -time -node 11 12 -dof 1  disp
recorder Node -file vel1.txt -time -node 11 12 -dof 1  vel
recorder Node -file accel1.txt -timeSeries $tag -time -node 11 12 -dof 1  accel

set patternTag 10010
set dir 1

# Create Uniform Excitation load
pattern UniformExcitation $patternTag $dir -accel $tag

# Analyze
constraints Transformation;
numberer RCM;
system FullGeneral
test NormDispIncr 1e-3 100 0
algorithm NewtonLineSearch 0.75
integrator Newmark 0.5 0.25
analysis Transient
set dt 0.01
set tEQ 100
while {[getTime] < $tEQ} {analyze 1 $dt;}
```

**Code Developed by**: Yuli Huang and [Xinzheng Lu](http://www.luxinzheng.net/english.htm) (Tsinghua University).

**References**

**1**

> Huang Y, Sturt R, Willford M. 2019. [A damping model for nonlinear dynamic analysis providing uniform damping over a frequency range](https://www.researchgate.net/publication/328827267_A_damping_model_for_nonlinear_dynamic_analysis_providing_uniform_damping_over_a_frequency_range). Computers and Structures, 212:101–9. [http://dx.doi.org/10.1016/j.compstruc.2018.10.016](http://dx.doi.org/10.1016/j.compstruc.2018.10.016)

**2**

> Tian Y, Huang Y, Qu Z, Fei Y, Lu X. 2023. [High-performance uniform damping model for response history analysis in OpenSees](https://www.researchgate.net/publication/363845908_High-Performance_Uniform_Damping_Model_for_Response_History_Analysis_in_OpenSees). Journal of Earthquake Engineering. [http://dx.doi.org/10.1080/13632469.2022.2124557](http://dx.doi.org/10.1080/13632469.2022.2124557)

**3**

> Fei Y, Tian Y, Huang Y, Lu X. 2022. [Influence of damping models on dynamic analyses of a base-isolated composite structure under earthquakes and environmental vibrations](http://dx.doi.org/10.6052/j.issn.1000-4750.2021.07.0500). Engineering Mechanics, 39(3): 201-211. [http://dx.doi.org/10.6052/j.issn.1000-4750.2021.07.0500](http://dx.doi.org/10.6052/j.issn.1000-4750.2021.07.0500)
