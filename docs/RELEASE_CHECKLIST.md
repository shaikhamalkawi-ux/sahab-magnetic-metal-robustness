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

## Journal production — still separate from GitHub publication

- [ ] Replace the old Zagreb-results-only Data Availability statement in the manuscript with [the current draft](JOURNAL_DATA_AVAILABILITY_DRAFT.md).
- [ ] Replace matching Zagreb-withheld descriptions in the supplement and any journal cover metadata.
- [ ] Update Abdel-Jaleel Al-Nawiseh's author contact using the user-supplied address, **after confirming his preferred publication address**. His institution remains the historically documented affiliation unless a current affiliation is separately verified.
- [ ] Compile and inspect Main PDF (19 pages historically), Supplement PDF (12 pages historically), combined PDF and clean Overleaf source; verify figure/table placement, references and author declarations.
- [x] Corresponding author reported coauthor approval, non-simultaneous submission, HCT APC support, and data-release permission subject to underlying source rights. These are user-confirmed, not independently verified documents.
- [ ] Do not submit without the user's explicit submission instruction.
- [ ] Zenodo record/DOI only *after acceptance*. No placeholder DOI.

Refer to [complete source and rights note](../release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md).