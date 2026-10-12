# Sahab Urban Soil Magnetic Susceptibility–Metal Associations

Reproducibility repository for the manuscript:

**Robustness of Magnetic Susceptibility–Metal Associations to Iron Adjustment and Chemical Target Definition: Evidence from Sahab Urban Soils**

**Research baseline:** Sahab V34 (12 October 2026)  
**Target journal:** *Environments* (MDPI)  
**Release status:** **PARTIAL PUBLIC METHOD RELEASE — the original V34 Zagreb example, generic algorithm, controlled simulation, and frozen simulation results are available and hash-verified under `public_method/`. Sahab/Amman analytic rows and the full V34 workflow are not publicly deposited here.** This repository is not yet the complete research archive.

## Authors

1. Mahdi Salem Lataifeh
2. Tayel Mahmoud El-Hasan
3. Abdel-Jaleel Al-Nawiseh
4. Ghassan Malkawi (corresponding author)
5. Ahmed Elsayed

## Scope

This retrospective analysis examines how Fe adjustment and the chemical target definition affect associations between soil magnetic susceptibility and measured metals. The declared nonnegative additive chemical families are **N4 = Mn, Cu, Ni, Zn** and **N5 = N4 + Pb** (Pb includes a historical censoring sensitivity). Studies are analyzed separately, without pooling.

| Study | Observed records admitted to the principal analysis | Role |
| --- | ---: | --- |
| Sahab, Jordan | 48 | Reconciled historical soil measurements (56 historical records; 54 sample identities resolved) |
| Amman–Airport, Jordan | 44 | Independent source-data comparison, not a pooled validation cohort |
| Zagreb, Croatia | 25 | Published matched surface sites for field/laboratory common-target comparison |

### Locked V34 findings (not predictive claims)

- Sahab large-fraction initial-susceptibility, Fe-adjusted N4, fixed-record upper endpoint: **0.0384271762**.
- Median held-out correlation using Sahab weights selected on training rows: **−0.1382145**, over 2,000 repeated random held-out splits.
- The corresponding selected-weight held-out medians are approximately **0.750** (Amman–Airport N4) and **0.819** (Zagreb field N4).
- These are recorded-sample analyses and exploratory random-split diagnostics; they are **not** population bounds, spatial/prospective validation, causal Fe-source separation, current contamination measurements, or evidence of instrument superiority.

## Data and software status

**Already released and verified:** [public_method/](public_method/) contains the 25-site Zagreb numeric transcription (published source: CC BY 4.0), exact V34 generic target-family engine, four-scenario simulation code, `requirements.txt`, 4,000 simulation-replicate rows, and frozen simulation summary. Each of the seven uploaded source files has a Git blob SHA matching the original V34 archive, and the simulation was replayed byte-for-byte. **Not yet publicly released:** Sahab/Amman input records, historical reconciliation ledger, complete held-out split-level files, and the full reviewer-only pipeline.

The archived V34 inputs and code must first be checked against their original file hashes and frozen numerical outputs. Historical source-specific public redistribution and license terms must be documented before the records are pushed. The authors' stated approval does not automatically set the license for third-party source-derived observations. This repository will **not** use guessed input data, synthetic substitutes, or unverified run commands to fill gaps.

See [Release checklist](docs/RELEASE_CHECKLIST.md) and [Dataset inventory](data/README.md).

## Original-source citation

- El-Hasan, T. (2002). *Urban geochemistry: Heavy metals distribution on the soils of relatively heavy industrial city of Sahab, central Jordan*. **Mu'tah Lil-Buhuth wad-Dirasat, Pure Sciences, 17**(3), 49–67.
- El-Hasan, T., Al-Nawiseh, A.-J., & Lataifeh, M. S. (2009). *Environmental magnetism: Heavy metal concentrations in soils as a function of magnetic materials content*. **Jordan Journal of Earth and Environmental Sciences, 2**, Special Publication No. 1, 38–49.
- Al-Gharram, M. S. S. (2022). *Measurement of magnetic susceptibility and heavy metals concentration in roadside topsoil along Amman–Airport Highway, Jordan*. Master's thesis, Yarmouk University.
- Frančišković-Bilinski, S., Peco, J., Sakan, S., Đorđević, D., & Inđić, D. (2023). *Magnetic and geochemical properties of Zagreb city area soils*. **Minerals, 13**, 1481. [https://doi.org/10.3390/min13121481](https://doi.org/10.3390/min13121481) (CC BY 4.0 with attribution and adaptation notice).

## Citation and persistent identifiers

A citable GitHub release and/or Zenodo dataset record will be linked here **only after publication**. No DOI or release tag has yet been issued for this Sahab repository.

## Licensing

**License assignment pending dataset/code audit.** The published Zagreb source is CC BY 4.0; this does not automatically license all other historical datasets or the newly written source code. Dataset-specific licenses and attribution will accompany the verified release.
