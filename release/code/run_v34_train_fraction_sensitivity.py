#!/usr/bin/env python3
import json, sys
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parent))
from run_v34_stability import run_splits, summarize, DATASETS
root=Path(__file__).resolve().parents[1]; res=root/'results'; res.mkdir(exist_ok=True)
fracs=[0.60,0.75]; seed=2026101211; out={}
i=0
for frac in fracs:
    key=f'{frac:.2f}'; out[key]={}
    for name,spec in DATASETS.items():
        # N4 only for split-fraction sensitivity
        df=pd.read_csv(root/spec['file'])
        d,invalid=run_splits(df,spec['mag'],spec['fe'],spec['n4'],seed+i,1000,frac);i+=1
        out[key][name]=summarize(d,invalid)
        d.to_csv(res/f'{name}_n4_heldout_trainfrac_{key}.csv',index=False)
(res/'heldout_train_fraction_sensitivity.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
