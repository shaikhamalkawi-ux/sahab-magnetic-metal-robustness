#!/usr/bin/env python3
"""Reproduce S14.1 training-only positive-scale comparators from frozen N4 splits.

Consumes public, historically attributed analytic CSVs and locked V34 N4
split-level results. Does not re-optimize endpoints, alter underlying data,
create an experimental validation, or infer unrecorded spatial locations.
Split indices are reconstructed from the published seed/order protocol;
original selected weights and held-out values are independently checked.
"""
import argparse,hashlib,json,sys
from pathlib import Path
import numpy as np
import pandas as pd

METALS=['Mn','Cu','Ni','Zn']
SPEC=[('Sahab','Sahab48_primary.csv','Large_Xin',2026101201),('Amman','Amman44_primary.csv','Fine_LF',2026101203),('Zagreb_field','Zagreb25_primary.csv','field_ms',2026101205),('Zagreb_lab','Zagreb25_primary.csv','lab_ms',2026101207)]
GIT_BLOBS={'Sahab48_primary.csv':'6e7a7bf8092ec635a2e2177332005cae85445b12','Amman44_primary.csv':'81881e3d7d4596ea2fd1ce2be7295f9cd366e6d7','Zagreb25_primary.csv':'d1a514bf037da9b8a62167b95e5839e466eb44a4'}

def pearson(a,b):
    a=np.asarray(a,float);b=np.asarray(b,float);a=a-a.mean();b=b-b.mean()
    return float(a@b/(np.linalg.norm(a)*np.linalg.norm(b)))

def check_blob(path):
    b=path.read_bytes();v=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    if v!=GIT_BLOBS[path.name]:raise ValueError(f'Public source identity mismatch: {path.name} {v}')
    return {'git_blob_sha1':v,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}

def run(data_root, output_root):
    output_root.mkdir(parents=True,exist_ok=True)
    provenance={};results={}
    for name,fn,mag,seed in SPEC:
        inp=data_root/fn;provenance[fn]=check_blob(inp)
        df=pd.read_csv(inp);replay=pd.read_csv(data_root/f'{name}_n4_heldout_REPLAY.csv')
        n=len(df); n_train=int(round(2*n/3)); n_train=max(len(METALS)+3,min(n-4,n_train))
        x=df[mag].to_numpy(float);f=df['Fe'].to_numpy(float);C=df[METALS].to_numpy(float)
        rng=np.random.default_rng(seed);raw=[];g=np.ones(4)/4
        for i in range(2000):
            p=rng.permutation(n);tr=np.sort(p[:n_train]);te=np.sort(p[n_train:]);srow=replay.iloc[i]
            assert int(srow['split'])==i
            Ztr=np.column_stack((np.ones(len(tr)),f[tr])); Zte=np.column_stack((np.ones(len(te)),f[te]));
            bx=np.linalg.lstsq(Ztr,x[tr],rcond=None)[0];bC=np.linalg.lstsq(Ztr,C[tr],rcond=None)[0]
            yt=x[te]-Zte@bx;At=C[te]-Zte@bC
            chosen=srow[['w_'+m for m in METALS]].to_numpy(float)
            selected=pearson(yt,At@chosen);equal=pearson(yt,At@g)
            std=C[tr].std(axis=0,ddof=1)
            assert (std>0).all()
            w_sd=1/std;w_sd/=w_sd.sum()
            sd=pearson(yt,At@w_sd)
            res={'split':i,'selected_test_r':selected,'equal_raw_test_r':equal,'sd_test_r':sd,
                 'selected_gt_equal':int(selected>equal),'selected_gt_sd':int(selected>sd)}
            if name=='Sahab':
                bg=df.iloc[tr].Activity.eq('Background').to_numpy()
                support=int(bg.sum());assert support>0
                mean=C[tr][bg].mean(axis=0);assert (mean>0).all()
                w_bg=1/mean;w_bg/=w_bg.sum();bg_corr=pearson(yt,At@w_bg)
                res.update(bg_rows=support,bg_test_r=bg_corr,selected_gt_bg=int(selected>bg_corr))
            raw.append(res)
        out=pd.DataFrame(raw)
        selected_diff=float(np.max(np.abs(out.selected_test_r.values-replay.test_selected.values)))
        equal_diff=float(np.max(np.abs(out.equal_raw_test_r.values-replay.test_equal.values)))
        if max(selected_diff,equal_diff)>1e-9:raise ValueError(f'{name}: frozen N4 replay mismatch: {selected_diff} {equal_diff}')
        out.to_csv(output_root/f'{name}_S14_1_frozen_split_comparators.csv',index=False,float_format='%.15g')
        q=lambda a:{'median':float(np.median(a)),'q025':float(np.quantile(a,.025)),'q975':float(np.quantile(a,.975))}
        summ={'n':n,'seed':seed,'n_splits':len(out),'train_n':n_train,'test_n':n-n_train,'source_weights_replay_max_diff':selected_diff,'source_equal_replay_max_diff':equal_diff,
              'test_selected':q(out.selected_test_r),'test_SD':q(out.sd_test_r),
              'selected_gt_equal_count':int(out.selected_gt_equal.sum()),'selected_gt_equal_pct':float(100*out.selected_gt_equal.mean()),
              'selected_gt_SD_count':int(out.selected_gt_sd.sum()),'selected_gt_SD_pct':float(100*out.selected_gt_sd.mean())}
        if name=='Sahab':
            summ['background_support_counts']={int(k):int(v) for k,v in out.bg_rows.value_counts().sort_index().items()}
            summ['background_conditioned']={str(k):{'eligible_splits':len(z),'background_median':float(z.bg_test_r.median()),'selected_gt_background_count':int(z.selected_gt_bg.sum()),'selected_gt_background_pct':float(100*z.selected_gt_bg.mean())}
                                            for k,z in [(1,out[out.bg_rows>=1]),(2,out[out.bg_rows>=2]),(3,out[out.bg_rows>=3])]}
        results[name]=summ
    checks={
    'Sahab':{'test_SD_median':.004,'selected_gt_equal_pct':24.95,'selected_gt_SD_pct':15.25},
    'Amman':{'test_SD_median':.760,'selected_gt_equal_pct':94.30,'selected_gt_SD_pct':52.45},
    'Zagreb_field':{'test_SD_median':.594,'selected_gt_equal_pct':72.65,'selected_gt_SD_pct':91.10},
    'Zagreb_lab':{'test_SD_median':.561,'selected_gt_equal_pct':62.70,'selected_gt_SD_pct':66.60}}
    verification=[]
    for name,v in checks.items():
        actual=results[name]
        for key,ref in v.items():
            val=actual['test_SD']['median'] if key=='test_SD_median' else actual[key]
            tol=.0005 if key=='test_SD_median' else 1e-8
            verification.append({'dataset':name,'metric':key,'expected_paper':ref,'replayed':val,'tolerance':tol,'pass':abs(val-ref)<=tol})
    for lower,n_expected,median,percentage in [(1,2000,.022,11.05),(2,1978,.024,11.02),(3,1849,.028,10.87)]:
        d=results['Sahab']['background_conditioned'][str(lower)]
        for key,expect,tol in [('eligible_splits',n_expected,0),('background_median',median,.0005),('selected_gt_background_pct',percentage,.0051)]:
            verification.append({'dataset':'Sahab','metric':f'bg_{lower}_{key}','expected_paper':expect,'replayed':d[key],'tolerance':tol,'pass':abs(d[key]-expect)<=tol})
    final={'provenance':provenance,'results':results,'verification':verification,'all_pass':all(e['pass'] for e in verification)}
    (output_root/'S14_1_replay_summary.json').write_text(json.dumps(final,indent=2)+'\n',encoding='utf-8')
    if not final['all_pass']:raise ValueError('One or more locked reported values DID NOT reproduce: see S14_1_replay_summary.json')
    print(json.dumps({'all_pass':final['all_pass'],'checks':len(verification),'Sahab':results['Sahab'],'Amman':results['Amman']},indent=2))
    return final

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--inputs',type=Path,default=Path(__file__).resolve().parents[1]/'inputs_public');p.add_argument('--results',type=Path,default=Path(__file__).resolve().parents[1]/'results');a=p.parse_args();run(a.inputs,a.results)
