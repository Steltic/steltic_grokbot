<!-- chunk_id: pypilinux_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pypilinux.html",
 "title": "1.1.2. PyPi (Linux)",
 "category": "general",
 "command": "pypilinux",
 "doc_section": "src",
 "rel_path": "src/pypilinux.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 557,
 "word_count": 88,
 "has_code": true,
 "has_table": false
} -->

## 1.1.2. PyPi (Linux)

#### 1.1.2.1. Install Python

- Install Python 3 using your Linux’s package manager

  - Ubuntu/Debian: `sudo apt install python3 python3-pip`
  - Centos/Redhat: `sudo yum install python3 python3-pip`

#### 1.1.2.2. Install in terminal

- To install

  > ```
  > python3 -m pip install openseespy
  >
  > python3 -m pip install --user openseespy
  > ```
- To upgrade

  > ```
  > python3 -m pip install --upgrade openseespy
  >
  > python3 -m pip install --user --upgrade openseespy
  > ```
- To import

  > ```
  > import openseespy.opensees as ops
  > ```
