# Dataset inventory — pending upload

**A public Zagreb sample-level CSV is now available in [`public_method/data/Zagreb25_primary.csv`](../public_method/data/Zagreb25_primary.csv), together with the generic engine and simulation results.** No Sahab or Amman sample-level analytic CSV has yet been released into this repository. The table below is the inventory for the eventual full release.

| Data source | Study role | Observation count |
| --- | --- | ---: |
| Sahab 2002 chemistry + 2009 magnetic archive | Historical source reconciliation and principal analysis | 56 original, 54 resolved, 48 principal |
| Amman–Airport published thesis-derived data | Separate N4/N5 comparison | 44 |
| Zagreb 2023 published chemical + field/laboratory measurements | Separate matched-site application | 25 surface sites |

When the original V34 archives become available and pass rights/hash checks, the release should include:

- **Sahab**: input records and the row-level reconciliation ledger with excluded/unresolved identities explicitly flagged; never silently force-match the unresolved records.
- **Amman–Airport**: admitted matched chemical and low-frequency magnetic input records.
- **Zagreb**: adapted published-table numeric transcription, source citation, CC BY 4.0 attribution and change notice.
- **Results**: frozen full-sample intervals, endpoint witnesses, 2,000 repeated held-out split diagnostics, source/tolerance sensitivity, and controlled simulation outputs.
- **Reproduction**: input hashes, exact code and dependencies, independent verification and manifest checks.

The original V34 inputs must be copied *exactly* from the verified archives. No new data, imaginary detection limits, inferred chemical concentrations, or synthetic placeholders may be substituted.
