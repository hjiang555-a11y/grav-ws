"""Recover sine/cosine coefficients on unchanged frozen grids; no new noise fitting."""
from pathlib import Path
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
import json,hashlib,platform
import numpy as np
import pandas as pd
from loader_amplitude import load,projector,residualize
from plot_config import CM_PER_1E18
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'data/amplitude';OUT.mkdir(exist_ok=True)
FA=ROOT/'data/frozen_auxiliary';FC=ROOT/'data/frozen_coupling'
SEED=20261108
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
SCAN_DIAGNOSTICS=[]
def scan(t,Y,f,N):
    if Y.ndim==1:Y=Y[:,None]
    Q=projector(N);Y=residualize(Y,Q);co=[];pw=[];grams=[];diagnostics=[]
    for lo in range(0,len(f),96):
        angle=2*np.pi*t[:,None]*f[lo:lo+96]
        c0,s0=np.cos(angle),np.sin(angle)
        c=residualize(c0,Q);s=residualize(s0,Q)
        G=np.empty((c.shape[1],2,2));G[:,0,0]=(c*c).sum(0);G[:,1,1]=(s*s).sum(0);G[:,0,1]=G[:,1,0]=(c*s).sum(0)
        rawG=np.empty_like(G);rawG[:,0,0]=(c0*c0).sum(0);rawG[:,1,1]=(s0*s0).sum(0);rawG[:,0,1]=rawG[:,1,0]=(c0*s0).sum(0)
        singular=np.sqrt(np.maximum(np.linalg.eigvalsh(G),0));raw_scale=np.sqrt(np.linalg.eigvalsh(rawG)[:,-1])
        ratios=singular/raw_scale[:,None];ranks=np.sum(ratios>1e-12,axis=1);valid=ranks==2
        rhs=np.stack([c.T@Y,s.T@Y],axis=1)
        beta=np.full_like(rhs,np.nan);power=np.full((len(rhs),Y.shape[1]),np.nan)
        # A coincident nuisance frequency has no unique extra sinusoidal pair.
        # Never invert its near-zero floating-point Gram matrix.
        beta[valid]=np.linalg.solve(G[valid],rhs[valid])
        power[valid]=np.einsum('fki,fkl,fli->fi',beta[valid],G[valid],beta[valid])
        np.testing.assert_allclose(power[valid],np.einsum('fki,fki->fi',rhs[valid],beta[valid]),rtol=2e-12,atol=1e-9)
        for j in range(len(rhs)):
            diagnostics.append({'frequency_uHz':float(f[lo+j]*1e6),'is_identifiable':bool(valid[j]),'rank':int(ranks[j]),'singular_values_relative_to_original_pair':ratios[j].tolist(),'Gram_eigenvalues':np.linalg.eigvalsh(G[j]).tolist(),'Gram_trace':float(np.trace(G[j])),'status':'identifiable' if valid[j] else 'non_identifiable'})
        co.append(beta);pw.append(power);grams.append(G)
    SCAN_DIAGNOSTICS.append(diagnostics)
    return np.concatenate(co),np.concatenate(pw),np.concatenate(grams)

def add_columns(out,prefix,b):
    out[prefix+'_cos_1e18']=b[:,0];out[prefix+'_sin_1e18']=b[:,1]
    out[prefix+'_amplitude_cm']=np.hypot(b[:,0],b[:,1])*CM_PER_1E18
checks=[]
def compare(name,new,old):
    new,old=np.asarray(new),np.asarray(old);valid=np.isfinite(new)
    np.testing.assert_allclose(new[valid],old[valid],rtol=2e-7,atol=2e-10)
    err=np.abs(new[valid]-old[valid]);checks.append({'check':name,'max_absolute_difference':float(err.max()),'n_identifiable_compared':int(valid.sum()),'non_identifiable_legacy_scores_not_validated':[{'row':int(i),'old_density':float(old[i])} for i in np.flatnonzero(~valid)],'status':'PASS on identifiable frequencies only'})
def direct_checks(name,t,Y,f,N,b,p,indices):
    if Y.ndim==1:Y=Y[:,None]
    Q=projector(N);base=residualize(Y,Q)
    for i in indices:
        if not np.all(np.isfinite(b[i])):
            checks.append({'check':name+' independent full LS','frequency_uHz':float(f[i]*1e6),'status':'Skipped structurally non-identifiable target pair'})
            continue
        X=np.column_stack([N,np.cos(2*np.pi*f[i]*t),np.sin(2*np.pi*f[i]*t)])
        beta=np.linalg.lstsq(X,Y,rcond=None)[0];r=Y-X@beta
        np.testing.assert_allclose(beta[-2:],b[i],rtol=2e-8,atol=2e-9)
        nested=np.sum(base*base,axis=0)-np.sum(r*r,axis=0)
        np.testing.assert_allclose(nested,p[i],rtol=2e-7,atol=2e-7)
        checks.append({'check':name+' independent full LS','frequency_uHz':float(f[i]*1e6),'coefficient_max_abs_difference_1e18':float(np.max(np.abs(beta[-2:]-b[i]))),'Gram_vs_nested_RSS_max_abs_difference':float(np.max(np.abs(nested-p[i]))),'status':'PASS'})
def main():
    d=load();t,y,N,Z,P=d['elapsed'],d['y'],d['N'],d['Z'],d['pairs'];Q=projector(N)
    old=pd.read_csv(FA/'results/spectra.csv');cond=pd.read_csv(FA/'results/conditional.csv');ref=json.loads((FA/'results/NUMERIC_RESULTS.json').read_text())
    B=np.column_stack([P['M2'],P['S2']]);beta=np.linalg.lstsq(residualize(B,Q),residualize(y,Q),rcond=None)[0]
    np.testing.assert_allclose(beta,ref['joint_coefficients_e18'],rtol=1e-11,atol=1e-11)
    m=P['M2']@beta[:2];s=P['S2']@beta[2:]
    Y=np.column_stack([y,y-m,y-s,y-m-s,m,s,m+s]);f=old.frequency_uHz.to_numpy()*1e-6
    b,p,g=scan(t,Y,f,N);ed7_diagnostics=SCAN_DIAGNOSTICS[-1]
    names=['observed_N2K2_controlled','minus_M2','minus_S2','minus_both','M2_only_fitted_phase','S2_only_fitted_phase','M2_plus_S2_model']
    out=pd.DataFrame({'frequency_uHz':old.frequency_uHz,'controlled_pair_is_identifiable':[r['is_identifiable'] for r in ed7_diagnostics],'controlled_pair_status':[r['status'] for r in ed7_diagnostics],'projected_pair_rank':[r['rank'] for r in ed7_diagnostics],'projected_singular_ratio_min':[r['singular_values_relative_to_original_pair'][0] for r in ed7_diagnostics],'projected_singular_ratio_max':[r['singular_values_relative_to_original_pair'][1] for r in ed7_diagnostics]})
    for i,name in enumerate(names):
        add_columns(out,name,b[:,:,i]);compare('ED7 '+name+' Gram reproduces frozen density',p[:,i]*6e-5,old[name+'_density_1e35_per_uHz'])
    # ED7a uses the existing main-Fig3 amplitude; independently match its observed fit.
    mainfig=pd.read_csv(ROOT/'data/main_figure3_amplitude.csv')
    grid=mainfig.frequency_uHz.to_numpy();ix=np.searchsorted(grid,old.frequency_uHz.to_numpy())
    ix=np.minimum(ix,len(grid)-1);prev=np.maximum(ix-1,0);ix=np.where(np.abs(grid[prev]-old.frequency_uHz.to_numpy())<np.abs(grid[ix]-old.frequency_uHz.to_numpy()),prev,ix)
    np.testing.assert_allclose(grid[ix],old.frequency_uHz,rtol=0,atol=1e-10)
    baseb,basep,baseg=scan(t,y,f,Z)
    compare('ED7a baseline Gram reproduces old density',basep[:,0]*6e-5,old.original_observed_density_1e35_per_uHz)
    compare('ED7a observed amplitude agrees with main Fig3',np.hypot(baseb[:,0,0],baseb[:,1,0])*CM_PER_1E18,mainfig.observed_peak_amplitude_cm.to_numpy()[ix])
    out['original_observed_amplitude_cm']=mainfig.observed_peak_amplitude_cm.to_numpy()[ix]
    out['original_after_unit_prediction_amplitude_cm']=mainfig.after_unit_physical_prediction_peak_amplitude_cm.to_numpy()[ix]
    for label,source in [('original_observed','observed'),('original_after_unit_prediction','after_unit_physical_prediction')]:
        out[label+'_cos_1e18']=mainfig[source+'_cos_1e18'].to_numpy()[ix];out[label+'_sin_1e18']=mainfig[source+'_sin_1e18'].to_numpy()[ix]
    # Main Fig3 residual density in the frozen scan equals the saved ED7 residual curve.
    compare('ED7a residual main-Fig3 Gram density matches old ED7',mainfig.after_unit_physical_prediction_nominal_fractional_PSD_per_uHz.to_numpy()[ix]/1e-35,old.original_after_unit_prediction_density_1e35_per_uHz)
    out.to_csv(OUT/'ed7_spectra.csv',index=False)
    rng=np.random.default_rng(SEED);picked=rng.choice(len(f),size=8,replace=False)
    direct_checks('ED7 controlled',t,Y,f,N,b,p,picked)
    direct_checks('ED7a baseline',t,y,f,Z,baseb,basep,picked[:3])
    conditional=[];condgram={};conditional_nonidentifiable=[]
    for target,other in [('M2','S2'),('S2','M2')]:
        z=cond[cond.target.eq(target)];ff=z.frequency_uHz.to_numpy()*1e-6;nn=np.column_stack([N,P[other]])
        cb,cp,cg=scan(t,y,ff,nn);cd=SCAN_DIAGNOSTICS[-1];conditional_nonidentifiable.extend([dict(target=target,**r) for r in cd if not r['is_identifiable']]);compare('ED7 '+target+' conditional Gram density',cp[:,0]*6e-5,z.density_1e35_per_uHz)
        conditional.append(pd.DataFrame({'target':target,'conditioned_on':other,'frequency_uHz':z.frequency_uHz.to_numpy(),'is_identifiable':[r['is_identifiable'] for r in cd],'status':[r['status'] for r in cd],'projected_pair_rank':[r['rank'] for r in cd],'projected_singular_ratio_min':[r['singular_values_relative_to_original_pair'][0] for r in cd],'projected_singular_ratio_max':[r['singular_values_relative_to_original_pair'][1] for r in cd],'cos_1e18':cb[:,0,0],'sin_1e18':cb[:,1,0],'amplitude_cm':np.hypot(cb[:,0,0],cb[:,1,0])*CM_PER_1E18}))
        direct_checks('ED7 '+target+' conditional',t,y,ff,nn,cb,cp,rng.choice(len(ff),size=3,replace=False));condgram[target]=cg
    pd.concat(conditional,ignore_index=True).to_csv(OUT/'ed7_conditional.csv',index=False)
    # ED10 retains every saved frequency and donor identity, including the original 20–25 microHz scan.
    old10=pd.read_csv(FC/'single_injection_spectra.csv');chunks=[];grams10={}
    for donor,wave in [('M2',m),('S2',s)]:
        z=old10[old10.donor.eq(donor)];ff=z.frequency_uHz.to_numpy()*1e-6;yy=np.column_stack([wave,y,y-wave])
        cb,cp,cg=scan(t,yy,ff,N);o=pd.DataFrame({'donor':donor,'frequency_uHz':z.frequency_uHz.to_numpy()})
        for i,name in enumerate(['donor','data','compensated']):
            add_columns(o,name,cb[:,:,i]);compare('ED10 '+donor+' '+name+' Gram density',cp[:,i]*6e-5,z[name+'_density_1e35'])
        chunks.append(o);grams10[donor]=cg
        direct_checks('ED10 '+donor,t,yy,ff,N,cb,cp,rng.choice(len(ff),size=4,replace=False))
    pd.concat(chunks,ignore_index=True).to_csv(OUT/'ed10_single_injection_spectra.csv',index=False)
    np.savez_compressed(OUT/'gram_matrices.npz',ed7=g,ed7_baseline=baseg,**{'conditional_'+k:v for k,v in condgram.items()},**{'ed10_'+k:v for k,v in grams10.items()})
    inputs=[FA/'input_manifest.json',FA/'results/spectra.csv',FA/'results/conditional.csv',FA/'results/NUMERIC_RESULTS.json',FC/'single_injection_spectra.csv',ROOT/'data/main_figure3_amplitude.csv']+sorted((FA/'inputs').glob('*'))
    report={'status':'PASS','scope':'Same sampling/grid/nuisance/weights; recover fitted pair amplitude. No JK refits, new significance, screening or interpolation.','n_rows':len(y),'n_segments':int(d['rows'].seg.nunique()),'conversion_cm_per_1e18':CM_PER_1E18,'joint_coefficients_e18':beta.tolist(),'joint_max_abs_difference':float(np.max(np.abs(beta-ref['joint_coefficients_e18']))),'random_frequency_verification_seed':SEED,'row_counts':{'ed7_spectra':len(out),'ed7_conditional':len(cond),'ed10_spectra':len(old10)},'checks':checks,'input_sha256':{str(x.relative_to(ROOT)):sha(x) for x in inputs if x.is_file()},'scripts_sha256':{p.name:sha(p) for p in [Path(__file__),ROOT/'scripts/loader_amplitude.py',ROOT/'scripts/plot_config.py']},'software':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__},'threads':1,'identifiability_definition':'Both singular values of nuisance-projected pair relative to largest singular value of original pair exceed 1e-12, consistent relative rcond scale. Keep every grid row; no amplitude threshold.','non_identifiable_frequencies':[r for r in ed7_diagnostics if not r['is_identifiable']],'conditional_non_identifiable_frequencies':conditional_nonidentifiable,'n_non_identifiable_all_scans':sum(not r['is_identifiable'] for group in SCAN_DIAGNOSTICS for r in group)}
    assert sum(not r['is_identifiable'] for r in ed7_diagnostics)==2
    np.testing.assert_allclose(sorted(r['frequency_uHz'] for r in ed7_diagnostics if not r['is_identifiable']),sorted(d['freq'][k]*1e6 for k in ['N2','K2']),rtol=0,atol=1e-10)
    (OUT/'SCAN_IDENTIFIABILITY.json').write_text(json.dumps(SCAN_DIAGNOSTICS,indent=2))
    (OUT/'RECOMPUTE_VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:report[k] for k in ['status','row_counts','joint_max_abs_difference']}))
if __name__=='__main__':main()
