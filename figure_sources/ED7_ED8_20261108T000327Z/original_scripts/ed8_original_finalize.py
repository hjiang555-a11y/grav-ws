"""Finalize displays and derive candidate minima from existing deterministic CSVs."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
def label(ax,letter):ax.text(-.12,1.05,letter,transform=ax.transAxes,fontweight='bold',fontsize=12)
def save(fig,name):
    fig.tight_layout();fig.savefig(ROOT/f'{name}.pdf');fig.savefig(ROOT/f'{name}.png',dpi=200);plt.close(fig)
def main():
    sweep=pd.read_csv(ROOT/'compensation_sweep.csv');alias=pd.read_csv(ROOT/'alias_compensation.csv')
    spectra=pd.read_csv(ROOT/'single_injection_spectra.csv');lags=pd.read_csv(ROOT/'template_lag_correlations.csv')
    directions=['M2_to_S2','S2_to_M2']; names=[('M₂','S₂'),('S₂','M₂')]
    fig,axs=plt.subplots(3,2,figsize=(10,9),sharex=True)
    for c,(direction,(donor,target)) in enumerate(zip(directions,names)):
        ss=sweep[sweep.direction.eq(direction)]
        for origin,ls in [('joint','-'),('single',':')]:
            s=ss[ss.donor_waveform.eq(origin)&ss['fit'].eq('target_only')]
            for r,v in enumerate([s.amplitude_1e18,np.degrees(np.unwrap(np.radians(s.phase_deg))),s.density_1e35_per_uHz]):
                axs[r,c].plot(s.lambda_,v,ls,label=f'{origin}-fit donor')
        s=ss[ss.donor_waveform.eq('joint')&ss['fit'].eq('joint_controlled')]
        for r,v in enumerate([s.amplitude_1e18,s.phase_deg,s.density_1e35_per_uHz]):
            axs[r,c].plot(s.lambda_,v,'--',color='0.4',label='joint-controlled identity')
            axs[r,c].axvline(1,color='.8',lw=.8);axs[r,c].grid(alpha=.2);label(axs[r,c],'abcdef'[r*2+c])
        axs[0,c].set_title(f'Subtract {donor}; re-estimate {target}');axs[2,c].set_xlabel('Compensation factor λ')
        axs[0,c].legend(fontsize=7)
    axs[0,0].set_ylabel('Target amplitude ($10^{-18}$)');axs[1,0].set_ylabel('Phase φ (degrees)')
    axs[2,0].set_ylabel('Nominal 600 s LS density\n($10^{-35}$/μHz)')
    for r in (0,2):
        ymax=max(a.get_ylim()[1] for a in axs[r])
        for a in axs[r]:a.set_ylim(0,ymax)
    fig.suptitle('Auxiliary 600-s route: compensation sensitivity; N₂/K₂ controlled',fontsize=11)
    save(fig,'compensation_sweep')
    fig,axs=plt.subplots(2,2,figsize=(11,6.4));minima=[]
    for c,(direction,(donor,target)) in enumerate(zip(directions,names)):
        ss=spectra[spectra.donor.eq(['M2','S2'][c])]
        axs[0,c].plot(ss.frequency_uHz,ss.donor_density_1e35,label=f'Pure fitted {donor} injection')
        axs[0,c].plot(ss.frequency_uHz,ss.data_density_1e35,color='.5',alpha=.7,lw=.8,label='Observed')
        axs[0,c].plot(ss.frequency_uHz,ss.compensated_density_1e35,color='black',alpha=.7,lw=.8,label=f'Observed minus {donor}')
        for j,(candidate,sub) in enumerate(alias[alias.direction.eq(direction)].groupby('candidate')):
            freq=float(sub.frequency_uHz.iloc[0]);p0=float(sub.loc[sub.lambda_.eq(0),'data_deltaRSS'].iloc[0]);p1=float(sub.loc[sub.lambda_.eq(1),'data_deltaRSS'].iloc[0])
            a=float(sub.donor_only_deltaRSS.iloc[0]);b=p1-p0-a;lam=-b/(2*a);clipped=np.clip(lam,0,1.5)
            scan=sub.loc[sub.data_deltaRSS.idxmin()]
            minima.append(dict(direction=direction,candidate=int(candidate),frequency_uHz=freq,
                               deltaRSS_lambda0=p0,deltaRSS_lambda1=p1,remaining_fraction_lambda1=p1/p0,
                               analytic_unrestricted_min_lambda=lam,analytic_min_deltaRSS=p0+b*lam+a*lam**2,
                               analytic_in_sweep_min_lambda=clipped,analytic_in_sweep_min_deltaRSS=p0+b*clipped+a*clipped**2,
                               grid_min_lambda=float(scan.lambda_),grid_min_deltaRSS=float(scan.data_deltaRSS),
                               donor_only_deltaRSS=a,linear_cross_term=b))
            axs[0,c].axvline(freq,color=f'C{j+1}',alpha=.6,lw=.8)
            axs[1,c].plot(sub.lambda_,sub.data_deltaRSS*6e-5,label=f'{freq:.4f} μHz',color=f'C{j+1}')
        axs[0,c].set_title(f'{donor} injection and observed spectra');axs[1,c].set_title(f'Observed after scaled {donor} subtraction')
        axs[0,c].set_xlabel('Frequency (μHz)');axs[1,c].set_xlabel('Compensation factor λ')
        axs[1,c].axvline(1,color='.7',lw=.8)
        for r in range(2):axs[r,c].grid(alpha=.2);axs[r,c].legend(fontsize=7);label(axs[r,c],'abcd'[r*2+c])
    for r in range(2):
        ymax=max(a.get_ylim()[1] for a in axs[r])
        for a in axs[r]:a.set_ylim(0,ymax)
        axs[r,0].set_ylabel('Nominal 600 s LS density\n($10^{-35}$/μHz)')
    save(fig,'alias_compensation')
    corr=pd.read_csv(ROOT/'projected_basis_correlations.csv',index_col=0)
    fig,axs=plt.subplots(1,2,figsize=(10,3.8));im=axs[0].imshow(corr,vmin=-1,vmax=1,cmap='coolwarm')
    axs[0].set_xticks(range(4),corr.columns,rotation=30);axs[0].set_yticks(range(4),corr.index)
    for i in range(4):
        for j in range(4):axs[0].text(j,i,f'{corr.iloc[i,j]:.3f}',ha='center',va='center',fontsize=9)
    fig.colorbar(im,ax=axs[0],shrink=.7);axs[0].set_title('Projected basis correlation')
    for direction,(donor,target) in zip(directions,names):
        s=lags[lags.direction.eq(direction)];axs[1].plot(s.lag_hours,s.normalized_template_correlation,label=f'Shifted {donor} versus {target}')
    axs[1].set(xlabel='Donor template lag (h)',ylabel='Normalized template correlation',ylim=(-1,1),title='Actual-sampling template lag correlation')
    axs[1].axhline(0,color='.7',lw=.7);axs[1].grid(alpha=.2);axs[1].legend(fontsize=8)
    for a,l in zip(axs,'ab'):label(a,l)
    save(fig,'coupling_geometry')
    m=pd.DataFrame(minima);m.to_csv(ROOT/'alias_candidate_minima.csv',index=False)
    (ROOT/'alias_candidate_minima.json').write_text(json.dumps(minima,indent=2))
    r=json.loads((ROOT/'results.json').read_text());r['alias_candidate_minima']=minima
    r['figure_finalization_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'results.json').write_text(json.dumps(r,indent=2))
    print(m.to_string(index=False))
if __name__=='__main__':main()
