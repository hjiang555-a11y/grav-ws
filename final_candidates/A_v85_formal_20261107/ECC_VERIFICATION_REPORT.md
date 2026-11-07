# ECC verification — editorial scope

Status: **READY FOR AUTHOR REVIEW**, not cleared for journal submission.

| Check | Result | Evidence / scope |
|---|---|---|
| PDF and Word build | PASS | Pandoc/XeLaTeX and DOCX returned zero; no final warnings (`render_v4/BUILD_RESULTS.json`). |
| Frozen sections | PASS | Abstract, Introduction, latest Results 1 and Fig. 1 caption appear verbatim; original input hashes unchanged (`FREEZE_MANIFEST.json`). |
| References and displays | PASS | First citations and lists run 1–28; four main figures, four Extended Data figures and five tables; resource files present. |
| Citation policy | PASS | Published Yb and Light entries retained; no Hou reference; Stahl mentioned only in the final Discussion sentence and its reference entry. |
| Figure change | PASS, display only | Fig. 3c uses logarithmic density axes. Stored plotting outputs reused. Other seven figure assets match previous files byte for byte. |
| Visual review | PASS | All 35 final PDF pages viewed through contact sheets; Figure 3 additionally inspected at image resolution. Abstract fits on page 1; legends remain with figures; no visible clipping or missing panels. |
| Academic-humanizer | REVIEWED | New Results, Discussion and reference-level Methods audited. Flagged generic wording and punctuation revised where useful; ordinary scientific terms retained. Frozen prose was not polished. |
| Experimental analysis / tests | NOT PERFORMED | No fits, simulations, counter-data processing or experimental-result correctness checks were authorized or run. Historical results are reproduced as reported. |
| Software types / coverage | NOT APPLICABLE | This is a document edition. No numerical pipeline was changed. |
| Author and access statements | PENDING AUTHOR | Names, contributions, funding, conflicts, actual AI use and reviewer data/code access remain explicit placeholders. |

The ECC verification-loop was adapted to document build, text integrity, cross-references, display provenance and visual checks. It does not certify the scientific correctness of inherited results. The Methods descriptions of earlier numerical replay and simulations are not new computations in this revision.

Skills used: ECC article-writing and verification-loop, Nature writing guidance, academic-humanizer and PDF review.
