<!-- chunk_id: compileqt_p1 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/compileqt.html",
 "title": "2.3. Compilation using QT",
 "category": "general",
 "command": "compileqt",
 "doc_section": "src",
 "rel_path": "src/compileqt.html",
 "part_index": 1,
 "part_count": 2,
 "char_count": 5553,
 "word_count": 806,
 "has_code": true,
 "has_table": false
} -->

## 2.3. Compilation using QT [part 2/2]

OpenMPI requires the following dependencies that will automatically be installed:

- GCC (GNU compiler collection)
- libevent (Asynchronous event library: [https://libevent.org/](https://libevent.org/))

#### 2.3.8. UMFPACK

UMFPACK is a set of routines for solving unsymmetric sparse linear systems of the form Ax=b, using the Unsymmetric MultiFrontal method (Matrix A is not required to be symmetric).
UMFPACK is part of suite-sparse library in homebrew/science

In terminal, copy and paste each command individually and execute:

```
brew tap homebrew/science
brew install suite-sparse
```

UMFPACK requires the following dependencies that will automatically be installed:

- Metis (‘METIS’ is a type of GraphPartitioner and numberer - An Unstructured Graph Partitioning And Sparse Matrix Ordering System’, developed by G. Karypis and V. Kumar at the University of Minnesota.

#### 2.3.9. SUPERLU

SUPERLU is a general purpose library for the direct solution of large, sparse, nonsymmetric systems of linear equations. The library is written in C and is callable from either C or Fortran program. It uses MPI, OpenMP and CUDA to support various forms of parallelism.

Installing SUPERLU via brew
In terminal, copy and paste the following command and execute:

```
brew install superlu
```

Should install by default with option `--with-openmp` enabled. Open MP is needed for parallel analysis.

SUPERLU requires the following dependencies that will automatically be installed:

- GCC (GNU compiler collection)
- openblas (In scientific computing, OpenBLAS is an open source implementation of the BLAS API with many hand-crafted optimizations for specific processor types)

#### 2.3.10. SUPERLUMT

SUPERLU but for for shared memory parallel machines. Provides Pthreads and OpenMP interfaces.

Installing SUPERLUMT via brew:
In terminal, copy and paste the following command and execute:

```
brew install superlu_mt
```

SUPERLUMT requires the following dependencies that will automatically be installed:

- openblas

#### 2.3.11. SUPERLUDIST

SUPERLU but for for for distributed memory parallel machines. Supports manycore heterogeous node architecture: MPI is used for interprocess communication, OpenMP is used for on-node threading, CUDA is used for computing on GPUs.

Installing SUPERLUDIST via brew:
In terminal, copy and paste the following command and execute:

```
brew install superlu_dist
```

SUPERLUDIST requires the following dependencies that will automatically be installed:

- GCC (GNU compiler collection)
- openblas (In scientific computing, OpenBLAS is an open source implementation of the BLAS API with many hand-crafted optimizations for specific processor types)
- OpenMPI (a high performance message passing library ([https://www.open-mpi.org/](https://www.open-mpi.org/)))
- Parmetis (MPI library for graph/mesh partitioning and fill-reducing orderings)

#### 2.3.12. LAPACK (SCALAPACK)

The Linear Algebra PACKage, or LAPACK, is written in Fortran 90 and provides routines for solving systems of simultaneous linear equations, least-squares solutions of linear systems of equations, eigenvalue problems, and singular value problems.The associated matrix factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are also provided, as are related computations such as reordering of the Schur factorizations and estimating condition numbers. Dense and banded matrices are handled, but not general sparse matrices. In all areas, similar functionality is provided for real and complex matrices, in both single and double precision.

LAPACK is given as a system library in OSX, you may have to update the locations of your system library in ‘OpenSeesLibs.pri’

#### 2.3.13. BLAS

The BLAS (Basic Linear Algebra Subprograms) are routines that provide standard building blocks for performing basic vector and matrix operations.

BLAS is given as a system library in OSX, you may have to update the locations of your system library in ‘OpenSeesLibs.pri’

#### 2.3.14. ARPACK

ARPACK contains routines to solve large scale eigenvalue problems

Installing ARPACK via brew:
In terminal, copy and paste the following command and execute:

```
brew install arpack
```

ARPACK requires the following dependencies that will automatically be installed:

- GCC (GNU compiler collection)
- openblas (In scientific computing, OpenBLAS is an open source implementation of the BLAS API with many hand-crafted optimizations for specific processor types)

#### 2.3.15. GCC

Many of the dependencies require fortran (there is still a lot of legacy fortran code floating around in the engineering world). On OSX, I found the best solution is to use the pre-bundled fortran capabilities in the GNU compiler collection or GCC. In addition to its fortran capabilities, GCC is a dependency for many other libraries.

Installing GCC via brew:
In terminal, copy and paste the following command and execute:

```
brew install GCC
```

#### 2.3.16. PYTHON

Python is an interpreted, high-level, general-purpose programming language. It is used in OpenSees as an interpreter in the OpenSeesPy version. In OpenSeesPy, Python version 3 is used.

Installing PYTHON via brew:

```
brew install python
```

#### 2.3.17. MISC. NOTES

For the SUPERLU library.
The file supermatrix.h throws an undefined error for the type `int_t`. It is actually defined in the file slu_ddefs.h, but for some reason the compiler is not linking the two. Add the following line, copied from slu_ddefs.h to supermatrix.h around line 17:

```
typedef int int_t; /* default */
```
