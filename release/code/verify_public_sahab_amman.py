#!/usr/bin/env python3
"""New public-release subset verifier; V34 original scientific code is unchanged.

Checks exactly Sahab/Amman cases with accessible inputs. Does not claim full
Zagreb verification in the absence of the Zagreb row-level data.
"""
import hashlib,sys,tempfile,json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path(__file__).resolve().parent))
import target_family_robustness as tfr
from run_v34_stability import DATASETS, fit_residual_model, run_splits

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def signed_corr(w,y,A):
 z=A@w
 den=np.linalg.norm(y)*np.linalg.norm(z)
 return -1e9 if den < 1e-14 else float(y@z/den)
def slsqp_max(y,A):
 p=A.shape[1]
 cons=({'type':'eq','fun':lambda w:w.sum()-1},)
 bounds=[(0,1)]*p
 starts=[np.ones(p)/p]+[np.eye(p)[i] for i in range(p)]
 rng=np.random.default_rng(88441)
 starts += [rng.dirichlet(np.ones(p)) for _ in range(20)]
 best=-1e99
 for x0 in starts:
  r=minimize(lambda w:-signed_corr(w,y,A),x0,method='SLSQP',bounds=bounds,constraints=cons,options={'ftol':1e-12,'maxiter':1000})
  if r.success:best=max(best,signed_corr(r.x,y,A))
 return best

available=['Sahab','Amman']
checks=[]; reproduced={}
seedbase=2026101201
for dataset_index,name in enumerate(available):
 spec=DATASETS[name]
 df=pd.read_csv(ROOT/'data_confidential'/spec['file'])
 x=df[spec['mag']].to_numpy(float)
 fe=df[spec['fe']].to_numpy(float)
 C=df[spec['n4']].to_numpy(float)
 rng=np.random.default_rng(seedbase+dataset_index*2)
 ntr=int(round(len(df)*2/3))
 for k in range(20):
  perm=rng.permutation(len(df))
  tr=np.sort(perm[:ntr])
  _,_,y,A=fit_residual_model(x[tr],C[tr],fe[tr])
  b=tfr.bounds(y,A)
  checks.append(abs(b['max']-slsqp_max(y,A)))
 for j,fam in enumerate(['n4','n5']):
  out,invalid=run_splits(df,spec['mag'],spec['fe'],spec[fam],seedbase+dataset_index*2+j,2000)
  if invalid: raise SystemExit(f'Invalid split: {name}-{fam}: {invalid}')
  with tempfile.TemporaryDirectory(prefix='sahab_pub_') as d:
   tmp=Path(d)/f'{name}_{fam}_heldout_splits.csv'
   out.to_csv(tmp,index=False)
   locked=ROOT/'results'/tmp.name
   reproduced[tmp.name]=(sha(tmp)==sha(locked))
maxdiff=max(checks)
report={'scope':'Sahab and Amman only; Zagreb source rows not publicly redistributed','independent_slsqp_checks':len(checks),'max_abs_difference':maxdiff,'full_original_v34_checks_not_repeated_here':80,'byte_replay':reproduced}
print(json.dumps(report,indent=2))
if len(checks)!=40 or maxdiff>2e-8 or not all(reproduced.values()):raise SystemExit('PUBLIC-SUBSET VERIFY FAIL')
