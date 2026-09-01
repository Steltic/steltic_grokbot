<!-- chunk_id: exampleRotDSpectra_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/exampleRotDSpectra.html",
 "title": "14.2.4. RotD Spectra of Ground Motion",
 "category": "examples",
 "command": "exampleRotDSpectra",
 "doc_section": "src",
 "rel_path": "src/exampleRotDSpectra.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5598,
 "word_count": 672,
 "has_code": true,
 "has_table": false
} -->

## 14.2.4. RotD Spectra of Ground Motion

1. The source code is developed by [Jawad Fayaz](https://jfayaz.github.io) from University of California- Irvine.
2. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/eeb7dc15e7ccdf8fe82b6b24da7b8120/example_RotD_Spectra_Generation.py).
3. Also download the code to read the provided GM file [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/6d439033e96547dfacbb567540131076/ReadGMFile.py).
4. The example bi-directional ground motion time histories are given [`GM11`](https://openseespydoc.readthedocs.io/en/latest/_downloads/93f9d0bab4354a67bb0c47f360c465bf/GM11.AT2), [`GM21`](https://openseespydoc.readthedocs.io/en/latest/_downloads/69205f49d3e1c9ccf3800429d78e5458/GM21.AT2), [`GM12`](https://openseespydoc.readthedocs.io/en/latest/_downloads/9116e34b8b6efb4437f37e3e561210b3/GM12.AT2), [`GM22`](https://openseespydoc.readthedocs.io/en/latest/_downloads/35aa969a233815d7537f45e7a2963534/GM22.AT2).
5. Run the source code in any Python IDE (e.g Spyder, Jupyter Notebook) and should see

```
"""
author : JAWAD FAYAZ (email: jfayaz@uci.edu) (website: https://jfayaz.github.io)

------------------------------ Instructions -------------------------------------
This code develops the RotD50 Sa and RotD100 Sa Spectra of the Bi-Directional
Ground Motion records as '.AT2' files provided in the current directory

The two directions of the ground motion record must be named as 'GM1i' and 'GM2i',
where 'i' is the ground motion number which goes from 1 to 'n', 'n' being the total
number of ground motions for which the Spectra needs to be generated. The extension
of the files must be '.AT2'

For example: If the Spectra of two ground motion records are required, 4 files with
the following names must be provided in the given 'GM' folder:
    'GM11.AT2' - Ground Motion 1 in direction 1 (direction 1 can be either one of the bi-directional GM as we are rotating the ground motions it does not matter)
    'GM21.AT2' - Ground Motion 1 in direction 2 (direction 2 is the other direction of the bi-directional GM)
    'GM12.AT2' - Ground Motion 2 in direction 1 (direction 1 can be either one of the bi-directional GM as we are rotating the ground motions it does not matter)
    'GM22.AT2' - Ground Motion 2 in direction 2 (direction 2 is the other direction of the bi-directional GM)

The Ground Motion file must be a vector file with 4 header lines.The first 3 lines can have
any content, however, the 4th header line must be written exactly as per the following example:
    'NPTS=  15864, DT= 0.0050'
The 'ReadGMFile.py' can be edited accordingly  for any other format

You may run this code in python IDE: 'Spyder' or any other similar IDE

Make sure you have the following python libraries installed:
    os
    sys
    pathlib
    fnmatch
    shutil
    IPython
    pandas
    numpy
    matplotlib.pyplot

INPUT:
This codes provides the option to have 3 different regions of developing the Spectra of ground motions with different period intervals (discretizations)
The following inputs within the code are required:
    'Path_to_openpyfiles'--> Path where the library files 'opensees.pyd' and 'LICENSE.rst' of OpenSeesPy are included (for further details go to https://openseespydoc.readthedocs.io/en/latest/windows.html)
    'Int_T_Reg_1'        --> Period Interval for the first region of the Spectrum
    'End_T_Reg_1'        --> Last Period of the first region of the Spectrum (where to end the first region)
    'Int_T_Reg_2'        --> Period Interval for the second region of the Spectrum
    'End_T_Reg_2'        --> Last Period of the second region of the Spectrum (where to end the second region)
    'Int_T_Reg_3'        --> Period Interval for the third region of the Spectrum
    'End_T_Reg_3'        --> Last Period of the third region of the Spectrum (where to end the third region)
    'Plot_Spectra'       --> whether to plot the generated Spectra of the ground motions (options: 'Yes', 'No')

OUTPUT:
The output will be provided in a saperate 'GMi_Spectra.txt' file for each ground motion record, where 'i' denotes the number of ground motion in the same of
provided 'GM1i.AT2' and 'GM2i.AT2' files. The output files will be generated in a saperate folder 'Spectra' which will be created in the current folder
The 'GMi_Spectra.txt' file will consist of space-saperated file with:
    'Periods (secs)' 'RotD50 Sa (g)' 'RotD100 Sa (g)'

%%%%% ========================================================================================================================================================================= %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""

##### ================== INPUTS  ================== #####

# Path where the library files 'opensees.pyd' and 'LICENSE.rst' are included (for further details go to https://openseespydoc.readthedocs.io/en/latest/windows.html)
Path_to_openpyfiles = 'C:\Tcl'

# For periods 0 to 'End_T_Reg_1' in an interval of 'Int_T_Reg_1'
Int_T_Reg_1       = 0.1
End_T_Reg_1       = 1

# For periods ['End_T_Reg_1'+'Int_T_Reg_2'] to 'End_T_Reg_2' in an interval of 'Int_T_Reg_2'
Int_T_Reg_2       = 0.2
End_T_Reg_2       = 2

# For periods ['End_T_Reg_2'+'Int_T_Reg_3'] to 'End_T_Reg_3' in an interval of 'Int_T_Reg_3'
Int_T_Reg_3       = 0.5
End_T_Reg_3       = 5

# Plot Spectra  (options: 'Yes' or 'No')
Plot_Spectra      = 'Yes'

##### =============== CODE BEGINS ================ #######
