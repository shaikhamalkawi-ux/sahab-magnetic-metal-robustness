# Sahab V34 — full public three-study reproducibility archive

**PRIMARY DOWNLOAD:** [Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip](Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip)

- SHA-256: `4971969d21f1ba09741e2551eba952a21ef2bb1d4cd33334066e45cb7e73cb95`
- Previously verified package: 55 ZIP entries, 54 manifested file payloads
- Original tested replay: 80 independent SLSQP comparisons, maximum absolute difference `7.327471962526033e-15`; five primary held-out files replayed byte-for-byte; 54/54 SHA-256 file checks
- The archive is an unchanged historical Git blob restored to `main`. Restoration proves *identity with the historical blob*, not a new independent rerun.
- Inputs: Sahab n=48, Amman–Airport n=44, Zagreb n=25 published matched surface locations. Historical Sahab records total 56; the reconciled analytical subset is not the full historical survey.

**Reproduce:** Extract the complete ZIP, install its `requirements.txt`, and run:

```sh
PYTHONDONTWRITEBYTECODE=1 python code/verify_v34.py
python verify_release.py
```

**Browsable files:** [Zagreb input](data/Zagreb25_primary.csv), [Sahab](data/Sahab48_primary.csv), [Amman](data/Amman44_primary.csv), [code](code/), [results](results/), [source crosswalk](docs/SOURCE_RIGHTS_AND_CROSSWALK.md).

**Historical alternative:** [Sahab_V34_ResearchData_ResultsOnlyZagreb_20261012.zip](Sahab_V34_ResearchData_ResultsOnlyZagreb_20261012.zip); SHA-256 `e65d2485eea6cd87a557e0223dc72f044d7f6bd60efaad02b9c32627704d6a9d`. It deliberately excludes Zagreb row-level inputs. Do not present it as full three-study self-contained reproduction; its public subset verifier covers 40 Sahab/Amman SLSQP checks and four split-output files.

Zagreb source adaptation: Frančišković-Bilinski, S.; Peco, J.; Sakan, S.; Đorđević, D.; Inđić, D. (2023). Magnetic and Geochemical Properties of Zagreb City Area Soils. Minerals 13(12), 1481. https://doi.org/10.3390/min13121481; licensed CC BY 4.0, Table 10 + Appendix A Table A1 joined by matched surface site, two deeper-layer chemical rows omitted. The Sahab and Amman datasets have separate provenance and reuse-rights boundaries. See [license and source notes](docs/ZAGREB_SOURCE_ATTRIBUTION.md).

Scientific baseline V34 unchanged. GitHub only until acceptance; no Sahab Zenodo DOI. Do not infer new data collection, causal claims, field-validation claims, or instrument superiority.