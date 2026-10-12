# Data-source, authorization, and sample-definition crosswalk

**Public release update (12 October 2026): The Zagreb 25-site numerical observations are NOT distributed through the current public GitHub files or replacement ZIP. Only derived Zagreb statistics and computation code are included.** Earlier public copies were withdrawn from the current branch; Git history and previously downloaded copies may remain accessible.

This document applies to the **GitHub-only** V34 reproducibility deposit. The manuscript authors have been reported by the corresponding author as consenting to this public availability. No documentation of a separate publisher-granted or university-granted reuse licence has been supplied to this audit. Public files are not automatically released under a new blanket licence; dataset-specific legal rights and source attribution remain in force.

## Sahab
1. El-Hasan, T. (2002). *Urban geochemistry: Heavy metals distribution on the soils of relatively heavy industrial city of Sahab, central Jordan*. Mu'tah Lil-Buhuth wad-Dirasat, Pure Sciences, 17(3), 49–67.
2. El-Hasan, T.; Al-Nawiseh, A.-J.; Lataifeh, M.S. (2009). *Environmental magnetism: Heavy metal concentrations in soils as a function of magnetic materials content*. Jordan Journal of Earth and Environmental Sciences 2(Special Publication No. 1), 38–49.
3. Source-derived workbook and thesis reconciliation are part of the original authors' research provenance; source-table transcriptions and candidate mappings must not be mistaken for new field observations.

Sahab full magnetic study: 56; 54 resolved chemistry identities; 48 in the ±0.10 mg kg⁻¹ primary reconstructed subset; two identities unresolved. The publicly provided 48-row analytic CSV is not a full 56-row historical sample archive. The workbook documents the larger historical accounting.

## Amman–Airport
1. Al-Gharram, M.S.S. (2022). *Measurement of magnetic susceptibility and heavy metals concentration in roadside topsoil along Amman–Airport Highway, Jordan*. Yarmouk University master's thesis.
2. Al-Momani, I.F.; Lataifeh, M.S.; Al-Gharram, M.S. (2026). Jordan Journal of Physics 19(2), 213–222.
3. An earlier, separately maintained public reproducibility deposit is https://github.com/shaikhamalkawi-ux/amman-airport-magnetic-screening , with archived DOI https://doi.org/10.5281/zenodo.22973207. That deposit distinguishes MIT licensed original software from CC BY 4.0 author-owned data and documentation. This is a source attribution/cross-reference, **not a new Sahab DOI**.

**Reconstruction discrepancy to keep visible:**
- V34 original locked input: sample ID 8 `Fine_LF=246.05`.
- Separate public independently reconstructed Amman master: sample ID 8 `Fine_LF_reconstructed≈224.390243902439`.
- Its data dictionary documents a sample-8 adopted fine-mass rule that differs from some historical cached/formula entries. This note does not determine which candidate is scientifically preferable or identify complete cause of disagreement; cross-source equivalence remains unverified. Never merge values silently or recalculate the locked V34 results with the alternate source.
- Different extracted chemistry display precision in the sources can lead to small per-component rounding differences.

## Zagreb
Frančišković-Bilinski, S.; Peco, J.; Sakan, S.; Đorđević, D.; Inđić, D. (2023). *Magnetic and geochemical properties of Zagreb city area soils*. *Minerals* 13(12), 1481. https://doi.org/10.3390/min13121481 . Source article: **CC BY 4.0**, attribution and indication of table adaptation required. The ORIGINAL V34 analysis joined Table 10 chemistry and Appendix A magnetic readings for 25 matched *surface* sites, excluding two deeper-layer rows. This joined numeric table is **not** part of the revised public release. These are source-derived published measurements, not independent new measurements.

## Data-license limits
- No blanket MIT licence is attached to third-party historical measurements.
- No blanket CC BY 4.0 licence for all original input files is implied merely by the Zagreb source licence.
- The historical publisher/table and thesis-rights status should be confirmed if broader redistribution or derivatives beyond the reported permission are proposed.
- No author email, original publisher PDF binary, personal credential, or unpublished participant data is included in this archive.
