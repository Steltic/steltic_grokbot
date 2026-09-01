<!-- chunk_id: Copyright_Silvia_Mazzoni_silviamazzoni_yahoo.com_2021_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "",
 "title": "Copyright Silvia Mazzoni, silviamazzoni@yahoo.com 2021",
 "category": "other",
 "manual_group": "",
 "command": "",
 "doc_section": "",
 "rel_path": "",
 "part_index": 0,
 "part_count": 1,
 "char_count": 851,
 "word_count": 46,
 "has_code": true,
 "has_table": false
} -->

## Copyright Silvia Mazzoni, silviamazzoni@yahoo.com 2021

import matplotlib.pyplot as plt
    plt.rc('font',size=3)
    plt.rc('font',size=3)
    if legendFontSize == 0:
        legendFontSize = otherFontSize
    axModel.grid(True,color='grey',linewidth=0.25)
    handles, labels = axModel.get_legend_handles_labels()
    if len(handles)>0:
        axModel.legend(fontsize=legendFontSize,loc=legendLocation,ncol=ncol)
    axModel.set_title(Title, fontsize=titleFontSize)
    axModel.set_xlabel(xLabel, fontsize=otherFontSize)
    axModel.set_ylabel(yLabel, fontsize=otherFontSize)
    axModel.tick_params('x', labelsize=otherFontSize, rotation=0)
    axModel.tick_params('y', labelsize=otherFontSize, rotation=0)
    axModel.yaxis.set_ticks_position('left')
    axModel.xaxis.set_ticks_position('bottom')

    if not backgroundColor == '':
        axModel.set_facecolor(backgroundColor)
```

```
[4]:
```

```
