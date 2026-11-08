"""New spectral diagnostics on frozen v86-route derived observations; no raw edits."""
from pathlib import Path
import json,sys,importlib.metadata
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from loader import load,projector,residualize,ROOT

def scan(t,Y,freq,N):
    if Y.ndim==1:Y=Y[:,None]
    Q=projector(N);Y=residualize(Y,Q);out=[]
    for lo in range(0,len(freq),96):
        angle=2*np.pi*t[:,None]*freq[lo:lo+96]
        co=residualize(np.cos(angle),Q);si=residualize(np.sin(angle),Q)
        G=np.empty((co.shape[1],2,2));G[:,0,0]=(co*co).sum(0);G[:,1,1]=(si*si).sum(0)
        G[:,0,1]=G[:,1,0]=(co*si).sum(0)
        rhs=np.stack([co.T@Y,si.T@Y],axis=1)
        delta=np.einsum('fki,fki->fi',rhs,np.linalg.solve(G,rhs))
        out.append(np.maximum(0,delta))
    return np.vstack(out)

def joint(y,B,N):
    Q=projector(N);b=residualize(B,Q);v=residualize(y,Q)
    a=np.linalg.lstsq(b,v,rcond=None)[0];r=v-b@a
    cov=np.linalg.inv(b.T@b)*(r@r)/(len(y)-Q.shape[1]-B.shape[1])
    return a,cov,r,float(np.linalg.cond(b/np.linalg.norm(b,axis=0)))

def main():
    x=load();r=x['rows'];y=x['y'];t=x['elapsed'];N=x['N'];Z=x['Z'];P=x['pairs'];fm=x['freq']
    old=pd.read_csv(ROOT/'inputs/semidiurnal_spectrum.csv');old=old[old.frequency_uHz.between(21,24.5)].copy()
    f=old.frequency_uHz.to_numpy()*1e-6
    original=scan(t,y,f,Z)[:,0]*600e-42
    np.testing.assert_allclose(original,old.observed_fractional_frequency_PSD_per_uHz,rtol=2e-7,atol=1e-46)
    B=np.column_stack([P['M2'],P['S2']]);a,cov,res,condition=joint(y,B,N)
    am0=joint(y,B,Z)[0]
    # UTC-day-deletion refits keep the actual remaining segments; all nuisance terms refit.
    reps=[]
    for day in np.unique(x['days']):
        keep=x['days']!=day;NN=N[keep];NN=NN[:,np.any(NN!=0,axis=0)]
        reps.append(joint(y[keep],B[keep],NN)[0])
    reps=np.array(reps);dr=reps-reps.mean(0);cvday=(len(reps)-1)/len(reps)*(dr.T@dr)
    modelM=P['M2']@a[:2];modelS=P['S2']@a[2:]
    Y=np.column_stack([y,y-modelM,y-modelS,y-modelM-modelS,modelM,modelS,modelM+modelS])
    raw=scan(t,Y,f,N);density=raw*6e-5
    cols=['observed_N2K2_controlled','minus_M2','minus_S2','minus_both','M2_only_fitted_phase','S2_only_fitted_phase','M2_plus_S2_model']
    tab=pd.DataFrame({'frequency_uHz':f*1e6})
    for k,name in enumerate(cols):tab[name+'_density_1e35_per_uHz']=density[:,k]
    tab['original_observed_density_1e35_per_uHz']=original/1e-35
    tab['original_after_unit_prediction_density_1e35_per_uHz']=old.residual_fractional_frequency_PSD_per_uHz.to_numpy()/1e-35
    conditional=[];nominal=[]
    for target,other in [('M2','S2'),('S2','M2')]:
        nn=np.column_stack([N,P[other]])
        take=abs(f-fm[target])<.16e-6
        d=scan(t,y,f[take],nn)[:,0]*6e-5
        conditional.extend([dict(target=target,conditioned_on=other,frequency_uHz=ff*1e6,density_1e35_per_uHz=dd) for ff,dd in zip(f[take],d)])
        v=scan(t,y,np.array([fm[target]]),nn)[0,0]
        # Verify the conditional score by a direct full-nuisance nested-model fit.
        Q=projector(nn);v0=residualize(y,Q);full=np.column_stack([nn,P[target]])
        rr=y-full@np.linalg.lstsq(full,y,rcond=None)[0];direct=v0@v0-rr@rr
        np.testing.assert_allclose(v,direct,rtol=2e-9,atol=1e-7)
        nominal.append(dict(target=target,conditional_delta_RSS_e36=float(v),conditional_density_1e35_per_uHz=float(v*6e-5)))
    cf=pd.DataFrame(conditional)
    # Deterministic fitted-phase injections: no invented observations, no added noise.
    nominal_inj=scan(t,np.column_stack([modelM,modelS]),np.array([fm['M2'],fm['S2']]),N)
    leak=dict(M2_at_S2=float(nominal_inj[1,0]/nominal_inj[0,0]),S2_at_M2=float(nominal_inj[0,1]/nominal_inj[1,1]),
              definition='opposite-frequency DeltaRSS divided by own-frequency DeltaRSS; fitted-phase pure sinusoids, equal-weight S54+free N2/K2; not astronomical nodal injections')
    # Joint nuisance control, single subtraction and simultaneous fits agree exactly at the nominal pair.
    both_check=joint(y-modelM-modelS,B,N)[0]
    assert np.max(abs(both_check))<1e-10
    uncontrolled=scan(t,y,f,Z)[:,0]*6e-5
    peaks=[]
    for name in ['M2','S2']:
        take=abs(f-fm[name])<1/np.ptp(x['t']);inds=np.where(take)[0]
        i=inds[np.argmax(density[inds,0])]
        peaks.append({'target':name,'controlled_local_grid_max_uHz':float(f[i]*1e6),'density_1e35_per_uHz':float(density[i,0])})
    result=dict(status='COMPUTED_AUXILIARY_NONOVERLAPPING_ROUTE',n_rows=len(r),n_segments=int(r.seg.nunique()),n_days=len(np.unique(x['days'])),
        accepted_member_hours=float(r.n.sum()/3600),calendar_span_days=float(np.ptp(x['t'])/86400),
        weights='equal for spectra and this joint harmonic fit; not the campaign-weighted physical coefficient fit',
        unit='y values in fractional-frequency units of 1e-18; nominal600 density per microhertz = 600*DeltaRSS*1e-42',
        normalization='deltaRSS is nonnegative reduction after fitting a trial cosine-sine pair with identical nuisance projection on response and pair; no Parseval claim',
        baseline='54 segment constants plus freely phased N2 and K2; raw rows.y, no fixed physical-template subtraction',
        bin_operator='sinusoids evaluated at stored bin-centre UTC times, as in v86 spectra; not reconstructed within-bin membership or v29 triangular filtering',
        frequency_Hz=fm,joint_order=['M2_cos','M2_sin','S2_cos','S2_sin'],joint_coefficients_e18=a.tolist(),
        joint_scaled_LS_covariance_e36=cov.tolist(),joint_UTC_day_jackknife_covariance_e36=cvday.tolist(),
        joint_working_coefficient_SE_e18=np.maximum(np.sqrt(np.diag(cov)),np.sqrt(np.diag(cvday))).tolist(),
        joint_amplitudes_e18=[float(np.hypot(*a[:2])),float(np.hypot(*a[2:]))],
        without_N2K2_joint_coefficients_e18=am0.tolist(),normalized_design_condition=condition,
        conditional_nominal=nominal,controlled_grid_peaks=peaks,fitted_phase_injection_cross_power=leak,
        original_spectrum_max_relative_error=float(np.max(abs(original/old.observed_fractional_frequency_PSD_per_uHz.to_numpy()-1))),
        tests=['input hashes and timestamps verified','original observed spectrum reproduced','conditional score agrees with full nested regression','subtracting joint M2/S2 removes their joint coefficients'],
        significance='No new false-alarm probability or calibrated detection significance computed; coefficient SEs are descriptive scaled-LS/day-jackknife checks.',
        model_scope='No solar or diurnal nuisance terms beyond N2/K2; this is a specified local harmonic diagnostic, not a full physical tide fit.',
        software={'python':sys.version,'packages':{k:importlib.metadata.version(k) for k in ['numpy','pandas','matplotlib']}})
    (ROOT/'results').mkdir(exist_ok=True)
    tab.to_csv(ROOT/'results/spectra.csv',index=False);cf.to_csv(ROOT/'results/conditional.csv',index=False)
    (ROOT/'results/NUMERIC_RESULTS.json').write_text(json.dumps(result,indent=2))
    np.savez_compressed(ROOT/'results/joint_refits.npz',day_delete_coefficients=reps,days=np.unique(x['days']))
    plt.rcParams.update({'font.size':8,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
    fig,axs=plt.subplots(2,2,figsize=(9,6.8),sharex=True,sharey=True,constrained_layout=True)
    c=['#2166ac','#d95f02','#1b9e77','#555555']
    ax=axs[0,0];ax.plot(f*1e6,original/1e-35,color=c[0],lw=1,label='Observed')
    ax.plot(f*1e6,tab.original_after_unit_prediction_density_1e35_per_uHz,color=c[1],lw=.9,label='After unit physical prediction')
    ax.set_title('a  Existing spectral route, reproduced',loc='left')
    ax=axs[0,1]
    for i,label in enumerate(['Observed, N₂/K₂ controlled','Subtract fitted M₂','Subtract fitted S₂','Subtract both']):
        ax.plot(f*1e6,density[:,i],color=c[i],lw=1 if i==0 else .8,ls=['-','--','-.',':'][i],label=label)
    ax.set_title('b  Single-component subtraction',loc='left')
    ax=axs[1,0];ax.plot(f*1e6,density[:,0],color='.65',lw=.8,label='N₂/K₂ controlled baseline')
    for target,color in [('M2',c[0]),('S2',c[1])]:
        z=cf[cf.target==target];ax.plot(z.frequency_uHz,z.density_1e35_per_uHz,color=color,lw=1.3,label=target+' conditional on '+('S₂' if target=='M2' else 'M₂'))
    ax.set_title('c  Conditional frequency scans',loc='left')
    ax=axs[1,1];ax.plot(f*1e6,density[:,0],color='.65',lw=.8,label='Observed, N₂/K₂ controlled')
    for i,label,col in [(4,'M₂-only fitted-phase injection',c[0]),(5,'S₂-only fitted-phase injection',c[1]),(6,'Joint M₂ + S₂ waveform',c[2])]:
        ax.plot(f*1e6,density[:,i],color=col,lw=.9,ls='--' if i<6 else '-',label=label)
    ax.set_title('d  Actual-window response and sidelobes',loc='left')
    ymax=max(float(original.max()/1e-35),float(density.max()),float(cf.density_1e35_per_uHz.max()),float(tab.original_after_unit_prediction_density_1e35_per_uHz.max()))*1.36
    for ax in axs.flat:
        for name in ['N2','M2','S2','K2']:ax.axvline(fm[name]*1e6,color='.75',lw=.5,ls=':')
        ax.set_xlim(21,24.5);ax.set_ylim(0,ymax);ax.set_yscale('linear');ax.legend(loc='upper left',fontsize=6.8,frameon=False)
    for ax in axs[1]:ax.set_xlabel('Frequency (µHz)')
    for ax in axs[:,0]:ax.set_ylabel('Nominal 600 s LS density\n(10⁻³⁵ fractional-frequency²/µHz)')
    fig.suptitle('Auxiliary 600 s non-overlapping route · 3,299 rows · 54 segment constants',fontsize=11)
    fig.savefig(ROOT/'results/ED7_v86_auxiliary_spectra.pdf');fig.savefig(ROOT/'results/ED7_v86_auxiliary_spectra.png',dpi=190)
    print(json.dumps({k:result[k] for k in ['n_rows','accepted_member_hours','joint_coefficients_e18','joint_working_coefficient_SE_e18','joint_amplitudes_e18','fitted_phase_injection_cross_power','original_spectrum_max_relative_error']},indent=2))

if __name__=='__main__':main()
