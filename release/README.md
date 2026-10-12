# Sahab V34 public release — Zagreb results only

[Download updated ZIP](Sahab_V34_ResearchData_ResultsOnlyZagreb_20261012.zip)

SHA-256: `e65d2485eea6cd87a557e0223dc72f044d7f6bd60efaad02b9c32627704d6a9d`; 2,161,434 bytes, 55 ZIP entries (54 payloads verified against its embedded SHA-256 manifest).

Included: Sahab 48-row analytic data, Amman–Airport 44-row analytic data, source reconciliation workbook, original V34 code, frozen numerical and split-level outputs for all three studies, including **Zagreb derived results**.

**Excluded:** Zagreb's 25-site original measurement/transcription table. Its direct GitHub CSV and both copies formerly in the ZIP were removed from the current branch. Consult Frančišković-Bilinski et al. (2023), *Minerals* 13, 1481, DOI 10.3390/min13121481 for independently sourced data.

To verify the included files after extraction:
```sh
python -m pip install -r requirements.txt
python verify_release.py
PYTHONDONTWRITEBYTECODE=1 python code/verify_public_sahab_amman.py
```

Public-only tests: 40/40 SLSQP comparisons; four N4/N5 Sahab/Amman held-out split CSVs reproduce byte-for-byte. Full three-study computation cannot be replayed without Zagreb inputs. Original 80-SLSQP check results remain historical verification of the internal archive before source-data withdrawal.

No scientific result was changed. GitHub only before journal acceptance; no Sahab Zenodo DOI has been created. Git commit history may still retain the previously shared source data.
