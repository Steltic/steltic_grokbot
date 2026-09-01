<!-- chunk_id: modalProperties_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/modalProperties.html",
 "title": "5.10. modalProperties Command",
 "category": "general",
 "command": "modalProperties",
 "doc_section": "src",
 "rel_path": "src/modalProperties.html",
 "part_index": 0,
 "part_count": 2,
 "char_count": 10062,
 "word_count": 1480,
 "has_code": true,
 "has_table": true
} -->

## 5.10. modalProperties Command [part 1/2]

This command is used to compute the modal properties of a model after an [eigen command](https://openseespydoc.readthedocs.io/en/latest/src/eigen.html).

This command computes the following modal properties:

> - \(m_t\) : A vector with the total mass of the structure for each DOF, considering both free and fixed DOFs.
> - \(m_f\) : The total mass of the structure, but considering only the masses at free DOFs.
> - \(CoM\) : The center of mass.
> - \(gm\) : The generalized mass matrix.
> - \(MPF\) : The modal participation factors.
> - \(MPM\) : The modal participation masses.
> - \(MPMc\) : The cumulative modal participation masses.
> - \(MPM\left(\%\right)\) : The modal participation masse ratios.
> - \(MPMc\left(\%\right)\) : The cumulative modal participation masse ratios.

**modalProperties(*<'-print'>*, *<'-file'*, *reportFileName>*, *<'-unorm'>*, *<'-return'>*)**

| Argument | Type | Description |
| --- | --- | --- |
| `'-print'` | ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Optional. If included, a report of the modal properties is printed to the console. |
| `'-file'` | ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Optional. If included, a report of the modal properties is printed to the file `reportFileName`. |
| `reportFileName` | ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Optional, but mandatory if the -file option is included. Indicates the filename for the report. If the file does not exist, it will be created. If the file exists, it will be overwritten. |
| `'-unorm'` | ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Optional. If included, the computation of the modal properties will be carried out using a displacement-normalized version of the eigenvectors. |
| `'-return'` | ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Optional. If included, a report of the modal properties will be returned as a dict object to Python. |

Return value with `'-return'` (In next version 3.4.0.3 or later)

```
{
   # list of one int value
   "domainSize": [ndm],

   # list of lambda values for all modes
   "eigenLambda": [lambdas],

   # list of omega values for all modes
   "eigenOmega": [omega],

   # list of frequency values for all modes
   "eigenFrequency": [frequency],

   # list of period values for all modes
   "eigenPeriod": [period],

   # list of total mass values, [MX] for 1D, [MX, MY, RMZ] for 2D,
   # [MX, MY, MZ, MRX, RMY, RMZ] for 3D
   "totalMass": [mass],

   # list of total mass values for free DOFs, [MX] for 1D,
   # [MX, MY, RMZ] for 2D,  [MX, MY, MZ, MRX, RMY, RMZ] for 3D
   "totalFreeMass": [mass],

   # coordinates of mass center, [X] for 1D, [X, Y] for 2D,
   # [X, Y, Z] for 3D
   "centerOfMass": [center],

   #
   # modal participation factors for all modes
   #

   # for MX direction for 1D, 2D and 3D
   "partiFactorMX": [factor],

   # for MY direction for 2D and 3D
   "partiFactorMY": [factor],

   # for MZ direction for 3D
   "partiFactorMZ": [factor],

   # for RMX direction for 3D
   "partiFactorRMX": [factor],

   # for RMY direction for 3D
   "partiFactorRMY": [factor],

   # for RMZ direction for 2D and 3D
   "partiFactorRMX": [factor],

   #
   # modal participation masses for all modes
   #

   # for MX direction for 1D, 2D and 3D
   "partiMassMX": [mass],

   # for MY direction for 2D and 3D
   "partiMassMY": [mass],

   # for MZ direction for 3D
   "partiMassMZ": [mass],

   # for RMX direction for 3D
   "partiMassRMX": [mass],

   # for RMY direction for 3D
   "partiMassRMY": [mass],

   # for RMZ direction for 2D and 3D
   "partiMassRMX": [mass],

   #
   # modal participation masses (cumulative) for all modes
   #

   # for MX direction for 1D, 2D and 3D
   "partiMassesCumuMX": [mass],

   # for MY direction for 2D and 3D
   "partiMassesCumuMY": [mass],

   # for MZ direction for 3D
   "partiMassesCumuMZ": [mass],

   # for RMX direction for 3D
   "partiMassesCumuRMX": [mass],

   # for RMY direction for 3D
   "partiMassesCumuRMY": [mass],

   # for RMZ direction for 2D and 3D
   "partiMassesCumuRMZ": [mass],

   #
   # modal participation mass ratios (%) for all modes
   #

   # for MX direction for 1D, 2D and 3D
   "partiMassRatiosMX": [mass],

   # for MY direction for 2D and 3D
   "partiMassRatiosMY": [mass],

   # for MZ direction for 3D
   "partiMassRatiosMZ": [mass],

   # for RMX direction for 3D
   "partiMassRatiosRMX": [mass],

   # for RMY direction for 3D
   "partiMassRatiosRMY": [mass],

   # for RMZ direction for 2D and 3D
   "partiMassRatiosRMX": [mass],

   #
   # modal participation mass ratios (%) (cumulative) for all modes
   #

   # for MX direction for 1D, 2D and 3D
   "partiMassRatiosCumuMX": [mass],

   # for MY direction for 2D and 3D
   "partiMassRatiosCumuMY": [mass],

   # for MZ direction for 3D
   "partiMassRatiosCumuMZ": [mass],

   # for RMX direction for 3D
   "partiMassRatiosCumuRMX": [mass],

   # for RMY direction for 3D
   "partiMassRatiosCumuRMY": [mass],

   # for RMZ direction for 2D and 3D
   "partiMassRatiosCumuRMX": [mass],
}
```

Note

- This command can be used only if a previous call to [eigen command](https://openseespydoc.readthedocs.io/en/latest/src/eigen.html) has been performed.
- This command has only optional arguments, and they can be given in any order. Note, however, that the only requirement is that the `reportFileName` must follow the `'-file'` option if used.
- The modal properties are computed and stored in the `Domain` object, so that they can be accessed later in the [responseSpectrumAnalysis Command](https://openseespydoc.readthedocs.io/en/latest/src/responseSpectrumAnalysis.html).
- This command directly accesses the mass matrix of the model, so it accounts for both nodal masses and element’s (distributed) masses. And the element mass matrix can be either lumped or consistent.
- The global mass matrix is then stored into a temporary sparse matrix storage, so it can be used for both small and large models.
- This command can be used for both 2D problems (-ndm = 2, -ndf = 2 or 3) and 3D problems (-ndm = 3, -ndf = 3, 4 or 6). In both cases the algorithm computes rotational masses. If a node has rotational DOFs, the rotational masses account for both the direct rotational masses (i.e. those input by the user at rotational DOFs) and the effect of translational masses gyrating about the center of mass. If a node has no rotational DOF, only the latter is considered.
- Only the values in \(gm\) and \(MPF\) depend on the normalization of the eigenvectors. This normalization depends on the solver used in the [eigen command](https://openseespydoc.readthedocs.io/en/latest/src/eigen.html). The default `'-genBandArpack'` uses a mass-normalization, so that the \(gm\) is the identity. On the contrary, the `'-fullGenLapack'` uses a displacement-normalization, so that the largest component of the eigenvector is 1. If you use the `'-genBandArpack'`, but want a displacement-normalization of the eigenvectors, use the `'-unorm'` option.

#### 5.10.1. Theory

The eigenvalues \(\lambda\) and the eigenvectors \(\Phi\) can be obtained after solving the *generalized eigenvalue problem* for two symmetric matrices \(K\) (stiffness) and \(M\) (mass) given by:

\[\left (K - \lambda M \right ) \Phi = 0\]

The global mass matrix \(M\) is given by the assembly of \(n\) elemental and nodal mass matrices \(m_e\):

\[M = \bigwedge_{i=1}^{n}m_e\]

\(M\) is not necessarily diagonal, because some elemental matrices \(m_e\) may be consistent. However, the computation of \(CoM\), \(m_t\) and \(m_f\) requires a lumped version of \(M\). The global lumped mass matrix \(LM\) can be computed by the assembly of a diagonalized version of the elemental mass matrices \(m_e\):

\[LM = \bigwedge_{i=1}^{n}diag\left(m_e\right)\]

\(diag\left(m_e\right)\) cannot be computed just by summing the summing the components of each row (in beams or solid with higher order interpolation, this would produces negative terms on the diagonal mass matrix that would be unphysical).

Instead we use the **HRZ** algorithm [HintonEtAl1976], named after the authors Hinton, Rock and Zienkiewicz: *“The procedure of lumping recommended in view of the infinite possibilities offered by condition (5) is to compute the diagonal terms of the consistent mass matrix and then scale these terms so as to preserve the total mass of the element”*.

The procedure is as follows:

> - compute \(DM\), a vector containing the sum of each row of \(m_e\).
> - compute \(SM\), a vector of size=ndf, obtained summing the components in \(DM\) pertaining to the same DOF (i to ndf). This procedures allows to obtain the total elemental mass for each DOF.
> - compute \(DC\), a vector containing only the diagonal terms in the consistent mass matrix \(m_e\).
> - compute \(SC\), a vector of size=ndf, obtained summing the components in \(DC\) pertaining to the same DOF (i to ndf).
> - now we can obtain the scale factors for each dof \(i\) as: \(SM_i/SC_i\).
> - scale each diagonal term of the consistent mass matrix \(DC_j\) using the scale factor of the respective DOF \(SM_i/SC_i\):
>
>   \(diag\left(m_e\right)_j = DC_j \cdot SM_i/SC_i\).

The center of mass \(CoM\) and the total masses \(m_t\) and \(m_f\) of the structure, for each node \(n\) with position \(X_n\) and each DOF \(i\), can now be easily computed from \(LM\):

\[\begin{split}m_{t_i} &= \sum_{n=1}^{Nnodes} LM_{ni}\\
m_{f_i} &= \sum_{n=1}^{Nnodes} LM_{ni}\quad(\text{if}\:i = free)\\
CoM_i &= \frac{\sum_{n=1}^{Nnodes} X_{ni} \cdot LM_{ni}}{m_{f_i}} \quad(\text{if}\:i = free)\end{split}\]

The generalized mass matrix is

\[gm = \Phi^T M \Phi\]

If the default solver is used in the [eigen command](https://openseespydoc.readthedocs.io/en/latest/src/eigen.html) (-genBandArpack), and the option **-unorm** is not used, the eigenvectors are mass-normalized and \(gm\) will be an identity matrix, i.e. a diagonal matrix whose diagonal entries are = 1, and whose size is \(n_m \times n_m\) (where \(n_m\) is the number of requested eigenvalues).
