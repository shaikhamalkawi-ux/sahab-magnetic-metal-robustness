# Sahab V34 public method — Zagreb sample data withheld

This smaller directory contains the generic target-family method, controlled simulation, and frozen simulation results. The former Zagreb 25-row numeric example was withdrawn at the depositor's request. **No Zagreb observations are supplied here.**

The original Zagreb study, Frančišković-Bilinski et al. (2023), *Minerals* 13, 1481, https://doi.org/10.3390/min13121481, contains the site measurements for readers wishing to make an independent matched transcription.

The generic engine remains usable with an independently supplied CSV:
```sh
python code/target_family_robustness.py --input YOUR_INDEPENDENTLY_SOURCED_CSV --magnetic field_ms --magnetic2 lab_ms --fe Fe --metals Mn Cu Ni Zn
```

The simulation requires no Zagreb source CSV:
```sh
python code/run_v34_simulation.py
```

The simulation is methodological, not environmental evidence. See [the main release](../release/) for Sahab and Amman input data and derived Zagreb statistical results.
