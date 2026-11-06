# Reproduce v80 Figure 4 and manuscript

Use the analysis Python environment listed in requirements_analysis.txt, with OPENBLAS_NUM_THREADS=1. The frozen derived observations are unchanged from the v79 review copy.

```bash
python scripts/period_estimates.py
python scripts/draw_periods.py
python scripts/revise_v80.py
python scripts/assemble_candidate.py
python render_candidate.py NATURE_ARTICLE_A_v80.md render_replayed
```

The renderer requires pandoc, XeLaTeX and python-docx. Use a new output directory for each render. Figure 4 uses only period_estimates/period_estimates.csv; other figures are preserved from v79. The two semidiurnal coefficients are fitted jointly with the auxiliary diurnal group within each period. No period-deletion estimate is plotted. The day-deletion replicates estimate the uncertainty within a period and are retained as source data.

Historical v79 manuscript material is under baseline_v79; earlier provenance stays explicitly labelled. The new primary entry point is NATURE_ARTICLE_A_v80.md. No author/submission approval is inferred from successful code or PDF checks.
