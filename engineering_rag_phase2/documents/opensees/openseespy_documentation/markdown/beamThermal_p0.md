<!-- chunk_id: beamThermal_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/beamThermal.html",
 "title": "14.5.1. Restrained beam under thermal expansion",
 "category": "general",
 "command": "beamThermal",
 "doc_section": "src",
 "rel_path": "src/beamThermal.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2427,
 "word_count": 281,
 "has_code": true,
 "has_table": false
} -->

## 14.5.1. Restrained beam under thermal expansion

1. The original model can be found [here](https://www.wiki.ed.ac.uk/display/opensees/Restrained+beam+under+thermal+expansion).
2. The Pypton source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/6f3619de93e27e08a51bb8021fb03513/beamThermal.py).
3. Make sure the [numpy](http://www.numpy.org/) and [matplotlib](https://matplotlib.org/) packages are installed in your Python distribution.
4. Run the source code in your favorate Python program and should see

```
 1from openseespy.opensees import *
 2
 3import numpy as np
 4import matplotlib.pyplot as plt
 5
 6# define model
 7model('basic', '-ndm', 2, '-ndf', 3)
 8
 9#define node
10node(1, 0.0, 0.0)
11node(2, 2.0, 0.0)
12node(3, 1.0, 0.0)
13
14#define boundary condition
15fix(1, 1, 1, 1)
16fix(2, 1, 1, 1)
17fix(3, 0, 1, 1)
18
19#define an elastic material with Tag=1 and E=2e11.
20matTag = 1
21uniaxialMaterial('Steel01Thermal', 1, 2e11, 2e11, 0.01)
22
23#define fibred section Two fibres: fiber $yLoc $zLoc $A $matTag
24secTag = 1
25section('FiberThermal',secTag)
26fiber(-0.025, 0.0, 0.005, matTag)
27fiber(0.025, 0.0, 0.005, matTag)
28
29#define coordinate transforamtion
30#three transformation types can be chosen: Linear, PDelta, Corotational)
31transfTag = 1
32geomTransf('Linear', transfTag)
33
34# beam integration
35np = 3
36biTag = 1
37beamIntegration('Lobatto',biTag, secTag, np)
38
39#define beam element
40element('dispBeamColumnThermal', 1, 1, 3, transfTag, biTag)
41element('dispBeamColumnThermal', 2, 3, 2, transfTag, biTag)
42
43# define time series
44tsTag = 1
45timeSeries('Linear',tsTag)
46
47# define load pattern
48patternTag = 1
49maxtemp = 1000.0
50pattern('Plain', patternTag, tsTag)
51eleLoad('-ele', 1, '-type', '-beamThermal', 1000.0, -0.05, 1000.0, 0.05)
52#eleLoad -ele 2 -type -beamThermal 0 -0.05 0 0.05
53
54# define analysis
55incrtemp = 0.01
56system('BandGeneral')
57constraints('Plain')
58numberer('Plain')
59test('NormDispIncr', 1.0e-3,  100, 1)
60algorithm('Newton')
61integrator('LoadControl', incrtemp)
62analysis('Static')
63
64# analysis
65nstep = 100
66temp = [0.0]
67disp = [0.0]
68for i in range(nstep):
69    if analyze(1) < 0:
70        break
71
72    temp.append(getLoadFactor(patternTag)*maxtemp)
73    disp.append(nodeDisp(3,1))
74
75
76plt.plot(temp,disp,'-o')
77plt.xlabel('Temperature')
78plt.ylabel('Nodal displacement')
79plt.grid()
80plt.show()
```
