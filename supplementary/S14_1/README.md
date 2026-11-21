# Supplementary Code S1 — exact S14.1 matched-split replay

**Project:** *Before Using Magnetic Susceptibility as a Soil-Metal Proxy: Iron Adjustment and Target Robustness in Sahab, Jordan*.

**Release status:** Reproducibility materials for a manuscript under author review; this folder is **not** a public preprint of the manuscript and **not** a journal acceptance, release DOI, full historical-source reconstruction, or new field validation.

This folder synchronizes the previously prepared **Supplementary Code S1** material for section S14.1 with the public Sahab V34 repository, without changing original V34 data, code or numeric results.

## One-command reproduction

From the repository root (requires Python 3):

```sh
python -m pip install -r supplementary/S14_1/requirements.txt
cd supplementary/S14_1
python code/replay_s14_1.py --inputs inputs_public --results results_rebuilt
```

Expected: `all_pass: true`, **21/21** frozen printed-value checks, 4 x 2,000 matched split records = **8,000 dependent split records**, and regenerated file contents byte-identical to `results/` under the recorded environment.

The replay implements four study/channel comparisons:

- Sahab, 48 admitted historical records, large-fraction initial susceptibility.
- Amman–Airport, 44 roadside records, fine low-frequency susceptibility.
- Zagreb, 25 matched surface sites, field susceptibility.
- Zagreb, same 25 sites, laboratory susceptibility.

**Source integrity:** Source-input CSV Git blob hashes are checked by the replay script. This directory includes copies of the same 3 publicly archived analysis-ready CSVs already under `release/data/` and four frozen replay result CSVs. `SHA256SUMS.txt` pins byte identity of every file in this folder except itself and this README.

**Scope limit:** This replays the S14.1 comparators only, without inventing missing source evidence. In particular the complete original 72-case full-precision historical source-reconciliation register, n44/n49/n54 reconciliation sources and exact primary Table 4 bootstrap stream are not provided here. The 2,000 random splits per case reuse the same observed samples; they are not independent population tests, spatial validation, predictive contamination screening, or causal source attribution.

**Data and attribution:** Sahab: El-Hasan (2002), El-Hasan, Al-Nawiseh & Lataifeh (2009). Amman: Al-Gharram (2022), Al-Momani et al. (2026). Zagreb: Frančišković-Bilinski et al. (2023), *Minerals* 13, 1481, DOI: 10.3390/min13121481 (paper CC BY 4.0). The Zagreb analytical transcription is attributed to its original study. Do not infer a blanket redistribution license for the original Jordanian source publications or workbooks.

No authorship approval, publisher submission, DOI, licence-extension or reprint permission is claimed by publishing this computational supplement.
