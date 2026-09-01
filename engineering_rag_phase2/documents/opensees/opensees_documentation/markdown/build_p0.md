<!-- chunk_id: build_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/developer/build.html",
 "title": "2. Building Application",
 "category": "developer",
 "manual_group": "",
 "command": "build",
 "doc_section": "developer",
 "rel_path": "developer/build.html",
 "part_index": 0,
 "part_count": 2,
 "char_count": 9718,
 "word_count": 1489,
 "has_code": true,
 "has_table": false
} -->

## 2. Building Application [part 1/2]

The OpenSees applications are built using [CMake](https://cmake.org/), an extensible open-source system that manages the build system. It provides a uniform build process across a range of operating systems: Windows, MacOS and different version of Linux. CMake needs to be installed on your system. For it to work, other applications such as C, C++ and Fortran compilers need to be also installed.

Note

Most code instructions below are run from a **Terminal** application. Type **cmd** in the Windows search or **terminal** in MacOS spotlight to start the application. If you are on a Unix machine this note may cause you some amusement!

#### 2.1. Windows 10

##### 2.1.1. Software Requirements

For Windows 10 the user must have the following applications installed on their computer: CMake, VisualStudio Basic, Intel One Basic and HPC Toolkits, and MUMPS, and conan:

1. **CMake**: We use [CMake](https://cmake.org/download/) for managing the build process. Version 3.20 or later is recommended.
2. **Visual Studio**: [Visual Studio (Community Edition)](https://visualstudio.microsoft.com/vs/) can be used. Some extensions of Visual Studio are also needed: Open Visual Studio Installer, go to Installed / More / Modify, under the Workloads tab, check Desktop development with C++ and Visual Studio extension development;

Warning

The very latest release of MSVC,  2022.2, does not currently work with Intel OneAPI. Install the version 2022.1 or the 2019 version of MSCV.

1. **IntelOne Basic & HPC Toolkits**: Intel’s [oneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html) toolkits. To install the Fortran compiler you need to install TWO toolkits, the [base toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html) and the [HPC toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html).  One advantage of installing the HPC one to obtain the Fortran compiler is that it comes with **MPI** for building and running the parallel OpenSees applications.

> Note
>
> > When downloading, you do not need to sign up with Intel. After you select the Download button a new window pops up titled ‘Get Your Download’. In bottom left had corner you can select the ‘Continue as Guest’ link to start a download without logging in.
>
> Warning
>
> 1. The install of the latest version of the base toolkit may fail due to issues installing Python. The error pops up right at the end. To overcome the problem, choose to install the selected components option and choose every package BUT Python.
> 2. On windows order matters, the Intel compilers come after Visual Studio. If you reverse the order or if the install was not successfullm cmake when running below will give an error message about failing to find a fortran compiler.

1. **MUMPS & conan**: MUMPS is a parallel solver used in OpenSees. Conan is a package build manager for C/C++ applications, that is used to install Tcl and HDF5. They are both installed via the command line, i.e. a DOS terminal.
  Mumps is one of the defaults solvers used in OpenSessMP and OpenSeesMP. Like OpenSees it  must be installed using **cmake**. Open a terminal window and type the following to set the intel env variables, download and then build the MUMPS library.

  > ```
  > "C:\Program Files (x86)\Intel\oneAPI\setVars" intel64 mod
  > git clone https://github.com/OpenSees/mumps.git
  > cd mumps
  > mkdir build
  > cd build
  > cmake .. -Darith=d -DCMAKE_MSVC_RUNTIME_LIBRARY="MultiThreaded" -G Ninja
  > cmake --build . --config Release --parallel 4
  > cd ..\..
  > pip install conan==1.59.0
  > ```

##### 2.1.2. Obtaining OpenSees Source Code

To obtain the source code, from a terminal **cd** to the directory you want to place OpenSees and then type the following:

> ```
> git clone https://github.com/OpenSees/OpenSees.git
> ```

Note

1. If you plan on contributing source code to the OpenSees effort, you should fork the OpenSees github repo and clone your own fork. To clone your own fork, replace OpenSees in above with your github username.

  ```
  git clone https://github.com/YOUR_USER_NAME/OpenSees.git
  ```

##### 2.1.3. Building the OpenSees Applications and Python module

With everything installed the build process is somewhat simple! From a terminal window move to the folder that contains the OpenSees folder and issue the following:

> ```
> "C:\Program Files (x86)\Intel\oneAPI\setVars" intel64 mod
> cd OpenSees
> git pull
> mkdir build
> cd build
> conan install .. --build missing --settings compiler.runtime="MT"
> cmake .. -DBLA_STATIC=ON -DMKL_LINK=static -DMKL_INTERFACE_FULL=intel_lp64 -DMUMPS_DIR="..\..\mumps\build"
> cmake --build . --config Release --target OpenSees --parallel 4
> cmake --build . --config Release --target OpenSeesPy
> cmake --build . --config Release --target OpenSeesMP
> cmake --build . --config Release --target OpenSeesSP
> cd lib
> copy OpenSeesPy.dll opensees.pyd
> ```

When completed the executables (OpenSees, OpenSeesMP, and OpenSeesMP) are located in the build/bin folder and the python module (opensees.pyd) is located in the build/lib folder.

Note

1. The –parallel option is used to compile the code in parallel. Change the **4** to how many cores is at your disposal.
2. The above assumes the OpenSees and mumps folders are located in the same folder.
3. The last copy is needed as the OpenSeesPy.dll module at present actually needs to load from a file named **opensees.pyd**. To import this module in a python script you can do one of 2 things:

1. If you have used pip to install openseespy, you can replace the opensees.pyd file in the site_package location with the opensees.pyd above. To find the location of this module, use the following:

  ```
  python3
  import opensees
  import inspect
  inspect.getfile(opensees)
  ```

  You may of course want to give the existing file a new name with the **copy** command before you overwrite it just in case! You can check the version of **opensees** installed by issuing :code: opensees.version() at the python command prompt above.
2. If you have not installed openseespy or you want to load the .pyd you built instead of the installed one you can add the path to opensees.pyd to your **PYTHONPATH** env variables. Search for **env settings** in search bar lower left. Add a line to the PYTHONPATH variable with your location of the **bin** folder. If you do this, you also need to copy the python39.dll (or the python310.dll is that is what was used INTO the bin folder). This is because of a security feature with python versions above 3.8 and the dll search path they now use.
3. Please note you will get a segmentation fault if you run with a different python exe than the one you build for. Look in output of **cmake ..** for the python library used.
4. **conan install .. -build missing** may fail. If it is related to a **zlib** mismatch error see below. If something else and you had installed conan before, it may be related to the version ypu are using. First try installing the latest  by issuing  *pip install conan –upgrade**. Ty the build again. If it fails (and again it does not issue a warning about a zlib mismatch) try installing the bleeding head latest using the following commands issued at a terminal

  ```
  git clone https://github.com/conan-io/conan.git conan-io
  cd conan-io
  pip install -e .
  ```
5. The **conan install .. –build missing** step may fail due to a **zlib mismatch**. This is due to fact that the **hdf5** and **tcl** packages used to build OpenSees both rely on **zlib** and the hdf5 group are more apt to update their package to the lastest zlib package than the tcl group. This sometimes results in the **conan** step failing. There is a fix, but it requires you do edit a file in the **tcl** package!

  In your home directory there is a **.conan** folder and in that folder there are some more folders. You need to edit the file **conanfile.py** in the folder **$HOME/.conan/data/tcl/8.6.10/_/_/export**. Change line **51** to use the same zlib as the hdf5 package, currently zlib 1.2.13, i.e. line 51 should now read **self.requires(“zlib/1.2.13”)**. Now go back to OpenSees/build folder and try again.

#### 2.2. MacOS

##### 2.2.1. Software Requirements

For MacOS the user must have the following applications installed on their computer: xcode command line tools, brew, cmake, gcc, gfortran, python, and open-mpi. All the applications are installed via the command line. Some of these you can skip as you may already have them installed.

1. **XCODE Command Line Tools**: To make Apple Clang and git available, type the following in a terminal application:

  ```
  xcode-select install
  ```

Note

1. if xcode-select: error: command line tools are already installed, use “Software Update” to install updates appears, skip because it’s already installed.
2. if xcode-select: error: command line tools are already installed, use “Software Update” to install updates appears, skip because it’s already installed.

1. **brew**: To install the HomeBrew package manager, type the following in a terminal window:

  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)
  ```
2. **cmake, gfortran, python & open-mpi**. Now we will use brew to install these applications. Again from the command line type:

  ```
  brew install cmake
  brew install gcc
  brew install open-mpi
  brew install scalapack
  brew install python@3.9
  git clone https://github.com/OpenSees/mumps.git
  cd mumps
  mkdir build
  cd build
  cmake .. -Darith=d
  cmake --build . --config Release --parallel 4
  cd ..
  ```

##### 2.2.2. Obtaining the Source Code
