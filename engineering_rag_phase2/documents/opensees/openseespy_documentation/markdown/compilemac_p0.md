<!-- chunk_id: compilemac_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/compilemac.html",
 "title": "2.2. Compilation for MacOS",
 "category": "general",
 "command": "compilemac",
 "doc_section": "src",
 "rel_path": "src/compilemac.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 742,
 "word_count": 100,
 "has_code": true,
 "has_table": false
} -->

## 2.2. Compilation for MacOS

This is a suggestive guide for MacOS.

- Download OpenSees Source code

  > ```
  > git clone https://github.com/OpenSees/OpenSees.git
  > ```
- Install [MacPorts](https://www.macports.org/install.php) for your macOs.
- Install [gcc8](https://ports.macports.org/port/gcc8)

  ```
  sudo port install gcc8
  ```
- Install Python 3.8 using MacPorts

  ```
  sudo port install python38 python38-devel
  ```
- Install boost using Macports

  ```
  sudo port install boost
  ```
- Create Makefile.def

  - Copy one of `MAKES/Makefile.def.MacOS10.x` to the root and rename to `Makefile.def`
  - Change the path and variables for your system
- Compile

  - Run `make python -j` from root
  - The library file will be at `SRC/interpreter/opensees.so`
