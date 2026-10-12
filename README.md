# Sahab urban-soil magnetic susceptibility–metal robustness

Research archive for **Robustness of Magnetic Susceptibility–Metal Associations to Iron Adjustment and Chemical Target Definition: Evidence from Sahab Urban Soils**.

**Scientific baseline:** V34; unchanged. **Target journal:** *Environments* (MDPI); the article has not been submitted or accepted. **Archiving policy:** GitHub now, Zenodo only following manuscript acceptance.

## Primary public reproducibility archive

[Download complete V34 data, code and results](release/Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip)

- **SHA-256:** `4971969d21f1ba09741e2551eba952a21ef2bb1d4cd33334066e45cb7e73cb95`.
- **Historical verified package:** 55 ZIP entries (54 manifested files), with Sahab, Amman–Airport, and Zagreb inputs; source reconciliation, code, original outputs and checks.
- **Browsable inputs:** [Sahab (48 analytic rows)](release/data/Sahab48_primary.csv), [Amman–Airport (44 rows)](release/data/Amman44_primary.csv), [Zagreb (25 matched published surface sites)](release/data/Zagreb25_primary.csv).
- **Legacy reduced archive:** [results-only Zagreb alternative](release/Sahab_V34_ResearchData_ResultsOnlyZagreb_20261012.zip) remains available for comparison; it does *not* contain Zagreb observations, and is not the primary release.

The ZIP is the exact historical V34 complete-public Git object restored to the current branch; no measurement or calculated result was rewritten. The originally recorded complete-public verification was **80/80 independent SLSQP checks**, maximum discrepancy `7.327471962526033e-15`, **five** byte-identical primary held-out files, and **54/54** manifest checks. Those exact-byte results are historical. A **new clean GitHub Actions replay** verified original ZIP checksum, 54/54 manifest files, 80/80 independent SLSQP checks, and all 16,000 held-out split rows numerically (maximum discrepancy 9.05e-15). The original strict byte replay differs under newer libraries; see the [fresh numeric portability audit](docs/PORTABILITY_AUDIT_20261012.md).

## Reproduce

Extract the **complete** ZIP and execute at the extracted archive root:

```sh
python -m pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 python code/verify_v34.py
python verify_release.py
```

The separate `code/verify_public_sahab_amman.py` is a historical subset verifier intended for the reduced alternative, not a replacement for full three-study verification.

## Interpretation

| Study | Analysis records | Evidential role |
| --- | ---: | --- |
| Sahab | 48 (from 56 historical measurements; 54 matched identities) | Fe adjustment and chemical-target robustness |
| Amman–Airport | 44 | Independent roadside-soil comparison; not pooled |
| Zagreb | 25 matched surface sites | Published-source common-target field/laboratory comparison |

Locked Sahab N4 Fe-adjusted upper endpoint: `0.0384271762`. N4 selected-weight held-out median correlations: Sahab `-0.1382145`, Amman `0.7499465`, Zagreb field `0.8191714`. These are retrospective sampled-data analyses, not population guarantees, current Sahab contamination assessments, causal Fe-source apportionment, prospective prediction, spatial validation, or proof that one Zagreb instrument is superior.

## Rights, provenance, and authors

The Zagreb 25-site numerical table is derived from Frančišković-Bilinski, S.; Peco, J.; Sakan, S.; Đorđević, D.; Inđić, D. (2023). Magnetic and Geochemical Properties of Zagreb City Area Soils. Minerals 13(12), 1481. https://doi.org/10.3390/min13121481, under the original **CC BY 4.0** publication license. The adaptation joins Table 10 chemistry and Appendix A magnetic measurements by matched *surface* site; two deeper-layer chemical rows are excluded. See [Zagreb attribution](release/docs/ZAGREB_SOURCE_ATTRIBUTION.md) and [full source crosswalk](release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md). The Zagreb license does **not** establish a blanket license for Sahab/Amman measurements; the corresponding author has reported approval for public research-data sharing subject to applicable source rights.

The frozen Amman sample-8 `Fine_LF=246.05` differs from a separate public source reconstruction (about `224.390243902439`). This unresolved definition difference is documented; no values were silently substituted.

**Authors (confirmed order):** Mahdi Salem Lataifeh; Tayel Mahmoud El-Hasan; Abdel-Jaleel Al-Nawiseh; Ghassan Malkawi (corresponding); Ahmed Elsayed.

[Journal Data Availability wording](docs/JOURNAL_DATA_AVAILABILITY_DRAFT.md) | [Historical release audit](docs/RECOVERY_AND_RELEASE_STATUS.md) | [Release guide](release/README.md).

No Sahab Zenodo record/DOI has been created. The legacy removal of Zagreb data from later current-branch commits did not erase the historical Git objects; the original verified public artifact has now been restored.