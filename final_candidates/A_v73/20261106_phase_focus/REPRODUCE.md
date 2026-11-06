# A_v73 editorial revision and reproduction

The numerical analysis is unchanged from the verified A_v72 candidate. This release changes prose, citation numbering, figure order and the arrangement of the saved spectral/amplitude panels. It adds a manuscript-reported apparatus performance coefficient, explicitly separated from the present noise weights.

Work in a fresh copy. Use the existing environment `/home/room115/pytorch_env/bin/python`; its numerical dependencies are the A_v72 dependencies. Pandoc and XeLaTeX produce PDF, editable LaTeX and Word. The following commands do not refit observations:

```bash
/home/room115/pytorch_env/bin/python -B scripts/revise_article.py
/home/room115/pytorch_env/bin/python -B scripts/assemble_candidate.py
/home/room115/pytorch_env/bin/python -B scripts/draw_candidate.py
/home/room115/pytorch_env/bin/python -B render_candidate.py NATURE_ARTICLE_A_v73.md render_reproduced
```

The output directory must be new. Compile the standalone `.tex` from the project root, where its `figures/*.pdf` paths resolve. Figure 2a uses the saved v71/A_v72 equal-weight scan, including every actual UTC time and missing interval; group amplitudes use the unchanged S54/Allan design. No synthetic values fill data gaps.

The package includes `original/manuscript_template_A_v72.md` so the structural revision can be reproduced. Original uploaded PDFs, old manuscript PDFs and downloaded publisher pages are retained locally and excluded from this clean source archive. The derived input tables needed by the included scripts remain in the package. `scripts/check_editorial_revision.py` verifies input hashes against the original local workstation paths, checks the expected formula changes and reference order, and runs the installed Academic Humanizer checker. On a different workstation, use `SOURCE_MANIFEST.json` for packaged-file integrity; original absolute paths, excluded PDFs and the installed checker need to be supplied or adjusted explicitly for the full origin check.

For a full *numerical* replay, use A_v72's documented `recompute_candidate.py`, `check_coverage.py` and numerical tests on a separate copy. No new numerical replay was needed or claimed for this editorial revision. Prior analysis results and all figure input tables are included unchanged.

`verification/EDITORIAL_INTEGRITY.json` records the preservation checks; `verification/PAGE_REVIEW.json` records final visual inspection. `editorial/HUMANIZER_CHANGE_RULES.json` and `verification/humanizer_compare.txt` document intended wording and numbering differences. The checker is a difference detector, not a scientific-claim validator.
