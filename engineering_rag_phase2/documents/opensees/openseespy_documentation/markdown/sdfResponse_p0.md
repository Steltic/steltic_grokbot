<!-- chunk_id: sdfResponse_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sdfResponse.html",
 "title": "7.12. sdfResponse command",
 "category": "general",
 "command": "sdfResponse",
 "doc_section": "src",
 "rel_path": "src/sdfResponse.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2045,
 "word_count": 201,
 "has_code": false,
 "has_table": true
} -->

## 7.12. sdfResponse command

**sdfResponse(*m*, *zeta*, *k*, *Fy*, *alpha*, *dtF*, *filename*, *dt*[, *uresidual*, *umaxprev*])**

It is a command that computes bilinear single degree of freedom response in C++, and is much quicker than using the OpenSees model builder.  The command implements Newmark’s method with an inner Newton loop.

| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | mass |
| --- | --- |
| `zeta` ([float](https://docs.python.org/3/library/functions.html#float)) | damping ratio |
| `k` ([float](https://docs.python.org/3/library/functions.html#float)) | stiffness |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | yielding strength |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | strain-hardening ratio |
| `dtF` ([float](https://docs.python.org/3/library/functions.html#float)) | time step for input data |
| `filename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | input data file, one force per line |
| `dt` ([float](https://docs.python.org/3/library/functions.html#float)) | time step for analysis |
| `uresidual` ([float](https://docs.python.org/3/library/functions.html#float)) | residual displacement at the end of previous analysis (optional, default=0) |
| `umaxprev` ([float](https://docs.python.org/3/library/functions.html#float)) | previous displacement (optional, default=0) |

The command returns a list of five response quantities.

| `umax` ([float](https://docs.python.org/3/library/functions.html#float)) | maximum displacement during analysis |
| --- | --- |
| `u` ([float](https://docs.python.org/3/library/functions.html#float)) | displacement at end of analysis |
| `up` ([float](https://docs.python.org/3/library/functions.html#float)) | permanent residual displacement at end of analysis |
| `amax` ([float](https://docs.python.org/3/library/functions.html#float)) | maximum acceleration during analysis |
| `tamax` ([float](https://docs.python.org/3/library/functions.html#float)) | time when maximum accleration occurred |
