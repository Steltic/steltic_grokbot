<!-- chunk_id: eigen_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/eigen.html",
 "title": "3.2.9. eigen Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "eigen",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/eigen.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1676,
 "word_count": 265,
 "has_code": true,
 "has_table": true
} -->

## 3.2.9. eigen Command

This command is used to perform the eigenvalue analysis.

**eigen <$solver> $numEigenvalues**

| Argument | Type | Description |
| --- | --- | --- |
| $numEigenvalues | *integer* | number of eigenvalues required. |
| $solver | *string* | optional string detailing type of solver: -genBandArpack, -symmBandLapack, -fullGenLapack (default: -genBandArpack). |

Returns

A list containing the eigenvalues

Note

1. The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, the nodeEigenvector command, or the Print command.
2. The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.

#### 3.2.9.1. Theory

A *generalized eigenvalue problem* for two symmetric matrices \(K\) and \(M\) of size \(n \times n\) is given by:

\[\left (K - \lambda M \right ) \Phi = 0\]

where:

> - \(K\) is the stiffness matrix
> - \(M\) is the mass matrix
> - \(\lambda\) is the eigenvalue
> - and \(\Phi\) is the associated eigenvector

Example

The following example shows how to use the eigen command to obtain a list of eigenvalues.

1. **Tcl Code**

```
# obtain 10 eigenvalues using the default solver (-genBandArpack)
set eigenvalues [eigen 10]

# or, obtain 10 eigenvalues explicitly specifying the solver
set eigenvalues [eigen -fullGenLapack 10]
```

1. **Python Code**

```
# obtain 10 eigenvalues using the default solver (-genBandArpack)
eigenvalues = eigen(10)

# or, obtain 10 eigenvalues explicitly specifying the solver
eigenvalues = eigen('-fullGenLapack', 10)
```

Code Developed by: **fmk**
