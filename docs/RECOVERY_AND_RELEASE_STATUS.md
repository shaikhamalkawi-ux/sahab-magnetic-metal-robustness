# Sahab V34 — historical archive recovery and current publication scope

**12 October 2026; scientific baseline V34 unchanged.**

## Present default: complete three-study public release

- Full ZIP: [release/Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip](../release/Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip); SHA-256 `4971969d21f1ba09741e2551eba952a21ef2bb1d4cd33334066e45cb7e73cb95`; stored historical Git blob SHA-1 `68bd7a36eb749b6039bd63b5f0e83c88d8b9f06b`.
- Direct Zagreb 25-site CSV: [release/data/Zagreb25_primary.csv](../release/data/Zagreb25_primary.csv); historical Git blob SHA-1 `d1a514bf037da9b8a62167b95e5839e466eb44a4`; identical source also in `public_method/data/`.
- The previously released results-only ZIP remains as a historical lower-distribution option: SHA-256 `e65d2485eea6cd87a557e0223dc72f044d7f6bd60efaad02b9c32627704d6a9d`. It lacks Zagreb source rows and cannot independently replay the complete cross-study verification.
- Original full archive was restored without rewriting ZIP contents or individual Zagreb CSV values. The public full-archive SHA-256 was previously recorded in the source package; current Git history demonstrates the original blob is preserved. This GitHub restoration alone does not constitute a fresh independent numerical rerun.

## Original completed numerical and integrity audit (historical provenance)

- Original internal V34 archive SHA-256 manifest: 59/59.
- Original reviewer/source archive manifest: 54/54.
- Original full independent SLSQP comparison: 80/80; maximum absolute discrepancy `7.327471962526033e-15`.
- Original primary held-out replay: five files byte-identical.
- Public-method original verification: seven/ seven file-hash matches; simulation outputs reproduced byte-for-byte.
- Original complete public ZIP: 55 ZIP entries and 54/54 payload SHA-256 checks.
- Subset-only verifier from the temporary results-only distribution: 40/40 SLSQP and four matching held-out output files.

These results were executed *before* the current documentation revision. Numerical reproduction in a newly installed environment is separately reportable only after a new run.

## Zagreb origin and rights

Frančišković-Bilinski, S.; Peco, J.; Sakan, S.; Đorđević, D.; Inđić, D. (2023). Magnetic and Geochemical Properties of Zagreb City Area Soils. Minerals 13(12), 1481. https://doi.org/10.3390/min13121481. Published article/data in Table 10 and Appendix A under CC BY 4.0. The adapted analysis table matches 25 *surface* observations; two deeper-layer chemistry measurements are omitted. See [attribution note](../release/docs/ZAGREB_SOURCE_ATTRIBUTION.md). Nothing in the Zagreb license grants license rights over Sahab or Amman source observations.

## Preserved scientific boundary

Sahab: 56 historical rows, 54 resolved identities, 48 primary analysis rows. Amman–Airport: 44 rows; `Fine_LF` sample 8 remains 246.05 despite differing external reconstructed value ~224.390243902439. Zagreb: 25 sites. All V34 equations, finite-sample bounds, split output, simulation, source deviations, and conclusions are unchanged; no new physical measurements or journal acceptance are claimed.

**Policy:** GitHub now; Zenodo **only after journal acceptance**. No DOI has been created for Sahab. The final MDPI PDFs must be synchronized with the complete archive before journal submission.