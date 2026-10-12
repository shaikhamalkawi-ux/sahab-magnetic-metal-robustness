# Sahab V34 — Release checklist

**Current status: PARTIAL PUBLIC METHOD RELEASE.** The original V34 Zagreb input, generic algorithm, controlled simulation code, and 4,000 source-matched simulation replicate records are available in `public_method/`. The complete primary Sahab/Amman source-derived inputs and full reviewer workflow are not yet public.

## Source-of-truth and scientific lock

- [x] Recovered original `Sahab_V34_Reviewer_Confidential_Reproducibility.zip` from Project Library (private working copy, not public).
- [x] Recovered and partially published original `Sahab_V34_Public_Method_Reproducibility.zip` source files; seven Git blobs byte-matched.
- [x] Recovered original `Sahab_V34_MDPI_Environments_Source.zip` for private journal-text synchronization.
- [x] Recovered original `Sahab_V34_Complete_INTERNAL_20261012.zip`; manifest 59/59 original ZIP entries PASS; nested code and data archives match standalone copies.
- [x] Original archives: reviewer manifest 54/54, public method manifest 7/7, and parent manifest 59/59 PASS before reruns; 80 independent SLSQP checks PASS and frozen-primary byte replay PASS. No approximations or reconstructed mock rows were used.
- [ ] Verify no scientific result, source reconciliation, N4/N5 definition, or inferential boundary has been changed.

## Rights, files, and safety

- [x] Coauthors' consent to public release reported by corresponding author (12 October 2026).
- [ ] Preserve documentary permissions for *public redistribution and reuse licensing* of historical Sahab and Amman–Airport source-derived values, including any thesis material held by a separate rights holder.
- [ ] Attribute the Zagreb CC BY 4.0 original article and label the paired-table transcription as an adaptation.
- [ ] Inspect the confidential archive: exclude passwords, unpublished personal information, sensitive paths, and publisher/third-party PDF binaries that lack distribution rights.
- [ ] Make dataset-specific license/NOTICE files; do not apply a blanket CC BY 4.0 or MIT license to third-party content without authorization.

## Reproducibility

- [ ] Add exact, source-admitted analytic CSVs, the sample-identity reconciliation ledger, and input-selection record.
- [ ] Add full reviewer-side source code and input records after rights review. Public subset already contains the original generic engine, simulation script, original requirement ranges, public Zagreb CSV and 4,000 frozen simulation records.
- [ ] Independently run the release workflow after fresh extraction, compare main V34 outputs and retained split-level files, and produce an exact SHA-256 manifest.
- [ ] Document what can and cannot be reproduced from public files; do not imply spatial/prospective validation.

## Publication

- [ ] Freeze validated GitHub snapshot and tag a release (e.g., `v1.0.0` only when verified).
- [ ] Archive the exact release in Zenodo, or publish a distinct dataset record with explicit software cross-link; avoid treating two DOI records for the same files as independent evidence.
- [ ] Record the actual DOI, public record URL, version, and Git commit in this README and citation metadata.
- [ ] Only after actual publication, update *all* Data Availability, Supplement, and journal-facing references to confidential archives.
- [ ] Recheck MDPI submission text, agreement on authorship, and link integrity.

**Locked study scopes:** Sahab 56 historical records / 54 resolved / 48 principal, Amman–Airport 44, Zagreb 25 matched surface sites.
