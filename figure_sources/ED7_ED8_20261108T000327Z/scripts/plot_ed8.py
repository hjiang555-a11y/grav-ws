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

hashes=check_inputs(['compensation_sweep.csv'])
sweep=pd.read_csv(DATA/'compensation_sweep.csv')
directions=['M2_to_S2','S2_to_M2'];names=[('M₂','S₂'),('S₂','M₂')]
def label(ax,letter):ax.text(-.12,1.05,letter,transform=ax.transAxes,fontweight='bold',fontsize=12)
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

checks=[]
for c,direction in enumerate(directions):
    ss=sweep[sweep.direction.eq(direction)]
    for k,origin in enumerate(['joint','single']):
        z=ss[ss.donor_waveform.eq(origin)&ss['fit'].eq('target_only')]
        for r,y in enumerate([z.amplitude_1e18,np.degrees(np.unwrap(np.radians(z.phase_deg))),z.density_1e35_per_uHz]):assert_curve(axs[r,c],k,z.lambda_.to_numpy(),np.asarray(y),direction+' '+origin+' target_only '+str(r),checks)
    z=ss[ss.donor_waveform.eq('joint')&ss['fit'].eq('joint_controlled')]
    for r,y in enumerate([z.amplitude_1e18,z.phase_deg,z.density_1e35_per_uHz]):assert_curve(axs[r,c],2,z.lambda_.to_numpy(),np.asarray(y),direction+' joint_controlled '+str(r),checks)
fig.tight_layout()
finish(fig,'ED_Figure_8',200,hashes,{'compensation_sweep':len(sweep),'lambda_values':int(sweep.lambda_.nunique()),'by_direction_waveform_fit':{'|'.join(map(str,k)):int(v) for k,v in sweep.groupby(['direction','donor_waveform','fit']).size().items()}},checks)
