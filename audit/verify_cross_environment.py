#!/usr/bin/env python3
"""Verify frozen V34 numeric outputs on a different dependency environment.

This secondary audit never changes original data, model scripts, or the
released research ZIP. It separates numerical agreement from bitwise CSV
serialization agreement, which can depend on NumPy/pandas/SciPy versions.
"""
import argparse
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import scipy
from scipy.optimize import minimize

def slsqp_max(y, A):
    p = A.shape[1]
    starts = [np.ones(p) / p] + [np.eye(p)[j] for j in range(p)]
    starts += list(np.random.default_rng(88441).dirichlet(np.ones(p), size=20))
    best = -1e99
    con = ({"type": "eq", "fun": lambda w: w.sum() - 1},)
    for x0 in starts:
        def obj(w):
            z = A @ w
            den = np.linalg.norm(y) * np.linalg.norm(z)
            return 1e9 if den < 1e-14 else float(-y @ z / den)
        fit = minimize(obj, x0, method="SLSQP", bounds=[(0, 1)] * p,
                       constraints=con, options={"ftol": 1e-12, "maxiter": 1000})
        if fit.success:
            best = max(best, -obj(fit.x))
    if best == -1e99:
        raise AssertionError("All independent SLSQP starts failed")
    return best

def compare_json(a, b, context="", out=None):
    if out is None:
        out = []
    if isinstance(a, dict):
        assert isinstance(b, dict) and set(a) == set(b), (context, "keys")
        for k in a:
            compare_json(a[k], b[k], context + "." + k, out)
    elif isinstance(a, list):
        assert isinstance(b, list) and len(a) == len(b), (context, "length")
        for i, (ai, bi) in enumerate(zip(a, b)):
            compare_json(ai, bi, context + "[" + str(i) + "]", out)
    elif isinstance(a, (int, float)) and not isinstance(a, bool):
        assert isinstance(b, (int, float)), (context, "numeric type")
        out.append((context, abs(float(a) - float(b))))
    else:
        assert a == b, (context, a, b)
    return out

def main():
    p = argparse.ArgumentParser()
    p.add_argument("root", type=Path)
    p.add_argument("--numeric-tolerance", type=float, default=1e-7)
    arg = p.parse_args()
    root = arg.root.resolve()
    sys.path.insert(0, str(root / "code"))
    import target_family_robustness as tfr
    from run_v34_stability import DATASETS, fit_residual_model, run_splits, summarize

    report = {
        "audit": "secondary numerical portability, original V34 science frozen",
        "python": sys.version.split()[0],
        "numpy": np.__version__, "scipy": scipy.__version__,
        "pandas": pd.__version__, "tolerance": arg.numeric_tolerance,
        "datasets": {}, "slsqp_count": 0, "slsqp_max_error": 0.0,
        "max_split_numeric_error": 0.0
    }
    split_seed_index = 0
    for dataset_index, (name, spec) in enumerate(DATASETS.items()):
        data = pd.read_csv(root / "data_confidential" / spec["file"])
        x = data[spec["mag"]].to_numpy(float)
        fe = data[spec["fe"]].to_numpy(float)
        C = data[spec["n4"]].to_numpy(float)
        rng = np.random.default_rng(2026101201 + 2 * dataset_index)
        ntrain = int(round(len(data) * 2 / 3))
        disagreements = []
        for _ in range(20):
            tr = np.sort(rng.permutation(len(data))[:ntrain])
            _, _, y, A = fit_residual_model(x[tr], C[tr], fe[tr])
            exact = tfr.bounds(y, A)["max"]
            independent = slsqp_max(y, A)
            disagreements.append(abs(exact - independent))
        report["slsqp_count"] += len(disagreements)
        report["slsqp_max_error"] = max(report["slsqp_max_error"], max(disagreements))
        report["datasets"][name] = {}
        for family in ("n4", "n5"):
            file = name + "_" + family + "_heldout_splits.csv"
            fresh, invalid = run_splits(data, spec["mag"], spec["fe"],
                                        spec[family], 2026101201 + split_seed_index)
            split_seed_index += 1
            original = pd.read_csv(root / "results" / file, float_precision="round_trip")
            assert len(fresh) == len(original) == 2000, (name, family, "row count")
            assert list(fresh.columns) == list(original.columns), (name, family, "schema")
            categorical = [c for c in original if not pd.api.types.is_numeric_dtype(original[c])]
            mismatches = {c: int((fresh[c].astype(str) != original[c].astype(str)).sum())
                          for c in categorical}
            diffs = {}
            for c in original.select_dtypes(include=["number"]).columns:
                a = original[c].to_numpy(float)
                b = fresh[c].to_numpy(float)
                assert np.isfinite(a).all() and np.isfinite(b).all(), (name, family, c)
                diffs[c] = float(np.max(np.abs(a - b)))
            worst = max(diffs.values(), default=0.0)
            report["max_split_numeric_error"] = max(report["max_split_numeric_error"], worst)
            report["datasets"][name][family] = {
                "rows": len(fresh), "invalid": invalid,
                "max_error": worst,
                "largest_columns": sorted(diffs.items(), key=lambda x: -x[1])[:5],
                "categorical_mismatches": mismatches
            }
            if any(mismatches.values()) or worst > arg.numeric_tolerance:
                print(json.dumps(report, indent=2))
                raise AssertionError((name, family, "non-equivalent replay", worst, mismatches))
    old_summary = json.loads((root / "results" / "heldout_summary.json").read_text())
    frozen_splits_summary = {
        name: {family: summarize(pd.read_csv(root / "results" /
                (name + "_" + family + "_heldout_splits.csv")), 0)
               for family in ("n4", "n5")} for name in DATASETS
    }
    deltas = compare_json(old_summary, frozen_splits_summary)
    report["frozen_summary_self_consistency_max_delta"] = max(v for _, v in deltas)
    assert report["frozen_summary_self_consistency_max_delta"] < 5e-12
    assert report["slsqp_count"] == 80
    assert report["slsqp_max_error"] < 2e-8
    print(json.dumps(report, indent=2))
    print("V34 CROSS-ENVIRONMENT NUMERIC REPLAY: PASS")

if __name__ == "__main__":
    main()
