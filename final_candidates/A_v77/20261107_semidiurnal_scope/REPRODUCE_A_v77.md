# Rebuild A_v77

This version changes positioning and presentation, preserving the A_v76 numerical data and estimator outputs. In a fresh extraction of `A_v77_SOURCE.zip`, using the recorded Python environment, Pandoc and XeLaTeX:

```bash
python -B scripts/edit_v77.py
python -B scripts/draw_candidate.py
python -B scripts/assemble_candidate.py
python -B scripts/export_nature_assets.py
python -B render_candidate.py NATURE_ARTICLE_A_v77.md render_rebuilt
```

`render_rebuilt` must not exist. These commands read frozen results and do not fit observations, change masks, fill gaps or run simulations. The original A_v76 keyed template is included. Figure source numbering is historical: `ed_figure2` supplies ED Fig. 1, `ed_figure1` ED Fig. 2, and `ed_figure3` ED Fig. 3.

The workstation uses `/home/room115/pytorch_env/bin/python`. Exact versions are in `verification/SOFTWARE.json`. `scripts/verify_v77.py` requires the original sibling A_v76 and the locally named final render directory; its local preservation result is included. Legacy numerical scripts and result provenance are included for traceability, not invoked by the editorial build.

The separate submission-assets archive contains vector main figures, Extended Data raster formats, legends and the Source Data workbook. Raw counters, colleague PDFs, full reference articles and credentials are excluded. No command above uploads or submits the paper.
