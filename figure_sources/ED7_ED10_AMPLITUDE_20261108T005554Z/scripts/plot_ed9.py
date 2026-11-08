#!/usr/bin/env python3
"""Draw ED9 from frozen dimensionless correlations; no fits or new statistics.

Run from any directory: python /path/to/scripts/plot_ed9.py
The saved correlation CSVs are plotted directly. Their coefficient order and
normalization are checked against the already-computed covariance metadata.
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
from plot_config import ROOT, FIGURES, CORRELATION_LABEL, LAG_CORRELATION_LABEL

DATA = ROOT / 'data' / 'frozen_coupling'
SOURCE = ROOT / 'data' / 'frozen_auxiliary' / 'results' / 'NUMERIC_RESULTS.json'
ORDER = ['M2_cos', 'M2_sin', 'S2_cos', 'S2_sin']
LABELS = ['M₂ cos', 'M₂ sin', 'S₂ cos', 'S₂ sin']

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=FIGURES)
    out = parser.parse_args().output
    out.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'pdf.fonttype': 42, 'ps.fonttype': 42,
                         'svg.fonttype': 'none'})
    results = json.loads(SOURCE.read_text())
    assert results['joint_order'] == ORDER
    inputs = [SOURCE, DATA/'projected_basis_correlations.csv',
              DATA/'template_lag_correlations.csv']
    basis_df = pd.read_csv(inputs[1], index_col=0)
    assert list(basis_df.columns) == LABELS and list(basis_df.index) == LABELS
    basis = basis_df.to_numpy()
    lags = pd.read_csv(inputs[2])
    matrices = {}
    checks = {}
    for name, key in [('scaled_LS', 'joint_scaled_LS_covariance_e36'),
                      ('UTC_day_jackknife', 'joint_UTC_day_jackknife_covariance_e36')]:
        path = DATA/f'joint_coefficient_correlation_{name}.csv'
        inputs.append(path)
        frame = pd.read_csv(path, index_col=0)
        assert list(frame.columns) == ORDER and list(frame.index) == ORDER
        matrix = frame.to_numpy()
        covariance = np.asarray(results[key], dtype=float)
        scale = np.sqrt(np.diag(covariance))
        # Consistency check only: plotted values remain the frozen CSV values.
        np.testing.assert_allclose(matrix, covariance/np.outer(scale, scale), rtol=0, atol=1e-12)
        np.testing.assert_allclose(matrix, matrix.T, rtol=0, atol=1e-12)
        np.testing.assert_allclose(np.diag(matrix), 1, rtol=0, atol=1e-12)
        assert np.max(np.abs(matrix)) <= 1+1e-12
        matrices[name] = matrix
        checks[name] = {'plotted_correlation': matrix.tolist(),
                       'matches_frozen_covariance_normalization': True}
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), constrained_layout=True)
    for ax, matrix, title in [
            (axs[0,0], basis, 'Projected design-basis correlation'),
            (axs[1,0], matrices['scaled_LS'], 'Joint coefficients: scaled least squares'),
            (axs[1,1], matrices['UTC_day_jackknife'], 'Joint coefficients: UTC-day jackknife')]:
        im = ax.imshow(matrix, vmin=-1, vmax=1, cmap='coolwarm')
        ax.set_xticks(range(4), LABELS, rotation=25)
        ax.set_yticks(range(4), LABELS)
        ax.set_title(title, fontsize=11)
        for i in range(4):
            for j in range(4):
                ax.text(j, i, f'{matrix[i,j]:.3f}', ha='center', va='center',
                        fontsize=10, color='white' if abs(matrix[i,j])>.7 else 'black')
    ax = axs[0,1]
    for direction, label in [('M2_to_S2', 'Shifted M₂ versus S₂'),
                             ('S2_to_M2', 'Shifted S₂ versus M₂')]:
        sub = lags[lags.direction.eq(direction)]
        ax.plot(sub.lag_hours, sub.normalized_template_correlation, label=label)
    ax.set(xlabel='Donor template lag (h)', ylabel=LAG_CORRELATION_LABEL,
           ylim=(-1,1), title='Fitted-template lag correlation')
    ax.axhline(0, color='.7', lw=.8)
    ax.grid(alpha=.2)
    ax.legend(fontsize=9, loc='lower left')
    for ax, letter in zip(axs.ravel(), 'abcd'):
        ax.text(-.13, 1.06, letter, transform=ax.transAxes, fontweight='bold', fontsize=13)
    fig.colorbar(im, ax=[axs[0,0], axs[1,0], axs[1,1]],
                 label=CORRELATION_LABEL, shrink=.7, pad=.025)
    fig.canvas.draw()
    tight = fig.get_tightbbox(fig.canvas.get_renderer())
    canvas_width, canvas_height = fig.get_size_inches()
    bounds = [float(tight.x0), float(tight.y0), float(tight.x1), float(tight.y1)]
    assert tight.x0 >= -1e-6 and tight.y0 >= -1e-6
    assert tight.x1 <= canvas_width+1e-6 and tight.y1 <= canvas_height+1e-6
    stem = out/'ED_Figure_9'
    for ext in ['pdf','png','svg']:
        fig.savefig(stem.with_suffix('.'+ext), dpi=220)
    plt.close(fig)
    arrays = {'projected_basis_correlation': basis,
              'joint_scaled_LS_correlation': matrices['scaled_LS'],
              'joint_UTC_day_jackknife_correlation': matrices['UTC_day_jackknife']}
    for direction in ['M2_to_S2','S2_to_M2']:
        sub = lags[lags.direction.eq(direction)]
        arrays[direction+'_lag_hours'] = sub.lag_hours.to_numpy()
        arrays[direction+'_correlation'] = sub.normalized_template_correlation.to_numpy()
    np.savez(out/'ED_Figure_9_plotted_arrays.npz', **arrays)
    metadata = {'figure': 'Extended Data Figure 9', 'dimensionless': True,
                'new_fitting': False, 'coefficient_order': ORDER,
                'all_matrices_color_limits': [-1,1], 'checks': checks,
                'tight_bbox_inches': bounds, 'canvas_inches': [float(canvas_width), float(canvas_height)],
                'tight_bbox_within_canvas': True,
                'sources': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
                'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'editable_svg_text_nodes': len(ET.parse(stem.with_suffix('.svg')).findall('.//{http://www.w3.org/2000/svg}text')),
                'software': {'python': platform.python_version(), 'numpy': np.__version__,
                             'pandas': pd.__version__, 'matplotlib': matplotlib.__version__}}
    (out/'ED_Figure_9_METADATA.json').write_text(json.dumps(metadata, indent=2))
    print(json.dumps({'figure': 'ED9', 'output': str(stem), 'new_fitting': False}))

if __name__ == '__main__':
    main()
