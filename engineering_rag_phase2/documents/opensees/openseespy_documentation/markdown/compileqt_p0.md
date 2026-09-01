<!-- chunk_id: compileqt_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/compileqt.html",
 "title": "2.3. Compilation using QT",
 "category": "general",
 "command": "compileqt",
 "doc_section": "src",
 "rel_path": "src/compileqt.html",
 "part_index": 0,
 "part_count": 2,
 "char_count": 10194,
 "word_count": 1495,
 "has_code": true,
 "has_table": false
} -->

## 2.3. Compilation using QT [part 1/2]

Following is the OpenSees Compilation using QT by

*Stevan Gavrilovic* [github](https://github.com/steva44)

PhD Candidate

University of British Columbia

Original instructions can be found at [here](https://github.com/steva44/OpenSees/blob/master/README).

#### 2.3.1. A Qt build environment for OpenSees

OpenSeesQt

A Qt build environment for OpenSees – Open System For Earthquake Engineering Simulation Pacific Earthquake Engineering Research Center([http://opensees.berkeley.edu](http://opensees.berkeley.edu)).

Qt is an open source, cross-platform development environment that is free for many uses.
Please see the [license](https://www.qt.io/licensing/).

#### 2.3.2. Dependency

The purpose of this project is to create a package that will allow aspiring developers to get started on writing code without having to worry about the compilation environment. A program as large as OpenSees relies on many third-party libraries, often referred to as dependencies. It can be a daunting task assembling, compiling, and linking these libraries. Many times, these libraries depend on other libraries, and so on. The current list of dependencies includes:

- MUMPS (5.1.2)
- Scalapack (2.0.2.13)
- UMFPACK (5.7.7) contained in Suite-Sparse (5.3.0)
- SUPERLU (5.2.1)
- SUPERLUMT (3.0)
- SUPERLUDIST (5.1.0)
- Openblas (0.3.5)
- Parmetis (4.0.3)
- ARPACK (3.6.3)
- Libevent (2.1.8)
- GCC(8.2.0)
- TCL (8.6.9)** Tcl only
- Python(3.7.2)** OpenSeesPy only

Please ensure that your project complies with each library’s licensing requirements.

Another feature of this build platform is modularity. Developers can select from a list of build options that can be turned on and off as required. The basic configuration builds the structural analysis core. Other build options include parallel processing, reliability, and the particle finite element method (PFEM) modules. Python and Tcl interpreters are additional build options. These options are located in single configuration file called qmake.conf. By default, the environment is configured to build the core along with the parallel processing module. Other options can be turned on by deleting the ‘#’symbol that precedes the option; this includes the option into the build environment.

Note

Note: This build environment comes with pre-compiled dependencies. Although this makes getting started easier, the caveat is that your build environment (compiler version) must match that of the environment used to compile the dependencies. The supported environments are listed below. There are no guarantees that it will work with other build environments. In other words, make sure your compiler type and version (i.e., clang-1000.11.45.5) matches the version below listed under the heading ‘Supported Build Environments’. Otherwise, bad things might happen. Also, this project is still a work in progress. Currently, only building in OS X is supported. Windows support will be added shortly. Moreover, not all build options are supported. For example, compiling with fortran is not supported.

Note

This project uses qmake and Qt Creator. qmake is a build tool for compiling and linking applications. Qt Creator is a free IDE (interactive development environment) that bundles code writing/editing and application building within one program. Qt Creator uses project (.pro) files. The project files contain all information required by qmake to build an application.

#### 2.3.3. Getting started:

1. Download and install Qt open source from [https://www.qt.io/download](https://www.qt.io/download) The version of the Qt library is not important in this case since the library is not used in the OpenSees project (although I use Qt in other projects and recommend it)
2. Download the OpenSeesQt source code into a folder of your choice ([https://github.com/steva44/OpenSees/archive/master.zip](https://github.com/steva44/OpenSees/archive/master.zip))
3. In the directory containing the code, double click on the ‘OpenSees.pro’ file. If compiling OpenSeesPy, open the ‘OpenSeesPy.pro’ file. The .pro files are project files that will automatically open the project in Qt Creator.
4. Select a build configuration, for example ‘Desktop Qt 5.12.1 clang 64bit’. The project will automatically configure itself. You only have to do this once.
5. The left-hand pane should now display the project directory structure. In the left-hand pane, under the heading qmake, open the ‘qmake.conf’ file. Review and select additional build options, if any. Note that this is still a work in progress and not all build options are supported.
6. Click on the ‘start’ button in the bottom lefthand corner of Qt Creator to compile. Clicking on the small computer symbol above the start button allows for switching between the debug and release deploy configurations. The release deployment results in faster program execution but it does not allow for debugging or stepping through the code. The start button with the bug symbol opens the debugger.
7. Go and have a coffee, it will take a few minutes to finish compiling!

#### 2.3.4. Building OpenSeesPy:

OpenSeesPy builds OpenSees as a library object that can be used within Python.

Steps:
Follow steps 1-4 under the heading getting started above.

1. The left-hand pane should now display the project directory structure. In the left-hand pane, under the heading qmake, open the ‘qmake.conf’ file. Under the heading #INTERPRETERS, uncomment the _PYTHON option by removing the ‘#’ symbol. Everything else should be configured automatically going forward. Python automatically compiles with the reliability, parallel, and PFEM modules.
2. The last few lines at the end of the ‘OpenSeesPy.pro’ file contain the location of the Python framework. Update this so that it matches the location of Python on your build system.
3. Click on the ‘start’ button in the bottom lefthand corner of Qt Creator to start compiling. Clicking on the small computer symbol allows for switching between the debug and release deploy configurations. The release deployment results in faster program execution but it does not allow for debugging or stepping through the code. Build in release mode if using OpenSees as a library in a Python project.
4. Go and have a coffee, it will take a few minutes to finish compiling!
5. After successful compilation, the library will be in the ‘bin’ folder. The bin folder is located in the ‘build’ folder which is created, by default, one directory higher than the OpenSeesQt source code. The name of the build folder should look something like this: build-OpenSeesPy-Desktop_Qt_5_12_1_clang_64bit-Debug
6. OS X only

  OS X automatically prepends a ‘lib’ to the library file. Remove this ‘lib’ and rename the file to be ‘opensees.dylib’ Next, a symbolic link is required for a Python project to import the library. To create a symbolic link, cd the directory containing the OpenSees library in terminal and run the following command to create a symbolic link:

  ```
  ln -s opensees.dylib opensees.so
  ```

There should now be a .so (shared object) file in addition to the .dylib file. Finally, copy both the .dylib and the .so ‘link’ into your python environment folder to import it into your project. Directions for using OpenSeesPy can be found at the project website: [https://openseespydoc.readthedocs.io/en/latest/index.html](https://openseespydoc.readthedocs.io/en/latest/index.html)

#### 2.3.5. Supported Build Environments:

**OSX**

Build Environment:

- OSX 10.14.3 (Mojave)
- Qt 5.12.1
- Qt Creator 4.8.1

Compiler:

- Apple LLVM version 10.0.0 (clang-1000.11.45.5)
- Target: x86_64-apple-darwin18.2.0
- Thread model: posix 64-BIT architecture

To find the version of clang on your computer, type the following in terminal:

```
clang --version
```

Note

This project comes with pre-built libraries for everything except Python. Therefore, you do not have to go through the trouble of building any libraries unless you are using a special build system or you want to experiment. The precompiled library files are located in the ‘OpenSeesLibs’ folder. In the event that you are feeling adventurous and you want to compile the libraries on your own, instructions are given below for each library, for each operating system. After successful compilation, note the installation directory. This directory contains the locations of the ‘include’ and ‘lib’ folders for that library. If replacing or adding new libraries, the file paths should be updated in the ‘OpenSeesLibs.pri’ file. This is required so that the compiler knows where to find the header files and to link the libraries to your project.

**OSX**

On OSX, the dependencies are built/installed with Homebrew. Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple’s macOS operating system and Linux. Homebrew maintains its own folder within `/usr/local/` directory aptly named the `'Cellar'`:

```
/usr/local/Cellar/
```

Each dependency installed through Homebrew will have its own subfolder within the Cellar directory. Each subfolder contains that dependencies `'include'` and `'lib'` folders.

#### 2.3.6. MUMPS

MUltifrontal Massively Parallel sparse direct Solver, or MUMPS, is a sparse direct solver used for parallel solving of a system of equations

Installing MUMPS via brew:
Dominique Orban has written a Homebrew formula ([http://brew.sh](http://brew.sh)) for Mac OSX users. Homebrew MUMPS is now available via the OpenBLAS tap. Build instructions are as follows:

In terminal, copy and paste each command individually and execute:

```
brew tap dpo/openblas
brew tap-pin dpo/openblas
brew options mumps # to discover build options
brew install mumps [options…]
```

The options can be left blank, i.e., with default options so the last line will look like:

```
brew install mumps
```

Mumps requires the following dependencies that will automatically be installed:

```
-Scalapack
```

#### 2.3.7. OpenMPI

OpenMPI is a high performance message passing library ([https://www.open-mpi.org/](https://www.open-mpi.org/))

Installing OpenMpi via brew:
In terminal, copy and paste the following command and execute:

```
brew install open-mpi
```
