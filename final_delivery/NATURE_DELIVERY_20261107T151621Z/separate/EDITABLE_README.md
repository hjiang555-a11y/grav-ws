# Separate editable manuscript and Supplementary Information

The main PDF preserves pages 1-39 of the selected combined manuscript. The SI PDF
has independent pagination and contains the same seven supplementary-method sections.

Both documents are supplied in Word, Markdown and standalone LaTeX. To compile
edited LaTeX, install XeLaTeX, DejaVu Serif and DejaVu Sans, then run twice:

```sh
xelatex -no-shell-escape NATURE_ARTICLE_MAIN.tex
xelatex -no-shell-escape SUPPLEMENTARY_INFORMATION.tex
```

Run in this directory so that the preserved figures/ relative paths resolve.
The submitted source is an author-review version; consult the delivery's red
checklist for the remaining author declarations and display-item organisation.
