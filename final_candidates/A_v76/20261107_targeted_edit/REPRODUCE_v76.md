# Rebuild A_v76

This is a targeted editorial revision of A_v75. Numerical inputs and estimator outputs are frozen. The commands below do not fit observations, change a mask, fill gaps or run simulations.

In a fresh extraction of `A_v76_SOURCE.zip`:

```bash
python -B scripts/edit_v76.py
python -B scripts/draw_candidate.py
python -B scripts/assemble_candidate.py
python -B render_candidate.py NATURE_ARTICLE_A_v76.md render_new
```

`render_new` must not exist. The original v75 keyed template is included. The plotting script reads saved means, phase covariances, coefficients and spectra. Its Figure 1/ED plot filenames remain historical source names; the manuscript specifies the final display numbering. In particular, `ed_figure2` supplies Extended Data Fig. 1 (conditional scans), `ed_figure1` supplies Extended Data Fig. 2 (reference-level diagnostics), and `ed_figure3` supplies the matched monitor.

The workstation uses `/home/room115/pytorch_env/bin/python`, Pandoc and XeLaTeX; exact versions are in `verification/SOFTWARE.json`. Figure PDFs preserve vector elements and rasterize dense observation points only.

`scripts/verify_v76.py` is the local preservation checker; it requires the sibling A_v75 directory. Its PASS record is included. The source package carries the unchanged numerical programs and prior baseline validation for provenance; they were not executed in this editing round and are not needed to rebuild the manuscript. This is not a new replay from raw counters.

The source export excludes raw counters, full original/colleague manuscript PDFs, the full local Light article and credentials. SHA256 manifests identify all included files. Nothing in the build commands uploads content or submits a manuscript.
