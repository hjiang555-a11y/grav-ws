# Reproduce the segment-based author-review candidate

This version starts from the preserved v78 draft and its verified frozen derived observations. It does not modify the original counter archive or the colleague's working tree. The latest author direction adopts a detection-led title; earlier title instructions remain documented in PLAN.md.

From the package root, with the recorded Python environment:

```bash
OPENBLAS_NUM_THREADS=1 python -B scripts/segment_reduce.py
OPENBLAS_NUM_THREADS=1 python -B scripts/full_tide_detection.py
OPENBLAS_NUM_THREADS=1 python -B scripts/draw_figure1.py
OPENBLAS_NUM_THREADS=1 python -B scripts/draw_segments.py
python -B scripts/write_manuscript.py
python -B scripts/assemble_candidate.py
python -B render_candidate.py NATURE_ARTICLE_A_v79_SEGMENT.md render_rebuilt
```

The render destination must not exist. `review_diagnostics/REVIEW_RESULTS.json` and associated tables are bound to the same frozen design by hashes; to rerun those diagnostics, use scripts/review_statistics.py and scripts/check_noise_adequacy.py before plotting. Both explicitly separate synthetic noise from observations. Frozen figure1, figure3 and original Extended Data remain verified v78 assets; the original complete numerical replay entry point is scripts/recompute_candidate.py and is optional for a fresh working copy, since it regenerates the saved derived tables. Exact raw-counter reconstruction requires the separately controlled original archive.

After assembly, scripts/prepare_review_bundle.py builds the Source Data workbook and reports. The main fit always uses original ten-minute means. Three-hour averaging is a display only. The script scripts/verify_segment_candidate.py checks numerical equivalence, observations, complete display membership, physical units and document/figure QA. All output is for author review; this script performs no upload or submission.
