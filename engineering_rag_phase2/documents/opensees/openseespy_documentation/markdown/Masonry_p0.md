<!-- chunk_id: Masonry_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Masonry.html",
 "title": "4.14.5.41. Masonry",
 "category": "general",
 "command": "Masonry",
 "doc_section": "src",
 "rel_path": "src/Masonry.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3189,
 "word_count": 315,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.41. Masonry

**uniaxialMaterial(*'Masonry'*, *matTag*, *Fm*, *Ft*, *Um*, *Uult*, *Ucl*, *Emo*, *L*, *a1*, *a2*, *D1*, *D2*, *Ach*, *Are*, *Ba*, *Bch*, *Gun*, *Gplu*, *Gplr*, *Exp1*, *Exp2*, *IENV*)**

This command is used to construct a uniaxialMaterial Masonry (Crisafulli, 1997; Torrisi, 2012), which is a uniaxial hysteretic constitutive model for Masonry developed by Crisafulli (1997) and modified by Torrisi (2012).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Fm` ([float](https://docs.python.org/3/library/functions.html#float)) | Compression strength of Masonry (Fm<0) |
| `Ft` ([float](https://docs.python.org/3/library/functions.html#float)) | Tension Strength of Masonry (Ft>0) |
| `Um` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain at maximum Strength (Um<0) |
| `Uult` ([float](https://docs.python.org/3/library/functions.html#float)) | Maximum compression strain (Uult<0) |
| `Ucl` ([float](https://docs.python.org/3/library/functions.html#float)) | Crack Closing strain (Ucl>0) |
| `Emo` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial Elastic Modulus |
| `L` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial Length (just add 1.0) |
| `a1` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial strut area as ratio of initial area (=1) |
| `a2` ([float](https://docs.python.org/3/library/functions.html#float)) | Ratio of residual strut area as inicitial strut area (Final area / Initial Area) |
| `D1` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain where strut degradation starts (D1<0)(For strain>D1 Area/Initial Area=a1) |
| `D2` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain where strut degradation ends (D2<0) (For strain <D2 Area/Initial Area=a2) |
| `Ach` ([float](https://docs.python.org/3/library/functions.html#float)) | Hysteresis parameter(0.3 to 0.6) See Crisafulli’s thesis |
| `Are` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain reloading factor (0.2 to 0.4) See Crisafulli’s thesis |
| `Ba` ([float](https://docs.python.org/3/library/functions.html#float)) | Hysteresis parameter(1.5 to 2.0) See Crisafulli’s thesis |
| `Gun` ([float](https://docs.python.org/3/library/functions.html#float)) | Stiffness unloading factor (1.5 to 2.5) See Crisafulli’s thesis |
| `Gplu` ([float](https://docs.python.org/3/library/functions.html#float)) | Hysteresis parameter(0.5 to 0.7) See Crisafulli’s thesis |
| `Gplr` ([float](https://docs.python.org/3/library/functions.html#float)) | Hysteresis parameter(1.1 to 1.5) See Crisafulli’s thesis |
| `Exp1` ([float](https://docs.python.org/3/library/functions.html#float)) | Hysteresis parameter(1.5 to 2.0) See Crisafulli’s thesis |
| `Exp2` ([float](https://docs.python.org/3/library/functions.html#float)) | Hysteresis parameter(1.0 to 1.5) See Crisafulli’s thesis |
| `IENV` ([int](https://docs.python.org/3/library/functions.html#int)) | Envelope: =0: Sargin stress-strain envelope descending branch; =1: Parabolic stress-strain envelope descending branch |
