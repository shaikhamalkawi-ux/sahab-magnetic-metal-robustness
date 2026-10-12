# Sahab V34 — Release checklist

**Current status: STAGING. This repository does not yet contain V34 primary data/code and is not a runnable reproduction.**

## Source-of-truth and scientific lock

- [ ] Obtain original `Sahab_V34_Reviewer_Confidential_Reproducibility.zip`.
- [ ] Obtain original `Sahab_V34_Public_Method_Reproducibility.zip`.
- [ ] Obtain original `Sahab_V34_MDPI_Environments_Source.zip` if journal-text synchronization is needed.
- [ ] If files are missing, obtain `Sahab_V34_Complete_INTERNAL_20261012.zip` as the authoritative backup.
- [ ] Confirm input and output SHA-256 hashes and original V34 reproducibility records. Do not use approximations or reconstructed mock rows.
- [ ] Verify no scientific result, source reconciliation, N4/N5 definition, or inferential boundary has been changed.

## Rights, files, and safety

- [x] Coauthors' consent to public release reported by corresponding author (12 October 2026).
- [ ] Preserve documentary permissions for *public redistribution and reuse licensing* of historical Sahab and Amman–Airport source-derived values, including any thesis material held by a separate rights holder.
- [ ] Attribute the Zagreb CC BY 4.0 original article and label the paired-table transcription as an adaptation.
- [ ] Inspect the confidential archive: exclude passwords, unpublished personal information, sensitive paths, and publisher/third-party PDF binaries that lack distribution rights.
- [ ] Make dataset-specific license/NOTICE files; do not apply a blanket CC BY 4.0 or MIT license to third-party content without authorization.

## Reproducibility

- [ ] Add exact, source-admitted analytic CSVs, the sample-identity reconciliation ledger, and input-selection record.
- [ ] Add full source code, environment specification, version-pinned dependencies, frozen outputs, and usable reproduction commands from the original archive.
- [ ] Independently run the release workflow after fresh extraction, compare main V34 outputs and retained split-level files, and produce an exact SHA-256 manifest.
- [ ] Document what can and cannot be reproduced from public files; do not imply spatial/prospective validation.

## Publication

- [ ] Freeze validated GitHub snapshot and tag a release (e.g., `v1.0.0` only when verified).
- [ ] Archive the exact release in Zenodo, or publish a distinct dataset record with explicit software cross-link; avoid treating two DOI records for the same files as independent evidence.
- [ ] Record the actual DOI, public record URL, version, and Git commit in this README and citation metadata.
- [ ] Only after actual publication, update *all* Data Availability, Supplement, and journal-facing references to confidential archives.
- [ ] Recheck MDPI submission text, agreement on authorship, and link integrity.

**Locked study scopes:** Sahab 56 historical records / 54 resolved / 48 principal, Amman–Airport 44, Zagreb 25 matched surface sites.
