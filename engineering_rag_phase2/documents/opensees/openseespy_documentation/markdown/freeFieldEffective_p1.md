<!-- chunk_id: freeFieldEffective_p1 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/freeFieldEffective.html",
 "title": "14.4.2. Effective Stress Site Response Analysis of a Layered Soil Column",
 "category": "analysis",
 "command": "freeFieldEffective",
 "doc_section": "src",
 "rel_path": "src/freeFieldEffective.html",
 "part_index": 1,
 "part_count": 2,
 "char_count": 21270,
 "word_count": 2067,
 "has_code": true,
 "has_table": false
} -->

## 14.4.2. Effective Stress Site Response Analysis of a Layered Soil Column [part 2/2]

```
  1# -*- coding: utf-8 -*-
  2"""
  3Created on Fri Jan 29 16:39:41 2021
  4
  5@author: harsh
  6"""
  7import numpy as np
  8import math as mm
  9import opensees as op
 10import time as tt
 11##################################################################
 12#                                                                #
 13# Effective stress site response analysis for a layered          #
 14# soil profile located on a 2% slope and underlain by an         #
 15# elastic half-space.  9-node quadUP elements are used.          #
 16# The finite rigidity of the elastic half space is               #
 17# considered through the use of a viscous damper at the          #
 18# base.                                                          #
 19#                                                                #
 20#    Converted to openseespy by: Harsh Mistry                    #
 21#                                The University of Manchester    #
 22#                                                                #
 23#   Created by:  Chris McGann                                    #
 24#                HyungSuk Shin                                   #
 25#                Pedro Arduino                                   #
 26#                Peter Mackenzie-Helnwein                        #
 27#              --University of Washington--                      #
 28#                                                                #
 29# ---> Basic units are kN and m   (unless specified)             #
 30#                                                                #
 31##################################################################
 32#-----------------------------------------------------------------------------------------
 33#  1. DEFINE SOIL AND MESH GEOMETRY
 34#-----------------------------------------------------------------------------------------
 35
 36op.wipe()
 37nodes_dict = dict()
 38
 39#---SOIL GEOMETRY
 40# thicknesses of soil profile (m)
 41soilThick = 30.0
 42# number of soil layers
 43numLayers = 3
 44# layer thicknesses
 45layerThick=[20.0,8.0,2.0]
 46
 47# depth of water table
 48waterTable = 2.0
 49
 50# define layer boundaries
 51layerBound=np.zeros((numLayers,1))
 52layerBound[0]=layerThick[0];
 53for i in range(1,numLayers):
 54    layerBound[i]=layerBound[i-1]+layerThick[i]
 55
 56#---MESH GEOMETRY
 57# number of elements in horizontal direction
 58nElemX = 1
 59# number of nodes in horizontal direction
 60nNodeX =2 * nElemX+1
 61# horizontal element size (m)
 62sElemX = 2.0
 63
 64# number of elements in vertical direction for each layer
 65nElemY = [40,16,4]
 66
 67# total number of elements in vertical direction
 68nElemT = 60
 69
 70sElemY = np.zeros((numLayers,1))
 71# vertical element size in each layer
 72for i in range(numLayers):
 73    sElemY[i] = [layerThick[i-1]/nElemY[i-1]]
 74    print('size:',sElemY[i])
 75
 76# number of nodes in vertical direction
 77nNodeY = 2 * nElemT+1
 78
 79# total number of nodes
 80nNodeT = nNodeX * nNodeY
 81
 82#-----------------------------------------------------------------------------------------
 83#  2. CREATE PORE PRESSURE NODES AND FIXITIES
 84#-----------------------------------------------------------------------------------------
 85op.model('basic', '-ndm', 2, '-ndf', 3)
 86
 87count = 1
 88layerNodeCount = 0
 89dry_Node=np.zeros((500,1))
 90node_save=np.zeros((500,1))
 91# loop over soil layers
 92for k in range(1,numLayers+1):
 93    # loop in horizontal direction
 94    for i in range(1,nNodeX+1,2):
 95       if k==1:
 96           bump = 1
 97       else:
 98           bump = 0
 99       j_end=2 * nElemY[k-1] + bump
100       for j in range(1,j_end+1,2):
101            xCoord  = (i-1) * (sElemX/2)
102            yctr    = j + layerNodeCount
103            yCoord  = (yctr-1) * (np.float(sElemY[k-1]))/2
104            nodeNum = i + ((yctr-1) * nNodeX)
105            op.node(nodeNum, xCoord, yCoord)
106
107          # output nodal information to data file
108            nodes_dict[nodeNum] = (nodeNum, xCoord, yCoord)
109            node_save[nodeNum] = np.int(nodeNum)
110          # designate nodes above water table
111            waterHeight = soilThick - waterTable
112            if yCoord >= waterHeight:
113                dry_Node[count] = nodeNum
114                count = count+1
115    layerNodeCount = yctr + 1
116
117dryNode=np.trim_zeros(dry_Node)
118Node_d=np.unique(node_save)
119Node_d=np.trim_zeros(Node_d)
120np.savetxt('Node_record.txt',Node_d)
121print('Finished creating all -ndf 3 nodes')
122print('Number of Dry Nodes:',len(dryNode))
123
124# define fixities for pore pressure nodes above water table
125for i in range(count-1):
126    n_dryNode=np.int(dryNode[i])
127    op.fix(n_dryNode, 0, 0, 1)
128
129op.fix(1, 0, 1, 0)
130op.fix(3, 0, 1, 0)
131print('Finished creating all -ndf 3 boundary conditions...')
132
133# define equal degrees of freedom for pore pressure nodes
134for i in range(1,((3*nNodeY)-2),6):
135    op.equalDOF(i, i+2, 1, 2)
136
137print("Finished creating equalDOF for pore pressure nodes...")
138
139#-----------------------------------------------------------------------------------------
140#  3. CREATE INTERIOR NODES AND FIXITIES
141#-----------------------------------------------------------------------------------------
142op.model('basic', '-ndm', 2, '-ndf', 2)
143
144xCoord = np.float(sElemX/2)
145
146# loop over soil layers
147layerNodeCount = 0
148
149for k in range(1,numLayers+1):
150    if k==1:
151        bump = 1
152    else:
153        bump = 0
154    j_end=2 * nElemY[k-1] + bump
155    for j in range(1,j_end+1,1):
156        yctr = j + layerNodeCount
157        yCoord  = (yctr-1) * (np.float(sElemY[k-1]))/2
158        nodeNum = (3*yctr) - 1
159        op.node(nodeNum, xCoord, yCoord)
160        # output nodal information to data file
161        nodes_dict[nodeNum] = (nodeNum, xCoord, yCoord)
162
163    layerNodeCount = yctr
164
165# interior nodes on the element edges
166# loop over layers
167layerNodeCount = 0
168
169for k in range(1,numLayers+1):
170    # loop in vertical direction
171    for j in range(1,((nElemY[k-1])+1)):
172        yctr     = j + layerNodeCount;
173        yCoord   = np.float(sElemY[k-1])*(yctr-0.5)
174        nodeNumL = (6*yctr) - 2
175        nodeNumR = nodeNumL + 2
176
177        op.node(nodeNumL ,0.0, yCoord)
178        op.node(nodeNumR , sElemX, yCoord)
179
180        # output nodal information to data file
181        nodes_dict[nodeNumL] = (nodeNumL ,0.0, yCoord)
182        nodes_dict[nodeNumR] = (nodeNumR , sElemX, yCoord)
183    layerNodeCount = yctr
184
185print("Finished creating all -ndf 2 nodes...")
186
187# define fixities for interior nodes at base of soil column
188op.fix(2, 0, 1)
189print('Finished creating all -ndf 2 boundary conditions...')
190
191# define equal degrees of freedom which have not yet been defined
192for i in range(1,((3*nNodeY)-6),6):
193    op.equalDOF(i  , i+1, 1, 2)
194    op.equalDOF(i+3, i+4, 1, 2)
195    op.equalDOF(i+3, i+5, 1, 2)
196
197op.equalDOF(nNodeT-2, nNodeT-1, 1, 2)
198print('Finished creating equalDOF constraints...')
199
200#-----------------------------------------------------------------------------------------
201#  4. CREATE SOIL MATERIALS
202#-----------------------------------------------------------------------------------------
203
204# define grade of slope (%)
205grade = 2.0
206slope = mm.atan(grade/100.0)
207g     = -9.81
208
209xwgt_var = g * (mm.sin(slope))
210ywgt_var = g * (mm.cos(slope))
211thick = [1.0,1.0,1.0]
212xWgt  = [xwgt_var, xwgt_var, xwgt_var]
213yWgt  = [ywgt_var, ywgt_var, ywgt_var]
214uBulk = [6.88E6,  5.06E6, 5.0E-6]
215hPerm = [1.0E-4, 1.0E-4, 1.0E-4]
216vPerm = [1.0E-4, 1.0E-4, 1.0E-4]
217
218
219# nDMaterial PressureDependMultiYield02
220# nDMaterial('PressureDependMultiYield02', matTag, nd, rho, refShearModul, refBulkModul,\
221#    frictionAng, peakShearStra, refPress, pressDependCoe, PTAng,\
222#        contrac[0], contrac[2], dilat[0], dilat[2], noYieldSurf=20.0,\
223#            *yieldSurf=[], contrac[1]=5.0, dilat[1]=3.0, *liquefac=[1.0,0.0],e=0.6, \
224#                *params=[0.9, 0.02, 0.7, 101.0], c=0.1)
225
226op.nDMaterial('PressureDependMultiYield02',3, 2, 1.8, 9.0e4, 2.2e5, 32, 0.1, \
227                                      101.0, 0.5, 26, 0.067, 0.23, 0.06, \
228                                      0.27, 20, 5.0, 3.0, 1.0, \
229                                      0.0, 0.77, 0.9, 0.02, 0.7, 101.0)
230
231op.nDMaterial('PressureDependMultiYield02', 2, 2, 2.24, 9.0e4, 2.2e5, 32, 0.1, \
232                                      101.0, 0.5, 26, 0.067, 0.23, 0.06, \
233                                      0.27, 20, 5.0, 3.0, 1.0, \
234                                      0.0, 0.77, 0.9, 0.02, 0.7, 101.0)
235
236op.nDMaterial('PressureDependMultiYield02',1, 2, 2.45, 1.3e5, 2.6e5, 39, 0.1, \
237                                      101.0, 0.5, 26, 0.010, 0.0, 0.35, \
238                                      0.0, 20, 5.0, 3.0, 1.0, \
239                                      0.0, 0.47, 0.9, 0.02, 0.7, 101.0)
240
241print("Finished creating all soil materials...")
242
243#-----------------------------------------------------------------------------------------
244#  5. CREATE SOIL ELEMENTS
245#-----------------------------------------------------------------------------------------
246
247for j in range(1,nElemT+1):
248    nI = ( 6*j) - 5
249    nJ = nI + 2
250    nK = nI + 8
251    nL = nI + 6
252    nM = nI + 1
253    nN = nI + 5
254    nP = nI + 7
255    nQ = nI + 3
256    nR = nI + 4
257
258    lowerBound = 0.0
259    for i in range(1,numLayers+1):
260        if j * sElemY[i-1] <= layerBound[i-1] and j * sElemY[i-1] > lowerBound:
261            # permeabilities are initially set at 1.0 m/s for gravity analysis,
262            op.element('9_4_QuadUP', j, nI, nJ, nK, nL, nM, nN, nP, nQ, nR, \
263                           thick[i-1], i, uBulk[i-1], 1.0, 1.0, 1.0, xWgt[i-1], yWgt[i-1])
264
265        lowerBound = layerBound[i-1]
266
267print("Finished creating all soil elements...")
268#-----------------------------------------------------------------------------------------
269#  6. LYSMER DASHPOT
270#-----------------------------------------------------------------------------------------
271
272# define dashpot nodes
273dashF =  nNodeT+1
274dashS =  nNodeT+2
275
276op.node(dashF,  0.0, 0.0)
277op.node(dashS,  0.0, 0.0)
278
279# define fixities for dashpot nodes
280op.fix(dashF, 1, 1)
281op.fix(dashS, 0, 1)
282
283# define equal DOF for dashpot and base soil node
284op.equalDOF(1, dashS,  1)
285print('Finished creating dashpot nodes and boundary conditions...')
286
287# define dashpot material
288colArea      = sElemX * thick[0]
289rockVS       = 700.0
290rockDen      = 2.5
291dashpotCoeff = rockVS * rockDen
292
293#uniaxialMaterial('Viscous', matTag, C, alpha)
294op.uniaxialMaterial('Viscous', numLayers+1, dashpotCoeff * colArea, 1)
295
296# define dashpot element
297op.element('zeroLength', nElemT+1, dashF, dashS, '-mat', numLayers+1, '-dir', 1)
298
299print("Finished creating dashpot material and element...")
300
301#-----------------------------------------------------------------------------------------
302#  7. CREATE GRAVITY RECORDERS
303#-----------------------------------------------------------------------------------------
304
305# create list for pore pressure nodes
306load_nodeList3=np.loadtxt('Node_record.txt')
307nodeList3=[]
308
309for i in range(len(load_nodeList3)):
310    nodeList3.append(np.int(load_nodeList3[i]))
311# record nodal displacment, acceleration, and porepressure
312op.recorder('Node','-file','Gdisplacement.txt','-time','-node',*nodeList3,'-dof', 1, 2, 'disp')
313op.recorder('Node','-file','Gacceleration.txt','-time','-node',*nodeList3,'-dof', 1, 2, 'accel')
314op.recorder('Node','-file','GporePressure.txt','-time','-node',*nodeList3,'-dof', 3, 'vel')
315
316# record elemental stress and strain (files are names to reflect GiD gp numbering)
317op.recorder('Element','-file','Gstress1.txt','-time','-eleRange', 1,nElemT,'material','1','stress')
318op.recorder('Element','-file','Gstress2.txt','-time','-eleRange', 1,nElemT,'material','2','stress')
319op.recorder('Element','-file','Gstress3.txt','-time','-eleRange', 1,nElemT,'material','3','stress')
320op.recorder('Element','-file','Gstress4.txt','-time','-eleRange', 1,nElemT,'material','4','stress')
321op.recorder('Element','-file','Gstress9.txt','-time','-eleRange', 1,nElemT,'material','9','stress')
322op.recorder('Element','-file','Gstrain1.txt','-time','-eleRange', 1,nElemT,'material','1','strain')
323op.recorder('Element','-file','Gstrain2.txt','-time','-eleRange', 1,nElemT,'material','2','strain')
324op.recorder('Element','-file','Gstrain3.txt','-time','-eleRange', 1,nElemT,'material','3','strain')
325op.recorder('Element','-file','Gstrain4.txt','-time','-eleRange', 1,nElemT,'material','4','strain')
326op.recorder('Element','-file','Gstrain9.txt','-time','-eleRange', 1,nElemT,'material','9','strain')
327
328print("Finished creating gravity recorders...")
329
330#-----------------------------------------------------------------------------------------
331#  8. DEFINE ANALYSIS PARAMETERS
332#-----------------------------------------------------------------------------------------
333
334#---GROUND MOTION PARAMETERS
335# time step in ground motion record
336motionDT = 0.005
337# number of steps in ground motion record
338motionSteps = 7990
339
340#---RAYLEIGH DAMPING PARAMETERS
341# damping ratio
342damp = 0.02
343# lower frequency
344omega1 = 2 * np.pi * 0.2
345# upper frequency
346omega2 = 2 * np.pi * 20
347# damping coefficients
348a0 = 2*damp*omega1*omega2/(omega1 + omega2)
349a1 = 2*damp/(omega1 + omega2)
350print("Damping Coefficients: a_0 = $a0;  a_1 = $a1")
351
352#---DETERMINE STABLE ANALYSIS TIME STEP USING CFL CONDITION
353# maximum shear wave velocity (m/s)
354vsMax = 250.0
355# duration of ground motion (s)
356duration = motionDT*motionSteps
357# minimum element size
358minSize = sElemY[0]
359
360for i in range(2,numLayers+1):
361    if sElemY[i-1] <= minSize:
362        minSize = sElemY[i-1]
363
364# trial analysis time step
365kTrial = minSize/(vsMax**0.5)
366# define time step and number of steps for analysis
367if motionDT <= kTrial:
368    nSteps = motionSteps
369    dT     = motionDT
370else:
371    nSteps = np.int(mm.floor(duration/kTrial)+1)
372    dT     = duration/nSteps
373
374
375print("Number of steps in analysis: $nSteps")
376print("Analysis time step: $dT")
377
378#---ANALYSIS PARAMETERS
379# Newmark parameters
380gamma = 0.5
381beta  = 0.25
382
383#-----------------------------------------------------------------------------------------
384#  9. GRAVITY ANALYSIS
385#-----------------------------------------------------------------------------------------
386# update materials to ensure elastic behavior
387op.updateMaterialStage('-material', 1, '-stage', 0)
388op.updateMaterialStage('-material', 2, '-stage', 0)
389op.updateMaterialStage('-material', 3, '-stage', 0)
390
391op.constraints('Penalty', 1.0E14, 1.0E14)
392op.test('NormDispIncr', 1e-4, 35, 1)
393op.algorithm('KrylovNewton')
394op.numberer('RCM')
395op.system('ProfileSPD')
396op.integrator('Newmark', gamma, beta)
397op.analysis('Transient')
398
399startT = tt.time()
400op.analyze(10, 5.0E2)
401print('Finished with elastic gravity analysis...')
402
403# update material to consider elastoplastic behavior
404op.updateMaterialStage('-material', 1, '-stage', 1)
405op.updateMaterialStage('-material', 2, '-stage', 1)
406op.updateMaterialStage('-material', 3, '-stage', 1)
407
408# plastic gravity loading
409op.analyze(40, 5.0e2)
410
411print('Finished with plastic gravity analysis...')
412
413#-----------------------------------------------------------------------------------------
414#  10. UPDATE ELEMENT PERMEABILITY VALUES FOR POST-GRAVITY ANALYSIS
415#-----------------------------------------------------------------------------------------
416
417# choose base number for parameter IDs which is higer than other tags used in analysis
418ctr = 10000.0
419# loop over elements to define parameter IDs
420for i in range(1,nElemT+1):
421    op.parameter(np.int(ctr+1.0), 'element', i, 'vPerm')
422    op.parameter(np.int(ctr+2.0), 'element', i, 'hPerm')
423    ctr   = ctr+2.0
424
425# update permeability parameters for each element using parameter IDs
426ctr = 10000.0
427for j in range(1,nElemT+1):
428    lowerBound = 0.0
429    for i in range(1,numLayers+1):
430        if j * sElemY[i-1] <= layerBound[i-1] and j*sElemY[i-1] > lowerBound:
431            op.updateParameter(np.int(ctr+1.0), vPerm[i-1])
432            op.updateParameter(np.int(ctr+2.0), hPerm[i-1])
433        lowerBound = layerBound[i-1]
434    ctr = ctr+2.0
435
436print("Finished updating permeabilities for dynamic analysis...")
437
438#-----------------------------------------------------------------------------------------
439#  11. CREATE POST-GRAVITY RECORDERS
440#-----------------------------------------------------------------------------------------
441
442# reset time and analysis
443op.setTime(0.0)
444op.wipeAnalysis()
445op.remove('recorders')
446
447# recorder time step
448recDT = 10*motionDT
449
450# record nodal displacment, acceleration, and porepressure
451op.recorder('Node','-file','displacement.txt','-time', '-dT',recDT,'-node',*nodeList3,'-dof', 1, 2, 'disp')
452op.recorder('Node','-file','acceleration.txt','-time', '-dT',recDT,'-node',*nodeList3,'-dof', 1, 2, 'accel')
453op.recorder('Node','-file','porePressure.txt','-time', '-dT',recDT,'-node',*nodeList3,'-dof', 3, 'vel')
454
455# record elemental stress and strain (files are names to reflect GiD gp numbering)
456op.recorder('Element','-file','stress1.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','1','stress')
457op.recorder('Element','-file','stress2.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','2','stress')
458op.recorder('Element','-file','stress3.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','3','stress')
459op.recorder('Element','-file','stress4.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','4','stress')
460op.recorder('Element','-file','stress9.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','9','stress')
461op.recorder('Element','-file','strain1.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','1','strain')
462op.recorder('Element','-file','strain2.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','2','strain')
463op.recorder('Element','-file','strain3.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','3','strain')
464op.recorder('Element','-file','strain4.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','4','strain')
465op.recorder('Element','-file','strain9.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','9','strain')
466
467print("Finished creating all recorders...")
468
469#-----------------------------------------------------------------------------------------
470#  12. DYNAMIC ANALYSIS
471#-----------------------------------------------------------------------------------------
472op.model('basic', '-ndm', 2, '-ndf', 3)
473
474# define constant scaling factor for applied velocity
475cFactor = colArea * dashpotCoeff
476
477# define velocity time history file
478velocityFile='velocityHistory';
479data_gm=np.loadtxt('velocityHistory.txt')
480#motionSteps=len(data_gm)
481#print('Number of point for GM:',motionSteps)
482
483# timeseries object for force history
484op.timeSeries('Path', 2, '-dt', motionDT, '-filePath', velocityFile+'.txt', '-factor', cFactor)
485op.pattern('Plain', 10, 2)
486op.load(1, 1.0, 0.0, 0.0)
487
488print( "Dynamic loading created...")
489
490op.constraints('Penalty', 1.0E16, 1.0E16)
491op.test('NormDispIncr', 1e-3, 35, 1)
492op.algorithm('KrylovNewton')
493op.numberer('RCM')
494op.system('ProfileSPD')
495op.integrator('Newmark', gamma, beta)
496op.rayleigh(a0, a1, 0.0, 0.0)
497op.analysis('Transient')
498
499# perform analysis with timestep reduction loop
500ok = op.analyze(nSteps,dT)
501
502# if analysis fails, reduce timestep and continue with analysis
503if ok !=0:
504    print("did not converge, reducing time step")
505    curTime = op.getTime()
506    mTime = curTime
507    print("curTime: ", curTime)
508    curStep = curTime/dT
509    print("curStep: ", curStep)
510    rStep   = (nSteps-curStep)*2.0
511    remStep = np.int((nSteps-curStep)*2.0)
512    print("remStep: ", remStep)
513    dT = dT/2.0
514    print("dT: ", dT)
515
516    ok = op.analyze(remStep, dT)
517    # if analysis fails again, reduce timestep and continue with analysis
518    if ok !=0:
519        print("did not converge, reducing time step")
520        curTime = op.getTime()
521        print("curTime: ", curTime)
522        curStep = (curTime-mTime)/dT
523        print("curStep: ", curStep)
524        remStep = np.int((rStep-curStep)*2.0)
525        print("remStep: ", remStep)
526        dT = dT/2.0
527        print("dT: ", dT)
528
529        ok = op.analyze(remStep, dT)
530
531endT = tt.time()
532print("Finished with dynamic analysis...")
533print("Analysis execution time: ",(endT-startT))
534op.wipe()
```
