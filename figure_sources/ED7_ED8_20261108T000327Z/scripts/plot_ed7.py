"""Plot frozen derived curves only; no observations fitted or spectra calculated."""
from pathlib import Path
import json,hashlib,platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data';OUT=ROOT/'reproduced';OUT.mkdir(exist_ok=True)
matplotlib.rcParams['svg.fonttype']='none'  # Preserve text nodes for editing.
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check_inputs(names):
    records={x['file']:x for x in json.loads((DATA/'INPUT_MANIFEST.json').read_text())}
    for name in names:assert sha(DATA/name)==records[name]['sha256'],name
    return {name:sha(DATA/name) for name in names}
def assert_curve(ax,index,x,y,source,checks):
    line=ax.lines[index]
    np.testing.assert_array_equal(np.asarray(line.get_xdata()),np.asarray(x))
    np.testing.assert_array_equal(np.asarray(line.get_ydata()),np.asarray(y))
    checks.append({'source':source,'points':len(np.asarray(x)),'x_exact':True,'y_exact':True})
def finish(fig,name,dpi,hashes,row_counts,checks):
    arrays={};axes=[]
    for i,ax in enumerate(fig.axes):
        lines=[]
        for j,line in enumerate(ax.lines):
            arrays[f'axis{i}_line{j}_x']=np.asarray(line.get_xdata())
            arrays[f'axis{i}_line{j}_y']=np.asarray(line.get_ydata())
            lines.append({'line':j,'label':line.get_label(),'points':len(line.get_xdata())})
        axes.append({'index':i,'title':ax.get_title(loc='left') or ax.get_title(),'xlabel':ax.get_xlabel(),'ylabel':ax.get_ylabel(),'xlim':list(ax.get_xlim()),'ylim':list(ax.get_ylim()),'yscale':ax.get_yscale(),'lines':lines})
    for ext in ['pdf','png','svg']:fig.savefig(OUT/f'{name}.{ext}',dpi=dpi)
    np.savez_compressed(OUT/f'{name}_plotted_arrays.npz',**arrays)
    svg=(OUT/f'{name}.svg').read_text();assert '<text' in svg
    report={'status':'PASS','action':'Frozen-data plotting only; no refit, rescan, resampling or new observations.','input_sha256':hashes,'row_counts':row_counts,'curve_array_checks':checks,'axes':axes,'svg_text_nodes':svg.count('<text'),'software':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'matplotlib':matplotlib.__version__},'script_sha256':sha(Path(__file__)),'outputs_sha256':{p.name:sha(p) for p in [OUT/f'{name}.{e}' for e in ['pdf','png','svg']]+[OUT/f'{name}_plotted_arrays.npz']}}
    (OUT/f'{name}_VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    plt.close(fig)
    print(json.dumps({'figure':name,'status':'PASS','row_counts':row_counts,'checked_data_curves':len(checks),'svg_text_nodes':report['svg_text_nodes']}))

hashes=check_inputs(['spectra.csv','conditional.csv','NUMERIC_RESULTS.json'])
tab=pd.read_csv(DATA/'spectra.csv');cf=pd.read_csv(DATA/'conditional.csv');result=json.loads((DATA/'NUMERIC_RESULTS.json').read_text())
frequency=tab.frequency_uHz.to_numpy();fm=result['frequency_Hz']
cols=['observed_N2K2_controlled','minus_M2','minus_S2','minus_both','M2_only_fitted_phase','S2_only_fitted_phase','M2_plus_S2_model']
density=tab[[s+'_density_1e35_per_uHz' for s in cols]].to_numpy()
assert np.all(np.isfinite(density)) and np.all(np.diff(frequency)>0)
plt.rcParams.update({'font.size':8,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,axs=plt.subplots(2,2,figsize=(9,6.8),sharex=True,sharey=True,constrained_layout=True)
c=['#2166ac','#d95f02','#1b9e77','#555555']
ax=axs[0,0];ax.plot(frequency,tab.original_observed_density_1e35_per_uHz.to_numpy(),color=c[0],lw=1,label='Observed')
ax.plot(frequency,tab.original_after_unit_prediction_density_1e35_per_uHz,color=c[1],lw=.9,label='After unit physical prediction')
ax.set_title('a  Existing spectral route, reproduced',loc='left')
ax=axs[0,1]
for i,label in enumerate(['Observed, N₂/K₂ controlled','Subtract fitted M₂','Subtract fitted S₂','Subtract both']):
    ax.plot(frequency,density[:,i],color=c[i],lw=1 if i==0 else .8,ls=['-','--','-.',':'][i],label=label)
ax.set_title('b  Single-component subtraction',loc='left')
ax=axs[1,0];ax.plot(frequency,density[:,0],color='.65',lw=.8,label='N₂/K₂ controlled baseline')
for target,color in [('M2',c[0]),('S2',c[1])]:
    z=cf[cf.target==target];ax.plot(z.frequency_uHz,z.density_1e35_per_uHz,color=color,lw=1.3,label=target+' conditional on '+('S₂' if target=='M2' else 'M₂'))
ax.set_title('c  Conditional frequency scans',loc='left')
ax=axs[1,1];ax.plot(frequency,density[:,0],color='.65',lw=.8,label='Observed, N₂/K₂ controlled')
for i,label,col in [(4,'M₂-only fitted-phase injection',c[0]),(5,'S₂-only fitted-phase injection',c[1]),(6,'Joint M₂ + S₂ waveform',c[2])]:
    ax.plot(frequency,density[:,i],color=col,lw=.9,ls='--' if i<6 else '-',label=label)
ax.set_title('d  Actual-window response and sidelobes',loc='left')
ymax=max(float(tab.original_observed_density_1e35_per_uHz.max()),float(density.max()),float(cf.density_1e35_per_uHz.max()),float(tab.original_after_unit_prediction_density_1e35_per_uHz.max()))*1.36
for ax in axs.flat:
    for name in ['N2','M2','S2','K2']:ax.axvline(fm[name]*1e6,color='.75',lw=.5,ls=':')
    ax.set_xlim(21,24.5);ax.set_ylim(0,ymax);ax.set_yscale('linear');ax.legend(loc='upper left',fontsize=6.8,frameon=False)
for ax in axs[1]:ax.set_xlabel('Frequency (µHz)')
for ax in axs[:,0]:ax.set_ylabel('Nominal 600 s LS density\n(10⁻³⁵ fractional-frequency²/µHz)')
fig.suptitle('Auxiliary 600 s non-overlapping route · 3,299 rows · 54 segment constants',fontsize=11)

checks=[]
for k,col in enumerate(['original_observed_density_1e35_per_uHz','original_after_unit_prediction_density_1e35_per_uHz']):assert_curve(axs[0,0],k,frequency,tab[col].to_numpy(),col,checks)
for k in range(4):assert_curve(axs[0,1],k,frequency,density[:,k],cols[k],checks)
assert_curve(axs[1,0],0,frequency,density[:,0],cols[0],checks)
for k,target in enumerate(['M2','S2'],1):
    z=cf[cf.target==target];assert_curve(axs[1,0],k,z.frequency_uHz.to_numpy(),z.density_1e35_per_uHz.to_numpy(),'conditional '+target,checks)
assert_curve(axs[1,1],0,frequency,density[:,0],cols[0],checks)
for k,col in enumerate([4,5,6],1):assert_curve(axs[1,1],k,frequency,density[:,col],cols[col],checks)
finish(fig,'ED_Figure_7',190,hashes,{'spectra':len(tab),'conditional':len(cf),'conditional_by_target':{str(k):int(v) for k,v in cf.groupby('target').size().items()}},checks)
