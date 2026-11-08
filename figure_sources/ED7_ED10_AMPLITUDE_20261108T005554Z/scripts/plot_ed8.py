"""Plot stored compensation coefficients as amplitude and phase; no new fitting."""
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from plot_config import ROOT, FIGURES, CM_PER_1E18, HEIGHT_LABEL, PHASE_LABEL, COMPENSATION_LABEL

def main():
    plt.rcParams.update({'font.size':10,'svg.fonttype':'none','pdf.fonttype':42})
    tab=pd.read_csv(ROOT/'data/frozen_coupling/compensation_sweep.csv')
    np.testing.assert_allclose(np.hypot(tab.cos,tab.sin),tab.amplitude_1e18,rtol=2e-13,atol=2e-13)
    tab['amplitude_cm']=np.hypot(tab.cos,tab.sin)*CM_PER_1E18
    output=ROOT/'data/amplitude';output.mkdir(exist_ok=True)
    tab.to_csv(output/'ed8_compensation_amplitude.csv',index=False)
    fig,axs=plt.subplots(2,2,figsize=(10,6.8),sharex=True,layout='constrained')
    checked=0
    for col,(direction,donor,target) in enumerate([('M2_to_S2','M₂','S₂'),('S2_to_M2','S₂','M₂')]):
        sub=tab[tab.direction.eq(direction)]
        for origin,fit,style,color,label in [('joint','target_only','-','C0','Joint-fit donor'),('single','target_only',':','C1','Single-frequency donor'),('joint','joint_controlled','--','0.4','Donor also controlled')]:
            z=sub[sub.donor_waveform.eq(origin)&sub['fit'].eq(fit)]
            values=[z.amplitude_cm,np.degrees(np.unwrap(np.radians(z.phase_deg))) if fit=='target_only' else z.phase_deg]
            for row,y in enumerate(values):
                ln=axs[row,col].plot(z.lambda_,y,style,color=color,label=label)[0]
                np.testing.assert_array_equal(ln.get_ydata(),np.asarray(y));checked+=1
        axs[0,col].set_title(f'Subtract {donor}; re-estimate {target}')
        axs[0,col].legend(fontsize=8)
        axs[1,col].set_xlabel(COMPENSATION_LABEL)
    for i,ax in enumerate(axs.flat):
        ax.axvline(1,color='.7',lw=.8);ax.grid(alpha=.2)
        ax.text(-.12,1.04,'abcd'[i],transform=ax.transAxes,fontweight='bold')
    axs[0,0].set_ylabel(HEIGHT_LABEL);axs[1,0].set_ylabel(PHASE_LABEL)
    ymax=max(ax.get_ylim()[1] for ax in axs[0])
    for ax in axs[0]:ax.set_ylim(0,ymax)
    fig.suptitle('Reciprocal compensation: amplitude and phase',fontsize=12)
    for ext in ['pdf','png','svg']:fig.savefig(FIGURES/f'ED_Figure_8.{ext}',dpi=200)
    plt.close(fig)
    report={'checked_curves':checked,'rows':len(tab),'amplitude_definition':'hypot(cos,sin) * 100 c^2 / g0 * 1e-18; cm','scope':'Frozen coefficients, no refit. Former density panels removed; 2x2 amplitude/phase display.'}
    (output/'ED8_VALIDATION.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report))

if __name__=='__main__':main()
