# Reproduce the v81 author-review package

Use Python and package versions in requirements_analysis.txt, set OPENBLAS_NUM_THREADS=1. Work in a fresh extraction. Existing v80 observations and figures are preserved in the delivery copy.

## Numerical checks

```
python scripts/segment_reduce.py
python scripts/period_estimates.py
python scripts/check_full_sensitivity.py
python scripts/check_weight_definition.py
```

The first command independently checks segment reduction against explicit intercept QR. The second checks eight disjoint period fits and their within-period day jackknife. The third replays the three scalar-response models in Extended Data Table 5. The fourth reconstructs every bin uncertainty from archived period coefficients and support counts. See DATA_DICTIONARY.md for y before/after the fixed remainder. These commands use frozen derived means and templates. They do not reconstruct the original counters or re-estimate alpha from raw members; the source algorithm and historical reconciliation are supplied separately.

## Figures and manuscript

```
python scripts/draw_figure1.py
python scripts/draw_segments.py figure2 figure3 extended4
python scripts/draw_periods.py
python scripts/draw_extended.py
python scripts/assemble_candidate.py
python render_candidate.py NATURE_ARTICLE_A_v81.md render_replayed
```

The renderer requires pandoc, XeLaTeX, python-docx and the listed fonts. Use a new output directory. Figure 1a embeds the exact author-supplied PNG. Its field grid and phase convention remain author provenance items; no fit uses the image. Figure 3c uses the archived equal-weight spectrum, while response estimates use the documented Allan weights. ED1/ED2 plot code is extracted from its archived version with original filenames retained (the manuscript maps ed_figure2 to ED1 and ed_figure1 to ED2). The original plot source is preserved under sources/plot_history.

The current editable manuscript is manuscript_template.md; the assembled numbered source is NATURE_ARTICLE_A_v81.md. Scripts integrate_v81.py, respond_round1.py, respond_round2.py and polish_round*.py document the editorial history and must not be rerun over the final manuscript. Historical v80/v79 sources are explicitly labelled.

Three review packets and nine mutually blind AI mock reports are archived; they are not human journal reviews or scientific approval. Author declarations, data access and related-manuscript status remain for the authors to confirm. No external submission was made.
