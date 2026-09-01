<!-- chunk_id: randomVariable_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/randomVariable.html",
 "title": "10.1. randomVariable command",
 "category": "general",
 "command": "randomVariable",
 "doc_section": "src",
 "rel_path": "src/randomVariable.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1152,
 "word_count": 92,
 "has_code": false,
 "has_table": true
} -->

## 10.1. randomVariable command

**randomVariable(*tag*, *dist*, *'-mean'*, *mean*, *'-stdv'*, *stdv*, *'-startPoint'*, *startPoint*, *'-parameters'*, **params*)**

Create a random variable with user specified distribution

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | random variable tag |
| --- | --- |
| `dist` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | random variable distribution `'normal'` `'lognormal'` `'gamma'` `'shiftedExponential'` `'shiftedRayleigh'` `'exponential'` `'rayleigh'` `'uniform'` `'beta'` `'type1LargestValue'` `'type1SmallestValue'` `'type2LargestValue'` `'type3SmallestValue'` `'chiSquare'` `'gumbel'` `'weibull'` `'laplace'` `'pareto'` |
| `mean` ([float](https://docs.python.org/3/library/functions.html#float)) | mean value |
| `stdv` ([float](https://docs.python.org/3/library/functions.html#float)) | standard deviation |
| `startPoint` ([float](https://docs.python.org/3/library/functions.html#float)) | starting point of the distribution |
| `params` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of parameter tags |
