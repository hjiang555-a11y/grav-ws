# Nature Article A v85 — author review

[Tidal potential measured on a coastal–inland optical-clock baseline](NATURE_ARTICLE_A_v85.md)

- [PDF](NATURE_ARTICLE_A_v85.pdf)
- [Editable Word](NATURE_ARTICLE_A_v85.docx)
- [Chinese editorial record](EDITORIAL_REPORT_ZH.md)
- [Suggestions for frozen text](FROZEN_TEXT_SUGGESTIONS_ZH.md)
- [Verification scope](ECC_VERIFICATION_REPORT.md)
- [Editable source package](NATURE_ARTICLE_A_v85_SOURCE.zip)

The agreed Abstract, Introduction and latest Results 1 are preserved. The remaining sections use previously reported results. This edition changes Figure 3c to logarithmic density axes and places the same-data reference-level comparison in Methods. It does not rerun fits, simulations or experimental-data validation.

The source package renders the document using its included figure files. From its root, run:

```sh
python render_candidate.py NATURE_ARTICLE_A_v85.md render_new
```

Dependencies: Python with python-docx, Pandoc, XeLaTeX and DejaVu fonts. The output directory must be new. The figure-drawing script separately reads prior derived plotting outputs in the original workstation; those experimental outputs are not bundled in this editorial package.

Author names, declarations and data/code access remain for author confirmation. No journal submission is made.
