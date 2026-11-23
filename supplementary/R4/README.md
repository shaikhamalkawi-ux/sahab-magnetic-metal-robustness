# Sahab S20R23-R4 — Public sign-feasibility replay

**Status:** R4 scientifically approved by the user on behalf of all authors on 23 November 2026. The manuscript targets *Environments*, has not been submitted or accepted, and is not posted here using the MDPI submission template.

The script `reproduce_R4.py` uses **only the previously public** `release/data/Sahab48_primary.csv` (48 rows) and does **not** import uncertain historical sample matches or change the frozen V34 release.

## Run

```sh
python -m pip install numpy
python supplementary/R4/reproduce_R4.py
```

The script writes `supplementary/R4/R4_replay_check.json` and asserts the stated finite-sample counts. Under linear Fe adjustment, all 0–4 deletion sets are enumerated with exact integer arithmetic. Log Fe and quadratic Fe alternatives are checked for deletion sizes 0–2 by least-squares residualization.

| Fe design | N4: minimum deletions | N5: minimum deletions |
|---|---:|---:|
| Intercept + Fe | 1 | 4 |
| Intercept + log(Fe) | 0 | 2 |
| Intercept + Fe + Fe² | 0 | 2 |

N4 = Mn, Cu, Ni, Zn; N5 adds Pb. This is an **exhaustive, post hoc within-sample sign-feasibility diagnostic**, not an environmental classifier, effect estimate, confidence interval, deployment guarantee, or a novel general mathematical theorem. A positive feasible association can be very weak. Refer to Supplement S15.1 for interpretation.

The 48 other historical reconstruction-case inputs discussed elsewhere in the manuscript are not supplied or independently reconstructed by this script. For source attribution and rights see [V34 source rights](../../release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md).