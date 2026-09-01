<!-- chunk_id: buildingMac_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/parallel/buildingMac.html",
 "title": "Building On a MAC",
 "category": "parallel",
 "manual_group": "",
 "command": "buildingMac",
 "doc_section": "parallel",
 "rel_path": "parallel/buildingMac.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 611,
 "word_count": 69,
 "has_code": true,
 "has_table": false
} -->

## Building On a MAC

#### Building OpenSees Sequential Version

#### Building Parallel Versions

1. Download latest stable release from [OpenMPI](https://www.open-mpi.org/), which at time of writing was openmpi-4.0.2. We downloaded into Downloads: openmpi-4.0.2.tar.gz

```
cd ~/Downloads
tar zxBf openmpi-4.0.2.tar.gz
cd openmpi-4.0.2/
./configure --prefix=/usr/local/openmpi
make -j 4
sudo make install
usr/local/openmpi/bin/mpirun --version

     mpirun (Open MPI) 4.0.2

     Report bugs to http://www.open-mpi.org/community/help/
```

Note

gfortran was previously installed on our machine.

#### 2. Install Some Other Software
