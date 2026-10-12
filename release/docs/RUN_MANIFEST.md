# Executable verification protocol

Original artifact origin: `Sahab_V34_Reviewer_Confidential_Reproducibility.zip`, recovered from the original V34 internal research archive; its implementation scripts, data and result CSVs are byte-for-byte preserved here. This public derivative omits historical "confidential reviewer" prose/flags and machine `__pycache__` files; it has its own SHA-256 manifest.

Execute from archive root after installing the original dependency ranges:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/verify_v34.py
python verify_release.py
```

Expected scientific check: independent SLSQP checks = 80, maximum absolute difference = `7.327471962526033e-15` in the recorded NumPy/SciPy environment, five primary held-out files have exact replay, manifest checks pass. Other platforms may exhibit numerical floating point tolerances.

Additional exploratory scripts (see their `--help` for arguments where provided):

- `code/run_v34_stability.py` — repeats all 2,000 primary held-out splits; refits Fe regression and nonnegative weights on training only.
- `code/run_v34_train_fraction_sensitivity.py` — 60% and 75% training proportion sensitivity.
- `code/run_v34_common_target_heldout.py` — frozen training min/max witness evaluation on held-out data.
- `code/run_v34_environmental_and_fe_sensitivity.py` — reference-normalized additive targets, log-Fe, and quadratic-Fe adjustments.
- `code/run_v34_simulation.py` — 4 controlled methodological simulations; not field validation.

`results/` includes the original 2000 split-level outputs per family and the controlled simulation replicate summaries. Outputs are deterministic for the original implementation and seed choices. Changes to original files invalidate release hashes.
