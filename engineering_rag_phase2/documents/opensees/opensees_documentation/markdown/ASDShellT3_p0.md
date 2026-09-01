<!-- chunk_id: ASDShellT3_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ASDShellT3.html",
 "title": "3.1.10.18. ASDShellT3 Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "ASDShellT3",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/ASDShellT3.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 6237,
 "word_count": 729,
 "has_code": false,
 "has_table": true
} -->

## 3.1.10.18. ASDShellT3 Element

This command is used to construct an ASDShellT3 element object. The ASDShellT3 element is a 3-node general purpose thick shell element with the following features:

1. The membrane behavior is based on the **ANDeS** [Felippa2003] formulation, which uses the corner rotational DOFs (drilling DOFs) to improve the membrane behavior of the element.
2. The plate bending part is treated using the **MITC3** [PSLee2004] formulation, to avoid the well known transverse shear locking behavior of thick plate elements.
3. Kinematics can be either **linear** or **corotational**. The corotational kinematics is based on the work of Felippa et al., i.e. the **EICR** [Felippa2000] [FelippaEtAl2005] (Element Independent Corotational formulation). Finite rotations are treated with Quaternions.
4. It uses 3 integration points to have a full rank for the ANDeS formulation and the MITC3 formulation. However, for computational efficiency, the user can optionally choose a single-point integration scheme. In this case, the 3 spurious zero-energy modes for the membrane behavior are constrained using the drilling DOF formulation according to **Hughes-Brezzi** [HughesEtAl1989] . This formulation constrains the drilling DOFs to the rigid body rotation via a penalty parameter as a function of the initial in-plane shear modulus. However, when using strain-softening materials, this (elastic) constraint may overstiffen the element as the in-plane shear modulus degrades. As a remedy in such a situation, the user can choose to make this constraint non-linear.

**element ASDShellT3 $eleTag $n1 $n2 $n3 $secTag <-corotational> <-reducedIntegration> <-drillingNL> <-damp $dampTag> <-local $x1 $x2 $x3>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | *integer* | unique integer tag identifying element object |
| $n1 $n2 $n3 | 3 *integer* | the three nodes defining the element (-ndm 3 -ndf 6) |
| $secTag | *integer* | unique integer tag associated with previously-defined SectionForceDeformation object |
| -corotational | *string* | optional flag, if provided, the element uses non-linear kinematics, suitable for large displacement/rotation problems. |
| -reducedIntegration | *string* | optional flag, if provided, the element uses 1-point integration rule. |
| -drillingNL | *string* | optional flag, if provided, the Hughes-Brezzi drilling DOF formulation considers the non-linear behavior of the section. Used only when -reducedIntegration is used. |
| -damp $dampTag | *string* + *integer* | optional, to activate elemental damping as per [elementalDamping](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/elementalDamping.html#elementaldamping) |
| -local $x1 $x2 $x3 | *string* + 3 *float* | optional, if provided it will be used as the local-x axis of the element (otherwise the default local X will be the direction of the 1-2 side). Note: it will be automatically normalized and projected onto the element plane. It must not be zero or parallel to the shell’s normal vector. |

Fig. 3.1.10.19 Nodes, Gauss points and local coordinate system

Note

Valid queries to the ASDShellT3 element when creating an ElementRecorder object are:

- **‘**force**’, ‘**forces**’, ‘**globalForce**’, or ‘**globalForces**’:**

  > - Internal forces at the element’s nodes.
  > - Orientation: global coordinate system.
  > - Size: 18 columns of data, 6 components for each one of the 3 nodes.
- **‘**material $secTag $secArg1 … $secArgN**’:**

  > - Section response at section **$secTag**
  > - **$secTag** is the 1-based index of the integration point (1 to 3).
  > - ‘**$secArg1 … $secArgN**’ are the arguments required by the SectionDeformationObject at the requested integration point.

Example 1 - Cantilever Bending Roll-up (corotational)

A Cantilever beam is subjected to a total end-moment about the Y axis \(M_y = n 2 \pi EI/L\), where \(n\) is the number of rotations (2 in this example).

[`figures/ASDShellT3/ASDShellT3_Example_GNL_BendingRollUp.py`](https://OpenSees.github.io/OpenSeesDocumentation/_downloads/81ebc13996fc659cf7cc6e8c00395fdb/ASDShellT3_Example_GNL_BendingRollUp.py)

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.

**Felippa2003**

> Felippa, Carlos A. “A study of optimal membrane triangles with drilling freedoms.” Computer Methods in Applied Mechanics and Engineering 192.16-18 (2003): 2125-2168. ([Link to article](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3bb24e4412df212dabb5183f0a8e9890143b9d7d))

**PSLee2004**

> Lee, Phill-Seung, and Klaus-Jürgen Bathe. “Development of MITC isotropic triangular shell finite elements.” Computers & Structures 82.11-12 (2004): 945-962. ([Link to article](https://web.mit.edu/kjb/www/Principal_Publications/Development_of_MITC_Isotropic_Triangular_Shell_Finite_Elements.pdf))

**Felippa2000**

> Felippa, Carlos A. “A systematic approach to the element-independent corotational dynamics of finite elements”. Technical Report CU-CAS-00-03, Center for Aerospace Structures, 2000. ([Link to article](https://d1wqtxts1xzle7.cloudfront.net/40660892/A_Systematic_Approach_to_the_Element-Ind20151205-15144-36jazx.pdf?1449356169=&response-content-disposition=inline%3B+filename%3DA_Systematic_Approach_to_the_Element_Ind.pdf&Expires=1611329637&Signature=DTV4RrGLOp4AWynE4kpUPHDNDuazgbqhI6KU1LR7jMBG6sqtx8McLgll918M3CeyBsjBjb7bUTz4ZVGJaoaq0B9Orhr4FVy0AMxrHlSbaTk8lnAXduaOPt~hsbJbiC5PXjSeKzYuT-8-chgyQvaB1gPlUwZ4zTBVJZocbr~Jh0zpTNF2b846iHBu9NQ2qfD5yTciVxMFjoRvOrb4H4AtVgtU~kM9TsiszQa6Vq8Amf~DivjfyB9~v7zgwiwm65PCcErFM8llNev~F1btwqNbSNJ62It7eWgMbkFe92xs6FmOkAIE8tmXnhb1tpUsCjW4kwmVCYcSAsYO4YAyj~6wig__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA))

**FelippaEtAl2005**

> Felippa, Carlos A., and Bjorn Haugen. “A unified formulation of small-strain corotational finite elements: I. Theory.” Computer Methods in Applied Mechanics and Engineering 194.21-24 (2005): 2285-2335. ([Link to article](http://www.cntech.com.cn/down/h000/h21/attach200903311026030.pdf))

**HughesEtAl1989**

> Hughes, Thomas JR, and F. Brezzi. “On drilling degrees of freedom.” Computer methods in applied mechanics and engineering 72.1 (1989): 105-121. ([Link to article](https://www.sciencedirect.com/science/article/pii/0045782589901242))
