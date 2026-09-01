<!-- chunk_id: FSIInterfaceElement2D_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html",
 "title": "3.1.10.36. FSIInterfaceElement2D Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "FSIInterfaceElement2D",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/FSIInterfaceElement2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3478,
 "word_count": 459,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.36. FSIInterfaceElement2D Element

#### 3.1.10.36.1. Description

This command is used to construct an FSIInterfaceElement2D element object. The FSIInterfaceElement2D element is a 2-node linear acoustic-structure interface element object with the following features:

1. It is based on the Eulerian pressure formulation ([ZienkiewiczEtAl1978] , [ZienkiewiczEtAl2000] , [LøkkeEtAl2017] ) for (Class I) fluid-structure interaction problems.
2. It couples the structure and fluid domains.
3. It uses a 2 integration points Gauss quadrature.
4. It has three DOFs per node: two displacements and one pressure DOF. The nodes on the fluid side of the interface between the acoustic/fluid and the solid domains share the same coordinates.

#### 3.1.10.36.2. Input Parameters

**element FSIInterfaceElement2D $eleTag $n1 $n2 $rho <-thickness $thickness>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | integer | unique integer tag identifying element object |
| $n1 $n2 | 2 integers | the two nodes defining the element (-ndm 2 -ndf 3) |
| $rho | float | the mass density of the fluid domain (acoustic medium) |
| Optional: |  |  |
| $thickness | float | the thickness in 2D problems (default 1.0). |

Fig. 3.1.10.44 **Figure 1. Nodes and local coordinate system**

#### 3.1.10.36.3. Theory

For additional documentation regarding the derivation of the implemented finite elements ([FSIFluidElement2D](https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIFluidElement2D.rst), [FSIFluidBoundaryElement2D](https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIFluidBoundaryElement2D.rst), FSIInterfaceElement2D) based on the Eulerian pressure formulation, please refer to the attached PDF document ([Link to PDF](https://drive.google.com/drive/folders/1QnWEC6kJrFct5korO89bqL1lcn7zi4yG))

#### 3.1.10.36.4. Example on how to define a single interface element

> 1. **Tcl Code**
>
> ```
> # set up a 2D-3DOF model
> model Basic -ndm 2 -ndf 3
> node 11  0.0  0.0
> node 22  1.0  1.0
>
> # create the acoustic-structure interface element with input variable rhoW
> set rhoW 1.000000e+03;  # mass density of water
> element FSIInterfaceElement2D 2   11 22   $rhoW -thickness 1.0
> ```
>
> 1. **Python Code**
>
> ```
> # set up a 2D-3DOF model
> model('Basic', '-ndm', 2, '-ndf', 3)
> node(11, 0.0, 0.0)
> node(22, 1.0, 1.0)
>
> # create the acoustic-structure interface element with input variable rhoW
> rhoW = 1.000000e+03  # mass density of water
> element('FSIInterfaceElement2D', 2, 11, 22, rhoW, thickness=1.0)
> ```

Code Developed, implemented and tested by:

Massimo Petracca (ASDEA Software),

Enrique Simbort (UC San Diego),

Joel Conte (UC San Diego).

#### 3.1.10.36.5. References

**ZienkiewiczEtAl1978**

> Zienkiewicz O.C., Bettess P. (1978) “Fluid-structure dynamic interaction and wave forces. An introduction to numerical treatment”, Inter. J. Numer. Meth. Eng.., 13(1): 1–16. ([Link to article](https://onlinelibrary.wiley.com/doi/10.1002/nme.1620130102))

**ZienkiewiczEtAl2000**

> Zienkiewicz O.C., Taylor R.L. (2000) “The Finite Element Method”, Butterworth-Heinemann, Vol.1, 5th Ed., Ch.19.

**LøkkeEtAl2017**

> Løkke A., Chopra A.K. (2017) “Direct finite element method for nonlinear analysis of semi-unbounded dam–water–foundation rock systems”, Earthquake Engineering and Structural Dynamics 46(8): 1267–1285. ([Link to article](https://onlinelibrary.wiley.com/doi/abs/10.1002/eqe.2855))
