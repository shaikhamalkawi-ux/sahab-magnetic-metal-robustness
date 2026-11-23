#!/usr/bin/env python3
"""Reproduce Sahab S20R23-R4 sharp sign-feasibility deletion thresholds.
Reads only the already released 48-row primary Sahab matrix.
Run: python supplementary/R4/reproduce_R4.py (requires numpy).
"""
import csv
import itertools
import json
from decimal import Decimal
from math import comb
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "release" / "data" / "Sahab48_primary.csv"
rows = list(csv.DictReader(INPUT.open()))
assert len(rows) == 48
ids = [int(r["sample_id"]) for r in rows]
columns = ("Fe", "Large_Xin", "Mn", "Cu", "Ni", "Zn", "Pb")
scales = (10, 100000, 1000, 1000, 1000, 1000, 1000)
V = [[int(Decimal(r[c])*scale) for c, scale in zip(columns, scales)] for r in rows]
n = len(V)
sums = [sum(r[k] for r in V) for k in range(7)]
f2 = sum(r[0]**2 for r in V)
fx = sum(r[0]*r[1] for r in V)
fm = [sum(r[0]*r[j] for r in V) for j in range(2, 7)]
xm = [sum(r[1]*r[j] for r in V) for j in range(2, 7)]

def exact_linear_signs(drop):
    nn = n-len(drop)
    f = sums[0]-sum(V[i][0] for i in drop)
    x = sums[1]-sum(V[i][1] for i in drop)
    ff = f2-sum(V[i][0]**2 for i in drop)
    xf = fx-sum(V[i][0]*V[i][1] for i in drop)
    den = nn*ff-f*f
    q = nn*xf-x*f
    assert den > 0
    out = []
    for j in range(5):
        k = j+2
        y = sums[k]-sum(V[i][k] for i in drop)
        xy = xm[j]-sum(V[i][1]*V[i][k] for i in drop)
        fy = fm[j]-sum(V[i][0]*V[i][k] for i in drop)
        out.append((nn*xy-x*y)*den-q*(nn*fy-f*y))
    return out

linear = []
for k in range(5):
    n4 = n5 = 0
    first4 = first5 = None
    for drop in itertools.combinations(range(n), k):
        z = exact_linear_signs(drop)
        if max(z[:4]) <= 0:
            n4 += 1
            if first4 is None:
                first4 = [ids[i] for i in drop]
        if max(z) <= 0:
            n5 += 1
            if first5 is None:
                first5 = [ids[i] for i in drop]
    linear.append(dict(k=k, total=comb(n,k), N4_no_positive=n4,
                       N5_no_positive=n5, first_N4=first4, first_N5=first5))
assert [z["N4_no_positive"] for z in linear] == [0,2,68,1413,19367]
assert [z["N5_no_positive"] for z in linear] == [0,0,0,0,6]
assert linear[4]["first_N5"] == [5,31,37,51]

A = np.array([[float(r[c]) for c in columns] for r in rows])
def covs(drop, model):
    keep = np.ones(n, dtype=bool)
    keep[list(drop)] = False
    data = A[keep]
    fe = data[:,0]
    targets = data[:,1:]
    if model == "log":
        design = np.column_stack([np.ones(len(fe)), np.log(fe)])
    elif model == "quadratic":
        design = np.column_stack([np.ones(len(fe)), fe, fe*fe])
    else:
        raise ValueError(model)
    residuals = targets-design@np.linalg.lstsq(design,targets,rcond=None)[0]
    return residuals[:,0]@residuals[:,1:]/len(fe)

alternative = {}
for model in ("log","quadratic"):
    rows_out = []
    for k in range(3):
        n4 = n5 = 0
        first4 = first5 = None
        for drop in itertools.combinations(range(n),k):
            z = covs(drop,model)
            if max(z[:4]) <= 0:
                n4 += 1
                if first4 is None:
                    first4 = [ids[i] for i in drop]
            if max(z) <= 0:
                n5 += 1
                if first5 is None:
                    first5 = [ids[i] for i in drop]
        rows_out.append(dict(k=k,N4_no_positive=n4,N5_no_positive=n5,
                             first_N4=first4,first_N5=first5))
    alternative[model] = rows_out
assert [x["N5_no_positive"] for x in alternative["log"]] == [0,0,2]
assert [x["N5_no_positive"] for x in alternative["quadratic"]] == [0,0,1]
assert alternative["log"][2]["first_N5"] == [24,31]
assert alternative["quadratic"][2]["first_N5"] == [31,51]
assert max(covs((), "log")[:4]) < 0
assert max(covs((), "quadratic")[:4]) < 0

output = dict(status="PASS", records=48, exact_linear=linear,
              alternative_Fe=alternative, R3_unverified_matches_used=False)
dest = Path(__file__).with_name("R4_replay_check.json")
dest.write_text(json.dumps(output,indent=2)+"\n")
print("PASS: linear N4=1/N5=4; log Fe N4=0/N5=2; quadratic Fe N4=0/N5=2")
