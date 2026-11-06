# Frozen derived-data dictionary

`data/primary_rows.csv`: `y` is the period-relative observed fractional clock rate in units of 1e-18, before subtracting the fixed theoretical remainder. It is a derived observation, not a raw counter reading.

`data/design.npz`: `y` is already CSV.y minus `fixed`, in the same units. `three` contains columns lunar M2+N2, neighbouring S2+K2, diurnal K1+O1+P1+Q1. `fixed` is the minor theoretical remainder. Thus full-response y = NPZ.y + fixed = CSV.y; full template = sum(three) + fixed. For grouped fitting use NPZ.y directly; do not subtract fixed again.

`sigma` supplies the frozen Allan-based weights 1/sigma², in the same fractional-rate units; `seg` has 54 labels, `period` eight labels, `days` UTC day labels, and `seconds` recorded bin-centre timestamps in Unix seconds since 1970-01-01 00:00:00 UTC. No interpolation or missing-time compression is applied. CSV t_utc specifies readable UTC times. `quad` is the lunar quadrature column. Original row memberships are unchanged.

Reported standard errors take the larger of residual-scaled least squares and UTC-day jackknife. Period deletion is a separate diagnostic. Figures 1–4 and ED figures use saved source tables; Figure 3c alone uses the documented equal-weight spectral scan. All files retain v80 hashes. Original counter reconstruction is outside this revision.
