# Sahab S8R1 — public code/data map for manuscript reviewers

**Status (5 November 2026):** Public data/code guidance for the seven-author *Environments* S8R1 manuscript. **Not a new research data release, preprint, submitted article, or Zenodo deposit.** Computations remain frozen as Sahab **V34**. S8R1 corrects two obsolete internal-version names only, after the S8 MDPI layout adaptation.

## Reproduce the underlying analysis, not the typeset article

1. Download the [complete V34 ZIP](../release/Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip), whose declared SHA-256 is `4971969d21f1ba09741e2551eba952a21ef2bb1d4cd33334066e45cb7e73cb95`.
2. Extract to a new directory, install the [archived requirements](../release/requirements.txt), then run `PYTHONDONTWRITEBYTECODE=1 python code/verify_v34.py` and `python verify_release.py` at the extracted root.
3. For a newer Python/NumPy/SciPy/Pandas stack, **do not mistake strict CSV byte differences for numerical disagreement**. Use the [secondary numerical validator](../audit/verify_cross_environment.py) and the documented [numeric portability report](PORTABILITY_AUDIT_20261012.md). The recorded clean GitHub run verified 54/54 frozen payload hashes, 80 independent SLSQP checks, and numerical consistency of 16,000 held-out split records. Exact CSV byte parity did not pass under those newer library versions.

## Trace scientific statements to released evidence

| Manuscript claim/diagnostic | Public input or output | Execution / evidence |
| --- | --- | --- |
| Historical Sahab reconciliation, 48 analytic observations drawn from 56 measurement records | [Sahab analytic input](../release/data/Sahab48_primary.csv), [source reconciliation](../release/docs/SOURCE_RIGHTS_AND_CROSSWALK.md) | Full ZIP's original code, source crosswalk and hash manifest; not a new field survey |
| Amman–Airport comparison, 44 records | [Amman analytic input](../release/data/Amman44_primary.csv) | [training/held-out stability implementation](../release/code/run_v34_stability.py); known sample-8 source-definition discrepancy disclosed in crosswalk |
| Zagreb, 25 matched surface sites | [Zagreb input](../release/data/Zagreb25_primary.csv), [attribution](../release/docs/ZAGREB_SOURCE_ATTRIBUTION.md) | Published chemistry and magnetic values joined by site under source CC BY 4.0; two deeper-layer chemical rows excluded |
| Nonnegative Fe-adjusted complete target-weight association envelope | [weight family algorithm](../release/code/target_family_robustness.py), [independent verifier](../release/code/verify_v34.py) | Exact values are **recorded-sample conditional**, not a universal chemical or population bound |
| Repeated nonspatial train/held-out splits and selection-stability summaries | [held-out summary](../release/results/heldout_summary.json), [summary CSV](../release/results/V34_Derived_Summary.csv) | [split code](../release/code/run_v34_stability.py); detailed split-level files retained in the complete ZIP |
| Paired-channel, common-target held-out evaluation | [common-target held-out results](../release/results/common_target_heldout_summary.json) | [run code](../release/code/run_v34_common_target_heldout.py) |
| Training-fraction and iron-model sensitivities | [training-fraction results](../release/results/heldout_train_fraction_sensitivity.json), [iron model CSV](../release/results/fe_adjustment_sensitivity.csv) | [training-fraction code](../release/code/run_v34_train_fraction_sensitivity.py), [environmental/Fe code](../release/code/run_v34_environmental_and_fe_sensitivity.py) |
| Environmental reference scaling | [environmental benchmark](../release/results/environmental_benchmark.json) | [environmental/Fe code](../release/code/run_v34_environmental_and_fe_sensitivity.py) |
| Four controlled methodological simulations | [simulation summary](../release/results/simulation_summary.json) | [simulation code](../release/code/run_v34_simulation.py); **not external field validation** |

All public file paths above refer to the existing V34 release. The manuscript's supplemental tables, qualifiers and proofs must be read with the article; the map is a navigation aid, not a replacement for the study.

## Claim limits

The study does not demonstrate contemporary Sahab contamination, causal source attribution, independent spatial generalization, calibrated uncertainty from overlapping resplits, absolute contamination rankings, superiority of one Zagreb instrument, or an implemented fuzzy-systems algorithm. The four Malkawi-related fuzzy publications remain cited as relevant mathematical background/future directions, not as executed experimental procedures.

The public repository's historical [`CITATION.cff`](../CITATION.cff) documents an earlier **V34 research-software archive**, not the current seven-author manuscript. The author-approved journal manuscript lists Mahdi Salem Lataifeh; Tayel Mahmoud El-Hasan; Ghassan Malkawi; Abdel-Jaleel Al-Nawiseh; Ahmed Elsayed; Haroun Albarghouthy (**corresponding**); and Mohammad Afzaal. The accepted-article bibliographic metadata, DOI, title, and publication venue must **not** be fabricated or entered before publication.

No Sahab Zenodo DOI has been registered. Defer any Zenodo deposit/release freeze to after the article is accepted, and validate provenance, licensing, included files, citation metadata and exact hashes at that time.
