#!/usr/bin/env python3
"""Draw ED10 in equivalent-height sinusoidal peak amplitude (cm).

Top panels read scan cosine/sine amplitudes reconstructed from frozen inputs by
recompute_amplitude.py. Bottom panels use the original stored alias-sweep
cosine and sine coefficients, in units of 1e-18. Nothing is converted by merely
relabeling a density axis. Original power-selected candidate frequencies are
retained exactly; they are not reselected as amplitude-spectrum maxima.
"""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from plot_config import (ROOT, FIGURES, CM_PER_1E18, HEIGHT_LABEL,
                         FREQUENCY_LABEL, COMPENSATION_LABEL)

SCAN = ROOT/'data/amplitude/ed10_single_injection_spectra.csv'
ALIAS = ROOT/'data/frozen_coupling/alias_compensation.csv'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=FIGURES)
    out = parser.parse_args().output
    out.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9,
                         'pdf.fonttype': 42, 'ps.fonttype': 42,
                         'svg.fonttype': 'none'})
    spectra = pd.read_csv(SCAN)
    alias = pd.read_csv(ALIAS)
    for column in ['donor', 'frequency_uHz', 'donor_amplitude_cm',
                   'data_amplitude_cm', 'compensated_amplitude_cm']:
        assert column in spectra.columns, f'Missing scan field {column}'
    assert set(spectra.donor.unique()) == {'M2','S2'}
    alias = alias.copy()
    alias['amplitude_cm'] = np.hypot(alias['cos'], alias['sin'])*CM_PER_1E18
    assert np.isfinite(alias.amplitude_cm).all()
    # The zoom insets occupy reserved space below their full-range parents;
    # they do not cover the large coefficients near the nuisance frequencies.
    fig = plt.figure(figsize=(11, 9.5))
    grid = fig.add_gridspec(2, 2, height_ratios=[2.2, 1], hspace=.31,
                           left=.10, right=.98, top=.94, bottom=.07, wspace=.22)
    axs = np.empty((2,2), dtype=object)
    zooms = []
    for col in range(2):
        container = fig.add_subplot(grid[0,col])
        container.set_axis_off()
        axs[0,col] = container.inset_axes([0,.59,1,.41])
        zooms.append(container.inset_axes([0,0,1,.41]))
        axs[1,col] = fig.add_subplot(grid[1,col])
    nuisance_source = ROOT/'data/frozen_coupling/results.json'
    frequencies = json.loads(nuisance_source.read_text())['frequency_Hz']
    directions = ['M2_to_S2','S2_to_M2']
    plotted = {}; candidates = []; rowmax = [0.,0.]
    for col, (direction, donor, pretty) in enumerate(zip(directions, ['M2','S2'], ['M₂','S₂'])):
        scan = spectra[spectra.donor.eq(donor)]
        frequency = scan.frequency_uHz.to_numpy()
        assert np.all(np.diff(frequency)>0)
        plotted[donor+'_frequency_uHz'] = frequency
        styles = [('donor_amplitude_cm', f'Pure fitted {pretty} injection', 'C0', 1., 1.),
                  ('data_amplitude_cm', 'Observed', '.5', .75, .8),
                  ('compensated_amplitude_cm', f'Observed minus {pretty}', 'black', .75, .8)]
        for column, label, color, alpha, lw in styles:
            values = scan[column].to_numpy()
            assert np.isfinite(values).all() and np.min(values)>=0
            axs[0,col].plot(frequency, values, color=color, alpha=alpha, lw=lw, label=label)
            zooms[col].plot(frequency, values, color=color, alpha=alpha, lw=lw)
            plotted[donor+'_'+column] = values
            rowmax[0] = max(rowmax[0], float(values.max()))
        for j,(candidate, sub) in enumerate(alias[alias.direction.eq(direction)].groupby('candidate', sort=True)):
            assert sub.frequency_uHz.nunique()==1
            frequency_value = float(sub.frequency_uHz.iloc[0])
            color = f'C{j+1}'
            axs[0,col].axvline(frequency_value, color=color, alpha=.6, lw=.8)
            zooms[col].axvline(frequency_value, color=color, alpha=.6, lw=.8)
            axs[1,col].plot(sub.lambda_, sub.amplitude_cm, label=f'{frequency_value:.4f} µHz', color=color)
            rowmax[1] = max(rowmax[1], float(sub.amplitude_cm.max()))
            key = f'{donor}_candidate_{int(candidate)}'
            plotted[key+'_lambda'] = sub.lambda_.to_numpy()
            plotted[key+'_amplitude_cm'] = sub.amplitude_cm.to_numpy()
            candidates.append({'direction': direction, 'candidate': int(candidate),
                               'frequency_uHz': frequency_value, 'rows': len(sub),
                               'selection': 'Retained historical power-spectrum candidate; not reselected by amplitude'})
        axs[0,col].set_title(f'{pretty} injection and observed amplitude spectra')
        axs[1,col].set_title(f'Observed after scaled {pretty} subtraction')
        zooms[col].set(xlabel=FREQUENCY_LABEL, ylim=(0,6),
                       title='Amplitude zoom: 0–6 cm')
        zooms[col].grid(alpha=.2)
        for name, label in [('N2','N₂'),('K2','K₂')]:
            frequency_uHz = frequencies[name]*1e6
            for axis in [axs[0,col], zooms[col]]:
                axis.axvline(frequency_uHz, color='.65', lw=.8, ls='--')
                axis.text(frequency_uHz, .97, label, transform=axis.get_xaxis_transform(),
                          va='top', ha='right', color='.35', fontsize=7,
                          bbox=dict(facecolor='white', edgecolor='none', alpha=.7, pad=.3))
        if col==0:
            zooms[col].set_ylabel(HEIGHT_LABEL)
        axs[1,col].set_xlabel(COMPENSATION_LABEL)
        axs[1,col].axvline(1, color='.7', lw=.8)
        for row in range(2):
            axs[row,col].grid(alpha=.2)
            axs[row,col].legend(fontsize=7)
            axs[row,col].text(-.12, 1.05, 'abcd'[row*2+col], transform=axs[row,col].transAxes,
                             fontweight='bold', fontsize=12)
    for row in range(2):
        for ax in axs[row]:
            ax.set_yscale('linear')
            ax.set_ylim(0, rowmax[row]*1.05)
        axs[row,0].set_ylabel(HEIGHT_LABEL)
    stem = out/'ED_Figure_10'
    for ext in ['pdf','png','svg']:
        fig.savefig(stem.with_suffix('.'+ext), dpi=220)
    plt.close(fig)
    np.savez(out/'ED_Figure_10_plotted_arrays.npz', **plotted)
    alias.to_csv(out/'ED_Figure_10_alias_amplitudes_cm.csv', index=False)
    summary = []
    for (direction, candidate), sub in alias.groupby(['direction', 'candidate'], sort=True):
        zero = sub.loc[np.isclose(sub.lambda_, 0)]
        one = sub.loc[np.isclose(sub.lambda_, 1)]
        assert len(zero)==1 and len(one)==1
        b0 = zero[['cos', 'sin']].to_numpy()[0]
        b1 = one[['cos', 'sin']].to_numpy()[0]
        bd = b0-b1
        denominator = float(bd@bd)
        assert denominator>0
        lam_min = float((b0@bd)/denominator)
        lam_clipped = float(np.clip(lam_min, 0, 1.5))
        amplitude0 = float(np.linalg.norm(b0)*CM_PER_1E18)
        amplitude1 = float(np.linalg.norm(b1)*CM_PER_1E18)
        # Validate the existing sweep against its exact linear coefficient map.
        expected = b0-sub.lambda_.to_numpy()[:,None]*bd
        np.testing.assert_allclose(sub[['cos','sin']].to_numpy(), expected, rtol=0, atol=1e-10)
        grid = sub.loc[sub.amplitude_cm.idxmin()]
        summary.append({'direction': direction, 'candidate': int(candidate),
                        'frequency_uHz': float(sub.frequency_uHz.iloc[0]),
                        'amplitude_lambda0_cm': amplitude0, 'amplitude_lambda1_cm': amplitude1,
                        'amplitude_reduction_at_lambda1_percent': 100*(1-amplitude1/amplitude0),
                        'amplitude_min_lambda_unrestricted': lam_min,
                        'amplitude_min_lambda_clipped_0_to_1p5': lam_clipped,
                        'amplitude_min_unrestricted_cm': float(np.linalg.norm(b0-lam_min*bd)*CM_PER_1E18),
                        'amplitude_min_clipped_cm': float(np.linalg.norm(b0-lam_clipped*bd)*CM_PER_1E18),
                        'grid_min_lambda': float(grid.lambda_),
                        'grid_min_amplitude_cm': float(grid.amplitude_cm)})
    pd.DataFrame(summary).to_csv(out/'alias_amplitude_summary.csv', index=False)
    (out/'alias_amplitude_summary.json').write_text(json.dumps(summary, indent=2))
    metadata = {'figure': 'Extended Data Figure 10', 'amplitude_conversion': 'hypot(cos_1e18, sin_1e18) * CM_PER_1E18',
                'CM_PER_1E18': CM_PER_1E18, 'new_fitting_in_plot_script': False,
                'top_data': 'Stored coefficient-based amplitudes from frozen-input reconstruction',
                'bottom_data': 'Original stored alias-sweep cosine/sine coefficients',
                'candidate_selection_repeated': False, 'candidates': candidates,
                'axis_scale': 'linear', 'zoom_insets_cm': [0,6], 'zoom_frequency_filter': None, 'row_shared_ylim_cm': [[0,rowmax[0]*1.05],[0,rowmax[1]*1.05]],
                'sources': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in [SCAN,ALIAS,nuisance_source]},
                'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'editable_svg_text_nodes': len(ET.parse(stem.with_suffix('.svg')).findall('.//{http://www.w3.org/2000/svg}text')),
                'software': {'python': platform.python_version(), 'numpy': np.__version__,
                             'pandas': pd.__version__, 'matplotlib': matplotlib.__version__}}
    (out/'ED_Figure_10_METADATA.json').write_text(json.dumps(metadata, indent=2))
    print(json.dumps({'figure': 'ED10', 'output': str(stem), 'row_shared_ylim_cm': metadata['row_shared_ylim_cm']}))

if __name__ == '__main__':
    main()
