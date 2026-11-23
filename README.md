# Sahab urban-soil magnetic susceptibility–metal robustness

Research archive for Sahab urban-soil magnetic susceptibility/metal evidence. The active author-review manuscript is titled **Before Using Magnetic Susceptibility as a Soil-Metal Proxy: Iron Adjustment and Target Robustness in Sahab, Jordan**. The frozen V34 reproducibility archive and its historical title remain unchanged.

**Scientific baseline:** The original V34 data/code release remains frozen. **Current manuscript preparation:** *Environments* (MDPI) **S20R22-EP3, targeted reviewer-issue closure (23 November 2026)**; 26-page main manuscript, 16-page supplement, 64 cited references, 9 main equations, 8 main tables, 5 main figures and Figure S1. This is a submission-formatted author-review manuscript, **not submitted or accepted**. No new environmental samples, numerical result revisions, or public manuscript preprint are claimed. A previous reviewer assessment prompted bounded clarification of Fe-conditional interpretation, Sahab reconciliation sensitivity, overlapping held-out stability, and the public-replay boundary. The fuzzy-weight S17 supplement and related mathematical references were preserved. **DO NOT alter or rename the frozen V34 archive**.

## Current *Environments* author-review manuscript — S20R22-EP3

The author-reported approval of all seven listed authors and the selection of **Marianne Tarun (mtarun@hct.ac.ae)** as corresponding author have been received; this repository has not independently inspected seven individual approval messages or institutional APC documentation. The published 2026 Mafraq study in *Environments* 13(11), 627, DOI 10.3390/environments13110627 is cited and distinguished; it is a different dataset and fixed-budget sampling decision question.

The public 48-row Sahab input and 44-row Amman–Airport input support direct recalculation of **24 finite-record target-family cases** (16 Sahab + 8 Amman). The additional **48 cases** in the 72-case historical audit depend on original-precision 44/49/54-row Sahab reconstruction sets that are not released in full. See [S14.1 replay](supplementary/S14_1/README.md) for a distinct public 8,000-row comparator diagnostic; it does not recover the 48 restricted historical case inputs. The source rights and the Amman sample-8 difference remain documented in [source attribution](release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md). Current source-to-score results and V34 code/data have not been altered.

No S20R22-EP3 journal PDF or MDPI publisher-template source is posted here. The public repository contains reproducibility files, not a journal submission. No Sahab Zenodo DOI, preprint submission, or journal acceptance is asserted. The author/corresponding-author confirmation is user-reported; HCT APC authorization, final publisher portal declarations and third-party reuse conditions remain separate submission checks. See [current paper status](docs/PAPER_STATUS_S20R22_EP3.md).

### Historical S15 author-review metadata

The historical **S15** draft had seven listed authors in this order: **Mahdi Salem Lataifeh; Tayel El-Hasan; Ghassan Malkawi; Abdel-Jaleel Al-Nawiseh; Marianne Tarun (fifth-listed, corresponding author); Ahmed Elsayed; Mohammad Afzaal**. Corresponding-author contact: **mtarun@hct.ac.ae**. The author-requested contribution for Marianne Tarun is **validation: physical interpretation and magnetic-measurement consistency review**. The Tayel El-Hasan initials in the manuscript's CRediT statement are **T.E.-H.** The proposed author-review byline and contributions are **subject to the applicable coauthor approvals before submission**; no unanimous author consent is asserted here.

The historical S15 was an author-metadata and focused copyediting revision, not a new experiment, dataset, algorithm or independent field validation. It retains all **43 cited references**, including the four Malkawi-related works, and the unchanged **V34** data/code archive. The current submission-formatted article and Supplementary Materials are held as author-review files, not published as a GitHub preprint; S20R17 remains a historical version. See [historical S15 author metadata](docs/CURRENT_MANUSCRIPT_AUTHOR_METADATA_S15_20261105.md), the [historical S8 alignment note](docs/S8_MANUSCRIPT_REPOSITORY_ALIGNMENT_20261105.md), and the [public claim-to-reproduction map](docs/S8_REPRODUCIBILITY_MAP_20261105.md). No submission, acceptance, new journal DOI or Sahab Zenodo deposit is claimed.

## S14.1 supplementary reproducibility synced to GitHub (22 November 2026)

The code, input matrices, frozen 2,000-split rows for four study/channel cases, and comparator results for Section S14.1 are now publicly available in [supplementary/S14_1](supplementary/S14_1/README.md). A fresh local execution prior to upload passed **21/21 declared checks across 8,000 dependent split rows**, regenerating outputs byte-for-byte. The original V34 release is unchanged. This is historical within-sample evidence, not new data, spatial validation or contamination predictions.

**Current paper status:** The current journal-template manuscript PDF is **not uploaded to this public GitHub repository**. Seven-author submission agreement was reported on 23 November 2026, but no public preprint permission or journal-template redistribution is inferred. See [current manuscript status](docs/PAPER_STATUS_S20R22_EP3.md). This repository is a public scientific archive and is not a manuscript or journal DOI.

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

**S20R22-EP3 manuscript byline (author approval reported; journal submission not yet made):** Mahdi Salem Lataifeh; Tayel El-Hasan; Ghassan Malkawi; Abdel-Jaleel Al-Nawiseh; Marianne Tarun (**fifth-listed and corresponding**); Ahmed Elsayed; Mohammad Afzaal.

**Archive citation distinction:** `CITATION.cff` documents the earlier frozen V34 software-archive attribution and should not be mistaken for the current S20R22-EP3 seven-author manuscript byline. Reconcile final repository citation metadata with the accepted manuscript when depositing a versioned Zenodo record.

[Journal Data Availability wording](docs/JOURNAL_DATA_AVAILABILITY_DRAFT.md) | [Historical release audit](docs/RECOVERY_AND_RELEASE_STATUS.md) | [Release guide](release/README.md).

No Sahab Zenodo record/DOI has been created. The legacy removal of Zagreb data from later current-branch commits did not erase the historical Git objects; the original verified public artifact has now been restored.