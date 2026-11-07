# Reproducible processed-data package / 可复现处理数据包

This package reproduces the auxiliary non-overlapping analysis and the current manuscript's scalar signal-to-noise table from frozen processed observations. It does **not** reproduce the original one-second acquisition, v29 screening/triangular filtering, or the direct-potential primary model from raw inputs.

## Run

Use Python 3.12 with NumPy, pandas and SciPy (the exact tested versions are in `requirements-tested.txt`). From any directory:

```sh
python /path/to/data_code/scripts/run_all.py
```

The entry point restricts BLAS/OpenMP/NumExpr to one thread and invokes all five scripts in order. It regenerates derived outputs and the JSON/SQLite summaries inside this package; packaged input files and `expected/` are read only. It requires no network, manuscript files, external repository or unpublished original data outside the package. Original machine paths in provenance JSON are source identifiers, not runtime dependencies.

1. `reproduce_amplitude_scan.py`: regenerate the paired sine/cosine coefficients, sinusoidal **peak** amplitudes, and nominal density diagnostic on all 12,833 frozen 5–40 µHz frequencies. The observed and fixed-unit-full-prediction-subtracted series are fitted separately with equal weights and 54 segment constants. This does not take a square root of a PSD. The saved grid includes exact astronomical frequencies. No figure rendering is required.
2. `build_results_library.py`: extract eight-constituent scan values and local maxima; reproduce complete-model projections, frozen physical phasor summaries, pair geometry and the exploratory solid/loading two-template fit including UTC-day deletion.
3. `calculate_signal_to_noise.py`: reproduce the existing weighted whole-template/group estimators and equal-weight solid/loading estimator, then propagate common white noise and observing-period noise through the same operators. The separate optimal-weight comparison is explicitly labelled; it does not replace the original estimator.
4. `constituent_snr/scripts/constituent_snr.py`: reproduce the equal-weight joint M₂/S₂/N₂/K₂ + 54-offset fit, scaled-LS and 43-UTC-day jackknife covariance; propagate each to the scalar amplitude using the local delta gradient.
5. `assemble_snr_table.py`: assemble the four manuscript targets from their own estimators. The main table uses common-white-noise and UTC-day-jackknife rows; observing-period noise is retained as supplementary information.

`run_all.py` compares every packaged expected CSV with its regenerated output and exports `RESULTS_LIBRARY.json` and `RESULTS_LIBRARY.sqlite`. `verification/VALIDATION.json` and per-step logs contain the actual execution evidence. The SQLite database contains summary tables and metadata, not bin-level observations.

## Data and estimators

- Inputs are **processed**, non-overlapping approximately 600-s clock means, not original 1-s records: 3,299 bins, 54 segments, 43 UTC days and 1,965,327 retained nominal one-second members (545.924 h).
- Fractional frequency is stored numerically in units of 10⁻¹⁸. `t_utc` is the bin-centre time; `n` is its retained nominal one-second membership; `sigma` is the stored observing-period-derived bin noise. The first time is 6 September 2025, 16:05 UTC. The effective exposure is not the 353.39-day elapsed span.
- `bins.csv`/`primary_rows.csv`, frozen templates and exact constituent frequencies are retained unchanged. Some input files are intentionally repeated in the independently runnable constituent subpackage and historical per-module manifests.
- Physical-template full/group fits use period-noise weights. The scans and joint free M₂/S₂/N₂/K₂ fits use equal weights. The exploratory complete solid/loading fit uses equal weights; full solid + full loading equals total, with no extra remainder.
- Scalar M₂/S₂ amplitude is the norm of the fitted pair; its local delta error is not an exact nonlinear amplitude confidence interval or a Gaussian detection significance. It is not a grouped-response error or a scan-maximum error.
- Common white noise assumes α=5.4×10⁻¹⁶√s and independent bin variance α²/n. Observing-period noise uses the measured α for each observing period, also as independent-bin noise; it does not mean a periodic disturbance. UTC-day deletion refits all retained parameters and allows a different empirical covariance.

## Expected main-table values (rounded)

| Ratio | M₂ | S₂ | Diurnal group | Complete ocean-loading template |
|---|---:|---:|---:|---:|
| S/R (white noise) | 7.17 | 2.78 | 1.55 | 1.17 |
| S/R (measured) | 7.02 | 1.96 | 1.08 | 0.89 |

The targets and amplitudes differ across columns and remain identified in `results/SNR_TABLE.json`. Additional observing-period propagation (7.32, 2.83, 1.59, 1.12) is saved for the Supplementary Methods.

## Primary v29 boundary / 原主分析缺口

The primary v29 route used extra transient screening, a 1,200-s triangular window at 600-s steps, approximately 544 h, and a direct-potential physical model. Its exact retained one-second mask, filtered arrays, aligned direct-potential solid/loading arrays, and the precise fit/error configuration behind the reported loading coefficient **0.89±0.55** are not available in this package. That value is explicitly `LEGACY_AUTHOR_REPORTED_NOT_REPRODUCED`; source excerpts and the source full-text hash are included without including an old full manuscript.

The separately reproducible non-overlapping complete-template loading coefficient is approximately **0.486±0.544** (UTC-day jackknife). It is labelled exploratory and does not replace or validate the original 0.89±0.55. Ratios copied from rounded legacy results are reported-value arithmetic, not primary-route reconstruction. Original v29 figures and the complete primary paper are delivered separately, outside this package.

## Provenance and contents

- `provenance/SOURCE_MANIFEST.json`: original source locations, hashes and packaging transformations.
- Per-module input manifests: hashes checked at execution.
- `expected/`: frozen reference outputs; never changed by the entry point.
- `results_library/`, `constituent_snr/results/`, `results/`: regenerated numeric outputs, operators, covariances and definitions.
- `RESULTS_LIBRARY.json` / `.sqlite`: consolidated derived summaries; CSV numeric data are also provided for direct reuse.
- `SHA256SUMS.txt`: delivery integrity inventory (excludes itself); regenerating outputs can change metadata hashes without changing numerical results.

No random simulation is used in the delivered entry point, so no random seed is required. Input processing upstream of these frozen means and full figure reproduction are outside the verified scope. No manuscript submission or external upload is performed by these scripts.
