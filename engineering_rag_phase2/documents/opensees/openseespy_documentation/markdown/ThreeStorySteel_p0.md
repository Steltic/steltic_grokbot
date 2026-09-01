<!-- chunk_id: ThreeStorySteel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ThreeStorySteel.html",
 "title": "14.1.7. Three story steel building with rigid beam-column connections and W-section",
 "category": "section",
 "command": "ThreeStorySteel",
 "doc_section": "src",
 "rel_path": "src/ThreeStorySteel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 10379,
 "word_count": 1085,
 "has_code": true,
 "has_table": false
} -->

## 14.1.7. Three story steel building with rigid beam-column connections and W-section

1. The source code is developed by [Anurag Upadhyay](https://github.com/anurag-upadhay) from University of Utah.
2. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/8d5d91915a61abfb0ffc8cb10f3799f6/SteelFrame2D.py).
3. Run the source code in your favorite Python program and should see following plot.

```
  1
  2##################################################################
  3## 2D steel frame example.
  4## 3 story steel building with rigid beam-column connections.
  5## This script uses W-section command inOpensees to create steel..
  6## .. beam-column fiber sections.
  7##
  8## By - Anurag Upadhyay, PhD Student, University of Utah.
  9## Date - 08/06/2018
 10##################################################################
 11
 12print("=========================================================")
 13print("Start 2D Steel Frame Example")
 14
 15from openseespy.opensees import *
 16
 17import numpy as np
 18import matplotlib.pyplot as plt
 19import os
 20
 21AnalysisType='Pushover'	;		#  Pushover  Gravity
 22
 23## ------------------------------
 24## Start of model generation
 25## -----------------------------
 26# remove existing model
 27wipe()
 28
 29# set modelbuilder
 30model('basic', '-ndm', 2, '-ndf', 3)
 31
 32import math
 33
 34############################################
 35### Units and Constants  ###################
 36############################################
 37
 38inch = 1;
 39kip = 1;
 40sec = 1;
 41
 42# Dependent units
 43sq_in = inch*inch;
 44ksi = kip/sq_in;
 45ft = 12*inch;
 46
 47# Constants
 48g = 386.2*inch/(sec*sec);
 49pi = math.acos(-1);
 50
 51#######################################
 52##### Dimensions
 53#######################################
 54
 55# Dimensions Input
 56H_story=10.0*ft;
 57W_bayX=16.0*ft;
 58W_bayY_ab=5.0*ft+10.0*inch;
 59W_bayY_bc=8.0*ft+4.0*inch;
 60W_bayY_cd=5.0*ft+10.0*inch;
 61
 62# Calculated dimensions
 63W_structure=W_bayY_ab+W_bayY_bc+W_bayY_cd;
 64
 65################
 66### Material
 67################
 68
 69# Steel02 Material
 70
 71matTag=1;
 72matConnAx=2;
 73matConnRot=3;
 74
 75Fy=60.0*ksi;		# Yield stress
 76Es=29000.0*ksi;		# Modulus of Elasticity of Steel
 77v=0.2;				# Poisson's ratio
 78Gs=Es/(1+v);		# Shear modulus
 79b=0.10;				# Strain hardening ratio
 80params=[18.0,0.925,0.15]		# R0,cR1,cR2
 81R0=18.0
 82cR1=0.925
 83cR2=0.15
 84a1=0.05
 85a2=1.00
 86a3=0.05
 87a4=1.0
 88sigInit=0.0
 89alpha=0.05
 90
 91uniaxialMaterial('Steel02', matTag, Fy, Es, b, R0, cR1, cR2, a1, a2, a3, a4, sigInit)
 92
 93# ##################
 94# ## Sections
 95# ##################
 96
 97colSecTag1=1;
 98colSecTag2=2;
 99beamSecTag1=3;
100beamSecTag2=4;
101beamSecTag3=5;
102
103# COMMAND: section('WFSection2d', secTag, matTag, d, tw, bf, tf, Nfw, Nff)
104
105section('WFSection2d', colSecTag1, matTag, 10.5*inch, 0.26*inch, 5.77*inch, 0.44*inch, 15, 16)		# outer Column
106section('WFSection2d', colSecTag2, matTag, 10.5*inch, 0.26*inch, 5.77*inch, 0.44*inch, 15, 16)		# Inner Column
107
108section('WFSection2d', beamSecTag1, matTag, 8.3*inch, 0.44*inch, 8.11*inch, 0.685*inch, 15, 15)		# outer Beam
109section('WFSection2d', beamSecTag2, matTag, 8.2*inch, 0.40*inch, 8.01*inch, 0.650*inch, 15, 15)		# Inner Beam
110section('WFSection2d', beamSecTag3, matTag, 8.0*inch, 0.40*inch, 7.89*inch, 0.600*inch, 15, 15)		# Inner Beam
111
112# Beam size - W10x26
113Abeam=7.61*inch*inch;
114IbeamY=144.*(inch**4);			# Inertia along horizontal axis
115IbeamZ=14.1*(inch**4);			# inertia along vertical axis
116
117# BRB input data
118Acore=2.25*inch;
119Aend=10.0*inch;
120LR_BRB=0.55;
121
122# ###########################
123# ##### Nodes
124# ###########################
125
126# Create All main nodes
127node(1, 0.0, 0.0)
128node(2, W_bayX, 0.0)
129node(3, 2*W_bayX, 0.0)
130
131node(11, 0.0, H_story)
132node(12, W_bayX, H_story)
133node(13, 2*W_bayX, H_story)
134
135node(21, 0.0, 2*H_story)
136node(22, W_bayX, 2*H_story)
137node(23, 2*W_bayX, 2*H_story)
138
139node(31, 0.0, 3*H_story)
140node(32, W_bayX, 3*H_story)
141node(33, 2*W_bayX, 3*H_story)
142
143# Beam Connection nodes
144
145node(1101, 0.0, H_story)
146node(1201, W_bayX, H_story)
147node(1202, W_bayX, H_story)
148node(1301, 2*W_bayX, H_story)
149
150node(2101, 0.0, 2*H_story)
151node(2201, W_bayX, 2*H_story)
152node(2202, W_bayX, 2*H_story)
153node(2301, 2*W_bayX, 2*H_story)
154
155node(3101, 0.0, 3*H_story)
156node(3201, W_bayX, 3*H_story)
157node(3202, W_bayX, 3*H_story)
158node(3301, 2*W_bayX, 3*H_story)
159
160# ###############
161#  Constraints
162# ###############
163
164fix(1, 1, 1, 1)
165fix(2, 1, 1, 1)
166fix(3, 1, 1, 1)
167
168# #######################
169# ### Elements
170# #######################
171
172# ### Assign beam-integration tags
173
174ColIntTag1=1;
175ColIntTag2=2;
176BeamIntTag1=3;
177BeamIntTag2=4;
178BeamIntTag3=5;
179
180beamIntegration('Lobatto', ColIntTag1, colSecTag1, 4)
181beamIntegration('Lobatto', ColIntTag2, colSecTag2, 4)
182beamIntegration('Lobatto', BeamIntTag1, beamSecTag1, 4)
183beamIntegration('Lobatto', BeamIntTag2, beamSecTag2, 4)
184beamIntegration('Lobatto', BeamIntTag3, beamSecTag3, 4)
185
186# Assign geometric transformation
187
188ColTransfTag=1
189BeamTranfTag=2
190
191geomTransf('PDelta', ColTransfTag)
192geomTransf('Linear', BeamTranfTag)
193
194
195# Assign Elements  ##############
196
197# ## Add non-linear column elements
198element('forceBeamColumn', 1, 1, 11, ColTransfTag, ColIntTag1, '-mass', 0.0)
199element('forceBeamColumn', 2, 2, 12, ColTransfTag, ColIntTag2, '-mass', 0.0)
200element('forceBeamColumn', 3, 3, 13, ColTransfTag, ColIntTag1, '-mass', 0.0)
201
202element('forceBeamColumn', 11, 11, 21, ColTransfTag, ColIntTag1, '-mass', 0.0)
203element('forceBeamColumn', 12, 12, 22, ColTransfTag, ColIntTag2, '-mass', 0.0)
204element('forceBeamColumn', 13, 13, 23, ColTransfTag, ColIntTag1, '-mass', 0.0)
205
206element('forceBeamColumn', 21, 21, 31, ColTransfTag, ColIntTag1, '-mass', 0.0)
207element('forceBeamColumn', 22, 22, 32, ColTransfTag, ColIntTag2, '-mass', 0.0)
208element('forceBeamColumn', 23, 23, 33, ColTransfTag, ColIntTag1, '-mass', 0.0)
209
210#
211
212#  ### Add linear main beam elements, along x-axis
213#element('elasticBeamColumn', 101, 1101, 1201, Abeam, Es, Gs, Jbeam, IbeamY, IbeamZ, beamTransfTag, '-mass', 0.0)
214
215element('forceBeamColumn', 101, 1101, 1201, BeamTranfTag, BeamIntTag1, '-mass', 0.0)
216element('forceBeamColumn', 102, 1202, 1301, BeamTranfTag, BeamIntTag1, '-mass', 0.0)
217
218element('forceBeamColumn', 201, 2101, 2201, BeamTranfTag, BeamIntTag2, '-mass', 0.0)
219element('forceBeamColumn', 202, 2202, 2301, BeamTranfTag, BeamIntTag2, '-mass', 0.0)
220
221element('forceBeamColumn', 301, 3101, 3201, BeamTranfTag, BeamIntTag3, '-mass', 0.0)
222element('forceBeamColumn', 302, 3202, 3301, BeamTranfTag, BeamIntTag3, '-mass', 0.0)
223
224# Assign constraints between beam end nodes and column nodes (RIgid beam column connections)
225equalDOF(11, 1101, 1,2,3)
226equalDOF(12, 1201, 1,2,3)
227equalDOF(12, 1202, 1,2,3)
228equalDOF(13, 1301, 1,2,3)
229
230equalDOF(21, 2101, 1,2,3)
231equalDOF(22, 2201, 1,2,3)
232equalDOF(22, 2202, 1,2,3)
233equalDOF(23, 2301, 1,2,3)
234
235equalDOF(31, 3101, 1,2,3)
236equalDOF(32, 3201, 1,2,3)
237equalDOF(32, 3202, 1,2,3)
238equalDOF(33, 3301, 1,2,3)
239
240
241################
242## Gravity Load
243################
244# create TimeSeries
245timeSeries("Linear", 1)
246
247# create a plain load pattern
248pattern("Plain", 1, 1)
249
250# Create the nodal load
251load(11, 0.0, -5.0*kip, 0.0)
252load(12, 0.0, -6.0*kip, 0.0)
253load(13, 0.0, -5.0*kip, 0.0)
254
255load(21, 0., -5.*kip, 0.0)
256load(22, 0., -6.*kip,0.0)
257load(23, 0., -5.*kip, 0.0)
258
259load(31, 0., -5.*kip, 0.0)
260load(32, 0., -6.*kip, 0.0)
261load(33, 0., -5.*kip, 0.0)
262
263
264# ------------------------------
265# Start of analysis generation
266# ------------------------------
267
268NstepsGrav = 10
269
270system("BandGEN")
271numberer("Plain")
272constraints("Plain")
273integrator("LoadControl", 1.0/NstepsGrav)
274algorithm("Newton")
275test('NormUnbalance',1e-8, 10)
276analysis("Static")
277
278
279# perform the analysis
280data = np.zeros((NstepsGrav+1,2))
281for j in range(NstepsGrav):
282    analyze(1)
283    data[j+1,0] = nodeDisp(31,2)
284    data[j+1,1] = getLoadFactor(1)*5
285
286loadConst('-time', 0.0)
287
288print("Gravity analysis complete")
289
290wipeAnalysis()
291
292###############################
293### PUSHOVER ANALYSIS
294###############################
295
296if(AnalysisType=="Pushover"):
297
298	print("<<<< Running Pushover Analysis >>>>")
299
300	# Create load pattern for pushover analysis
301	# create a plain load pattern
302	pattern("Plain", 2, 1)
303
304	load(11, 1.61, 0.0, 0.0)
305	load(21, 3.22, 0.0, 0.0)
306	load(31, 4.83, 0.0, 0.0)
307
308	ControlNode=31
309	ControlDOF=1
310	MaxDisp=0.15*H_story
311	DispIncr=0.1
312	NstepsPush=int(MaxDisp/DispIncr)
313
314	system("ProfileSPD")
315	numberer("Plain")
316	constraints("Plain")
317	integrator("DisplacementControl", ControlNode, ControlDOF, DispIncr)
318	algorithm("Newton")
319	test('NormUnbalance',1e-8, 10)
320	analysis("Static")
321
322	PushDataDir = r'PushoverOut'
323	if not os.path.exists(PushDataDir):
324		os.makedirs(PushDataDir)
325	recorder('Node', '-file', "PushoverOut/Node2React.out", '-closeOnWrite', '-node', 2, '-dof',1, 'reaction')
326	recorder('Node', '-file', "PushoverOut/Node31Disp.out", '-closeOnWrite', '-node', 31, '-dof',1, 'disp')
327	recorder('Element', '-file', "PushoverOut/BeamStress.out", '-closeOnWrite', '-ele', 102, 'section', '4', 'fiber','1', 'stressStrain')
328
329	# analyze(NstepsPush)
330
331	# Perform pushover analysis
332	dataPush = np.zeros((NstepsPush+1,5))
333	for j in range(NstepsPush):
334		analyze(1)
335		dataPush[j+1,0] = nodeDisp(31,1)
336		reactions()
337		dataPush[j+1,1] = nodeReaction(1, 1) + nodeReaction(2, 1) + nodeReaction(3, 1)
338
339	plt.plot(dataPush[:,0], -dataPush[:,1])
340	plt.xlim(0, MaxDisp)
341	plt.xticks(np.linspace(0,MaxDisp,5,endpoint=True))
342	plt.yticks(np.linspace(0, -int(dataPush[NstepsPush,1]),10,endpoint=True))
343	plt.grid(linestyle='dotted')
344	plt.xlabel('Top Displacement (inch)')
345	plt.ylabel('Base Shear (kip)')
346	plt.show()
347
348
349	print("Pushover analysis complete")
350
351
352
353
```
