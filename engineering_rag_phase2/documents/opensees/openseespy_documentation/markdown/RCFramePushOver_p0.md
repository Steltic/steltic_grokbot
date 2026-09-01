<!-- chunk_id: RCFramePushOver_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/RCFramePushOver.html",
 "title": "14.1.6. Reinforced Concrete Frame Pushover Analysis",
 "category": "analysis",
 "command": "RCFramePushOver",
 "doc_section": "src",
 "rel_path": "src/RCFramePushOver.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4348,
 "word_count": 521,
 "has_code": true,
 "has_table": false
} -->

## 14.1.6. Reinforced Concrete Frame Pushover Analysis

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/1ac2354e9eaac9db5ddf14cc14a1cbcd/RCFramePushOver.py).
2. The file for gravity analysis is also needed :[`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/c5216600efa55eb2f4414ae80ad646a5/RCFrameGravity.py).
3. Run the source code in your favorite Python program and should see `Passed!` in the results.

```
  1print("==========================")
  2print("Start RCFramePushover Example")
  3
  4# Units: kips, in, sec
  5#
  6# Written: GLF/MHS/fmk
  7# Date: January 2001
  8from openseespy.opensees import *
  9
 10wipe()
 11# ----------------------------------------------------
 12# Start of Model Generation & Initial Gravity Analysis
 13# ----------------------------------------------------
 14
 15# Do operations of Example3.1 by sourcing in the tcl file
 16import RCFrameGravity
 17print("Gravity Analysis Completed")
 18
 19# Set the gravity loads to be constant & reset the time in the domain
 20loadConst('-time', 0.0)
 21
 22# ----------------------------------------------------
 23# End of Model Generation & Initial Gravity Analysis
 24# ----------------------------------------------------
 25
 26
 27# ----------------------------------------------------
 28# Start of additional modelling for lateral loads
 29# ----------------------------------------------------
 30
 31# Define lateral loads
 32# --------------------
 33
 34# Set some parameters
 35H = 10.0  # Reference lateral load
 36
 37# Set lateral load pattern with a Linear TimeSeries
 38pattern('Plain', 2, 1)
 39
 40# Create nodal loads at nodes 3 & 4
 41#    nd    FX  FY  MZ
 42load(3, H, 0.0, 0.0)
 43load(4, H, 0.0, 0.0)
 44
 45# ----------------------------------------------------
 46# End of additional modelling for lateral loads
 47# ----------------------------------------------------
 48
 49
 50# ----------------------------------------------------
 51# Start of modifications to analysis for push over
 52# ----------------------------------------------------
 53
 54# Set some parameters
 55dU = 0.1  # Displacement increment
 56
 57# Change the integration scheme to be displacement control
 58#                             node dof init Jd min max
 59integrator('DisplacementControl', 3, 1, dU, 1, dU, dU)
 60
 61# ----------------------------------------------------
 62# End of modifications to analysis for push over
 63# ----------------------------------------------------
 64
 65
 66# ------------------------------
 67# Start of recorder generation
 68# ------------------------------
 69
 70# Stop the old recorders by destroying them
 71# remove recorders
 72
 73# Create a recorder to monitor nodal displacements
 74# recorder Node -file node32.out -time -node 3 4 -dof 1 2 3 disp
 75
 76# Create a recorder to monitor element forces in columns
 77# recorder EnvelopeElement -file ele32.out -time -ele 1 2 forces
 78
 79# --------------------------------
 80# End of recorder generation
 81# ---------------------------------
 82
 83
 84# ------------------------------
 85# Finally perform the analysis
 86# ------------------------------
 87
 88# Set some parameters
 89maxU = 15.0  # Max displacement
 90currentDisp = 0.0
 91ok = 0
 92
 93test('NormDispIncr', 1.0e-12, 1000)
 94algorithm('ModifiedNewton', '-initial')
 95
 96while ok == 0 and currentDisp < maxU:
 97
 98    ok = analyze(1)
 99
100    # if the analysis fails try initial tangent iteration
101    if ok != 0:
102        print("modified newton failed")
103        break
104    # print "regular newton failed .. lets try an initail stiffness for this step"
105    # test('NormDispIncr', 1.0e-12,  1000)
106    # # algorithm('ModifiedNewton', '-initial')
107    # ok = analyze(1)
108    # if ok == 0:
109    #     print "that worked .. back to regular newton"
110
111    # test('NormDispIncr', 1.0e-12,  10)
112    # algorithm('Newton')
113
114    currentDisp = nodeDisp(3, 1)
115
116results = open('results.out', 'a+')
117
118if ok == 0:
119    results.write('PASSED : RCFramePushover.py\n')
120    print("Passed!")
121else:
122    results.write('FAILED : RCFramePushover.py\n')
123    print("Failed!")
124
125results.close()
126
127# Print the state at node 3
128# print node 3
129
130
131print("==========================")
```
