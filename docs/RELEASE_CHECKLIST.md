# Sahab V34 — release and journal-production checklist

## GitHub public data release

- [x] V34 scientific results locked; no new measurements, optimization or retuning.
- [x] Original full-data ZIP found in previous Git history and restored byte-identically at `release/Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip`.
- [x] Original Zagreb 25-row CSV source Git blob restored in `release/data/` and `public_method/data/`.
- [x] Source crosswalk and explicit Zagreb CC BY 4.0 attribution included.
- [x] Existing Sahab 48 / Amman 44 CSVs, split outputs, code and optional reduced ZIP preserved.
- [x] Public README, release README, checksums, release-status record and journal Data Availability draft synchronized to the restored default archive.
- [x] Executed new public [clean-environment verification](PORTABILITY_AUDIT_20261012.md): exact ZIP checksum PASS, 54/54 file manifest PASS, 80/80 optimizer PASS (max 6.99e-15), and 16,000 held-out split records numerically reproduced (max 9.05e-15). The original strict CSV byte replay FAILED with newer numerical libraries; this difference is documented, not concealed.
- [ ] Independently reconcile the Amman sample-8 definition difference if source equivalence is later claimed; no change to locked V34 without demonstrated error.

## Journal production — current status, 5 November 2026

- [x] S8R1 *Environments* manuscript includes the full public GitHub Data Availability statement; Zagreb 25-site provenance/licence and Amman sample-8 definition boundary are retained.
- [x] Main manuscript and Supplementary Materials compiled with the MDPI `environments` class from the archived template; **24 pages + 16 pages**, seven authors, 43 bibliography entries.
- [x] Four Malkawi-related cited references preserved, and two obsolete internal S3 archive labels removed in S8R1.
- [x] Independent editable-source/PDF compilation checks completed for these minor S8R1 editorial changes; no numerical/model result updates.
- [x] Earlier five-author public-repository README author metadata updated to match the seven-author S8R1 manuscript, with Haroun Albarghouthy corresponding.
- [x] Public GitHub V34 reproducibility package and its checksum preserved; `CITATION.cff` remains a historical V34 archive attribution rather than an S8R1 manuscript author declaration.
- [ ] Independently reconcile the Amman sample-8 input-definition discrepancy **only if a future claim of source equivalence is proposed**.
- [ ] Check the current MDPI production template and confirm any new portal-required metadata at submission; do not make up affiliations, ORCIDs or contact details.
- [ ] Corresponding author to review MDPI-generated proof before final submission; no current journal submission is claimed.
- [ ] After acceptance, review the final public archive, rights, authorship/citation fields, and release record before Zenodo deposition. **No DOI placeholder**.

Historical earlier release checklists referred to a 19-page main manuscript, a 12-page supplement, older correspondent details, or Zagreb inputs withheld; those were superseded by the subsequent S7A/S8/S8R1 manuscript versions.

See [current S8R1 archive map](S8_REPRODUCIBILITY_MAP_20261105.md) and the [source and rights note](../release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md).
