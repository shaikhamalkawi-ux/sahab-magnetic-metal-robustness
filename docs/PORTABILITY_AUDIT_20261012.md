# Sahab V34 — clean GitHub numeric portability audit (2026-10-12)

**Public executed workflow:** https://github.com/shaikhamalkawi-ux/sahab-magnetic-metal-robustness/actions/runs/38248951051  
**Result:** PASS for ZIP integrity, original manifest, the independent optimizer checks and the complete held-out numerical replay. The original strict byte-parity diagnostic failed under updated dependency versions; this is disclosed below.  
**Workflow source:** [verify-v34.yml](../.github/workflows/verify-v34.yml)  
**Secondary test source:** [verify_cross_environment.py](../audit/verify_cross_environment.py)

## Immutable tested source

- Original complete-public V34 ZIP: `release/Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip`
- Expected and verified SHA-256: `4971969d21f1ba09741e2551eba952a21ef2bb1d4cd33334066e45cb7e73cb95`
- Frozen manifest recheck: **54/54 PASS**
- The restored Git blob is the historical original, `68bd7a36eb749b6039bd63b5f0e83c88d8b9f06b`; neither this ZIP nor the V34 source data/code was edited.

## New clean runner environment

- Python 3.13.16, Linux GitHub Actions
- NumPy 2.5.4
- SciPy 1.18.1
- pandas 3.0.6

## Recomputed scientific checks

- 80/80 independent multistart SLSQP upper-bound checks PASS
- Worst optimizer-vs-bounds absolute discrepancy: **6.994405055138486e-15**
- All **eight** held-out families: Sahab N4/N5, Amman N4/N5, Zagreb field N4/N5, Zagreb laboratory N4/N5
- **2,000 splits each**, each matched to the original frozen split rows and numeric fields (16,000 split rows total); **zero** invalid splits, **zero** categorical `top_component` disagreements
- Maximum absolute difference across numerical split fields: **9.048317650695026e-15**
- Frozen baseline split-vs-summary self-consistency max difference: **1.1102230246251565e-16**
- Cross-environment numerical equivalence tolerance was predeclared in the secondary script as `1e-7`; the observed numerical discrepancy was much smaller.

## Exact byte parity is distinct from numerical parity

The old `code/verify_v34.py` requires **byte-identical** regenerated CSV/JSON output. Under the new package versions above it ended with `byte replay failed`. The necessary source files and SHA-256 manifest nevertheless passed and the separate numerical, row/categorical, and independent optimizer checks all passed at floating-point precision. We do **not** relabel the strict historical verifier as passing in this new environment. The prior clean replay under its original environment remains part of the historical audit.

**Claim boundary:** This checks the original recorded analytical rows and deterministic random splits, not new environmental samples, prospective prediction, population bounds, causal source attribution, or spatial validation. There is no result-changing revision.

To rerun, use the GitHub Actions workflow or extract the original ZIP and execute `python audit/verify_cross_environment.py <extracted-root>` using the repository's **outside-of-ZIP** secondary validator. The original archived scripts remain untouched.

**Journal production:** The 19-page manuscript and 12-page supplement currently contain Zagreb-results-only wording from the previous release phase; they must be recompiled from the journal LaTeX source after applying the [updated Data Availability Statement](JOURNAL_DATA_AVAILABILITY_DRAFT.md), prior to submission.