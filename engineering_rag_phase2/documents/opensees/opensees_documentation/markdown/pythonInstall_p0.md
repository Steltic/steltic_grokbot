<!-- chunk_id: pythonInstall_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/pythonInstall.html",
 "title": "2.2. Python Install",
 "category": "user_guide",
 "manual_group": "",
 "command": "pythonInstall",
 "doc_section": "user",
 "rel_path": "user/pythonInstall.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 579,
 "word_count": 96,
 "has_code": true,
 "has_table": false
} -->

## 2.2. Python Install

There are a number of steps to getting an OpenSees python script up and running. These work whther you are running on Windos, Mac, or a Linux operating system/

#### 2.2.1. Install Python

- Install  Python from python.org

#### 2.2.2. Install OpenSeesPy

- To install

  > ```
  > python -m pip install openseespy
  >
  > python -m pip install --user openseespy
  > ```
- To upgrade

  > ```
  > python -m pip install --upgrade openseespy
  >
  > python -m pip install --user --upgrade openseespy
  > ```

#### 2.2.3. Import OpenSeesPy

```
import openseespy.opensees as ops
```
