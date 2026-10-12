# Sahab Urban-Soil Magnetic–Metal Robustness

Reproducibility materials for **Robustness of Magnetic Susceptibility–Metal Associations to Iron Adjustment and Chemical Target Definition: Evidence from Sahab Urban Soils**.

**Scientific baseline:** V34 (unchanged). **Target journal:** *Environments* (MDPI), not yet accepted. **Archiving policy:** GitHub now; Zenodo after journal acceptance.

## Latest public archive

[Download updated Sahab / Amman data and Zagreb-results ZIP](release/Sahab_V34_ResearchData_ResultsOnlyZagreb_20261012.zip)

SHA-256: `e65d2485eea6cd87a557e0223dc72f044d7f6bd60efaad02b9c32627704d6a9d`.

**What is public:** source-reconciled Sahab analytic data (48 rows; 56 historical records and 54 resolved identities), Amman–Airport analytic data (44 rows), source reconciliation workbook, original code, and frozen results for all three studies, including **derived Zagreb statistical and held-out results**.

**What is not public:** the 25-site Zagreb numerical observation table. The earlier direct Zagreb CSV and older full-data ZIP were withdrawn from the *current branch* at the depositor's request. The revised archive also omits both duplicate Zagreb input CSVs. The numerical conclusions have not changed.

Original Zagreb source: Frančišković-Bilinski et al. (2023), *Minerals* 13, 1481, https://doi.org/10.3390/min13121481. Consult its Table 10 and Appendix A to independently reconstruct the paired source values. The full Zagreb numerical replay requires separately obtained observations; it cannot be run from the public ZIP alone.

## Reproduction

Extract the ZIP, install `requirements.txt`, and run:

```sh
python verify_release.py
PYTHONDONTWRITEBYTECODE=1 python code/verify_public_sahab_amman.py
```

The updated public verification passes 40 Sahab/Amman SLSQP tests and reproduces four original 2,000-split CSVs byte-for-byte. The **historical complete V34** 80-test verifier previously passed on the original internal archive, before Zagreb's row-level data were withheld. Original outcomes remain locked. Do not claim complete three-study replay from this public package alone.

Primary held-out medians: Sahab N4 −0.1382145; Amman N4 0.7499465; Zagreb field N4 0.8191714. These are retrospective sample-selection diagnostics, not prospective or spatial validation.

**Authors:** Mahdi Salem Lataifeh; Tayel Mahmoud El-Hasan; Abdel-Jaleel Al-Nawiseh; Ghassan Malkawi (corresponding); Ahmed Elsayed.

For release scope and provenance, see [release information](release/README.md) and [original-source guidance](release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md). Amman sample 8 retains the original V34 input difference from a separate previously published Amman master; no data were silently replaced.

**History limitation:** deleting files from the current GitHub branch does not erase older commits, clones, downloaded archives or caches. Previous Zagreb data availability cannot be retroactively undone merely by this update. No Sahab Zenodo DOI is assigned.
