<!-- chunk_id: PortalFrame2d_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PortalFrame2d.html",
 "title": "14.1.3. Portal Frame 2d Analysis",
 "category": "analysis",
 "command": "PortalFrame2d",
 "doc_section": "src",
 "rel_path": "src/PortalFrame2d.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 7104,
 "word_count": 898,
 "has_code": true,
 "has_table": false
} -->

## 14.1.3. Portal Frame 2d Analysis

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/8a2d670e46dbdcd4499e0ce151525495/PortalFrame2d.py).
2. Run the source code in your favorite Python program and should see results below

```
Period Comparisons:
 Period       OpenSees        SAP2000   SeismoStruct
      1        1.27321         1.2732         1.2732
      2        0.43128         0.4313         0.4313
      3        0.24204         0.2420         0.2420
      4        0.16018         0.1602         0.1602
      5        0.11899         0.1190         0.1190
      6        0.09506         0.0951         0.0951
      7        0.07951         0.0795         0.0795

 tSatic Analysis Result Comparisons:
                  Parameter       OpenSees        SAP2000   SeismoStruct
                   Disp Top          1.451           1.45           1.45
    Axial Force Bottom Left         69.987          69.99          70.01
         Moment Bottom Left       2324.677        2324.68        2324.71
 PASSED Verification Test PortalFrame2d.py
```

```
  1from openseespy.opensees import *
  2
  3from math import asin, sqrt
  4
  5# Two dimensional Frame: Eigenvalue & Static Loads
  6
  7
  8# REFERENCES:
  9# used in verification by SAP2000:
 10# SAP2000 Integrated Finite Element Analysis and Design of Structures, Verification Manual,
 11# Computers and Structures, 1997. Example 1.
 12# and seismo-struct (Example 10)
 13# SeismoStruct, Verification Report For Version 6, 2012. Example 11.
 14
 15
 16# set some properties
 17wipe()
 18
 19model('Basic', '-ndm', 2)
 20
 21# properties
 22
 23#    units kip, ft
 24
 25numBay = 2
 26numFloor = 7
 27
 28bayWidth = 360.0
 29storyHeights = [162.0, 162.0, 156.0, 156.0, 156.0, 156.0, 156.0]
 30
 31E = 29500.0
 32massX = 0.49
 33M = 0.
 34coordTransf = "Linear"  # Linear, PDelta, Corotational
 35massType = "-lMass"  # -lMass, -cMass
 36
 37beams = ['W24X160', 'W24X160', 'W24X130', 'W24X130', 'W24X110', 'W24X110', 'W24X110']
 38eColumn = ['W14X246', 'W14X246', 'W14X246', 'W14X211', 'W14X211', 'W14X176', 'W14X176']
 39iColumn = ['W14X287', 'W14X287', 'W14X287', 'W14X246', 'W14X246', 'W14X211', 'W14X211']
 40columns = [eColumn, iColumn, eColumn]
 41
 42WSection = {
 43    'W14X176': [51.7, 2150.],
 44    'W14X211': [62.1, 2670.],
 45    'W14X246': [72.3, 3230.],
 46    'W14X287': [84.4, 3910.],
 47    'W24X110': [32.5, 3330.],
 48    'W24X130': [38.3, 4020.],
 49    'W24X160': [47.1, 5120.]
 50}
 51
 52nodeTag = 1
 53
 54
 55# procedure to read
 56def ElasticBeamColumn(eleTag, iNode, jNode, sectType, E, transfTag, M, massType):
 57    found = 0
 58
 59    prop = WSection[sectType]
 60
 61    A = prop[0]
 62    I = prop[1]
 63    element('elasticBeamColumn', eleTag, iNode, jNode, A, E, I, transfTag, '-mass', M, massType)
 64
 65
 66# add the nodes
 67#  - floor at a time
 68yLoc = 0.
 69for j in range(0, numFloor + 1):
 70
 71    xLoc = 0.
 72    for i in range(0, numBay + 1):
 73        node(nodeTag, xLoc, yLoc)
 74        xLoc += bayWidth
 75        nodeTag += 1
 76
 77    if j < numFloor:
 78        storyHeight = storyHeights[j]
 79
 80    yLoc += storyHeight
 81
 82# fix first floor
 83fix(1, 1, 1, 1)
 84fix(2, 1, 1, 1)
 85fix(3, 1, 1, 1)
 86
 87# rigid floor constraint & masses
 88nodeTagR = 5
 89nodeTag = 4
 90for j in range(1, numFloor + 1):
 91    for i in range(0, numBay + 1):
 92
 93        if nodeTag != nodeTagR:
 94            equalDOF(nodeTagR, nodeTag, 1)
 95        else:
 96            mass(nodeTagR, massX, 1.0e-10, 1.0e-10)
 97
 98        nodeTag += 1
 99
100    nodeTagR += numBay + 1
101
102# add the columns
103# add column element
104geomTransf(coordTransf, 1)
105eleTag = 1
106for j in range(0, numBay + 1):
107
108    end1 = j + 1
109    end2 = end1 + numBay + 1
110    thisColumn = columns[j]
111
112    for i in range(0, numFloor):
113        secType = thisColumn[i]
114        ElasticBeamColumn(eleTag, end1, end2, secType, E, 1, M, massType)
115        end1 = end2
116        end2 += numBay + 1
117        eleTag += 1
118
119# add beam elements
120for j in range(1, numFloor + 1):
121    end1 = (numBay + 1) * j + 1
122    end2 = end1 + 1
123    secType = beams[j - 1]
124    for i in range(0, numBay):
125        ElasticBeamColumn(eleTag, end1, end2, secType, E, 1, M, massType)
126        end1 = end2
127        end2 = end1 + 1
128        eleTag += 1
129
130# calculate eigenvalues & print results
131numEigen = 7
132eigenValues = eigen(numEigen)
133PI = 2 * asin(1.0)
134
135#
136# apply loads for static analysis & perform analysis
137#
138
139timeSeries('Linear', 1)
140pattern('Plain', 1, 1)
141load(22, 20.0, 0., 0.)
142load(19, 15.0, 0., 0.)
143load(16, 12.5, 0., 0.)
144load(13, 10.0, 0., 0.)
145load(10, 7.5, 0., 0.)
146load(7, 5.0, 0., 0.)
147load(4, 2.5, 0., 0.)
148
149integrator('LoadControl', 1.0)
150algorithm('Linear')
151analysis('Static')
152analyze(1)
153
154# determine PASS/FAILURE of test
155ok = 0
156
157#
158# print pretty output of comparisons
159#
160
161#               SAP2000   SeismoStruct
162comparisonResults = [[1.2732, 0.4313, 0.2420, 0.1602, 0.1190, 0.0951, 0.0795],
163                     [1.2732, 0.4313, 0.2420, 0.1602, 0.1190, 0.0951, 0.0795]]
164print("\n\nPeriod Comparisons:")
165print('{:>10}{:>15}{:>15}{:>15}'.format('Period', 'OpenSees', 'SAP2000', 'SeismoStruct'))
166
167# formatString {%10s%15.5f%15.4f%15.4f}
168for i in range(0, numEigen):
169    lamb = eigenValues[i]
170    period = 2 * PI / sqrt(lamb)
171    print('{:>10}{:>15.5f}{:>15.4f}{:>15.4f}'.format(i + 1, period, comparisonResults[0][i], comparisonResults[1][i]))
172    resultOther = comparisonResults[0][i]
173    if abs(period - resultOther) > 9.99e-5:
174        ok - 1
175
176# print table of comparision
177#       Parameter          SAP2000   SeismoStruct
178comparisonResults = [["Disp Top", "Axial Force Bottom Left", "Moment Bottom Left"],
179                     [1.45076, 69.99, 2324.68],
180                     [1.451, 70.01, 2324.71]]
181tolerances = [9.99e-6, 9.99e-3, 9.99e-3]
182
183print("\n\nSatic Analysis Result Comparisons:")
184print('{:>30}{:>15}{:>15}{:>15}'.format('Parameter', 'OpenSees', 'SAP2000', 'SeismoStruct'))
185for i in range(3):
186    response = eleResponse(1, 'forces')
187    if i == 0:
188        result = nodeDisp(22, 1)
189    elif i == 1:
190        result = abs(response[1])
191    else:
192        result = response[2]
193
194    print('{:>30}{:>15.3f}{:>15.2f}{:>15.2f}'.format(comparisonResults[0][i],
195                                                     result,
196                                                     comparisonResults[1][i],
197                                                     comparisonResults[2][i]))
198    resultOther = comparisonResults[1][i]
199    tol = tolerances[i]
200    if abs(result - resultOther) > tol:
201        ok - 1
202        print("failed-> ", i, abs(result - resultOther), tol)
203
204if ok == 0:
205    print("PASSED Verification Test PortalFrame2d.py \n\n")
206else:
207    print("FAILED Verification Test PortalFrame2d.py \n\n")
208
```
