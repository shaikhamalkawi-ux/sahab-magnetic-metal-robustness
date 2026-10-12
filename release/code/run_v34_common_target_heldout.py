#!/usr/bin/env python3
import json,sys
from pathlib import Path
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parent))
import target_family_robustness as tfr
root=Path(__file__).resolve().parents[1];res=root/'results';res.mkdir(exist_ok=True)

def fit_betas(x,C,fe,tr):
 Z=np.column_stack([np.ones(len(tr)),fe[tr]])
 return np.linalg.lstsq(Z,x[tr],rcond=None)[0],np.linalg.lstsq(Z,C[tr],rcond=None)[0]
def apply(x,C,fe,ids,bx,bC):
 Z=np.column_stack([np.ones(len(ids)),fe[ids]])
 return x[ids]-Z@bx, C[ids]-Z@bC
def corr(a,b):
 a=a-a.mean();b=b-b.mean();den=np.linalg.norm(a)*np.linalg.norm(b); return np.nan if den<=1e-14 else float(a@b/den)
def difference_bounds(y1,y2,A):
 u1=y1/np.linalg.norm(y1);u2=y2/np.linalg.norm(y2);d=u1-u2
 if np.linalg.norm(d)<=1e-14:return {'min':0.,'max':0.,'min_weights':[.25]*A.shape[1],'max_weights':[.25]*A.shape[1]}
 b=tfr.bounds(d,A); scale=np.linalg.norm(d); b['min']*=scale;b['max']*=scale;return b

def one_dataset(path,x1c,x2c,metals,seed,nsplits=2000,frac=2/3):
 df=pd.read_csv(path);x1=df[x1c].to_numpy(float);x2=df[x2c].to_numpy(float);fe=df.Fe.to_numpy(float);C=df[metals].to_numpy(float)
 n=len(df);ntr=int(round(n*frac));rng=np.random.default_rng(seed);rows=[];invalid=0
 for s in range(nsplits):
  perm=rng.permutation(n);tr=np.sort(perm[:ntr]);te=np.sort(perm[ntr:])
  try:
   b1,bC=fit_betas(x1,C,fe,tr);b2,_=fit_betas(x2,C,fe,tr)
   y1tr,Atr=apply(x1,C,fe,tr,b1,bC);y2tr,_=apply(x2,C,fe,tr,b2,bC)
   b=difference_bounds(y1tr,y2tr,Atr)
   y1te,Ate=apply(x1,C,fe,te,b1,bC);y2te,_=apply(x2,C,fe,te,b2,bC)
   wmin=np.array(b['min_weights']);wmax=np.array(b['max_weights'])
   testmin=corr(y1te,Ate@wmin)-corr(y2te,Ate@wmin)
   testmax=corr(y1te,Ate@wmax)-corr(y2te,Ate@wmax)
   if not np.isfinite(testmin+testmax):raise ValueError
   rows.append({'split':s,'train_min':b['min'],'train_max':b['max'],'test_at_train_min':testmin,'test_at_train_max':testmax})
  except Exception:invalid+=1
 return pd.DataFrame(rows),invalid

def q(a):return {'q025':float(np.quantile(a,.025)),'median':float(np.median(a)),'q975':float(np.quantile(a,.975)),'mean':float(np.mean(a))}
configs=[
 ('Sahab_chi','Sahab48_primary.csv','Large_Xin','Fine_Xin',2026101231),
 ('Sahab_Ms','Sahab48_primary.csv','Large_Ms','Fine_Ms',2026101232),
 ('Amman_LF','Amman44_primary.csv','Fine_LF','Coarse_LF',2026101233),
 ('Zagreb_field_lab','Zagreb25_primary.csv','field_ms','lab_ms',2026101234),
]
out={}
for name,file,x1,x2,seed in configs:
 d,inv=one_dataset(root/file,x1,x2,['Mn','Cu','Ni','Zn'],seed)
 d.to_csv(res/f'{name}_n4_common_target_heldout.csv',index=False)
 out[name]={'valid':len(d),'invalid':inv,'train_min':q(d.train_min),'train_max':q(d.train_max),'test_at_train_min':q(d.test_at_train_min),'test_at_train_max':q(d.test_at_train_max),'test_min_negative_fraction':float((d.test_at_train_min<0).mean()),'test_max_positive_fraction':float((d.test_at_train_max>0).mean()),'test_reversal_both_signs_fraction':float(((d.test_at_train_min<0)&(d.test_at_train_max>0)).mean())}
(res/'common_target_heldout_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
