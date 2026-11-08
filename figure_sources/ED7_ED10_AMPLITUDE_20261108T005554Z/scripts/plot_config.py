"""Shared display definitions. Change labels here, never relabel old density as amplitude."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / 'figures'
FIGURES.mkdir(exist_ok=True)
C = 299792458.0
G0 = 9.80665
CM_PER_1E18 = 100 * C**2 / G0 * 1e-18
HEIGHT_LABEL = 'Equivalent-height sinusoidal\npeak amplitude (cm)'
PHASE_LABEL = 'Phase (degrees)'
FREQUENCY_LABEL = 'Frequency (µHz)'
COMPENSATION_LABEL = 'Compensation factor λ'
CORRELATION_LABEL = 'Correlation coefficient'
LAG_CORRELATION_LABEL = 'Normalized template correlation'
RAYLEIGH_UHZ = 0.03275
GRID_UHZ = 0.002729
