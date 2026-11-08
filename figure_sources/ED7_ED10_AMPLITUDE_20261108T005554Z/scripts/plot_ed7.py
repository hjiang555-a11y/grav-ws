"""ED7 scalar amplitude spectra from saved sine/cosine fits; plot only."""
from pathlib import Path
import json,hashlib,platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from plot_config import ROOT,FIGURES,HEIGHT_LABEL,FREQUENCY_LABEL,RAYLEIGH_UHZ,GRID_UHZ
DATA=ROOT/'data/amplitude'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    tab=pd.read_csv(DATA/'ed7_spectra.csv');cf=pd.read_csv(DATA/'ed7_conditional.csv')
    meta=json.loads((ROOT/'data/frozen_auxiliary/results/NUMERIC_RESULTS.json').read_text());freq=tab.frequency_uHz.to_numpy();fm=meta['frequency_Hz']
    names=['observed_N2K2_controlled','minus_M2','minus_S2','minus_both','M2_only_fitted_phase','S2_only_fitted_phase','M2_plus_S2_model']
    amp=tab[[name+'_amplitude_cm' for name in names]].to_numpy()
    matplotlib.rcParams.update({'font.size':8,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'svg.fonttype':'none'})
    fig=plt.figure(figsize=(10,9.5));axs=np.empty((2,2),dtype=object)
    for r,y0 in enumerate([.68,.24]):
        for c,x0 in enumerate([.09,.56]):axs[r,c]=fig.add_axes([x0,y0,.39,.21])
    colors=['#2166ac','#d95f02','#1b9e77','#555555']
    ax=axs[0,0];ax.plot(freq,tab.original_observed_amplitude_cm,color=colors[0],lw=1,label='Observed')
    ax.plot(freq,tab.original_after_unit_prediction_amplitude_cm,color=colors[1],lw=.9,label='After unit physical prediction')
    ax.set_title('a  Observed and tide-subtracted spectra',loc='left')
    ax=axs[0,1]
    for i,label in enumerate(['Observed, N₂/K₂ controlled','Subtract fitted M₂','Subtract fitted S₂','Subtract both']):
        ax.plot(freq,amp[:,i],color=colors[i],lw=1 if i==0 else .8,ls=['-','--','-.',':'][i],label=label)
    ax.set_title('b  Single-component subtraction',loc='left')
    ax=axs[1,0];ax.plot(freq,amp[:,0],color='.65',lw=.8,label='N₂/K₂ controlled baseline')
    for target,color in [('M2',colors[0]),('S2',colors[1])]:
        z=cf[cf.target.eq(target)];ax.plot(z.frequency_uHz,z.amplitude_cm,color=color,lw=1.3,label=target+' conditional on '+('S₂' if target=='M2' else 'M₂'))
    ax.set_title('c  Conditional frequency scans',loc='left')
    ax=axs[1,1];ax.plot(freq,amp[:,0],color='.65',lw=.8,label='Observed, N₂/K₂ controlled')
    for i,label,color in [(4,'M₂-only fitted-phase injection',colors[0]),(5,'S₂-only fitted-phase injection',colors[1]),(6,'Joint M₂ + S₂ waveform',colors[2])]:
        ax.plot(freq,amp[:,i],color=color,lw=.9,ls='--' if i<6 else '-',label=label)
    ax.set_title('d  Actual-window response and sidelobes',loc='left')
    ymax=1.36*max(float(tab.original_observed_amplitude_cm.max()),float(tab.original_after_unit_prediction_amplitude_cm.max()),float(np.nanmax(amp)),float(cf.amplitude_cm.max()))
    for ax in axs.flat:
        for name in ['N2','M2','S2','K2']:ax.axvline(fm[name]*1e6,color='.75',lw=.5,ls=':')
        ax.set_xlim(21,24.5);ax.set_ylim(0,ymax);ax.set_yscale('linear');ax.legend(loc='upper left',fontsize=6.8,frameon=False)
    for ax in axs[1]:ax.set_xlabel(FREQUENCY_LABEL)
    for ax in axs[:,0]:ax.set_ylabel(HEIGHT_LABEL)
    fig.suptitle('Auxiliary 600 s non-overlapping route · 3,299 rows · 54 segment constants',fontsize=11)
    fig.text(.5,.035,f'Rayleigh scale 1/Tspan = {RAYLEIGH_UHZ:.5f} µHz; base grid step = {GRID_UHZ:.6f} µHz',ha='center',fontsize=8)
    fig.text(.5,.015,'N₂ and K₂ are nuisance frequencies in b–d; their exact coincident scan amplitudes are undefined.',ha='center',fontsize=8)
    zooms=[]
    for i,ax in enumerate(axs.flat):
        zoom=ax.inset_axes([0,-.62,1,.43])
        for line in ax.lines:
            zoom.plot(line.get_xdata(),line.get_ydata(),color=line.get_color(),lw=line.get_linewidth(),ls=line.get_linestyle())
        zoom.set(xlim=ax.get_xlim(),ylim=(0,6),xlabel=FREQUENCY_LABEL,ylabel='cm')
        zoom.set_title('Zoom: 0–6 cm',loc='left',fontsize=7,pad=3)
        zoom.tick_params(labelsize=7);zoom.xaxis.label.set_size(7);zoom.yaxis.label.set_size(7)
        zoom.set_yticks([0,3,6]);zooms.append(zoom)
        ax.set_xlabel('')
        if i>0:
            for key in ['N2','K2']:
                ax.text(fm[key]*1e6,.31,('N₂' if key=='N2' else 'K₂')+' nuisance',transform=ax.get_xaxis_transform(),rotation=90,fontsize=6,color='.4',ha='right',va='center')
    # Save the actual plotted arrays and test every data curve, independent of PDF metadata.
    expected=[[tab.original_observed_amplitude_cm.to_numpy(),tab.original_after_unit_prediction_amplitude_cm.to_numpy()], [amp[:,i] for i in range(4)], [amp[:,0]]+[cf[cf.target.eq(k)].amplitude_cm.to_numpy() for k in ['M2','S2']], [amp[:,0]]+[amp[:,i] for i in [4,5,6]]]
    arrays={};axes=[]
    for i,ax in enumerate(axs.flat):
        for j,y in enumerate(expected[i]):np.testing.assert_array_equal(ax.lines[j].get_ydata(),y)
        for j,line in enumerate(ax.lines):arrays[f'axis{i}_line{j}_x']=line.get_xdata();arrays[f'axis{i}_line{j}_y']=line.get_ydata()
        axes.append({'panel':'abcd'[i],'ylim':list(ax.get_ylim()),'xlim':list(ax.get_xlim()),'yscale':ax.get_yscale(),'data_curves':len(expected[i]),'ylabel':ax.get_ylabel()})
    np.savez_compressed(DATA/'ed7_plotted_arrays.npz',**arrays)
    for ext in ['pdf','png','svg']:fig.savefig(FIGURES/f'ED_Figure_7.{ext}',dpi=300)
    plt.close(fig)
    report={'status':'PASS','scope':'Plot saved scalar pair amplitudes in cm, no rescan or fits in this plotting script.','checked_data_curves':13,'display':'All identifiable scan values retained in full-range main axes; separate labelled 0–6 cm zoom insets below each panel. Exact nuisance rows retained with NaN/status.','axes':axes,'input_sha256':{p.name:sha(p) for p in [DATA/'ed7_spectra.csv',DATA/'ed7_conditional.csv',ROOT/'data/frozen_auxiliary/results/NUMERIC_RESULTS.json']},'script_sha256':sha(Path(__file__)),'software':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'matplotlib':matplotlib.__version__},'outputs_sha256':{p.name:sha(p) for p in [FIGURES/f'ED_Figure_7.{e}' for e in ['pdf','png','svg']]}}
    (DATA/'ED7_PLOT_VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({'figure':'ED7','status':'PASS','checked_data_curves':13,'shared_amplitude_ylim_cm':[0,ymax]}))
if __name__=='__main__':main()
