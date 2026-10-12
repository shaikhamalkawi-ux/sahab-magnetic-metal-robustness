#!/usr/bin/env python3
import json,sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parent))
import target_family_robustness as tfr

def pearson(a,b):
    a=np.asarray(a,float);b=np.asarray(b,float);a=a-a.mean();b=b-b.mean();d=np.linalg.norm(a)*np.linalg.norm(b)
    return np.nan if d<=1e-14 else float(a@b/d)

def train_apply(x,C,fe,tr,te):
    Ztr=np.column_stack([np.ones(len(tr)),fe[tr]])
    bx=np.linalg.lstsq(Ztr,x[tr],rcond=None)[0]; bC=np.linalg.lstsq(Ztr,C[tr],rcond=None)[0]
    ytr=x[tr]-Ztr@bx; Atr=C[tr]-Ztr@bC
    b=tfr.bounds(ytr,Atr); w=np.array(b['max_weights'])
    Zte=np.column_stack([np.ones(len(te)),fe[te]])
    yte=x[te]-Zte@bx; Ate=C[te]-Zte@bC
    return b['max'],pearson(yte,Ate@w),pearson(yte,Ate@np.ones(C.shape[1])/C.shape[1])

def generate(rng,n,scenario):
    f=rng.normal(size=n); h=rng.normal(size=n); e=rng.normal(size=(n,4))
    C=np.column_stack([
      0.45*f+0.35*h+0.80*e[:,0],
      0.50*f+0.35*h+0.80*e[:,1],
      0.30*f+0.45*h+0.75*e[:,2],
      0.40*f+0.50*h+0.70*e[:,3],
    ])
    # standardized concentrations, then shift positive (shift does not affect correlations)
    C=(C-C.mean(0))/C.std(0,ddof=0)+3.0
    noise=rng.normal(scale=0.85,size=n)
    if scenario=='A_Fe_only': x=0.90*f+noise
    elif scenario=='B_one_nonFe': x=0.75*f+0.85*e[:,1]+noise
    elif scenario=='C_multi_nonFe': x=0.65*f+0.45*h+0.55*e[:,1]+0.45*e[:,2]+0.25*e[:,3]+noise
    elif scenario=='D_perturbed':
        x=0.75*f+0.85*e[:,1]+noise
        # prespecified perturbations: 10% magnetic outliers; lower 20% Cu/Ni left-censored to their threshold
        k=max(1,int(round(.10*n))); ids=rng.choice(n,k,replace=False); x[ids]+=rng.normal(loc=0,scale=5.0,size=k)
        for j in [1,2]:
            q=np.quantile(C[:,j],.20); C[:,j]=np.maximum(C[:,j],q)
    else: raise ValueError(scenario)
    return x,C,f

def main():
    root=Path(__file__).resolve().parents[1];res=root/'results';res.mkdir(exist_ok=True)
    rng=np.random.default_rng(2026101221); scenarios=['A_Fe_only','B_one_nonFe','C_multi_nonFe','D_perturbed']; rows=[]
    reps=1000;n=48;ntrain=32
    for sc in scenarios:
      for rep in range(reps):
        x,C,fe=generate(rng,n,sc)
        y,A=tfr.residualize(x,C,fe)
        b=tfr.bounds(y,A); eq=np.ones(4)/4
        full_eq=pearson(y,A@eq)
        perm=rng.permutation(n);tr=np.sort(perm[:ntrain]);te=np.sort(perm[ntrain:])
        trmax,ter,teq=train_apply(x,C,fe,tr,te)
        rows.append({'scenario':sc,'rep':rep,'full_equal_fe_adj':full_eq,'full_rmax_fe_adj':b['max'],'train_rmax':trmax,'test_r_selected':ter,'test_r_equal':teq})
    df=pd.DataFrame(rows);df.to_csv(res/'simulation_replicates.csv',index=False)
    summ={}
    for sc,g in df.groupby('scenario'):
      summ[sc]={}
      for c in ['full_equal_fe_adj','full_rmax_fe_adj','train_rmax','test_r_selected','test_r_equal']:
        a=g[c].to_numpy();summ[sc][c]={'q025':float(np.quantile(a,.025)),'median':float(np.median(a)),'q975':float(np.quantile(a,.975)),'mean':float(np.mean(a))}
      summ[sc]['test_selected_positive_fraction']=float((g.test_r_selected>0).mean())
      summ[sc]['test_selected_gt_0_3_fraction']=float((g.test_r_selected>.3).mean())
    (res/'simulation_summary.json').write_text(json.dumps(summ,indent=2),encoding='utf-8');print(json.dumps(summ,indent=2))
if __name__=='__main__': main()
