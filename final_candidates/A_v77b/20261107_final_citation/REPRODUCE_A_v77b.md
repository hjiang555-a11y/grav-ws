# Rebuild A_v77b

A_v77b only moves one existing citation sentence to the end of the Discussion. Frozen data and all results are identical to A_v77. From a fresh source extraction, using the recorded Python environment, Pandoc and XeLaTeX:

```bash
python -B scripts/edit_v77b.py
python -B scripts/draw_candidate.py
python -B scripts/assemble_candidate.py
python -B scripts/export_nature_assets.py
python -B render_candidate.py NATURE_ARTICLE_A_v77b.md render_rebuilt
```

The render destination must not exist. No fit, data selection, gap filling or upload is performed. See CITATION_PLACEMENT_A_v77b_ZH.md for the exact author-directed move. The separate ocean-loading study is not incorporated in the primary manuscript.
