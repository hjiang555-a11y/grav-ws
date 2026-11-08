"""Display previously computed covariance; no observations, fits or null tests run."""
from pathlib import Path
import json, hashlib, platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'v86_auxiliary/results/NUMERIC_RESULTS.json'

def main():
    results=json.loads(SOURCE.read_text())
    order=['M2_cos','M2_sin','S2_cos','S2_sin']
    assert results['joint_order']==order
    labels=['M₂ cos','M₂ sin','S₂ cos','S₂ sin']
    basis=pd.read_csv(ROOT/'projected_basis_correlations.csv',index_col=0).to_numpy()
    lags=pd.read_csv(ROOT/'template_lag_correlations.csv')
    matrices={};checks={}
    for name,key in [('scaled_LS','joint_scaled_LS_covariance_e36'),('UTC_day_jackknife','joint_UTC_day_jackknife_covariance_e36')]:
        C=np.asarray(results[key],dtype=float)
        assert C.shape==(4,4) and np.all(np.diag(C)>0)
        np.testing.assert_allclose(C,C.T,rtol=0,atol=1e-12)
        scale=np.sqrt(np.diag(C));R=C/np.outer(scale,scale)
        np.testing.assert_allclose(np.diag(R),1,rtol=0,atol=1e-12)
        assert np.max(np.abs(R))<=1+1e-12
        matrices[name]=R
        checks[name]={'min_eigenvalue':float(np.linalg.eigvalsh(R).min()),'correlation':R.tolist()}
        pd.DataFrame(R,index=order,columns=order).to_csv(ROOT/f'joint_coefficient_correlation_{name}.csv')
    fig,axs=plt.subplots(2,2,figsize=(10,8),constrained_layout=True)
    for ax,R,title in [(axs[0,0],basis,'Projected design-basis correlation'),
                        (axs[1,0],matrices['scaled_LS'],'Joint coefficients: scaled least squares'),
                        (axs[1,1],matrices['UTC_day_jackknife'],'Joint coefficients: UTC-day jackknife')]:
        im=ax.imshow(R,vmin=-1,vmax=1,cmap='coolwarm')
        ax.set_xticks(range(4),labels,rotation=25);ax.set_yticks(range(4),labels)
        ax.set_title(title,fontsize=11)
        for i in range(4):
            for j in range(4):ax.text(j,i,f'{R[i,j]:.3f}',ha='center',va='center',fontsize=10,
                                      color='white' if abs(R[i,j])>.7 else 'black')
    ax=axs[0,1]
    for name,label in [('M2_to_S2','Shifted M₂ versus S₂'),('S2_to_M2','Shifted S₂ versus M₂')]:
        s=lags[lags.direction.eq(name)]
        ax.plot(s.lag_hours,s.normalized_template_correlation,label=label)
    ax.set(xlabel='Donor template lag (h)',ylabel='Normalized template correlation',ylim=(-1,1),
           title='Fitted-template lag correlation')
    ax.axhline(0,color='.7',lw=.8);ax.grid(alpha=.2);ax.legend(fontsize=9,loc='lower left')
    for ax,letter in zip(axs.ravel(),'abcd'):
        ax.text(-.13,1.06,letter,transform=ax.transAxes,fontweight='bold',fontsize=13)
    fig.colorbar(im,ax=[axs[0,0],axs[1,0],axs[1,1]],label='Correlation coefficient',shrink=.7,pad=.025)
    fig.savefig(ROOT/'coupling_geometry_joint.pdf')
    fig.savefig(ROOT/'coupling_geometry_joint.png',dpi=220)
    plt.close(fig)
    manifest={'action':'Deterministic normalization of existing covariances; no fitting or new significance tests.',
              'coefficient_order':order,'source_relative':'../v86_auxiliary/results/NUMERIC_RESULTS.json',
              'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'n_rows':results['n_rows'],'n_segments':results['n_segments'],'n_UTC_days':results['n_days'],
              'correlations':checks,'software':{'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'matplotlib':matplotlib.__version__}}
    (ROOT/'joint_correlation_manifest.json').write_text(json.dumps(manifest,indent=2))
    print(json.dumps(checks,indent=2))

if __name__=='__main__':main()
