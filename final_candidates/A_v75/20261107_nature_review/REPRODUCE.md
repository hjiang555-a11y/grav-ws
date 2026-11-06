# Rebuild A_v75

A_v75 revises the scientific framing and introductory context of A_v74. Its numerical results and all figures remain those of the A_v72 analysis. The current manuscript, figures and methods were reviewed together; no observational fit was rerun this round.

In a fresh copy of the source package:

```bash
python -B scripts/revise_for_nature.py
python -B scripts/assemble_candidate.py
python -B render_candidate.py NATURE_ARTICLE_A_v75.md render_new
```

The new render directory must not already exist. The saved A_v74 keyed template is the input to the revision script. Pandoc, XeLaTeX, DejaVu Serif/Sans, python-docx, pandas, numpy and tabulate are used. The workstation Python is `/home/room115/pytorch_env/bin/python`; exact versions are recorded in `verification/SOFTWARE.json`.

The archive also retains the unchanged numerical scripts and frozen derived means/templates. Their prior execution records and simulation settings are in `verification/baseline_A_v72/`. For a separately authorized numerical replay use another fresh copy, with `recompute_candidate.py`, `check_coverage.py` and `draw_candidate.py` in that order before manuscript assembly. This is a replay from derived inputs, not a replacement for original-counter provenance review. No observation is invented to fill a gap.

`scripts/verify_nature_revision.py` uses the original workstation directories for preservation checks. Its result is supplied as a record; it is not portable without those originals. Manuscript assembly is portable within the exported package. The current guide supersedes the inherited A_v74 guide.

Source export excludes original counters and author-uploaded/previous manuscript PDFs. The complete input manifest retains their provenance in the controlled archive. The export manifest gives the exact included files and hashes. No reproduction command uploads files or submits a manuscript.
