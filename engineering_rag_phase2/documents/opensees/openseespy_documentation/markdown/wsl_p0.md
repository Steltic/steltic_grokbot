<!-- chunk_id: wsl_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/wsl.html",
 "title": "Windows Subsystem for Linux (Windows)",
 "category": "analysis",
 "command": "wsl",
 "doc_section": "src",
 "rel_path": "src/wsl.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1876,
 "word_count": 246,
 "has_code": true,
 "has_table": false
} -->

## Windows Subsystem for Linux (Windows)

This is a real Linux subsystem for you
to run OpenSeesPy Linux version on Windows.

#### Install the Windows Subsystem for Linux

Follow the instruction on [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
to install Windows Subsystem for Linux on Windows 10.
There are a couple of Linux distributions available and Ubuntu is recommended.
Once the Linux is installed, it will show as an application in the start menu.

#### Install Anaconda and start Jupyter Notebook

- Run the subsystem from start menu and a terminal window will show.
- Download Anaconda Linux version with command

  ```
  ~$ wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
  ```
- Install Anconda Linux version with commands

  ```
  ~$ bash Anaconda3-2021.05-Linux-x86_64.sh

  >>> Please answer 'yes' or 'no':
  >>> yes

  >>> Anaconda3 will not be installed into this location:

  [/home/username/anaconda3] >>> (enter)
  ```
- Start Jupyter Notebook

  > ```
  > ~$ /home/username/anaconda3/bin/jupyter-notebook
  > ```
- Copy the address in red box to a web browser

#### In Jupyter Notebook

Start a new notebook and then

#### In the command line (optional)

- Run Anaconda with following command,
  where username is your username of your computer. Please use
  the username shown in last step

  ```
  ~$ /home/username/anaconda3/bin/python3.8
  ```
- Install or Upgrade OpenSeesPy with commands

  ```
  ~$ /home/username/anaconda3/bin/python3.8 -m pip install openseespy
  ~$ /home/username/anaconda3/bin/python3.8 -m pip install --upgrade openseespy
  ```
- Run OpenSeesPy

  First run Anaconda with

  ```
  ~$ /home/username/anaconda3/bin/python3.8
  ```

  Then import OpenSeesPy with

  ```
  import openseespy.opensees as ops
  ops.printModel()
  ```
- run OpenSeesPy scripts

  > ```
  > /home/username/anaconda3/bin/python3.8 script.py
  > ```
