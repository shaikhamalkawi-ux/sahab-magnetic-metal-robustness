#!/usr/bin/env python3
import argparse, csv, json, math, sys
from pathlib import Path
import numpy as np
import pandas as pd

ENGINE = Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE))
import target_family_robustness as tfr

DATASETS = {
    'Sahab': {
        'file':'Sahab48_primary.csv','mag':'Large_Xin','mag2':None,'fe':'Fe',
        'n4':['Mn','Cu','Ni','Zn'],'n5':['Mn','Cu','Ni','Zn','Pb']},
    'Amman': {
        'file':'Amman44_primary.csv','mag':'Fine_LF','mag2':'Coarse_LF','fe':'Fe',
        'n4':['Mn','Cu','Ni','Zn'],'n5':['Mn','Cu','Ni','Zn','Pb']},
    'Zagreb_field': {
        'file':'Zagreb25_primary.csv','mag':'field_ms','mag2':'lab_ms','fe':'Fe',
        'n4':['Mn','Cu','Ni','Zn'],'n5':['Mn','Cu','Ni','Zn','Pb']},
    'Zagreb_lab': {
        'file':'Zagreb25_primary.csv','mag':'lab_ms','mag2':'field_ms','fe':'Fe',
        'n4':['Mn','Cu','Ni','Zn'],'n5':['Mn','Cu','Ni','Zn','Pb']},
}

def fit_residual_model(train_x, train_C, train_fe):
    Z=np.column_stack([np.ones(len(train_fe)), train_fe])
    bx=np.linalg.lstsq(Z,train_x,rcond=None)[0]
    bC=np.linalg.lstsq(Z,train_C,rcond=None)[0]
    y=train_x-Z@bx
    A=train_C-Z@bC
    return bx,bC,y,A

def apply_residual_model(x,C,fe,bx,bC):
    Z=np.column_stack([np.ones(len(fe)), fe])
    return x-Z@bx, C-Z@bC

def pearson(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    a=a-a.mean(); b=b-b.mean()
    den=np.linalg.norm(a)*np.linalg.norm(b)
    return np.nan if den<=1e-14 else float(a@b/den)

def run_splits(df, mag, fe_col, metals, seed, nsplits=2000, train_frac=2/3):
    rng=np.random.default_rng(seed)
    n=len(df); ntrain=int(round(n*train_frac)); ntrain=max(len(metals)+3,min(n-4,ntrain))
    x=df[mag].to_numpy(float); fe=df[fe_col].to_numpy(float); C=df[metals].to_numpy(float)
    eq=np.ones(len(metals))/len(metals)
    out=[]
    invalid=0
    for s in range(nsplits):
        perm=rng.permutation(n); tr=np.sort(perm[:ntrain]); te=np.sort(perm[ntrain:])
        try:
            bx,bC,ytr,Atr=fit_residual_model(x[tr],C[tr],fe[tr])
            b=tfr.bounds(ytr,Atr); w=np.array(b['max_weights'],float)
            yte,Ate=apply_residual_model(x[te],C[te],fe[te],bx,bC)
            r_test=pearson(yte,Ate@w)
            r_eq=pearson(yte,Ate@eq)
            if not np.isfinite(r_test) or not np.isfinite(r_eq): raise ValueError('undefined heldout correlation')
            top=int(np.argmax(w))
            out.append({
                'split':s,'n_train':len(tr),'n_test':len(te),'train_rmax':b['max'],
                'test_r_selected':r_test,'test_r_equal':r_eq,'optimism_gap':b['max']-r_test,
                'top_component':metals[top],
                **{f'w_{m}':float(v) for m,v in zip(metals,w)}
            })
        except Exception:
            invalid+=1
    return pd.DataFrame(out), invalid

def summarize(d, invalid):
    def qs(col):
        a=d[col].to_numpy(float)
        return {'q025':float(np.quantile(a,.025)),'median':float(np.median(a)),'q975':float(np.quantile(a,.975)),'mean':float(np.mean(a))}
    top=d['top_component'].value_counts(normalize=True).to_dict()
    return {
        'valid_splits':int(len(d)),'invalid_splits':int(invalid),
        'train_rmax':qs('train_rmax'),'test_r_selected':qs('test_r_selected'),
        'test_r_equal':qs('test_r_equal'),'optimism_gap':qs('optimism_gap'),
        'test_positive_fraction':float((d['test_r_selected']>0).mean()),
        'test_gt_0_3_fraction':float((d['test_r_selected']>0.3).mean()),
        'selected_beats_equal_fraction':float((d['test_r_selected']>d['test_r_equal']).mean()),
        'top_component_fraction':{str(k):float(v) for k,v in top.items()},
        'weight_medians':{c[2:]:float(d[c].median()) for c in d.columns if c.startswith('w_')},
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default=str(Path(__file__).resolve().parents[1])); ap.add_argument('--splits',type=int,default=2000); args=ap.parse_args()
    root=Path(args.root); res=root/'results'; res.mkdir(exist_ok=True)
    allsum={}
    seedbase=2026101201
    idx=0
    for name,spec in DATASETS.items():
        df=pd.read_csv(root/spec['file'])
        allsum[name]={}
        for fam in ['n4','n5']:
            metals=spec[fam]
            d,invalid=run_splits(df,spec['mag'],spec['fe'],metals,seedbase+idx,args.splits)
            idx+=1
            d.to_csv(res/f'{name}_{fam}_heldout_splits.csv',index=False)
            allsum[name][fam]=summarize(d,invalid)
    (res/'heldout_summary.json').write_text(json.dumps(allsum,indent=2),encoding='utf-8')
    print(json.dumps(allsum,indent=2))
if __name__=='__main__': main()
