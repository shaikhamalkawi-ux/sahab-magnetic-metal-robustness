# Sahab urban-soil magnetic susceptibility–metal robustness

Research archive for Sahab urban-soil magnetic susceptibility/metal evidence. The active author-review manuscript is titled **Before Using Magnetic Susceptibility as a Soil-Metal Proxy: Iron Adjustment and Target Robustness in Sahab, Jordan**. The frozen V34 reproducibility archive and its historical title remain unchanged.

**Scientific baseline:** V34 scientific data/code and numerical results remain frozen and unchanged. **Current manuscript preparation:** *Environments* (MDPI) **S20R13 author-review version** (21 November 2026), **not submitted or accepted**. S20R13 supersedes S20R12 for author-approved figure legibility and date-presentation cleanup only; the publicly released V34 data and scientific calculations remain frozen. S15, S14, S8R1 and Springer EMAS S7A remain historical versions. **Archiving policy:** retain the public V34 reproducibility archive and postpone any Sahab Zenodo record/DOI until after acceptance.


## Current *Environments* author-review manuscript — S20R13

The S20R13 manuscript (28-page main text and 17-page supplement) implements the user's approved decision to retain the established scientific figure formats and improve label legibility, without changing source measurements, calculations, equations, results, scientific text, tables, or citations. The source-lineage diagram preserves the same A/B schematic with 2002/2009 provenance and 56/54/48 records; numerical figures 3-5 and Supplementary Figure S1 received font-size-operator improvements only, with every plotted vector/drawing command unchanged. The independently drawn Sahab city locator now uses 'Historical campaign period' rather than the oversized 'Jan-Apr 2000' banner; the exact January-April 2000 sampling period remains stated in Materials and Methods and the Figure 1 caption. The historic 2009 publisher's sample-site map was NOT inserted because its reprint permission remains unverified. Main and supplementary TeX text are byte-identical to S20R12; the rebuilt article retains all 9 main equations, 8 tables, 5 main figures and 57 references. Clean-source rebuild and page-by-page visual parity passed at 28/28 + 17/17 pages. The S20R12 independent 218-number/102-math-check audit remains the scientific baseline and was not counted as freshly rerun in S20R13. The full historical 72-case register remains author-retained and not independently replayed. Current files are kept privately in Google Drive folder 83, not published on GitHub as a manuscript preprint. No external outreach, journal submission or DOI deposit occurred; coauthor approvals and submission declarations remain pending.

### Historical S15 author-review metadata

The historical **S15** draft had seven listed authors in this order: **Mahdi Salem Lataifeh; Tayel El-Hasan; Ghassan Malkawi; Abdel-Jaleel Al-Nawiseh; Marianne Tarun (fifth-listed, corresponding author); Ahmed Elsayed; Mohammad Afzaal**. Corresponding-author contact: **mtarun@hct.ac.ae**. The author-requested contribution for Marianne Tarun is **validation: physical interpretation and magnetic-measurement consistency review**. The Tayel El-Hasan initials in the manuscript's CRediT statement are **T.E.-H.** The proposed author-review byline and contributions are **subject to the applicable coauthor approvals before submission**; no unanimous author consent is asserted here.

The historical S15 was an author-metadata and focused copyediting revision, not a new experiment, dataset, algorithm or independent field validation. It retains all **43 cited references**, including the four Malkawi-related works, and the unchanged **V34** data/code archive. The complete S20R13 article and its Supplementary Materials are held in the author's Google Drive review folder, not published as a GitHub preprint. See [historical S15 author metadata](docs/CURRENT_MANUSCRIPT_AUTHOR_METADATA_S15_20261105.md), the [historical S8 alignment note](docs/S8_MANUSCRIPT_REPOSITORY_ALIGNMENT_20261105.md), and the [public claim-to-reproduction map](docs/S8_REPRODUCIBILITY_MAP_20261105.md). No submission, acceptance, new journal DOI or Sahab Zenodo deposit is claimed.

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

**S20R13 manuscript byline (author-review; final coauthor approval pending):** Mahdi Salem Lataifeh; Tayel El-Hasan; Ghassan Malkawi; Abdel-Jaleel Al-Nawiseh; Marianne Tarun (**fifth-listed and corresponding**); Ahmed Elsayed; Mohammad Afzaal.

**Archive citation distinction:** `CITATION.cff` documents the earlier frozen V34 software-archive attribution and should not be mistaken for the current S20R13 seven-author manuscript byline. Reconcile final repository citation metadata with the accepted manuscript when depositing a versioned Zenodo record.

[Journal Data Availability wording](docs/JOURNAL_DATA_AVAILABILITY_DRAFT.md) | [Historical release audit](docs/RECOVERY_AND_RELEASE_STATUS.md) | [Release guide](release/README.md).

No Sahab Zenodo record/DOI has been created. The legacy removal of Zagreb data from later current-branch commits did not erase the historical Git objects; the original verified public artifact has now been restored.