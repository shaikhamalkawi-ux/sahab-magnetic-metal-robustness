#!/usr/bin/env python3
"""Finite-sample robustness envelope for magnetic--metal correlations.

Computes the complete signed Pearson-correlation range over every nonnegative
additive weighting of a declared metal set, with optional Fe residualization.
If --magnetic2 is supplied, it also computes the complete common-target
correlation-difference range magnetic1 minus magnetic2.

The coefficient vector is a mathematical witness, not a recommended pollution
index. Inputs are ordinary CSV columns; no domain-specific row filtering is
performed by this script.
"""
import argparse,csv,itertools,json
from pathlib import Path
import numpy as np
from scipy.optimize import nnls

def load_csv(path, cols):
    with open(path,encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    arr={c:np.array([float(r[c]) for r in rows],float) for c in cols}
    return rows,arr

def residualize(x,C,fe=None):
    n=len(x)
    Z=np.ones((n,1)) if fe is None else np.column_stack([np.ones(n),fe])
    if np.linalg.matrix_rank(Z)!=Z.shape[1]: raise ValueError('rank-deficient adjustment design')
    y=x-Z@np.linalg.lstsq(Z,x,rcond=None)[0]
    A=C-Z@np.linalg.lstsq(Z,C,rcond=None)[0]
    return y,A

def bounds(y,A):
    y=np.asarray(y,float);A=np.asarray(A,float);ny=np.linalg.norm(y)
    if ny<=1e-13: raise ValueError('constant magnetic residual')
    scale=np.linalg.norm(A,axis=0)
    if np.any(scale<=1e-13): raise ValueError('constant metal residual')
    B=A/scale
    s=np.linalg.svd(B,compute_uv=False)
    if s[-1]/s[0]<=1e-10: raise ValueError('rank-deficient chemical matrix')
    G=B.T@B;c=B.T@y;p=B.shape[1];cand=[]
    for k in range(1,p+1):
        for face in itertools.combinations(range(p),k):
            if k==1:
                v=np.zeros(p);v[face[0]]=1.0
                cand.append((float(y@(B@v)/(ny*np.linalg.norm(B@v))),v));continue
            t=np.linalg.solve(G[np.ix_(face,face)],c[list(face)])
            for vv in (t,-t):
                if np.min(vv)>1e-10:
                    v=np.zeros(p);v[list(face)]=vv/vv.sum()
                    cand.append((float(y@(B@v)/(ny*np.linalg.norm(B@v))),v))
    if not cand: raise RuntimeError('no feasible active-face candidates')
    lo,lw=min(cand,key=lambda z:z[0]); hi,hw=max(cand,key=lambda z:z[0])
    def unscale(v):
        q=v/scale; q=q/q.sum(); return [float(x) for x in q]
    # independent NNLS projection check
    def projmax(yy):
        u=yy/np.linalg.norm(yy);w=nnls(B,u,maxiter=50*p)[0];z=B@w
        if np.linalg.norm(z)>1e-10:return float(np.linalg.norm(z))
        return max(float(yy@B[:,j]/(np.linalg.norm(yy)*np.linalg.norm(B[:,j]))) for j in range(p))
    if abs(hi-projmax(y))>5e-10 or abs(lo+projmax(-y))>5e-10:raise RuntimeError('NNLS verification mismatch')
    return {'min':float(lo),'max':float(hi),'min_weights':unscale(lw),'max_weights':unscale(hw),'faces':2**p-1}

def corr(y,z): return float(y@z/(np.linalg.norm(y)*np.linalg.norm(z)))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True)
    ap.add_argument('--magnetic',required=True)
    ap.add_argument('--magnetic2')
    ap.add_argument('--fe')
    ap.add_argument('--metals',nargs='+',required=True)
    ap.add_argument('--output')
    a=ap.parse_args()
    cols=[a.magnetic]+([a.magnetic2] if a.magnetic2 else [])+([a.fe] if a.fe else [])+a.metals
    rows,d=load_csv(a.input,cols)
    C=np.column_stack([d[m] for m in a.metals]); fe=d[a.fe] if a.fe else None
    y,A=residualize(d[a.magnetic],C,fe)
    out={'n':len(rows),'magnetic':a.magnetic,'fe':a.fe,'metals':a.metals,'range':bounds(y,A)}
    if a.magnetic2:
        z,_=residualize(d[a.magnetic2],C,fe)
        u1=y/np.linalg.norm(y);u2=z/np.linalg.norm(z);delta=u1-u2
        if np.linalg.norm(delta)<=1e-13:
            db={'min':0.0,'max':0.0,'min_weights':[1/len(a.metals)]*len(a.metals),'max_weights':[1/len(a.metals)]*len(a.metals),'faces':2**len(a.metals)-1}
        else:
            b=bounds(delta,A); b['min']*=np.linalg.norm(delta); b['max']*=np.linalg.norm(delta); db=b
        out['magnetic2']=a.magnetic2;out['common_target_difference']=db;out['channel_correlation']=corr(y,z)
    txt=json.dumps(out,indent=2)
    print(txt)
    if a.output: Path(a.output).write_text(txt,encoding='utf-8')
if __name__=='__main__':main()
