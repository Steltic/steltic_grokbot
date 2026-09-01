<!-- chunk_id: TEMPLATE_MF_09ST | collection: opensees_building_templates -->
<!-- meta: {
 "source": "building_template",
 "kind": "building_template",
 "template_id": "TEMPLATE_MF_09ST",
 "system": "moment_frame",
 "storeys": 9,
 "base_condition": "fixed",
 "members": "col W14x211; beam W27x94",
 "code": "ASCE7-22",
 "base_shear_kip": 417.8,
 "computed_T1_s": 2.173,
 "max_interstorey_drift": 0.00723,
 "modal_mass_mode1": 0.817,
 "analysis": "linear_static seismic ELF (DAM 0.8E) + modal",
 "status": "validated"
} -->

## TEMPLATE_MF_09ST

OpenSeesPy steel building template TEMPLATE_MF_09ST: moment_frame, 9 storeys, regular, 30 ft bays, base fixed. Members: col W14x211; beam W27x94. Designed/analysed to ASCE7-22. Seismic weight 4400 kip, Cs=0.0949, base shear 417.8 kip; computed period T1=2.173 s (Ta=1.264); max interstorey drift 0.00723; mode-1 modal mass 0.817. Sanity checks: equilibrium=True, stable=True, period_vs_Ta=True, modal_mass_mode1=True, drift_ok=True. Status validated.

# MF_09ST — MF 9-storey building template

2D lateral frame, regular 30 ft bays, members W14x211/W27x94.

ASCE 7 seismic ELF (DAM 0.8E): W=4400 kip, Cs=0.0949, V=418 kip; computed T1=2.17s (Ta=1.26s); max interstorey drift 0.0072 (1/138); mode-1 modal mass 0.82.

Sanity checks: {'equilibrium': True, 'stable': True, 'period_vs_Ta': True, 'modal_mass_mode1': True, 'drift_ok': True}. Status: validated.
Reproduce via generators/mf2d.py or cbf2d.py with these parameters.

