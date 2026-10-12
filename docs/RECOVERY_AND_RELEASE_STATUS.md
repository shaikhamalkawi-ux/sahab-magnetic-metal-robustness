# Sahab V34 — Verified recovery and public release boundary

**Record date:** 12 October 2026. **Scientific baseline:** V34, unchanged.

## Source archives recovered

Original archives were recovered directly from the existing Project 58 ChatGPT Library without reconstructing or inventing numerical inputs. The original `Sahab_V34_Complete_INTERNAL_20261012.zip` was checked before extraction.

- Parent archive: 59/59 listed SHA-256 payloads match.
- Original reviewer package: 54/54 listed SHA-256 payloads match before execution.
- Pristine clean rerun (`PYTHONDONTWRITEBYTECODE=1 python code/verify_v34.py`): 80 independent SLSQP checks; maximum absolute difference `7.327471962526033e-15`, five primary split-level files reproduce byte-for-byte, and the reviewer manifest remains 54/54.
- Principal reviewer checks: 5/5 PASS.
- Original public-method package: 7/7 SHA-256 records PASS.
- Public-method simulation outputs were regenerated from the original code and matched the archived `simulation_replicates.csv` and `simulation_summary.json` byte-for-byte.

The internal and reviewer archives **are not attached to this public GitHub repository**.

## Public method material uploaded

The following seven files were copied from the existing V34 public-safe ZIP into `public_method/`, without changing their bytes. Comparison of original `git hash-object` blob SHA-1 values to the GitHub repository tree yields **7/7 exact matches**:

- `public_method/README.md`
- `public_method/requirements.txt`
- `public_method/data/Zagreb25_primary.csv`
- `public_method/code/target_family_robustness.py`
- `public_method/code/run_v34_simulation.py`
- `public_method/results/simulation_replicates.csv`
- `public_method/results/simulation_summary.json`

Additionally, `public_method/results/V34_Derived_Summary.csv` was copied byte-identically from `Research_Analysis/V34_Derived_Summary.csv` in the recovered V34 parent archive. It contains source-excluded aggregate statistics, not sample-level Sahab or Amman inputs.

From the `public_method/` directory, the original source README documents the executable Zagreb and simulation commands. Do not label the simulation as measured environmental data.

## Provenance and copyright boundary

The 25 Zagreb matched-site observations are adapted from:

> Frančišković-Bilinski, S.; Peco, J.; Sakan, S.; Đorđević, D.; Inđić, D. (2023). *Magnetic and geochemical properties of Zagreb city area soils*. *Minerals*, 13(12), 1481. https://doi.org/10.3390/min13121481. Source article license: **CC BY 4.0**. Adaptation: match reported Table 10 chemistry to Appendix A surface field/laboratory readings, omit two deeper-layer chemical records, select the six numeric chemical analytes used by the study.

The historical source-derived Sahab and Amman–Airport analytic inputs and reconciliation ledger remain omitted from this public repository. All five current manuscript authors have reportedly consented to publication; before re-releasing the archival source-derived sample rows as CC BY 4.0, confirm that the appropriate underlying source holders have authority to grant this public reuse license. Source-data approval and source-specific licensing are distinct from coauthor approval of the paper.

A prior separately maintained Amman–Airport reproducibility repository already contains a CC BY 4.0 statement for author-owned archived data and a citable archive (https://doi.org/10.5281/zenodo.22973207). However, its independently reconstructed `Fine_LF_reconstructed` field is **not identical** to the locked V34 `Fine_LF` input for every row. In particular, sample ID 8 is `246.05` in V34 and approximately `224.390243902439` in that public reconstructed master, while the public master explicitly documents an alternative adopted fine-mass rule for sample 8. This source-definition discrepancy requires attribution/audit before claiming these two CSVs are interchangeable. The V34 value and scientific outputs have **not** been changed.

## Claim boundaries

V34's full-sample bounds, selected-weight held-out statistics, and simulation results remain locked. The random held-out runs are exploratory, not population confidence guarantees, spatial transfer validation, prospective prediction, or causal source separation. Zagreb paired-channel sign reversals should not be described as a stable device-superiority claim.

**Zenodo status:** No Sahab V34 GitHub release was archived in Zenodo yet, and no Sahab V34 repository DOI has been assigned. Do not cite a placeholder DOI.
