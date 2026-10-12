# Public method materials for Sahab V34

This public-safe package contains the generic target-family robustness engine, the controlled simulation stress test, and a 25-row Zagreb example derived from Frančišković-Bilinski et al. (2023), Minerals 13(12), 1481, DOI 10.3390/min13121481 (CC BY 4.0).

It does **not** contain source-derived Sahab or Amman-Airport sample-level data, whose public redistribution rights have not been established.

Example endpoint calculation:
`python code/target_family_robustness.py --input data/Zagreb25_primary.csv --magnetic field_ms --magnetic2 lab_ms --fe Fe --metals Mn Cu Ni Zn`

Simulation stress test:
`python code/run_v34_simulation.py`

The simulation is methodological and is not environmental evidence.
