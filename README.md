# Sahab Urban Soil Magnetic Susceptibility–Metal Robustness

**Repository for the reproducible scientific analysis**

**Robustness of Magnetic Susceptibility–Metal Associations to Iron Adjustment and Chemical Target Definition: Evidence from Sahab Urban Soils**

**Scientific baseline:** Sahab V34 (12 October 2026), unchanged.  
**Target journal:** *Environments* (MDPI); manuscript acceptance or publication is **not** claimed.  
**Current publication policy:** GitHub only. **Zenodo will be considered after journal acceptance**, as requested.

## Get the complete reproducibility package

**[Download full V34 data, code, ledger and results (ZIP)](release/Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip)**

The [release directory](release/) also has a human-readable [release guide](release/README.md), [SHA-256 checksum](release/SHA256SUMS.txt), [direct CSV inputs](release/data/), [analysis scripts](release/code/), and selected [summary outputs](release/results/).

**Archive:** 55 ZIP entries, 2,155,168 bytes, SHA-256 `4971969d21f1ba09741e2551eba952a21ef2bb1d4cd33334066e45cb7e73cb95`. Includes exact original V34 input values, scripts, full split-level outputs and the historical Sahab source-reconciliation workbook. The source-text and analysis outputs have not been retuned.

## Authorship

1. Mahdi Salem Lataifeh
2. Tayel Mahmoud El-Hasan
3. Abdel-Jaleel Al-Nawiseh
4. Ghassan Malkawi — corresponding author
5. Ahmed Elsayed

## Studies and scope

| Dataset | Observations in analysis | Role |
| --- | ---: | --- |
| Sahab, Jordan | **48** principal reconstructed rows | Historical magnetic/chemical association and source reconciliation; 56 magnetic rows historically, 54 identities resolved |
| Amman–Airport, Jordan | **44** | Separate comparison; chemical extraction and magnetic protocol differ |
| Zagreb, Croatia | **25** matched surface sites | Published-source field/laboratory comparison at a common chemical target |

The nonnegative metal families are N4 = {Mn, Cu, Ni, Zn} and N5 = N4 plus Pb (the latter retains historical non-detect sensitivity). Studies are not pooled.

### Locked V34 outcomes

- Sahab N4 Fe-adjusted recorded-sample upper endpoint: `0.0384271762`.
- Sahab median held-out correlation with training-optimized weights: `-0.1382145` across 2,000 repeated random held-out splits.
- Corresponding N4 held-out medians: Amman–Airport `0.7499465`; Zagreb field `0.8191714`.
- Sample-selection and weight-domain calculations are retrospective/exploratory, **not** spatial/prospective validation, population-level bounds, contamination-class diagnosis, causal Fe-source apportionment, or instrument superiority.

## Reproduction

Download and extract the **complete ZIP**, not just the browsable subset:

```bash
python -m pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 python code/verify_v34.py
python verify_release.py
```

On the recovered archive, the verification produced **80/80 independent SLSQP checks**, maximum absolute difference `7.327471962526033e-15`, **5/5 primary held-out output byte replay**, and **54/54** post-execution SHA-256 manifest checks.

The smaller [public_method/](public_method/) directory is retained as a self-contained Zagreb and simulation demonstration with original source-file hashes. The full package supplies Sahab and Amman inputs and broader executed V34 analyses.

## Provenance, rights and limits

The depositor confirms that the manuscript coauthors approve public research-data availability. Original datasets must still be cited, and source-dependent legal rights and reuse licenses are distinct from coauthor manuscript approval. This repository **does not claim a new blanket CC BY 4.0 or MIT grant over every source-derived file**. See [data provenance and reuse notes](release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md).

The Zagreb source is published under CC BY 4.0: Frančišković-Bilinski et al. (2023), *Minerals* 13, 1481. [DOI 10.3390/min13121481](https://doi.org/10.3390/min13121481). Amman–Airport has [a separate archived reproducibility source](https://github.com/shaikhamalkawi-ux/amman-airport-magnetic-screening); **sample ID 8 has a documented input-definition difference** from V34, so the two masters should not be silently interchanged.

No Sahab GitHub-release DOI has been issued. The repository publication is intended for reproducibility before journal submission; Zenodo deposition is postponed until acceptance.

## Original survey sources

- El-Hasan, T. (2002). *Urban geochemistry: Heavy metals distribution on the soils of relatively heavy industrial city of Sahab, central Jordan*. *Mu’tah Lil-Buhuth wad-Dirasat, Pure Sciences*, 17(3), 49–67.
- El-Hasan, T.; Al-Nawiseh, A.-J.; Lataifeh, M. S. (2009). *Environmental magnetism: Heavy metal concentrations in soils as a function of magnetic materials content*. *Jordan Journal of Earth and Environmental Sciences*, 2 (Special Publication No. 1), 38–49.
- Al-Gharram, M. S. S. (2022). *Measurement of magnetic susceptibility and heavy metals concentration in roadside topsoil along Amman–Airport Highway, Jordan*. Master’s thesis, Yarmouk University.
- Frančišković-Bilinski et al. (2023). *Magnetic and geochemical properties of Zagreb city area soils*. *Minerals* 13, 1481.
