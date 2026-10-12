#!/usr/bin/env python3
import json,sys
from pathlib import Path
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parent))
import target_family_robustness as tfr
root=Path(__file__).resolve().parents[1];res=root/'results';res.mkdir(exist_ok=True)

def corr(a,b):
 a=np.asarray(a,float);b=np.asarray(b,float);a=a-a.mean();b=b-b.mean();return float(a@b/(np.linalg.norm(a)*np.linalg.norm(b)))
def residualize_custom(x,C,fe,kind):
 n=len(x)
 if kind=='linear': Z=np.column_stack([np.ones(n),fe])
 elif kind=='log': Z=np.column_stack([np.ones(n),np.log(fe)])
 elif kind=='quadratic':
  fs=(fe-fe.mean())/fe.std(ddof=0); Z=np.column_stack([np.ones(n),fs,fs**2])
 else: raise ValueError
 y=x-Z@np.linalg.lstsq(Z,x,rcond=None)[0]; A=C-Z@np.linalg.lstsq(Z,C,rcond=None)[0]
 return y,A

# Local-background modified contamination-degree style benchmark for Sahab N4.
df=pd.read_csv(root/'Sahab48_primary.csv'); metals=['Mn','Cu','Ni','Zn']; C=df[metals].to_numpy(float);x=df.Large_Xin.to_numpy(float);fe=df.Fe.to_numpy(float)
bg=df.loc[df.Activity.eq('Background'),metals]
bg_mean=bg.mean().to_numpy();bg_median=bg.median().to_numpy()
y,A=residualize_custom(x,C,fe,'linear')
bench={}
for label,bvals in [('equal_raw',np.ones(4)),('local_background_mean',1/bg_mean),('local_background_median',1/bg_median)]:
 w=bvals/bvals.sum(); bench[label]={'weights':{m:float(v) for m,v in zip(metals,w)},'fe_adjusted_r':corr(y,A@w)}
bench['background_reference']={'n_background':int(len(bg)),'mean':{m:float(v) for m,v in zip(metals,bg_mean)},'median':{m:float(v) for m,v in zip(metals,bg_median)}}
bench['full_envelope']=tfr.bounds(y,A)
(res/'environmental_benchmark.json').write_text(json.dumps(bench,indent=2),encoding='utf-8')

# Adjustment-form sensitivity: linear Fe, log Fe, quadratic Fe.
specs=[('Sahab',root/'Sahab48_primary.csv','Large_Xin'),('Amman',root/'Amman44_primary.csv','Fine_LF'),('Zagreb_field',root/'Zagreb25_primary.csv','field_ms'),('Zagreb_lab',root/'Zagreb25_primary.csv','lab_ms')]
rows=[]
for name,path,mag in specs:
 d=pd.read_csv(path); C=d[metals].to_numpy(float); x=d[mag].to_numpy(float); fe=d.Fe.to_numpy(float)
 for kind in ['linear','log','quadratic']:
  y,A=residualize_custom(x,C,fe,kind); b=tfr.bounds(y,A)
  rows.append({'dataset':name,'adjustment':kind,'rmin':b['min'],'rmax':b['max'],'max_weights':json.dumps(b['max_weights'])})
pd.DataFrame(rows).to_csv(res/'fe_adjustment_sensitivity.csv',index=False)
print(json.dumps(bench,indent=2));print(pd.DataFrame(rows).to_string(index=False))
