#!/usr/bin/env python3
import hashlib,json,subprocess,sys,tempfile,shutil
from pathlib import Path
import numpy as np,pandas as pd
from scipy.optimize import minimize
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path(__file__).resolve().parent))
import target_family_robustness as tfr
from run_v34_stability import DATASETS,fit_residual_model

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def corrw(w,y,A):
    z=A@w; den=np.linalg.norm(y)*np.linalg.norm(z)
    return -1e9 if den<1e-14 else float(y@z/den)
def slsqp_max(y,A):
    p=A.shape[1]; cons=({'type':'eq','fun':lambda w:w.sum()-1},); bounds=[(0,1)]*p
    starts=[np.ones(p)/p]+[np.eye(p)[i] for i in range(p)]
    rng=np.random.default_rng(88441); starts += [rng.dirichlet(np.ones(p)) for _ in range(20)]
    best=-1e99
    for x0 in starts:
        r=minimize(lambda w:-corrw(w,y,A),x0,method='SLSQP',bounds=bounds,constraints=cons,options={'ftol':1e-12,'maxiter':1000})
        if r.success: best=max(best,corrw(r.x,y,A))
    return best

seedbase=2026101201; checks=[]; idx=0
for name,spec in DATASETS.items():
    df=pd.read_csv(ROOT/'data_confidential'/spec['file']); x=df[spec['mag']].to_numpy(float); fe=df[spec['fe']].to_numpy(float); C=df[spec['n4']].to_numpy(float)
    rng=np.random.default_rng(seedbase+idx); idx+=2; n=len(df); ntr=int(round(n*2/3))
    for k in range(20):
        perm=rng.permutation(n); tr=np.sort(perm[:ntr]); _,_,y,A=fit_residual_model(x[tr],C[tr],fe[tr]); b=tfr.bounds(y,A); alt=slsqp_max(y,A); checks.append(abs(b['max']-alt))
maxdiff=max(checks)
if maxdiff>2e-8: raise SystemExit(f'SLSQP mismatch {maxdiff}')
# deterministic primary replay into temp package-shaped root
tmp=Path(tempfile.mkdtemp(prefix='v34verify_')); (tmp/'code').mkdir(); (tmp/'results').mkdir(); (tmp/'data_confidential').mkdir()
for f in ['Sahab48_primary.csv','Amman44_primary.csv','Zagreb25_primary.csv']: shutil.copy2(ROOT/'data_confidential'/f,tmp/f); shutil.copy2(ROOT/'data_confidential'/f,tmp/'data_confidential'/f)
for f in ['target_family_robustness.py','run_v34_stability.py']: shutil.copy2(ROOT/'code'/f,tmp/'code'/f)
subprocess.run([sys.executable,str(tmp/'code'/'run_v34_stability.py'),'--root',str(tmp),'--splits','2000'],check=True,stdout=subprocess.DEVNULL)
principal=['heldout_summary.json','Sahab_n4_heldout_splits.csv','Amman_n4_heldout_splits.csv','Zagreb_field_n4_heldout_splits.csv','Zagreb_lab_n4_heldout_splits.csv']
parity={f:sha(ROOT/'results'/f)==sha(tmp/'results'/f) for f in principal}
if not all(parity.values()): raise SystemExit('byte replay failed')
# package manifest verification
manifest=ROOT/'SHA256SUMS.txt'; manifest_ok=0; manifest_total=0
if manifest.exists():
    for line in manifest.read_text().splitlines():
        if not line.strip(): continue
        h,rel=line.split(None,1); rel=rel.strip().lstrip('*'); manifest_total+=1
        if sha(ROOT/rel)==h: manifest_ok+=1
report={'independent_slsqp_checks':len(checks),'independent_slsqp_max_difference':maxdiff,'clean_primary_byte_replay':parity,'manifest':f'{manifest_ok}/{manifest_total}'}
print(json.dumps(report,indent=2))
