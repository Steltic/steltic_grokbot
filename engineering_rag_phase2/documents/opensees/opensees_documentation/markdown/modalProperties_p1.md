<!-- chunk_id: modalProperties_p1 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/modalProperties.html",
 "title": "3.2.10. modalProperties Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "modalProperties",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/modalProperties.html",
 "part_index": 1,
 "part_count": 2,
 "char_count": 10256,
 "word_count": 1150,
 "has_code": true,
 "has_table": false
} -->

## 3.2.10. modalProperties Command [part 2/2]

The modal participation factor matrix \(MPF\) is a \(n_m \times ndf\) matrix (where ndf = 3 in 2D and 6 in 3D), where each row contains the modal participation factors for each DOF. The modal participation factor for a certain mode \(i\) and DOF \(j\) indicates how strongly the motion (or rotation) associated to that DOF is represented in the eigenvector \(i\)

\[MPF_{ij} = \frac{\Phi_{i}^T M T_j}{gm_{ii}}\]

where \(T_j\) defines the magnitude of the rigid body response to imposed rigid body motion (displacement or infinitesimal rotation) in the DOF \(j\). Each \(ndf \times 1\) block \(T_{nj}\) corresponds to the node \(n\) and it is defined as (for the 3D/6DOFs case):

\[\begin{split}T_{nj} =
\begin{pmatrix}
1 & 0 & 0 & 0 & d_z & -d_z \\
0 & 1 & 0 & -d_z & 0 & d_x \\
0 & 0 & 1 & d_y & -d_x & 0 \\
0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
\begin{Bmatrix}
e_1 \\
e_2 \\
e_3 \\
e_4 \\
e_5 \\
e_6 \\
\end{Bmatrix}\end{split}\]

where \(e_j\) is 1, and all other \(e_p\:(\text{with}\:p \neq j)\) are 0. \(d_x\), \(d_y\) and \(d_z\) are the distances of the node \(n\) coordinates \(X_n=\left(x, y, z\right)\) from the center of mass \(CoM=\left(x_0, y_0, z_0\right)\). Therefore, the modal participation factors accounts for the masses directly input at translational and rotational DOFs, and also the rotational masses given by the translational masses gyrating about the center of mass. Note, in fact, that even if the user does not input any rotational mass, or even if the user uses 3D solid elements with no rotational DOF, the modal participation factors associated to the rotational DOFs may be \(\neq 0\).

The modal participation mass matrix \(MPM\) is a \(n_m \times ndf\) matrix (where ndf = 3 in 2D and 6 in 3D), where each row contains the modal participation masses for each DOF. The modal participation mass for a certain mode \(i\) and DOF \(j\) is defined as

\[MPM_{ij} = \frac{\left(\Phi_{i}^T M T_j\right)^2}{gm_{ii}}\]

If the modal participation masses for each mode in a particular DOF are summed, it should give the total mass of the structure for that DOF, exlcluding the masses at fixed DOFs.

**HintonEtAl1976**

> Hinton, E., Rock, T. & Zienkiewicz, O. (1976). “A note on mass lumping and related processes in the Finite element method.” Earthquake Engineering and Structural Dynamics, 13, 9, p. A112.

Example

The following example shows how to:

- Use the modalProperties command
- Print the results on the console (-print)
- Generate a report file in the current directory (-file ‘ModalReport.txt’)
- Use a displacement-normalization for the eigenvectors

1. **Tcl Code**

```
modalProperties -print -file "ModalReport.txt" -unorm
```

1. **Python Code**

```
modalProperties('-print', '-file', 'ModalReport.txt', '-unorm')
```

For a complete example that runs an **eigenvalue analysis**, extracts the **modal properties** and runs a **response spectrum analysis**, see the documentation of the [responseSpectrumAnalysis Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/responseSpectrumAnalysis.html#responsespectrumanalysis)

ReportFile

The generated report file looks like this:

```
# MODAL ANALYSIS REPORT

* 1. DOMAIN SIZE:
# This is the size of the problem: 2 for 2D problems, 3 for 3D problems.
3

* 2. EIGENVALUE ANALYSIS:
#          MODE        LAMBDA         OMEGA     FREQUENCY        PERIOD
# ------------- ------------- ------------- ------------- -------------
              1        7578.8       87.0563       13.8554     0.0721738
              2       8484.47       92.1112       14.6599     0.0682131
              3       10518.5        102.56       16.3229     0.0612636
              4         85779       292.881       46.6134     0.0214531
              5       89260.1       298.764       47.5498     0.0210306
              6        101089       317.945       50.6025     0.0197619
              7   1.71885e+06       1311.05        208.66    0.00479249

* 3. TOTAL MASS OF THE STRUCTURE:
# The total masses (translational and rotational) of the structure
# including the masses at fixed DOFs (if any).
#            MX            MY            MZ           RMX           RMY           RMZ
# ------------- ------------- ------------- ------------- ------------- -------------
           1600          1600          1600          7200         10000         10000

* 4. TOTAL FREE MASS OF THE STRUCTURE:
# The total masses (translational and rotational) of the structure
# including only the masses at free DOFs.
#            MX            MY            MZ           RMX           RMY           RMZ
# ------------- ------------- ------------- ------------- ------------- -------------
           1600          1600          1600          7200         10000         10000

* 5. CENTER OF MASS:
# The center of mass of the structure, calculated from free masses.
#             X             Y             Z
# ------------- ------------- -------------
              2           1.5           4.5

* 6. MODAL PARTICIPATION FACTORS:
# The participation factor for a certain mode 'a' in a certain direction 'i'
# indicates how strongly displacement along (or rotation about)
# the global axes is represented in the eigenvector of that mode.
#          MODE            MX            MY            MZ           RMX           RMY           RMZ
# ------------- ------------- ------------- ------------- ------------- ------------- -------------
              1       1.20368             0             0             0      0.661418             0
              2             0      -1.20172             0      0.637456             0             0
              3             0             0             0             0             0      -2.39705
              4      0.430981             0             0             0       -1.8352             0
              5             0      -0.41375             0      -1.83591             0             0
              6             0             0             0             0             0      0.780575
              7             0             0      -1.17082             0             0             0

* 7. MODAL PARTICIPATION MASSES:
# The modal participation masses for each mode.
#          MODE            MX            MY            MZ           RMX           RMY           RMZ
# ------------- ------------- ------------- ------------- ------------- ------------- -------------
              1       1418.18             0             0             0        428.21             0
              2             0       1430.41             0        402.49             0             0
              3             0             0             0             0             0       9041.23
              4        181.82             0             0             0       3296.78             0
              5             0        169.58             0       3338.87             0             0
              6             0             0             0             0             0       958.755
              7             0             0       1515.54             0             0             0

* 8. MODAL PARTICIPATION MASSES (cumulative):
# The cumulative modal participation masses for each mode.
#          MODE            MX            MY            MZ           RMX           RMY           RMZ
# ------------- ------------- ------------- ------------- ------------- ------------- -------------
              1       1418.18             0             0             0        428.21             0
              2       1418.18       1430.41             0        402.49        428.21             0
              3       1418.18       1430.41             0        402.49        428.21       9041.23
              4          1600       1430.41             0        402.49       3724.99       9041.23
              5          1600       1599.99             0       3741.36       3724.99       9041.23
              6          1600       1599.99             0       3741.36       3724.99       9999.99
              7          1600       1599.99       1515.54       3741.36       3724.99       9999.99

* 9. MODAL PARTICIPATION MASS RATIOS (%):
# The modal participation mass ratios (%) for each mode.
#          MODE            MX            MY            MZ           RMX           RMY           RMZ
# ------------- ------------- ------------- ------------- ------------- ------------- -------------
              1        88.636             0             0             0        4.2821             0
              2             0       89.4005             0       5.59014             0             0
              3             0             0             0             0             0       90.4123
              4       11.3638             0             0             0       32.9678             0
              5             0       10.5988             0       46.3732             0             0
              6             0             0             0             0             0       9.58755
              7             0             0       94.7214             0             0             0

* 10. MODAL PARTICIPATION MASS RATIOS (%) (cumulative):
# The cumulative modal participation mass ratios (%) for each mode.
#          MODE            MX            MY            MZ           RMX           RMY           RMZ
# ------------- ------------- ------------- ------------- ------------- ------------- -------------
              1        88.636             0             0             0        4.2821             0
              2        88.636       89.4005             0       5.59014        4.2821             0
              3        88.636       89.4005             0       5.59014        4.2821       90.4123
              4       99.9997       89.4005             0       5.59014       37.2499       90.4123
              5       99.9997       99.9993             0       51.9633       37.2499       90.4123
              6       99.9997       99.9993             0       51.9633       37.2499       99.9999
              7       99.9997       99.9993       94.7214       51.9633       37.2499       99.9999
```

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy
