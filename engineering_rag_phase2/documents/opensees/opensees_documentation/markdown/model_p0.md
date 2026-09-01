<!-- chunk_id: model_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "",
 "title": "model",
 "category": "other",
 "manual_group": "",
 "command": "",
 "doc_section": "",
 "rel_path": "",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1586,
 "word_count": 235,
 "has_code": true,
 "has_table": false
} -->

## model

model basic -ndm 2 -ndf 2

# nodes
node 1 0 0
node 2 0 0

# a linear time series
timeSeries Linear 1

# contact element
set Kn 1.0e10
set Kt 100.0
set mu 0.5
element zeroLengthContactASDimplex 1   1 2   $Kn $Kt $mu -orient 0 1 0

# initial fixities
fix 1 1 1
fix 2 1 0

# set normal force = -10
set N -10.0
pattern Plain 1 1 {
  load 2 0.0 $N
}
constraints Transformation
numberer Plain
system FullGeneral
test NormDispIncr 1.0e-6 10 0
algorithm Newton
integrator LoadControl 1.0
analysis Static
analyze 1
loadConst -time 0.0

# remove horizontal constraint
remove sp 2 1

# apply an horizontal imposed displacement = 1
pattern Plain 2 1 {
  sp 2 1 1.0
}
constraints Transformation
numberer Plain
system FullGeneral
test NormDispIncr 1.0e-6 10 0
algorithm Newton
integrator LoadControl 0.01
analysis Static
analyze 100

# check results
reactions
set reference [expr abs($N*$mu)]
set RFx [expr abs([nodeReaction 2 1])]
set err [expr abs($RFx-$reference)/$reference]
puts "Expected X force: $reference"
puts "Obtained X force: $RFx"
puts "Relative Error: [expr $err*100.0] %"
```

Code Developed by: **Onur Deniz Akan** at IUSS, Italy & **Massimo Petracca** at ASDEA Software, Italy.

**OliverEtAl**

> Oliver, Javier, Alfredo Edmundo Huespe, and J. C. Cante. “An implicit/explicit integration scheme to increase computability of non-linear material and contact/friction problems.” Computer Methods in Applied Mechanics and Engineering 197.21-24 (2008): 1865-1889. ([Link to article](https://upcommons.upc.edu/bitstream/handle/2117/185752/2019_J_ENG_MECH_Titscher_IMPL-EX.pdf?sequence=1))
