"""Shared frozen 600 s non-overlapping route: equal-weight bin-centre spectra."""
from pathlib import Path
import hashlib, json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent

def load():
    for item in json.loads((ROOT/'input_manifest.json').read_text()):
        assert hashlib.sha256((ROOT/item['copy']).read_bytes()).hexdigest()==item['sha256']
    rows=pd.read_csv(ROOT/'inputs/primary_rows.csv')
    d=np.load(ROOT/'inputs/design.npz')
    t=pd.to_datetime(rows.t_utc,utc=True).dt.as_unit('ns').astype('int64').to_numpy()/1e9
    np.testing.assert_array_equal(t,d['seconds'])
    np.testing.assert_array_equal(rows.seg,d['seg'])
    np.testing.assert_allclose(rows.y-rows.fixed_remainder,d['y'],rtol=0,atol=1e-12)
    assert len(rows)==3299 and rows.seg.nunique()==54
    freq=json.loads((ROOT/'inputs/RESULTS.json').read_text())['spectrum']['frequency_Hz']
    t0=t.min();elapsed=t-t0
    pairs={name:np.column_stack([np.cos(2*np.pi*f*elapsed),np.sin(2*np.pi*f*elapsed)]) for name,f in freq.items()}
    Z=(rows.seg.to_numpy()[:,None]==np.unique(rows.seg)[None,:]).astype(float)
    N=np.column_stack([Z,pairs['N2'],pairs['K2']])
    return dict(rows=rows,t=t,elapsed=elapsed,y=rows.y.to_numpy(),freq=freq,pairs=pairs,Z=Z,N=N,
                days=pd.to_datetime(rows.t_utc,utc=True).dt.strftime('%Y-%m-%d').to_numpy())

def projector(N):
    u,s,_=np.linalg.svd(N,full_matrices=False)
    return u[:,s>s[0]*1e-12]

def residualize(v,Q):
    return v-Q@(Q.T@v)
