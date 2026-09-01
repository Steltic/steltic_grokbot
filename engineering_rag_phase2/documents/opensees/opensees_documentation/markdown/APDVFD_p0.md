<!-- chunk_id: APDVFD_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/APDVFD.html",
 "title": "APDVFD Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "APDVFD",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/APDVFD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2019,
 "word_count": 286,
 "has_code": false,
 "has_table": false
} -->

## APDVFD Material

This command is used to construct a uniaxialMaterial model that simulates the hysteretic responses (axial load-deformation) of an asynchronous parallel double-stage viscous fluid damper (APDVFD) with specific parameters. An adaptive iterative algorithm with a high-precision accuracy has been implemented and validated to solve numerically the constitutive equations. (Specific parameters are shown in Fig. 1.)

**uniaxialMaterial APDVFD $matTag $K $G1 $G2 $Alpha $L $LC $DP $DG $N1 $N2 $DO1 $DO2 $DC $S $HP $HC <$LGap> <$NM $RelTol $AbsTol $MaxHalf>**

**Example:**

> In order to verify the reliability of the asynchronous parallel double-stage viscous fluid damper, two sets of test and simulation results are selected for verification. Material parameters are shown in the following table (Units can be arbitrarily converted, but must be unified):

Using these parameters, comparison between the experimental and simulated load-deformation curves of APDVFD1 for sinusoidal displacement increment of 80mm and a frequency f = 0.02Hz is shown in Fig. 2. The comparison between the experimental and simulated load-deformation curves of APDVFD2 for sinusoidal displacement increment of 120mm and a frequency f = 0.02Hz is shown in Fig. 3.

Code Developed by: Linlin Xie, Cantian Yang, Haoxiang Wang, Aiqun Li, Beijing University of Civil Engineering and Architecture.

References:

[1] Yang C, Wang H, Xie L, Li A, Wang X. “Experimental and theoretical investigations on an asynchronized parallel double-stage viscous fluid damper.” Structural Control and Health Monitoring,(under review).

[2] Akcelyan, S., Lignos, D. G., Hikino, T. (2018). “Adaptive Numerical Method Algorithms for Nonlinear Viscous and Bilinear Oil Damper Models Subjected to Dynamic Loading.” Soil Dynamics and Earthquake Engineering, 113, 488-502.

[3] Oohara, K., and Kasai, K. (2002), “Time-History Analysis Models for Nonlinear Viscous Dampers”, Proc. Structural Engineers World Congress (SEWC), Yokohama, JAPAN, CD-ROM, T2-2-b-3 (in Japanese).
