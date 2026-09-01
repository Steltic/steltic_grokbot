<!-- chunk_id: build_p1 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/developer/build.html",
 "title": "2. Building Application",
 "category": "developer",
 "manual_group": "",
 "command": "build",
 "doc_section": "developer",
 "rel_path": "developer/build.html",
 "part_index": 1,
 "part_count": 2,
 "char_count": 7176,
 "word_count": 1109,
 "has_code": true,
 "has_table": false
} -->

## 2. Building Application [part 2/2]

To obtain the source code, from a terminal **cd** to the directory you want to place OpenSees and then type the following:

> ```
> git clone https://github.com/OpenSees/OpenSees.git
> ```

Note

1. If you plan on contributing source code to the OpenSees effort, you should fork the OpenSees github repo and clone your own fork. To clone your own fork, replace OpenSees in above with your github username.

  ```
  git clone https://github.com/YOUR_USER_NAME/OpenSees.git
  ```

##### 2.2.3. Building the OpenSees Tcl Application

With everything installed the build process is somehwat simple! Again from a terminal window:

> ```
> cd OpenSees
> git pull
> mkdir build
> cd build
> conan install .. --build missing
> cmake .. -DMUMPS_DIR=$PWD/../../mumps/build -DOPENMPI=TRUE -DSCALAPACK_LIBRARIES=/usr/local/Cellar/scalapack/2.2.0_1/lib/libscalapack.dylib
> cmake --build . --config Release --target OpenSees --parallel 4
> cmake --build . --config Release --target OpenSeesPy
> cmake --build . --config Release --target OpenSeesMP
> cmake --build . --config Release --target OpenSeesSP
> mv ./lib/OpenSeesPy.dylib ./lib/opensees.so
> ```

Warning

1. The path to scalapack might change depending on your Mac type, e.g. x86 or ARM cpu, and the version of scalapack. When using brew install scalapack, look to see what path the library is located in. USE THAT PATH IF DIFFERENT!
2. This last copy is needed as the OpenSeesPy.dylib module at present actually needs to load from a file named **opensees.so** To import this module now in your code you must do one of 2 things:

2.1 If you have used pip3 to install openseespy, you can replace the opensees.so file in the site_package location with the opensees.so above. To find the location of this module, use the following:

> ```
> python3
> import opensees
> import inspect
> inspect.getfile(opensees)
> ```
>
> You may of course want to give the existing file a new name with the **mv** command. You can check the version of **opensees** installed by issuing :code: opensees.version() at the python command prompt above.

2.2 If you have not installed openseespy or you want to load the .so you built instead of the installed one you can add the path to opensees.so to your **PYTHONPATH** env variables with export PYTHONPATH=$PWD or PYTHONPATH=$PWD:$PYTHONPATH depending on if PYTHONPATH exists when you type **env** in the terminal. NOTE: Using $PWD assumes you are in the directory containing the lib file, other put in the full path to the directory.

1. Finally plase note you will get a segmentation fault if you run with a different python exe than the one you build for. Look in output of **cmake ..** for the python library used.

#### 2.3. Ubuntu

##### 2.3.1. Software Requirements

1. **Needed Applications and Libraries**: For Ubuntu, the user must have a number of packages installed on their system. These can be installed following commands issued in a terminal window.

  ```
  sudo apt-get update
  sudo apt install -y cmake
  sudo apt install -y gcc g++ gfortran
  sudo apt install -y python3-pip
  sudo apt install -y liblapack-dev
  sudo apt install -y libopenmpi-dev
  sudo apt install -y libmkl-rt
  sudo apt install -y libmkl-blacs-openmpi-lp64
  sudo apt install -y libscalapack-openmpi-dev
  git clone https://github.com/OpenSees/mumps.git
  cd mumps
  mkdir build
  cd build
  cmake .. -Darith=d
  cmake --build . --config Release --parallel 4
  cd ../..
  git clone --depth 1 --branch hdf5-1_12_2 https://github.com/HDFGroup/hdf5.git
  cd hdf5
  ./configure --prefix=/usr/local/hdf5
  make
  sudo make install
  pip3 install conan==1.59.0
  ```

Warning

Read the output from the last command. When building **OpenSees** below you will use the conan executable just installed, or find it using :code: whereis conan from the command line. If located in a different location to the path used below, you will get an error. Change the command below to path where conan was just installed.

##### 2.3.2. Obtaining the Source Code

You need to obtain the OpenSees source code from github. To obtain the source code, from a terminal **cd** to the directory you want to place OpenSees and then type the following:

> ```
> git clone https://github.com/OpenSees/OpenSees.git
> ```

##### 2.3.3. Building the OpenSees Applications

With everything installed the build process is somehwat simple! Again from a terminal window enter the following commands:

> ```
> cd OpenSees
> git pull
> mkdir build
> cd build
> $HOME/.local/bin/conan install .. --build missing
> cmake .. -DMUMPS_DIR=$PWD/../../mumps/build -DOPENMPI=TRUE -DSCALAPACK_LIBRARIES="/usr/lib/x86_64-linux-gnu/libmkl_blacs_openmpi_lp64.so;/usr/lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1"
> cmake --build . --config Release --target OpenSees --parallel 4
> cmake --build . --config Release --target OpenSeesPy
> cmake --build . --config Release --target OpenSeesMP
> cmake --build . --config Release --target OpenSeesSP
> mv ./lib/OpenSeesPy.so ./opensees.so
> ```

Note

1. If you have more than **4** cores available, you can use the extra cores by changing the **4** value!

Warning

This last copy is needed as the OpenSeesPy.dylib module at present actually needs to load from a file named **opensees.so** (go figure). Also to import this module now in your code you can do one of 2 things:

1. If you have used pip3 to install openseespy, you can replace the opensees.so file in the site_package location with the opensees.so above. To find the location of this module, use the following:

  ```
  python3
  import opensees
  import inspect
  inspect.getfile(opensees)
  ```

  You may of course want to give the existing file a new name with the **mv** command. You can check the version of **opensees** installed by issuing :code: opensees.version() at the python command prompt above.
2. If you have not installed openseespy or you want to load the .so you built instead of the installed one you can add the path to opensees.so to your **PYTHONPATH** env variables with export PYTHONPATH=$PWD or PYTHONPATH=$PWD:$PYTHONPATH depending on if PYTHONPATH exists when you type **env** in the terminal. NOTE: Using $PWD assumes you are in the directory containg the lib file.
3. Finally please note you will get a segmentation fault if you run with a different python exe than the one you build with. Look in output of **cmake ..** for the python library used.
4. The **conan install .. –build missing** step may fail. This is due to fact that the **hdf5** and **tcl** packages used to build OpenSees both rely on **zlib** and the hdf5 group are more apt to update their package to the lastest zlib package than the tcl group. This sometimes results in the **conan** step failing. There is a fix, but it requires you do edit a file in the **tcl** package!

  In your home directory there is a **.conan** folder and in that folder there are some more folders. You need to edit the file **conanfile.py** in the folder **$HOME/.conan/data/tcl/8.6.10/_/_/export**. Change line **51** to use the same zlib as the hdf5 package, currently zlib 1.2.13, i.e. self.requires(“zlib/1.2.13”). Now go back to OpenSees/build folder and try again.
