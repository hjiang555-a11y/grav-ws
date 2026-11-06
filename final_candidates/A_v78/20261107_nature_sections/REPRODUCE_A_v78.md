# Rebuild the editorial A_v78 candidate

The input is the preserved A_v77b template and its frozen derived results. This package rebuilds the narrative revision and manuscript; it does not rerun a fit or raw-counter processing.

```bash
/data/AI_Research/environments/python/sci/bin/python -B scripts/edit_v78.py
/data/AI_Research/environments/python/sci/bin/python -B scripts/assemble_candidate.py
/data/AI_Research/environments/python/sci/bin/python -B render_candidate.py NATURE_ARTICLE_A_v78.md render_rebuilt
/home/room115/pytorch_env/bin/python -B scripts/verify_v78.py --render render_rebuilt
```

Run from the package root. The render destination must not already exist. Dependencies are the existing Python packages (NumPy, pandas, tabulate, python-docx; PyMuPDF/Pillow in the PDF review environment), Pandoc and XeLaTeX. No installation or external service is required for rebuilding the manuscript.

`original/BASELINE_MANIFEST.json` records the pre-edit hashes. Verification of the live baseline directory is performed only if it exists; the preserved manuscript and frozen data/figure copies are always checked. The A_v78 source archive retains the editable template, rendered Markdown, figures, frozen derived tables, citation inputs, editing and assembly code, and the editorial record. Raw counter files remain in the original research archive.
