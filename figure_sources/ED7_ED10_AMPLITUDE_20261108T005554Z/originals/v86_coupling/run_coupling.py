"""Deterministic coupling diagnostics, frozen non-overlapping 600-s auxiliary route."""
from pathlib import Path
import sys, json, hashlib, platform
import numpy as np
import pandas as pd
import scipy
from scipy.signal import find_peaks
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(OUT.parent/'v86_auxiliary'))
from loader import load,projector,residualize

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def polar(b): return float(np.linalg.norm(b)),float(np.degrees(np.arctan2(b[1],b[0])))
def gram_power(X,b): return float(b@(X.T@X)@b)
def record(X,b):
    a,p=polar(b)
    return dict(cos=float(b[0]),sin=float(b[1]),amplitude_1e18=a,phase_deg=p,
                delta_rss_1e36=gram_power(X,b),density_1e35_per_uHz=6e-5*gram_power(X,b))

def main():
    d=load(); y=d['y']; Q=projector(d['N']); yr=residualize(y,Q)
    P={k:residualize(d['pairs'][k],Q) for k in ('M2','S2')}
    J=np.column_stack([P['M2'],P['S2']]); coef=np.linalg.lstsq(J,yr,rcond=1e-12)[0]
    betas={'M2':coef[:2],'S2':coef[2:]}
    single={k:np.linalg.lstsq(P[k],yr,rcond=1e-12)[0] for k in P}
    qq={k:projector(P[k]) for k in P}
    canonical=np.linalg.svd(qq['M2'].T@qq['S2'],compute_uv=False)
    normJ=J/np.linalg.norm(J,axis=0)
    summary=dict(route='Frozen A_v81-derived v86 auxiliary equal-weight non-overlapping 600-s bin-centre route; not v29',
                 n=len(y),segments=d['rows'].seg.nunique(),baseline_rank=Q.shape[1],
                 time_origin_utc=str(pd.to_datetime(d['t'].min(),unit='s',utc=True)),
                 frequency_Hz={k:d['freq'][k] for k in ('M2','S2','N2','K2')},
                 canonical_correlations=canonical.tolist(),canonical_squared=canonical.__pow__(2).tolist(),
                 normalized_joint_condition=float(np.linalg.cond(normJ)),
                 joint_coefficients={k:record(P[k],betas[k]) for k in P},
                 target_only_coefficients={k:record(P[k],single[k]) for k in P},directions={})
    for rec in summary['joint_coefficients'].values():
        rec['projected_component_energy_1e36']=rec.pop('delta_rss_1e36')
        rec['component_energy_nominal_density_1e35_per_uHz']=rec.pop('density_1e35_per_uHz')
    sweep=[]; lagrows=[]; aliasrows=[]; spectra=[]; identities=[]
    lamgrid=np.linspace(0,1.5,61); laggrid=np.linspace(-24,24,577)
    rayleigh=1/np.ptp(d['elapsed']); grid=np.arange(20e-6,25e-6,rayleigh/12)
    # A scan on actual bin-centre timestamps; no interpolation across missing observations.
    bases=[]; pinvs=[]
    for f in grid:
        X=residualize(np.column_stack([np.cos(2*np.pi*f*d['elapsed']),np.sin(2*np.pi*f*d['elapsed'])]),Q)
        bases.append(X);pinvs.append(np.linalg.pinv(X,rcond=1e-12))
    fig,axs=plt.subplots(3,2,figsize=(10,9),sharex=True)
    fig_alias, ax_alias=plt.subplots(2,2,figsize=(11,6))
    for column,(donor,target) in enumerate((('M2','S2'),('S2','M2'))):
        X=P[target]; D=P[donor]; inv=np.linalg.pinv(X,rcond=1e-12)
        T=inv@D; transfer=T@betas[donor]
        direction=f'{donor}_to_{target}'
        qcontrolled=projector(np.column_stack([d['N'],d['pairs'][donor]]))
        Xcontrolled=residualize(d['pairs'][target],qcontrolled)
        invcontrolled=np.linalg.pinv(Xcontrolled,rcond=1e-12)
        detail=dict(transfer_matrix=T.tolist(),unit_amplitude_transfer_singular_values=np.linalg.svd(T,compute_uv=False).tolist(),
                    delta_coefficient_per_lambda=(-transfer).tolist(),lambda0=record(X,single[target]),
                    lambda1=record(X,single[target]-transfer),joint_controlled=record(Xcontrolled,betas[target]))
        detail['amplitude_change_0_to_1']=detail['lambda1']['amplitude_1e18']-detail['lambda0']['amplitude_1e18']
        detail['phase_change_0_to_1_deg']=float(np.degrees(np.angle(np.exp(1j*np.radians(detail['lambda1']['phase_deg']-detail['lambda0']['phase_deg'])))))
        detail['relative_density_change_0_to_1']=detail['lambda1']['delta_rss_1e36']/detail['lambda0']['delta_rss_1e36']-1
        summary['directions'][direction]=detail
        for origin,donorb in (('joint',betas[donor]),('single',single[donor])):
            wave=d['pairs'][donor]@donorb
            for lam in lamgrid:
                ysub=y-lam*wave
                b=inv@residualize(ysub,Q)
                bpred=single[target]-lam*T@donorb
                identities.append(np.max(np.abs(b-bpred)))
                bc=invcontrolled@residualize(ysub,qcontrolled)
                identities.append(np.max(np.abs(bc-betas[target])))
                sweep.append(dict(direction=direction,donor_waveform=origin,lambda_=float(lam),fit='target_only',**record(X,b)))
                sweep.append(dict(direction=direction,donor_waveform=origin,lambda_=float(lam),fit='joint_controlled',**record(Xcontrolled,bc)))
        ss=pd.DataFrame(sweep);ss=ss[ss.direction.eq(direction)]
        for origin,ls in (('joint','-'),('single',':')):
            a=ss[ss.donor_waveform.eq(origin)&ss['fit'].eq('target_only')]
            vals=[a.amplitude_1e18,np.degrees(np.unwrap(np.radians(a.phase_deg))),a.density_1e35_per_uHz]
            for row,v in enumerate(vals): axs[row,column].plot(a.lambda_,v,ls,label=f'{origin}-fit donor')
        a=ss[ss.donor_waveform.eq('joint')&ss['fit'].eq('joint_controlled')]
        for row,v in enumerate([a.amplitude_1e18,a.phase_deg,a.density_1e35_per_uHz]):
            axs[row,column].plot(a.lambda_,v,'--',color='0.4',label='joint-controlled identity')
            axs[row,column].axvline(1,color='0.8',lw=.8);axs[row,column].grid(alpha=.2)
        axs[0,column].set_title(f'Subtract {donor}; re-estimate {target}')
        axs[2,column].set_xlabel('Compensation factor λ')
        targetwave=X@betas[target]
        for lag in laggrid:
            phase=2*np.pi*d['freq'][donor]*(d['elapsed']-lag*3600)
            shifted=residualize(np.column_stack([np.cos(phase),np.sin(phase)])@betas[donor],Q)
            corr=float(shifted@targetwave/(np.linalg.norm(shifted)*np.linalg.norm(targetwave)))
            lagrows.append(dict(direction=direction,lag_hours=lag,normalized_template_correlation=corr))
        corrsubset=[r for r in lagrows if r['direction']==direction]
        detail['zero_lag_fitted_waveform_correlation']=next(r['normalized_template_correlation'] for r in corrsubset if r['lag_hours']==0)
        detail['max_abs_template_lag_correlation']=max(abs(r['normalized_template_correlation']) for r in corrsubset)
        donorwave=D@betas[donor]
        powers=[]; observed=[]; compensated=[]; donorbs=[]; databs=[]
        for f,Xf,If in zip(grid,bases,pinvs):
            bd=If@donorwave;b0=If@yr
            powers.append(gram_power(Xf,bd));observed.append(gram_power(Xf,b0));compensated.append(gram_power(Xf,b0-bd));donorbs.append(bd);databs.append(b0)
            spectra.append(dict(donor=donor,frequency_uHz=f*1e6,donor_density_1e35=6e-5*powers[-1],data_density_1e35=6e-5*observed[-1],compensated_density_1e35=6e-5*compensated[-1]))
        peaks=find_peaks(powers)[0]
        peaks=[i for i in peaks if abs(grid[i]-d['freq'][donor])>=2*rayleigh]
        candidates=sorted(peaks,key=lambda i:powers[i],reverse=True)[:3]
        detail['alias_candidates_uHz']=[float(grid[i]*1e6) for i in candidates]
        ax_alias[0,column].plot(grid*1e6,np.asarray(powers)*6e-5,label=f'Pure fitted {donor} injection')
        ax_alias[0,column].plot(grid*1e6,np.asarray(observed)*6e-5,color='0.5',alpha=.65,lw=.8,label='Observed')
        ax_alias[0,column].plot(grid*1e6,np.asarray(compensated)*6e-5,color='black',alpha=.65,lw=.8,label=f'Observed minus {donor}')
        for j,i in enumerate(candidates):
            Xf=bases[i]; b0=databs[i]; bd=donorbs[i]
            ax_alias[0,column].axvline(grid[i]*1e6,color=f'C{j+1}',alpha=.6,lw=.8)
            ps=[]
            for lam in lamgrid:
                actual=pinvs[i]@(yr-lam*donorwave)
                predicted=b0-lam*bd
                identities.append(np.max(np.abs(actual-predicted)))
                power=gram_power(Xf,actual);ps.append(power*6e-5)
                aliasrows.append(dict(direction=direction,candidate=j+1,frequency_uHz=grid[i]*1e6,lambda_=lam,
                                      data_deltaRSS=power,predicted_deltaRSS=gram_power(Xf,predicted),
                                      donor_only_deltaRSS=gram_power(Xf,bd),cos=actual[0],sin=actual[1]))
            ax_alias[1,column].plot(lamgrid,ps,label=f'{grid[i]*1e6:.4f} μHz',color=f'C{j+1}')
        ax_alias[0,column].set_title(f'{donor} sampling response')
        ax_alias[0,column].set_xlabel('Frequency (μHz)');ax_alias[1,column].set_xlabel('Compensation factor λ')
        for aa in ax_alias[:,column]:aa.set_ylim(bottom=0);aa.grid(alpha=.2);aa.legend(fontsize=7)
    axs[0,0].set_ylabel('Target amplitude ($10^{-18}$)')
    axs[1,0].set_ylabel('Phase φ (degrees)')
    axs[2,0].set_ylabel('Nominal 600 s LS density\n($10^{-35}$/μHz)')
    for aa in axs[0]:aa.set_ylim(bottom=0);aa.legend(fontsize=7)
    for aa in axs[2]:aa.set_ylim(bottom=0)
    for aa in ax_alias[:,0]:aa.set_ylabel('Nominal 600 s LS density\n($10^{-35}$/μHz)')
    for row in (0,2):
        ymax=max(aa.get_ylim()[1] for aa in axs[row])
        for aa in axs[row]:aa.set_ylim(0,ymax)
    for row in range(2):
        ymax=max(aa.get_ylim()[1] for aa in ax_alias[row])
        for aa in ax_alias[row]:aa.set_ylim(0,ymax)
    fig.suptitle('Auxiliary 600-s route: compensation sensitivity; N₂/K₂ controlled',fontsize=11)
    fig.tight_layout();fig_alias.tight_layout()
    for name,ff in [('compensation_sweep',fig),('alias_compensation',fig_alias)]:
        ff.savefig(OUT/f'{name}.pdf');ff.savefig(OUT/f'{name}.png',dpi=200);plt.close(ff)
    corr=normJ.T@normJ
    lagdf=pd.DataFrame(lagrows)
    ff,aa=plt.subplots(1,2,figsize=(10,3.7))
    im=aa[0].imshow(corr,vmin=-1,vmax=1,cmap='coolwarm');labels=['M₂ cos','M₂ sin','S₂ cos','S₂ sin']
    aa[0].set_xticks(range(4),labels,rotation=30);aa[0].set_yticks(range(4),labels)
    for i in range(4):
        for j in range(4):aa[0].text(j,i,f'{corr[i,j]:.3f}',ha='center',va='center',fontsize=9)
    ff.colorbar(im,ax=aa[0],shrink=.7);aa[0].set_title('Projected basis correlation')
    for name,sub in lagdf.groupby('direction'):aa[1].plot(sub.lag_hours,sub.normalized_template_correlation,label=name.replace('_',' '))
    aa[1].set(xlabel='Donor template lag (h)',ylabel='Normalized template correlation',ylim=(-1,1),title='Actual-sampling template lag correlation')
    aa[1].axhline(0,color='0.7',lw=.7);aa[1].legend(fontsize=8);aa[1].grid(alpha=.2)
    ff.tight_layout();ff.savefig(OUT/'coupling_geometry.pdf');ff.savefig(OUT/'coupling_geometry.png',dpi=200);plt.close(ff)
    pd.DataFrame(sweep).to_csv(OUT/'compensation_sweep.csv',index=False)
    pd.DataFrame(aliasrows).to_csv(OUT/'alias_compensation.csv',index=False)
    pd.DataFrame(spectra).to_csv(OUT/'single_injection_spectra.csv',index=False)
    lagdf.to_csv(OUT/'template_lag_correlations.csv',index=False)
    pd.DataFrame(corr,index=labels,columns=labels).to_csv(OUT/'projected_basis_correlations.csv')
    summary['max_absolute_identity_error']=float(max(identities))
    assert max(identities)<1e-10
    summary['environment']=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,pandas=pd.__version__,matplotlib=matplotlib.__version__)
    summary['inputs']=json.loads((OUT.parent/'v86_auxiliary/input_manifest.json').read_text())
    summary['implementation_sha256']=sha(Path(__file__))
    summary['loader_sha256']=sha(OUT.parent/'v86_auxiliary/loader.py')
    summary['uncertainty']='Deterministic conditional diagnostics; no confidence intervals or detection probabilities calculated.'
    (OUT/'results.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps({k:v for k,v in summary.items() if k not in ('inputs','environment')},indent=2))

if __name__=='__main__':main()
