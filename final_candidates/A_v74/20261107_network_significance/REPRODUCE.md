# A_v74 reproduction and scope

A_v74 is an editorial revision of A_v72 with a separately sourced literature extension. The selected model, accepted observations, weights, error rule and all six figure files are unchanged. This round checked exact file identity and claims against frozen results; it did not refit observations, regenerate simulations or change a data mask.

## Rebuild the manuscript

Use a fresh copy of this package. Python dependencies for assembly are NumPy, pandas and tabulate; rendering needs python-docx, Pandoc, XeLaTeX and the fonts DejaVu Serif/Sans. The workstation interpreter is `/home/room115/pytorch_env/bin/python`; a compatible Python interpreter can be substituted.

```bash
python -B scripts/revise_from_v72.py
python -B scripts/add_network_context.py
python -B scripts/assemble_candidate.py
python -B render_candidate.py NATURE_ARTICLE_A_v74.md render_new
```

`render_new` must not already exist. The renderer creates PDF, Word and editable LaTeX. Compile the exported LaTeX from the package root so `figures/*.pdf` resolves. The Markdown template uses citation keys; the assembler numbers references in order of first appearance and sorts each citation group numerically. The four new references have verified metadata and BibTeX in `editorial/network_research/`.

## Numerical provenance

The copied A_v72 numerical scripts are included unchanged: `recompute_candidate.py`, `check_coverage.py`, and `draw_candidate.py`. They start from archived **derived means and templates**, not an invented complete series or the original counter files. Their A_v72 execution records are retained under `verification/baseline_A_v72/`. They were not rerun for this editorial revision.

If a new numerical replay is needed, use a separate copy, create `data/`, `figures/` and `verification/`, and run those three scripts in that order before assembly. Dependencies include NumPy, SciPy, pandas, pyTMD, matplotlib, cartopy and shapely; the basemap and estimator modules are bundled. Set `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1` and `PYTHONDONTWRITEBYTECODE=1` for the recorded numerical setup. Seed 2026110617 controls conditional coverage simulations. Simulated observations never enter the measured data table.

Original counters, author-uploaded interval PDFs and previous manuscripts' PDFs are excluded from the review source archive. `INPUT_MANIFEST.json` retains the original full provenance list, including files that remain only in the controlled workstation archive. The export manifest lists exactly what is included. This distinction limits a raw-counter origin audit, not the manuscript build from the provided frozen tables.

`scripts/verify_editorial_revision.py` checks the unchanged A_v72 directory and frozen inputs on this workstation, plus claim conservation. Its absolute-origin checks intentionally require that original directory. They should not be represented as having run on a recipient's computer.

No upload or submission is part of these reproduction commands. Author declarations, data/code access and submission decisions remain with the authors.
