<!-- chunk_id: pm4sand_cyc_cal_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pm4sand_cyc_cal.html",
 "title": "14.4.3. PM4Sand model undrained cyclic simple shear element",
 "category": "element",
 "command": "pm4sand_cyc_cal",
 "doc_section": "src",
 "rel_path": "src/pm4sand_cyc_cal.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 11487,
 "word_count": 1390,
 "has_code": true,
 "has_table": false
} -->

## 14.4.3. PM4Sand model undrained cyclic simple shear element

1. The original model is from 2D Undrained Cyclic Direct Simple Shear Test Using One Element at University of Washington, Department of Civil and Environmental Eng by Geotechnical Eng Group L. Chen, P. Arduino - Feb 2018.
2. The Python code is converted by **Steve Xu from University of Texas at Austin** (zhongzexu@utexas.edu), and shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/35553d5f6357928dad9defb1ed836789/PM4Sand_Cyc_Cal.py).

```
  1# -*- coding: utf-8 -*-
  2"""
  3Created on Sat Apr  9 17:00:41 2022
  4
  5@author: Zhongze Xu, The University of Texas at Austin
  6
  7Openseespy code to run plane-strain stress-controlled undrained cyclic simple shear element
  8to calibrate pm4sand model
  9Basic Units are m, kN and s unless otherwise specified
 10
 11original opensees code is from:
 12
 132D Undrained Cyclic Direct Simple Shear Test Using One Element
 14University of Washington, Department of Civil and Environmental Eng
 15Geotechnical Eng Group, L. Chen, P. Arduino - Feb 2018
 16Basic Units are m, kN and s unless otherwise specified
 17
 18"""
 19# from IPython import get_ipython;
 20# get_ipython().run_line_magic('reset', '-sf')
 21
 22from datetime import datetime
 23import openseespy.opensees as op
 24import numpy as np
 25import matplotlib.pyplot as plt
 26plt.rcParams["font.family"] = "Times New Roman"
 27
 28#==============================================================================
 29#Input Variables
 30'''
 31nDMaterial('PM4Sand', matTag, Dr, G0, hpo, rho, P_atm, h0, e_max, e_min,
 32           nb, nd, Ado, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf,
 33           Q, R, m_par, F_sed, p_sed)
 34'''
 35atm = -101.325
 36sig_v0 = 2.0* atm #initial vertical stress
 37CSR = 0.2 #cyclic stress ratio
 38Cycle_max = 5 #maximxum number of cycles
 39strain_in = 5.0e-6 #strain increment
 40K0 = 0.5
 41nu = K0/(1+K0) #poisson's ratio
 42devDisp = 0.03 #cutoff shear strain
 43perm = 1e-9 #permeability
 44#==============================================================================
 45
 46#primary parameters
 47Dr = 0.5
 48G0 = 476.0
 49hpo = 0.53 #Contraction rate parameter
 50rho = 1.42 #mass density, KN/m3
 51
 52#secondary parameters
 53P_atm = 101.325
 54# all initial stress dependant parameters have negative default values
 55# and will be calculated during initialization
 56h0 = -1.0  #Variable that adjusts the ratio of plastic modulus to elastic modulus
 57e_max = 0.8
 58e_min = 0.5
 59e_ini = e_max - (e_max - e_min)*Dr #initial void ratio
 60nb = 0.5 #Bounding surface parameter, nb>=0
 61nd = 0.1 #Dilatancy surface parameter, nd>=0
 62Ado = -1.0
 63#Dilatancy parameter, will be computed at the time of initialization if input value is negative
 64z_max = -1.0 #Fabric-dilatancy tensor parameter
 65c_z = 250.0 #Fabric-dilatancy tensor parameter
 66c_e = -1.0 #Fabric-dilatancy tensor parameter
 67phi_cv = 26.0 #Critical state effective friction angle
 68g_degr = 2.0 #Variable that adjusts degradation of elastic modulus with accumulation of fabric
 69c_dr = -1.0 #Variable that controls the rotated dilatancy surface
 70c_kaf = -1.0 # Variable that controls the effect that sustained static shear stresses have on plastic modulus
 71Q = 10.0 #Critical state line parameter
 72R = 1.5 #Critical state line parameter
 73m_par = 0.01#Yield surface constant
 74F_sed = -1.0#Variable that controls the minimum value the reduction factor of the elastic moduli can get during reconsolidation
 75p_sed = -1.0#Mean effective stress up to which reconsolidation strains are enhanced
 76
 77#%%
 78#Rayleigh Damping Parameters
 79'''
 80rayleigh(alphaM, betaK, betaKinit, betaKcomm)
 81'''
 82damp = 0.02
 83omega1 = 0.2
 84omega2 = 20.0
 85a1 = 2.0*damp/(omega1+omega2) #a1 is alphaM
 86a0 = a1*omega1*omega2 #a0 is betaK
 87#%%
 88#create model
 89#Remove the existing model, important!!!
 90op.wipe()
 91
 92# set modelbuilder
 93op.model('basic', '-ndm', 2, '-ndf', 3)
 94
 95#model nodes
 96x1 = 0.0
 97y1 = 0.0
 98
 99x2 = 1.0
100y2 = 0.0
101
102x3 = 1.0
103y3 = 1.0
104
105x4 = 0.0
106y4 = 1.0
107
108#create nodes
109
110op.node(1, x1, y1)
111op.node(2, x2, y2)
112op.node(3, x3, y3)
113op.node(4, x4, y4)
114
115#boundary conditions
116op.fix(1, 1, 1, 1)
117op.fix(2, 1, 1, 1)
118op.fix(3, 0, 0, 1)
119op.fix(4, 0, 0, 1)
120op.equalDOF(3,4,1,2) #make node 3 and 4 equal displacement at degrees 1 & 2
121
122#material
123#==================================================================
124#nDMaterial('PM4Sand', matTag, D_r, G_o, h_po, Den, P_atm, h_o, e_max,
125#e_min, n_b, n_d, A_do, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf,
126#Q_bolt, R_bolt, m_par, F_sed, p_sed)
127#==================================================================
128op.nDMaterial('PM4Sand', 1, Dr, G0, hpo, rho, P_atm, h0, e_max, e_min,
129           nb, nd, Ado, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf,
130           Q, R, m_par, F_sed, p_sed)
131
132#element
133op.element('SSPquadUP',1, 1,2,3,4, 1, 1.0, 2.2e6, 1.0, perm, perm, e_ini, 1.0e-5)
134
135#create recorders
136op.recorder('Node','-file', 'Cycdisp.txt','-time', '-node',1,2,3,4,'-dof', 1, 2, 'disp')
137op.recorder('Node','-file', 'CycPP.txt','-time', '-node',1,2,3,4,'-dof', 3, 'vel')
138op.recorder('Element','-file', 'Cycstress.txt','-time','-ele', 1, 'stress')
139op.recorder('Element','-file', 'Cycstrain.txt','-time','-ele', 1, 'strain')
140#%%
141#Analysis officially starts here
142op.constraints('Transformation')
143op.test('NormDispIncr', 1.0e-5, 35, 1)
144op.algorithm('Newton')
145op.numberer('RCM')
146op.system('FullGeneral')
147op.integrator('Newmark', 5.0/6.0, 4.0/9.0)
148op.rayleigh(a1, a0, 0.0, 0.0) #modification
149op.analysis('Transient')
150
151#%%apply consolidation pressure
152pNode = sig_v0/2.0 #put confining pressure evenly on two nodes
153
154# create a plain load pattern with time series 1
155op.timeSeries('Path', 1, '-values', 0, 1, 1, '-time', 0.0, 100.0, 1.0e10)
156op.pattern("Plain", 1, 1, '-factor',1.0)
157op.load(3, 0.0, pNode, 0.0) #apply vertical pressure at y direction
158op.load(4, 0.0, pNode, 0.0)
159op.updateMaterialStage('-material', 1, '-stage', 0)
160op.analyze(100,1.0)
161vDisp = op.nodeDisp(3,2)
162b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
163print('shear stress is',b[2])
164op.timeSeries('Path', 2, '-values', 1.0, 1.0, 1.0, '-time', 100.0, 80000.0, 1.0e10, '-factor', 1.0)
165op.pattern('Plain', 2, 2,'-factor',1.0)
166op.sp(3, 2, vDisp)
167op.sp(4, 2, vDisp)
168
169#Close Drainage
170for i in range(4):
171    op.remove('sp', i+1, 3)
172    print('Node ID', i+1)
173
174
175op.analyze(25,1.0)
176b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
177print('shear stress is',b[2])
178print('Drainage is closed')
179
180op.updateMaterialStage('-material', 1, '-stage', 1)
181'''
182Note:
183The program will use the default value of a secondary parameter if
184a negative input is assigned to that parameter, e.g. Ado = -1.
185However, FirstCall is mandatory when switching from elastic to elastoplastic
186if negative inputs are assigned to stress-dependent secondary parameters,
187e.g. Ado and zmax.
188'''
189
190#setParameter('-value', 0, '-ele', elementTag, 'FirstCall', matTag)
191op.setParameter('-val', 0, '-ele', 1, 'FirstCall', '1')
192
193op.analyze(25,1.0)
194b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
195print('shear stress is',b[2])
196print('finished update fixties')
197# update Poisson's ratio for analysis
198#setParameter -value 0.3 -ele 1 poissonRatio 1
199op.setParameter('-val', 0.3, '-ele',1, 'poissonRatio', '1')
200
201
202controlDisp = 1.1 * devDisp
203numCycle = 0.25
204print('Current Number of Cycle:', numCycle)
205
206start = datetime.now()
207while (numCycle <= Cycle_max):
208    #impose 1/4 cycle: zero stress to positve max stress
209    hDisp = op.nodeDisp(3,1)
210    cur_time = op.getTime()
211    steps = controlDisp/strain_in
212    time_change = cur_time + steps
213    op.timeSeries('Path', 3,'-values', hDisp, controlDisp, controlDisp, '-time', cur_time, time_change, 1.0e10, '-factor', 1.0)
214    op.pattern('Plain', 3, 3, '-fact', 1.0)
215    op.sp(3, 1, 1.0)
216    b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
217    print('shear stress is',b[2])
218    while b[2] <= CSR*sig_v0*(-1.0): #b[2] is the shear stress, sigmaxy
219        op.analyze(1, 1.0)
220        b = op.eleResponse(1, 'stress')
221        hDisp = op.nodeDisp(3,1)
222        if hDisp >= devDisp:
223            print('loading break')
224            break
225    numCycle = numCycle + 0.25
226    hDisp = op.nodeDisp(3,1)
227    cur_time = op.getTime()
228    op.remove('loadPattern', 3)
229    op.remove('timeSeries', 3)
230    op.remove('sp', 3, 1)
231    #impose 1/2 cycle: Postive max stress to negative max stress
232    steps = (controlDisp+hDisp)/strain_in
233    time_change = cur_time + steps
234    op.timeSeries('Path', 3,'-values', hDisp, -1.0*controlDisp, -1.0*controlDisp, '-time', cur_time, time_change, 1.0e10, '-factor', 1.0)
235    op.pattern('Plain', 3, 3)
236    op.sp(3, 1, 1.0)
237    while b[2] > CSR*sig_v0:
238        op.analyze(1, 1.0)
239        b = op.eleResponse(1, 'stress')
240        print('shear stress is',b[2])
241        hDisp = op.nodeDisp(3,1)
242        if hDisp <= -1.0*devDisp:
243            print('unloading break')
244            break
245    numCycle = numCycle + 0.5
246    hDisp = op.nodeDisp(3,1)
247    cur_time = op.getTime()
248    op.remove('loadPattern', 3)
249    op.remove('timeSeries', 3)
250    op.remove('sp', 3, 1)
251    #impose 1/4 cycle
252    steps = (controlDisp+hDisp)/strain_in
253    op.timeSeries('Path', 3,'-values', hDisp, controlDisp, controlDisp, '-time', cur_time, time_change, 1.0e10, '-factor', 1.0)
254    op.pattern('Plain', 3, 3, '-fact', 1.0)
255    op.sp(3, 1, 1.0)
256    while b[2] <= 0.0: #b[2] is the shear stress, sigmaxy
257        op.analyze(1, 1.0)
258        b = op.eleResponse(1, 'stress')
259        print('shear stress is',b[2])
260        hDisp = op.nodeDisp(3,1)
261        if hDisp >= devDisp:
262            print('reloading break')
263            break
264    numCycle = numCycle + 0.25
265    print('Current Number of Cycle:', numCycle)
266    op.remove('loadPattern', 3)
267    op.remove('timeSeries', 3)
268    #op.remove('sp', 3, 1)
269
270op.wipe()
271print('Analysis is done!')
272end = datetime.now()
273run_time = end-start
274print('Computation time is' , run_time)
275#%%PostProcessing
276import pandas as pd
277df_stress = pd.read_csv('Cycstress.txt', sep=" ", header=None)
278df_strain = pd.read_csv('Cycstrain.txt', sep=" ", header=None)
279#df_PP = pd.read_csv('CycPP.txt', sep=" ", header=None)
280
281Stress_V = df_stress.iloc[:, 1].to_numpy()*(-1.0) #compression is positive
282Shear_Stress = df_stress.iloc[:, 3].to_numpy()
283Shear_Strain = df_strain.iloc[:, 3].to_numpy()*100.0
284
285fig = plt.figure(figsize=(10,18))
286ax0 = fig.add_subplot(211)
287ax0.plot(Shear_Strain, Shear_Stress, label='stress-strain', linewidth=0.8)
288ax0.set_xlabel("Shear Strain,%", fontsize=16)
289ax0.set_ylabel("Shear Stress, kPa", fontsize=16)
290ax0.legend(fontsize=16)
291
292ax1 = fig.add_subplot(212)
293ax1.plot(Stress_V, Shear_Stress, label='Stress Path', linewidth=0.8)
294ax1.set_xlabel("Vertical Stress, kPa", fontsize=16)
295ax1.set_ylabel("Shear Stress, kPa", fontsize=16)
296ax1.legend(fontsize=16)
297plt.show()
298plt.close()
```
