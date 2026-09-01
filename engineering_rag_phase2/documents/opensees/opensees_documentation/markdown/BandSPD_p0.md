<!-- chunk_id: BandSPD_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/BandSPD.html",
 "title": "3.2.3.2. BandSPD System",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "BandSPD",
 "doc_section": "user/manual/analysis/system",
 "rel_path": "user/manual/analysis/system/BandSPD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1614,
 "word_count": 275,
 "has_code": true,
 "has_table": false
} -->

## 3.2.3.2. BandSPD System

This command is used to construct a BandSPD linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems which have a banded profile. The matrix is stored as shown below in a 1 dimensional array of size equal to the (bandwidth/2) times the number of unknowns. When a solution is required, the Lapack routines DPBSV and DPBTRS are used. The following command is used to construct such a system:

**system BandSPD**

An n×n matrix is a symmetric positive definite banded matrix if:

1. \(A_{i,j}=0 \quad\mbox{if}\quad j<i-k \quad\mbox{ or }\quad j>i+k; \quad k \ge 0.\)
2. \(A_{i,j} = A_{j,i}\)
3. \(y^T A y != 0\) for all non-zero vectors y with real entries (\(y \in \mathbb{R}^n\)),

The bandwidth of the matrix is k + k + 1.

For example, a symmetric 6-by-6 matrix with a right bandwidth of 2:

\[\begin{split}\begin{bmatrix}
A_{11} & A_{12} & A_{13} &   0  & \cdots & 0 \\
& A_{22} & A_{23} & A_{24} & \ddots & \vdots \\
&        & A_{33} & A_{34} & A_{35} & 0 \\
&        &        & A_{44} & A_{45} & A_{46} \\
& sym    &        &        & A_{55} & A_{56} \\
&        &        &        &        & A_{66}
\end{bmatrix}\end{split}\]

is stored as follows:

\[\begin{split}\begin{bmatrix}
A_{11} & A_{12} & A_{13} \\
A_{22} & A_{23} & A_{24} \\
A_{33} & A_{34} & A_{35} \\
A_{44} & A_{45} & A_{46} \\
A_{55} & A_{56} & 0 \\
A_{66} & 0 & 0
\end{bmatrix}\end{split}\]

Example

The following example shows how to construct a BandSPD system

1. **Tcl Code**

```
system BandSPD
```

1. **Python Code**

```
system('BandSPD')
```

Code developed by: **fmk**
