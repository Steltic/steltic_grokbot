<!-- chunk_id: FSIFluidElement2D_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIFluidElement2D.html",
 "title": "3.1.10.35. FSIFluidElement2D Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "FSIFluidElement2D",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/FSIFluidElement2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4563,
 "word_count": 568,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.35. FSIFluidElement2D Element

#### 3.1.10.35.1. Description

This command is used to construct an FSIFluidElement2D element object. The FSIFluidElement2D element is a 4-node bilinear acoustic element with the following features:

1. It is based on the Eulerian pressure formulation ([[ZienkiewiczEtAl1978]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html#zienkiewiczetal1978) , [[ZienkiewiczEtAl2000]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html#zienkiewiczetal2000) , [[LøkkeEtAl2017]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html#lokkeetal2017)) for (Class I) fluid-structure interaction problems.
2. It uses a full 2x2 Gauss quadrature, and therefore has a total of 4 integration points.

#### 3.1.10.35.2. Input Parameters

**element FSIFluidElement2D $eleTag $n1 $n2 $n3 $n4 $cc**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | integer | unique integer tag identifying element object |
| $n1 $n2 $n3 $n4 | 4 integers | the four nodes defining the element (-ndm 2 -ndf 1) |
| $cc | float | speed of pressure waves in water |

Fig. 3.1.10.43 **Figure 1. Nodes, Gauss points and parent coordinate system**

#### 3.1.10.35.3. Recorders

This element does not feature specific queries for element recorders. However, you can visualize the following quantities: the **added hydrodynamic pressure**, its **first-time derivative**, and its **second-time derivative** by examining the first component of **displacement**, **velocity**, and **acceleration** at the nodes.

#### 3.1.10.35.4. Theory

For additional documentation regarding the derivation of the implemented finite elements (FSIFluidElement2D, [FSIFluidBoundaryElement2D](https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIFluidBoundaryElement2D.rst), [FSIInterfaceElement2D](https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIInterfaceElement2D.rst)) based on the Eulerian pressure formulation, please refer to the attached PDF document ([Link to PDF](https://drive.google.com/drive/folders/1QnWEC6kJrFct5korO89bqL1lcn7zi4yG))

#### 3.1.10.35.5. Example of how to define a single 2D acoustic finite element

> 1. **Tcl Code**
>
> ```
> # set up a 2D-1DOF model
> model Basic -ndm 2 -ndf 1
> node 1  0.0  0.0
> node 2  1.0  0.0
> node 3  1.0  1.0
> node 4  0.0  1.0
>
> # create the acoustic element with speed of pressure waves in water, c = 1.440000e+03
> set cc 1.440000e+03
> element FSIFluidElement2D  1  1 2 3 4  $cc
>
> # record added hydrodynamic pressures at element nodes (4 columns, 1 for each node)
> recorder Element  -xml  pressure_out.xml  -ele  1  pressure
> # record first time derivative of added hydrodynamic pressures at element nodes (4 columns, 1 for each node)
> recorder Element  -xml  dpressure_dt_out.xml  -ele  1  dpressure_dt
> ```
>
> 1. **Python Code**
>
> ```
> # set up a 2D-1DOF model
> model('Basic', '-ndm', 2, '-ndf', 1)
> node(1, 0.0, 0.0)
> node(2, 1.0, 0.0)
> node(3, 1.0, 1.0)
> node(4, 0.0, 1.0)
>
> # create the acoustic element with speed of pressure waves in water, c = 1.440000e+03
> cc = 1.440000e+03
> element('FSIFluidElement2D', 1, 1,2,3,4, cc)
>
> # record added hydrodynamic pressures at element nodes (4 columns, 1 for each node)
> recorder('Element', '-xml', 'pressure_out.xml', '-ele', 1, 'pressure')
> # record first time derivative of added hydrodynamic pressures at element nodes (4 columns, 1 for each node)
> recorder('Element', '-xml', 'dpressure_dt_out.xml', '-ele', 1, 'dpressure_dt')
> ```

Code Developed, implemented and tested by:

Massimo Petracca (ASDEA Software),

Enrique Simbort (UC San Diego),

Joel Conte (UC San Diego).

#### 3.1.10.35.6. References

**ZienkiewiczEtAl1978**

> Zienkiewicz O.C., Bettess P. (1978) “Fluid-structure dynamic interaction and wave forces. An introduction to numerical treatment”, Inter. J. Numer. Meth. Eng.., 13(1): 1–16. ([Link to article](https://onlinelibrary.wiley.com/doi/10.1002/nme.1620130102))

**ZienkiewiczEtAl2000**

> Zienkiewicz O.C., Taylor R.L. (2000) “The Finite Element Method”, Butterworth-Heinemann, Vol.1, 5th Ed., Ch.19.

**LøkkeEtAl2017**

> Løkke A., Chopra A.K. (2017) “Direct finite element method for nonlinear analysis of semi-unbounded dam–water–foundation rock systems”, Earthquake Engineering and Structural Dynamics 46(8): 1267–1285. ([Link to article](https://onlinelibrary.wiley.com/doi/abs/10.1002/eqe.2855))
