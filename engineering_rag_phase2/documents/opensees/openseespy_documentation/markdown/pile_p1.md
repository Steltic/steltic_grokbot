<!-- chunk_id: pile_p1 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pile.html",
 "title": "14.4.1. Laterally-Loaded Pile Foundation",
 "category": "general",
 "command": "pile",
 "doc_section": "src",
 "rel_path": "src/pile.html",
 "part_index": 1,
 "part_count": 2,
 "char_count": 27239,
 "word_count": 3421,
 "has_code": true,
 "has_table": false
} -->

## 14.4.1. Laterally-Loaded Pile Foundation [part 2/2]

```
  1# -*- coding: utf-8 -*-
  2"""
  3Created on Thu Jan 10 18:24:47 2019
  4
  5@author: pchi893
  6"""
  7
  8
  9
 10
 11##########################################################
 12#                                                         #
 13# Procedure to compute ultimate lateral resistance, p_u,  #
 14#  and displacement at 50% of lateral capacity, y50, for  #
 15#  p-y springs representing cohesionless soil.            #
 16#   Converted to openseespy by: Pavan Chigullapally       #
 17#                               University of Auckland    #
 18#                                                         #
 19#   Created by:   Hyung-suk Shin                          #
 20#                 University of Washington                #
 21#   Modified by:  Chris McGann                            #
 22#                 Pedro Arduino                           #
 23#                 Peter Mackenzie-Helnwein                #
 24#                 University of Washington                #
 25#                                                         #
 26###########################################################
 27
 28# references
 29#  American Petroleum Institute (API) (1987). Recommended Practice for Planning, Designing and
 30#   Constructing Fixed Offshore Platforms. API Recommended Practice 2A(RP-2A), Washington D.C,
 31#   17th edition.
 32#
 33# Brinch Hansen, J. (1961). "The ultimate resistance of rigid piles against transversal forces."
 34#  Bulletin No. 12, Geoteknisk Institute, Copenhagen, 59.
 35#
 36#  Boulanger, R. W., Kutter, B. L., Brandenberg, S. J., Singh, P., and Chang, D. (2003). Pile
 37#   Foundations in liquefied and laterally spreading ground during earthquakes: Centrifuge experiments
 38#   and analyses. Center for Geotechnical Modeling, University of California at Davis, Davis, CA.
 39#   Rep. UCD/CGM-03/01.
 40#
 41#  Reese, L.C. and Van Impe, W.F. (2001), Single Piles and Pile Groups Under Lateral Loading.
 42#    A.A. Balkema, Rotterdam, Netherlands.
 43
 44import math
 45
 46def get_pyParam ( pyDepth, gamma, phiDegree, b, pEleLength, puSwitch, kSwitch, gwtSwitch):
 47
 48    #----------------------------------------------------------
 49    #  define ultimate lateral resistance, pult
 50    #----------------------------------------------------------
 51
 52    # pult is defined per API recommendations (Reese and Van Impe, 2001 or API, 1987) for puSwitch = 1
 53    #  OR per the method of Brinch Hansen (1961) for puSwitch = 2
 54
 55    pi = 3.14159265358979
 56    phi = phiDegree * (pi/180)
 57    zbRatio = pyDepth / b
 58
 59    #-------API recommended method-------
 60
 61    if puSwitch == 1:
 62
 63      # obtain loading-type coefficient A for given depth-to-diameter ratio zb
 64      #  ---> values are obtained from a figure and are therefore approximate
 65        zb = []
 66        dataNum = 41
 67        for i in range(dataNum):
 68            b1 = i * 0.125
 69            zb.append(b1)
 70        As = [2.8460, 2.7105, 2.6242, 2.5257, 2.4271, 2.3409, 2.2546, 2.1437, 2.0575, 1.9589, 1.8973, 1.8111, 1.7372, 1.6632, 1.5893, 1.5277, 1.4415, 1.3799, 1.3368, 1.2690, 1.2074, 1.1581,
 71            1.1211, 1.0780, 1.0349, 1.0164, 0.9979, 0.9733, 0.9610, 0.9487, 0.9363, 0.9117, 0.8994, 0.8994, 0.8871, 0.8871, 0.8809, 0.8809, 0.8809, 0.8809, 0.8809]
 72
 73      # linear interpolation to define A for intermediate values of depth:diameter ratio
 74        for i in range(dataNum):
 75            if zbRatio >= 5.0:
 76                A = 0.88
 77            elif zb[i] <= zbRatio and zbRatio <= zb[i+1]:
 78                A = (As[i+1] - As[i])/(zb[i+1] - zb[i]) * (zbRatio-zb[i]) + As[i]
 79
 80      # define common terms
 81        alpha = phi / 2
 82        beta = pi / 4 + phi / 2
 83        K0 = 0.4
 84
 85        tan_1 = math.tan(pi / 4 - phi / 2)
 86        Ka = math.pow(tan_1 , 2)
 87
 88      # terms for Equation (3.44), Reese and Van Impe (2001)
 89        tan_2 = math.tan(phi)
 90        tan_3 = math.tan(beta - phi)
 91        sin_1 = math.sin(beta)
 92        cos_1 = math.cos(alpha)
 93        c1 = K0 * tan_2 * sin_1 / (tan_3*cos_1)
 94
 95        tan_4 = math.tan(beta)
 96        tan_5 = math.tan(alpha)
 97        c2 = (tan_4/tan_3)*tan_4 * tan_5
 98
 99        c3 = K0 * tan_4 * (tan_2 * sin_1 - tan_5)
100
101        c4 = tan_4 / tan_3 - Ka
102
103        # terms for Equation (3.45), Reese and Van Impe (2001)
104        pow_1 = math.pow(tan_4,8)
105        pow_2 = math.pow(tan_4,4)
106        c5 = Ka * (pow_1-1)
107        c6 = K0 * tan_2 * pow_2
108
109      # Equation (3.44), Reese and Van Impe (2001)
110        pst = gamma * pyDepth * (pyDepth * (c1 + c2 + c3) + b * c4)
111
112      # Equation (3.45), Reese and Van Impe (2001)
113        psd = b * gamma * pyDepth * (c5 + c6)
114
115      # pult is the lesser of pst and psd. At surface, an arbitrary value is defined
116        if pst <=psd:
117            if pyDepth == 0:
118                pu = 0.01
119
120            else:
121                pu = A * pst
122
123        else:
124            pu = A * psd
125
126      # PySimple1 material formulated with pult as a force, not force/length, multiply by trib. length
127        pult = pu * pEleLength
128
129    #-------Brinch Hansen method-------
130    elif puSwitch == 2:
131      # pressure at ground surface
132        cos_2 = math.cos(phi)
133
134        tan_6 = math.tan(pi/4+phi/2)
135
136        sin_2 = math.sin(phi)
137        sin_3 = math.sin(pi/4 + phi/2)
138
139        exp_1 = math.exp((pi/2+phi)*tan_2)
140        exp_2 = math.exp(-(pi/2-phi) * tan_2)
141
142        Kqo = exp_1 * cos_2 * tan_6 - exp_2 * cos_2 * tan_1
143        Kco = (1/tan_2) * (exp_1 * cos_2 * tan_6 - 1)
144
145      # pressure at great depth
146        exp_3 = math.exp(pi * tan_2)
147        pow_3 = math.pow(tan_2,4)
148        pow_4 = math.pow(tan_6,2)
149        dcinf = 1.58 + 4.09 * (pow_3)
150        Nc = (1/tan_2)*(exp_3)*(pow_4 - 1)
151        Ko = 1 - sin_2
152        Kcinf = Nc * dcinf
153        Kqinf = Kcinf * Ko * tan_2
154
155      # pressure at an arbitrary depth
156        aq = (Kqo/(Kqinf - Kqo))*(Ko*sin_2/sin_3)
157        KqD = (Kqo + Kqinf * aq * zbRatio)/(1 + aq * zbRatio)
158
159      # ultimate lateral resistance
160        if pyDepth == 0:
161            pu = 0.01
162        else:
163            pu = gamma * pyDepth * KqD * b
164
165      # PySimple1 material formulated with pult as a force, not force/length, multiply by trib. length
166        pult  = pu * pEleLength
167
168    #----------------------------------------------------------
169    #  define displacement at 50% lateral capacity, y50
170    #----------------------------------------------------------
171
172    # values of y50 depend of the coefficent of subgrade reaction, k, which can be defined in several ways.
173    #  for gwtSwitch = 1, k reflects soil above the groundwater table
174    #  for gwtSwitch = 2, k reflects soil below the groundwater table
175    #  a linear variation of k with depth is defined for kSwitch = 1 after API (1987)
176    #  a parabolic variation of k with depth is defined for kSwitch = 2 after Boulanger et al. (2003)
177
178    # API (1987) recommended subgrade modulus for given friction angle, values obtained from figure (approximate)
179
180    ph = [28.8, 29.5, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0]
181
182    # subgrade modulus above the water table
183    if gwtSwitch == 1:
184        k = [10, 23, 45, 61, 80, 100, 120, 140, 160, 182, 215, 250, 275]
185
186    else:
187        k = [10, 20, 33, 42, 50, 60, 70, 85, 95, 107, 122, 141, 155]
188
189    dataNum = 13
190    for i in range(dataNum):
191        if ph[i] <= phiDegree and phiDegree <= ph[i+1]:
192            khat = (k[i+1]-k[i])/(ph[i+1]-ph[i])*(phiDegree - ph[i]) + k[i]
193
194    # change units from (lb/in^3) to (kN/m^3)
195    k_SIunits = khat * 271.45
196
197    # define parabolic distribution of k with depth if desired (i.e. lin_par switch == 2)
198    sigV = pyDepth * gamma
199
200    if sigV == 0:
201         sigV = 0.01
202
203    if kSwitch == 2:
204       # Equation (5-16), Boulanger et al. (2003)
205        cSigma = math.pow(50 / sigV , 0.5)
206       # Equation (5-15), Boulanger et al. (2003)
207        k_SIunits = cSigma * k_SIunits
208
209    # define y50 based on pult and subgrade modulus k
210
211    # based on API (1987) recommendations, p-y curves are described using tanh functions.
212    #  tcl does not have the atanh function, so must define this specifically
213
214    #  i.e.  atanh(x) = 1/2*ln((1+x)/(1-x)), |x| < 1
215
216    # when half of full resistance has been mobilized, p(y50)/pult = 0.5
217    x = 0.5
218    log_1 = math.log((1+x)/(1-x))
219    atanh_value = 0.5 * log_1
220
221    # need to be careful at ground surface (don't want to divide by zero)
222    if pyDepth == 0.0:
223        pyDepth = 0.01
224
225    y50 = 0.5 * (pu/ A)/(k_SIunits * pyDepth) * atanh_value
226    # return pult and y50 parameters
227    outResult = []
228    outResult.append(pult)
229    outResult.append(y50)
230
231    return outResult
232
233#########################################################################################################################################################################
234
235#########################################################################################################################################################################
236
237###########################################################
238#                                                         #
239# Procedure to compute ultimate tip resistance, qult, and #
240#  displacement at 50% mobilization of qult, z50, for     #
241#  use in q-z curves for cohesionless soil.               #
242#   Converted to openseespy by: Pavan Chigullapally       #
243#                               University of Auckland    #
244#   Created by:  Chris McGann                             #
245#                Pedro Arduino                            #
246#                University of Washington                 #
247#                                                         #
248###########################################################
249
250# references
251#  Meyerhof G.G. (1976). "Bearing capacity and settlement of pile foundations."
252#   J. Geotech. Eng. Div., ASCE, 102(3), 195-228.
253#
254#  Vijayvergiya, V.N. (1977). "Load-movement characteristics of piles."
255#   Proc., Ports 77 Conf., ASCE, New York.
256#
257#  Kulhawy, F.H. ad Mayne, P.W. (1990). Manual on Estimating Soil Properties for
258#   Foundation Design. Electrical Power Research Institute. EPRI EL-6800,
259#   Project 1493-6 Final Report.
260
261def get_qzParam (phiDegree, b, sigV, G):
262
263    # define required constants; pi, atmospheric pressure (kPa), pa, and coeff. of lat earth pressure, Ko
264    pi = 3.14159265358979
265    pa = 101
266    sin_4 = math.sin(phiDegree * (pi/180))
267    Ko = 1 - sin_4
268
269  # ultimate tip pressure can be computed by qult = Nq*sigV after Meyerhof (1976)
270  #  where Nq is a bearing capacity factor, phi is friction angle, and sigV is eff. overburden
271  #  stress at the pile tip.
272    phi = phiDegree * (pi/180)
273
274  # rigidity index
275    tan_7 = math.tan(phi)
276    Ir = G/(sigV * tan_7)
277  # bearing capacity factor
278    tan_8 = math.tan(pi/4+phi/2)
279    sin_5 = math.sin(phi)
280    pow_4 = math.pow(tan_8,2)
281    pow_5 = math.pow(Ir,(4*sin_5)/(3*(1+sin_5)))
282    exp_4 = math.exp(pi/2-phi)
283
284    Nq = (1+2*Ko)*(1/(3-sin_5))*exp_4*(pow_4)*(pow_5)
285  # tip resistance
286    qu = Nq * sigV
287  # QzSimple1 material formulated with qult as force, not stress, multiply by area of pile tip
288    pow_6 = math.pow(b, 2)
289    qult = qu * pi*pow_6/4
290
291  # the q-z curve of Vijayvergiya (1977) has the form, q(z) = qult*(z/zc)^(1/3)
292  #  where zc is critical tip deflection given as ranging from 3-9% of the
293  #  pile diameter at the tip.
294
295  # assume zc is 5% of pile diameter
296    zc = 0.05 * b
297
298  # based on Vijayvergiya (1977) curve, z50 = 0.125*zc
299    z50 = 0.125 * zc
300
301  # return values of qult and z50 for use in q-z material
302    outResult = []
303    outResult.append(qult)
304    outResult.append(z50)
305
306    return outResult
307
308#########################################################################################################################################################################
309
310#########################################################################################################################################################################
311##########################################################
312#                                                         #
313# Procedure to compute ultimate resistance, tult, and     #
314#  displacement at 50% mobilization of tult, z50, for     #
315#  use in t-z curves for cohesionless soil.               #
316#   Converted to openseespy by: Pavan Chigullapally       #
317#                               University of Auckland    #
318#   Created by:  Chris McGann                             #
319#                University of Washington                 #
320#                                                         #
321###########################################################
322
323def get_tzParam ( phi, b, sigV, pEleLength):
324
325# references
326#  Mosher, R.L. (1984). "Load transfer criteria for numerical analysis of
327#   axial loaded piles in sand." U.S. Army Engineering and Waterways
328#   Experimental Station, Automatic Data Processing Center, Vicksburg, Miss.
329#
330#  Kulhawy, F.H. (1991). "Drilled shaft foundations." Foundation engineering
331#   handbook, 2nd Ed., Chap 14, H.-Y. Fang ed., Van Nostrand Reinhold, New York
332
333    pi = 3.14159265358979
334
335  # Compute tult based on tult = Ko*sigV*pi*dia*tan(delta), where
336  #   Ko    is coeff. of lateral earth pressure at rest,
337  #         taken as Ko = 0.4
338  #   delta is interface friction between soil and pile,
339  #         taken as delta = 0.8*phi to be representative of a
340  #         smooth precast concrete pile after Kulhawy (1991)
341
342    delta = 0.8 * phi * pi/180
343
344  # if z = 0 (ground surface) need to specify a small non-zero value of sigV
345
346    if sigV == 0.0:
347        sigV = 0.01
348
349    tan_9 = math.tan(delta)
350    tu = 0.4 * sigV * pi * b * tan_9
351
352  # TzSimple1 material formulated with tult as force, not stress, multiply by tributary length of pile
353    tult = tu * pEleLength
354
355  # Mosher (1984) provides recommended initial tangents based on friction angle
356	# values are in units of psf/in
357    kf = [6000, 10000, 10000, 14000, 14000, 18000]
358    fric = [28, 31, 32, 34, 35, 38]
359
360    dataNum = len(fric)
361
362
363	# determine kf for input value of phi, linear interpolation for intermediate values
364    if phi < fric[0]:
365        k = kf[0]
366    elif phi > fric[5]:
367        k = kf[5]
368    else:
369        for i in range(dataNum):
370            if fric[i] <= phi and phi <= fric[i+1]:
371                k = ((kf[i+1] - kf[i])/(fric[i+1] - fric[i])) * (phi - fric[i]) + kf[i]
372
373
374  # need to convert kf to units of kN/m^3
375    kSIunits =  k * 1.885
376
377  # based on a t-z curve of the shape recommended by Mosher (1984), z50 = tult/kf
378    z50 = tult / kSIunits
379
380  # return values of tult and z50 for use in t-z material
381    outResult = []
382    outResult.append(tult)
383    outResult.append(z50)
384
385    return outResult
386
387
388#########################################################################################################################################################################
389
390#########################################################################################################################################################################
391
392###########################################################
393#                                                         #
394# Static pushover of a single pile, modeled as a beam on  #
395#  a nonlinear Winkler foundation.  Lateral soil response #
396#  is described by p-y springs.  Vertical soil response   #
397#  described by t-z and q-z springs.                      #
398#   Converted to openseespy by: Pavan Chigullapally       #
399#                               University of Auckland    #
400#   Created by:  Chris McGann                             #
401#                HyungSuk Shin                            #
402#                Pedro Arduino                            #
403#                Peter Mackenzie-Helnwein                 #
404#              --University of Washington--               #
405#                                                         #
406# ---> Basic units are kN and meters                      #
407#                                                         #
408###########################################################
409
410
411import openseespy.opensees as op
412
413op.wipe()
414
415#########################################################################################################################################################################
416
417#########################################################################################################################################################################
418
419# all the units are in SI units N and mm
420
421#----------------------------------------------------------
422#  pile geometry and mesh
423#----------------------------------------------------------
424
425# length of pile head (above ground surface) (m)
426L1 = 1.0
427# length of embedded pile (below ground surface) (m)
428L2 = 20.0
429# pile diameter
430diameter = 1.0
431
432# number of pile elements
433nElePile = 84
434# pile element length
435eleSize = (L1+L2)/nElePile
436
437# number of total pile nodes
438nNodePile =  1 + nElePile
439
440#----------------------------------------------------------
441#  create spring nodes
442#----------------------------------------------------------
443# spring nodes created with 3 dim, 3 dof
444op.model('basic', '-ndm', 3, '-ndf', 3)
445
446# counter to determine number of embedded nodes
447count = 0
448
449# create spring nodes
450
451#1 to 85 are spring nodes
452
453pile_nodes = dict()
454
455for i in range(nNodePile):
456    zCoord = eleSize * i
457    if zCoord <= L2:
458        op.node(i+1, 0.0, 0.0, zCoord)
459        op.node(i+101, 0.0, 0.0, zCoord)
460        pile_nodes[i+1] = (0.0, 0.0, zCoord)
461        pile_nodes[i+101] = (0.0, 0.0, zCoord)
462        count = count + 1
463
464print("Finished creating all spring nodes...")
465
466# number of embedded nodes
467nNodeEmbed = count
468
469# spring node fixities
470for i in range(nNodeEmbed):
471    op.fix(i+1, 1, 1, 1)
472    op.fix(i+101, 0, 1, 1)
473
474print("Finished creating all spring node fixities...")
475
476#----------------------------------------------------------
477#  soil properties
478#----------------------------------------------------------
479
480# soil unit weight (kN/m^3)
481gamma = 17.0
482# soil internal friction angle (degrees)
483phi = 36.0
484# soil shear modulus at pile tip (kPa)
485Gsoil = 150000.0
486
487# select pult definition method for p-y curves
488# API (default) --> 1
489# Brinch Hansen --> 2
490puSwitch = 1
491
492# variation in coefficent of subgrade reaction with depth for p-y curves
493# API linear variation (default)   --> 1
494# modified API parabolic variation --> 2
495kSwitch = 1
496
497# effect of ground water on subgrade reaction modulus for p-y curves
498# above gwt --> 1
499# below gwt --> 2
500gwtSwitch = 1
501
502#----------------------------------------------------------
503#  create spring material objects
504#----------------------------------------------------------
505
506# p-y spring material
507
508for i in range(1 , nNodeEmbed+1):
509    # depth of current py node
510    pyDepth = L2 - eleSize * (i-1)
511    # procedure to define pult and y50
512    pyParam = get_pyParam(pyDepth, gamma, phi, diameter, eleSize, puSwitch, kSwitch, gwtSwitch)
513    pult = pyParam [0]
514    y50 = pyParam [1]
515    op.uniaxialMaterial('PySimple1', i, 2, pult, y50, 0.0)
516
517
518# t-z spring material
519for i in range(2, nNodeEmbed+1):
520  # depth of current tz node
521    pyDepth = eleSize * (i-1)
522  # vertical effective stress at current depth
523    sigV = gamma * pyDepth
524  # procedure to define tult and z50
525    tzParam = get_tzParam(phi, diameter, sigV, eleSize)
526    tult = tzParam [0]
527    z50 = tzParam [1]
528    op.uniaxialMaterial('TzSimple1', i+100, 2, tult, z50, 0.0)
529
530
531# q-z spring material
532
533  # vertical effective stress at pile tip, no water table (depth is embedded pile length)
534sigVq = gamma * L2
535  # procedure to define qult and z50
536qzParam = get_qzParam (phi, diameter, sigVq, Gsoil)
537qult = qzParam [0]
538z50q = qzParam [1]
539
540#op.uniaxialMaterial('QzSimple1', 101, 2, qult, z50q) #, 0.0, 0.0
541op.uniaxialMaterial('TzSimple1', 101, 2, qult, z50q, 0.0)
542
543print("Finished creating all p-y, t-z, and z-z spring material objects...")
544
545
546#----------------------------------------------------------
547#  create zero-length elements for springs
548#----------------------------------------------------------
549
550# element at the pile tip (has q-z spring)
551op.element('zeroLength', 1001, 1, 101, '-mat', 1, 101, '-dir', 1, 3)
552
553# remaining elements
554for i in range(2, nNodeEmbed+1):
555    op.element('zeroLength', 1000+i, i, 100+i, '-mat', i, 100+i, '-dir', 1, 3)
556
557print("Finished creating all zero-Length elements for springs...")
558
559#----------------------------------------------------------
560#  create pile nodes
561#----------------------------------------------------------
562
563# pile nodes created with 3 dimensions, 6 degrees of freedom
564op.model('basic', '-ndm', 3, '-ndf', 6)
565
566# create pile nodes
567for i in range(1, nNodePile+1):
568    zCoord = eleSize * i
569    op.node(i+200, 0.0, 0.0, zCoord)
570
571print("Finished creating all pile nodes...")
572
573# create coordinate-transformation object
574op.geomTransf('Linear', 1, 0.0, -1.0, 0.0)
575
576
577# create fixity at pile head (location of loading)
578op.fix(200+nNodePile, 0, 1, 0, 1, 0, 1)
579
580
581# create fixities for remaining pile nodes
582for i in range(201, 200+nNodePile):
583    op.fix(i, 0, 1, 0, 1, 0, 1)
584
585print("Finished creating all pile node fixities...")
586
587#----------------------------------------------------------
588#  define equal dof between pile and spring nodes
589#----------------------------------------------------------
590
591for i in range(1, nNodeEmbed+1):
592    op.equalDOF(200+i, 100+i, 1, 3)
593
594print("Finished creating all equal degrees of freedom...")
595
596#----------------------------------------------------------
597#  pile section
598#----------------------------------------------------------
599##########################################################################################################################################################################
600
601#########################################################################################################################################################################
602
603#----------------------------------------------------------
604#  create elastic pile section
605#----------------------------------------------------------
606
607secTag = 1
608E = 25000000.0
609A = 0.785
610Iz = 0.049
611Iy = 0.049
612G = 9615385.0
613J = 0.098
614
615matTag = 3000
616op.section('Elastic', 1, E, A, Iz, Iy, G, J)
617
618# elastic torsional material for combined 3D section
619op.uniaxialMaterial('Elastic', 3000, 1e10)
620
621# create combined 3D section
622secTag3D = 3
623op.section('Aggregator', secTag3D, 3000, 'T', '-section', 1)
624
625
626#########################################################################################################################################################################
627
628##########################################################################################################################################################################
629
630# elastic pile section
631#import elasticPileSection
632
633#----------------------------------------------------------
634#  create pile elements
635#----------------------------------------------------------
636op.beamIntegration('Legendre', 1, secTag3D, 3)  # we are using gauss-Legendre  integration as it is the default integration scheme used in opensees tcl (check dispBeamColumn)
637
638for i in range(201, 201+nElePile):
639    op.element('dispBeamColumn', i, i, i+1, 1, 1)
640
641print("Finished creating all pile elements...")
642
643#----------------------------------------------------------
644#  create recorders
645#----------------------------------------------------------
646
647# record information at specified increments
648timeStep = 0.5
649
650# record displacements at pile nodes
651op.recorder('Node', '-file', 'pileDisp.out','-time', '-dT', timeStep, '-nodeRange', 201, 200 + nNodePile, '-dof', 1,2,3, 'disp')
652
653# record reaction force in the p-y springs
654op.recorder('Node', '-file', 'reaction.out','-time', '-dT', timeStep, '-nodeRange', 1, nNodePile, '-dof', 1, 'reaction')
655
656# record element forces in pile elements
657op.recorder('Element', '-file', 'pileForce.out','-time', '-dT', timeStep, '-eleRange', 201, 200+nElePile, 'globalForce')
658
659print("Finished creating all recorders...")
660
661#----------------------------------------------------------
662#  create the loading
663#----------------------------------------------------------
664
665op.setTime(10.0)
666
667# apply point load at the uppermost pile node in the x-direction
668values = [0.0, 0.0, 1.0, 1.0]
669time = [0.0, 10.0, 20.0, 10000.0]
670
671nodeTag = 200+nNodePile
672loadValues = [3500.0, 0.0, 0.0, 0.0, 0.0, 0.0]
673op.timeSeries('Path', 1, '-values', *values, '-time', *time, '-factor', 1.0)
674
675op.pattern('Plain', 10, 1)
676op.load(nodeTag, *loadValues)
677
678print("Finished creating loading object...")
679
680#----------------------------------------------------------
681#  create the analysis
682#----------------------------------------------------------
683op.integrator('LoadControl', 0.05)
684op.numberer('RCM')
685op.system('SparseGeneral')
686op.constraints('Transformation')
687op.test('NormDispIncr', 1e-5, 20, 1)
688op.algorithm('Newton')
689op.analysis('Static')
690
691print("Starting Load Application...")
692op.analyze(201)
693
694print("Load Application finished...")
695#print("Loading Analysis execution time: [expr $endT-$startT] seconds.")
696
697#op.wipe
698
699op.reactions()
700Nodereactions = dict()
701Nodedisplacements = dict()
702for i in range(201,nodeTag+1):
703    Nodereactions[i] = op.nodeReaction(i)
704    Nodedisplacements[i] = op.nodeDisp(i)
705print('Node Reactions are: ', Nodereactions)
706print('Node Displacements are: ', Nodedisplacements)
707
708
709
710
711
```
